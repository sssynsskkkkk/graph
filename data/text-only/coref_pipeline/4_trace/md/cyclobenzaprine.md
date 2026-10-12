# Cyclobenzaprine — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/cyclobenzaprine.txt` · 283 sentences · 32 changed by pronoun resolution · 461 sentences sent to EDC

## What is cyclobenzaprine?

**L5.0** `Complex Sentence` (0.796) → `decomposed`
- original: Cyclobenzaprine is a prescription muscle relaxant used short-term to relieve muscle spasms caused by sprains, strains, and injuries, including low back and neck pain.
  - S1: Cyclobenzaprine is a prescription muscle relaxant.
  - S2: It is used short-term to relieve muscle spasms.
  - S3: The spasms are caused by sprains, strains, and injuries.
  - S4: These include low back and neck pain.

**L5.1** `Complex Sentence` (0.864) → `decomposed`
- original: It is used together with rest and physical therapy to help relieve the pain, tenderness, and limited movement caused by muscle spasm.
- pronoun resolved: Cyclobenzaprine is used together with rest and physical therapy to help relieve the pain, tenderness, and limited movement caused by muscle spasm.
  - edits: “It” → “Cyclobenzaprine”
  - S1: Cyclobenzaprine is used together with rest and physical therapy.
  - S2: This combination helps relieve pain, tenderness, and limited movement.
  - S3: These symptoms are caused by muscle spasm.

**L5.2** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: 1,2

**L6.0** `Compound Sentence` (0.65) → `decomposed`
- original: Cyclobenzaprine is also used to treat fibromyalgia in adults, where it can help reduce pain.
- pronoun resolved: Cyclobenzaprine is also used to treat fibromyalgia in adults, where Cyclobenzaprine can help reduce pain.
  - edits: “it” → “Cyclobenzaprine”
  - S1: Cyclobenzaprine is also used to treat fibromyalgia in adults.
  - S2: Cyclobenzaprine can help reduce pain.

**L6.1** `Simple Sentence` (0.732) → `passthrough`
- original: For fibromyalgia, it is taken as a sublingual (under the tongue) tablet at bedtime under the brand name Tonmya.
- pronoun resolved: For fibromyalgia, Cyclobenzaprine is taken as a sublingual (under the tongue) tablet at bedtime under the brand name Tonmya.
  - edits: “it” → “Cyclobenzaprine”

**L6.2** `Compound Sentence` (0.9) → `decomposed`
- original: In clinical trials, Tonmya significantly reduced fibromyalgia pain compared with placebo over 14 weeks, and close to half of treated patients achieved at least a 30% improvement in pain.
  - S1: In clinical trials, Tonmya significantly reduced fibromyalgia pain compared with placebo over 14 weeks.
  - S2: Close to half of treated patients achieved at least a 30% improvement in pain.

**L6.3** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: 3

**L7.0** `Compound Sentence` (0.96) → `decomposed`
- original: The Flexeril brand has been discontinued, but cyclobenzaprine is available as generic tablets and as the brand-name products Amrix (extended-release capsules) and Fexmid.
  - S1: The Flexeril brand has been discontinued.
  - S2: Cyclobenzaprine is available as generic tablets.
  - S3: Cyclobenzaprine is also available as the brand-name products Amrix (extended-release capsules) and Fexmid.

**L7.1** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: 2,4

## How does cyclobenzaprine work?

**L10.0** `Complex Sentence` (0.945) → `decomposed`
- original: Cyclobenzaprine works by reducing the nerve signals in the brain that drive muscle tone and spasm, which allows tight, overactive muscles to relax.
  - S1: Cyclobenzaprine works by reducing the nerve signals in the brain.
  - S2: These signals drive muscle tone and spasm.
  - S3: This reduction allows tight, overactive muscles to relax.

**L10.1** `Compound Sentence` (0.959) → `decomposed`
- original: It acts within the central nervous system, primarily at the level of the brain stem, and does not act on the muscles themselves or at the junction between nerves and muscle.
- pronoun resolved: Cyclobenzaprine acts within the central nervous system, primarily at the level of the brain stem, and does not act on the muscles themselves or at the junction between nerves and muscle.
  - edits: “It” → “Cyclobenzaprine”
  - S1: Cyclobenzaprine acts within the central nervous system.
  - S2: It acts primarily at the level of the brain stem.
  - S3: It does not act on the muscles themselves.
  - S4: It does not act at the junction between nerves and muscle.

**L10.2** `Complex Sentence` (0.941) → `decomposed`
- original: 1,2 Because cyclobenzaprine works through the nervous system in this way, it will not relieve muscle spasm caused by central nervous system disease, such as cerebral palsy or spinal cord disease.
- pronoun resolved: 1,2 Because cyclobenzaprine works through the nervous system in this way, Cyclobenzaprine will not relieve muscle spasm caused by central nervous system disease, such as cerebral palsy or spinal cord disease.
  - edits: “it” → “Cyclobenzaprine”
  - S1: Cyclobenzaprine works through the nervous system in this way.
  - S2: Cyclobenzaprine will not relieve muscle spasm caused by central nervous system disease.
  - S3: Examples of central nervous system disease include cerebral palsy or spinal cord disease.

**L10.3** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: 1,2

**L11.0** `Simple Sentence` (0.98) → `passthrough`
- original: The way cyclobenzaprine works in fibromyalgia is not known.

**L11.1** `Complex Sentence` (0.877) → `decomposed`
- original: Laboratory studies show it blocks several receptor types, including serotonin (5-HT2A), histamine, and muscarinic receptors.
- pronoun resolved: Laboratory studies show Cyclobenzaprine blocks several receptor types, including serotonin (5-HT2A), histamine, and muscarinic receptors.
  - edits: “it” → “Cyclobenzaprine”
  - S1: Laboratory studies show Cyclobenzaprine blocks several receptor types.
  - S2: These receptor types include serotonin (5-HT2A), histamine, and muscarinic receptors.

**L11.2** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: 3

**L12.0** `Complex Sentence` (0.878) → `decomposed`
- original: Cyclobenzaprine is chemically related to tricyclic antidepressants such as amitriptyline, which explains several of its side effects (such as drowsiness and dry mouth) and some of its most important drug interactions.
- pronoun resolved: Cyclobenzaprine is chemically related to tricyclic antidepressants such as amitriptyline, which explains several of Cyclobenzaprine's side effects (such as drowsiness and dry mouth) and some of Cyclobenzaprine's most important drug interactions.
  - edits: “its” → “Cyclobenzaprine's”; “its” → “Cyclobenzaprine's”
  - S1: Cyclobenzaprine is chemically related to tricyclic antidepressants such as amitriptyline.
  - S2: This relationship explains several of Cyclobenzaprine's side effects.
  - S3: These side effects include drowsiness and dry mouth.
  - S4: The relationship also explains some of Cyclobenzaprine's most important drug interactions.

**L12.1** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: 1,2

## Is cyclobenzaprine a controlled substance or narcotic?

**L15.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: No.

**L15.1** `Compound Sentence` (0.773) → `decomposed`
- original: Cyclobenzaprine is not a controlled substance and is not a narcotic, opioid, or benzodiazepine.
  - S1: Cyclobenzaprine is not a controlled substance.
  - S2: It is not a narcotic, opioid, or benzodiazepine.

