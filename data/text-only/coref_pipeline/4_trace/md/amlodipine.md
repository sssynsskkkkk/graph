# Amlodipine — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/amlodipine.txt` · 120 sentences · 11 changed by pronoun resolution · 181 sentences sent to EDC

## What is amlodipine?

**L5.0** `Complex Sentence` (0.714) → `decomposed`
- original: Amlodipine besylate is a prescription medicine used to treat high blood pressure (hypertension) and to prevent certain types of angina (chest pain).
  - S1: Amlodipine besylate is a prescription medicine.
  - S2: It is used to treat high blood pressure (hypertension).
  - S3: It is used to prevent certain types of angina (chest pain).

**L5.1** `Simple Sentence` (0.99) → `passthrough`
- original: It belongs to a class of medications called calcium channel blockers.
- pronoun resolved: Amlodipine besylate belongs to a class of medications called calcium channel blockers.
  - edits: “It” → “Amlodipine besylate”

**L6.0** `Complex Sentence` (0.729) → `decomposed`
- original: Amlodipine besylate works by relaxing and widening the blood vessels, so blood flows more easily which improves blood pressure.
  - S1: Amlodipine besylate works by relaxing and widening the blood vessels.
  - S2: This causes blood to flow more easily.
  - S3: This improves blood pressure.

**L7.0** `Simple Sentence` (0.912) → `passthrough`
- original: Amlodipine besylate controls angina chest pain by increasing the supply of blood to the heart.

**L7.1** `Compound Sentence` (0.945) → `decomposed`
- original: If taken regularly, this medicine controls chest pain, but it does not stop chest pain once it starts.
- pronoun resolved: If taken regularly, Amlodipine besylate controls chest pain, but Amlodipine besylate does not stop chest pain once Amlodipine besylate starts.
  - edits: “this medicine” → “Amlodipine besylate”; “it” → “Amlodipine besylate”; “it” → “Amlodipine besylate”
  - S1: If taken regularly, Amlodipine besylate controls chest pain.
  - S2: Amlodipine besylate does not stop chest pain once Amlodipine besylate starts.

**L7.2** `Simple Sentence` (0.975) → `passthrough`
- original: Your doctor may prescribe a different medication to take when you have chest pain.

**L8.0** `Simple Sentence` (0.433) → `passthrough`
- original: Amlodipine is also used alone or in combination with other medicines to treat high blood pressure (hypertension) in adults and children at least 6 years old.

**L8.1** `Simple Sentence` (0.98) → `passthrough`
- original: Lowering blood pressure may lower your risk of a stroke or heart attack.

**L9.0** `Simple Sentence` (0.863) → `passthrough`
- original: Amlodipine besylate is available as:

**L10.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Amlodipine 5 mg tablets (Norvasc)

**L11.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Amlodipine 10 mg tablets (Norvasc)

**L12.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Amlodipine 2.5 mg tablets (Norvasc)

**L13.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Amlodipine 1 mg/mL solution (Norliqva)

**L14.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Amlodipine 1 mg/mL oral suspension (Katerzia)

**L15.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Amlodipine single-dose powder for oral solution (Sdamlo).

## Amlodipine side effects

**L18.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Common amlodipine side effects:

**L19.0** `Simple Sentence` (0.956) → `passthrough`
- original: The most common amlodipine side may include:

**L20.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: dizziness, drowsiness;

**L21.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: swelling of your legs or ankles;

**L22.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: irregular heartbeat;

**L23.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: pounding heartbeats or fluttering in your chest;

**L24.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: muscle stiffness;

**L25.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: uncontrolled muscle movements;

**L26.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: feeling tired;

**L27.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: stomach pain, nausea; or

**L28.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: flushing (sudden warmth, redness, or tingly feeling).

**L29.0** `Simple Sentence` (0.99) → `passthrough`
- original: Amlodipine besylate may cause serious side effects:

