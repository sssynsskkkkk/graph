# Losartan — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/losartan.txt` · 90 sentences · 12 changed by pronoun resolution · 141 sentences sent to EDC

## What is losartan?

**L5.0** `Simple Sentence` (0.974) → `passthrough`
- original: Losartan is used alone or in combination with other medications to treat high blood pressure in adults and children at least 6 years old.

**L6.0** `Complex Sentence` (0.802) → `decomposed`
- original: Losartan is also used to decrease the risk of stroke in people who have high blood pressure and a heart condition called left ventricular hypertrophy (enlargement of the walls of the left side of the heart).
  - S1: Losartan is also used to decrease the risk of stroke.
  - S2: This use applies to people who have high blood pressure.
  - S3: It also applies to people with a heart condition called left ventricular hypertrophy.
  - S4: Left ventricular hypertrophy is the enlargement of the walls of the left side of the heart.

**L7.0** `Simple Sentence` (0.919) → `passthrough`
- original: Losartan may not decrease the risk of stroke in African Americans who have these conditions.

**L8.0** `Complex Sentence` (0.855) → `decomposed`
- original: Losartan is also used to treat kidney disease in people who have type 2 diabetes (condition in which the body does not use insulin normally and therefore cannot control the amount of sugar in the blood) and high blood pressure.
  - S1: Losartan is also used to treat kidney disease.
  - S2: This treatment is for people who have type 2 diabetes.
  - S3: Type 2 diabetes is a condition in which the body does not use insulin normally.
  - S4: Consequently, the body cannot control the amount of sugar in the blood.
  - S5: Losartan is also used to treat high blood pressure.

**L9.0** `Simple Sentence` (0.988) → `passthrough`
- original: Losartan belongs to a class of medications called angiotensin II receptor antagonists.

**L9.1** `Complex Sentence` (0.877) → `decomposed`
- original: It works by blocking the action of certain natural substances that tighten the blood vessels, allowing the blood to flow more smoothly and the heart to pump more efficiently.
- pronoun resolved: Losartan works by blocking the action of certain natural substances that tighten the blood vessels, allowing the blood to flow more smoothly and the heart to pump more efficiently.
  - edits: “It” → “Losartan”
  - S1: Losartan works by blocking the action of certain natural substances.
  - S2: These substances tighten the blood vessels.
  - S3: Blocking them allows the blood to flow more smoothly.
  - S4: This allows the heart to pump more efficiently.

## Warnings

**L12.0** `Compound Sentence` (0.795) → `decomposed`
- original: Do not use losartan if you are pregnant, and tell your doctor right away if you become pregnant.
  - S1: Do not use losartan if you are pregnant.
  - S2: Tell your doctor right away if you become pregnant.

**L12.1** `Simple Sentence` (0.988) → `passthrough`
- original: It can cause injury or death to the unborn baby.
- pronoun resolved: Losartan can cause injury or death to the unborn baby.
  - edits: “It” → “Losartan”

**L13.0** `Complex Sentence` (0.394) → `decomposed`
- original: If you have diabetes, do not use losartan together with any medication that contains aliskiren (a blood pressure medicine).
  - S1: If you have diabetes, do not use losartan together with any medication that contains aliskiren.
  - S2: Aliskiren is a blood pressure medicine.

**L14.0** `Simple Sentence` (0.873) → `passthrough`
- original: You may also need to avoid taking losartan with aliskiren if you have kidney disease.

**L15.0** `Complex Sentence` (0.894) → `decomposed`
- original: In rare cases, this medicine can cause a condition that results in the breakdown of skeletal muscle tissue, leading to kidney failure.
- pronoun resolved: In rare cases, losartan can cause a condition that results in the breakdown of skeletal muscle tissue, leading to kidney failure.
  - edits: “this medicine” → “losartan”
  - S1: In rare cases, losartan can cause a condition.
  - S2: The condition results in the breakdown of skeletal muscle tissue.
  - S3: The breakdown leads to kidney failure.

**L15.1** `Compound-Complex Sentence` (0.251) → `decomposed`
- original: Call your doctor right away if you have unexplained muscle pain, tenderness, or weakness especially if you also have fever, unusual tiredness, and dark colored urine.
  - S1: Call your doctor right away if you have unexplained muscle pain.
  - S2: Call your doctor right away if you have muscle tenderness.
  - S3: Call your doctor right away if you have muscle weakness.
  - S4: Call your doctor right away if you have a fever.
  - S5: Call your doctor right away if you have unusual tiredness.
  - S6: Call your doctor right away if you have dark colored urine.

## Before taking this medicine

**L18.0** `Simple Sentence` (0.988) → `passthrough`
- original: You should not use losartan if you are allergic to it.
- pronoun resolved: You should not use losartan if you are allergic to losartan.
  - edits: “it.” → “losartan.”

