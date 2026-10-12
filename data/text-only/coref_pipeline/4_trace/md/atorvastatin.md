# Atorvastatin — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/atorvastatin.txt` · 156 sentences · 19 changed by pronoun resolution · 250 sentences sent to EDC

## What is atorvastatin?

**L5.0** `Compound-Complex Sentence` (0.467) → `decomposed`
- original: Atorvastatin is a prescription medicine used to treat high cholesterol and to reduce the risk of heart attack, stroke, angina, and to decrease the chance that heart surgery will be needed in people who have heart disease or who are at risk of developing heart disease.
  - S1: Atorvastatin is a prescription medicine.
  - S2: Atorvastatin is used to treat high cholesterol.
  - S3: Atorvastatin is used to reduce the risk of heart attack.
  - S4: Atorvastatin is used to reduce the risk of stroke.
  - S5: Atorvastatin is used to reduce the risk of angina.
  - S6: Atorvastatin is used to decrease the chance that heart surgery will be needed.
  - S7: Atorvastatin is used in people who have heart disease.
  - S8: Atorvastatin is used in people who are at risk of developing heart disease.

**L6.0** `Compound Sentence` (0.599) → `decomposed`
- original: Atorvastatin helps lower LDL cholesterol ('bad cholesterol') and triglyceride levels, and increases HDL cholesterol ('good cholesterol') levels, to improve your overall lipid profile.
  - S1: Atorvastatin helps lower LDL cholesterol ('bad cholesterol') and triglyceride levels.
  - S2: It increases HDL cholesterol ('good cholesterol') levels.
  - S3: These actions improve your overall lipid profile.

**L7.0** `Simple Sentence` (0.965) → `passthrough`
- original: Atorvastatin calcium belongs to a class of medications called HMG-CoA reductase inhibitors, commonly referred to as statins.

**L8.0** `Simple Sentence` (0.99) → `passthrough`
- original: Atrovastatin tablets are taken once daily with or without food.

## How does atorvastatin work?

**L11.0** `Complex Sentence` (0.45) → `decomposed`
- original: Atorvastatin works by selectively blocking HMG-CoA reductase, the key enzyme the liver uses to produce cholesterol.
  - S1: Atorvastatin works by selectively blocking HMG-CoA reductase.
  - S2: HMG-CoA reductase is the key enzyme the liver uses to produce cholesterol.

**L11.1** `Complex Sentence` (0.921) → `decomposed`
- original: By slowing this process, it reduces cholesterol production in the liver and increases the number of LDL receptors on liver cells, which helps remove more LDL (“bad”) cholesterol from the bloodstream.
- pronoun resolved: By slowing this process, Atorvastatin reduces cholesterol production in the liver and increases the number of LDL receptors on liver cells, which helps remove more LDL (“bad”) cholesterol from the bloodstream.
  - edits: “it” → “Atorvastatin”
  - S1: Atorvastatin reduces cholesterol production in the liver.
  - S2: Atorvastatin increases the number of LDL receptors on liver cells.
  - S3: This helps remove more LDL ("bad") cholesterol from the bloodstream.
  - S4: Atorvastatin works by slowing this process.

**L12.0** `Compound Sentence` (0.831) → `decomposed`
- original: As a result, it lowers overall LDL levels, decreases the number of LDL particles, and improves the body’s ability to clear cholesterol.
- pronoun resolved: As a result, Atorvastatin lowers overall LDL levels, decreases the number of LDL particles, and improves the body’s ability to clear cholesterol.
  - edits: “it” → “Atorvastatin”
  - S1: As a result, Atorvastatin lowers overall LDL levels.
  - S2: It decreases the number of LDL particles.
  - S3: It improves the body's ability to clear cholesterol.

## What is atrovastatin used for?

**L15.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Atorvastatin FDA-approved uses:

**L16.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: To reduce the risk of cardiovascular events in adults with:

**L17.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Multiple risk factors for coronary heart disease (CHD), but without established CHD.

**L17.1** `Incomplete Sentence` (0.731) → `excluded_incomplete`
- original: Use: to reduce the risk of myocardial infarction (MI), stroke, revascularization procedures, and angina.

**L18.0** `Incomplete Sentence` (0.953) → `excluded_incomplete`
- original: Type 2 diabetes and multiple risk factors for CHD, without established CHD Use: to help reduce the risk of MI and stroke.

