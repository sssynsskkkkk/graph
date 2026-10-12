# Hydrochlorothiazide (HCTZ) — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/hydrochlorothiazide.txt` · 223 sentences · 24 changed by pronoun resolution · 322 sentences sent to EDC

## What is hydrochlorothiazide?

**L5.0** `Complex Sentence` (0.666) → `decomposed`
- original: Hydrochlorothiazide is a thiazide diuretic, often called a water pill, used to treat high blood pressure and to reduce a build-up of fluid in the body (edema).
  - S1: Hydrochlorothiazide is a thiazide diuretic.
  - S2: It is often called a water pill.
  - S3: It is used to treat high blood pressure.
  - S4: It is used to reduce a build-up of fluid in the body.
  - S5: This build-up of fluid is called edema.

**L5.1** `Compound Sentence` (0.692) → `decomposed`
- original: It works by making the kidneys pass more salt and water out of the body, so you urinate more.
- pronoun resolved: Hydrochlorothiazide works by making the kidneys pass more salt and water out of the body, so you urinate more.
  - edits: “It” → “Hydrochlorothiazide”
  - S1: Hydrochlorothiazide works by making the kidneys pass more salt and water out of the body.
  - S2: You urinate more.

**L6.0** `Simple Sentence` (0.987) → `passthrough`
- original: Hydrochlorothiazide is often shortened to HCTZ on prescriptions and medical records.

**L6.1** `Compound Sentence` (0.867) → `decomposed`
- original: It is available as a tablet, capsule, and liquid (suspension) taken by mouth and is usually taken once or twice a day.
- pronoun resolved: Hydrochlorothiazide is available as a tablet, capsule, and liquid (suspension) taken by mouth and is usually taken once or twice a day.
  - edits: “It” → “Hydrochlorothiazide”
  - S1: Hydrochlorothiazide is available as a tablet, capsule, and liquid (suspension) taken by mouth.
  - S2: It is usually taken once or twice a day.

**L7.0** `Simple Sentence` (0.727) → `passthrough`
- original: Hydrochlorothiazide is available as:

**L8.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: oral tablet (12.5 mg, 25 mg, and 50 mg)

**L9.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: oral capsule (12.5 mg)

**L10.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: powder for oral suspension (10 mg/mL)

**L11.0** `Compound Sentence` (0.81) → `decomposed`
- original: Hydrochlorothiazide (HCTZ) brand names included HydroDIURIL tablets (discontinued), Esidrix (discontinued), and Microzide capsules (discontinued); now generic tablets and capsules are available.
  - S1: Hydrochlorothiazide (HCTZ) brand names included HydroDIURIL tablets (discontinued).
  - S2: Esidrix (discontinued) was a brand name for Hydrochlorothiazide (HCTZ).
  - S3: Microzide capsules (discontinued) were a brand name for Hydrochlorothiazide (HCTZ).
  - S4: Now generic tablets and capsules are available.

**L11.1** `Simple Sentence` (0.981) → `passthrough`
- original: The brand name of hydrochlorothiazide oral suspension is Inzirqo.

**L12.0** `Compound Sentence` (0.345) → `decomposed`
- original: Hydrochlorothiazide is also an ingredient in many combination blood pressure medicines, including with losartan, lisinopril, valsartan, and more.
  - S1: Hydrochlorothiazide is also an ingredient in many combination blood pressure medicines.
  - S2: These medicines include combinations with losartan, lisinopril, valsartan, and more.

## What is hydrochlorothiazide (HCTZ) used for?

**L15.0** `Simple Sentence` (0.829) → `passthrough`
- original: Hydrochlorothiazide is approved to treat high blood pressure (hypertension) and fluid retention (edema) in certain patients.

**L16.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: High blood pressure:

**L17.0** `Complex Sentence` (0.604) → `decomposed`
- original: HCTZ is used to manage high blood pressure (hypertension), either on its own or alongside other blood pressure medicines.
- pronoun resolved: HCTZ is used to manage high blood pressure (hypertension), either on HCTZ's own or alongside other blood pressure medicines.
  - edits: “its” → “HCTZ's”
  - S1: HCTZ is used to manage high blood pressure (hypertension).
  - S2: HCTZ is used on its own.
  - S3: HCTZ is used alongside other blood pressure medicines.

**L17.1** `Simple Sentence` (0.574) → `passthrough`
- original: Lowering blood pressure reduces the risk of fatal and non-fatal cardiovascular events, mainly strokes and heart attacks.

**L18.0** `Compound Sentence` (0.948) → `decomposed`
- original: All three forms of hydrochlorothiazide, tablets, capsules and the oral suspension, are approved for high blood pressure in adults, and the oral suspension is also approved for children.
  - S1: All three forms of hydrochlorothiazide, tablets, capsules and the oral suspension, are approved for high blood pressure in adults.
  - S2: The oral suspension is also approved for children.

**L19.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Fluid retention:

**L20.0** `Simple Sentence` (0.985) → `passthrough`
- original: Hydrochlorothiazide tablets are used to treat a build-up of fluid (edema) associated with:

**L21.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: congestive heart failure

**L22.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: cirrhosis of the liver

**L23.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: kidney conditions, including nephrotic syndrome, acute glomerulonephritis and chronic kidney failure

**L24.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: treatment with corticosteroid or estrogen medicines