**L19.0** `Complex Sentence` (0.382) → `decomposed`
- original: If you have diabetes, do not take losartan with any medication that contains aliskiren (a blood pressure medicine).
  - S1: If you have diabetes, do not take losartan with any medication that contains aliskiren.
  - S2: Aliskiren is a blood pressure medicine.

**L20.0** `Incomplete Sentence` (0.591) → `excluded_incomplete`
- original: To make sure this medicine is safe for you, tell your doctor if you have ever had:
- pronoun resolved: To make sure losartan is safe for you, tell your doctor if you have ever had:
  - edits: “this medicine” → “losartan”

**L21.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: heart disease or congestive heart failure;

**L22.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: an electrolyte imbalance (such as high levels of potassium in your blood);

**L23.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: if you are on a low-salt diet;

**L24.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: liver disease; or

**L25.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: kidney disease.

**L26.0** `Simple Sentence` (0.873) → `passthrough`
- original: You may also need to avoid taking losartan with aliskiren if you have kidney disease.

**L27.0** `Simple Sentence` (0.559) → `passthrough`
- original: Stop using this medicine and tell your doctor right away if you become pregnant.
- pronoun resolved: Stop using losartan and tell your doctor right away if you become pregnant.
  - edits: “this medicine” → “losartan”

**L27.1** `Simple Sentence` (0.988) → `passthrough`
- original: Losartan can cause injury or death to the unborn baby.

**L28.0** `Simple Sentence` (0.913) → `passthrough`
- original: You should not breastfeed while using this medicine and for 2 days after your last dose.
- pronoun resolved: You should not breastfeed while using losartan and for 2 days after your last dose.
  - edits: “this medicine” → “losartan”

## How should I take losartan?

**L31.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Take losartan exactly as prescribed by your doctor.

**L31.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L31.2** `Simple Sentence` (0.984) → `passthrough`
- original: Your doctor may occasionally change your dose.

**L32.0** `Simple Sentence` (0.982) → `passthrough`
- original: Losartan is usually taken once per day.

**L33.0** `Simple Sentence` (0.947) → `passthrough`
- original: You may take losartan with or without food.

**L34.0** `Incomplete Sentence` (0.47) → `excluded_incomplete`
- original: Call your doctor if you are sick with vomiting or diarrhea, or if you are sweating more than usual.

**L34.1** `Simple Sentence` (0.988) → `passthrough`
- original: You can easily become dehydrated while taking losartan.

**L34.2** `Simple Sentence` (0.714) → `passthrough`
- original: This can lead to very low blood pressure, a serious electrolyte imbalance, or kidney failure.
- pronoun resolved: Dehydrated can lead to very low blood pressure, a serious electrolyte imbalance, or kidney failure.
  - edits: “This” → “Dehydrated”

**L35.0** `Compound Sentence` (0.918) → `decomposed`
- original: Your blood pressure will need to be checked often, and you may need frequent blood tests.
  - S1: Your blood pressure will need to be checked often.
  - S2: You may need frequent blood tests.

**L36.0** `Simple Sentence` (0.585) → `passthrough`
- original: If you have high blood pressure, keep using this medicine even if you feel well.
- pronoun resolved: If you have high blood pressure, keep using Losartan even if you feel well.
  - edits: “this medicine” → “Losartan”

**L36.1** `Simple Sentence` (0.988) → `passthrough`
- original: High blood pressure often has no symptoms.

**L37.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Store tightly closed at room temperature, away from moisture, heat, and light.

## Dosing information

**L40.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Diabetic Nephropathy:

**L41.0** `Complex Sentence` (0.523) → `decomposed`
- original: Initial dose: 50 mg orally once a day Maximum dose: 100 mg orally once a day Comments: -If hypertensive patients with left ventricular hypertrophy or type 2 diabetic nephropathy patients require titration from initial dose, increase to 100 mg orally once a day.
  - S1: The initial dose is 50 mg orally once a day.
  - S2: The maximum dose is 100 mg orally once a day.
  - S3: If hypertensive patients with left ventricular hypertrophy require titration from the initial dose, increase to 100 mg orally once a day.
  - S4: If type 2 diabetic nephropathy patients require titration from the initial dose, increase to 100 mg orally once a day.

**L41.1** `Compound Sentence` (0.956) → `decomposed`
- original: -Antihypertension is substantially present within 1 week but in some studies the maximal effect occurred in 3 to 6 weeks.
  - S1: Antihypertension is substantially present within 1 week.
  - S2: In some studies, the maximal effect occurred in 3 to 6 weeks.

**L41.2** `Incomplete Sentence` (0.979) → `excluded_incomplete`
- original: Uses: -Treatment of hypertension.

