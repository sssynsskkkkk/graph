# Per-drug quality of EDC triples

EDC-extracted triples only (structured metadata excluded). centric = subject is the drug itself; seed = seed-schema relation; conform = subject/object types match the relation's domain/range; clean = object is a short concept (<= 6 words, not a clause); quality = mean of the four. Automatic proxies, not precision.

## Overall (mean over drugs; n = total triples)

| metric | text_edc | decomp_edc | coref_decomp_edc |
|---|---|---|---|
| n | 11,385 | 12,512 | 12,533 |
| centric | 89.4 | 81.7 | 81.0 |
| seed | 90.4 | 81.6 | 80.9 |
| conform | 89.9 | 88.1 | 85.4 |
| clean | 70.4 | 68.3 | 68.6 |
| enriched_rels | 9.3 | 16.2 | 16.8 |
| quality | 85.0 | 79.9 | 79.0 |

## Per drug (sorted by coref_decomp_edc quality; Δ = coref_decomp_edc − text_edc)

| drug | text_edc n / quality | decomp_edc n / quality | coref_decomp_edc n / quality | Δ quality |
|---|---|---|---|---|
| mtm/ergocalciferol | 102 / 90.1 | 115 / 87.6 | 114 / 87.7 | -2.4 |
| clopidogrel | 153 / 88.6 | 139 / 86.9 | 138 / 86.2 | -2.4 |
| allopurinol | 136 / 88.9 | 157 / 85.9 | 156 / 84.7 | -4.1 |
| hydrocodone-acetaminophen | 170 / 86.4 | 190 / 84.9 | 199 / 84.7 | -1.6 |
| cetirizine | 96 / 87.6 | 118 / 84.4 | 114 / 84.0 | -3.6 |
| hydrochlorothiazide | 339 / 85.6 | 348 / 86.9 | 358 / 83.6 | -2.0 |
| furosemide | 233 / 85.8 | 283 / 83.6 | 278 / 83.4 | -2.4 |
| carvedilol | 139 / 89.2 | 141 / 84.4 | 136 / 83.4 | -5.8 |
| adderall | 280 / 87.2 | 304 / 85.0 | 323 / 82.8 | -4.3 |
| spironolactone | 422 / 85.2 | 449 / 81.5 | 464 / 82.6 | -2.6 |
| tamsulosin | 148 / 86.0 | 197 / 85.6 | 188 / 82.5 | -3.5 |
| amlodipine | 125 / 82.4 | 150 / 82.2 | 141 / 82.0 | -0.3 |
| levothyroxine | 344 / 85.1 | 383 / 83.2 | 388 / 81.9 | -3.3 |
| apixaban | 136 / 88.1 | 158 / 82.5 | 161 / 81.8 | -6.3 |
| simvastatin | 149 / 92.1 | 186 / 81.6 | 185 / 81.7 | -10.4 |
| atorvastatin | 247 / 86.7 | 241 / 81.5 | 241 / 81.3 | -5.4 |
| meloxicam | 177 / 83.0 | 223 / 78.6 | 222 / 81.1 | -1.9 |
| losartan | 104 / 86.9 | 129 / 81.4 | 136 / 81.0 | -5.9 |
| prednisone | 389 / 87.0 | 453 / 82.8 | 463 / 80.9 | -6.1 |
| venlafaxine | 254 / 88.0 | 262 / 81.6 | 260 / 80.7 | -7.4 |
| albuterol | 144 / 86.8 | 137 / 81.7 | 139 / 80.4 | -6.3 |
| tramadol | 369 / 84.1 | 473 / 80.4 | 457 / 80.3 | -3.9 |
| lisinopril | 199 / 86.3 | 206 / 81.2 | 206 / 80.2 | -6.1 |
| sertraline | 642 / 81.7 | 705 / 80.3 | 696 / 79.5 | -2.2 |
| escitalopram | 216 / 91.0 | 215 / 79.9 | 230 / 78.9 | -12.1 |
| amoxicillin | 121 / 85.1 | 137 / 80.6 | 148 / 78.8 | -6.3 |
| fluoxetine | 377 / 86.3 | 434 / 80.4 | 440 / 78.6 | -7.6 |
| trazodone | 211 / 86.0 | 216 / 80.2 | 205 / 78.4 | -7.6 |
| pantoprazole | 185 / 85.6 | 196 / 75.1 | 184 / 78.0 | -7.6 |
| famotidine | 107 / 84.6 | 99 / 80.7 | 100 / 77.8 | -6.9 |
| hydroxyzine | 216 / 79.6 | 225 / 76.9 | 216 / 77.3 | -2.3 |
| duloxetine | 167 / 88.7 | 198 / 77.0 | 197 / 77.1 | -11.6 |
| flonase | 179 / 83.9 | 175 / 79.6 | 173 / 76.9 | -7.0 |
| omeprazole | 189 / 87.8 | 192 / 78.0 | 195 / 76.9 | -10.9 |
| bupropion | 326 / 82.7 | 387 / 78.6 | 379 / 76.8 | -5.8 |
| cyclobenzaprine | 355 / 80.7 | 400 / 79.4 | 408 / 76.7 | -4.0 |
| rosuvastatin | 182 / 80.4 | 203 / 77.5 | 202 / 76.7 | -3.7 |
| gabapentin | 326 / 80.7 | 352 / 77.3 | 355 / 76.7 | -4.0 |
| ondansetron | 171 / 84.3 | 223 / 76.6 | 221 / 76.1 | -8.2 |
| montelukast | 124 / 89.7 | 118 / 76.6 | 117 / 75.2 | -14.5 |
| ibuprofen | 143 / 88.1 | 165 / 76.5 | 169 / 75.1 | -13.0 |
| methylphenidate | 229 / 88.9 | 247 / 75.5 | 248 / 74.6 | -14.3 |
| potassium-chloride | 131 / 84.1 | 154 / 74.6 | 152 / 74.0 | -10.1 |
| insulin-glargine | 212 / 80.4 | 221 / 78.2 | 224 / 74.0 | -6.4 |
| buspirone | 106 / 86.8 | 109 / 75.6 | 109 / 73.7 | -13.1 |
| semaglutide | 427 / 77.5 | 453 / 76.3 | 459 / 73.7 | -3.8 |
| empagliflozin | 150 / 85.6 | 141 / 73.1 | 138 / 72.8 | -12.8 |
| metoprolol | 336 / 79.2 | 378 / 75.1 | 395 / 72.6 | -6.6 |
| metformin | 300 / 74.8 | 320 / 68.8 | 303 / 71.6 | -3.2 |
| tirzepatide | 402 / 71.0 | 407 / 72.2 | 403 / 70.5 | -0.5 |