**L25.0** `Complex Sentence` (0.83) → `decomposed`
- original: The HCTZ oral suspension is approved for fluid retention associated with congestive heart failure, cirrhosis of the liver, and kidney disease including nephrotic syndrome, in both adults and children.
  - S1: The HCTZ oral suspension is approved for fluid retention.
  - S2: The fluid retention is associated with congestive heart failure, cirrhosis of the liver, and kidney disease.
  - S3: Kidney disease includes nephrotic syndrome.
  - S4: The approval applies to both adults and children.

**L26.0** `Simple Sentence` (0.677) → `passthrough`
- original: The capsules are approved for high blood pressure only, not for fluid retention.

**L27.0** `Simple Sentence` (0.982) → `passthrough`
- original: Not all forms of HCTZ are approved for all indications and age groups.

**L28.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Approved HCTZ uses by age groups and dosage form:

**L29.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: HCTZ Form and strengths | High blood pressure | Fluid retention (edema) | Ages

**L30.0** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: Tablets 12.5 mg, 25 mg, 50 mg | Yes | As an add-on therapy for edema due to congestive heart failure, hepatic cirrhosis, and corticosteroid and estrogen therapy.

**L30.1** `Incomplete Sentence` (0.979) → `excluded_incomplete`
- original: Yes, for edema due to various forms of renal dysfunction such as nephrotic syndrome, acute glomerulonephritis, and chronic renal failure.

**L30.2** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: | Adults and children

**L31.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Capsules 12.5 mg | Yes | No | Adults

**L32.0** `Incomplete Sentence` (0.976) → `excluded_incomplete`
- original: Oral suspension 10 mg/mL | Yes | Yes, for edema due to congestive heart failure, hepatic cirrhosis, and renal disease including the nephrotic syndrome in adult and pediatric patients.

**L32.1** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: | Adults and children

## How does hydrochlorothiazide work?

**L35.0** `Compound-Complex Sentence` (0.809) → `decomposed`
- original: Hydrochlorothiazide works by inhibiting the kidneys from reabsorbing sodium and chloride, so more salt and water leave the body in the urine, which helps reduce excess fluid buildup (edema).
  - S1: Hydrochlorothiazide works by inhibiting the kidneys from reabsorbing sodium and chloride.
  - S2: More salt and water leave the body in the urine.
  - S3: This helps reduce excess fluid buildup (edema).

**L35.1** `Simple Sentence` (0.98) → `passthrough`
- original: Exactly how thiazides lower blood pressure is not fully understood.

**L35.2** `Simple Sentence` (0.982) → `passthrough`
- original: The early effect is thought to come from a drop in blood volume.

**L35.3** `Compound Sentence` (0.842) → `decomposed`
- original: With longer-term use, blood volume returns towards normal while the blood vessels themselves offer less resistance to blood flow.
  - S1: With longer-term use, blood volume returns towards normal.
  - S2: The blood vessels themselves offer less resistance to blood flow.

**L35.4** `Simple Sentence` (0.987) → `passthrough`
- original: Hydrochlorothiazide does not usually change blood pressure that is already normal.

**L36.0** `Simple Sentence` (0.962) → `passthrough`
- original: Hydrochlorothiazide is a thiazide diuretic.

## Before taking this medicine

**L39.0** `Compound Sentence` (0.761) → `decomposed`
- original: Do not take hydrochlorothiazide if you are unable to pass urine (anuria), or if you are allergic to hydrochlorothiazide or to other sulfonamide-derived medicines (sometimes called sulfa drugs).
  - S1: Do not take hydrochlorothiazide if you are unable to pass urine (anuria).
  - S2: Do not take hydrochlorothiazide if you are allergic to hydrochlorothiazide or to other sulfonamide-derived medicines (sometimes called sulfa drugs).

**L40.0** `Simple Sentence` (0.837) → `passthrough`
- original: Before you start HCTZ, tell your doctor if you have or have ever had:

**L41.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: kidney disease or reduced kidney function

**L42.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: liver disease, including cirrhosis

**L43.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: diabetes

**L44.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: gout or high uric acid levels

**L45.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: high cholesterol or high triglycerides

**L46.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: high calcium levels or a parathyroid gland disorder

**L47.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: low potassium or low sodium levels

**L48.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: lupus (systemic lupus erythematosus)

**L49.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: glaucoma

**L50.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: an allergy to sulfa medicines or to penicillin

**L51.0** `Incomplete Sentence` (0.819) → `excluded_incomplete`
- original: Also tell your doctor if you are pregnant, planning to become pregnant, or breastfeeding.

**L51.1** `Simple Sentence` (0.991) → `passthrough`
- original: Hydrochlorothiazide may cause jaundice or bleeding problems in a newborn.

**L51.2** `Compound-Complex Sentence` (0.889) → `decomposed`
- original: It can also pass into breast milk and may cause serious side effects in a nursing baby, so you and your doctor should decide whether you will take this medicine or breastfeed.
- pronoun resolved: Hydrochlorothiazide can also pass into breast milk and may cause serious side effects in a nursing baby, so you and your doctor should decide whether you will take Hydrochlorothiazide or breastfeed.
  - edits: “It” → “Hydrochlorothiazide”; “this medicine” → “Hydrochlorothiazide”
  - S1: Hydrochlorothiazide can pass into breast milk.
  - S2: Hydrochlorothiazide may cause serious side effects in a nursing baby.
  - S3: You and your doctor should decide whether to take Hydrochlorothiazide or breastfeed.

## Warning and precautions

**L54.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Fluid and salt imbalance:

**L55.0** `Simple Sentence` (0.967) → `passthrough`
- original: Hydrochlorothiazide can lower the levels of potassium, sodium, magnesium and chloride in your blood.