**L41.3** `Incomplete Sentence` (0.866) → `excluded_incomplete`
- original: -To reduce the risk of stroke in patients with hypertension and left ventricular hypertrophy.

**L41.4** `Incomplete Sentence` (0.753) → `excluded_incomplete`
- original: -Treatment of diabetic nephropathy with an elevated serum creatinine and proteinuria (urinary albumin to creatinine ratio 300 mg/g or greater) in patients with type 2 diabetes and a history of hypertension.

**L42.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Hypertension:

**L43.0** `Complex Sentence` (0.523) → `decomposed`
- original: Initial dose: 50 mg orally once a day Maximum dose: 100 mg orally once a day Comments: -If hypertensive patients with left ventricular hypertrophy or type 2 diabetic nephropathy patients require titration from initial dose, increase to 100 mg orally once a day.
  - S1: The initial dose is 50 mg orally once a day.
  - S2: The maximum dose is 100 mg orally once a day.
  - S3: If hypertensive patients with left ventricular hypertrophy require titration from the initial dose, increase to 100 mg orally once a day.
  - S4: If type 2 diabetic nephropathy patients require titration from the initial dose, increase to 100 mg orally once a day.

**L43.1** `Compound Sentence` (0.956) → `decomposed`
- original: -Antihypertension is substantially present within 1 week but in some studies the maximal effect occurred in 3 to 6 weeks.
  - S1: Antihypertension is substantially present within 1 week.
  - S2: In some studies, the maximal effect occurred in 3 to 6 weeks.

**L43.2** `Incomplete Sentence` (0.979) → `excluded_incomplete`
- original: Uses: -Treatment of hypertension.

**L43.3** `Incomplete Sentence` (0.866) → `excluded_incomplete`
- original: -To reduce the risk of stroke in patients with hypertension and left ventricular hypertrophy.

**L43.4** `Incomplete Sentence` (0.753) → `excluded_incomplete`
- original: -Treatment of diabetic nephropathy with an elevated serum creatinine and proteinuria (urinary albumin to creatinine ratio 300 mg/g or greater) in patients with type 2 diabetes and a history of hypertension.

**L44.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Pediatric Dose for Hypertension:

**L45.0** `Compound Sentence` (0.41) → `decomposed`
- original: 6 Years or Older: Initial dose: 0.7 mg/kg orally once a day (up to 50 mg total) Comments: -May be given as a tablet or suspension.
  - S1: The initial dose for individuals 6 years or older is 0.7 mg/kg orally once a day, up to a total of 50 mg.
  - S2: This dose may be given as a tablet or suspension.

**L45.1** `Compound Sentence` (0.329) → `decomposed`
- original: If using the suspension, use an oral dosing syringe or an oral dosing cup to measure the prescribed dose.
  - S1: If using the suspension, use an oral dosing syringe to measure the prescribed dose.
  - S2: If using the suspension, use an oral dosing cup to measure the prescribed dose.

**L45.2** `Incomplete Sentence` (0.934) → `excluded_incomplete`
- original: Do not use a teaspoon or tablespoon.

**L45.3** `Simple Sentence` (0.953) → `passthrough`
- original: -Doses above 1.4 mg/kg (or 100 mg) daily have not been studied in pediatric patients.

## What happens if I miss a dose?

**L48.0** `Compound Sentence` (0.576) → `decomposed`
- original: Take the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
- pronoun resolved: Take Losartan as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - edits: “the medicine” → “Losartan”
  - S1: Take Losartan as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L48.1** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

## What happens if I overdose?

**L51.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

## What should I avoid while taking losartan?

**L54.0** `Incomplete Sentence` (0.599) → `excluded_incomplete`
- original: Avoid getting up too fast from a sitting or lying position, or you may feel dizzy.

**L55.0** `Incomplete Sentence` (0.812) → `excluded_incomplete`
- original: Do not use potassium supplements or salt substitutes, unless your doctor has told you to.

## Losartan side effects

**L58.0** `Compound Sentence` (0.508) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to losartan: hives, difficulty breathing, swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to losartan.
  - S2: These signs include hives, difficulty breathing, and swelling of your face, lips, tongue, or throat.

**L59.0** `Simple Sentence` (0.989) → `passthrough`
- original: Losartan may cause serious side effects.

**L59.1** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L60.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a light-headed feeling, like you might pass out;

**L61.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: high blood potassium - nausea, weakness, tingly feeling, chest pain, irregular heartbeats, loss of movement; or

**L62.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: kidney problems - swelling, urinating less, feeling tired or short of breath.

**L63.0** `Simple Sentence` (0.948) → `passthrough`
- original: Common losartan side effects may include:

**L64.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: dizziness, tiredness;

**L65.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: low blood pressure;

**L66.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: low blood sugar;

**L67.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: diarrhea;

**L68.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: back pain; or