**L19.0** `Compound Sentence` (0.331) → `decomposed`
- original: Adults with clinically evident CHD: Use: To reduce the risk of non-fatal MI, fatal and non-fatal stroke, revascularization procedures, hospitalization for congestive heart failure, and angina.
  - S1: Adults with clinically evident CHD should use this to reduce the risk of non-fatal MI.
  - S2: It is used to reduce the risk of fatal and non-fatal stroke.
  - S3: It is used to reduce the risk of revascularization procedures.
  - S4: It is used to reduce the risk of hospitalization for congestive heart failure.
  - S5: It is used to reduce the risk of angina.

**L20.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: As an adjunct to diet to lower LDL-C:

**L21.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Adults with primary hyperlipidemia.

**L22.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Adults and pediatric patients (10 years and older) with heterozygous familial hypercholesterolemia (HeFH).

**L23.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: As an adjunct to other LDL-lowering therapies:

**L24.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: For adults and pediatric patients (10 years and older) with homozygous familial hypercholesterolemia.

**L25.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: As an adjunct to diet for additional lipid disorders in adults:

**L26.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Primary dysbetalipoproteinemia.

**L27.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Hypertriglyceridemia.

## How atorvastatin improves cholesterol and heart health

**L30.0** `Complex Sentence` (0.959) → `decomposed`
- original: When cholesterol and fats build up along your artery walls, in a process called atherosclerosis, they narrow the blood vessels and reduce blood and oxygen flow to your heart, brain, and other parts of your body.
- pronoun resolved: When cholesterol and fats build up along your artery walls, in a process called atherosclerosis, cholesterol and fats narrow the blood vessels and reduce blood and oxygen flow to your heart, brain, and other parts of your body.
  - edits: “they” → “cholesterol and fats”
  - S1: When cholesterol and fats build up along your artery walls.
  - S2: This process is called atherosclerosis.
  - S3: Cholesterol and fats narrow the blood vessels.
  - S4: This reduces blood and oxygen flow to your heart, brain, and other parts of your body.

**L30.1** `Complex Sentence` (0.94) → `decomposed`
- original: By slowing cholesterol production, atorvastatin helps prevent this buildup to keep blood flowing more freely to vital organs.
  - S1: Atorvastatin helps prevent this buildup.
  - S2: This is done by slowing cholesterol production.
  - S3: This keeps blood flowing more freely to vital organs.

**L31.0** `Complex Sentence` (0.787) → `decomposed`
- original: Lowering your blood level of cholesterol and fats with atorvastatin may help prevent heart disease, angina (chest pain), strokes, and heart attacks.
  - S1: Lowering your blood level of cholesterol and fats with atorvastatin may help prevent heart disease.
  - S2: It may also help prevent angina (chest pain).
  - S3: It may also help prevent strokes.
  - S4: It may also help prevent heart attacks.

**L32.0** `Simple Sentence` (0.86) → `passthrough`
- original: Your healthcare provider will check your blood lipid levels regularly to assess how well your treatment is working.

**L32.1** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: These measurements include:

**L33.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: LDL-C: Low-density lipoprotein (“bad” cholesterol)

**L34.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: HDL-C: High-density lipoprotein (“good” cholesterol)

**L35.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: TG: Triglycerides (a type of blood fat)

**L36.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Total-C: Total cholesterol

## Warnings

**L39.0** `Simple Sentence` (0.975) → `passthrough`
- original: You should not take atrovastatin calcium if you have liver disease or cirrhosis.

**L40.0** `Complex Sentence` (0.863) → `decomposed`
- original: Atorvastatin calcium can cause the breakdown of muscle tissue, which can lead to kidney failure.
  - S1: Atorvastatin calcium can cause the breakdown of muscle tissue.
  - S2: The breakdown of muscle tissue can lead to kidney failure.

**L40.1** `Compound Sentence` (0.291) → `decomposed`
- original: Call your doctor right away if you have unexplained muscle pain, tenderness, or weakness, especially if you also have fever, unusual tiredness, or dark urine.
  - S1: Call your doctor right away if you have unexplained muscle pain, tenderness, or weakness.
  - S2: Do so especially if you also have fever, unusual tiredness, or dark urine.

**L41.0** `Simple Sentence` (0.98) → `passthrough`
- original: Serious drug interactions can occur when certain medicines are used together with atrovastatin calcium.

**L41.1** `Incomplete Sentence` (0.745) → `excluded_incomplete`
- original: Tell each of your healthcare providers about all medicines you use now, and any medicine you start or stop using.

