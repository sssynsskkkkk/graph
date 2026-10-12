# Lisinopril — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/lisinopril.txt` · 126 sentences · 13 changed by pronoun resolution · 199 sentences sent to EDC

## What is lisinopril?

**L5.0** `Simple Sentence` (0.958) → `passthrough`
- original: Lisinopril is used alone or in combination with other medications to treat high blood pressure in adults and children 6 years of age and older.

**L6.0** `Compound Sentence` (0.637) → `decomposed`
- original: Lisinopril is also used in adults to treat congestive heart failure and to improve survival after a heart attack.
  - S1: Lisinopril is also used in adults to treat congestive heart failure.
  - S2: It is used to improve survival after a heart attack.

**L7.0** `Simple Sentence` (0.99) → `passthrough`
- original: Lisinopril belongs to a class of medications called angiotensin-converting enzyme (ACE) inhibitors.

**L7.1** `Compound-Complex Sentence` (0.614) → `decomposed`
- original: It works by decreasing certain chemicals that tighten the blood vessels, so blood flows more smoothly and the heart can pump blood more efficiently.
- pronoun resolved: Lisinopril works by decreasing certain chemicals that tighten the blood vessels, so blood flows more smoothly and the heart can pump blood more efficiently.
  - edits: “It” → “Lisinopril”
  - S1: Lisinopril decreases certain chemicals that tighten the blood vessels.
  - S2: Blood flows more smoothly.
  - S3: The heart can pump blood more efficiently.

**L8.0** `Compound Sentence` (0.82) → `decomposed`
- original: High blood pressure is a common condition and when not treated, can cause damage to the brain, heart, blood vessels, kidneys, and other parts of the body.
  - S1: High blood pressure is a common condition.
  - S2: When not treated, it can cause damage to the brain, heart, blood vessels, kidneys, and other parts of the body.

**L8.1** `Compound Sentence` (0.476) → `decomposed`
- original: Damage to these organs may cause heart disease, a heart attack, heart failure, stroke, kidney failure, loss of vision, and other problems.
  - S1: Damage to these organs may cause heart disease.
  - S2: It may cause a heart attack.
  - S3: It may cause heart failure.
  - S4: It may cause a stroke.
  - S5: It may cause kidney failure.
  - S6: It may cause loss of vision.
  - S7: It may cause other problems.

**L8.2** `Complex Sentence` (0.677) → `decomposed`
- original: In addition to taking medication, making lifestyle changes will also help to control your blood pressure.
  - S1: Taking medication will help to control your blood pressure.
  - S2: Making lifestyle changes will also help to control your blood pressure.

**L8.3** `Compound Sentence` (0.652) → `decomposed`
- original: These changes include eating a diet that is low in fat and salt, maintaining a healthy weight, exercising at least 30 minutes most days, not smoking, and using alcohol in moderation.
  - S1: These changes include eating a diet that is low in fat and salt.
  - S2: These changes include maintaining a healthy weight.
  - S3: These changes include exercising at least 30 minutes most days.
  - S4: These changes include not smoking.
  - S5: These changes include using alcohol in moderation.

## Warnings

**L11.0** `Simple Sentence` (0.547) → `passthrough`
- original: Do not use lisinopril if you are pregnant.

**L11.1** `Simple Sentence` (0.989) → `passthrough`
- original: It could harm the unborn baby.
- pronoun resolved: Lisinopril could harm the unborn baby.
  - edits: “It” → “Lisinopril”

**L11.2** `Simple Sentence` (0.631) → `passthrough`
- original: Stop using this medicine and tell your doctor right away if you become pregnant.
- pronoun resolved: Stop using Lisinopril and tell your doctor right away if you become pregnant.
  - edits: “this medicine” → “Lisinopril”

**L12.0** `Simple Sentence` (0.988) → `passthrough`
- original: You should not use this medicine if you have ever had angioedema.
- pronoun resolved: You should not use Lisinopril if you have ever had angioedema.
  - edits: “this medicine” → “Lisinopril”

**L12.1** `Simple Sentence` (0.535) → `passthrough`
- original: Do not take lisinopril within 36 hours before or after taking medicine that contains sacubitril (such as Entresto).

**L13.0** `Complex Sentence` (0.632) → `decomposed`
- original: If you have diabetes, do not use lisinopril together with any medication that contains aliskiren (such as Amturnide, Tekturna, Tekamlo).
  - S1: If you have diabetes, do not use lisinopril together with any medication that contains aliskiren.
  - S2: Examples of medications containing aliskiren include Amturnide, Tekturna, and Tekamlo.