**L55.1** `Compound Sentence` (0.787) → `decomposed`
- original: Low potassium (hypokalemia) is the most common of these and is more likely at higher doses, during rapid fluid loss, if you have severe cirrhosis, or after long-term use..
  - S1: Low potassium (hypokalemia) is the most common of these.
  - S2: It is more likely at higher doses.
  - S3: It is more likely during rapid fluid loss.
  - S4: It is more likely if you have severe cirrhosis.
  - S5: It is more likely after long-term use.

**L55.2** `Simple Sentence` (0.888) → `passthrough`
- original: Your doctor will check your blood before you start and at intervals during treatment.

**L56.0** `Incomplete Sentence` (0.891) → `excluded_incomplete`
- original: Contact your doctor if you have any of the following, which can be signs of a fluid or salt imbalance:

**L57.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: dry mouth, thirst, or unusual weakness or tiredness

**L58.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: drowsiness, restlessness or confusion

**L59.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: muscle pain, cramps or muscle fatigue

**L60.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: fast heartbeat

**L61.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: passing much less urine than usual

**L62.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: nausea or vomiting

**L63.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: seizures

**L64.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Kidney and liver problems:

**L65.0** `Complex Sentence` (0.72) → `decomposed`
- original: HCTZ reduces the fluid volume in your body, which can lead to sudden kidney injury.
  - S1: HCTZ reduces the fluid volume in your body.
  - S2: This reduction can lead to sudden kidney injury.

**L65.1** `Compound Sentence` (0.462) → `decomposed`
- original: The risk is higher if you have chronic kidney disease, heart failure, or are already low on fluid.
  - S1: The risk is higher if you have chronic kidney disease.
  - S2: The risk is higher if you have heart failure.
  - S3: The risk is higher if you are already low on fluid.

**L65.2** `Complex Sentence` (0.884) → `decomposed`
- original: If you have liver disease, small changes in fluid and salt balance can trigger a serious complication called hepatic coma.
  - S1: If you have liver disease, small changes in fluid and salt balance can trigger a serious complication.
  - S2: The complication is called hepatic coma.

**L65.3** `Simple Sentence` (0.943) → `passthrough`
- original: Your doctor will monitor your kidney function and watch for changes in alertness.

**L66.0** `Simple Sentence` (0.99) → `passthrough`
- original: Sudden vision changes need urgent care:

**L67.0** `Compound Sentence` (0.46) → `decomposed`
- original: Rarely, hydrochlorothiazide causes sudden short-sightedness (acute myopia) and a sharp rise in pressure inside the eye (acute angle-closure glaucoma), usually within hours to weeks of starting the medicine.
  - S1: Rarely, hydrochlorothiazide causes sudden short-sightedness (acute myopia).
  - S2: It also causes a sharp rise in pressure inside the eye (acute angle-closure glaucoma).
  - S3: These side effects usually occur within hours to weeks of starting the medicine.

**L67.1** `Compound Sentence` (0.664) → `decomposed`
- original: Stop taking it and get medical help immediately if your vision drops suddenly or your eye hurts.
- pronoun resolved: Stop taking Hydrochlorothiazide and get medical help immediately if your vision drops suddenly or your eye hurts.
  - edits: “it” → “Hydrochlorothiazide”
  - S1: Stop taking Hydrochlorothiazide and get medical help immediately if your vision drops suddenly.
  - S2: Stop taking Hydrochlorothiazide and get medical help immediately if your eye hurts.

**L67.2** `Simple Sentence` (0.966) → `passthrough`
- original: Left untreated, this can cause permanent loss of vision.
- pronoun resolved: Left untreated, acute angle-closure glaucoma can cause permanent loss of vision.
  - edits: “this” → “acute angle-closure glaucoma”

**L67.3** `Simple Sentence` (0.947) → `passthrough`
- original: A history of allergy to sulfa medicines or penicillin may increase the risk.

**L68.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Blood sugar, cholesterol, uric acid and calcium:

**L69.0** `Simple Sentence` (0.95) → `passthrough`
- original: Hydrochlorothiazide can raise blood sugar, cholesterol, triglycerides, uric acid and calcium.

**L69.1** `Compound Sentence` (0.967) → `decomposed`
- original: Your diabetes medicine or insulin dose may need adjusting, and diabetes that was previously unnoticed can become apparent during treatment.
  - S1: Your diabetes medicine or insulin dose may need adjusting.
  - S2: Diabetes that was previously unnoticed can become apparent during treatment.

**L69.2** `Compound Sentence` (0.894) → `decomposed`
- original: The rise in uric acid is related to the dose and can cause gout or make existing gout worse.
  - S1: The rise in uric acid is related to the dose.
  - S2: It can cause gout.
  - S3: It can make existing gout worse.

**L69.3** `Complex Sentence` (0.454) → `decomposed`
- original: Because the medicine also affects calcium, it is stopped before parathyroid function tests, so tell any doctor arranging tests that you take it.
- pronoun resolved: Because the medicine also affects calcium, Hydrochlorothiazide is stopped before parathyroid function tests, so tell any doctor arranging tests that you take it.
  - edits: “it” → “Hydrochlorothiazide”
  - S1: Hydrochlorothiazide is stopped before parathyroid function tests.
  - S2: This is because the medicine also affects calcium.
  - S3: Tell any doctor arranging tests that you take it.

**L69.4** `Simple Sentence` (0.974) → `passthrough`
- original: Your doctor will check these levels from time to time.

**L70.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Skin cancer risk:

**L71.0** `Complex Sentence` (0.893) → `decomposed`
- original: Long-term use of hydrochlorothiazide is linked to a small increase in the risk of non-melanoma skin cancer, mainly squamous cell carcinoma.
  - S1: Long-term use of hydrochlorothiazide is linked to a small increase in the risk of non-melanoma skin cancer.
  - S2: The risk is mainly due to squamous cell carcinoma.

**L71.1** `Compound Sentence` (0.787) → `decomposed`
- original: In a large safety study the increase was about 1 extra case per 16,000 people per year, rising to about 1 extra case per 6,700 people per year among white patients who had taken a total of 50,000 mg or more.
  - S1: In a large safety study, the increase was about 1 extra case per 16,000 people per year.
  - S2: This figure rose to about 1 extra case per 6,700 people per year among white patients who had taken a total of 50,000 mg or more.

**L72.0** `Compound Sentence` (0.898) → `decomposed`
- original: Protect your skin from the sun, wear protective clothing and use sunscreen, avoid sunlamps and tanning beds, and have regular skin checks.
  - S1: Protect your skin from the sun.
  - S2: Wear protective clothing and use sunscreen.
  - S3: Avoid sunlamps and tanning beds.
  - S4: Have regular skin checks.

**L72.1** `Incomplete Sentence` (0.822) → `excluded_incomplete`
- original: Tell your doctor about any new or changing skin growth, or a sore that does not heal.

**L73.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Lupus and allergic reactions:

**L74.0** `Simple Sentence` (0.98) → `passthrough`
- original: Thiazide diuretics have been reported to worsen lupus or bring it on.

**L74.1** `Simple Sentence` (0.986) → `passthrough`
- original: Sensitivity reactions can happen whether or not you have a history of allergies or asthma.

## Hydrochlorothiazide side effects

**L77.0** `Complex Sentence` (0.452) → `decomposed`
- original: The most noticeable effect of hydrochlorothiazide is passing urine more often, particularly in the first few weeks.
  - S1: The most noticeable effect of hydrochlorothiazide is passing urine more often.
  - S2: This effect is particularly noticeable in the first few weeks.

**L77.1** `Compound Sentence` (0.951) → `decomposed`
- original: This is how the medicine works rather than a side effect, and it usually settles as your body adjusts.
- pronoun resolved: This is how the medicine works rather than a side effect, and side effect usually settles as your body adjusts.
  - edits: “it” → “side effect”
  - S1: This is how the medicine works rather than a side effect.
  - S2: A side effect usually settles as your body adjusts.

**L78.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious side effects:

**L79.0** `Incomplete Sentence` (0.406) → `excluded_incomplete`
- original: Get emergency medical help if you have signs of an allergic reaction, such as hives, difficulty breathing, or swelling of your face, lips, tongue or throat.

**L80.0** `Incomplete Sentence` (0.582) → `excluded_incomplete`
- original: Get emergency medical help if you have a severe skin reaction, such as a spreading red or purple rash with blistering and peeling, or skin that is painful to touch.

**L81.0** `Compound Sentence` (0.684) → `decomposed`
- original: Stop taking hydrochlorothiazide and get medical help immediately if you have a sudden change in your vision or pain in your eye.
  - S1: Stop taking hydrochlorothiazide if you have a sudden change in your vision.
  - S2: Get medical help immediately if you have pain in your eye.

**L82.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L83.0** `Incomplete Sentence` (0.874) → `excluded_incomplete`
- original: severe pain in your upper stomach that spreads to your back, with nausea and vomiting, which can be a sign of inflammation of the pancreas (pancreatitis)

**L84.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: yellowing of your skin or the whites of your eyes (jaundice)

**L85.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: fever, chills, sore throat, mouth sores or other signs of infection

**L86.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: unusual bruising or bleeding, or pale skin and unusual tiredness, which can be signs of a blood problem

**L87.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: shortness of breath, wheezing, or a cough with frothy mucus

**L88.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: passing much less urine than usual, or swelling in your legs and ankles

**L89.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: light-headedness or fainting, especially when standing up

**L90.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: signs of dehydration or a salt imbalance, such as extreme thirst, dry mouth, confusion, muscle cramps, irregular heartbeat or unusual weakness

**L91.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Other side effects:

**L92.0** `Simple Sentence` (0.904) → `passthrough`
- original: Other hydrochlorothiazide side effects include:

**L93.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: dizziness, a spinning sensation (vertigo), headache, restlessness, or tingling and numbness (paresthesia)

**L94.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: weakness

**L95.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: nausea, vomiting, diarrhea, constipation, stomach cramping, stomach irritation, or loss of appetite

**L96.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: muscle spasm

**L97.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: increased sensitivity to sunlight, causing sunburn more easily

**L98.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: hair loss or thinning

**L99.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: difficulty getting or keeping an erection

**L100.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: temporary blurred vision, or objects looking yellow-tinged (xanthopsia)

**L101.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: swelling and tenderness of the salivary glands

**L102.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: raised blood sugar, sugar in the urine, or raised uric acid

**L103.0** `Complex Sentence` (0.61) → `decomposed`
- original: If a side effect is moderate or severe, your doctor may lower your dose or stop the medicine.
- pronoun resolved: If a side effect is moderate or severe, your doctor may lower your dose or stop Hydrochlorothiazide.
  - edits: “the medicine.” → “Hydrochlorothiazide.”
  - S1: If a side effect is moderate or severe, your doctor may lower your dose.
  - S2: Your doctor may stop Hydrochlorothiazide.

**L103.1** `Simple Sentence` (0.607) → `passthrough`
- original: Do not stop taking HCTZ on your own without speaking to your doctor first.