**L42.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Avoid drinking more than 1.2 liters of grapefruit juice each day.

**L43.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Avoid eating foods that are high in fat or cholesterol.

**L43.1** `Simple Sentence` (0.99) → `passthrough`
- original: Atrovastatin is often used in conjunction with a cholesterol-lowering diet.

## Atorvastatin side effects

**L46.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Common atorvastatin side effects:

**L47.0** `Complex Sentence` (0.61) → `decomposed`
- original: Common atorvastatin side effects may include pain in your bones, spine, joints, or muscles, muscle spasms, upset stomach, trouble sleeping, stuffy nose, runny nose, sore throat, diarrhea, nausea, or pain in your arms or legs, urinary tract infection with pain and burning when you urinate, painful urination.
  - S1: Common atorvastatin side effects may include pain in your bones, spine, joints, or muscles.
  - S2: Common atorvastatin side effects may include muscle spasms.
  - S3: Common atorvastatin side effects may include upset stomach.
  - S4: Common atorvastatin side effects may include trouble sleeping.
  - S5: Common atorvastatin side effects may include a stuffy nose.
  - S6: Common atorvastatin side effects may include a runny nose.
  - S7: Common atorvastatin side effects may include a sore throat.
  - S8: Common atorvastatin side effects may include diarrhea.
  - S9: Common atorvastatin side effects may include nausea.
  - S10: Common atorvastatin side effects may include pain in your arms or legs.
  - S11: Common atorvastatin side effects may include a urinary tract infection with pain and burning when you urinate.
  - S12: Common atorvastatin side effects may include painful urination.

**L48.0** `Simple Sentence` (0.882) → `passthrough`
- original: Some people taking statins have reported memory loss, forgetfulness, or confusion.

**L48.1** `Simple Sentence` (0.869) → `passthrough`
- original: These symptoms are usually not serious and go away after stopping the medication.
- pronoun resolved: These symptoms are usually not serious and go away after stopping Atorvastatin.
  - edits: “the medication.” → “Atorvastatin.”

**L49.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious atorvastatin side effects

**L50.0** `Complex Sentence` (0.631) → `decomposed`
- original: Allergic reactions: Get emergency medical help if you have signs of an allergic reaction to atorvastatin (hives, difficult breathing, swelling in your face or throat) or a severe skin reaction (fever, sore throat, burning eyes, skin pain, red or purple skin rash with blistering and peeling).
  - S1: Get emergency medical help if you have signs of an allergic reaction to atorvastatin.
  - S2: Signs of an allergic reaction include hives, difficult breathing, and swelling in your face or throat.
  - S3: Get emergency medical help if you have a severe skin reaction.
  - S4: Signs of a severe skin reaction include fever, sore throat, burning eyes, skin pain, and a red or purple skin rash with blistering and peeling.

**L51.0** `Complex Sentence` (0.805) → `decomposed`
- original: Myopathy and Rhabdomyolysis: Atorvastatin calcium can cause the breakdown of muscle tissue, which can lead to kidney failure.
  - S1: Myopathy and Rhabdomyolysis are conditions related to Atorvastatin calcium.
  - S2: Atorvastatin calcium can cause the breakdown of muscle tissue.
  - S3: The breakdown of muscle tissue can lead to kidney failure.

**L51.1** `Compound Sentence` (0.291) → `decomposed`
- original: Call your doctor right away if you have unexplained muscle pain, tenderness, or weakness, especially if you also have fever, unusual tiredness, or dark urine.
  - S1: Call your doctor right away if you have unexplained muscle pain, tenderness, or weakness.
  - S2: Do so especially if you also have fever, unusual tiredness, or dark urine.

**L51.2** `Complex Sentence` (0.4) → `decomposed`
- original: This serious side effect is more likely in older adults and those who have kidney problems, thyroid problems, or take certain other medicines.
  - S1: This serious side effect is more likely in older adults.
  - S2: This serious side effect is more likely in those who have kidney problems.
  - S3: This serious side effect is more likely in those who have thyroid problems.
  - S4: This serious side effect is more likely in those who take certain other medicines.

**L52.0** `Simple Sentence` (0.985) → `passthrough`
- original: Other serious side effects may occur.

**L52.1** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L53.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: muscle weakness in your hips, shoulders, neck, and back;

**L54.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: trouble lifting your arms, trouble climbing, or standing;

