# Spironolactone — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/spironolactone.txt` · 275 sentences · 61 changed by pronoun resolution · 477 sentences sent to EDC

## What is spironolactone?

**L5.0** `Complex Sentence` (0.873) → `decomposed`
- original: Spironolactone is a potassium-sparing diuretic (water pill) used for heart failure, high blood pressure, fluid build-up (edema) caused by liver or kidney disease, and a hormone condition called primary hyperaldosteronism.
  - S1: Spironolactone is a potassium-sparing diuretic.
  - S2: Spironolactone is used for heart failure.
  - S3: Spironolactone is used for high blood pressure.
  - S4: Spironolactone is used for fluid build-up caused by liver or kidney disease.
  - S5: Spironolactone is used for a hormone condition called primary hyperaldosteronism.

**L5.1** `Simple Sentence` (0.927) → `passthrough`
- original: Spironolactone is sometimes prescribed off-label for women with acne or excessive facial hair growth (hirsutism).

**L6.0** `Complex Sentence` (0.953) → `decomposed`
- original: Spironolactone works by blocking a hormone called aldosterone, which causes your body to pass more salt and water in your urine while keeping potassium in.
  - S1: Spironolactone works by blocking a hormone called aldosterone.
  - S2: Aldosterone causes your body to pass more salt and water in your urine.
  - S3: Aldosterone keeps potassium in.

**L6.1** `Compound-Complex Sentence` (0.746) → `decomposed`
- original: This is why it is called potassium-sparing, and it is what makes spironolactone different from most other water pills, which flush potassium out.
- pronoun resolved: This is why Spironolactone is called potassium-sparing, and Spironolactone is what makes spironolactone different from most other water pills, which flush potassium out.
  - edits: “it” → “Spironolactone”; “it” → “Spironolactone”
  - S1: Spironolactone is called potassium-sparing.
  - S2: Spironolactone makes spironolactone different from most other water pills.
  - S3: Most other water pills flush potassium out.

**L7.0** `Complex Sentence` (0.875) → `decomposed`
- original: Spironolactone also blocks androgens such as testosterone from binding to the androgen receptor, which explains several of its side effects, including breast tenderness and breast growth.
- pronoun resolved: Spironolactone also blocks androgens such as testosterone from binding to the androgen receptor, which explains several of Spironolactone's side effects, including breast tenderness and breast growth.
  - edits: “its” → “Spironolactone's”
  - S1: Spironolactone blocks androgens such as testosterone from binding to the androgen receptor.
  - S2: This mechanism explains several of Spironolactone's side effects.
  - S3: These side effects include breast tenderness and breast growth.

**L8.0** `Simple Sentence` (0.989) → `passthrough`
- original: Spironolactone is FDA-approved to treat adults with:

**L9.0** `Incomplete Sentence` (0.973) → `excluded_incomplete`
- original: Heart failure (NYHA Class III-IV) with a reduced ejection fraction to help live longer, reduce swelling, and reduce the need for hospital stays.

**L9.1** `Simple Sentence` (0.984) → `passthrough`
- original: It is taken alongside other heart failure medicines rather than on its own.
- pronoun resolved: Spironolactone is taken alongside other heart failure medicines rather than on Spironolactone's own.
  - edits: “It” → “Spironolactone”; “its” → “Spironolactone's”

**L10.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: High blood pressure as an add-on treatment for people whose blood pressure is not controlled well enough by other medicines.

**L10.1** `Simple Sentence` (0.975) → `passthrough`
- original: Lowering blood pressure reduces the risk of stroke and heart attack.

**L11.0** `Compound-Complex Sentence` (0.847) → `decomposed`
- original: Fluid build-up (edema) caused by cirrhosis of the liver when cutting back on fluid and salt has not been enough, and also for swelling caused by nephrotic syndrome (a kidney disorder) when treating the underlying disease and using other water pills have not worked well enough.
  - S1: Fluid build-up (edema) caused by cirrhosis of the liver has occurred.
  - S2: Cutting back on fluid and salt has not been enough to treat this edema.
  - S3: Swelling caused by nephrotic syndrome (a kidney disorder) has occurred.
  - S4: Treating the underlying disease has not worked well enough to treat this swelling.
  - S5: Using other water pills has not worked well enough to treat this swelling.

**L12.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Primary hyperaldosteronism, which is a condition where the adrenal glands make too much aldosterone.

**L12.1** `Compound Sentence` (0.87) → `decomposed`
- original: Spironolactone is used short-term to prepare for surgery, and long-term for people who are not suitable for surgery.
  - S1: Spironolactone is used short-term to prepare for surgery.
  - S2: It is used long-term for people who are not suitable for surgery.

**L13.0** `Simple Sentence` (0.98) → `passthrough`
- original: Spironolactone tablets come in 25 mg, 50 mg, and 100 mg strengths.

**L13.1** `Simple Sentence` (0.982) → `passthrough`
- original: Spironolactone 25 mg is the strength most often used to start treatment.

**L13.2** `Simple Sentence` (0.737) → `passthrough`
- original: There is also a banana-flavored oral liquid for people who cannot swallow tablets.

**L13.3** `Compound Sentence` (0.916) → `decomposed`
- original: The liquid and the tablets are not interchangeable, so never switch between them without your doctor changing your dose.
- pronoun resolved: The liquid and the tablets are not interchangeable, so never switch between the liquid and the tablets without your doctor changing your dose.
  - edits: “them” → “the liquid and the tablets”
  - S1: The liquid and the tablets are not interchangeable.
  - S2: Never switch between the liquid and the tablets without your doctor changing your dose.

## Spironolactone side effects

**L16.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Reported spironolactone side effects:

**L17.0** `Complex Sentence` (0.76) → `decomposed` · repaired
- original: Reported spironolactone side effects include breast and nipple pain in both men and women, a lower sex drive, trouble getting or keeping an erection, irregular or missed periods, bleeding after menopause, dizziness, headache, drowsiness, feeling sluggish, leg cramps, nausea, vomiting, diarrhea, stomach cramps, indigestion, hair thinning, and itching.
  - S1: Reported spironolactone side effects include breast and nipple pain in both men and women.
  - S2: Reported spironolactone side effects include a lower sex drive.
  - S3: Reported spironolactone side effects include trouble getting or keeping an erection.
  - S4: Reported spironolactone side effects include irregular or missed periods.
  - S5: Reported spironolactone side effects include bleeding after menopause.
  - S6: Reported spironolactone side effects include dizziness.
  - S7: Reported spironolactone side effects include headache.
  - S8: Reported spironolactone side effects include drowsiness.
  - S9: Reported spironolactone side effects include feeling sluggish.
  - S10: Reported spironolactone side effects include leg cramps.
  - S11: Reported spironolactone side effects include nausea.
  - S12: Reported spironolactone side effects include vomiting.
  - S13: Reported spironolactone side effects include diarrhea.
  - S14: Reported spironolactone side effects include stomach cramps.
  - S15: Reported spironolactone side effects include indigestion.
  - S16: Reported spironolactone side effects include hair thinning.
  - S17: Reported spironolactone side effects include itching.

**L18.0** `Simple Sentence` (0.447) → `passthrough`
- original: The most common side effect of spironolactone is breast growth in men, known as gynecomastia.

**L18.1** `Simple Sentence` (0.872) → `passthrough`
- original: In the main heart failure study, about 9 in 100 men taking an average of 26 mg a day developed it.

**L18.2** `Simple Sentence` (0.973) → `passthrough`
- original: The chance goes up on higher doses.

**L18.3** `Compound Sentence` (0.969) → `decomposed`
- original: It can start anywhere from one or two months into treatment to more than a year later, and it usually goes away after the medicine is stopped.
- pronoun resolved: It can start anywhere from one or two months into treatment to more than a year later, and breast growth usually goes away after the medicine is stopped.
  - edits: “it” → “breast growth”
  - S1: It can start anywhere from one or two months into treatment to more than a year later.
  - S2: Breast growth usually goes away after the medicine is stopped.

**L19.0** `Compound-Complex Sentence` (0.769) → `decomposed`
- original: Several of these effects are dose-related, so they are more likely on higher doses, and many settle after the dose is lowered or the medicine is stopped.
- pronoun resolved: Several of these effects are dose-related, so these effects are more likely on higher doses, and many settle after the dose is lowered or the medicine is stopped.
  - edits: “they” → “these effects”
  - S1: Several of these effects are dose-related.
  - S2: These effects are more likely on higher doses.
  - S3: Many of these effects settle after the dose is lowered.
  - S4: Many of these effects settle after the medicine is stopped.