**L104.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L104.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L104.2** `Simple Sentence` (0.97) → `passthrough`
- original: You may report side effects to the FDA at 1-800-FDA-1088.

## Hydrochlorothiazide (HCTZ) dosage information

**L107.0** `Compound Sentence` (0.956) → `decomposed`
- original: Your doctor will choose the smallest dose that controls your condition, and may adjust it over time.
- pronoun resolved: Your doctor will choose the smallest dose that controls your condition, and may adjust dose over time.
  - edits: “it” → “dose”
  - S1: Your doctor will choose the smallest dose that controls your condition.
  - S2: Your doctor may adjust the dose over time.

**L107.1** `Incomplete Sentence` (0.527) → `excluded_incomplete`
- original: Follow your prescription label and do not change your dose yourself.

**L108.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: HCTZ dose for high blood pressure (adults):

**L109.0** `Complex Sentence` (0.478) → `decomposed`
- original: Tablets: The starting dose is hydrochlorothiazide 25 mg once a day, which may be increased to 50 mg a day, taken as a single dose or split into two doses.
  - S1: Tablets: The starting dose is hydrochlorothiazide 25 mg once a day.
  - S2: The dose may be increased to 50 mg a day.
  - S3: The dose is taken as a single dose or split into two doses.

**L109.1** `Simple Sentence` (0.963) → `passthrough`
- original: Doses above 50 mg a day are often associated with a marked drop in blood potassium.

**L109.2** `Simple Sentence` (0.951) → `passthrough`
- original: Most people do not need more than 50 mg a day when hydrochlorothiazide is taken alongside other blood pressure medicines

**L110.0** `Compound Sentence` (0.436) → `decomposed`
- original: Capsules: The starting dose is a hydrochlorothiazide 12.5 mg capsule once a day, whether taken on its own or with other blood pressure medicines.
  - S1: The starting dose is a hydrochlorothiazide 12.5 mg capsule once a day.
  - S2: It can be taken on its own or with other blood pressure medicines.

**L110.1** `Simple Sentence` (0.983) → `passthrough`
- original: Total daily doses above 50 mg are not recommended.

**L110.2** `Simple Sentence` (0.916) → `passthrough`
- original: Capsules are approved for high blood pressure only, not for fluid retention.

**L111.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: HCTZ dose for fluid retention (adults):

**L112.0** `Simple Sentence` (0.74) → `passthrough`
- original: Tablets: The usual dose is hydrochlorothiazide 25 mg to 100 mg a day, taken as a single dose or split into two doses.

**L112.1** `Complex Sentence` (0.828) → `decomposed`
- original: Many people with fluid retention respond to intermittent treatment, such as taking it every other day or on 3 to 5 days each week.
- pronoun resolved: Many people with fluid retention respond to intermittent treatment, such as taking treatment every other day or on 3 to 5 days each week.
  - edits: “it” → “treatment”
  - S1: Many people with fluid retention respond to intermittent treatment.
  - S2: Intermittent treatment includes taking treatment every other day.
  - S3: Intermittent treatment also includes taking treatment on 3 to 5 days each week.

**L112.2** `Simple Sentence` (0.737) → `passthrough`
- original: Excessive response and undesirable electrolyte imbalance are less likely to occur with intermittent dosing.

**L113.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: HCTZ dose for children for high blood pressure and fluid retention:

**L114.0** `Complex Sentence` (0.866) → `decomposed`
- original: The usual HCTZ dose in children, for both high blood pressure and fluid retention, is 1 mg to 2 mg per kilogram of body weight (0.5 mg to 1 mg per pound) a day, given as a single dose or split into two doses.
  - S1: The usual HCTZ dose in children is 1 mg to 2 mg per kilogram of body weight (0.5 mg to 1 mg per pound) a day.
  - S2: This dose is used for both high blood pressure and fluid retention.
  - S3: The dose is given as a single dose or split into two doses.

**L115.0** `Compound Sentence` (0.426) → `decomposed`
- original: Infants under 6 months: may be need doses of up to 3 mg per kilogram (1.5 mg per pound) a day, given as two divided doses up to the same maximum 37.5 mg daily limit
  - S1: Infants under 6 months may need doses of up to 3 mg per kilogram (1.5 mg per pound) a day.
  - S2: These doses are given as two divided doses up to the same maximum 37.5 mg daily limit.

**L116.0** `Incomplete Sentence` (0.515) → `excluded_incomplete`
- original: Infants and children under 2 years: do not exceed 37.5 mg a day

**L117.0** `Incomplete Sentence` (0.856) → `excluded_incomplete`
- original: Children 2 to 12 years: do not exceed 100 mg a day

**L118.0** `Simple Sentence` (0.702) → `passthrough`
- original: The dose is based on your child's weight and must be worked out by their doctor.

**L119.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Taking the oral suspension:

**L120.0** `Complex Sentence` (0.41) → `decomposed`
- original: If your child has been prescribed the liquid form (oral suspension), the following applies:
  - S1: If your child has been prescribed the liquid form.
  - S2: The liquid form is an oral suspension.
  - S3: The following applies.

**L121.0** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: Shake the bottle well before every dose.

**L122.0** `Incomplete Sentence` (0.971) → `excluded_incomplete`
- original: Measure each dose with the oral dosing syringe.

**L122.1** `Incomplete Sentence` (0.827) → `excluded_incomplete`
- original: Ask your pharmacist for a syringe and a bottle adapter if you do not have them.

**L123.0** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Never measure a dose with a household teaspoon or tablespoon, because these do not give an accurate amount.