**L55.0** `Incomplete Sentence` (0.845) → `excluded_incomplete`
- original: liver problems - loss of appetite, stomach pain (upper right side), tiredness, itching, dark urine, clay-colored stools, jaundice (yellowing of the skin or eyes);

**L56.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: kidney problems - swelling, urinating less, feeling tired or short of breath;

**L57.0** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: high blood sugar - increased thirst, increased urination, dry mouth, fruity breath odor;

**L58.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: new or worsening symptoms of myasthenia gravis (such as muscle weakness, drooping eyelids, double vision, or trouble swallowing, chewing, or breathing).

**L59.0** `Compound Sentence` (0.545) → `decomposed`
- original: This is not a complete list of side effects, and others may occur.
  - S1: This is not a complete list of side effects.
  - S2: Others may occur.

**L59.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L59.2** `Simple Sentence` (0.97) → `passthrough`
- original: You may report side effects to the FDA at 1-800-FDA-1088.

## Warnings

**L62.0** `Simple Sentence` (0.978) → `passthrough`
- original: You should not take atorvastatin if you have liver disease or cirrhosis.

**L63.0** `Complex Sentence` (0.571) → `decomposed`
- original: Atorvastatin can cause the breakdown of muscle tissue, which can lead to kidney failure.
  - S1: Atorvastatin can cause the breakdown of muscle tissue.
  - S2: The breakdown of muscle tissue can lead to kidney failure.

**L63.1** `Compound Sentence` (0.291) → `decomposed`
- original: Call your doctor right away if you have unexplained muscle pain, tenderness, or weakness, especially if you also have fever, unusual tiredness, or dark urine.
  - S1: Call your doctor right away if you have unexplained muscle pain, tenderness, or weakness.
  - S2: Do so especially if you also have fever, unusual tiredness, or dark urine.

**L64.0** `Simple Sentence` (0.986) → `passthrough`
- original: Serious drug interactions can occur when certain medicines are used together with atorvastatin.

**L64.1** `Incomplete Sentence` (0.745) → `excluded_incomplete`
- original: Tell each of your healthcare providers about all medicines you use now, and any medicine you start or stop using.

**L65.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Avoid eating foods that are high in fat or cholesterol.

**L65.1** `Complex Sentence` (0.362) → `decomposed`
- original: Atorvastatin will not be as effective in lowering your cholesterol if you do not follow a cholesterol-lowering diet plan.
  - S1: Atorvastatin will not be as effective in lowering your cholesterol.
  - S2: This is because you do not follow a cholesterol-lowering diet plan.

**L66.0** `Simple Sentence` (0.853) → `passthrough`
- original: Atorvastatin is only part of a complete program of treatment that also includes diet, exercise, and weight control.

**L66.1** `Incomplete Sentence` (0.934) → `excluded_incomplete`
- original: Follow your diet, medication, and exercise routines very closely.

## Before taking this medicine

**L69.0** `Compound Sentence` (0.643) → `decomposed`
- original: You should not use atorvastatin if you are allergic to it, or if you have liver failure or cirrhosis.
- pronoun resolved: You should not use atorvastatin if you are allergic to atorvastatin, or if you have liver failure or cirrhosis.
  - edits: “it,” → “atorvastatin,”
  - S1: You should not use atorvastatin if you are allergic to atorvastatin.
  - S2: You should not use atorvastatin if you have liver failure.
  - S3: You should not use atorvastatin if you have cirrhosis.

**L70.0** `Simple Sentence` (0.739) → `passthrough`
- original: To make sure atorvastatin is safe for you, tell your doctor if you have ever had:

**L71.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: muscle pain or weakness;

**L72.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: diabetes;

**L73.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: stroke;

**L74.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a thyroid disorder;

**L75.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a habit of drinking more than 2 alcoholic beverages per day; or

**L76.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: kidney disease.

**L77.0** `Complex Sentence` (0.571) → `decomposed`
- original: Atorvastatin can cause the breakdown of muscle tissue, which can lead to kidney failure.
  - S1: Atorvastatin can cause the breakdown of muscle tissue.
  - S2: The breakdown of muscle tissue can lead to kidney failure.

**L77.1** `Compound Sentence` (0.474) → `decomposed`
- original: This happens more often in women, in older adults, or people who have kidney disease or poorly controlled hypothyroidism (underactive thyroid).
  - S1: This happens more often in women.
  - S2: This happens more often in older adults.
  - S3: This happens more often in people who have kidney disease.
  - S4: This happens more often in people who have poorly controlled hypothyroidism.