**L30.0** `Compound Sentence` (0.479) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to amlodipine: hives; difficulty breathing; swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to amlodipine.
  - S2: Signs of an allergic reaction to amlodipine include hives.
  - S3: Signs of an allergic reaction to amlodipine include difficulty breathing.
  - S4: Signs of an allergic reaction to amlodipine include swelling of your face, lips, tongue, or throat.

**L31.0** `Complex Sentence` (0.784) → `decomposed`
- original: In rare cases, when you first start taking this medicine, your chest pain may get worse or you could have a heart attack.
  - S1: In rare cases, your chest pain may get worse when you first start taking this medicine.
  - S2: In rare cases, you could have a heart attack when you first start taking this medicine.
  - S3: This medicine is being taken for the first time.

**L31.1** `Compound Sentence` (0.338) → `decomposed`
- original: Seek emergency medical attention or call your doctor right away if you have symptoms such as: chest pain or pressure, pain spreading to your jaw or shoulder, nausea, sweating.
  - S1: Seek emergency medical attention or call your doctor right away if you have symptoms such as chest pain or pressure.
  - S2: Seek emergency medical attention or call your doctor right away if you have symptoms such as pain spreading to your jaw or shoulder.
  - S3: Seek emergency medical attention or call your doctor right away if you have symptoms such as nausea.
  - S4: Seek emergency medical attention or call your doctor right away if you have symptoms such as sweating.

**L32.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L33.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: worsening chest pain; or

**L34.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: a light-headed feeling, like you might pass out.

**L35.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L35.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L35.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## Warnings

**L38.0** `Simple Sentence` (0.517) → `passthrough`
- original: Before taking amlodipine besylate, tell your doctor if you have congestive heart failure or liver disease.

**L39.0** `Compound Sentence` (0.729) → `decomposed`
- original: Drinking alcohol can further lower your blood pressure and may increase certain side effects of amlodipine.
  - S1: Drinking alcohol can further lower your blood pressure.
  - S2: Drinking alcohol may increase certain side effects of amlodipine.

**L40.0** `Simple Sentence` (0.468) → `passthrough`
- original: If you are being treated for high blood pressure, keep using amlodipine even if you feel well.

**L40.1** `Simple Sentence` (0.988) → `passthrough`
- original: High blood pressure often has no symptoms.

**L40.2** `Simple Sentence` (0.976) → `passthrough`
- original: You may need to use blood pressure medication for the rest of your life.

**L41.0** `Complex Sentence` (0.362) → `decomposed`
- original: Amlodipine is only part of a complete program of treatment that may also include diet, exercise, weight control, and other medications.
  - S1: Amlodipine is only part of a complete program of treatment.
  - S2: The program may also include diet, exercise, weight control, and other medications.

**L41.1** `Incomplete Sentence` (0.934) → `excluded_incomplete`
- original: Follow your diet, medication, and exercise routines very closely.

**L42.0** `Incomplete Sentence` (0.929) → `excluded_incomplete`
- original: Tell your doctor about all other heart or blood pressure medications you are taking.

**L43.0** `Simple Sentence` (0.427) → `passthrough`
- original: Your chest pain may become worse when you first start taking amlodipine or when your dose is increased.

**L43.1** `Incomplete Sentence` (0.83) → `excluded_incomplete`
- original: Call your doctor if your chest pain is severe or ongoing.

## Before taking this medicine

**L46.0** `Simple Sentence` (0.987) → `passthrough`
- original: You should not take amlodipine if you are allergic to it.
- pronoun resolved: You should not take amlodipine if you are allergic to Amlodipine.
  - edits: “it.” → “Amlodipine.”

**L47.0** `Simple Sentence` (0.739) → `passthrough`
- original: To make sure this medicine is safe for you, tell your doctor if you have ever had:
- pronoun resolved: To make sure Amlodipine is safe for you, tell your doctor if you have ever had:
  - edits: “this medicine” → “Amlodipine”

**L48.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: severe narrowing of a certain valve in your heart (aortic stenosis), or other heart problems;

**L49.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: coronary artery disease (clogged arteries); or

**L50.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: liver disease.