**L19.1** `Complex Sentence` (0.784) → `decomposed`
- original: How often most of them happen is not known, because they come from reports gathered after the medicine was approved rather than from counted numbers in trials.
- pronoun resolved: How often most of these effects happen is not known, because these effects come from reports gathered after the medicine was approved rather than from counted numbers in trials.
  - edits: “them” → “these effects”; “they” → “these effects”
  - S1: How often most of these effects happen is not known.
  - S2: This is because these effects come from reports gathered after the medicine was approved.
  - S3: They do not come from counted numbers in trials.

**L20.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious spironolactone side effects:

**L21.0** `Compound Sentence` (0.417) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to spironolactone: hives, difficulty breathing, or swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to spironolactone.
  - S2: These signs include hives.
  - S3: These signs include difficulty breathing.
  - S4: These signs include swelling of your face, lips, tongue, or throat.

**L22.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L23.0** `Incomplete Sentence` (0.711) → `excluded_incomplete`
- original: signs of a high potassium level (hyperkalemia), such as muscle weakness or a heavy feeling in your legs, a slow or uneven heartbeat, numbness or tingling in your hands, feet, or lips, nausea, or feeling restless and on edge;

**L24.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: a light-headed feeling like you might pass out, which can be a sign you have low blood pressure (hypotension)

**L25.0** `Incomplete Sentence` (0.747) → `excluded_incomplete`
- original: little or no urination, or swelling in your ankles, hands, or feet, which can be signs your kidneys are struggling (worsening renal function);

**L26.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: signs of a low sodium level, such as confusion, severe weakness, muscle pain or cramps, feeling unsteady, or slurred speech;

**L27.0** `Incomplete Sentence` (0.952) → `excluded_incomplete`
- original: severe or ongoing vomiting or diarrhea, since losing too much fluid and salt can send your blood pressure and kidney function the wrong way;

**L28.0** `Compound-Complex Sentence` (0.633) → `decomposed`
- original: a skin rash that spreads or blisters, peeling skin, sores in your mouth, or a rash with a fever and swollen glands, which can be signs of a rare but serious skin reaction;
  - S1: A skin rash spreads.
  - S2: A skin rash blisters.
  - S3: Skin peels.
  - S4: Sores form in your mouth.
  - S5: A rash appears with a fever.
  - S6: Glands swell.
  - S7: These symptoms can be signs of a rare but serious skin reaction.

**L29.0** `Incomplete Sentence` (0.974) → `excluded_incomplete`
- original: yellowing of your eyes or skin, dark urine, or pain in your upper stomach, which can be signs of a liver problem;

**L30.0** `Incomplete Sentence` (0.951) → `excluded_incomplete`
- original: a fever, sore throat, or unusual bruising or bleeding, which can be signs of a problem with your blood cells; or

**L31.0** `Incomplete Sentence` (0.768) → `excluded_incomplete`
- original: new confusion, unsteadiness, or extreme drowsiness if you have liver disease, since spironolactone can make brain function worse in people with cirrhosis.

**L32.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Spironolactone side effects in men:

**L33.0** `Simple Sentence` (0.973) → `passthrough`
- original: Men are most likely to notice effects linked to spironolactone blocking male hormones.

**L33.1** `Compound Sentence` (0.704) → `decomposed`
- original: These include breast growth and breast tenderness, a lower sex drive, and difficulty getting or keeping an erection.
- pronoun resolved: Side effects include breast growth and breast tenderness, a lower sex drive, and difficulty getting or keeping an erection.
  - edits: “These” → “Side effects”
  - S1: Side effects include breast growth and breast tenderness.
  - S2: Side effects include a lower sex drive.
  - S3: Side effects include difficulty getting or keeping an erection.

**L33.2** `Compound-Complex Sentence` (0.848) → `decomposed`
- original: Breast growth is dose related, so tell your doctor early rather than waiting, since a lower dose or a different medicine may be an option.
  - S1: Breast growth is dose related.
  - S2: Tell your doctor early.
  - S3: Do not wait.
  - S4: A lower dose may be an option.
  - S5: A different medicine may be an option.

**L34.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Spironolactone side effects in women:

**L35.0** `Simple Sentence` (0.752) → `passthrough`
- original: Women may notice irregular periods, missed periods, breast tenderness, or bleeding after menopause.

**L35.1** `Simple Sentence` (0.958) → `passthrough`
- original: Some women also notice patchy darkening of the skin on the face.

**L35.2** `Incomplete Sentence` (0.422) → `excluded_incomplete`
- original: Report any unexpected bleeding after menopause to your doctor so it can be checked properly rather than assumed to be a side effect.
- pronoun resolved: Report any unexpected bleeding after menopause to your doctor so bleeding can be checked properly rather than assumed to be a side effect.
  - edits: “it” → “bleeding”

**L36.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Long-term spironolactone side effects:

**L37.0** `Simple Sentence` (0.979) → `passthrough`
- original: The main long-term concerns with spironolactone are chemical rather than something you would feel.

**L37.1** `Compound-Complex Sentence` (0.883) → `decomposed`
- original: Over time it can push your potassium too high, and it can also lower your sodium, magnesium, and calcium, raise your blood sugar, and raise your uric acid, which occasionally brings on gout.
- pronoun resolved: Over time spironolactone can push your potassium too high, and spironolactone can also lower your sodium, magnesium, and calcium, raise your blood sugar, and raise your uric acid, which occasionally brings on gout.
  - edits: “it” → “spironolactone”; “it” → “spironolactone”
  - S1: Over time, spironolactone can push your potassium too high.
  - S2: Spironolactone can lower your sodium.
  - S3: Spironolactone can lower your magnesium.
  - S4: Spironolactone can lower your calcium.
  - S5: Spironolactone can raise your blood sugar.
  - S6: Spironolactone can raise your uric acid.
  - S7: High uric acid occasionally brings on gout.

**L37.2** `Simple Sentence` (0.552) → `passthrough`
- original: This is why you need regular blood tests for as long as you take it, not just at the start.

**L38.0** `Complex Sentence` (0.691) → `decomposed`
- original: In animal studies, spironolactone given at high doses over long periods caused tumors in rats, mainly in hormone-producing glands and the liver.
  - S1: In animal studies, spironolactone given at high doses over long periods caused tumors in rats.
  - S2: The tumors were mainly in hormone-producing glands and the liver.

**L38.1** `Compound Sentence` (0.751) → `decomposed`
- original: No increase in tumors was seen at the lower doses tested, which were still around five times the highest recommended human dose when adjusted for body size.
  - S1: No increase in tumors was seen at the lower doses tested.
  - S2: These doses were still around five times the highest recommended human dose when adjusted for body size.

**L38.2** `Simple Sentence` (0.962) → `passthrough`
- original: Whether this happens in people is not known.

**L39.0** `Compound Sentence` (0.545) → `decomposed`
- original: This is not a complete list of side effects, and others may occur.
  - S1: This is not a complete list of side effects.
  - S2: Others may occur.

**L39.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L39.2** `Simple Sentence` (0.97) → `passthrough`
- original: You may report side effects to the FDA at 1-800-FDA-1088.

## Warnings

**L42.0** `Compound Sentence` (0.624) → `decomposed`
- original: Do not take spironolactone if you have a high potassium level in your blood, if you have Addison's disease (an adrenal gland disorder), or if you are taking eplerenone (Inspra), another medicine of the same type.
  - S1: Do not take spironolactone if you have a high potassium level in your blood.
  - S2: Do not take spironolactone if you have Addison's disease (an adrenal gland disorder).
  - S3: Do not take spironolactone if you are taking eplerenone (Inspra), another medicine of the same type.

**L43.0** `Simple Sentence` (0.991) → `passthrough`
- original: Spironolactone can raise your potassium to a dangerous level.

**L43.1** `Compound Sentence` (0.79) → `decomposed`
- original: A high potassium level can cause a life-threatening change in your heart rhythm, and it often causes no symptoms until it is already high.
- pronoun resolved: A high potassium level can cause a life-threatening change in your heart rhythm, and A high potassium level often causes no symptoms until A high potassium level is already high.
  - edits: “it” → “A high potassium level”; “it” → “A high potassium level”
  - S1: A high potassium level can cause a life-threatening change in your heart rhythm.
  - S2: A high potassium level often causes no symptoms until A high potassium level is already high.

**L43.2** `Compound Sentence` (0.681) → `decomposed`
- original: Your doctor should check your potassium with a blood test within a week of you starting spironolactone or having your dose changed, and regularly after that.
  - S1: Your doctor should check your potassium with a blood test within a week of you starting spironolactone or having your dose changed.
  - S2: Your doctor should check your potassium regularly after that.