**L78.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Pregnancy:

**L79.0** `Incomplete Sentence` (0.699) → `excluded_incomplete`
- original: Tell your healthcare professional if you are pregnant, or plan to become pregnant, or become pregnant.

**L79.1** `Simple Sentence` (0.989) → `passthrough`
- original: Atorvastatin may harm your unborn baby.

**L79.2** `Simple Sentence` (0.431) → `passthrough`
- original: If you become pregnant, stop taking atorvastatin and call your healthcare provider right away.

**L80.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Breastfeeding:

**L81.0** `Incomplete Sentence` (0.882) → `excluded_incomplete`
- original: Tell your healthcare professional if you are breastfeeding or plan to breastfeed.

**L81.1** `Simple Sentence` (0.958) → `passthrough`
- original: You and your healthcare provider should decide if you will take this medicine or breastfeed.
- pronoun resolved: You and your healthcare provider should decide if you will take Atorvastatin or breastfeed.
  - edits: “this medicine” → “Atorvastatin”

**L81.2** `Simple Sentence` (0.989) → `passthrough`
- original: You should not take atorvastatin if you breastfeed.

**L81.3** `Incomplete Sentence` (0.918) → `excluded_incomplete`
- original: Talk to your healthcare provider about the best way to feed your baby if you take LIPITOR.

## How should I take atorvastatin?

**L84.0** `Incomplete Sentence` (0.952) → `excluded_incomplete`
- original: Take atorvastatin tablet once daily with or without food.

**L84.1** `Simple Sentence` (0.984) → `passthrough`
- original: Many people ask when to take atorvastatin morning or night?

**L84.2** `Compound Sentence` (0.615) → `decomposed`
- original: It can be taken any time of the day, but try and take it at the same time each day.
- pronoun resolved: It can be taken any time of the day, but try and take atorvastatin at the same time each day.
  - edits: “it” → “atorvastatin”
  - S1: It can be taken any time of the day.
  - S2: Try and take atorvastatin at the same time each day.

**L85.0** `Incomplete Sentence` (0.915) → `excluded_incomplete`
- original: Take the liquid medicine on an empty stomach, at least 1 hour before a meal or 2 hours after a meal.

**L85.1** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Shake the oral suspension (liquid).

**L85.2** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Measure a dose with the supplied measuring device (not a kitchen spoon).

**L86.0** `Incomplete Sentence` (0.971) → `excluded_incomplete`
- original: Take atorvastatin exactly as prescribed by your doctor.

**L86.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L86.2** `Simple Sentence` (0.984) → `passthrough`
- original: Your doctor may occasionally change your dose.

**L87.0** `Incomplete Sentence` (0.494) → `excluded_incomplete`
- original: Do not change your dose or stop taking any of your medications without your doctor's advice.

**L88.0** `Compound Sentence` (0.966) → `decomposed`
- original: It may take up to 2 weeks before your cholesterol levels improve, and you may need frequent blood tests.
  - S1: It may take up to 2 weeks before your cholesterol levels improve.
  - S2: You may need frequent blood tests.

**L88.1** `Complex Sentence` (0.926) → `decomposed`
- original: Even if you have no symptoms, tests can help your doctor determine if this medicine is effective.
  - S1: Tests can help your doctor determine if this medicine is effective.
  - S2: This is true even if you have no symptoms.

**L89.0** `Simple Sentence` (0.95) → `passthrough`
- original: Your treatment may also include diet, exercise, weight control, and blood tests.

**L90.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Store at room temperature away from moisture, heat, and light.

**L91.0** `Incomplete Sentence` (0.944) → `excluded_incomplete`
- original: Throw away in the trash any unused liquid 60 days after opening the bottle.

## Atorvastatin Dosing Information

**L94.0** `Simple Sentence` (0.816) → `passthrough`
- original: Recommended Dosage in Adult Patients The recommended starting dosage of Lipitor is 10 mg to 20 mg once daily.

**L94.1** `Simple Sentence` (0.972) → `passthrough`
- original: The dosage range is 10 mg to 80 mg once daily.

**L94.2** `Simple Sentence` (0.867) → `passthrough`
- original: Patients who require a reduction in LDL-C greater than 45% may be started at 40 mg once daily.