**L14.0** `Simple Sentence` (0.755) → `passthrough`
- original: You may also need to avoid taking lisinopril with aliskiren if you have kidney disease.

## Before taking this medicine

**L17.0** `Complex Sentence` (0.936) → `decomposed`
- original: You should not use lisinopril if you are allergic to it or to any other ACE (angiotensin converting enzyme) inhibitor such as captopril, fosinopril, enalapril, benazepril, moexipril, perindopril, quinapril, ramipril, or trandolapril.
- pronoun resolved: You should not use lisinopril if you are allergic to lisinopril or to any other ACE (angiotensin converting enzyme) inhibitor such as captopril, fosinopril, enalapril, benazepril, moexipril, perindopril, quinapril, ramipril, or trandolapril.
  - edits: “it” → “lisinopril”
  - S1: You should not use lisinopril if you are allergic to lisinopril.
  - S2: You should not use lisinopril if you are allergic to any other ACE inhibitor.
  - S3: Examples of other ACE inhibitors include captopril, fosinopril, enalapril, benazepril, moexipril, perindopril, quinapril, ramipril, or trandolapril.

**L18.0** `Simple Sentence` (0.535) → `passthrough`
- original: Do not take lisinopril within 36 hours before or after taking medicine that contains sacubitril (such as Entresto).

**L19.0** `Simple Sentence` (0.449) → `passthrough`
- original: If you have diabetes, do not take lisinopril with any medication that contains aliskiren (a blood pressure medicine).

**L20.0** `Simple Sentence` (0.838) → `passthrough`
- original: Do not take lisinopril if you have a history of angioedema (severe allergic reaction).

**L21.0** `Simple Sentence` (0.59) → `passthrough`
- original: To make sure this medicine is safe for you, tell your doctor if you have ever had:

**L22.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: heart disease, heart problems such as a recent heart attack;

**L23.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: low blood pressure;

**L24.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: low white blood cell count;

**L25.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: stomach pain;

**L26.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: if you are on a low-salt diet;

**L27.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: diabetes;

**L28.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: liver disease; or

**L29.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: kidney disease (or if you are on dialysis).

**L30.0** `Simple Sentence` (0.755) → `passthrough`
- original: You may also need to avoid taking lisinopril with aliskiren if you have kidney disease.

**L31.0** `Simple Sentence` (0.589) → `passthrough`
- original: Stop using this medicine and tell your doctor right away if you become pregnant.

**L31.1** `Simple Sentence` (0.857) → `passthrough`
- original: Lisinopril can cause injury or death to the unborn baby if you use the medicine during your second or third trimester.

**L32.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Do not breastfeed.

## How should I take lisinopril?

**L35.0** `Incomplete Sentence` (0.973) → `excluded_incomplete`
- original: Take lisinopril exactly as prescribed by your doctor.

**L35.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L35.2** `Simple Sentence` (0.946) → `passthrough`
- original: Your doctor may occasionally change your dose..

**L36.0** `Simple Sentence` (0.975) → `passthrough`
- original: You may take lisinopril with or without food.

**L37.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Measure liquid medicine with the supplied measuring device (not a kitchen spoon).

**L38.0** `Compound Sentence` (0.768) → `decomposed`
- original: Your blood pressure will need to be checked often and you may need frequent blood tests.
  - S1: Your blood pressure will need to be checked often.
  - S2: You may need frequent blood tests.

**L39.0** `Incomplete Sentence` (0.955) → `excluded_incomplete`
- original: Tell your doctor if you have a planned surgery.

**L40.0** `Incomplete Sentence` (0.5) → `excluded_incomplete`
- original: Call your doctor if you have ongoing vomiting or diarrhea, or if you are sweating more than usual.

**L40.1** `Simple Sentence` (0.99) → `passthrough`
- original: You can easily become dehydrated while taking lisinopril.

**L40.2** `Simple Sentence` (0.408) → `passthrough`
- original: This can lead to very low blood pressure, an electrolyte imbalance, or kidney failure.

**L41.0** `Simple Sentence` (0.874) → `passthrough`
- original: If you have high blood pressure, keep using lisinopril even if you feel well.

**L41.1** `Simple Sentence` (0.988) → `passthrough`
- original: High blood pressure often has no symptoms.

**L42.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Store tightly closed at room temperature, away from moisture and heat.