**L44.0** `Compound-Complex Sentence` (0.567) → `decomposed`
- original: Your risk of high potassium is greater if your kidneys do not work well, if you take potassium supplements or a salt substitute containing potassium, or if you take an ACE inhibitor, an ARB, an NSAID, heparin, or trimethoprim.
  - S1: Your risk of high potassium is greater if your kidneys do not work well.
  - S2: Your risk of high potassium is greater if you take potassium supplements.
  - S3: Your risk of high potassium is greater if you take a salt substitute containing potassium.
  - S4: Your risk of high potassium is greater if you take an ACE inhibitor.
  - S5: Your risk of high potassium is greater if you take an ARB.
  - S6: Your risk of high potassium is greater if you take an NSAID.
  - S7: Your risk of high potassium is greater if you take heparin.
  - S8: Your risk of high potassium is greater if you take trimethoprim.

**L45.0** `Incomplete Sentence` (0.756) → `excluded_incomplete`
- original: Do not use potassium supplements or salt substitutes containing potassium unless your doctor has specifically told you to.

**L46.0** `Complex Sentence` (0.85) → `decomposed`
- original: Passing too much fluid can drop your blood pressure and make your kidney function worse, especially if you are also taking an ACE inhibitor or an ARB.
  - S1: Passing too much fluid can drop your blood pressure.
  - S2: Passing too much fluid can make your kidney function worse.
  - S3: This effect is especially true if you are also taking an ACE inhibitor or an ARB.

**L46.1** `Incomplete Sentence` (0.475) → `excluded_incomplete`
- original: Tell your doctor if you feel faint, or if you become unwell with vomiting or diarrhea.

**L47.0** `Complex Sentence` (0.925) → `decomposed`
- original: If you have cirrhosis with fluid in your abdomen, spironolactone is usually started in hospital, because sudden shifts in fluid and salt can affect how your brain works.
  - S1: If you have cirrhosis with fluid in your abdomen, spironolactone is usually started in hospital.
  - S2: Sudden shifts in fluid and salt can affect how your brain works.
  - S3: Spironolactone is started in hospital because sudden shifts in fluid and salt can affect how your brain works.

**L48.0** `Complex Sentence` (0.93) → `decomposed`
- original: Spironolactone should be avoided in pregnancy where possible, because it blocks male hormones and may affect how a male baby develops.
- pronoun resolved: Spironolactone should be avoided in pregnancy where possible, because Spironolactone blocks male hormones and may affect how a male baby develops.
  - edits: “it” → “Spironolactone”
  - S1: Spironolactone should be avoided in pregnancy where possible.
  - S2: Spironolactone blocks male hormones.
  - S3: Spironolactone may affect how a male baby develops.

## Before taking this medicine

**L51.0** `Simple Sentence` (0.898) → `passthrough`
- original: You should not use spironolactone if you are allergic to it, or if you have:
- pronoun resolved: You should not use spironolactone if you are allergic to spironolactone, or if you have:
  - edits: “it,” → “spironolactone,”

**L52.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a high level of potassium in your blood (hyperkalemia);

**L53.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Addison's disease (an adrenal gland disorder); or

**L54.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: if you are taking eplerenone.

**L55.0** `Simple Sentence` (0.776) → `passthrough`
- original: To make sure spironolactone is safe for you, tell your doctor if you have or have ever had:

**L56.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: kidney disease, or reduced kidney function;

**L57.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: liver disease, especially cirrhosis or fluid in the abdomen (ascites);

**L58.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: an electrolyte imbalance, such as a low sodium, magnesium, or calcium level;

**L59.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: dehydration, or any illness causing vomiting or diarrhea;

**L60.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: diabetes, since spironolactone can raise blood sugar;

**L61.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: gout or a high uric acid level; or

**L62.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: prostate cancer treated with abiraterone.

**L63.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Pregnancy:

**L64.0** `Compound Sentence` (0.965) → `decomposed`
- original: Spironolactone blocks the effect of male hormones, and male hormones are needed for a male baby to develop normally.
  - S1: Spironolactone blocks the effect of male hormones.
  - S2: Male hormones are needed for a male baby to develop normally.

**L64.1** `Simple Sentence` (0.98) → `passthrough`
- original: In animal studies, male offspring exposed in the womb showed feminized development.

**L64.2** `Compound Sentence` (0.856) → `decomposed`
- original: The limited information available in humans has not shown a clear increase in birth defects, but the concern remains.
  - S1: The limited information available in humans has not shown a clear increase in birth defects.
  - S2: The concern remains.

**L64.3** `Compound Sentence` (0.768) → `decomposed`
- original: Your doctor will usually avoid spironolactone in pregnancy, or talk through the possible risk to a male baby with you.
  - S1: Your doctor will usually avoid spironolactone in pregnancy.
  - S2: Your doctor will talk through the possible risk to a male baby with you.

**L64.4** `Compound Sentence` (0.684) → `decomposed`
- original: Untreated heart failure, cirrhosis, and high blood pressure also carry real risks in pregnancy, so this is a decision to make with your doctor rather than by stopping on your own.
  - S1: Untreated heart failure, cirrhosis, and high blood pressure also carry real risks in pregnancy.
  - S2: This is a decision to make with your doctor rather than by stopping on your own.

**L65.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Breastfeeding:

**L66.0** `Simple Sentence` (0.98) → `passthrough`
- original: Spironolactone itself does not pass into breast milk.
- pronoun resolved: Spironolactone Spironolactone does not pass into breast milk.
  - edits: “itself” → “Spironolactone”

**L66.1** `Complex Sentence` (0.888) → `decomposed`
- original: Its active breakdown product, canrenone, has been found in breast milk in very small amounts that are not expected to affect a breastfed baby.
- pronoun resolved: Spironolactone's active breakdown product, canrenone, has been found in breast milk in very small amounts that are not expected to affect a breastfed baby.
  - edits: “Its” → “Spironolactone's”
  - S1: Spironolactone's active breakdown product is canrenone.
  - S2: Canrenone has been found in breast milk.
  - S3: The amounts found are very small.
  - S4: These amounts are not expected to affect a breastfed baby.

**L66.2** `Compound Sentence` (0.97) → `decomposed`
- original: No side effects were reported in the one infant studied over a short period, and the long-term picture is not known.
  - S1: No side effects were reported in the one infant studied over a short period.
  - S2: The long-term picture is not known.

**L66.3** `Incomplete Sentence` (0.957) → `excluded_incomplete`
- original: Talk to your doctor so you can weigh this up together.

**L67.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Children:

**L68.0** `Simple Sentence` (0.967) → `passthrough`
- original: Spironolactone has not been shown to be safe and effective in children.

**L68.1** `Complex Sentence` (0.842) → `decomposed`
- original: The oral liquid is specifically not recommended for treating high blood pressure in children, because of the hormonal effects of the medicine.
  - S1: The oral liquid is specifically not recommended for treating high blood pressure in children.
  - S2: This is because of the hormonal effects of the medicine.

**L68.2** `Simple Sentence` (0.937) → `passthrough`
- original: Any use in a child must be decided and monitored by a specialist.

**L69.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Older adults:

**L70.0** `Compound Sentence` (0.968) → `decomposed`
- original: Spironolactone is cleared by the kidneys, and kidney function tends to fall with age.
  - S1: Spironolactone is cleared by the kidneys.
  - S2: Kidney function tends to fall with age.

**L70.1** `Compound Sentence` (0.82) → `decomposed`
- original: Older adults are therefore more likely to build up a high potassium level, so kidney function and potassium need monitoring.
  - S1: Older adults are therefore more likely to build up a high potassium level.
  - S2: Kidney function and potassium need monitoring.

## How should I take spironolactone?

**L73.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Take spironolactone exactly as prescribed.

**L73.1** `Incomplete Sentence` (0.823) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides.

**L74.0** `Incomplete Sentence` (0.969) → `excluded_incomplete`
- original: Take it the same way each day, either always with food or always without.
- pronoun resolved: Take spironolactone the same way each day, either always with food or always without.
  - edits: “it” → “spironolactone”

**L74.1** `Compound Sentence` (0.569) → `decomposed`
- original: Food increases how much spironolactone your body absorbs, roughly doubling it, so switching back and forth changes how much medicine you actually get.
- pronoun resolved: Food increases how much spironolactone your body absorbs, roughly doubling spironolactone, so switching back and forth changes how much medicine you actually get.
  - edits: “it,” → “spironolactone,”
  - S1: Food increases how much spironolactone your body absorbs.
  - S2: This roughly doubles spironolactone absorption.
  - S3: Switching back and forth changes how much medicine you actually get.