**L95.0** `Simple Sentence` (0.48) → `passthrough`
- original: Recommended Dosage in Pediatric Patients 10 Years of Age and Older with HeFH The recommended starting dosage of Lipitor is 10 mg once daily.

**L95.1** `Simple Sentence` (0.975) → `passthrough`
- original: The dosage range is 10 mg to 20 mg once daily.

**L96.0** `Simple Sentence` (0.396) → `passthrough`
- original: Recommended Dosage in Pediatric Patients 10 Years of Age and Older with HoFH The recommended starting dosage of Lipitor is 10 mg to 20 mg once daily.

**L96.1** `Simple Sentence` (0.972) → `passthrough`
- original: The dosage range is 10 mg to 80 mg once daily.

**L97.0** `Compound Sentence` (0.595) → `decomposed`
- original: Comments: Assess LDL-C when clinically appropriate, as early as 4 weeks after initiating Lipitor, and adjust the dosage if necessary.
  - S1: Assess LDL-C when clinically appropriate.
  - S2: Do this as early as 4 weeks after initiating Lipitor.
  - S3: Adjust the dosage if necessary.

**L98.0** `Compound Sentence` (0.46) → `decomposed`
- original: This medicine is available as: atorvastatin 10 mg tablets, atorvastatin 20 mg tablets, atorvastatin 40 mg tablet, 80 mg tablets.
- pronoun resolved: Atorvastatin is available as: atorvastatin 10 mg tablets, atorvastatin 20 mg tablets, atorvastatin 40 mg tablet, 80 mg tablets.
  - edits: “This medicine” → “Atorvastatin”
  - S1: Atorvastatin is available as atorvastatin 10 mg tablets.
  - S2: Atorvastatin is available as atorvastatin 20 mg tablets.
  - S3: Atorvastatin is available as atorvastatin 40 mg tablet.
  - S4: Atorvastatin is available as 80 mg tablets.

**L99.0** `Compound Sentence` (0.965) → `decomposed`
- original: The original brand name of atorvastatin was Lipitor, and now it is also available as a generic.
- pronoun resolved: The original brand name of atorvastatin was Lipitor, and now atorvastatin is also available as a generic.
  - edits: “it” → “atorvastatin”
  - S1: The original brand name of atorvastatin was Lipitor.
  - S2: Now atorvastatin is also available as a generic.

**L99.1** `Simple Sentence` (0.925) → `passthrough`
- original: Atorvastatin calcium oral suspension is also available as the brand Aorvaliq 20mg/5ml.

## What happens if I miss a dose?

**L102.0** `Compound-Complex Sentence` (0.534) → `decomposed`
- original: If you miss a dose of the oral suspension, take it as soon as you remember, but skip the missed dose if you are more than 12 hours late.
- pronoun resolved: If you miss a dose of the oral suspension, take oral suspension as soon as you remember, but skip the missed dose if you are more than 12 hours late.
  - edits: “it” → “oral suspension”
  - S1: You should take the oral suspension as soon as you remember if you miss a dose.
  - S2: You should skip the missed dose if you are more than 12 hours late.

**L102.1** `Compound Sentence` (0.528) → `decomposed`
- original: If you miss a dose of the tablets, do not take the missed dose and wait until your next scheduled dose.
  - S1: If you miss a dose of the tablets, do not take the missed dose.
  - S2: Wait until your next scheduled dose.

**L102.2** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

## What happens if I overdose?

**L105.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

## What should I avoid while taking atorvastatin?

**L108.0** `Compound Sentence` (0.484) → `decomposed`
- original: Avoid eating foods high in fat or cholesterol, or atorvastatin will not be as effective.
  - S1: Avoid eating foods high in fat or cholesterol.
  - S2: Atorvastatin will not be as effective.

**L109.0** `Simple Sentence` (0.991) → `passthrough`
- original: Drinking alcohol may increase your risk of liver damage.

**L110.0** `Simple Sentence` (0.988) → `passthrough`
- original: Grapefruit may interact with atorvastatin and cause side effects.

**L110.1** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Avoid consuming grapefruit products and drinking more than 1.2 liters of grapefruit juice each day.

## What other drugs will affect atorvastatin?

**L113.0** `Simple Sentence` (0.978) → `passthrough`
- original: Sometimes it is not safe to use certain medicines at the same time.

**L113.1** `Complex Sentence` (0.854) → `decomposed`
- original: Some drugs can affect your blood levels of other drugs you use, which can increase the risk of serious muscle problems or make the medicines less effective.
  - S1: Some drugs can affect your blood levels of other drugs you use.
  - S2: This can increase the risk of serious muscle problems.
  - S3: This can make the medicines less effective.