**L15.2** `Compound Sentence` (0.85) → `decomposed`
- original: It is a skeletal muscle relaxant that is chemically related to tricyclic antidepressants, and its FDA labeling states directly that cyclobenzaprine is not a controlled substance.
- pronoun resolved: Cyclobenzaprine is a skeletal muscle relaxant that is chemically related to tricyclic antidepressants, and Cyclobenzaprine's FDA labeling states directly that cyclobenzaprine is not a controlled substance.
  - edits: “It” → “Cyclobenzaprine”; “its” → “Cyclobenzaprine's”
  - S1: Cyclobenzaprine is a skeletal muscle relaxant that is chemically related to tricyclic antidepressants.
  - S2: Cyclobenzaprine's FDA labeling states directly that cyclobenzaprine is not a controlled substance.

**L15.3** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: 3

**L16.0** `Simple Sentence` (0.881) → `passthrough`
- original: Cyclobenzaprine is not considered addictive in the way opioids or benzodiazepines are.

**L16.1** `Compound Sentence` (0.856) → `decomposed`
- original: Stopping suddenly after prolonged use may rarely cause nausea, headache, and a general unwell feeling, but these effects are not a sign of addiction.
  - S1: Stopping suddenly after prolonged use may rarely cause nausea, headache, and a general unwell feeling.
  - S2: These effects are not a sign of addiction.

**L16.2** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: 1,3

## Cyclobenzaprine warnings

**L19.0** `Compound Sentence` (0.632) → `decomposed`
- original: Do not take cyclobenzaprine if you have an overactive thyroid (hyperthyroidism), congestive heart failure, a heart rhythm or conduction problem including heart block, or if you have recently had a heart attack.
  - S1: Do not take cyclobenzaprine if you have an overactive thyroid (hyperthyroidism).
  - S2: Do not take cyclobenzaprine if you have congestive heart failure.
  - S3: Do not take cyclobenzaprine if you have a heart rhythm or conduction problem including heart block.
  - S4: Do not take cyclobenzaprine if you have recently had a heart attack.

**L19.1** `Simple Sentence` (0.577) → `passthrough`
- original: Do not take cyclobenzaprine within 14 days of taking an MAO inhibitor.

**L19.2** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: 1,2,3

**L20.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: MAO inhibitors.

**L20.1** `Compound Sentence` (0.304) → `decomposed`
- original: Do not take MAO inhibitors, including isocarboxazid, linezolid, phenelzine, rasagiline, selegiline, and tranylcypromine with cyclobenzaprine.
  - S1: Do not take MAO inhibitors with cyclobenzaprine.
  - S2: MAO inhibitors include isocarboxazid, linezolid, phenelzine, rasagiline, selegiline, and tranylcypromine.

**L20.2** `Simple Sentence` (0.825) → `passthrough`
- original: Dangerously high fever, seizures, and deaths have occurred when cyclobenzaprine or similar drugs were combined with these medicines.

**L20.3** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: 1,2,3

**L21.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serotonin syndrome.

**L21.1** `Complex Sentence` (0.912) → `decomposed`
- original: Cyclobenzaprine can cause a serious condition called serotonin syndrome when taken with certain other medicines, especially antidepressants (SSRIs, SNRIs, tricyclics), tramadol, bupropion, meperidine, and verapamil.
  - S1: Cyclobenzaprine can cause a serious condition called serotonin syndrome.
  - S2: This condition occurs when cyclobenzaprine is taken with certain other medicines.
  - S3: These medicines include antidepressants (SSRIs, SNRIs, tricyclics), tramadol, bupropion, meperidine, and verapamil.

**L21.2** `Compound Sentence` (0.422) → `decomposed`
- original: Get medical help right away if you have agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness or twitching, loss of coordination, nausea, vomiting, or diarrhea.
  - S1: Get medical help right away if you have agitation.
  - S2: Get medical help right away if you have hallucinations.
  - S3: Get medical help right away if you have fever.
  - S4: Get medical help right away if you have sweating.
  - S5: Get medical help right away if you have shivering.
  - S6: Get medical help right away if you have a fast heart rate.
  - S7: Get medical help right away if you have muscle stiffness or twitching.
  - S8: Get medical help right away if you have loss of coordination.
  - S9: Get medical help right away if you have nausea.
  - S10: Get medical help right away if you have vomiting.
  - S11: Get medical help right away if you have diarrhea.

**L21.3** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: 1,2,3

**L22.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Drowsiness and alcohol.

**L22.1** `Compound Sentence` (0.969) → `decomposed`
- original: Cyclobenzaprine can impair your thinking and reactions, and this effect is stronger with alcohol or other medicines that cause drowsiness.
  - S1: Cyclobenzaprine can impair your thinking and reactions.
  - S2: This effect is stronger with alcohol or other medicines that cause drowsiness.

**L22.2** `Incomplete Sentence` (0.722) → `excluded_incomplete`
- original: Do not drive or do anything that needs alertness until you know how it affects you.

**L22.3** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: 1,2,3

**L23.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Pregnancy: If you use Tonmya for fibromyalgia.

**L23.1** `Complex Sentence` (0.946) → `decomposed`
- original: Based on animal studies, Tonmya may increase the risk of neural tube defects (a type of birth defect affecting the spine) if used in early pregnancy.
  - S1: Tonmya may increase the risk of neural tube defects if used in early pregnancy.
  - S2: Neural tube defects are a type of birth defect affecting the spine.
  - S3: This risk is based on animal studies.

**L23.2** `Incomplete Sentence` (0.821) → `excluded_incomplete`
- original: Do not use Tonmya in the two weeks before conception or during the first trimester.

**L23.3** `Incomplete Sentence` (0.971) → `excluded_incomplete`
- original: See the Pregnancy section below.

**L23.4** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: 3

## Before taking this medicine

**L26.0** `Simple Sentence` (0.791) → `passthrough`
- original: You should not take cyclobenzaprine if you are allergic to it, or if you have:
- pronoun resolved: You should not take cyclobenzaprine if you are allergic to cyclobenzaprine, or if you have:
  - edits: “it,” → “cyclobenzaprine,”

**L27.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: hyperthyroidism (overactive thyroid);

**L28.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: heart block, a heart rhythm disorder, or congestive heart failure; or

**L29.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: had a recent heart attack.

**L29.1** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: 1,2,3

**L30.0** `Simple Sentence` (0.806) → `passthrough`
- original: To make sure cyclobenzaprine is safe for you, tell your doctor if you have ever had:

**L31.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: liver disease; 1,2,3

**L32.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: glaucoma or increased pressure in the eye; 1,2,3

**L33.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: a seizure disorder (Tonmya); 3

**L34.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: an enlarged prostate or problems with urination.

**L34.1** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: 1,2,3

**L35.0** `Simple Sentence` (0.935) → `passthrough`
- original: The safety and effectiveness of cyclobenzaprine tablets have not been established in children under 15 years of age.

**L35.1** `Simple Sentence` (0.971) → `passthrough`
- original: The safety and effectiveness of Tonmya and Amrix have not been established in children of any age.

**L35.2** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: 1,2,3

**L36.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Older adults:

**L37.0** `Compound Sentence` (0.919) → `decomposed`
- original: Cyclobenzaprine builds up to higher levels in older adults and is more likely to cause side effects such as confusion, hallucinations, heart problems, and falls.
  - S1: Cyclobenzaprine builds up to higher levels in older adults.
  - S2: It is more likely to cause side effects such as confusion, hallucinations, heart problems, and falls.

**L37.1** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: In people 65 and older:

**L38.0** `Complex Sentence` (0.522) → `decomposed`
- original: Immediate-release tablets should be used only if clearly needed, starting at 5 mg and increasing slowly under medical supervision.
  - S1: Immediate-release tablets should be used only if clearly needed.
  - S2: The dosage should start at 5 mg.
  - S3: The dosage should increase slowly under medical supervision.

**L38.1** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: 1

