# KGGen relation-cluster audit (which relations were merged, and why it is an over-merge)

Summary: {"decomp_edc_ec": {"clusters": 25, "relations_merged": 92, "triples_relabelled": 4194, "clusters_with_negation_mix": 4, "clusters_collapsing_seed_relations": 4, "clusters_with_multiple_type_signatures": 20}, "decomp_edc_ec_g": {"clusters": 24, "relations_merged": 104, "triples_relabelled": 5073, "clusters_with_negation_mix": 3, "clusters_collapsing_seed_relations": 7, "clusters_with_multiple_type_signatures": 19}}

## decomp_edc_ec

| representative | merged relations | triples affected | flags |
|---|---|---|---|
| has side effect | has overdose symptom, has serious side effect, has side effect, has side effect frequency, has symptom, has withdrawal symptom | 1178 | 3 type signatures; 3 seed relations collapsed |
| used in combination with | interacts with, must be used in combination with, resolves with, should discuss risks and benefits with, use with caution in, use with caution with, used in combination with, used in population | 1430 | 8 type signatures; 4 seed relations collapsed |
| compared with | compared with, differs from, more common in, similar to | 541 | 3 type signatures |
| has warning | has boxed warning, has pregnancy or breastfeeding warning, has warning | 97 | 3 seed relations collapsed |
| treats | are being treated with, treats | 2 | 2 type signatures |
| includes | includes, may include | 7 | 2 type signatures |
| has benefit | has benefit, has effect in, has mechanism of action, has use indication, helps control | 244 | 4 type signatures |
| reduces risk of | has increased risk in, has no identified risk of, has overdose risk, has risk magnitude, higher risk in, increases level of, lowers level of, reduces, reduces risk of | 167 | negation mixed; 6 type signatures; 3 seed relations collapsed |
| should be avoided with | interferes with, not substitute for, should be avoided during, should be avoided with, should be made with, should be replaced with, should not be taken with | 41 | negation mixed; 6 type signatures |
| causes | can worsen, caused by, causes, worsens | 30 | direction/inverse; 3 type signatures |
| increases | can lead to, has increased duration in, improves, increases, increases response to | 92 | 5 type signatures |
| requires reporting to | applies to patients who are to be managed with, requires medical attention, requires monitoring of, requires reporting to | 101 | 4 type signatures |
| not used for | not approved for, not used for | 67 | 2 type signatures |
| described as | described as, has definition, is defined as | 67 | 3 type signatures |
| has availability | has availability, has availability date | 2 | - |
| administered via | administered via, not administered via | 2 | negation mixed |
| has duration in system | has duration in system, has duration of treatment, has effect duration | 28 | 3 type signatures |
| has effect on clearance | depend on, does not act on, has effect on clearance, has limited data on, has no harmful effects on, has rules on | 41 | negation mixed; 5 type signatures |
| is | is, is for | 4 | 2 type signatures |
| not chemically related to | is not, not chemically related to | 20 | - |
| have | have, may have added | 7 | 2 type signatures |
| no dose adjustment needed with | no dose adjustment needed with, no dose change needed in | 4 | 2 type signatures |
| used off label to improve symptoms of | may be used for, used off label to improve symptoms of | 10 | - |
| has reason | discontinued due to, has discontinuation reason, has reason | 6 | 3 type signatures |
| has been approved by | has been approved by, has fda statement | 6 | direction/inverse; 2 type signatures |

## decomp_edc_ec_g

| representative | merged relations | triples affected | flags |
|---|---|---|---|
| has symptom | has overdose symptom, has serious side effect, has side effect, has side effect frequency, has symptom, has withdrawal symptom | 2595 | 3 type signatures; 3 seed relations collapsed |
| has administration instruction | has administration instruction, has administration pattern | 4 | - |
| interacts with | applies to patients who are to be managed with, can be differentiated from, compared with, differs from, interacts with, interferes with, should be avoided with, should be made with, should not be taken with | 169 | negation mixed; 5 type signatures; 2 seed relations collapsed |
| has dose | has dose adjustment instruction, has dose classification, has dose increase instruction, has estimated dose in breastfed baby, has maximum dose, has missed dose consequence, has missed dose instruction, has recommended dose | 666 | 3 type signatures; 2 seed relations collapsed |
| has function | has availability, has brand name, has composition, has dosage form, has formulation, has function, has generic name, has multiple brands and forms, has note, has participant, has reason, has related question, has uncertainty, has usage instruction, have | 651 | 11 type signatures; 4 seed relations collapsed |
| has warning | has boxed warning, has pregnancy or breastfeeding warning, has warning | 97 | 3 seed relations collapsed |
| treats | are being treated with, treats | 2 | 2 type signatures |
| use with caution in | use with caution in, use with caution with | 8 | 2 type signatures |
| includes | includes, may include | 7 | 2 type signatures |
| has effect in | has benefit, has effect in, has mechanism of action, has onset of effect, has use indication, helps control | 299 | 5 type signatures; 2 seed relations collapsed |
| higher risk in | has duration in system, has duration of treatment, has effect duration, has increased duration in, has increased risk in, has no identified risk of, has overdose risk, has risk magnitude, higher risk in, increases level of, increases risk of, more common in | 236 | negation mixed; 9 type signatures; 3 seed relations collapsed |
| reduces | reduces, reduces risk of | 76 | - |
| not used for | does not contain, is not, not approved for, not chemically related to, not substitute for, not used for | 100 | 5 type signatures |
| increases | can lead to, improves, increases, increases response to | 90 | 4 type signatures |
| causes | can worsen, causes, worsens | 6 | 2 type signatures |
| is defined as | described as, has definition, is defined as | 14 | 3 type signatures |
| used in combination with | must be used in combination with, used alone or in combination with, used in combination with | 15 | 2 type signatures |
| administered via | administered via, not administered via | 2 | negation mixed |
| is | for breakdown by, has consideration for, is, is for | 9 | direction/inverse; 4 type signatures |
| no dose adjustment needed with | no dose adjustment needed with, no dose change needed in | 4 | 2 type signatures |
| may be used for | may be used for, used off label to improve symptoms of | 5 | - |
| has no harmful effects on | has no harmful effects on, has no interaction with | 9 | 2 type signatures |
| has been approved by | has been approved by, has fda statement | 6 | direction/inverse; 2 type signatures |
| has discontinuation reason | discontinued due to, has discontinuation reason | 3 | 2 type signatures |