**L75.0** `Compound Sentence` (0.798) → `decomposed`
- original: Shake the oral liquid well before every dose, and measure it with the marked oral syringe, dosing spoon, or medicine cup that comes with it, not a kitchen spoon.
- pronoun resolved: Shake the oral liquid well before every dose, and measure oral liquid with the marked oral syringe, dosing spoon, or medicine cup that comes with oral liquid, not a kitchen spoon.
  - edits: “it” → “oral liquid”; “it,” → “oral liquid,”
  - S1: Shake the oral liquid well before every dose.
  - S2: Measure oral liquid with the marked oral syringe, dosing spoon, or medicine cup that comes with oral liquid.
  - S3: Do not use a kitchen spoon.

**L76.0** `Simple Sentence` (0.852) → `passthrough`
- original: Do not switch between tablets and the oral liquid without your doctor changing the dose.

**L76.1** `Compound Sentence` (0.927) → `decomposed`
- original: They are not interchangeable, and the liquid gives a higher level of medicine in your blood for the same number of milligrams.
  - S1: They are not interchangeable.
  - S2: The liquid gives a higher level of medicine in your blood for the same number of milligrams.

**L77.0** `Simple Sentence` (0.428) → `passthrough`
- original: You will need regular blood tests to check your potassium, sodium, kidney function, uric acid, and blood sugar.

**L77.1** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: Keep these appointments even if you feel completely well.

**L78.0** `Simple Sentence` (0.672) → `passthrough`
- original: If you are being treated for high blood pressure, keep taking spironolactone even when you feel fine.

**L78.1** `Simple Sentence` (0.986) → `passthrough`
- original: High blood pressure usually has no symptoms.

**L79.0** `Compound Sentence` (0.644) → `decomposed`
- original: Tell any doctor or dentist treating you that you take spironolactone, and tell your surgeon before any operation.
  - S1: Tell any doctor or dentist treating you that you take spironolactone.
  - S2: Tell your surgeon before any operation.

**L80.0** `Compound Sentence` (0.613) → `decomposed`
- original: Spironolactone can interfere with one type of blood test used to measure digoxin, so mention it if you take digoxin.
- pronoun resolved: Spironolactone can interfere with one type of blood test used to measure digoxin, so mention digoxin if you take digoxin.
  - edits: “it” → “digoxin”
  - S1: Spironolactone can interfere with one type of blood test used to measure digoxin.
  - S2: You should mention digoxin if you take digoxin.

**L81.0** `Incomplete Sentence` (0.92) → `excluded_incomplete`
- original: Do not share this medicine with anyone else.

**L82.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Store tablets at room temperature, 68°F to 77°F (20°C to 25°C), and protect them from light.

**L82.1** `Incomplete Sentence` (0.819) → `excluded_incomplete`
- original: Store the oral liquid at room temperature and keep it in a tightly closed bottle.
- pronoun resolved: Store the oral liquid at room temperature and keep oral liquid in a tightly closed bottle.
  - edits: “it” → “oral liquid”

## What is the usual spironolactone dosage?

**L85.0** `Compound Sentence` (0.46) → `decomposed`
- original: The usual starting dose of spironolactone tablets for adults is 25 mg to 100 mg a day, depending on the condition being treated.
  - S1: The usual starting dose of spironolactone tablets for adults is 25 mg to 100 mg a day.
  - S2: This dose depends on the condition being treated.

**L85.1** `Compound Sentence` (0.496) → `decomposed`
- original: Your doctor will pick a starting dose and then adjust it based on your blood tests and how you respond.
- pronoun resolved: Your doctor will pick a starting dose and then adjust dose based on your blood tests and how you respond.
  - edits: “it” → “dose”
  - S1: Your doctor will pick a starting dose.
  - S2: Then, the doctor will adjust the dose based on your blood tests and how you respond.

**L86.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Spironolactone dosage for heart failure:

**L87.0** `Compound Sentence` (0.505) → `decomposed`
- original: Treatment starts at spironolactone 25 mg once a day, provided your potassium level is 5.0 mEq/L or lower and your kidney function (eGFR) is above 50.
  - S1: Treatment starts at spironolactone 25 mg once a day.
  - S2: This is provided your potassium level is 5.0 mEq/L or lower and your kidney function (eGFR) is above 50.

**L87.1** `Simple Sentence` (0.851) → `passthrough`
- original: If you tolerate that, the dose may go up to 50 mg once a day.

**L87.2** `Compound Sentence` (0.595) → `decomposed`
- original: If your potassium rises too high, the dose may drop to 25 mg every other day.
  - S1: If your potassium rises too high.
  - S2: The dose may drop to 25 mg every other day.

**L87.3** `Complex Sentence` (0.895) → `decomposed`
- original: If your eGFR is between 30 and 50, your doctor may start you at 25 mg every other day because of the higher risk of high potassium.
  - S1: If your eGFR is between 30 and 50, your doctor may start you at 25 mg every other day.
  - S2: This is because of the higher risk of high potassium.

**L88.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Spironolactone dosage for high blood pressure:

**L89.0** `Simple Sentence` (0.436) → `passthrough`
- original: The usual starting dose is spironolactone 25 mg to 100 mg a day, taken as one dose or split into two.

**L89.1** `Simple Sentence` (0.983) → `passthrough`
- original: The dose can be adjusted every two weeks.

**L89.2** `Simple Sentence` (0.979) → `passthrough`
- original: Doses above 100 mg a day do not generally lower blood pressure any further.

**L90.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Spironolactone dosage for fluid build-up (edema):

**L91.0** `Compound Sentence` (0.961) → `decomposed`
- original: The usual starting dose is 100 mg a day, taken as one dose or split into two, and the dose can range from 25 mg to 200 mg a day.
  - S1: The usual starting dose is 100 mg a day.
  - S2: It is taken as one dose or split into two.
  - S3: The dose can range from 25 mg to 200 mg a day.

**L91.1** `Simple Sentence` (0.795) → `passthrough`
- original: If you have cirrhosis, treatment is started in hospital and increased slowly.

**L91.2** `Complex Sentence` (0.879) → `decomposed`
- original: When spironolactone is the only water pill being used, it is given for at least five days before the dose is increased.
- pronoun resolved: When spironolactone is the only water pill being used, spironolactone is given for at least five days before the dose is increased.
  - edits: “it” → “spironolactone”
  - S1: Spironolactone is given for at least five days.
  - S2: The dose is increased after five days.
  - S3: This applies when spironolactone is the only water pill being used.

**L92.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Spironolactone dosage for primary hyperaldosteronism:

**L93.0** `Simple Sentence` (0.983) → `passthrough`
- original: The dose is 100 mg to 400 mg a day when preparing for surger y.

**L93.1** `Complex Sentence` (0.442) → `decomposed`
- original: For people who are not suitable for surgery, the lowest dose that works is used long term.
  - S1: The lowest dose that works is used long term.
  - S2: This is for people who are not suitable for surgery.

**L94.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Spironolactone oral liquid doses:

**L95.0** `Simple Sentence` (0.923) → `passthrough`
- original: The oral liquid has its own separate doses because it is absorbed differently.
- pronoun resolved: The oral liquid has its own separate doses because oral liquid is absorbed differently.
  - edits: “it” → “oral liquid”

**L95.1** `Simple Sentence` (0.989) → `passthrough`
- original: Heart failure starts at 20 mg (4 mL) once a day.

**L95.2** `Simple Sentence` (0.987) → `passthrough`
- original: High blood pressure starts at 20 mg (4 mL) to 75 mg (15 mL) a day.

**L95.3** `Simple Sentence` (0.98) → `passthrough`
- original: Swelling from cirrhosis starts at 75 mg (15 mL) a day, begun in hospital.

**L95.4** `Compound Sentence` (0.403) → `decomposed`
- original: If more than 100 mg a day is needed, a different form of the medicine should be used instead.
  - S1: If more than 100 mg a day is needed, a different form of the medicine should be used.
  - S2: Instead, a different form of the medicine should be used.

**L96.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Spironolactone formulations:

**L97.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Spironolactone 25 mg tablets

**L98.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Spironolactone 50 mg tablets

**L99.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Spironolactone 100 mg tablets

**L100.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Spironolactone oral suspension 25 mg per 5 mL

## What happens if I miss a dose?

**L103.0** `Incomplete Sentence` (0.926) → `excluded_incomplete`
- original: Take the missed dose as soon as you remember.

**L103.1** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Skip it if it is almost time for your next dose.
- pronoun resolved: Skip dose if it is almost time for your next dose.
  - edits: “it” → “dose”

**L103.2** `Incomplete Sentence` (0.631) → `excluded_incomplete`
- original: Do not take two doses at once to make up for a missed one.

## What happens if I overdose?