**L114.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Tell your doctor about all your current medicines.

**L114.1** `Simple Sentence` (0.991) → `passthrough`
- original: Many drugs can interact with atorvastatin, especially:

**L115.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: other cholesterol-lowering medicines - gemfibrozil, niacin, fenofibrate, fenofibric acid, and others;

**L116.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: colchicine;

**L117.0** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: antibiotic or antifungal medicine - rifampin, erythromycin, clarithromycin, itraconazole, ketoconazole, posaconazole, and voriconazole;

**L118.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: birth control pills;

**L119.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: medicine to prevent organ transplant rejection; or

**L120.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: antiviral medicine to treat hepatitis C, HIV, or cytomegalovirus (such as letermovir).

**L121.0** `Compound Sentence` (0.901) → `decomposed`
- original: This list is not complete, and many other drugs may interact with atorvastatin.
  - S1: This list is not complete.
  - S2: Many other drugs may interact with atorvastatin.

**L121.1** `Incomplete Sentence` (0.491) → `excluded_incomplete`
- original: This includes prescription and over-the-counter medicines, vitamins, and herbal products.
- pronoun resolved: List includes prescription and over-the-counter medicines, vitamins, and herbal products.
  - edits: “This” → “List”

**L121.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.

## Popular FAQ

**L124.0** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: Q: Best time to take atorvastatin: Morning or Night?

**L124.1** `Complex Sentence` (0.858) → `decomposed`
- original: A: Atorvastatin can generally be taken either in the morning or at night, because it is a long‑acting statin that stays active in the body around the clock.
- pronoun resolved: A: Atorvastatin can generally be taken either in the morning or at night, because Atorvastatin is a long‑acting statin that stays active in the body around the clock.
  - edits: “it” → “Atorvastatin”
  - S1: Atorvastatin can generally be taken either in the morning or at night.
  - S2: This is because Atorvastatin is a long-acting statin.
  - S3: It stays active in the body around the clock.

**L124.2** `Complex Sentence` (0.881) → `decomposed`
- original: The most important factor is taking it at the same time every day so your cholesterol levels and cardiovascular protection remain stable over time.
- pronoun resolved: The most important factor is taking Atorvastatin at the same time every day so your cholesterol levels and cardiovascular protection remain stable over time.
  - edits: “it” → “Atorvastatin”
  - S1: The most important factor is taking Atorvastatin at the same time every day.
  - S2: This ensures your cholesterol levels remain stable over time.
  - S3: This also ensures your cardiovascular protection remains stable over time.

**L125.0** `Incomplete Sentence` (0.716) → `excluded_incomplete`
- original: Q: Rosuvastatin or Atorvastatin: What’s the better choice for you?

**L125.1** `Complex Sentence` (0.95) → `decomposed`
- original: A: Rosuvastatin (Crestor) and atorvastatin (Lipitor) are both statins that lower “bad” LDL cholesterol and reduce the risk of heart attack and stroke in people at increased cardiovascular risk.
  - S1: Rosuvastatin (Crestor) and atorvastatin (Lipitor) are both statins.
  - S2: These statins lower "bad" LDL cholesterol.
  - S3: They reduce the risk of heart attack and stroke.
  - S4: This applies to people at increased cardiovascular risk.

**L125.2** `Compound Sentence` (0.659) → `decomposed`
- original: The better choice for you depends on factors such as how much LDL reduction you need, your medical history, and cost and insurance coverage.
  - S1: The better choice for you depends on factors such as how much LDL reduction you need.
  - S2: It depends on your medical history.
  - S3: It depends on cost and insurance coverage.

**L126.0** `Incomplete Sentence` (0.484) → `excluded_incomplete`
- original: Q: Do I need to eat food when taking atorvastatin?

**L126.1** `Simple Sentence` (0.809) → `passthrough`
- original: A: Atorvastatin (also known as Lipitor) can be taken any time of the day, with or without food.

**L126.2** `Compound Sentence` (0.79) → `decomposed`
- original: An oral dose of atorvastatin will be absorbed rapidly, with maximum plasma concentrations occurring within 1 to 2 hours after you take it.
- pronoun resolved: An oral dose of atorvastatin will be absorbed rapidly, with maximum plasma concentrations occurring within 1 to 2 hours after you take atorvastatin.
  - edits: “it.” → “atorvastatin.”
  - S1: An oral dose of atorvastatin will be absorbed rapidly.
  - S2: Maximum plasma concentrations occur within 1 to 2 hours after you take atorvastatin.

