#!/usr/bin/env python3
"""Reproduce the CoDe-KG BERT-Large sentence classifier experiment.

Uses all 2,000 released training examples (no validation split), then evaluates
once on the released 5,269-example test set. Saves model, metrics, confusion
matrix, and per-example predictions.
"""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    DataCollatorWithPadding,
    Trainer,
    TrainingArguments,
)


LABELS = [
    "Simple Sentence",
    "Compound Sentence",
    "Complex Sentence",
    "Compound-Complex Sentence",
    "Incomplete Sentence",
]
LABEL2ID = {label: idx for idx, label in enumerate(LABELS)}
ID2LABEL = {idx: label for label, idx in LABEL2ID.items()}


class SentenceDataset(torch.utils.data.Dataset):
    def __init__(self, frame: pd.DataFrame, tokenizer, max_length: int):
        self.sentences = frame["Sentence"].astype(str).tolist()
        self.labels = [LABEL2ID[label] for label in frame["label"].astype(str)]
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.sentences)

    def __getitem__(self, index):
        item = self.tokenizer(
            self.sentences[index],
            truncation=True,
            max_length=self.max_length,
        )
        item["labels"] = self.labels[index]
        return item


def read_csv(path: Path) -> pd.DataFrame:
    for encoding in ("utf-8", "utf-8-sig", "latin-1"):
        try:
            frame = pd.read_csv(path, encoding=encoding)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise UnicodeError(f"Unable to decode {path}")
    required = {"PMID", "Sentence", "label"}
    if not required.issubset(frame.columns):
        raise ValueError(f"{path} must contain {sorted(required)}; got {list(frame.columns)}")
    unknown = sorted(set(frame["label"]) - set(LABEL2ID))
    if unknown:
        raise ValueError(f"Unknown labels in {path}: {unknown}")
    return frame


def classification_metrics(gold: np.ndarray, pred: np.ndarray) -> dict:
    confusion = np.zeros((len(LABELS), len(LABELS)), dtype=np.int64)
    for target, output in zip(gold, pred):
        confusion[int(target), int(output)] += 1

    per_class = {}
    f1_values = []
    for idx, label in enumerate(LABELS):
        tp = int(confusion[idx, idx])
        fp = int(confusion[:, idx].sum() - tp)
        fn = int(confusion[idx, :].sum() - tp)
        support = int(confusion[idx, :].sum())
        precision = tp / (tp + fp) if tp + fp else 0.0
        recall = tp / (tp + fn) if tp + fn else 0.0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
        f1_values.append(f1)
        per_class[label] = {
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "support": support,
        }
    return {
        "accuracy": float((gold == pred).mean()),
        "macro_f1": float(np.mean(f1_values)),
        "per_class": per_class,
        "confusion_matrix": confusion.tolist(),
        "confusion_matrix_labels": LABELS,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    base = Path("external/CoDe-KG_EMNLP_2025/datasets/Sentence_Classifier_Dataset")
    parser.add_argument("--train-csv", type=Path, default=base / "train.csv")
    parser.add_argument("--test-csv", type=Path, default=base / "test.csv")
    parser.add_argument("--output-dir", type=Path, default=Path("models/codekg_bert_large"))
    parser.add_argument("--model-name", default="bert-large-uncased")
    parser.add_argument("--epochs", type=float, default=3.0)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--learning-rate", type=float, default=2e-5)
    parser.add_argument("--max-length", type=int, default=512)
    parser.add_argument("--seed", type=int, default=4000)
    args = parser.parse_args()

    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)

    train_frame = read_csv(args.train_csv)
    test_frame = read_csv(args.test_csv)
    print(f"train={len(train_frame)} test={len(test_frame)} validation=0", flush=True)
    print(f"cuda={torch.cuda.is_available()} gpu_count={torch.cuda.device_count()}", flush=True)
    if torch.cuda.is_available():
        print("gpus=" + repr([torch.cuda.get_device_name(i) for i in range(torch.cuda.device_count())]), flush=True)

    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    model = AutoModelForSequenceClassification.from_pretrained(
        args.model_name,
        num_labels=len(LABELS),
        label2id=LABEL2ID,
        id2label=ID2LABEL,
    )
    train_dataset = SentenceDataset(train_frame, tokenizer, args.max_length)
    test_dataset = SentenceDataset(test_frame, tokenizer, args.max_length)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    training_args = TrainingArguments(
        output_dir=str(args.output_dir),
        overwrite_output_dir=True,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size * 2,
        learning_rate=args.learning_rate,
        weight_decay=0.0,
        warmup_ratio=0.0,
        logging_steps=25,
        save_strategy="epoch",
        save_total_limit=1,
        evaluation_strategy="no",
        fp16=torch.cuda.is_available(),
        seed=args.seed,
        data_seed=args.seed,
        report_to=[],
    )
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        tokenizer=tokenizer,
        data_collator=DataCollatorWithPadding(tokenizer=tokenizer),
    )
    train_result = trainer.train()
    trainer.save_model(str(args.output_dir / "final_model"))
    tokenizer.save_pretrained(str(args.output_dir / "final_model"))

    prediction = trainer.predict(test_dataset)
    predicted_ids = np.argmax(prediction.predictions, axis=1)
    gold_ids = np.asarray(test_dataset.labels)
    metrics = classification_metrics(gold_ids, predicted_ids)
    metrics.update({
        "model_name": args.model_name,
        "seed": args.seed,
        "epochs": args.epochs,
        "learning_rate": args.learning_rate,
        "per_device_batch_size": args.batch_size,
        "train_examples": len(train_frame),
        "validation_examples": 0,
        "test_examples": len(test_frame),
        "train_runtime": train_result.metrics,
    })
    (args.output_dir / "test_metrics.json").write_text(
        json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    output = test_frame.copy()
    output["predicted_label"] = [ID2LABEL[int(idx)] for idx in predicted_ids]
    output["correct"] = output["label"] == output["predicted_label"]
    output.to_csv(args.output_dir / "test_predictions.csv", index=False)

    print(json.dumps({"accuracy": metrics["accuracy"], "macro_f1": metrics["macro_f1"]}, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