**L51.0** `Simple Sentence` (0.984) → `passthrough`
- original: It is not known if amlodipine will harm an unborn baby.

**L51.1** `Complex Sentence` (0.338) → `decomposed`
- original: However, having high blood pressure during pregnancy may cause complications or medical problems in both mother and baby.
  - S1: However, having high blood pressure during pregnancy may cause complications.
  - S2: It may also cause medical problems in both mother and baby.

**L51.2** `Simple Sentence` (0.761) → `passthrough`
- original: The benefit of treating hypertension may outweigh any risks to the baby.

**L52.0** `Incomplete Sentence` (0.511) → `excluded_incomplete`
- original: Do not breastfeed while taking amlodipine.

**L52.1** `Simple Sentence` (0.956) → `passthrough`
- original: You can stop breastfeeding or take a different medicine.

## How should I take amlodipine?

**L55.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Take amlodipine exactly as prescribed by your doctor.

**L55.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L55.2** `Simple Sentence` (0.984) → `passthrough`
- original: Your doctor may occasionally change your dose.

**L56.0** `Simple Sentence` (0.99) → `passthrough`
- original: Amlodipine is usually taken once per day.

**L57.0** `Incomplete Sentence` (0.962) → `excluded_incomplete`
- original: Take the medicine at the same time each day, with or without food.
- pronoun resolved: Take Amlodipine at the same time each day, with or without food.
  - edits: “the medicine” → “Amlodipine”

**L58.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Shake the oral suspension (liquid).

**L58.1** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Measure a dose with the supplied measuring device (not a kitchen spoon).

**L59.0** `Complex Sentence` (0.662) → `decomposed`
- original: Amlodipine for oral solution (Sdamlo) comes as a powder that you must mix with water to make a liquid (solution) before taking or giving it.
  - S1: Amlodipine for oral solution (Sdamlo) comes as a powder.
  - S2: You must mix the powder with water.
  - S3: This makes a liquid (solution) before taking or giving it.

**L59.1** `Incomplete Sentence` (0.821) → `excluded_incomplete`
- original: Throw away Sdamlo if you do not take or give it within 60 minutes of mixing and get a new bottle.
- pronoun resolved: Throw away Sdamlo if you do not take or give Sdamlo within 60 minutes of mixing and get a new bottle.
  - edits: “it” → “Sdamlo”

**L59.2** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Do not store mixed Sdamlo.

**L60.0** `Simple Sentence` (0.978) → `passthrough`
- original: Your blood pressure will need to be checked often.

**L61.0** `Simple Sentence` (0.716) → `passthrough`
- original: If you have high blood pressure, keep using amlodipine even if you feel well.

**L61.1** `Simple Sentence` (0.988) → `passthrough`
- original: High blood pressure often has no symptoms.

**L62.0** `Incomplete Sentence` (0.573) → `excluded_incomplete`
- original: Do not change your doses or stop taking any of your medications without your doctor's advice.

**L63.0** `Simple Sentence` (0.95) → `passthrough`
- original: Your treatment may also include diet, exercise, weight control, and blood tests.

**L64.0** `Incomplete Sentence` (0.849) → `excluded_incomplete`
- original: Store amlodipine tablets and oral solution (liquid) at room temperature away from moisture, heat, and light.

**L65.0** `Incomplete Sentence` (0.975) → `excluded_incomplete`
- original: Store amlodipine oral suspension in the refrigerator; do not freeze.

## Amlodipine Dosing Information

**L68.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Amlodipine Adult Dose for Hypertension:

**L69.0** `Complex Sentence` (0.492) → `decomposed`
- original: Initial dose: 5 mg orally once a day Maintenance dose: 5 to 10 mg orally once a day Maximum dose: 10 mg/day Comments: Patients who are small or fragile may be started on 2.5 mg orally once a day.
  - S1: Initial dose: 5 mg orally once a day.
  - S2: Maintenance dose: 5 to 10 mg orally once a day.
  - S3: Maximum dose: 10 mg/day.
  - S4: Patients who are small or fragile may be started on 2.5 mg orally once a day.

