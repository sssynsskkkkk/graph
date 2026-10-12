# Why pronoun resolution + sentence decomposition did not improve the KG

## One-line conclusion
**Preprocessing does not add information; it only changes how the text is expressed. EDC was already handling those expression issues on its own, and the real bottleneck lies in a different stage.**

---

### Reason 1. The data had few of the problems the method fixes
CoDe-KG was designed for **scientific abstracts**, which are full of pronouns and long complex sentences. Consumer drug pages on Drugs.com are mostly short sentences, lists and imperatives to begin with.

| What preprocessing actually changed | Share |
|---|---|
| Sentences decomposed (complex/compound) | 1,916 of 8,028 (24%) |
| Simple sentences left unchanged | 2,210 (28%) |
| Incomplete sentences (list items, imperatives) left unchanged | 3,902 (49%) |
| Sentences changed by pronoun resolution | 923 (11%) |

→ Preprocessing left three quarters of all sentences untouched. Even if it helped where it applied, the effect is diluted in the overall result.

**Slide message**: "We applied a fixing tool to data with little to fix."

### Reason 2. EDC was already doing the same job
The EDC extraction prompt already says:
> Expressions such as "this medicine", "this medication", "this drug" or "it" refer to {drug}; always use "{drug}" as the entity name for the drug itself.

The same prompt also instructs: "Extract every fact stated in the text."

- **Pronoun resolution**: the prompt supplies the drug name and section heading and tells the model how to treat pronouns, so the 14B model resolves them itself within the 1,100-character context.
- **Sentence decomposition**: an LLM extracts several triples from a single complex sentence. There is no need to split it beforehand.

CoDe-KG was motivated by small models and sentence-level extraction struggling with complex sentences. EDC, with context-rich chunks and a specific prompt, had already largely solved that problem.

**Slide message**: "We repeated, upstream, work the extractor already does."

### Reason 3. Errors arise in relation selection, not in the input
The incorrect triples in both KGs share the same causes.
- 74–84% of incorrect triples are "the relation misrepresents the text".
- More than two thirds of those come from a single relation, `has administration instruction`, e.g. classifying "call your doctor if a side effect occurs" as a way of taking the drug.
- Most of the ~40% partially correct triples lost a qualifier such as population or formulation.

These errors occur whether sentences are long or short, with or without pronouns. They are **problems of the schema and relation canonicalization**, so polishing the input does not fix them.

**Slide message**: "We improved a stage that was not the bottleneck."

### Reason 4. Splitting loses as much as it gains
Decomposition simplifies sentences, but it also cuts the links between them.
- Conditions and reasons ("if …", "because …") are split into separate sentences.
- List headers such as "Tell your doctor if you have:" are separated from their items.

As a result, EDC failed to map to existing relations more often and **created more new relations**: the share of triples using a new relation rose from 11.4% (baseline EDC) to 18.6% (e.g. `includes`, `may cause weight regain after discontinuation`), and relation types grew from 149 to 201. What was gained by simplifying was offset by what was lost in context.

**Slide message**: "What we gained in simplicity, we lost in context."

### Reason 5. Each added stage adds its own errors
Pronoun resolution and decomposition are LLM tasks too, and they can be wrong.
- In a random check of 30 pronoun replacements, about 3 were wrong, e.g. an "it" referring to a dog replaced with `Prozac`.
- In the precision sample, **triples from sentences changed by pronoun resolution had a 17–21% error rate, versus 12% for unchanged sentences.** That subsample has only 48 triples, so treat it as indicative only.

Every added stage passes its errors straight on to the next one.

**Slide message**: "A longer pipeline propagates more errors."

---

## Closing message (suggested)
> The benefit of preprocessing depends on **the nature of the data** and **the capability of the extractor**. When sentences are already simple and the LLM can handle pronouns and complex sentences within context, preprocessing adds no information. To improve quality, we need to improve the **relation schema and canonicalization**, where the errors actually occur.

## Notes for presenting
- Reasons 1, 2 and 3 are backed directly by data and code.
- Reason 4 is supported by the rise in new relations, but attributing it to lost context is an interpretation.
- Reason 5 rests on a small sample; present it as a tendency only.
- It is worth stating in one line that all results come from AI judgments without human review.