**L69.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: cold symptoms such as stuffy nose, sneezing, sore throat.

**L70.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L70.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L70.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## What other drugs will affect losartan?

**L73.0** `Simple Sentence` (0.978) → `passthrough`
- original: Sometimes it is not safe to use certain medicines at the same time.

**L73.1** `Complex Sentence` (0.909) → `decomposed`
- original: Some drugs can affect your blood levels of other drugs you use, which may increase side effects or make the medicines less effective.
  - S1: Some drugs can affect your blood levels of other drugs you use.
  - S2: This may increase side effects.
  - S3: This may make the medicines less effective.

**L74.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Tell your doctor about all your other medicines, especially:

**L75.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: a diuretic or "water pill" that may increase blood potassium such as spironolactone, triamterene, amiloride;

**L76.0** `Incomplete Sentence` (0.385) → `excluded_incomplete`
- original: NSAIDs (nonsteroidal anti-inflammatory drugs) - aspirin, ibuprofen (Advil, Motrin), naproxen (Aleve), celecoxib, diclofenac, indomethacin, meloxicam, and others; or

**L77.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: heart or blood pressure medication.

**L78.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: lithium.

**L79.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L79.1** `Complex Sentence` (0.415) → `decomposed`
- original: Other drugs may affect losartan, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may affect losartan.
  - S2: These other drugs include prescription and over-the-counter medicines.
  - S3: These other drugs also include vitamins and herbal products.

**L79.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.

## Popular FAQ

**L82.0** `Incomplete Sentence` (0.806) → `excluded_incomplete`
- original: Q: Can you eat bananas when taking losartan?

**L82.1** `Simple Sentence` (0.622) → `passthrough`
- original: A: Most people taking losartan can eat bananas, or any other food naturally high in potassium.

**L82.2** `Compound-Complex Sentence` (0.611) → `decomposed`
- original: But people with poor kidney function, heart failure, a history of high potassium, or who also take certain diuretics, such as spironolactone, should be cautious about eating foods high in potassium and ask their doctor to monitor their potassium levels.
- pronoun resolved: But people with poor kidney function, heart failure, a history of high potassium, or who also take certain diuretics, such as spironolactone, should be cautious about eating foods high in potassium and ask people's doctor to monitor people's potassium levels.
  - edits: “their” → “people's”; “their” → “people's”
  - S1: People with poor kidney function should be cautious about eating foods high in potassium.
  - S2: People with heart failure should be cautious about eating foods high in potassium.
  - S3: People with a history of high potassium should be cautious about eating foods high in potassium.
  - S4: People who take certain diuretics, such as spironolactone, should be cautious about eating foods high in potassium.
  - S5: People with poor kidney function should ask their doctor to monitor their potassium levels.
  - S6: People with heart failure should ask their doctor to monitor their potassium levels.
  - S7: People with a history of high potassium should ask their doctor to monitor their potassium levels.
  - S8: People who take certain diuretics, such as spironolactone, should ask their doctor to monitor their potassium levels.

**L83.0** `Incomplete Sentence` (0.957) → `excluded_incomplete`
- original: Q: Does Losartan block COVID-19 Coronavirus Receptors?

**L83.1** `Compound-Complex Sentence` (0.892) → `decomposed`
- original: A: Losartan (Cozaar) does not directly block SARS-CoV-2 coronavirus receptors, but this angiotensin receptor blocker (ARB), may influence COVID-19 outcomes through its effects on the renin-angiotensin-aldosterone system (RAAS).
- pronoun resolved: A: Losartan (Cozaar) does not directly block SARS-CoV-2 coronavirus receptors, but this angiotensin receptor blocker (ARB), may influence COVID-19 outcomes through Losartan's effects on the renin-angiotensin-aldosterone system (RAAS).
  - edits: “its” → “Losartan's”
  - S1: Losartan (Cozaar) does not directly block SARS-CoV-2 coronavirus receptors.
  - S2: Losartan is an angiotensin receptor blocker (ARB).
  - S3: Losartan may influence COVID-19 outcomes.
  - S4: Losartan influences COVID-19 outcomes through its effects on the renin-angiotensin-aldosterone system (RAAS).

**L83.2** `Complex Sentence` (0.922) → `decomposed`
- original: Losartan works by blocking angiotensin II from binding to angiotensin II type 1 receptors (AT1) in the heart, blood vessels, kidneys, and lungs, reducing the activity of RAAS, which lowers blood pressure and may modulate the inflammatory response.
  - S1: Losartan works by blocking angiotensin II from binding to angiotensin II type 1 receptors (AT1).
  - S2: These receptors are located in the heart, blood vessels, kidneys, and lungs.
  - S3: This action reduces the activity of RAAS.
  - S4: Reducing RAAS activity lowers blood pressure.
  - S5: It may also modulate the inflammatory response.