**L106.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L107.0** `Simple Sentence` (0.833) → `passthrough`
- original: Taking too much spironolactone can cause drowsiness, confusion, a rash, nausea, vomiting, dizziness, or diarrhea.

**L107.1** `Complex Sentence` (0.589) → `decomposed`
- original: A dangerously high potassium level is the main serious risk, particularly if your kidneys do not work well.
  - S1: A dangerously high potassium level is the main serious risk.
  - S2: This risk is particularly present if your kidneys do not work well.

## What should I avoid while taking spironolactone?

**L110.0** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Avoid potassium supplements, salt substitutes containing potassium, and low-sodium products that use potassium instead of salt.

**L110.1** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Check labels, since potassium chloride is a common salt replacement.

**L111.0** `Incomplete Sentence` (0.786) → `excluded_incomplete`
- original: Go easy on foods very high in potassium if your doctor has told you to.

**L111.1** `Complex Sentence` (0.58) → `decomposed`
- original: This is worth asking about specifically, because most people are told to eat more potassium, not less.
  - S1: This is worth asking about specifically.
  - S2: Most people are told to eat more potassium.
  - S3: Most people are told not to eat less potassium.

**L112.0** `Incomplete Sentence` (0.821) → `excluded_incomplete`
- original: Be careful with NSAIDs such as ibuprofen and naproxen.

**L112.1** `Compound Sentence` (0.627) → `decomposed`
- original: They can push your potassium up, make spironolactone work less well, and strain your kidneys.
- pronoun resolved: NSAIDs can push your potassium up, make spironolactone work less well, and strain your kidneys.
  - edits: “They” → “NSAIDs”
  - S1: NSAIDs can push your potassium up.
  - S2: NSAIDs can make spironolactone work less well.
  - S3: NSAIDs can strain your kidneys.

**L113.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Limit alcohol.

**L113.1** `Simple Sentence` (0.857) → `passthrough`
- original: It can add to the dizziness and light-headedness, especially when you first start.
- pronoun resolved: Alcohol can add to the dizziness and light-headedness, especially when you first start.
  - edits: “It” → “Alcohol”

**L114.0** `Compound Sentence` (0.529) → `decomposed`
- original: Avoid getting up quickly from sitting or lying down, and avoid driving or anything hazardous until you know how spironolactone affects you.
  - S1: Avoid getting up quickly from sitting or lying down.
  - S2: Avoid driving or anything hazardous until you know how spironolactone affects you.

**L115.0** `Compound Sentence` (0.8) → `decomposed`
- original: Do not take another medicine containing spironolactone at the same time, such as Aldactazide, and do not take eplerenone.
  - S1: Do not take another medicine containing spironolactone at the same time, such as Aldactazide.
  - S2: Do not take eplerenone.

## What other drugs will affect spironolactone?

**L118.0** `Complex Sentence` (0.936) → `decomposed`
- original: The most important interactions with spironolactone are medicines that also raise potassium, because the combined effect can push your level dangerously high.
  - S1: The most important interactions with spironolactone are medicines that also raise potassium.
  - S2: The combined effect of these medicines can push your potassium level dangerously high.

**L118.1** `Incomplete Sentence` (0.877) → `excluded_incomplete`
- original: Tell your doctor about every medicine you take, including anything you start or stop during treatment.

**L118.2** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Be especially careful with:

**L119.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: eplerenone, which should not be taken with spironolactone at all;

**L120.0** `Incomplete Sentence` (0.927) → `excluded_incomplete`
- original: medicines that raise potassium, including ACE inhibitors such as lisinopril and ramipril, ARBs such as losartan and valsartan, NSAIDs, heparin and low molecular weight heparin, and trimethoprim;

**L121.0** `Incomplete Sentence` (0.964) → `excluded_incomplete`
- original: potassium supplements and potassium-containing salt substitutes, which are usually stopped when spironolactone is started for heart failure;

**L122.0** `Compound-Complex Sentence` (0.724) → `decomposed`
- original: lithium, since spironolactone slows how fast your kidneys clear it and can cause lithium toxicity, so lithium levels need monitoring;
- pronoun resolved: lithium, since spironolactone slows how fast your kidneys clear spironolactone and can cause lithium toxicity, so lithium levels need monitoring;
  - edits: “it” → “spironolactone”
  - S1: Spironolactone slows how fast your kidneys clear spironolactone.
  - S2: Spironolactone can cause lithium toxicity.
  - S3: Lithium levels need monitoring.

**L123.0** `Compound-Complex Sentence` (0.84) → `decomposed`
- original: digoxin, which needs care for two separate reasons: spironolactone interferes with one type of blood test used to measure digoxin, and it can also raise the actual amount of digoxin in your body;
- pronoun resolved: digoxin, which needs care for two separate reasons: spironolactone interferes with one type of blood test used to measure digoxin, and spironolactone can also raise the actual amount of digoxin in your body;
  - edits: “it” → “spironolactone”
  - S1: Digoxin needs care for two separate reasons.
  - S2: Spironolactone interferes with one type of blood test used to measure digoxin.
  - S3: Spironolactone can raise the actual amount of digoxin in your body.

**L124.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: NSAIDs, which can also make spironolactone less effective as a water pill and as a blood pressure medicine;

**L125.0** `Incomplete Sentence` (0.937) → `excluded_incomplete`
- original: aspirin, which can reduce how well spironolactone works, so your dose may need adjusting;

**L126.0** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: cholestyramine, which together with spironolactone has caused a high potassium level with too much acid in the blood;

**L127.0** `Incomplete Sentence` (0.672) → `excluded_incomplete`
- original: abiraterone, used in prostate cancer, which should not be combined with spironolactone because spironolactone attaches to the androgen receptor and can raise PSA readings;

**L128.0** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: mitotane, which should be avoided because spironolactone lowers its level in the blood; and
- pronoun resolved: mitotane, which should be avoided because spironolactone lowers spironolactone's level in the blood; and
  - edits: “its” → “spironolactone's”

**L129.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: other blood pressure medicines and water pills, which add to the blood pressure lowering effect.

**L130.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L130.1** `Simple Sentence` (0.876) → `passthrough`
- original: Other prescription and over-the-counter medicines, vitamins, and herbal products can interact with spironolactone.

**L130.2** `Incomplete Sentence` (0.956) → `excluded_incomplete`
- original: Give a list of all your medicines to any healthcare provider who treats you.

## Spironolactone FAQs

**L133.0** `Incomplete Sentence` (0.974) → `excluded_incomplete`
- original: Is spironolactone a diuretic?

**L133.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L134.0** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Yes.

**L134.1** `Compound Sentence` (0.967) → `decomposed`
- original: Spironolactone is a diuretic, or water pill, and it belongs to the group called potassium-sparing diuretics.
- pronoun resolved: Spironolactone is a diuretic, or water pill, and Spironolactone belongs to the group called potassium-sparing diuretics.
  - edits: “it” → “Spironolactone”
  - S1: Spironolactone is a diuretic, or water pill.
  - S2: Spironolactone belongs to the group called potassium-sparing diuretics.

**L134.2** `Simple Sentence` (0.867) → `passthrough`
- original: It works by blocking aldosterone, a hormone that makes your kidneys hold onto salt and water.
- pronoun resolved: Spironolactone works by blocking aldosterone, a hormone that makes your kidneys hold onto salt and water.
  - edits: “It” → “Spironolactone”

**L134.3** `Complex Sentence` (0.852) → `decomposed`
- original: Unlike most water pills, which make you lose potassium, spironolactone makes your body keep potassium in.
  - S1: Unlike most water pills, spironolactone makes your body keep potassium in.
  - S2: Most water pills make you lose potassium.

**L134.4** `Complex Sentence` (0.644) → `decomposed`
- original: It is a weaker diuretic than medicines such as furosemide, which is one reason it is often given alongside another water pill rather than instead of one.
- pronoun resolved: It is a weaker diuretic than medicines such as furosemide, which is one reason spironolactone is often given alongside another water pill rather than instead of one.
  - edits: “it” → “spironolactone”
  - S1: It is a weaker diuretic than medicines such as furosemide.
  - S2: Furosemide is one reason spironolactone is often given alongside another water pill.
  - S3: Spironolactone is often given alongside another water pill rather than instead of one.

**L135.0** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Is spironolactone used for acne?

**L135.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L136.0** `Compound Sentence` (0.951) → `decomposed`
- original: Spironolactone is not approved by the FDA for treating acne, but doctors sometimes prescribe it off-label for hormonal acne in women.
- pronoun resolved: Spironolactone is not approved by the FDA for treating acne, but doctors sometimes prescribe Spironolactone off-label for hormonal acne in women.
  - edits: “it” → “Spironolactone”
  - S1: Spironolactone is not approved by the FDA for treating acne.
  - S2: Doctors sometimes prescribe Spironolactone off-label for hormonal acne in women.