**L126.3** `Complex Sentence` (0.966) → `decomposed`
- original: While you may or may not eat food when taking atorvastatin, there are certain foods you should avoid when taking the drug.
  - S1: You may or may not eat food when taking atorvastatin.
  - S2: There are certain foods you should avoid when taking the drug.
  - S3: The drug is atorvastatin.

**L127.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Q: How long does atorvastatin stay in the system after stopping the drug?
- pronoun resolved: Q: How long does atorvastatin stay in the system after stopping atorvastatin?
  - edits: “the drug?” → “atorvastatin?”

**L127.1** `Simple Sentence` (0.932) → `passthrough`
- original: A: It takes about 77 hours (3 days) for atorvastatin to be out of your system.
- pronoun resolved: A: Atorvastatin takes about 77 hours (3 days) for atorvastatin to be out of your system.
  - edits: “It” → “Atorvastatin”

**L127.2** `Simple Sentence` (0.987) → `passthrough`
- original: The elimination half life of atorvastatin is approximately 14 hours.

**L127.3** `Simple Sentence` (0.952) → `passthrough`
- original: This is the time it takes for your body to reduce plasma drug levels by half.
- pronoun resolved: This is the time atorvastatin takes for your body to reduce plasma drug levels by half.
  - edits: “it” → “atorvastatin”

**L127.4** `Simple Sentence` (0.96) → `passthrough`
- original: It takes approximately 5.5 x elimination half lives for a medicine to be out of ones system.
- pronoun resolved: Atorvastatin takes approximately 5.5 x elimination half lives for a medicine to be out of ones system.
  - edits: “It” → “Atorvastatin”

**L128.0** `Incomplete Sentence` (0.976) → `excluded_incomplete`
- original: Q: Does atorvastatin cause weight gain?

**L128.1** `Compound-Complex Sentence` (0.887) → `decomposed`
- original: A: Atorvastatin itself does not consistently cause weight gain in clinical trials, but some studies suggest a small association between statin use (including atorvastatin) and modest weight gain and higher diabetes risk over time.
- pronoun resolved: A: Atorvastatin Atorvastatin does not consistently cause weight gain in clinical trials, but some studies suggest a small association between statin use (including atorvastatin) and modest weight gain and higher diabetes risk over time.
  - edits: “itself” → “Atorvastatin”
  - S1: Atorvastatin does not consistently cause weight gain in clinical trials.
  - S2: Some studies suggest a small association between statin use and modest weight gain.
  - S3: Some studies suggest a small association between statin use and higher diabetes risk over time.
  - S4: Atorvastatin is a type of statin.

**L128.2** `Complex Sentence` (0.935) → `decomposed`
- original: For most people, the heart‑protective benefits of atorvastatin outweigh these potential metabolic effects, especially when combined with lifestyle measures that support a healthy weight.
  - S1: For most people, the heart-protective benefits of atorvastatin outweigh these potential metabolic effects.
  - S2: This is especially true when combined with lifestyle measures.
  - S3: These lifestyle measures support a healthy weight.

**L129.0** `Incomplete Sentence` (0.936) → `excluded_incomplete`
- original: Q: Can you use limes or lime juice while taking statin drugs (i.e.

**L129.1** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: atorvastatin)?

**L129.2** `Complex Sentence` (0.859) → `decomposed`
- original: A: Limes, pomegranates, pomelos, and Seville oranges can also interact with some medications, including statins such as atorvastatin.
  - S1: Limes, pomegranates, pomelos, and Seville oranges can interact with some medications.
  - S2: Some of these medications include statins.
  - S3: An example of a statin is atorvastatin.

**L129.3** `Simple Sentence` (0.766) → `passthrough`
- original: There just hasn't been as much research published regarding how other types of citrus (apart from grapefruit) interact with statins.

**L129.4** `Compound Sentence` (0.832) → `decomposed`
- original: Large quantities of lime or lime peel should be avoided, although small amounts (such as a twist of lime in a drink) are unlikely to cause a significant interaction.
  - S1: Large quantities of lime or lime peel should be avoided.
  - S2: Small amounts (such as a twist of lime in a drink) are unlikely to cause a significant interaction.