**L42.1** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Do not freeze.

## Dosing information

**L45.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Hypertension:

**L46.0** `Compound Sentence` (0.559) → `decomposed`
- original: Initial dose: 10 mg orally once a day; 5 mg orally once a day Maintenance dose: 20 to 40 mg orally once a day Maximum dose: 80 mg orally once a day Comments: -The initial dose is 5 mg orally once a day in patients receiving a diuretic.
  - S1: The initial dose is 10 mg orally once a day.
  - S2: The maintenance dose is 20 to 40 mg orally once a day.
  - S3: The maximum dose is 80 mg orally once a day.
  - S4: The initial dose is 5 mg orally once a day in patients receiving a diuretic.

**L46.1** `Simple Sentence` (0.522) → `passthrough`
- original: -The 80 mg dose is used but does not appear to give greater effect.

**L46.2** `Complex Sentence` (0.765) → `decomposed`
- original: -If blood pressure is not controlled with lisinopril alone, a low dose of a diuretic may be added (e.g., hydrochlorothiazide, 12.5 mg).
  - S1: If blood pressure is not controlled with lisinopril alone, a low dose of a diuretic may be added.
  - S2: Hydrochlorothiazide is an example of such a diuretic.
  - S3: The dose of hydrochlorothiazide is 12.5 mg.

**L46.3** `Complex Sentence` (0.802) → `decomposed`
- original: After the addition of a diuretic, it may be possible to reduce the dose of lisinopril.
  - S1: It may be possible to reduce the dose of lisinopril.
  - S2: This is after the addition of a diuretic.

**L47.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Congestive Heart Failure:

**L48.0** `Complex Sentence` (0.473) → `decomposed`
- original: Initial dose: 2.5 to 5 mg orally once a day Maintenance dose: Dosage should be increased as tolerated Maximum dose: 40 mg orally once a day Comments: -The diuretic dose may need to be adjusted to help minimize hypovolemia, which may contribute to hypotension.
  - S1: Initial dose: 2.5 to 5 mg orally once a day.
  - S2: Maintenance dose: Dosage should be increased as tolerated.
  - S3: Maximum dose: 40 mg orally once a day.
  - S4: The diuretic dose may need to be adjusted.
  - S5: This adjustment may help minimize hypovolemia.
  - S6: Hypovolemia may contribute to hypotension.

**L48.1** `Compound Sentence` (0.483) → `decomposed`
- original: The appearance of hypotension after the initial dose of lisinopril does not preclude subsequent careful dose titration with the drug.
- pronoun resolved: The appearance of hypotension after the initial dose of lisinopril does not preclude subsequent careful dose titration with lisinopril.
  - edits: “the drug.” → “lisinopril.”
  - S1: The appearance of hypotension after the initial dose of lisinopril does not preclude subsequent careful dose titration.
  - S2: The dose titration involves lisinopril.

**L49.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Myocardial Infarction:

**L50.0** `Compound Sentence` (0.748) → `decomposed`
- original: Initial dose: 5 mg orally (within 24 hours of the onset of acute myocardial infarction) Subsequent doses: 5 mg orally after 24 hours, then 10 mg orally after 48 hours.
  - S1: The initial dose is 5 mg orally within 24 hours of the onset of acute myocardial infarction.
  - S2: Subsequent doses are 5 mg orally after 24 hours.
  - S3: Then, the dose is 10 mg orally after 48 hours.

**L50.1** `Incomplete Sentence` (0.906) → `excluded_incomplete`
- original: Maintenance dose: 10 mg orally once a day.

**L50.2** `Simple Sentence` (0.984) → `passthrough`
- original: Dosing should continue for at least 6 weeks.

**L50.3** `Complex Sentence` (0.799) → `decomposed`
- original: Comments: -Therapy should be initiated at 2.5 mg in patients with a low systolic blood pressure (less than or equal to 120 mm Hg and greater than 100 mmHg) during the first 3 days after the infarct.
  - S1: Therapy should be initiated at 2.5 mg.
  - S2: This applies to patients with a low systolic blood pressure.
  - S3: The low systolic blood pressure is defined as less than or equal to 120 mm Hg and greater than 100 mmHg.
  - S4: Therapy should be initiated during the first 3 days after the infarct.