**L124.0** `Incomplete Sentence` (0.775) → `excluded_incomplete`
- original: Store the made-up suspension at room temperature and do not freeze it.
- pronoun resolved: Store the made-up suspension at room temperature and do not freeze suspension.
  - edits: “it.” → “suspension.”

**L125.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Throw away any unused suspension 30 days after it was made up.
- pronoun resolved: Throw away any unused suspension 30 days after suspension was made up.
  - edits: “it” → “suspension”

**L125.1** `Simple Sentence` (0.941) → `passthrough`
- original: The pharmacist will write this date on the bottle.

**L126.0** `Simple Sentence` (0.988) → `passthrough`
- original: The oral suspension can be taken with or without food.

**L127.0** `Incomplete Sentence` (0.971) → `excluded_incomplete`
- original: What happens if I miss a dose?

**L127.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L128.0** `Compound Sentence` (0.555) → `decomposed`
- original: Take the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - S1: Take the medicine as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L128.1** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

**L129.0** `Incomplete Sentence` (0.942) → `excluded_incomplete`
- original: What happens if I overdose?

**L129.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L130.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L131.0** `Compound Sentence` (0.421) → `decomposed`
- original: Overdose symptoms may include nausea, dizziness, dry mouth, thirst, and muscle pain or weakness.
  - S1: Overdose symptoms may include nausea, dizziness, dry mouth, thirst, and muscle pain or weakness.

## How long does hydrochlorothiazide take to work?

**L134.0** `Compound Sentence` (0.681) → `decomposed`
- original: Hydrochlorothiazide starts to work within 2 hours of a dose, with the peak effect at about 4 hours.
  - S1: Hydrochlorothiazide starts to work within 2 hours of a dose.
  - S2: The peak effect occurs at about 4 hours.

**L134.1** `Compound Sentence` (0.94) → `decomposed`
- original: The increase in urine output lasts for around 6 to 12 hours, while the medicine's overall action on the body can persist for up to 24 hours.
  - S1: The increase in urine output lasts for around 6 to 12 hours.
  - S2: The medicine's overall action on the body can persist for up to 24 hours.

**L135.0** `Compound Sentence` (0.96) → `decomposed`
- original: Lowering blood pressure takes longer than the fluid effect, and your doctor will usually reassess your blood pressure after a few weeks rather than straight away.
  - S1: Lowering blood pressure takes longer than the fluid effect.
  - S2: Your doctor will usually reassess your blood pressure after a few weeks rather than straight away.

**L136.0** `Compound Sentence` (0.859) → `decomposed`
- original: The medicine is well absorbed, is not broken down by the body, and is cleared by the kidneys, with most of a dose passing out unchanged in the urine.
- pronoun resolved: Hydrochlorothiazide is well absorbed, is not broken down by the body, and is cleared by the kidneys, with most of a dose passing out unchanged in the urine.
  - edits: “The medicine” → “Hydrochlorothiazide”
  - S1: Hydrochlorothiazide is well absorbed.
  - S2: It is not broken down by the body.
  - S3: It is cleared by the kidneys.
  - S4: Most of a dose passes out unchanged in the urine.

**L136.1** `Compound Sentence` (0.462) → `decomposed`
- original: Its half-life, meaning the time for blood levels to fall by half, has been reported as 6 to 15 hours.
  - S1: Its half-life has been reported as 6 to 15 hours.
  - S2: Its half-life means the time for blood levels to fall by half.

**L136.2** `Compound Sentence` (0.892) → `decomposed`
- original: In people with kidney disease, levels in the blood are higher and the medicine stays in the body longer.
- pronoun resolved: In people with kidney disease, levels in the blood are higher and Hydrochlorothiazide stays in the body longer.
  - edits: “the medicine” → “Hydrochlorothiazide”
  - S1: In people with kidney disease, levels in the blood are higher.
  - S2: In people with kidney disease, Hydrochlorothiazide stays in the body longer.

**L137.0** `Simple Sentence` (0.694) → `passthrough`
- original: Hydrochlorothiazide controls high blood pressure but does not cure it.

**L137.1** `Incomplete Sentence` (0.579) → `excluded_incomplete`
- original: Keep taking it even if you feel well, because high blood pressure often causes no symptoms.

## What other drugs will affect hydrochlorothiazide?

**L140.0** `Incomplete Sentence` (0.805) → `excluded_incomplete`
- original: Tell your doctor and pharmacist about all the medicines you take, including prescription and over-the-counter medicines, vitamins, and herbal products.

**L141.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Medicines that need particular care:

**L142.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Lithium.

**L142.1** `Simple Sentence` (0.988) → `passthrough`
- original: Lithium and diuretics generally should not be taken together.

**L142.2** `Complex Sentence` (0.881) → `decomposed`
- original: Hydrochlorothiazide reduces how quickly the kidneys clear lithium, which carries a high risk of lithium toxicity.
  - S1: Hydrochlorothiazide reduces how quickly the kidneys clear lithium.
  - S2: This reduction carries a high risk of lithium toxicity.

**L143.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Cholestyramine and colestipol.

**L143.1** `Compound Sentence` (0.702) → `decomposed`
- original: These cholesterol-lowering resins bind hydrochlorothiazide in the gut and can reduce how much you absorb by up to 85 percent for cholestyramine and 43 percent for colestipol.
  - S1: These cholesterol-lowering resins bind hydrochlorothiazide in the gut.
  - S2: They can reduce how much you absorb by up to 85 percent for cholestyramine and 43 percent for colestipol.

