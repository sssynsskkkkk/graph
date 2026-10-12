# Relation redundancy (cosine similarity of relation definitions, bge-base-en-v1.5)

| KG | relations | mean nearest-neighbour sim | pairs ≥0.85 | pairs ≥0.90 | relations with a neighbour ≥0.85 | share of triples under those relations | seed-only mean nearest | seed-only pairs ≥0.85 |
|---|---|---|---|---|---|---|---|---|
| main (4B) | 147 | 0.840 | 187 | 13 | 66 | 93% | 0.887 | 81 |
| decomp_edc | 210 | 0.881 | 934 | 77 | 162 | 98% | 0.887 | 81 |
| decomp_edc_ec (canon) | 143 | 0.869 | 425 | 34 | 98 | 97% | 0.887 | 42 |
| decomp_edc_ec_g (canon) | 130 | 0.866 | 361 | 17 | 91 | 90% | 0.867 | 30 |
| text_edc | 149 | 0.878 | 562 | 44 | 115 | 97% | 0.887 | 81 |

## main (4B): most similar relation pairs

| relation A | relation B | cosine | origins |
|---|---|---|---|
| has brand name | manufactured by | 0.941 | seed/seed |
| has brand name | distributed from | 0.930 | seed/enriched |
| has side effect | has side effect variation | 0.927 | seed/enriched |
| manufactured by | distributed from | 0.926 | seed/enriched |
| has side effect | has serious side effect | 0.925 | seed/seed |
| has dosage form | has recommended dose | 0.921 | seed/seed |
| has dosage form | has strength | 0.916 | seed/seed |
| contains ingredient | has inactive ingredient | 0.915 | seed/enriched |
| has generic name | has brand name | 0.915 | seed/seed |
| treats | reduces risk of | 0.914 | seed/seed |
| has duration of treatment | has half life | 0.907 | seed/enriched |
| has side effect | has overdose symptom | 0.904 | seed/seed |

## decomp_edc: most similar relation pairs

| relation A | relation B | cosine | origins |
|---|---|---|---|
| no dose change needed in | no dose adjustment needed with | 0.963 | enriched/enriched |
| improves | increases response to | 0.952 | enriched/enriched |
| has dosage form | has formulation | 0.946 | seed/enriched |
| has duration in system | has increased duration in | 0.944 | enriched/enriched |
| treats | applies to patients who are to be managed with | 0.943 | seed/enriched |
| has brand name | manufactured by | 0.941 | seed/seed |
| does not contain | not chemically related to | 0.941 | enriched/enriched |
| is defined as | can be | 0.940 | enriched/enriched |
| has side effect | has side effect frequency | 0.938 | seed/enriched |
| has dosage form | available dose count | 0.936 | seed/enriched |
| treats | used after | 0.933 | seed/enriched |
| treats | has use indication | 0.931 | seed/enriched |

## decomp_edc_ec (canon): most similar relation pairs

| relation A | relation B | cosine | origins |
|---|---|---|---|
| has dosage form | has formulation | 0.946 | seed/enriched |
| has brand name | manufactured by | 0.941 | seed/seed |
| does not contain | not chemically related to | 0.941 | enriched/enriched |
| has dosage form | available dose count | 0.936 | seed/enriched |
| treats | used after | 0.933 | seed/enriched |
| tested in | compared with | 0.929 | enriched/enriched |
| has strength | available dose count | 0.925 | seed/enriched |
| has dosage form | has recommended dose | 0.921 | seed/seed |
| has absorption characteristic | described as | 0.921 | enriched/enriched |
| causes | used after | 0.921 | enriched/enriched |
| has side effect | causes | 0.919 | seed/enriched |
| has related treatment guide | used after | 0.917 | enriched/enriched |

## decomp_edc_ec_g (canon): most similar relation pairs

| relation A | relation B | cosine | origins |
|---|---|---|---|
| is defined as | can be | 0.940 | enriched/enriched |
| treats | used after | 0.933 | seed/enriched |
| has strength | available dose count | 0.925 | seed/enriched |
| causes | used after | 0.921 | enriched/enriched |
| has related treatment guide | used after | 0.917 | enriched/enriched |
| interacts with | causes | 0.913 | seed/enriched |
| similar to | should be replaced with | 0.911 | seed/enriched |
| has absorption characteristic | has metabolism characteristic | 0.909 | enriched/enriched |
| available dose count | has dose | 0.909 | enriched/kggen-alias |
| reduces | reduces effectiveness of | 0.906 | enriched/enriched |
| contraindicated in | should be avoided during | 0.903 | seed/enriched |
| has effect in | has sertraline level | 0.903 | enriched/enriched |

## text_edc: most similar relation pairs

| relation A | relation B | cosine | origins |
|---|---|---|---|
| has brand name | manufactured by | 0.941 | seed/seed |
| has side effect | has side effect frequency | 0.938 | seed/enriched |
| may cost | cost condition | 0.937 | enriched/enriched |
| not chemically related to | does not interact with | 0.934 | enriched/enriched |
| used in | used after | 0.930 | enriched/enriched |
| has mechanism of action | has effect | 0.929 | seed/enriched |
| treats | used in | 0.927 | seed/enriched |
| used in | may be used for | 0.926 | enriched/enriched |
| used in | has recommendation | 0.925 | enriched/enriched |
| has side effect | has serious side effect | 0.925 | seed/seed |
| treats | may be used for | 0.925 | seed/enriched |
| has dosage form | has concentration | 0.924 | seed/enriched |