**L136.1** `Compound-Complex Sentence` (0.673) → `decomposed`
- original: Off-label means a doctor is prescribing a medicine for something other than its approved uses, which is legal and common, but it means the FDA has not reviewed the medicine for that purpose.
- pronoun resolved: Off-label means a doctor is prescribing a medicine for something other than its approved uses, which is legal and common, but Off-label means the FDA has not reviewed the medicine for that purpose.
  - edits: “it” → “Off-label”
  - S1: Off-label means a doctor is prescribing a medicine for something other than its approved uses.
  - S2: This practice is legal.
  - S3: This practice is common.
  - S4: Off-label means the FDA has not reviewed the medicine for that purpose.

**L137.0** `Simple Sentence` (0.853) → `passthrough`
- original: The reason it is used this way relates to how spironolactone works.
- pronoun resolved: The reason spironolactone is used this way relates to how spironolactone works.
  - edits: “it” → “spironolactone”

**L137.1** `Complex Sentence` (0.885) → `decomposed`
- original: As well as blocking aldosterone, spironolactone attaches to the androgen receptor, the docking point for male hormones such as testosterone.
  - S1: Spironolactone blocks aldosterone.
  - S2: Spironolactone attaches to the androgen receptor.
  - S3: The androgen receptor is the docking point for male hormones such as testosterone.

**L137.2** `Compound Sentence` (0.965) → `decomposed`
- original: Male hormones increase how much oil the skin produces, and oil production is one factor in acne.
  - S1: Male hormones increase how much oil the skin produces.
  - S2: Oil production is one factor in acne.

**L138.0** `Complex Sentence` (0.924) → `decomposed`
- original: Because acne is not an approved use, there is no FDA-approved dose for it.
  - S1: Acne is not an approved use.
  - S2: There is no FDA-approved dose for it.

**L138.1** `Simple Sentence` (0.963) → `passthrough`
- original: Any dose is chosen by the prescriber.

**L138.2** `Complex Sentence` (0.872) → `decomposed`
- original: Spironolactone is generally avoided in pregnancy because it may affect how a male baby develops, which is an important consideration for anyone taking it for a skin condition rather than a heart or kidney condition.
- pronoun resolved: Spironolactone is generally avoided in pregnancy because Spironolactone may affect how a male baby develops, which is an important consideration for anyone taking Spironolactone for a skin condition rather than a heart or kidney condition.
  - edits: “it” → “Spironolactone”; “it” → “Spironolactone”
  - S1: Spironolactone is generally avoided in pregnancy.
  - S2: Spironolactone may affect how a male baby develops.
  - S3: This is an important consideration for anyone taking Spironolactone for a skin condition rather than a heart or kidney condition.

**L139.0** `Compound-Complex Sentence` (0.724) → `decomposed`
- original: If you are considering spironolactone for acne, this is a conversation to have with a doctor or dermatologist who can review your full medical history, since spironolactone still carries the same risk of raising your potassium level, whatever it is prescribed for.
- pronoun resolved: If you are considering spironolactone for acne, this is a conversation to have with a doctor or dermatologist who can review your full medical history, since spironolactone still carries the same risk of raising your potassium level, whatever spironolactone is prescribed for.
  - edits: “it” → “spironolactone”
  - S1: If you are considering spironolactone for acne, this is a conversation to have with a doctor or dermatologist.
  - S2: A doctor or dermatologist can review your full medical history.
  - S3: Spironolactone still carries the same risk of raising your potassium level.
  - S4: This risk exists regardless of what spironolactone is prescribed for.

**L140.0** `Incomplete Sentence` (0.877) → `excluded_incomplete`
- original: Does spironolactone cause weight gain?

**L140.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L141.0** `Compound Sentence` (0.966) → `decomposed`
- original: Weight gain is not a recognized side effect of spironolactone, and it is not listed in the medicine's official prescribing information.
- pronoun resolved: Weight gain is not a recognized side effect of spironolactone, and spironolactone is not listed in the medicine's official prescribing information.
  - edits: “it” → “spironolactone”
  - S1: Weight gain is not a recognized side effect of spironolactone.
  - S2: Spironolactone is not listed in the medicine's official prescribing information.

**L141.1** `Compound Sentence` (0.888) → `decomposed`
- original: Spironolactone is a diuretic, so it usually causes a small drop in weight in the first week or two as your body sheds extra fluid.
- pronoun resolved: Spironolactone is a diuretic, so Spironolactone usually causes a small drop in weight in the first week or two as your body sheds extra fluid.
  - edits: “it” → “Spironolactone”
  - S1: Spironolactone is a diuretic.
  - S2: Spironolactone usually causes a small drop in weight in the first week or two as your body sheds extra fluid.

**L142.0** `Complex Sentence` (0.693) → `decomposed`
- original: If you are gaining weight while taking it, it is worth telling your doctor rather than assuming the medicine is to blame.
  - S1: You should tell your doctor if you are gaining weight while taking it.
  - S2: It is not worth assuming the medicine is to blame.

**L142.1** `Complex Sentence` (0.736) → `decomposed`
- original: Rapid weight gain with swelling in your ankles or legs or shortness of breath can be a sign of fluid building up, which may mean the condition being treated needs a closer look.
  - S1: Rapid weight gain with swelling in your ankles or legs or shortness of breath can be a sign of fluid building up.
  - S2: This may mean the condition being treated needs a closer look.

**L142.2** `Simple Sentence` (0.867) → `passthrough`
- original: Slower weight gain is more often down to appetite, activity, or another medicine.

**L143.0** `Incomplete Sentence` (0.879) → `excluded_incomplete`
- original: Does spironolactone cause hair loss?

**L143.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L144.0** `Compound Sentence` (0.879) → `decomposed`
- original: Hair thinning, known as alopecia, is listed as a possible side effect of spironolactone, though how often it happens is not known.
- pronoun resolved: Hair thinning, known as alopecia, is listed as a possible side effect of spironolactone, though how often spironolactone happens is not known.
  - edits: “it” → “spironolactone”
  - S1: Hair thinning, known as alopecia, is listed as a possible side effect of spironolactone.
  - S2: How often spironolactone happens is not known.

**L144.1** `Simple Sentence` (0.989) → `passthrough`
- original: It is reported far less often than breast tenderness or breast growth.
- pronoun resolved: Spironolactone is reported far less often than breast tenderness or breast growth.
  - edits: “It” → “Spironolactone”

**L145.0** `Complex Sentence` (0.938) → `decomposed`
- original: The picture is complicated because spironolactone is also prescribed off label for hair loss in women, on the basis that blocking male hormones may help with hormone-related thinning.
  - S1: The picture is complicated.
  - S2: Spironolactone is prescribed off label for hair loss in women.
  - S3: This is based on the idea that blocking male hormones may help with hormone-related thinning.

**L145.1** `Simple Sentence` (0.981) → `passthrough`
- original: Spironolactone is not approved by the FDA for treating hair loss.

**L145.2** `Complex Sentence` (0.521) → `decomposed`
- original: If your hair is thinning while you take it, speak to your doctor, since there are several possible causes worth ruling out.
  - S1: If your hair is thinning while you take it, speak to your doctor.
  - S2: There are several possible causes worth ruling out.

**L146.0** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: How long does it take for spironolactone to work?

**L146.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L147.0** `Simple Sentence` (0.972) → `passthrough`
- original: It depends what you are taking it for.
- pronoun resolved: It depends what you are taking spironolactone for.
  - edits: “it” → “spironolactone”

**L147.1** `Compound-Complex Sentence` (0.886) → `decomposed`
- original: Spironolactone reaches its highest level in your blood in about 2 to 3 hours, and its active breakdown product peaks at around 4 hours, so it starts having an effect on your kidneys the same day.
- pronoun resolved: Spironolactone reaches its highest level in your blood in about 2 to 3 hours, and its active breakdown product peaks at around 4 hours, so spironolactone starts having an effect on your kidneys the same day.
  - edits: “it” → “spironolactone”
  - S1: Spironolactone reaches its highest level in your blood in about 2 to 3 hours.
  - S2: The active breakdown product of spironolactone peaks at around 4 hours.
  - S3: Spironolactone starts having an effect on your kidneys the same day.

**L148.0** `Simple Sentence` (0.899) → `passthrough`
- original: The results you notice take longer.

**L148.1** `Complex Sentence` (0.859) → `decomposed`
- original: For fluid build-up, spironolactone is given for at least five days before the dose is increased, because that is how long the full effect takes to show.
  - S1: For fluid build-up, spironolactone is given for at least five days.
  - S2: The dose is increased after this period.
  - S3: This delay is because the full effect takes that long to show.