**L39.0** `Compound-Complex Sentence` (0.771) → `decomposed`
- original: Amrix extended-release capsules are not recommended at all, because blood levels run about 40% higher and the drug stays in the body much longer (half-life of 50 hours versus 32 hours in younger adults).
- pronoun resolved: Amrix extended-release capsules are not recommended at all, because blood levels run about 40% higher and Amrix stays in the body much longer (half-life of 50 hours versus 32 hours in younger adults).
  - edits: “the drug” → “Amrix”
  - S1: Amrix extended-release capsules are not recommended.
  - S2: Blood levels run about 40% higher.
  - S3: Amrix stays in the body much longer.
  - S4: The half-life is 50 hours versus 32 hours in younger adults.

**L39.1** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: 2

**L40.0** `Simple Sentence` (0.985) → `passthrough`
- original: Tonmya is limited to the lower 2.8 mg dose once daily at bedtime.

**L40.1** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: 3

**L41.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Pregnancy:

**L42.0** `Compound Sentence` (0.5) → `decomposed`
- original: Pregnancy guidance differs by product, so check which cyclobenzaprine product you use.
  - S1: Pregnancy guidance differs by product.
  - S2: Check which cyclobenzaprine product you use.

**L43.0** `Complex Sentence` (0.87) → `decomposed`
- original: Tonmya (fibromyalgia): Based on animal data, Tonmya may increase the risk of neural tube defects when used two weeks before conception and through the first trimester.
  - S1: Tonmya is associated with fibromyalgia.
  - S2: Animal data suggests Tonmya may increase the risk of neural tube defects.
  - S3: This risk occurs when Tonmya is used two weeks before conception and through the first trimester.

**L43.1** `Complex Sentence` (0.902) → `decomposed`
- original: Because neural tube development happens early, often before pregnancy is recognized, avoid Tonmya during this window.
  - S1: Neural tube development happens early.
  - S2: This often occurs before pregnancy is recognized.
  - S3: Avoid Tonmya during this window.

**L43.2** `Compound Sentence` (0.965) → `decomposed`
- original: Your healthcare provider should do a pregnancy test before you start Tonmya, and you should use effective contraception during treatment and for two weeks after the final dose.
  - S1: Your healthcare provider should do a pregnancy test before you start Tonmya.
  - S2: You should use effective contraception during treatment and for two weeks after the final dose.

**L43.3** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: 3

**L44.0** `Compound-Complex Sentence` (0.908) → `decomposed`
- original: Immediate-release tablets and Amrix (muscle spasm): available data have not identified a risk of major birth defects or miscarriage, and animal studies at usual doses did not show harm to the fetus, although data are limited.
  - S1: Immediate-release tablets and Amrix (muscle spasm) are available.
  - S2: Data have not identified a risk of major birth defects.
  - S3: Data have not identified a risk of miscarriage.
  - S4: Animal studies at usual doses did not show harm to the fetus.
  - S5: Data are limited.

**L44.1** `Simple Sentence` (0.989) → `passthrough`
- original: These products should be used during pregnancy only if clearly needed.
- pronoun resolved: Cyclobenzaprine should be used during pregnancy only if clearly needed.
  - edits: “These products” → “Cyclobenzaprine”

**L44.2** `Incomplete Sentence` (0.915) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or plan to become pregnant.

**L44.3** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: 1,2

**L45.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Breastfeeding:

**L46.0** `Compound Sentence` (0.935) → `decomposed`
- original: Small published reports suggest cyclobenzaprine passes into breast milk in low amounts, but there is no information on effects on a breastfed baby or on milk supply.
  - S1: Small published reports suggest cyclobenzaprine passes into breast milk in low amounts.
  - S2: There is no information on effects on a breastfed baby or on milk supply.

**L46.1** `Incomplete Sentence` (0.975) → `excluded_incomplete`
- original: Talk with your healthcare provider about the benefits of breastfeeding alongside your need for this medicine.
- pronoun resolved: Talk with your healthcare provider about the benefits of breastfeeding alongside your need for Cyclobenzaprine.
  - edits: “this medicine.” → “Cyclobenzaprine.”

**L46.2** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: 2,3

## How should I take cyclobenzaprine?

**L49.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Cyclobenzaprine dose for muscle spasm:

**L50.0** `Simple Sentence` (0.985) → `passthrough`
- original: Cyclobenzaprine is usually taken for up to 2 or 3 weeks for muscle spasm.

**L50.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L50.2** `Simple Sentence` (0.984) → `passthrough`
- original: Your doctor may occasionally change your dose.

**L51.0** `Simple Sentence` (0.989) → `passthrough`
- original: Immediate-release tablets are taken three times a day.

**L51.1** `Simple Sentence` (0.978) → `passthrough`
- original: Extended-release capsules are taken once daily, at about the same time each day.

**L51.2** `Compound-Complex Sentence` (0.613) → `decomposed`
- original: Swallow the capsules whole; if you have difficulty swallowing them, you can open the capsule and sprinkle the contents onto a tablespoon of applesauce, then swallow the mixture right away without chewing.
  - S1: Swallow the capsules whole.
  - S2: You can open the capsule if you have difficulty swallowing them.
  - S3: Sprinkle the contents onto a tablespoon of applesauce.
  - S4: Swallow the mixture right away.
  - S5: Do not chew the mixture.

**L52.0** `Incomplete Sentence` (0.925) → `excluded_incomplete`
- original: Follow your doctor's dosing instructions very carefully.

**L53.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Cyclobenzaprine for fibromyalgia:

**L54.0** `Simple Sentence` (0.971) → `passthrough`
- original: Tonmya is taken once daily at bedtime, after brushing your teeth.

**L54.1** `Compound Sentence` (0.84) → `decomposed`
- original: Drink a few sips of water first so your mouth is moist, place the tablet(s) under your tongue until dissolved, and do not swallow whole, cut, crush, or chew.
  - S1: Drink a few sips of water first so your mouth is moist.
  - S2: Place the tablet(s) under your tongue until dissolved.
  - S3: Do not swallow whole, cut, crush, or chew.

**L54.2** `Compound Sentence` (0.882) → `decomposed`
- original: Avoid eating or drinking for at least 15 minutes afterward, avoid hot, cold, or acidic drinks until morning, and avoid talking for about 5 minutes after dosing.
  - S1: Avoid eating or drinking for at least 15 minutes afterward.
  - S2: Avoid hot, cold, or acidic drinks until morning.
  - S3: Avoid talking for about 5 minutes after dosing.

**L54.3** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: 3

## Cyclobenzaprine dosage

**L57.0** `Compound Sentence` (0.751) → `decomposed`
- original: The usual cyclobenzaprine dose for muscle spasm is 5 mg three times a day, which may be increased to 10 mg three times a day if needed.
  - S1: The usual cyclobenzaprine dose for muscle spasm is 5 mg three times a day.
  - S2: This dose may be increased to 10 mg three times a day if needed.

**L57.1** `Simple Sentence` (0.986) → `passthrough`
- original: The maximum dose is 30 mg per day.

**L57.2** `Simple Sentence` (0.988) → `passthrough`
- original: Cyclobenzaprine is taken for a maximum of 2 to 3 weeks.

**L57.3** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: 1

**L58.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Cyclobenzaprine dosage chart:

**L59.0** `Simple Sentence` (0.608) → `passthrough`
- original: Immediate-release tablets: the usual starting dose is 5 mg three times a day, increased to 10 mg three times a day based on your response.

**L59.1** `Compound Sentence` (0.466) → `decomposed`
- original: In adults 65 and older and in people with mild liver problems, treatment should start at 5 mg and be increased slowly, if at all.
  - S1: In adults 65 and older and in people with mild liver problems, treatment should start at 5 mg.
  - S2: It should be increased slowly, if at all.

