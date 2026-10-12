# Experiment comparison

| metric | text_edc | decomp_edc | decomp_edc_ec | decomp_edc_ec_g |
|---|---|---|---|---|
| model | Qwen/Qwen3-14B-AWQ | Qwen/Qwen3-14B-AWQ | None | None |
| input | text | sentences | decomp_edc | decomp_edc |
| n_chunks | 854 | 911 | 911 | 911 |
| open_triplets | 12113 | 13180 | 13180 | 13180 |
| final_triplets | 12113 | 13180 | 13180 | 13180 |
| extract_seconds | 1492 | 1559 | 1559 | 1559 |
| status_mapped | 2468 | 2657 | 2657 | 2657 |
| status_direct | 9426 | 10241 | 10241 | 10241 |
| status_enriched | 166 | 239 | 239 | 239 |
| status_mapped_new | 41 | 32 | 32 | 32 |
| status_auto | 12 | 11 | 11 | 11 |
| kg_entities | 7529 | 8466 | 8466 | 8466 |
| kg_triples | 12233 | 13198 | 13198 | 13198 |
| kg_relations | 149 | 210 | 210 | 210 |
| kg_relations_enriched | 109 | 170 | 170 | 170 |
| audit_entities_with_issue | 4323 | 4984 | 4984 | 4984 |
| audit_dup_groups | 237 | 235 | 235 | 235 |
| audit_sentence_like_concepts | 685 | 781 | 781 | 781 |
| audit_composite | 606 | 636 | 636 | 636 |
| audit_alias_split | 43 | 45 | 45 | 45 |
| audit_type_mismatch_entities | 267 | 361 | 361 | 361 |
| audit_boilerplate_hubs | 12 | 14 | 14 | 14 |
| canon_entities |  |  | 5064 | 5669 |
| canon_triples |  |  | 11940 | 11746 |
| canon_relations |  |  | 143 | 130 |
| canon_lm_calls |  |  | 5471 | 6019 |
| canon_entities_after_semhash |  |  | 7844 | 8037 |
| audit_canon_entities_with_issue |  |  | 3392 | 3527 |
| audit_canon_dup_groups |  |  | 53 | 68 |
| audit_canon_sentence_like_concepts |  |  | 463 | 523 |
| audit_canon_composite |  |  | 294 | 366 |
| audit_canon_alias_split |  |  | 34 | None |
| audit_canon_type_mismatch_entities |  |  | 1136 | 1001 |
| audit_canon_boilerplate_hubs |  |  | 26 | 20 |

Stage seconds: {"text_edc": {"prepare": 0.0, "extract": 1507.7, "consolidate": 49.6, "export": 12.2, "audit": 0.7}, "decomp_edc": {"prepare": 0.2, "extract": 1582.0, "consolidate": 70.2, "export": 12.5, "audit": 0.7}, "decomp_edc_ec": {"copy_from": 0, "export": 21.5, "canon_entities": 528.6, "audit": 1.4}, "decomp_edc_ec_g": {"copy_from": 0, "export": 22.5, "canon_entities": 852.1, "audit": 1.3}}