**L148.2** `Compound Sentence` (0.933) → `decomposed`
- original: For high blood pressure, the dose is adjusted at two-week intervals, so give it a couple of weeks before judging it.
- pronoun resolved: For high blood pressure, the dose is adjusted at two-week intervals, so give spironolactone a couple of weeks before judging it.
  - edits: “it” → “spironolactone”
  - S1: For high blood pressure, the dose is adjusted at two-week intervals.
  - S2: So, give spironolactone a couple of weeks before judging it.

**L148.3** `Complex Sentence` (0.761) → `decomposed`
- original: For heart failure, the benefit is a lower risk of being admitted to hospital and living longer, which is not something you feel week to week.
  - S1: For heart failure, the benefit is a lower risk of being admitted to hospital and living longer.
  - S2: This benefit is not something you feel week to week.

**L149.0** `Incomplete Sentence` (0.979) → `excluded_incomplete`
- original: How long does spironolactone stay in your system?

**L149.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L150.0** `Complex Sentence` (0.907) → `decomposed`
- original: Spironolactone itself leaves your blood very quickly, with a half-life of about 1.4 hours, meaning half of it is gone in that time.
- pronoun resolved: Spironolactone Spironolactone leaves your blood very quickly, with a half-life of about 1.4 hours, meaning half of Spironolactone is gone in that time.
  - edits: “itself” → “Spironolactone”; “it” → “Spironolactone”
  - S1: Spironolactone leaves your blood very quickly.
  - S2: It has a half-life of about 1.4 hours.
  - S3: This means half of Spironolactone is gone in that time.

**L150.1** `Simple Sentence` (0.889) → `passthrough`
- original: Its active breakdown products last much longer, with half-lives of roughly 14 to 17 hours.
- pronoun resolved: Spironolactone's active breakdown products last much longer, with half-lives of roughly 14 to 17 hours.
  - edits: “Its” → “Spironolactone's”

**L150.2** `Compound Sentence` (0.951) → `decomposed`
- original: Because of those, the effect of a dose carries on well after the spironolactone itself has gone, and it takes a few days for the medicine to clear fully after you stop.
- pronoun resolved: Because of half-lives, the effect of a dose carries on well after the spironolactone spironolactone has gone, and it takes a few days for spironolactone to clear fully after you stop.
  - edits: “those,” → “half-lives,”; “itself” → “spironolactone”; “the medicine” → “spironolactone”
  - S1: Because of half-lives, the effect of a dose carries on well after the spironolactone has gone.
  - S2: It takes a few days for spironolactone to clear fully after you stop.

**L150.3** `Simple Sentence` (0.989) → `passthrough`
- original: Clearance is slower if you have cirrhosis.

**L151.0** `Incomplete Sentence` (0.965) → `excluded_incomplete`
- original: Is spironolactone a blood thinner?

**L151.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L152.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: No.

**L152.1** `Simple Sentence` (0.99) → `passthrough`
- original: Spironolactone is not a blood thinner.

**L152.2** `Compound Sentence` (0.951) → `decomposed`
- original: It does not affect blood clotting and it is not used to prevent clots or strokes in the way that warfarin, apixaban, or aspirin are.
- pronoun resolved: Spironolactone does not affect blood clotting and Spironolactone is not used to prevent clots or strokes in the way that warfarin, apixaban, or aspirin are.
  - edits: “It” → “Spironolactone”; “it” → “Spironolactone”
  - S1: Spironolactone does not affect blood clotting.
  - S2: Spironolactone is not used to prevent clots or strokes.
  - S3: Warfarin, apixaban, or aspirin are used to prevent clots or strokes.

**L152.3** `Simple Sentence` (0.708) → `passthrough`
- original: It is a diuretic that lowers blood pressure and reduces fluid build-up.
- pronoun resolved: Spironolactone is a diuretic that lowers blood pressure and reduces fluid build-up.
  - edits: “It” → “Spironolactone”

**L153.0** `Simple Sentence` (0.992) → `passthrough`
- original: Spironolactone does interact with some blood thinners indirectly.

**L153.1** `Compound-Complex Sentence` (0.579) → `decomposed`
- original: Heparin and low molecular weight heparin can raise potassium, so taking them with spironolactone increases the risk of a high potassium level.
- pronoun resolved: Heparin and low molecular weight heparin can raise potassium, so taking Heparin and low molecular weight heparin with spironolactone increases the risk of a high potassium level.
  - edits: “them” → “Heparin and low molecular weight heparin”
  - S1: Heparin can raise potassium.
  - S2: Low molecular weight heparin can raise potassium.
  - S3: Spironolactone can raise potassium.
  - S4: Taking Heparin with spironolactone increases the risk of a high potassium level.
  - S5: Taking low molecular weight heparin with spironolactone increases the risk of a high potassium level.

**L154.0** `Incomplete Sentence` (0.973) → `excluded_incomplete`
- original: Can I stop taking spironolactone suddenly?

**L154.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L155.0** `Compound Sentence` (0.925) → `decomposed`
- original: Spironolactone does not cause withdrawal symptoms and does not need to be tapered the way a steroid does.
  - S1: Spironolactone does not cause withdrawal symptoms.
  - S2: Spironolactone does not need to be tapered the way a steroid does.

**L155.1** `Simple Sentence` (0.893) → `passthrough`
- original: Even so, do not stop it without speaking to your doctor.
- pronoun resolved: Even so, do not stop Spironolactone without speaking to your doctor.
  - edits: “it” → “Spironolactone”

**L155.2** `Compound-Complex Sentence` (0.843) → `decomposed`
- original: Stopping it can allow fluid to build up again, your blood pressure to rise, or your heart failure to worsen, and if you are taking it for heart failure it is one of the medicines shown to help people live longer.
- pronoun resolved: Stopping Spironolactone can allow fluid to build up again, your blood pressure to rise, or your heart failure to worsen, and if you are taking Spironolactone for heart failure Spironolactone is one of the medicines shown to help people live longer.
  - edits: “it” → “Spironolactone”; “it” → “Spironolactone”; “it” → “Spironolactone”
  - S1: Stopping Spironolactone can allow fluid to build up again.
  - S2: Stopping Spironolactone can allow your blood pressure to rise.
  - S3: Stopping Spironolactone can allow your heart failure to worsen.
  - S4: If you are taking Spironolactone for heart failure, Spironolactone is one of the medicines shown to help people live longer.
  - S5: Spironolactone is one of the medicines shown to help people with heart failure live longer.

**L155.3** `Complex Sentence` (0.816) → `decomposed`
- original: If side effects are the reason you want to stop, a dose change or a different medicine may be an option.
  - S1: If side effects are the reason you want to stop.
  - S2: A dose change may be an option.
  - S3: A different medicine may be an option.

**L156.0** `Incomplete Sentence` (0.938) → `excluded_incomplete`
- original: Can you take spironolactone at night?

**L156.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L157.0** `Simple Sentence` (0.991) → `passthrough`
- original: There is no fixed time of day for spironolactone.

**L157.1** `Complex Sentence` (0.773) → `decomposed`
- original: What matters more is that you take it at the same time each day and always the same way with regard to food, since food changes how much you absorb.
- pronoun resolved: What matters more is that you take Spironolactone at the same time each day and always the same way with regard to food, since food changes how much you absorb.
  - edits: “it” → “Spironolactone”
  - S1: What matters more is that you take Spironolactone at the same time each day.
  - S2: You should always take it the same way with regard to food.
  - S3: This is because food changes how much you absorb.

**L157.2** `Compound Sentence` (0.966) → `decomposed`
- original: Many people prefer the morning because spironolactone makes you pass more urine, and a late dose can mean getting up in the night.
  - S1: Many people prefer the morning because spironolactone makes you pass more urine.
  - S2: A late dose can mean getting up in the night.

**L157.3** `Simple Sentence` (0.776) → `passthrough`
- original: If a nighttime dose suits you better, check with your doctor or pharmacist first.

**L158.0** `Incomplete Sentence` (0.965) → `excluded_incomplete`
- original: Can you drink alcohol while taking spironolactone?

**L158.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L159.0** `Compound Sentence` (0.927) → `decomposed`
- original: There is no direct interaction between alcohol and spironolactone, but drinking is best kept modest.
  - S1: There is no direct interaction between alcohol and spironolactone.
  - S2: Drinking is best kept modest.

**L159.1** `Compound Sentence` (0.93) → `decomposed`
- original: Both can lower your blood pressure and make you light-headed, so together they raise the chance of feeling dizzy or faint, particularly when you stand up.
  - S1: Both can lower your blood pressure and make you light-headed.
  - S2: Together they raise the chance of feeling dizzy or faint.
  - S3: This is particularly true when you stand up.