**L50.4** `Complex Sentence` (0.722) → `decomposed`
- original: If prolonged hypotension occurs (systolic blood pressure less than 90 mmHg for more than 1 hour) therapy should be withdrawn.
  - S1: Therapy should be withdrawn.
  - S2: This occurs if prolonged hypotension happens.
  - S3: Prolonged hypotension is defined as a systolic blood pressure less than 90 mmHg for more than 1 hour.

**L50.5** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Uses: Reduction of mortality in acute myocardial infarction

**L51.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Diabetic Nephropathy:

**L52.0** `Compound Sentence` (0.797) → `decomposed`
- original: Initial dose: 10 to 20 mg orally once a day Maintenance dose: 20 to 40 mg orally once a day Dosage may be titrated upward every 3 days Comments: -Not an approved indication.
  - S1: The initial dose is 10 to 20 mg orally once a day.
  - S2: The maintenance dose is 20 to 40 mg orally once a day.
  - S3: The dosage may be titrated upward every 3 days.
  - S4: This is not an approved indication.

**L53.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Geriatric Dose for Hypertension:

**L54.0** `Compound Sentence` (0.698) → `decomposed`
- original: Initial dose: 2.5 to 5 mg orally once a day Maintenance dose: Dosages should be increased at 2.5 mg to 5 mg per day at 1 to 2 week intervals.
  - S1: Initial dose: 2.5 to 5 mg orally once a day.
  - S2: Maintenance dose: Dosages should be increased at 2.5 mg to 5 mg per day at 1 to 2 week intervals.

**L54.1** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Maximum dose: 40 mg orally once a day

**L55.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Pediatric Dose for Hypertension:

**L56.0** `Complex Sentence` (0.789) → `decomposed`
- original: Pediatric patients greater than or equal to 6 years of age: Initial dose: 0.07 mg/kg orally once a day (Maximum initial dose is 5 mg once a day) Maintenance dose: Dosage should be adjusted according to blood pressure response at 1 to 2 week intervals.
  - S1: Pediatric patients greater than or equal to 6 years of age were studied.
  - S2: The initial dose was 0.07 mg/kg orally once a day.
  - S3: The maximum initial dose is 5 mg once a day.
  - S4: The maintenance dose should be adjusted according to blood pressure response.
  - S5: Adjustments should occur at 1 to 2 week intervals.

**L56.1** `Complex Sentence` (0.452) → `decomposed`
- original: Maximum dose: Doses above 0.61 mg/kg or greater than 40 mg have not been studied in pediatric patients Comments: -This drug is not recommended in pediatric patients less than 6 years old or in pediatric patients with glomerular filtration rate less than 30 mL/min.
  - S1: Maximum dose information is provided.
  - S2: Doses above 0.61 mg/kg have not been studied in pediatric patients.
  - S3: Doses greater than 40 mg have not been studied in pediatric patients.
  - S4: This drug is not recommended in pediatric patients less than 6 years old.
  - S5: This drug is not recommended in pediatric patients with a glomerular filtration rate less than 30 mL/min.

## What happens if I miss a dose?

**L59.0** `Compound Sentence` (0.539) → `decomposed`
- original: Take the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
- pronoun resolved: Take Lisinopril as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - edits: “the medicine” → “Lisinopril”
  - S1: Take Lisinopril as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L59.1** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

## What happens if I overdose?

**L62.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

## What should I avoid while taking lisinopril?

**L65.0** `Incomplete Sentence` (0.599) → `excluded_incomplete`
- original: Avoid getting up too fast from a sitting or lying position, or you may feel dizzy.

**L66.0** `Incomplete Sentence` (0.812) → `excluded_incomplete`
- original: Do not use potassium supplements or salt substitutes, unless your doctor has told you to.

**L67.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: Avoid becoming overheated or dehydrated during exercise, in hot weather, or by not drinking enough fluids.

**L67.1** `Incomplete Sentence` (0.974) → `excluded_incomplete`
- original: Follow your doctor's instructions about the type and amount of liquids you should drink.

**L67.2** `Simple Sentence` (0.92) → `passthrough`
- original: In some cases, drinking too much liquid can be as unsafe as not drinking enough.

## Lisinopril side effects

**L70.0** `Compound Sentence` (0.5) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to lisinopril: severe stomach pain, hives, difficult breathing, swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to lisinopril.
  - S2: Signs of an allergic reaction to lisinopril include severe stomach pain, hives, difficult breathing, and swelling of your face, lips, tongue, or throat.

**L71.0** `Simple Sentence` (0.99) → `passthrough`
- original: Lisinopril may cause serious side effects.