**L59.2** `Simple Sentence` (0.981) → `passthrough`
- original: The tablets are not recommended with moderate to severe liver impairment.

**L59.3** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: 1

**L60.0** `Compound Sentence` (0.676) → `decomposed`
- original: Amrix extended-release capsules: the recommended dose is 15 mg once daily for most adults; some people may need 30 mg once daily (one 30 mg capsule or two 15 mg capsules).
  - S1: The recommended dose of Amrix extended-release capsules is 15 mg once daily for most adults.
  - S2: Some people may need 30 mg once daily.
  - S3: This can be achieved with one 30 mg capsule or two 15 mg capsules.

**L60.1** `Simple Sentence` (0.678) → `passthrough`
- original: Amrix is not recommended in adults 65 and older, or in anyone with liver impairment of any severity.

**L60.2** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: 2

**L61.0** `Complex Sentence` (0.805) → `decomposed`
- original: Tonmya sublingual tablets (fibromyalgia): The recommended starting dose of Tonmya is 2.8 mg (1 sublingual tablet) once daily at bedtime for the first 14 days, then increases to the target dose of 5.6 mg (2 sublingual tablets) once daily at bedtime from day 15 onward.
  - S1: Tonmya is a sublingual tablet used for fibromyalgia.
  - S2: The recommended starting dose is 2.8 mg (1 sublingual tablet) once daily at bedtime.
  - S3: This starting dose is for the first 14 days.
  - S4: The dose then increases to the target dose of 5.6 mg (2 sublingual tablets).
  - S5: The target dose is taken once daily at bedtime from day 15 onward.

**L61.1** `Simple Sentence` (0.985) → `passthrough`
- original: The maximum is 5.6 mg once daily.

**L61.2** `Compound Sentence` (0.947) → `decomposed`
- original: In adults 65 and older and in people with mild liver impairment, the maximum is 2.8 mg once daily at bedtime, and Tonmya is not recommended with moderate or severe liver impairment.
  - S1: In adults 65 and older and in people with mild liver impairment, the maximum is 2.8 mg once daily at bedtime.
  - S2: Tonmya is not recommended with moderate or severe liver impairment.

**L61.3** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: 3

**L62.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Product | Usual adult dose | Maximum dose | How long

**L63.0** `Compound-Complex Sentence` (0.489) → `decomposed`
- original: Immediate-release tablets, formerly sold as Flexeril (adults and children 15 and older) | 5 mg three times a day, increased to 10 mg three times a day if needed | 30 mg per day (10 mg three times a day) | Up to 2 to 3 weeks
  - S1: Immediate-release tablets were formerly sold as Flexeril.
  - S2: Flexeril is for adults and children 15 and older.
  - S3: The dosage is 5 mg three times a day.
  - S4: The dosage can be increased to 10 mg three times a day if needed.
  - S5: The maximum daily dosage is 30 mg.
  - S6: The maximum daily dosage consists of 10 mg three times a day.
  - S7: The treatment duration is up to 2 to 3 weeks.

**L64.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Amrix extended-release capsules | 15 mg once daily | 30 mg once daily | Up to 2 to 3 weeks

**L65.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Tonmya sublingual tablets (fibromyalgia) | 2.8 mg once daily at bedtime for 14 days, then 5.6 mg once daily at bedtime | 5.6 mg once daily | Ongoing, as directed

**L66.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: 1,2,3

**L67.0** `Incomplete Sentence` (0.535) → `excluded_incomplete`
- original: Can I take 2 cyclobenzaprine 10 mg at the same time?

**L67.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L68.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: No.

**L68.1** `Simple Sentence` (0.722) → `passthrough`
- original: Do not take two cyclobenzaprine 10 mg tablets at once.

**L68.2** `Compound Sentence` (0.375) → `decomposed`
- original: The maximum recommended single dose of the immediate-release tablet is 10 mg, taken up to three times a day.
  - S1: The maximum recommended single dose of the immediate-release tablet is 10 mg.
  - S2: It is taken up to three times a day.

**L68.3** `Compound-Complex Sentence` (0.844) → `decomposed`
- original: Taking 20 mg at one time increases the risk of side effects such as severe drowsiness and fast heart rate, and in overdose cyclobenzaprine can cause dangerous heart rhythm problems, without providing better muscle spasm relief.
  - S1: Taking 20 mg of cyclobenzaprine at one time increases the risk of side effects.
  - S2: Taking 20 mg at one time can cause severe drowsiness.
  - S3: Taking 20 mg at one time can cause a fast heart rate.
  - S4: In an overdose, cyclobenzaprine can cause dangerous heart rhythm problems.
  - S5: Taking 20 mg at one time does not provide better muscle spasm relief.

**L68.4** `Simple Sentence` (0.478) → `passthrough`
- original: If your dose is not controlling your symptoms, talk with your doctor rather than doubling up.

**L68.5** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: 1

**L69.0** `Incomplete Sentence` (0.862) → `excluded_incomplete`
- original: How often can you take cyclobenzaprine?

**L69.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L70.0** `Simple Sentence` (0.989) → `passthrough`
- original: Immediate-release tablets are taken three times a day.

**L70.1** `Simple Sentence` (0.98) → `passthrough`
- original: Amrix extended-release capsules and Tonmya sublingual tablets are taken once a day.

**L70.2** `Incomplete Sentence` (0.942) → `excluded_incomplete`
- original: Do not take extra doses between scheduled doses.

**L70.3** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: 1,2,3

**L71.0** `Compound Sentence` (0.737) → `decomposed`
- original: How long does cyclobenzaprine take to work, and how long does it last?
- pronoun resolved: How long does cyclobenzaprine take to work, and how long does cyclobenzaprine last?
  - edits: “it” → “cyclobenzaprine”
  - S1: How long does cyclobenzaprine take to work?
  - S2: How long does cyclobenzaprine last?

**L71.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L72.0** `Complex Sentence` (0.421) → `decomposed`
- original: In clinical trials of the immediate-release tablets, the muscle relaxant effect was measurable within the first several days, with significant improvement in muscle spasm and pain by day 3 or 4 of treatment.
  - S1: In clinical trials of the immediate-release tablets, the muscle relaxant effect was measurable within the first several days.
  - S2: There was significant improvement in muscle spasm and pain by day 3 or 4 of treatment.

**L72.1** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: 1

**L73.0** `Compound Sentence` (0.831) → `decomposed`
- original: With Amrix extended-release capsules, the drug is first detectable in the blood about 1.5 hours after a dose, with peak levels at 7 to 8 hours, and one daily dose provides day-long coverage.
- pronoun resolved: With Amrix extended-release capsules, Cyclobenzaprine is first detectable in the blood about 1.5 hours after a dose, with peak levels at 7 to 8 hours, and one daily dose provides day-long coverage.
  - edits: “the drug” → “Cyclobenzaprine”
  - S1: With Amrix extended-release capsules, Cyclobenzaprine is first detectable in the blood about 1.5 hours after a dose.
  - S2: Peak levels occur at 7 to 8 hours.
  - S3: One daily dose provides day-long coverage.

**L73.1** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: 2

**L74.0** `Incomplete Sentence` (0.969) → `excluded_incomplete`
- original: How long does cyclobenzaprine stay in your system?

**L74.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L75.0** `Simple Sentence` (0.986) → `passthrough`
- original: Cyclobenzaprine stays in your system for about 3 to 7 days after your last dose.