**L143.2** `Simple Sentence` (0.968) → `passthrough`
- original: The doses need to be separated.

**L143.3** `Complex Sentence` (0.693) → `decomposed`
- original: For the oral suspension, the label advises taking hydrochlorothiazide at least 4 hours before, or 4 to 6 hours after, the resin.
  - S1: The label advises taking hydrochlorothiazide for the oral suspension.
  - S2: The label advises taking hydrochlorothiazide at least 4 hours before the resin.
  - S3: The label advises taking hydrochlorothiazide 4 to 6 hours after the resin.

**L144.0** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: NSAIDs such as ibuprofen (Advil, Motrin), naproxen (Aleve), diclofenac, meloxicam, indomethacin, celecoxib and aspirin.

**L144.1** `Compound Sentence` (0.936) → `decomposed`
- original: These can reduce the fluid-clearing and blood-pressure-lowering effects of hydrochlorothiazide, and your doctor will check whether the medicine is still working as intended.
- pronoun resolved: NSAIDs can reduce the fluid-clearing and blood-pressure-lowering effects of hydrochlorothiazide, and your doctor will check whether the medicine is still working as intended.
  - edits: “These” → “NSAIDs”
  - S1: NSAIDs can reduce the fluid-clearing and blood-pressure-lowering effects of hydrochlorothiazide.
  - S2: Your doctor will check whether the medicine is still working as intended.

**L145.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Insulin and oral diabetes medicines.

**L145.1** `Simple Sentence` (0.987) → `passthrough`
- original: Your diabetes medicine dose may need adjusting.

**L146.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Corticosteroids and ACTH.

**L146.1** `Complex Sentence` (0.663) → `decomposed`
- original: Taken with hydrochlorothiazide, these increase the loss of salts from the body, particularly potassium.
  - S1: These increase the loss of salts from the body.
  - S2: The loss of salts is particularly potassium.
  - S3: This effect occurs when taken with hydrochlorothiazide.

**L147.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Digoxin and other digitalis medicines.

**L147.1** `Complex Sentence` (0.863) → `decomposed`
- original: Low potassium caused by hydrochlorothiazide can make the heart more sensitive to the toxic effects of digitalis, including irregular heart rhythms.
  - S1: Low potassium caused by hydrochlorothiazide can make the heart more sensitive to the toxic effects of digitalis.
  - S2: These toxic effects include irregular heart rhythms.

**L148.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Other blood pressure medicines.

**L148.1** `Compound Sentence` (0.65) → `decomposed`
- original: The effects add together, which may be intended, but can also lower blood pressure more than expected.
  - S1: The effects add together.
  - S2: This may be intended.
  - S3: However, it can also lower blood pressure more than expected.

**L149.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Alcohol, barbiturates and opioid pain medicines.

**L149.1** `Complex Sentence` (0.414) → `decomposed`
- original: These can make the drop in blood pressure on standing worse, causing dizziness or fainting.
- pronoun resolved: Alcohol, barbiturates and opioid pain medicines can make the drop in blood pressure on standing worse, causing dizziness or fainting.
  - edits: “These” → “Alcohol, barbiturates and opioid pain medicines”
  - S1: Alcohol, barbiturates and opioid pain medicines can make the drop in blood pressure on standing worse.
  - S2: This can cause dizziness or fainting.

**L150.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Muscle relaxants used during surgery (nondepolarizing muscle relaxants such as tubocurarine).

**L150.1** `Compound Sentence` (0.756) → `decomposed`
- original: You may respond more strongly to them, so tell your surgeon and anesthetist that you take hydrochlorothiazide.
- pronoun resolved: You may respond more strongly to Muscle relaxants, so tell your surgeon and anesthetist that you take hydrochlorothiazide.
  - edits: “them,” → “Muscle relaxants,”
  - S1: You may respond more strongly to Muscle relaxants.
  - S2: Tell your surgeon and anesthetist that you take hydrochlorothiazide.

**L151.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Medicines that raise blood pressure (pressor amines such as norepinephrine).

**L151.1** `Compound Sentence` (0.809) → `decomposed`
- original: Your response to them may be reduced, although this does not usually prevent their use.
- pronoun resolved: Your response to Medicines that raise blood pressure may be reduced, although this does not usually prevent Medicines that raise blood pressure's use.
  - edits: “them” → “Medicines that raise blood pressure”; “their” → “Medicines that raise blood pressure's”
  - S1: Your response to Medicines that raise blood pressure may be reduced.
  - S2: This does not usually prevent Medicines that raise blood pressure's use.

**L152.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L152.1** `Compound Sentence` (0.921) → `decomposed`
- original: Other medicines may affect hydrochlorothiazide, and hydrochlorothiazide may affect other medicines.
  - S1: Other medicines may affect hydrochlorothiazide.
  - S2: Hydrochlorothiazide may affect other medicines.

## Hydrochlorothiazide FAQ

**L155.0** `Incomplete Sentence` (0.937) → `excluded_incomplete`
- original: Does hydrochlorothiazide cause weight loss?

**L155.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L156.0** `Simple Sentence` (0.988) → `passthrough`
- original: Hydrochlorothiazide is not a weight loss medicine.

**L156.1** `Compound-Complex Sentence` (0.668) → `decomposed`
- original: Some people see the number on the scales drop in the first days or weeks of treatment, but this is extra fluid leaving the body rather than any loss of body fat, and it levels off.
- pronoun resolved: Some people see the number on the scales drop in the first days or weeks of treatment, but this is extra fluid leaving the body rather than any loss of body fat, and fluid levels off.
  - edits: “it” → “fluid”
  - S1: Some people see the number on the scales drop in the first days or weeks of treatment.
  - S2: This is extra fluid leaving the body.
  - S3: This is not any loss of body fat.
  - S4: Fluid levels off.