**L71.1** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L72.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a light-headed feeling, like you might pass out;

**L73.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: high blood potassium - nausea, weakness, tingly feeling, chest pain, irregular heartbeats, loss of movement;

**L74.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: low white blood cell counts - fever, mouth sores, skin sores, sore throat, cough;

**L75.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: kidney problems - swelling, urinating less, feeling tired or short of breath; or

**L76.0** `Simple Sentence` (0.507) → `passthrough`
- original: liver problems - loss of appetite, stomach pain (upper right side), tiredness, itching, dark urine, clay-colored stools, jaundice (yellowing of the skin or eyes).

**L77.0** `Simple Sentence` (0.962) → `passthrough`
- original: Common lisinopril side effects may include:

**L78.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: headache, dizziness;

**L79.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: low blood pressure, cough; or

**L80.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: chest pain.

**L81.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L81.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L81.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## What other drugs will affect lisinopril?

**L84.0** `Complex Sentence` (0.658) → `decomposed`
- original: Lisinopril can harm your kidneys, especially if you also use certain medicines for infections, cancer, or osteoporosis.
  - S1: Lisinopril can harm your kidneys.
  - S2: This risk is especially high if you also use certain medicines.
  - S3: These medicines are for infections, cancer, or osteoporosis.

**L85.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Tell your doctor about all your other medicines, especially:

**L86.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: a diuretic or "water pill" that may increase blood potassium such as spironolactone, triamterene, or amiloride;

**L87.0** `Incomplete Sentence` (0.955) → `excluded_incomplete`
- original: NSAIDs (nonsteroidal anti-inflammatory drugs) - aspirin, ibuprofen (Advil, Motrin), naproxen (Aleve), celecoxib, diclofenac, indomethacin, meloxicam, and others;

**L88.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: insulin or diabetes medications;

**L89.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: medicine to prevent organ transplant rejection such as temsirolimus, sirolimus, or everolimus; or

**L90.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: heart or blood pressure medication

**L91.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: lithium

**L92.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: gold injections.

**L93.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L93.1** `Complex Sentence` (0.627) → `decomposed`
- original: Other drugs may interact with lisinopril, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may interact with lisinopril.
  - S2: These include prescription and over-the-counter medicines.
  - S3: These also include vitamins and herbal products.

**L93.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.

## Popular FAQ

**L96.0** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: Q: Which blood pressure medications cause coughing?

**L96.1** `Complex Sentence` (0.652) → `decomposed`
- original: A: Angiotensin-converting enzyme (ACE) inhibitors are a class of prescription blood pressure medications that commonly cause coughing as a side effect.
  - S1: Angiotensin-converting enzyme (ACE) inhibitors are a class of prescription blood pressure medications.
  - S2: These medications commonly cause coughing as a side effect.

**L96.2** `Incomplete Sentence` (0.902) → `excluded_incomplete`
- original: Available medications in this class include...

**L97.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Q: Why does lisinopril cause a dry cough and how to fix it?
- pronoun resolved: Q: Why does lisinopril cause a dry cough and how to fix cough?
  - edits: “it?” → “cough?”

**L97.1** `Simple Sentence` (0.583) → `passthrough`
- original: A: A dry, tickly cough is one of the most common side effects of lisinopril and other ACE inhibitors.

**L97.2** `Simple Sentence` (0.721) → `passthrough`
- original: It is usually not dangerous, but can be very annoying.
- pronoun resolved: Cough is usually not dangerous, but can be very annoying.
  - edits: “It” → “Cough”

**L97.3** `Compound Sentence` (0.868) → `decomposed`
- original: In most people, the cough improves or disappears after the medication is changed, and there are safe alternatives such as ARBs that your clinician can use instead.
  - S1: In most people, the cough improves or disappears after the medication is changed.
  - S2: There are safe alternatives such as ARBs that your clinician can use instead.

**L98.0** `Incomplete Sentence` (0.703) → `excluded_incomplete`
- original: Q: When is the best time to take lisinopril?

**L98.1** `Compound Sentence` (0.835) → `decomposed`
- original: A: Lisinopril is usually taken once a day, and for most people it can be taken in the morning or evening as long as it is taken at the same time every day.
- pronoun resolved: A: Lisinopril is usually taken once a day, and for most people lisinopril can be taken in the morning or evening as long as lisinopril is taken at the same time every day.
  - edits: “it” → “lisinopril”; “it” → “lisinopril”
  - S1: Lisinopril is usually taken once a day.
  - S2: For most people, lisinopril can be taken in the morning or evening.
  - S3: This is as long as lisinopril is taken at the same time every day.