**L75.1** `Compound Sentence` (0.965) → `decomposed`
- original: It has a half-life of around 18 hours for the immediate-release tablets, and a drug takes 4 to 5 half-lives to clear from the body.
- pronoun resolved: Cyclobenzaprine has a half-life of around 18 hours for the immediate-release tablets, and a drug takes 4 to 5 half-lives to clear from the body.
  - edits: “It” → “Cyclobenzaprine”
  - S1: Cyclobenzaprine has a half-life of around 18 hours for the immediate-release tablets.
  - S2: A drug takes 4 to 5 half-lives to clear from the body.

**L75.2** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: 1

**L76.0** `Compound-Complex Sentence` (0.731) → `decomposed`
- original: The once-daily forms last longer: the half-life is about 32 hours for Amrix extended-release capsules and about 36 hours for Tonmya sublingual tablets, so these can take a week or more to fully clear.
- pronoun resolved: The once-daily forms last longer: the half-life is about 32 hours for Amrix extended-release capsules and about 36 hours for Tonmya sublingual tablets, so Amrix extended-release capsules can take a week or more to fully clear.
  - edits: “these” → “Amrix extended-release capsules”
  - S1: The once-daily forms last longer.
  - S2: The half-life is about 32 hours for Amrix extended-release capsules.
  - S3: The half-life is about 36 hours for Tonmya sublingual tablets.
  - S4: Amrix extended-release capsules can take a week or more to fully clear.

**L76.1** `Compound Sentence` (0.704) → `decomposed`
- original: Cyclobenzaprine also stays in the body longer in older adults and in people with liver problems, in whom blood levels run higher.
  - S1: Cyclobenzaprine also stays in the body longer in older adults.
  - S2: It stays in the body longer in people with liver problems.
  - S3: In people with liver problems, blood levels run higher.

**L76.2** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: 1,2,3

**L77.0** `Incomplete Sentence` (0.963) → `excluded_incomplete`
- original: Does cyclobenzaprine show up on a drug test?

**L77.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L78.0** `Compound-Complex Sentence` (0.875) → `decomposed`
- original: No, cyclobenzaprine does not usually show up on a drug test, as it is not a controlled substance and it is not one of the five substances (amphetamines, cannabinoids, cocaine, opiates, and phencyclidine) required on standard federal workplace drug tests.
- pronoun resolved: No, cyclobenzaprine does not usually show up on a drug test, as cyclobenzaprine is not a controlled substance and cyclobenzaprine is not one of the five substances (amphetamines, cannabinoids, cocaine, opiates, and phencyclidine) required on standard federal workplace drug tests.
  - edits: “it” → “cyclobenzaprine”; “it” → “cyclobenzaprine”
  - S1: Cyclobenzaprine does not usually show up on a drug test.
  - S2: Cyclobenzaprine is not a controlled substance.
  - S3: Cyclobenzaprine is not one of the five substances required on standard federal workplace drug tests.
  - S4: The five substances required on standard federal workplace drug tests are amphetamines, cannabinoids, cocaine, opiates, and phencyclidine.

**L78.1** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: 3,5

**L79.0** `Compound Sentence` (0.816) → `decomposed`
- original: However, cyclobenzaprine has a similar structure to tricyclic antidepressants, and it is a recognized cause of false positive results on tricyclic antidepressant immunoassays, including urine immunoassays.
- pronoun resolved: However, cyclobenzaprine has a similar structure to tricyclic antidepressants, and Cyclobenzaprine is a recognized cause of false positive results on tricyclic antidepressant immunoassays, including urine immunoassays.
  - edits: “it” → “Cyclobenzaprine”
  - S1: However, cyclobenzaprine has a similar structure to tricyclic antidepressants.
  - S2: Cyclobenzaprine is a recognized cause of false positive results on tricyclic antidepressant immunoassays.
  - S3: This includes urine immunoassays.

**L79.1** `Simple Sentence` (0.975) → `passthrough`
- original: Tests for tricyclic antidepressants are not part of routine drugs-of-abuse screening.

**L79.2** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: 5

**L80.0** `Compound Sentence` (0.346) → `decomposed`
- original: If you take cyclobenzaprine and need a drug test, tell the testing provider what medicines you take.
  - S1: If you take cyclobenzaprine and need a drug test, tell the testing provider what medicines you take.

**L80.1** `Compound Sentence` (0.967) → `decomposed`
- original: A screening result is only presumptive, and a confirmatory laboratory test such as gas chromatography-mass spectrometry can tell cyclobenzaprine apart from a tricyclic antidepressant.
  - S1: A screening result is only presumptive.
  - S2: A confirmatory laboratory test such as gas chromatography-mass spectrometry can tell cyclobenzaprine apart from a tricyclic antidepressant.

**L80.2** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: 5

## What happens if I miss a dose?

**L83.0** `Compound Sentence` (0.742) → `decomposed`
- original: Immediate-release tablets and Amrix: take the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
- pronoun resolved: Immediate-release tablets and Amrix: take Cyclobenzaprine as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - edits: “the medicine” → “Cyclobenzaprine”
  - S1: Immediate-release tablets and Amrix: take Cyclobenzaprine as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L83.1** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

**L84.0** `Simple Sentence` (0.705) → `passthrough`
- original: Tonmya: if you miss your bedtime dose, take your next dose at the regular time the following evening.

**L84.1** `Compound Sentence` (0.603) → `decomposed`
- original: Do not take a missed dose during the day, and do not take two doses to make up for a missed dose.
  - S1: Do not take a missed dose during the day.
  - S2: Do not take two doses to make up for a missed dose.

**L84.2** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: 3

## What happens if I overdose?

**L87.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L87.1** `Compound Sentence` (0.688) → `decomposed`
- original: An overdose of cyclobenzaprine can be fatal, and deliberate overdoses often involve other drugs or alcohol, which raises the danger.
  - S1: An overdose of cyclobenzaprine can be fatal.
  - S2: Deliberate overdoses often involve other drugs or alcohol.
  - S3: This raises the danger.

**L87.2** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: 1,2

**L88.0** `Compound Sentence` (0.477) → `decomposed`
- original: Overdose symptoms may include severe drowsiness, fast heartbeats, tremors, agitation, slurred speech, confusion, dizziness, nausea, vomiting, or hallucinations.
  - S1: Overdose symptoms may include severe drowsiness.
  - S2: They may include fast heartbeats.
  - S3: They may include tremors.
  - S4: They may include agitation.
  - S5: They may include slurred speech.
  - S6: They may include confusion.
  - S7: They may include dizziness.
  - S8: They may include nausea.
  - S9: They may include vomiting.
  - S10: They may include hallucinations.

**L88.1** `Simple Sentence` (0.638) → `passthrough`
- original: Rare but critical effects include seizures, dangerously low blood pressure, heart rhythm disturbances, and cardiac arrest.

**L88.2** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: 1,2

## What to avoid

**L91.0** `Incomplete Sentence` (0.956) → `excluded_incomplete`
- original: Avoid driving or hazardous activity until you know how cyclobenzaprine will affect you.

**L91.1** `Compound Sentence` (0.969) → `decomposed`
- original: It can impair your thinking and reactions, and this effect is stronger with alcohol or other medicines that cause drowsiness.
- pronoun resolved: Cyclobenzaprine can impair your thinking and reactions, and this effect is stronger with alcohol or other medicines that cause drowsiness.
  - edits: “It” → “Cyclobenzaprine”
  - S1: Cyclobenzaprine can impair your thinking and reactions.
  - S2: This effect is stronger with alcohol or other medicines that cause drowsiness.

**L91.2** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Avoid drinking alcohol while taking cyclobenzaprine.

**L91.3** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: 1,2,3

## Cyclobenzaprine side effects

**L94.0** `Simple Sentence` (0.916) → `passthrough`
- original: The most common cyclobenzaprine side effects are drowsiness, dry mouth, dizziness, fatigue, and headache.