**L70.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Angina Pectoris:

**L71.0** `Incomplete Sentence` (0.93) → `excluded_incomplete`
- original: Maintenance dose: 5 to 10 mg orally once a day Maximum dose: 10 mg/day

**L72.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Coronary Artery Disease:

**L73.0** `Incomplete Sentence` (0.93) → `excluded_incomplete`
- original: Maintenance dose: 5 to 10 mg orally once a day Maximum dose: 10 mg/day

**L74.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Geriatric Dose for Hypertension:

**L75.0** `Compound Sentence` (0.515) → `decomposed`
- original: Initial dose: 2.5 mg orally once a day Maintenance dose: 2.5 to 10 mg orally once a day Maximum dose: 10 mg/day.
  - S1: The initial dose is 2.5 mg orally once a day.
  - S2: The maintenance dose is 2.5 to 10 mg orally once a day.
  - S3: The maximum dose is 10 mg/day.

**L76.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Geriatric Dose for Angina Pectoris:

**L77.0** `Incomplete Sentence` (0.77) → `excluded_incomplete`
- original: Initial dose: 5 mg orally once a day Maintenance dose: 5 to 10 mg orally once a day Maximum dose: 10 mg/day..

**L77.1** `Compound-Complex Sentence` (0.684) → `decomposed`
- original: Uses: Alone or in combination with other antianginal agents for the symptomatic treatment of chronic stable angina -Alone or in combination with other antianginal agents for the treatment of confirmed/suspected vasospastic angina -To reduce the risk of hospitalization for angina and to reduce the risk of a coronary revascularization procedure in patients with recently documented CAD by angiography and without heart failure or an ejection fraction less than 40%
  - S1: The drug is used alone or in combination with other antianginal agents for the symptomatic treatment of chronic stable angina.
  - S2: The drug is used alone or in combination with other antianginal agents for the treatment of confirmed or suspected vasospastic angina.
  - S3: The drug is used to reduce the risk of hospitalization for angina.
  - S4: The drug is used to reduce the risk of a coronary revascularization procedure.
  - S5: This use applies to patients with recently documented coronary artery disease by angiography.
  - S6: This use applies to patients without heart failure.
  - S7: This use applies to patients without an ejection fraction less than 40%.

**L78.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Pediatric Dose for Hypertension:

**L79.0** `Compound Sentence` (0.473) → `decomposed`
- original: 6 to 17 years: -Maintenance dose: 2.5 to 5 mg orally once a day -Maximum dose: 5 mg/day Comments: Doses higher than 5 mg have not been studied in pediatric patients.
  - S1: The maintenance dose for patients aged 6 to 17 years is 2.5 to 5 mg orally once a day.
  - S2: The maximum dose is 5 mg per day.
  - S3: Doses higher than 5 mg have not been studied in pediatric patients.

**L79.1** `Simple Sentence` (0.977) → `passthrough`
- original: The dosage should be adjusted according to patient response.

**L79.2** `Simple Sentence` (0.984) → `passthrough`
- original: In general, titration should proceed over 7 to 14 days.

**L79.3** `Complex Sentence` (0.899) → `decomposed`
- original: If clinically warranted, titration may proceed more rapidly, provided the patient is assessed frequently.
  - S1: Titration may proceed more rapidly if clinically warranted.
  - S2: This is provided the patient is assessed frequently.

**L79.4** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Use: Alone or in combination with other antihypertensive agents to treat hypertension

## What happens if I miss a dose?

**L82.0** `Compound Sentence` (0.604) → `decomposed`
- original: Take the medicine as soon as you can, but skip the missed dose if you are more than 12 hours late for the dose.
- pronoun resolved: Take Amlodipine as soon as you can, but skip the missed dose if you are more than 12 hours late for the dose.
  - edits: “the medicine” → “Amlodipine”
  - S1: Take Amlodipine as soon as you can.
  - S2: Skip the missed dose if you are more than 12 hours late for the dose.

**L82.1** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