**L98.2** `Complex Sentence` (0.9) → `decomposed`
- original: Morning dosing is common because it fits daily routines and aligns with how blood pressure naturally rises after waking.
- pronoun resolved: Morning dosing is common because lisinopril fits daily routines and aligns with how blood pressure naturally rises after waking.
  - edits: “it” → “lisinopril”
  - S1: Morning dosing is common.
  - S2: This is because lisinopril fits daily routines.
  - S3: It also aligns with how blood pressure naturally rises after waking.

**L99.0** `Incomplete Sentence` (0.944) → `excluded_incomplete`
- original: Q: Does Green Tea interact with any drugs?

**L99.1** `Complex Sentence` (0.771) → `decomposed`
- original: A: Drug interactions with green tea can include certain blood pressure medicines, statin cholesterol-lowering treatments, and warfarin, an anticoagulant (blood thinner) used to help prevent blood clots and medicines used to treat hot flashes and night sweats in women due to menopause.
  - S1: Drug interactions with green tea can include certain blood pressure medicines.
  - S2: Drug interactions with green tea can include statin cholesterol-lowering treatments.
  - S3: Drug interactions with green tea can include warfarin.
  - S4: Warfarin is an anticoagulant used to help prevent blood clots.
  - S5: Drug interactions with green tea can include medicines used to treat hot flashes and night sweats in women due to menopause.

**L100.0** `Incomplete Sentence` (0.616) → `excluded_incomplete`
- original: Q: Can I just stop taking lisinopril?

**L100.1** `Compound Sentence` (0.52) → `decomposed`
- original: A: Lisinopril is a commonly prescribed medication for high blood pressure and heart conditions, but stopping it suddenly without medical advice can be dangerous and is not recommended in most situations.
- pronoun resolved: A: Lisinopril is a commonly prescribed medication for high blood pressure and heart conditions, but stopping Lisinopril suddenly without medical advice can be dangerous and is not recommended in most situations.
  - edits: “it” → “Lisinopril”
  - S1: Lisinopril is a commonly prescribed medication for high blood pressure and heart conditions.
  - S2: Stopping Lisinopril suddenly without medical advice can be dangerous.
  - S3: It is not recommended in most situations.

**L101.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Q: Does lisinopril cause weight gain?

**L101.1** `Simple Sentence` (0.978) → `passthrough`
- original: A: No, lisinopril does not cause weight gain.

**L101.2** `Compound Sentence` (0.967) → `decomposed`
- original: Weight gain was not reported as a side effect in the clinical studies used to approve the drug, and research reviews describe lisinopril as "weight neutral."
- pronoun resolved: Weight gain was not reported as a side effect in the clinical studies used to approve lisinopril, and research reviews describe lisinopril as "weight neutral."
  - edits: “the drug,” → “lisinopril,”
  - S1: Weight gain was not reported as a side effect in the clinical studies used to approve lisinopril.
  - S2: Research reviews describe lisinopril as "weight neutral."

**L101.3** `Complex Sentence` (0.732) → `decomposed`
- original: If you notice the scale going up after starting lisinopril, the cause is usually something else such as fluid buildup, another medicine, or a health condition.
  - S1: If you notice the scale going up after starting lisinopril, the cause is usually something else.
  - S2: The cause is usually fluid buildup.
  - S3: The cause is usually another medicine.
  - S4: The cause is usually a health condition.

**L102.0** `Incomplete Sentence` (0.931) → `excluded_incomplete`
- original: Q: What is the strength of Qbrelis (lisinopril) oral solution?

**L102.1** `Simple Sentence` (0.806) → `passthrough`
- original: A: Qbrelis (lisinopril) Qbrelis (lisinopril) oral solution comes in one strength: 1 milligram per milliliter (1 mg/mL).

**L102.2** `Complex Sentence` (0.449) → `decomposed`
- original: This means every 1 mL of the liquid contains 1 mg of lisinopril, a widely used blood pressure medicine.
  - S1: This means every 1 mL of the liquid contains 1 mg of lisinopril.
  - S2: Lisinopril is a widely used blood pressure medicine.

**L102.3** `Simple Sentence` (0.98) → `passthrough`
- original: Qbrelis is sold as a ready-to-use liquid in a 150 mL bottle.