**L94.1** `Compound Sentence` (0.956) → `decomposed`
- original: Most side effects are mild and settle as your body adjusts, but cyclobenzaprine can occasionally cause serious heart rhythm effects and serotonin syndrome.
  - S1: Most side effects are mild and settle as your body adjusts.
  - S2: Cyclobenzaprine can occasionally cause serious heart rhythm effects and serotonin syndrome.

**L94.2** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: 1

**L95.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Common cyclobenzaprine side effects:

**L96.0** `Simple Sentence` (0.621) → `passthrough`
- original: Common cyclobenzaprine side effects may include: 1

**L97.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: drowsiness and tiredness;

**L98.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: dry mouth;

**L99.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: dizziness;

**L100.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: fatigue;

**L101.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: headache;

**L102.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: nausea, indigestion, or constipation;

**L103.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: blurred vision;

**L104.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: unpleasant taste;

**L105.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: nervousness or confusion.

**L106.0** `Complex Sentence` (0.94) → `decomposed`
- original: In placebo-controlled trials of the immediate-release tablets, side effects were dose-related, occurring more often with 10 mg than with 5 mg: 1
  - S1: In placebo-controlled trials of the immediate-release tablets, side effects were dose-related.
  - S2: The side effects occurred more often with 10 mg than with 5 mg.

**L107.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Side effect | Cyclobenzaprine 5 mg | Cyclobenzaprine 10 mg | Placebo

**L108.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Drowsiness | 29% | 38% | 10%

**L109.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Dry mouth | 21% | 32% | 7%

**L110.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Fatigue | 6% | 6% | 3%

**L111.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Headache | 5% | 5% | 8%

**L112.0** `Complex Sentence` (0.57) → `decomposed`
- original: With Amrix, the most common side effects are dry mouth (up to 14% at 30 mg), dizziness, fatigue, constipation, nausea, indigestion, and drowsiness.
  - S1: With Amrix, the most common side effects are dry mouth, dizziness, fatigue, constipation, nausea, indigestion, and drowsiness.
  - S2: Dry mouth occurs in up to 14% of patients at 30 mg.

**L112.1** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: 2

**L113.0** `Complex Sentence` (0.882) → `decomposed`
- original: With Tonmya, because it dissolves under the tongue, the most common side effects involve the mouth: reduced feeling or numbness in the mouth (23%), mouth discomfort, abnormal taste, tingling, mouth pain, and canker sores, along with sleepiness, fatigue, and dry mouth.
  - S1: With Tonmya, the most common side effects involve the mouth.
  - S2: Tonmya dissolves under the tongue.
  - S3: The side effects include reduced feeling or numbness in the mouth.
  - S4: The side effects include mouth discomfort.
  - S5: The side effects include abnormal taste.
  - S6: The side effects include tingling.
  - S7: The side effects include mouth pain.
  - S8: The side effects include canker sores.
  - S9: The side effects include sleepiness.
  - S10: The side effects include fatigue.
  - S11: The side effects include dry mouth.

**L113.1** `Compound Sentence` (0.787) → `decomposed`
- original: Mouth-related effects usually begin within minutes of a dose and most resolve within an hour.
  - S1: Mouth-related effects usually begin within minutes of a dose.
  - S2: Most resolve within an hour.

**L113.2** `Simple Sentence` (0.912) → `passthrough`
- original: Moistening your mouth with sips of water before dosing reduces the risk of numbness.

**L113.3** `Incomplete Sentence` (0.878) → `excluded_incomplete`
- original: Tell your healthcare provider if mouth effects are severe.

**L113.4** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: 3

**L114.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious cyclobenzaprine side effects:

**L115.0** `Compound Sentence` (0.503) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to cyclobenzaprine: hives; difficult breathing; swelling of your face, lips, tongue, or throat; or itching.
  - S1: Get emergency medical help if you have signs of an allergic reaction to cyclobenzaprine.
  - S2: These signs include hives.
  - S3: These signs include difficult breathing.
  - S4: These signs include swelling of your face, lips, tongue, or throat.
  - S5: These signs include itching.

**L115.1** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: 2,3

**L116.0** `Incomplete Sentence` (0.966) → `excluded_incomplete`
- original: Stop taking cyclobenzaprine and call your doctor at once if you have: 1,2,3

**L117.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: fast, pounding, or irregular heartbeats;

**L118.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: chest pain or pressure, or pain spreading to your jaw or shoulder;

**L119.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: sudden numbness or weakness, slurred speech, or balance problems; or

**L120.0** `Simple Sentence` (0.623) → `passthrough`
- original: symptoms of serotonin syndrome: agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness or twitching, loss of coordination, nausea, vomiting, or diarrhea.

**L121.0** `Simple Sentence` (0.676) → `passthrough`
- original: Serious side effects, including confusion, hallucinations, and heart problems leading to falls, are more likely in older adults.

**L121.1** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: 1

**L122.0** `Incomplete Sentence` (0.902) → `excluded_incomplete`
- original: Does cyclobenzaprine make you sleepy?

**L122.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L123.0** `Complex Sentence` (0.748) → `decomposed`
- original: Yes, drowsiness is the most common side effect of the tablets, affecting up to 38% of people taking the 10 mg dose in clinical trials.
  - S1: Yes, drowsiness is the most common side effect of the tablets.
  - S2: This side effect affects up to 38% of people taking the 10 mg dose.
  - S3: These figures are from clinical trials.

**L123.1** `Complex Sentence` (0.833) → `decomposed`
- original: This is one reason 5 mg is the usual starting dose, since it causes less drowsiness with comparable effectiveness.
- pronoun resolved: This is one reason 5 mg is the usual starting dose, since 5 mg causes less drowsiness with comparable effectiveness.
  - edits: “it” → “5 mg”
  - S1: This is one reason 5 mg is the usual starting dose.
  - S2: 5 mg causes less drowsiness.
  - S3: 5 mg has comparable effectiveness.

**L123.2** `Compound Sentence` (0.597) → `decomposed`
- original: Analysis of trial data shows cyclobenzaprine relieves muscle spasm whether or not sedation occurs, so drowsiness is not required for it to work.
- pronoun resolved: Analysis of trial data shows cyclobenzaprine relieves muscle spasm whether or not sedation occurs, so drowsiness is not required for cyclobenzaprine to work.
  - edits: “it” → “cyclobenzaprine”
  - S1: Analysis of trial data shows cyclobenzaprine relieves muscle spasm whether or not sedation occurs.
  - S2: Drowsiness is not required for cyclobenzaprine to work.

**L123.3** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: 1

**L124.0** `Incomplete Sentence` (0.897) → `excluded_incomplete`
- original: Does cyclobenzaprine cause constipation?

**L124.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L125.0** `Compound Sentence` (0.546) → `decomposed`
- original: Constipation is a known side effect, reported in 1% to 3% of people taking the immediate-release tablets and up to 3% of people taking Amrix 30 mg in clinical trials.
  - S1: Constipation is a known side effect.
  - S2: It is reported in 1% to 3% of people taking the immediate-release tablets.
  - S3: It is reported in up to 3% of people taking Amrix 30 mg in clinical trials.

**L125.1** `Compound Sentence` (0.555) → `decomposed`
- original: It results from the drug's anticholinergic (drying) effects, the same mechanism behind dry mouth and blurred vision.
- pronoun resolved: Constipation results from the drug's anticholinergic (drying) effects, the same mechanism behind dry mouth and blurred vision.
  - edits: “It” → “Constipation”
  - S1: Constipation results from the drug's anticholinergic (drying) effects.
  - S2: The same mechanism is behind dry mouth and blurred vision.

**L125.2** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: 1,2