## What happens if I overdose?

**L85.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L86.0** `Simple Sentence` (0.416) → `passthrough`
- original: Overdose symptoms may include rapid heartbeats, redness or warmth in your arms or legs, or fainting.

## What should I avoid while taking amlodipine?

**L89.0** `Incomplete Sentence` (0.599) → `excluded_incomplete`
- original: Avoid getting up too fast from a sitting or lying position, or you may feel dizzy.

## What other drugs will affect amlodipine?

**L92.0** `Simple Sentence` (0.978) → `passthrough`
- original: Sometimes it is not safe to use certain medicines at the same time.

**L92.1** `Complex Sentence` (0.909) → `decomposed`
- original: Some drugs can affect your blood levels of other drugs you use, which may increase side effects or make the medicines less effective.
  - S1: Some drugs can affect your blood levels of other drugs you use.
  - S2: This may increase side effects.
  - S3: This may make the medicines less effective.

**L93.0** `Complex Sentence` (0.644) → `decomposed`
- original: Other drugs may interact with amlodipine, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may interact with amlodipine.
  - S2: These include prescription and over-the-counter medicines.
  - S3: These also include vitamins and herbal products.

**L93.1** `Incomplete Sentence` (0.967) → `excluded_incomplete`
- original: Tell your doctor about all other medicines you use.

**L94.0** `Incomplete Sentence` (0.946) → `excluded_incomplete`
- original: Tell your doctor if you take simvastatin.

**L94.1** `Simple Sentence` (0.98) → `passthrough`
- original: You should not take more than 20 mg of simvastatin daily while taking amlodipine.

## Popular FAQ

**L97.0** `Simple Sentence` (0.808) → `passthrough`
- original: Q: What is the best time of day to take blood pressure medication?

**L97.1** `Complex Sentence` (0.932) → `decomposed`
- original: A: Research has suggested that taking your blood pressure medication at night instead of in the morning can provide better blood pressure control at night without compromising daytime blood pressure control and reduce your overall risk of dying because of cardiovascular disease by 45%.
  - S1: Research has suggested that taking your blood pressure medication at night instead of in the morning can provide better blood pressure control at night.
  - S2: This approach does not compromise daytime blood pressure control.
  - S3: It can reduce your overall risk of dying because of cardiovascular disease by 45%.

**L98.0** `Incomplete Sentence` (0.888) → `excluded_incomplete`
- original: Q: How long does it take for amlodipine to work?

**L98.1** `Simple Sentence` (0.984) → `passthrough`
- original: A: Amlodipine decreases blood pressure over 4 to 8 hours after a single dose.

**L98.2** `Complex Sentence` (0.946) → `decomposed`
- original: Because the decrease in blood pressure is gradual, a patient's heart rate is not affected because their physiological reflexes (such as an increase in heart rate) are not activated.
  - S1: The decrease in blood pressure is gradual.
  - S2: A patient's heart rate is not affected.
  - S3: Physiological reflexes are not activated.
  - S4: These reflexes include an increase in heart rate.

**L99.0** `Incomplete Sentence` (0.705) → `excluded_incomplete`
- original: Q: How do I reduce swelling from amlodipine?

**L99.1** `Complex Sentence` (0.941) → `decomposed`
- original: A: Swelling from amlodipine is a common, but often troublesome side effect of amlodipine with 5% to 9% of people stopping amlodipine because of it.
  - S1: Swelling from amlodipine is a common side effect of amlodipine.
  - S2: Swelling from amlodipine is often troublesome.
  - S3: 5% to 9% of people stop amlodipine because of swelling.

**L99.2** `Complex Sentence` (0.853) → `decomposed`
- original: If you develop swelling with amlodipine, tell your doctor right away because they may be able to change your blood pressure medications slightly to help reduce the swelling.
- pronoun resolved: If you develop swelling with amlodipine, tell your doctor right away because doctor may be able to change your blood pressure medications slightly to help reduce the swelling.
  - edits: “they” → “doctor”
  - S1: If you develop swelling with amlodipine, tell your doctor right away.
  - S2: The doctor may be able to change your blood pressure medications slightly.
  - S3: This change may help reduce the swelling.