**L156.2** `Simple Sentence` (0.514) → `passthrough`
- original: Do not take hydrochlorothiazide to lose weight.

**L157.0** `Incomplete Sentence` (0.964) → `excluded_incomplete`
- original: Can you drink alcohol while taking hydrochlorothiazide?

**L157.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L158.0** `Complex Sentence` (0.618) → `decomposed`
- original: Alcohol can make the drop in blood pressure that happens when you stand up worse, which may leave you feeling dizzy or faint.
  - S1: Alcohol can make the drop in blood pressure that happens when you stand up worse.
  - S2: This drop in blood pressure may leave you feeling dizzy or faint.

**L158.1** `Simple Sentence` (0.97) → `passthrough`
- original: The same applies to barbiturates and opioid pain medicines.

**L158.2** `Incomplete Sentence` (0.881) → `excluded_incomplete`
- original: Tell your doctor how much you drink so they can advise you.
- pronoun resolved: Tell your doctor how much you drink so doctor can advise you.
  - edits: “they” → “doctor”

**L159.0** `Incomplete Sentence` (0.938) → `excluded_incomplete`
- original: Does hydrochlorothiazide lower your potassium?

**L159.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L160.0** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Yes.

**L160.1** `Compound-Complex Sentence` (0.897) → `decomposed`
- original: Hydrochlorothiazide can lower blood potassium (hypokalemia), and this is more likely at higher doses, when fluid is lost quickly, if you have severe cirrhosis, or after taking the medicine for a long time.
  - S1: Hydrochlorothiazide can lower blood potassium.
  - S2: This condition is known as hypokalemia.
  - S3: This effect is more likely at higher doses.
  - S4: This effect is more likely when fluid is lost quickly.
  - S5: This effect is more likely if you have severe cirrhosis.
  - S6: This effect is more likely after taking the medicine for a long time.

**L160.2** `Simple Sentence` (0.977) → `passthrough`
- original: Your doctor will check your potassium with blood tests.

**L160.3** `Incomplete Sentence` (0.462) → `excluded_incomplete`
- original: Tell them if you have muscle cramps, unusual weakness or tiredness, or an irregular heartbeat.
- pronoun resolved: Tell doctor if you have muscle cramps, unusual weakness or tiredness, or an irregular heartbeat.
  - edits: “them” → “doctor”

**L161.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Should you eat more potassium while taking hydrochlorothiazide?

**L161.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L162.0** `Incomplete Sentence` (0.96) → `excluded_incomplete`
- original: Only if your doctor tells you to.

**L162.1** `Complex Sentence` (0.848) → `decomposed`
- original: Low potassium can sometimes be managed with potassium-rich foods, a potassium supplement, or a different type of diuretic that holds on to potassium.
  - S1: Low potassium can sometimes be managed with potassium-rich foods.
  - S2: Low potassium can sometimes be managed with a potassium supplement.
  - S3: Low potassium can sometimes be managed with a different type of diuretic.
  - S4: This diuretic holds on to potassium.

**L162.2** `Compound-Complex Sentence` (0.676) → `decomposed`
- original: Do not start any of these yourself, because too much potassium can also be harmful, and some people on hydrochlorothiazide do not need extra potassium at all.
  - S1: Do not start any of these yourself.
  - S2: Too much potassium can be harmful.
  - S3: Some people on hydrochlorothiazide do not need extra potassium at all.

**L163.0** `Incomplete Sentence` (0.973) → `excluded_incomplete`
- original: Is hydrochlorothiazide 12.5mg enough?

**L163.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L164.0** `Simple Sentence` (0.971) → `passthrough`
- original: For many people it is.
- pronoun resolved: For many people Hydrochlorothiazide is.
  - edits: “it” → “Hydrochlorothiazide”

**L164.1** `Compound Sentence` (0.81) → `decomposed`
- original: In published trials comparing the two doses, 12.5 mg kept most of the blood pressure reduction seen with 25 mg, and low potassium was consistently less common at 12.5 mg.
  - S1: In published trials comparing the two doses, 12.5 mg kept most of the blood pressure reduction seen with 25 mg.
  - S2: Low potassium was consistently less common at 12.5 mg.

**L164.2** `Simple Sentence` (0.983) → `passthrough`
- original: Starting at 12.5 mg is recommended for adults over 65.

**L164.3** `Compound Sentence` (0.687) → `decomposed`
- original: Your doctor will decide the right dose for you and may adjust it over time.
- pronoun resolved: Your doctor will decide the right dose for you and may adjust dose over time.
  - edits: “it” → “dose”
  - S1: Your doctor will decide the right dose for you.
  - S2: Your doctor may adjust the dose over time.

## Popular FAQ

**L167.0** `Simple Sentence` (0.808) → `passthrough`
- original: Q: What is the best time of day to take blood pressure medication?

**L167.1** `Complex Sentence` (0.932) → `decomposed`
- original: A: Research has suggested that taking your blood pressure medication at night instead of in the morning can provide better blood pressure control at night without compromising daytime blood pressure control and reduce your overall risk of dying because of cardiovascular disease by 45%.
  - S1: Research has suggested that taking your blood pressure medication at night instead of in the morning can provide better blood pressure control at night.
  - S2: This approach does not compromise daytime blood pressure control.
  - S3: It can reduce your overall risk of dying because of cardiovascular disease by 45%.