**L126.0** `Compound Sentence` (0.545) → `decomposed`
- original: This is not a complete list of side effects, and others may occur.
  - S1: This is not a complete list of side effects.
  - S2: Others may occur.

**L126.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L126.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## Cyclobenzaprine interactions

**L129.0** `Complex Sentence` (0.72) → `decomposed`
- original: The most serious cyclobenzaprine (Flexeril) drug interactions are with MAO inhibitors, which must never be combined with cyclobenzaprine, and with antidepressants and other serotonergic medicines, which can cause serotonin syndrome.
  - S1: The most serious cyclobenzaprine (Flexeril) drug interactions are with MAO inhibitors.
  - S2: MAO inhibitors must never be combined with cyclobenzaprine.
  - S3: The most serious cyclobenzaprine (Flexeril) drug interactions are also with antidepressants and other serotonergic medicines.
  - S4: These medicines can cause serotonin syndrome.

**L129.1** `Complex Sentence` (0.576) → `decomposed`
- original: Cyclobenzaprine also interacts with alcohol and other medicines that cause drowsiness, making sedation worse.
  - S1: Cyclobenzaprine interacts with alcohol and other medicines that cause drowsiness.
  - S2: This interaction makes sedation worse.

**L129.2** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: 1,2,3

**L130.0** `Simple Sentence` (0.885) → `passthrough`
- original: Other medicines and substances that interact with cyclobenzaprine include: 1,2,3

**L131.0** `Incomplete Sentence` (0.953) → `excluded_incomplete`
- original: MAO inhibitors such as isocarboxazid, linezolid, phenelzine, rasagiline, selegiline, and tranylcypromine (contraindicated; do not use within 14 days);

**L132.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: antidepressants of any kind, including SSRIs, SNRIs, and tricyclics (risk of serotonin syndrome);

**L133.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: bupropion, tramadol, or meperidine;

**L134.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: verapamil;

**L135.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: alcohol;

**L136.0** `Incomplete Sentence` (0.949) → `excluded_incomplete`
- original: opioid medicines, sleeping pills, other muscle relaxers, and medicines for anxiety or seizures;

**L137.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: barbiturates and other CNS depressants;

**L138.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: anticholinergic medicines;

**L139.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: guanethidine or similar blood pressure medicines;

**L140.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: cold or allergy medicines containing an antihistamine.

**L141.0** `Compound Sentence` (0.963) → `decomposed`
- original: Cyclobenzaprine may increase the risk of seizures in people taking tramadol, and may block the blood pressure-lowering effect of guanethidine and similar drugs.
  - S1: Cyclobenzaprine may increase the risk of seizures in people taking tramadol.
  - S2: It may block the blood pressure-lowering effect of guanethidine and similar drugs.

**L141.1** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: 1,2,3

**L142.0** `Incomplete Sentence` (0.967) → `excluded_incomplete`
- original: Tell your doctor about all your other medicines.

**L142.1** `Compound Sentence` (0.964) → `decomposed`
- original: This list is not complete, and other drugs may interact with cyclobenzaprine, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: This list is not complete.
  - S2: Other drugs may interact with cyclobenzaprine.
  - S3: These include prescription and over-the-counter medicines, vitamins, and herbal products.

**L143.0** `Incomplete Sentence` (0.831) → `excluded_incomplete`
- original: Can you take ibuprofen with cyclobenzaprine?

**L143.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L144.0** `Compound-Complex Sentence` (0.727) → `decomposed`
- original: There is no listed drug interaction between cyclobenzaprine and ibuprofen, and the two are commonly prescribed together for painful muscle injuries, since they work in different ways.
- pronoun resolved: There is no listed drug interaction between cyclobenzaprine and ibuprofen, and the two are commonly prescribed together for painful muscle injuries, since cyclobenzaprine and ibuprofen work in different ways.
  - edits: “they” → “cyclobenzaprine and ibuprofen”
  - S1: There is no listed drug interaction between cyclobenzaprine and ibuprofen.
  - S2: Cyclobenzaprine and ibuprofen are commonly prescribed together for painful muscle injuries.
  - S3: Cyclobenzaprine and ibuprofen work in different ways.

**L144.1** `Compound-Complex Sentence` (0.857) → `decomposed`
- original: In studies, taking cyclobenzaprine with aspirin did not change blood levels of either drug, and combining it with naproxen was well tolerated, although the combination caused more drowsiness than naproxen alone.
- pronoun resolved: In studies, taking cyclobenzaprine with aspirin did not change blood levels of either drug, and combining cyclobenzaprine with naproxen was well tolerated, although the combination caused more drowsiness than naproxen alone.
  - edits: “it” → “cyclobenzaprine”
  - S1: In studies, taking cyclobenzaprine with aspirin did not change blood levels of either drug.
  - S2: Combining cyclobenzaprine with naproxen was well tolerated.
  - S3: The combination of cyclobenzaprine and naproxen caused more drowsiness than naproxen alone.
  - S4: Cyclobenzaprine and naproxen together caused more drowsiness than naproxen by itself.

**L144.2** `Incomplete Sentence` (0.448) → `excluded_incomplete`
- original: Check with your doctor or pharmacist before combining medicines, especially if you take other drugs as well.

**L144.3** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: 1

**L145.0** `Incomplete Sentence` (0.788) → `excluded_incomplete`
- original: Can you take Tylenol with cyclobenzaprine?

**L145.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L146.0** `Compound Sentence` (0.969) → `decomposed`
- original: There is no listed interaction between cyclobenzaprine and acetaminophen (Tylenol), and they may be used together when recommended by your doctor.
- pronoun resolved: There is no listed interaction between cyclobenzaprine and acetaminophen (Tylenol), and cyclobenzaprine and acetaminophen may be used together when recommended by your doctor.
  - edits: “they” → “cyclobenzaprine and acetaminophen”
  - S1: There is no listed interaction between cyclobenzaprine and acetaminophen (Tylenol).
  - S2: Cyclobenzaprine and acetaminophen may be used together when recommended by your doctor.

**L146.1** `Simple Sentence` (0.432) → `passthrough`
- original: Be careful with combination cold or nighttime products, which may contain antihistamines or other sedating ingredients that do interact with cyclobenzaprine.

**L146.2** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: 1

## Flexeril and other brand names

**L149.0** `Compound Sentence` (0.812) → `decomposed`
- original: Flexeril was the original brand name for cyclobenzaprine and remains the name many people know it by.
- pronoun resolved: Flexeril was the original brand name for cyclobenzaprine and remains the name many people know Flexeril by.
  - edits: “it” → “Flexeril”
  - S1: Flexeril was the original brand name for cyclobenzaprine.
  - S2: It remains the name many people know Flexeril by.

**L149.1** `Compound-Complex Sentence` (0.9) → `decomposed`
- original: The Flexeril brand has been discontinued and is no longer on the marke t, but this was a commercial decision, not a safety withdrawal: generic cyclobenzaprine tablets containing the same active ingredient remain widely available and inexpensive.
- pronoun resolved: The Flexeril brand has been discontinued and is no longer on the marke t, but Flexeril was a commercial decision, not a safety withdrawal: generic cyclobenzaprine tablets containing the same active ingredient remain widely available and inexpensive.
  - edits: “this” → “Flexeril”
  - S1: The Flexeril brand has been discontinued.
  - S2: The Flexeril brand is no longer on the market.
  - S3: Flexeril was a commercial decision.
  - S4: Flexeril was not a safety withdrawal.
  - S5: Generic cyclobenzaprine tablets contain the same active ingredient.
  - S6: Generic cyclobenzaprine tablets remain widely available.
  - S7: Generic cyclobenzaprine tablets are inexpensive.