**L99.3** `Complex Sentence` (0.816) → `decomposed`
- original: Swelling caused by amlodipine does not usually respond to treatment with diuretics (such as furosemide) because it is caused by changes in capillary pressure that result in leakage into the spaces between capillaries (called the interstitial area) rather than water retention.
- pronoun resolved: Swelling caused by amlodipine does not usually respond to treatment with diuretics (such as furosemide) because Swelling is caused by changes in capillary pressure that result in leakage into the spaces between capillaries (called the interstitial area) rather than water retention.
  - edits: “it” → “Swelling”
  - S1: Swelling caused by amlodipine does not usually respond to treatment with diuretics.
  - S2: Diuretics include drugs such as furosemide.
  - S3: Swelling is caused by changes in capillary pressure.
  - S4: These changes result in leakage into the spaces between capillaries.
  - S5: These spaces are called the interstitial area.
  - S6: This leakage occurs rather than water retention.

**L100.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Q: Best time to take amlodipine - day or night?

**L100.1** `Simple Sentence` (0.624) → `passthrough`
- original: A: You can take amlodipine in the morning or at night, whichever works best for your schedule.

**L100.2** `Complex Sentence` (0.825) → `decomposed`
- original: The key is to take it at the same time each day to maintain consistent blood levels and support its effectiveness.
- pronoun resolved: The key is to take amlodipine at the same time each day to maintain consistent blood levels and support amlodipine's effectiveness.
  - edits: “it” → “amlodipine”; “its” → “amlodipine's”
  - S1: The key is to take amlodipine at the same time each day.
  - S2: This maintains consistent blood levels.
  - S3: This supports amlodipine's effectiveness.

**L101.0** `Incomplete Sentence` (0.672) → `excluded_incomplete`
- original: Q: How long does amlodipine stay in your system?

**L101.1** `Simple Sentence` (0.967) → `passthrough`
- original: A: Amlodipine can stay in your system for up to 11.5 days after your last dose.

**L101.2** `Complex Sentence` (0.891) → `decomposed`
- original: This is because it has a long elimination half-life of 30 to 50 hours, meaning it takes that long for your body to reduce the drug level by half.
- pronoun resolved: This is because amlodipine has a long elimination half-life of 30 to 50 hours, meaning amlodipine takes that long for your body to reduce the drug level by half.
  - edits: “it” → “amlodipine”; “it” → “amlodipine”
  - S1: This is because amlodipine has a long elimination half-life.
  - S2: The elimination half-life of amlodipine is 30 to 50 hours.
  - S3: This means amlodipine takes that long for your body to reduce the drug level by half.

**L102.0** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Q: Does amlodipine cause weight gain?

**L102.1** `Compound-Complex Sentence` (0.601) → `decomposed`
- original: A: Weight gain has been reported by some people taking amlodipine but this is not a common side effect and some people have also reported weight loss.
  - S1: Some people taking amlodipine have reported weight gain.
  - S2: Weight gain is not a common side effect of amlodipine.
  - S3: Some people taking amlodipine have reported weight loss.

**L102.2** `Complex Sentence` (0.759) → `decomposed`
- original: Weight gain with amlodipine may also be a symptom of edema, which is when you retain fluid, which may be particularly noticeable around your ankles or lower legs.
  - S1: Weight gain with amlodipine may also be a symptom of edema.
  - S2: Edema is when you retain fluid.
  - S3: This fluid retention may be particularly noticeable around your ankles or lower legs.

**L102.3** `Compound Sentence` (0.966) → `decomposed`
- original: The risk of edema is greater in women compared with men and in those people taking a higher dosage of amlodipine, and edema is usually noticed as weight gain.
  - S1: The risk of edema is greater in women compared with men.
  - S2: The risk of edema is greater in those people taking a higher dosage of amlodipine.
  - S3: Edema is usually noticed as weight gain.