**L159.2** `Simple Sentence` (0.654) → `passthrough`
- original: Alcohol is also a problem in its own right if you are taking spironolactone for liver disease.
- pronoun resolved: Alcohol is also a problem in Alcohol's own right if you are taking spironolactone for liver disease.
  - edits: “its” → “Alcohol's”

**L159.3** `Incomplete Sentence` (0.963) → `excluded_incomplete`
- original: Ask your doctor what is reasonable for your situation.

**L160.0** `Incomplete Sentence` (0.957) → `excluded_incomplete`
- original: Can you take spironolactone while pregnant?

**L160.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L161.0** `Simple Sentence` (0.992) → `passthrough`
- original: Spironolactone is generally avoided in pregnancy.

**L161.1** `Compound Sentence` (0.969) → `decomposed`
- original: It blocks the action of male hormones, and in animal studies male offspring exposed before birth developed abnormally.
- pronoun resolved: Spironolactone blocks the action of male hormones, and in animal studies male offspring exposed before birth developed abnormally.
  - edits: “It” → “Spironolactone”
  - S1: Spironolactone blocks the action of male hormones.
  - S2: In animal studies, male offspring exposed before birth developed abnormally.

**L161.2** `Compound-Complex Sentence` (0.88) → `decomposed`
- original: Human data are limited and have not shown a clear increase in birth defects, but the concern is enough that the manufacturer advises avoiding it or discussing the potential risk to a male baby.
- pronoun resolved: Human data are limited and have not shown a clear increase in birth defects, but the concern is enough that the manufacturer advises avoiding Spironolactone or discussing the potential risk to a male baby.
  - edits: “it” → “Spironolactone”
  - S1: Human data are limited.
  - S2: Human data have not shown a clear increase in birth defects.
  - S3: The concern is enough.
  - S4: The manufacturer advises avoiding Spironolactone.
  - S5: The manufacturer advises discussing the potential risk to a male baby.

**L162.0** `Simple Sentence` (0.863) → `passthrough`
- original: Do not stop spironolactone on your own if you find out you are pregnant.

**L162.1** `Compound-Complex Sentence` (0.691) → `decomposed`
- original: Tell your doctor straight away, because untreated heart failure, cirrhosis, and high blood pressure also carry serious risks in pregnancy and your treatment will need to be changed carefully.
  - S1: Tell your doctor straight away.
  - S2: Untreated heart failure carries serious risks in pregnancy.
  - S3: Untreated cirrhosis carries serious risks in pregnancy.
  - S4: Untreated high blood pressure carries serious risks in pregnancy.
  - S5: Your treatment will need to be changed carefully.

**L163.0** `Incomplete Sentence` (0.916) → `excluded_incomplete`
- original: Does spironolactone cause constipation?

**L163.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L164.0** `Simple Sentence` (0.987) → `passthrough`
- original: Constipation is not a listed side effect of spironolactone.

**L164.1** `Compound Sentence` (0.801) → `decomposed`
- original: The digestive side effects that have been reported are the opposite, including diarrhea and stomach cramping, along with nausea, vomiting, and indigestion.
  - S1: The digestive side effects that have been reported are the opposite.
  - S2: They include diarrhea and stomach cramping.
  - S3: They also include nausea, vomiting, and indigestion.

**L164.2** `Compound Sentence` (0.737) → `decomposed`
- original: If you are constipated while taking spironolactone, another cause is more likely, and it is worth mentioning to your pharmacist, who can check the rest of your medicines.
- pronoun resolved: If you are constipated while taking spironolactone, another cause is more likely, and spironolactone is worth mentioning to your pharmacist, who can check the rest of your medicines.
  - edits: “it” → “spironolactone”
  - S1: If you are constipated while taking spironolactone, another cause is more likely.
  - S2: Spironolactone is worth mentioning to your pharmacist.
  - S3: The pharmacist can check the rest of your medicines.

**L165.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Is 200 mg of spironolactone too much?

**L165.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L166.0** `Simple Sentence` (0.96) → `passthrough`
- original: It depends on the reason you are taking it.
- pronoun resolved: It depends on the reason you are taking spironolactone.
  - edits: “it.” → “spironolactone.”

**L166.1** `Compound-Complex Sentence` (0.723) → `decomposed`
- original: For fluid build-up, the approved dose range goes up to 200 mg a day, and for primary hyperaldosteronism it goes up to 400 mg a day, so 200 mg is within the licensed range for both.
- pronoun resolved: For fluid build-up, the approved dose range goes up to 200 mg a day, and for primary hyperaldosteronism spironolactone goes up to 400 mg a day, so 200 mg is within the licensed range for both.
  - edits: “it” → “spironolactone”
  - S1: The approved dose range for fluid build-up goes up to 200 mg a day.
  - S2: The approved dose range for primary hyperaldosteronism goes up to 400 mg a day.
  - S3: 200 mg is within the licensed range for fluid build-up.
  - S4: 200 mg is within the licensed range for primary hyperaldosteronism.

**L167.0** `Complex Sentence` (0.711) → `decomposed`
- original: For high blood pressure it would be above the usual range, since doses over 100 mg a day do not lower blood pressure any further.
- pronoun resolved: For high blood pressure Spironolactone would be above the usual range, since doses over 100 mg a day do not lower blood pressure any further.
  - edits: “it” → “Spironolactone”
  - S1: For high blood pressure, Spironolactone would be above the usual range.
  - S2: Doses over 100 mg a day do not lower blood pressure any further.

**L167.1** `Compound Sentence` (0.954) → `decomposed`
- original: For heart failure the usual dose is 25 mg to 50 mg a day, so 200 mg would be well above what is normally used.
  - S1: For heart failure, the usual dose is 25 mg to 50 mg a day.
  - S2: Therefore, 200 mg would be well above what is normally used.

**L167.2** `Compound Sentence` (0.427) → `decomposed`
- original: Higher doses also carry a greater risk of high potassium and of breast growth in men.
  - S1: Higher doses carry a greater risk of high potassium.
  - S2: Higher doses also carry a greater risk of breast growth in men.

**L167.3** `Compound Sentence` (0.367) → `decomposed`
- original: If your dose seems high for your condition, ask your prescriber rather than adjusting it yourself.
- pronoun resolved: If your dose seems high for your condition, ask your prescriber rather than adjusting dose yourself.
  - edits: “it” → “dose”
  - S1: If your dose seems high for your condition, ask your prescriber.
  - S2: Do not adjust the dose yourself.

**L168.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Why is spironolactone described as a high-risk medicine?

**L168.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L169.0** `Complex Sentence` (0.88) → `decomposed`
- original: The main reason is the risk of a high potassium level, which can cause a dangerous change in your heart rhythm and often gives no warning symptoms.
  - S1: The main reason is the risk of a high potassium level.
  - S2: A high potassium level can cause a dangerous change in your heart rhythm.
  - S3: A high potassium level often gives no warning symptoms.

**L169.1** `Compound-Complex Sentence` (0.537) → `decomposed`
- original: The risk rises if your kidneys do not work well or if you take other medicines that raise potassium, and several very common medicines do, including ibuprofen and some blood pressure tablets.
  - S1: The risk rises if your kidneys do not work well.
  - S2: The risk rises if you take other medicines that raise potassium.
  - S3: Several very common medicines raise potassium.
  - S4: Ibuprofen is a very common medicine that raises potassium.
  - S5: Some blood pressure tablets are very common medicines that raise potassium.

**L170.0** `Compound Sentence` (0.481) → `decomposed`
- original: This risk is manageable, which is why blood tests are built into treatment.
  - S1: This risk is manageable.
  - S2: Blood tests are built into treatment.

**L170.1** `Compound Sentence` (0.836) → `decomposed`
- original: Your potassium should be checked within a week of starting spironolactone or changing your dose, and regularly after that.
  - S1: Your potassium should be checked within a week of starting spironolactone or changing your dose.
  - S2: It should be checked regularly after that.

**L170.2** `Simple Sentence` (0.987) → `passthrough`
- original: Spironolactone also needs care in pregnancy and in people with liver disease.

## Popular FAQ

**L173.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Q: Winlevi vs Spironolactone: How do they compare?

**L173.1** `Simple Sentence` (0.981) → `passthrough`
- original: A: Winlevi (clascoterone) and spironolactone are both prescribed to treat acne.

**L173.2** `Compound Sentence` (0.959) → `decomposed`
- original: Winlevi is a topical cream, while spironolactone is available in an oral tablet and oral suspension.
  - S1: Winlevi is a topical cream.
  - S2: Spironolactone is available in an oral tablet and oral suspension.