**L149.2** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: 4

**L150.0** `Compound Sentence` (0.686) → `decomposed`
- original: Current brand names include Amrix (15 mg and 30 mg extended-release capsules taken once daily), Fexmid (7.5 mg tablets), and Tonmya (2.8 mg sublingual tablets for fibromyalgia, approved August 2025).
  - S1: Current brand names include Amrix (15 mg and 30 mg extended-release capsules taken once daily).
  - S2: Current brand names include Fexmid (7.5 mg tablets).
  - S3: Current brand names include Tonmya (2.8 mg sublingual tablets for fibromyalgia, approved August 2025).

**L150.1** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: 2,3

## Popular FAQ

**L153.0** `Incomplete Sentence` (0.658) → `excluded_incomplete`
- original: Q: Does cyclobenzaprine make you sleepy?

**L153.1** `Compound Sentence` (0.936) → `decomposed`
- original: A: Yes, cyclobenzaprine can make you very sleepy and this side effect may get worse with higher doses.
  - S1: Yes, cyclobenzaprine can make you very sleepy.
  - S2: This side effect may get worse with higher doses.

**L153.2** `Simple Sentence` (0.826) → `passthrough`
- original: Drowsiness is the most commonly reported side effect in studies, occurring in up to 38% (38 out of 100) of people.

**L153.3** `Simple Sentence` (0.978) → `passthrough`
- original: Fatigue and dizziness may also occur.

**L153.4** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Avoid or limit the use of alcohol or other sedating medicines while being treated with cyclobenzaprine.

**L153.5** `Incomplete Sentence` (0.903) → `excluded_incomplete`
- original: Also avoid driving, operating machinery, or other hazardous activities until you know how cyclobenzaprine affects you.

**L154.0** `Incomplete Sentence` (0.919) → `excluded_incomplete`
- original: Q: How long does it take for cyclobenzaprine to work?

**L154.1** `Simple Sentence` (0.633) → `passthrough`
- original: A: Immediate-release cyclobenzaprine tablets work in about 30 to 60 minutes to start relieving your muscle spasm pain.

**L154.2** `Compound Sentence` (0.92) → `decomposed`
- original: Its duration of action is 4 to 6 hours and it is typically given 3 times per day.
- pronoun resolved: Its duration of action is 4 to 6 hours and cyclobenzaprine is typically given 3 times per day.
  - edits: “it” → “cyclobenzaprine”
  - S1: Its duration of action is 4 to 6 hours.
  - S2: Cyclobenzaprine is typically given 3 times per day.

**L154.3** `Simple Sentence` (0.972) → `passthrough`
- original: It may take up to 7 days for you to see the full therapeutical effect.
- pronoun resolved: Cyclobenzaprine may take up to 7 days for you to see the full therapeutical effect.
  - edits: “It” → “Cyclobenzaprine”

**L154.4** `Compound Sentence` (0.57) → `decomposed`
- original: The extended-release cyclobenzaprine capsules (brand name: Amrix) are usually given once per day but may take longer to start working.
  - S1: The extended-release cyclobenzaprine capsules (brand name: Amrix) are usually given once per day.
  - S2: They may take longer to start working.

**L154.5** `Simple Sentence` (0.985) → `passthrough`
- original: Cyclobenzaprine use for periods longer than 2 or 3 weeks is not recommended.

**L155.0** `Incomplete Sentence` (0.67) → `excluded_incomplete`
- original: Q: How much cyclobenzaprine can I take?

**L155.1** `Complex Sentence` (0.45) → `decomposed`
- original: A: For most adults, immediate-release cyclobenzaprine is taken as 5 mg three times daily and may be increased to 10 mg three times daily.
  - S1: Immediate-release cyclobenzaprine is taken as 5 mg three times daily for most adults.
  - S2: The dosage may be increased to 10 mg three times daily.

**L155.2** `Compound Sentence` (0.753) → `decomposed`
- original: Extended-release cyclobenzaprine (Amrix) is usually 15 mg once daily and may be increased to 30 mg. Tonmya for fibromyalgia has a maximum recommended dose of 5.6 mg nightly, and 2.8 mg daily for older adults or people with liver disease.
  - S1: Extended-release cyclobenzaprine (Amrix) is usually 15 mg once daily.
  - S2: It may be increased to 30 mg.
  - S3: Tonmya for fibromyalgia has a maximum recommended dose of 5.6 mg nightly.
  - S4: It has a dose of 2.8 mg daily for older adults or people with liver disease.

**L156.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Q: How long does it take for Flexeril to work?

**L156.1** `Compound Sentence` (0.92) → `decomposed`
- original: A: Flexeril (cyclobenzaprine) is a fast-acting medicine and you should start to feel some muscle relaxant effects within 30 minutes to one hour.
  - S1: Flexeril (cyclobenzaprine) is a fast-acting medicine.
  - S2: You should start to feel some muscle relaxant effects within 30 minutes to one hour.

**L156.2** `Simple Sentence` (0.975) → `passthrough`
- original: The full effect can take up to 7 days.

**L156.3** `Compound Sentence` (0.723) → `decomposed`
- original: The drowsy side effect will set in quickly, too, so be sure you are not driving or doing other hazardous activities.
  - S1: The drowsy side effect will set in quickly.
  - S2: You should be sure you are not driving or doing other hazardous activities.

**L157.0** `Incomplete Sentence` (0.958) → `excluded_incomplete`
- original: Q: Is cyclobenzaprine a controlled substance or addictive?

**L157.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: A: No.

**L157.2** `Simple Sentence` (0.68) → `passthrough`
- original: Cyclobenzaprine is not a controlled substance and is not considered addictive.

**L157.3** `Compound Sentence` (0.744) → `decomposed`
- original: Rarely, stopping it suddenly after prolonged use may cause nausea, headache, or malaise, but these symptoms are not signs of addiction.
- pronoun resolved: Rarely, stopping Cyclobenzaprine suddenly after prolonged use may cause nausea, headache, or malaise, but these symptoms are not signs of addiction.
  - edits: “it” → “Cyclobenzaprine”
  - S1: Rarely, stopping Cyclobenzaprine suddenly after prolonged use may cause nausea, headache, or malaise.
  - S2: These symptoms are not signs of addiction.

**L157.4** `Compound Sentence` (0.904) → `decomposed`
- original: Cyclobenzaprine can cause drowsiness and should not be combined with alcohol or other CNS depressants without medical advice.
  - S1: Cyclobenzaprine can cause drowsiness.
  - S2: It should not be combined with alcohol or other CNS depressants without medical advice.

**L158.0** `Incomplete Sentence` (0.853) → `excluded_incomplete`
- original: Q: How long does Flexeril (cyclobenzaprine) stay in your system?

**L158.1** `Simple Sentence` (0.621) → `passthrough`
- original: A: As an estimate, after taking a dose of Flexeril it should be out of your system within 5.5 days to 16.5 days.
- pronoun resolved: A: As an estimate, after taking a dose of Flexeril Flexeril should be out of your system within 5.5 days to 16.5 days.
  - edits: “it” → “Flexeril”

**L159.0** `Simple Sentence` (0.742) → `passthrough`
- original: Q: Can I take cyclobenzaprine and Tylenol together?

**L159.1** `Simple Sentence` (0.964) → `passthrough`
- original: A: Yes, you can take cyclobenzaprine and Tylenol (acetaminophen) together.

**L159.2** `Compound Sentence` (0.742) → `decomposed`
- original: There are no known interactions between these medicines, however this doesn't necessarily mean that no interaction exist.
  - S1: There are no known interactions between these medicines.
  - S2: However, this doesn't necessarily mean that no interaction exists.
