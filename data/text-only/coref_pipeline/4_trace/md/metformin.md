# Metformin — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/metformin.txt` · 180 sentences · 23 changed by pronoun resolution · 329 sentences sent to EDC

## What is metformin?

**L5.0** `Complex Sentence` (0.654) → `decomposed`
- original: Metformin is a first-line treatment used for type 2 diabetes in adults and children 10 years and older to help improve blood sugar levels.
  - S1: Metformin is a first-line treatment used for type 2 diabetes.
  - S2: It is used in adults and children 10 years and older.
  - S3: It helps improve blood sugar levels.

**L5.1** `Simple Sentence` (0.505) → `passthrough`
- original: It is also used off-label to improve symptoms of polycystic ovarian syndrome (PCOS) and other conditions.
- pronoun resolved: Metformin is also used off-label to improve symptoms of polycystic ovarian syndrome (PCOS) and other conditions.
  - edits: “It” → “Metformin”

**L5.2** `Simple Sentence` (0.972) → `passthrough`
- original: Metformin tablets should be used together with dietary changes and exercise for better results.

**L6.0** `Simple Sentence` (0.991) → `passthrough`
- original: Metformin belongs to the drug class biguanides.

**L7.0** `Compound Sentence` (0.461) → `decomposed`
- original: Metformin works by reducing glucose absorption from the intestines, lowering liver glucose production, and improving insulin sensitivity.
  - S1: Metformin works by reducing glucose absorption from the intestines.
  - S2: It works by lowering liver glucose production.
  - S3: It works by improving insulin sensitivity.

**L7.1** `Complex Sentence` (0.737) → `decomposed`
- original: Managing blood sugar levels with medications like metformin can prevent diabetes complications such as kidney damage, nerve issues, blindness, amputations, sexual dysfunction, and lower the risk of cardiovascular disease.
  - S1: Managing blood sugar levels with medications like metformin can prevent diabetes complications.
  - S2: These complications include kidney damage, nerve issues, blindness, and amputations.
  - S3: Managing blood sugar levels with medications like metformin can also lower the risk of cardiovascular disease.

## Warnings

**L10.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Boxed warning for lactic acidosis:

**L11.0** `Complex Sentence` (0.847) → `decomposed`
- original: Metformin has a boxed warning for lactic acidosis, a dangerous build-up of lactic acid in your blood, which can cause death, hypothermia, hypotension, and resistant bradyarrhythmias.
  - S1: Metformin has a boxed warning for lactic acidosis.
  - S2: Lactic acidosis is a dangerous build-up of lactic acid in your blood.
  - S3: Lactic acidosis can cause death, hypothermia, hypotension, and resistant bradyarrhythmias.

**L11.1** `Simple Sentence` (0.978) → `passthrough`
- original: A boxed warning is the strongest safety-related warning issued by the FDA.

**L12.0** `Compound-Complex Sentence` (0.884) → `decomposed`
- original: This is an extremely rare side effect but certain things can raise your risk of lactic acidosis, including kidney problems, taking certain other medicines, being over 65, having an imaging test that uses contrast dye, having surgery or other medical procedures, conditions that lower oxygen levels in the body, drinking too much alcohol, liver problems, and certain rare inherited metabolic disorders (mitochondrial diseases).
- pronoun resolved: A boxed warning is an extremely rare side effect but certain things can raise your risk of lactic acidosis, including kidney problems, taking certain other medicines, being over 65, having an imaging test that uses contrast dye, having surgery or other medical procedures, conditions that lower oxygen levels in the body, drinking too much alcohol, liver problems, and certain rare inherited metabolic disorders (mitochondrial diseases).
  - edits: “This” → “A boxed warning”
  - S1: A boxed warning is an extremely rare side effect.
  - S2: Certain things can raise your risk of lactic acidosis.
  - S3: Kidney problems can raise your risk of lactic acidosis.
  - S4: Taking certain other medicines can raise your risk of lactic acidosis.
  - S5: Being over 65 can raise your risk of lactic acidosis.
  - S6: Having an imaging test that uses contrast dye can raise your risk of lactic acidosis.
  - S7: Having surgery or other medical procedures can raise your risk of lactic acidosis.
  - S8: Conditions that lower oxygen levels in the body can raise your risk of lactic acidosis.
  - S9: Drinking too much alcohol can raise your risk of lactic acidosis.
  - S10: Liver problems can raise your risk of lactic acidosis.
  - S11: Certain rare inherited metabolic disorders (mitochondrial diseases) can raise your risk of lactic acidosis.

**L13.0** `Incomplete Sentence` (0.466) → `excluded_incomplete`
- original: Stop taking metformin and call your healthcare professional immediately if you have any symptoms of lactic acidosis, including if you feel:

**L14.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: very weak and tired

**L15.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: have unusual (not normal) muscle pain

**L16.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: have trouble breathing

**L17.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: have unusual sleepiness or sleep longer than usual

**L18.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: have unexplained stomach or intestinal problems with nausea and vomiting, or diarrhea

**L19.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: cold, especially in your arms and legs

**L20.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: dizzy or lightheaded

**L21.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: have a slow or irregular heartbeat

**L22.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Other warnings:

**L23.0** `Simple Sentence` (0.991) → `passthrough`
- original: Vitamin B12 deficiency: Metformin can lower your vitamin B12 levels over time.

**L23.1** `Compound Sentence` (0.406) → `decomposed`
- original: Your doctor may check your blood counts every year and your B12 levels every 2 to 3 years to catch any problems early.
  - S1: Your doctor may check your blood counts every year.
  - S2: Your doctor may check your B12 levels every 2 to 3 years.
  - S3: This is done to catch any problems early.

**L24.0** `Complex Sentence` (0.915) → `decomposed`
- original: Low blood sugar when taken with insulin or other diabetes medicines: Taking metformin along with insulin or certain other diabetes drugs (ones that boost insulin release) raises the risk of low blood sugar.
  - S1: Low blood sugar is a risk when taken with insulin or other diabetes medicines.
  - S2: Taking metformin along with insulin or certain other diabetes drugs raises the risk of low blood sugar.
  - S3: These certain other diabetes drugs are ones that boost insulin release.

**L24.1** `Compound Sentence` (0.493) → `decomposed`
- original: If you're on one of these combinations, your doctor may lower the dose of the other medicine.
  - S1: If you're on one of these combinations.
  - S2: Your doctor may lower the dose of the other medicine.

**L25.0** `Complex Sentence` (0.922) → `decomposed`
- original: Macrovascular Outcomes: There have been no clinical studies that clearly show metformin reduces the risk of macrovascular disease, such as diseases or conditions that affect the coronary arteries, the aorta, and large arteries in the brain and limbs.
  - S1: There have been no clinical studies that clearly show metformin reduces the risk of macrovascular disease.
  - S2: Macrovascular disease includes diseases or conditions that affect the coronary arteries, the aorta, and large arteries in the brain and limbs.

## Metformin side effects

**L28.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Common side effects:

**L29.0** `Complex Sentence` (0.36) → `decomposed`
- original: Common side effects of metformin hydrochloride tablets include diarrhea, nausea, vomiting, wind (flatulence), indigestion, and headache.
  - S1: Common side effects of metformin hydrochloride tablets include diarrhea, nausea, vomiting, wind (flatulence), indigestion, and headache.

**L29.1** `Complex Sentence` (0.496) → `decomposed`
- original: These side effects occurred in 5% or more of patients in the US clinical trial of using metformin for type 2 diabetic patients.
  - S1: These side effects occurred in 5% or more of patients.
  - S2: The patients were in the US clinical trial.
  - S3: The trial was for using metformin for type 2 diabetic patients.

**L29.2** `Simple Sentence` (0.497) → `passthrough`
- original: In the same study, 6% of patients discontinued metformin due to diarrhea.

**L30.0** `Compound Sentence` (0.469) → `decomposed`
- original: Less common side effects were abnormal stools, hypoglycemia, myalgia, lightheadedness, dyspnea, nail disorder, rash, increased sweating, taste disorder, chest discomfort, chills, flu syndrome, flushing, and palpitation, which occurred between 1% and less than 5% of patients.
  - S1: Less common side effects were abnormal stools, hypoglycemia, myalgia, lightheadedness, dyspnea, nail disorder, rash, increased sweating, taste disorder, chest discomfort, chills, flu syndrome, flushing, and palpitation.
  - S2: These side effects occurred between 1% and less than 5% of patients.

**L31.0** `Compound Sentence` (0.896) → `decomposed`
- original: Taking your medicine with meals can help reduce these side effects, and you may find the slow-release tablets reduce gastric side effects.
  - S1: Taking your medicine with meals can help reduce these side effects.
  - S2: You may find the slow-release tablets reduce gastric side effects.

**L31.1** `Compound Sentence` (0.613) → `decomposed`
- original: Tell your doctor if the side effects bother you a lot, last for more than a few weeks, come back after they've gone away, or start later in therapy.
  - S1: Tell your doctor if the side effects bother you a lot.
  - S2: Tell your doctor if the side effects last for more than a few weeks.
  - S3: Tell your doctor if the side effects come back after they've gone away.
  - S4: Tell your doctor if the side effects start later in therapy.

**L31.2** `Simple Sentence` (0.503) → `passthrough`
- original: You may need a lower dose or need to stop taking the medicine for a short period or for good.

**L32.0** `Simple Sentence` (0.98) → `passthrough`
- original: Metformin rarely causes hypoglycemia (low blood sugar) by itself.

**L32.1** `Compound Sentence` (0.564) → `decomposed`
- original: However, hypoglycemia can happen if you do not eat enough, if you drink alcohol, or if you take other medicines to lower blood sugar.
  - S1: However, hypoglycemia can happen if you do not eat enough.
  - S2: Hypoglycemia can happen if you drink alcohol.
  - S3: Hypoglycemia can happen if you take other medicines to lower blood sugar.

**L33.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious side effects:

**L34.0** `Compound Sentence` (0.415) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to metformin: hives; difficult breathing; swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to metformin.
  - S2: Signs of an allergic reaction to metformin include hives.
  - S3: Signs of an allergic reaction to metformin include difficult breathing.
  - S4: Signs of an allergic reaction to metformin include swelling of your face, lips, tongue, or throat.

**L35.0** `Complex Sentence` (0.501) → `decomposed`
- original: This medicine can rarely cause patients to develop lactic acidosis, which can be fatal.
  - S1: This medicine can rarely cause patients to develop lactic acidosis.
  - S2: Lactic acidosis can be fatal.

**L35.1** `Simple Sentence` (0.802) → `passthrough`
- original: See the “Warnings - Boxed Warning” for more details.

**L36.0** `Compound-Complex Sentence` (0.318) → `decomposed`
- original: Call your doctor at once if you have signs of liver problems, such as upper stomach pain, loss of appetite, dark urine, clay-colored stools, or yellowing of your skin or eyes (jaundice).
  - S1: Call your doctor at once if you have signs of liver problems.
  - S2: Upper stomach pain is a sign of liver problems.
  - S3: Loss of appetite is a sign of liver problems.
  - S4: Dark urine is a sign of liver problems.
  - S5: Clay-colored stools are a sign of liver problems.
  - S6: Yellowing of your skin or eyes is a sign of liver problems.
  - S7: Yellowing of your skin or eyes is jaundice.

## Contraindications

**L39.0** `Simple Sentence` (0.826) → `passthrough`
- original: You should not use metformin if you have:

**L40.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: severe kidney disease, or

**L41.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: metabolic acidosis or diabetic ketoacidosis (call your doctor for treatment), or

**L42.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: an allergy to metformin or any of the inactive ingredients in this medicine.

## Before taking this medicine

**L45.0** `Complex Sentence` (0.926) → `decomposed`
- original: If you need to have surgery or any type of x-ray or CT scan using a dye that is injected into your veins, you may need to temporarily stop taking metformin.
  - S1: You may need to temporarily stop taking metformin.
  - S2: This is needed if you have surgery.
  - S3: This is also needed for any type of x-ray or CT scan.
  - S4: These scans use a dye injected into your veins.

**L45.1** `Incomplete Sentence` (0.635) → `excluded_incomplete`
- original: Be sure your caregivers know ahead of time that you are using this medication.
- pronoun resolved: Be sure your caregivers know ahead of time that you are using metformin.
  - edits: “this medication.” → “metformin.”

**L46.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Tell your doctor if you have ever had:

**L47.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: kidney disease (your kidney function may need to be checked before you take this medicine);
- pronoun resolved: kidney disease (your kidney function may need to be checked before you take metformin);
  - edits: “this medicine);” → “metformin);”

**L48.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: high ketone levels in your blood or urine;

**L49.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: heart disease, congestive heart failure;

**L50.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: liver disease or liver impairment

**L51.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: if you also use insulin, or other oral diabetes medications.

**L52.0** `Simple Sentence` (0.978) → `passthrough`
- original: You may develop lactic acidosis, a dangerous build-up of lactic acid in your blood.

**L52.1** `Complex Sentence` (0.44) → `decomposed`
- original: This may be more likely if you have other medical conditions, a severe infection, chronic alcoholism, or if you are 65 or older.
- pronoun resolved: Lactic acidosis may be more likely if you have other medical conditions, a severe infection, chronic alcoholism, or if you are 65 or older.
  - edits: “This” → “Lactic acidosis”
  - S1: Lactic acidosis may be more likely if you have other medical conditions.
  - S2: Lactic acidosis may be more likely if you have a severe infection.
  - S3: Lactic acidosis may be more likely if you have chronic alcoholism.
  - S4: Lactic acidosis may be more likely if you are 65 or older.

**L52.2** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Ask your doctor about your risk.

**L53.0** `Simple Sentence` (0.98) → `passthrough`
- original: Metformin immediate release tablets should not be given to a child younger than 10 years old.

**L54.0** `Simple Sentence` (0.992) → `passthrough`
- original: This medicine should not be used for type 1 diabetes.
- pronoun resolved: Metformin should not be used for type 1 diabetes.
  - edits: “This medicine” → “Metformin”

**L55.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Pregnancy:

**L56.0** `Incomplete Sentence` (0.937) → `excluded_incomplete`
- original: Follow your doctor's instructions about using metformin if you are pregnant or you become pregnant.

**L56.1** `Compound Sentence` (0.965) → `decomposed`
- original: Controlling diabetes is very important during pregnancy, and having high blood sugar may cause complications in both the mother and the baby.
  - S1: Controlling diabetes is very important during pregnancy.
  - S2: Having high blood sugar may cause complications in both the mother and the baby.

**L56.2** `Incomplete Sentence` (0.894) → `excluded_incomplete`
- original: Tell your doctor if you become pregnant while taking metformin.

**L57.0** `Compound Sentence` (0.869) → `decomposed`
- original: Metformin may stimulate ovulation in some women and may increase the risk of unintended pregnancy.
  - S1: Metformin may stimulate ovulation in some women.
  - S2: Metformin may increase the risk of unintended pregnancy.

**L57.1** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Talk to your doctor about your risk.

**L58.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Breastfeeding:

**L59.0** `Incomplete Sentence` (0.935) → `excluded_incomplete`
- original: Talk to your healthcare provider if you are breastfeeding or plan to breastfeed.

**L59.1** `Simple Sentence` (0.991) → `passthrough`
- original: Metformin can pass into your breast milk.

**L59.2** `Simple Sentence` (0.501) → `passthrough`
- original: Your healthcare provider will be able to advise you about the best way to feed your baby while you take this medicine.
- pronoun resolved: Your healthcare provider will be able to advise you about the best way to feed your baby while you take Metformin.
  - edits: “this medicine.” → “Metformin.”

## How should I take metformin?

**L62.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Take metformin exactly as prescribed by your doctor.

**L62.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L62.2** `Simple Sentence` (0.984) → `passthrough`
- original: Your doctor may occasionally change your dose.

**L62.3** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Use the medicine exactly as directed.
- pronoun resolved: Use metformin exactly as directed.
  - edits: “the medicine” → “metformin”

**L63.0** `Incomplete Sentence` (0.91) → `excluded_incomplete`
- original: Take metformin with a meal, unless your doctor tells you otherwise.

**L63.1** `Simple Sentence` (0.987) → `passthrough`
- original: Some forms of metformin are taken only once daily with the evening meal.

**L63.2** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Follow your doctor's instructions.

**L64.0** `Incomplete Sentence` (0.902) → `excluded_incomplete`
- original: Take immediate release tablets in divided doses 2 to 3 times a day with meals.

**L64.1** `Simple Sentence` (0.967) → `passthrough`
- original: Your dose will be increased slowly to minimise gastrointestinal side effects.

**L65.0** `Incomplete Sentence` (0.588) → `excluded_incomplete`
- original: Do not crush, chew, or break an extended-release tablet.

**L65.1** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Swallow it whole.

**L66.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Measure liquid medicine carefully.

**L66.1** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Shake the oral suspension before you measure a dose.

**L66.2** `Incomplete Sentence` (0.955) → `excluded_incomplete`
- original: Use the dosing syringe provided, or use a medicine dose-measuring device (not a kitchen spoon).

**L67.0** `Simple Sentence` (0.969) → `passthrough`
- original: Some tablets are made with a shell that is not absorbed or melted in the body.

**L67.1** `Simple Sentence` (0.984) → `passthrough`
- original: Part of this shell may appear in your stool.

**L67.2** `Simple Sentence` (0.945) → `passthrough`
- original: This is normal and will not make the medicine less effective.
- pronoun resolved: This is normal and will not make metformin less effective.
  - edits: “the medicine” → “metformin”

**L68.0** `Compound Sentence` (0.783) → `decomposed`
- original: You may have low blood sugar (hypoglycemia) and feel very hungry, dizzy, irritable, confused, anxious, or shaky.
  - S1: You may have low blood sugar (hypoglycemia).
  - S2: You may feel very hungry, dizzy, irritable, confused, anxious, or shaky.

**L68.1** `Complex Sentence` (0.471) → `decomposed`
- original: To quickly treat hypoglycemia, eat or drink a fast-acting source of sugar (fruit juice, hard candy, crackers, raisins, or non-diet soda).
  - S1: To quickly treat hypoglycemia, eat or drink a fast-acting source of sugar.
  - S2: Examples of fast-acting sources of sugar include fruit juice, hard candy, crackers, raisins, or non-diet soda.

**L69.0** `Simple Sentence` (0.594) → `passthrough`
- original: Your doctor may prescribe a glucagon injection kit in case you have severe hypoglycemia.

**L69.1** `Incomplete Sentence` (0.628) → `excluded_incomplete`
- original: Be sure your family or close friends know how to give you this injection in an emergency.

**L70.0** `Simple Sentence` (0.823) → `passthrough`
- original: Blood sugar levels can be affected by stress, illness, surgery, exercise, alcohol use, or skipping meals.

**L70.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Ask your doctor before changing your dose or medication schedule.

**L71.0** `Complex Sentence` (0.595) → `decomposed`
- original: Metformin is only part of a complete treatment program that may also include diet, exercise, weight control, regular blood sugar testing, and special medical care.
  - S1: Metformin is only part of a complete treatment program.
  - S2: The program may also include diet, exercise, weight control, regular blood sugar testing, and special medical care.

**L71.1** `Incomplete Sentence` (0.969) → `excluded_incomplete`
- original: Follow your doctor's instructions very closely.

**L72.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Store at room temperature away from moisture, heat, and light.

**L73.0** `Simple Sentence` (0.979) → `passthrough`
- original: Your doctor may have you take extra vitamin B12 while you are taking this medicine.

**L73.1** `Incomplete Sentence` (0.914) → `excluded_incomplete`
- original: Take only the amount of vitamin B12 that your doctor has prescribed.

## Metformin dose Information

**L76.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Metformin Dose for Diabetes Type 2:

**L77.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Immediate-release tablets:

**L78.0** `Compound Sentence` (0.728) → `decomposed`
- original: Initial dose: 500 mg orally twice a day or 850 mg orally once a day Dose titration: Increase by 500 mg increments weekly or 850 mg every 2 weeks as tolerated.
  - S1: Initial dose: 500 mg orally twice a day or 850 mg orally once a day.
  - S2: Dose titration: Increase by 500 mg increments weekly or 850 mg every 2 weeks as tolerated.

**L78.1** `Incomplete Sentence` (0.927) → `excluded_incomplete`
- original: Maintenance dose: 2000 mg/day in divided doses Maximum dose: 2550 mg/day.

**L78.2** `Simple Sentence` (0.981) → `passthrough`
- original: Doses above 2,000 mg may be better tolerated given 3 times

**L79.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Extended-release tablets:

**L80.0** `Incomplete Sentence` (0.675) → `excluded_incomplete`
- original: Initial dose: 500 to 1000 mg orally once a day Dose titration: Increase in 500 mg increments weekly as tolerated Maximum dose: 2000 mg/day

**L81.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Usual Pediatric Dose for Diabetes Type 2 (10 years or older):

**L82.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Immediate-release tablets:

**L83.0** `Compound Sentence` (0.304) → `decomposed`
- original: Initial dose: 500 mg orally twice a day Dose titration: Increase in 500 mg increments weekly as tolerated; daily dose should be taken in divided doses 2 to 3 times a day with meals Maximum dose: 2000 mg/day
  - S1: Initial dose: 500 mg orally twice a day.
  - S2: Dose titration: Increase in 500 mg increments weekly as tolerated.
  - S3: Daily dose should be taken in divided doses 2 to 3 times a day with meals.
  - S4: Maximum dose: 2000 mg/day.

**L84.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Extended-release oral suspension:

**L85.0** `Compound Sentence` (0.513) → `decomposed`
- original: Initial dose: 500 mg orally once a day with evening meal Dose titration: Increase in 500 mg increments weekly based on glycemic control and tolerability Maximum dose: 2000 mg/day
  - S1: Initial dose: 500 mg orally once a day with evening meal.
  - S2: Dose titration: Increase in 500 mg increments weekly based on glycemic control and tolerability.
  - S3: Maximum dose: 2000 mg/day.

**L86.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Renal Impairment:

**L87.0** `Simple Sentence` (0.846) → `passthrough`
- original: Before starting treatment, assess renal function with estimated glomerular filtration rate (eGFR)

**L88.0** `Incomplete Sentence` (0.915) → `excluded_incomplete`
- original: Do not use this medicine in patients with eGFR below 30 mL/minute/1.73 m 2
- pronoun resolved: Do not use Metformin in patients with eGFR below 30 mL/minute/1.73 m 2
  - edits: “this medicine” → “Metformin”

**L89.0** `Simple Sentence` (0.694) → `passthrough`
- original: It is not recommended to start metformin tablets in patients with eGFR between 30 to 45 mL/minute/1.73 m 2

**L90.0** `Simple Sentence` (0.768) → `passthrough`
- original: While taking this medicine, assess the risk/benefit of continuing if eGFR falls below 45 mL/minute/1.73 m 2
- pronoun resolved: While taking Metformin, assess the risk/benefit of continuing if eGFR falls below 45 mL/minute/1.73 m 2
  - edits: “this medicine,” → “Metformin,”

**L91.0** `Simple Sentence` (0.982) → `passthrough`
- original: If eGFR falls below 30 mL/minute/1.73 m 2 discontinue this medication
- pronoun resolved: If eGFR falls below 30 mL/minute/1.73 m 2 discontinue Metformin
  - edits: “this medication” → “Metformin”

**L92.0** `Simple Sentence` (0.968) → `passthrough`
- original: Metformin immediate release tablets are available as 500 mg, 850 mg, and 1,000 mg tablets.

**L93.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Hepatic Impairment:

**L94.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Avoid use in patients with hepatic impairment.

## What happens if I miss a dose?

**L97.0** `Compound Sentence` (0.555) → `decomposed`
- original: Take the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - S1: Take the medicine as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L97.1** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

## What happens if I overdose?

**L100.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L100.1** `Simple Sentence` (0.988) → `passthrough`
- original: An overdose can cause severe hypoglycemia or lactic acidosis.

## What to avoid

**L103.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Avoid drinking alcohol.

**L103.1** `Simple Sentence` (0.883) → `passthrough`
- original: It lowers blood sugar and may increase your risk of lactic acidosis.
- pronoun resolved: Metformin lowers blood sugar and may increase your risk of lactic acidosis.
  - edits: “It” → “Metformin”

## What other drugs will affect metformin?

**L106.0** `Compound Sentence` (0.529) → `decomposed`
- original: Many drugs can interact with metformin; this includes prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Many drugs can interact with metformin.
  - S2: This includes prescription and over-the-counter medicines, vitamins, and herbal products.

**L106.1** `Simple Sentence` (0.949) → `passthrough`
- original: Not all possible interactions are listed here.

**L106.2** `Incomplete Sentence` (0.904) → `excluded_incomplete`
- original: Tell your doctor about all your current medicines and any medicine you start or stop using.

**L107.0** `Complex Sentence` (0.938) → `decomposed`
- original: Medicines that have a carbonic anhydrase inhibiting effect like topiramate (often used for seizures or migraines), zonisamide (used for seizures), acetazolamide (used for glaucoma, altitude sickness, and other conditions), and dichlorphenamide (used for a muscle condition called periodic paralysis) can raise the risk of a rare but serious condition called lactic acidosis when taken with metformin.
  - S1: Medicines that have a carbonic anhydrase inhibiting effect can raise the risk of a rare but serious condition called lactic acidosis when taken with metformin.
  - S2: Topiramate is often used for seizures or migraines.
  - S3: Zonisamide is used for seizures.
  - S4: Acetazolamide is used for glaucoma, altitude sickness, and other conditions.
  - S5: Dichlorphenamide is used for a muscle condition called periodic paralysis.

**L107.1** `Complex Sentence` (0.859) → `decomposed`
- original: These medicines commonly lower a substance in your blood called bicarbonate, which your body needs to keep its acid levels balanced.
  - S1: These medicines commonly lower a substance in your blood called bicarbonate.
  - S2: Your body needs bicarbonate to keep its acid levels balanced.

**L107.2** `Complex Sentence` (0.889) → `decomposed`
- original: If you're taking metformin along with any of these medicines, your doctor may want to monitor you more closely.
- pronoun resolved: If you're taking metformin along with any of Medicines that have a carbonic anhydrase inhibiting effect, your doctor may want to monitor you more closely.
  - edits: “these medicines,” → “Medicines that have a carbonic anhydrase inhibiting effect,”
  - S1: If you're taking metformin along with any of Medicines that have a carbonic anhydrase inhibiting effect.
  - S2: Your doctor may want to monitor you more closely.

**L108.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Other medicines that may increase risk of lactic acidosis.

**L108.1** `Complex Sentence` (0.89) → `decomposed`
- original: Some medicines including cimetidine (used for heartburn), ranolazine (used for chest pain/angina), dolutegravir (used to treat HIV), and vandetanib (used to treat certain thyroid cancers) can all cause metformin levels to increase.
  - S1: Some medicines can cause metformin levels to increase.
  - S2: Cimetidine is used for heartburn.
  - S3: Ranolazine is used for chest pain/angina.
  - S4: Dolutegravir is used to treat HIV.
  - S5: Vandetanib is used to treat certain thyroid cancers.

**L108.2** `Simple Sentence` (0.96) → `passthrough`
- original: They do this by blocking the same pathway your kidneys use to clear metformin out of your system.

**L108.3** `Complex Sentence` (0.954) → `decomposed`
- original: Since higher metformin levels raise the risk of lactic acidosis, your doctor will weigh the benefits and risks before prescribing any of these together with metformin.
  - S1: Higher metformin levels raise the risk of lactic acidosis.
  - S2: Your doctor will weigh the benefits and risks.
  - S3: The doctor will do this before prescribing any of these together with metformin.

**L109.0** `Complex Sentence` (0.335) → `decomposed`
- original: Insulin or other diabetes medicines that raise insulin (like sulfonylureas): Combining these with metformin can lower your blood sugar too much.
  - S1: Insulin or other diabetes medicines that raise insulin can lower your blood sugar too much when combined with metformin.
  - S2: Sulfonylureas are examples of diabetes medicines that raise insulin.
  - S3: Combining these medicines with metformin can lower your blood sugar too much.

**L109.1** `Simple Sentence` (0.857) → `passthrough`
- original: Your doctor may need to adjust your dose if you're taking more than one diabetes medicine.

**L110.0** `Complex Sentence` (0.86) → `decomposed`
- original: Alcohol: Drinking alcohol, especially in large amounts or regularly, can make it harder for your body to process metformin normally and raises the risk of lactic acidosis.
  - S1: Drinking alcohol can make it harder for your body to process metformin normally.
  - S2: Drinking alcohol in large amounts or regularly can make it harder for your body to process metformin normally.
  - S3: Drinking alcohol raises the risk of lactic acidosis.
  - S4: Drinking alcohol in large amounts or regularly raises the risk of lactic acidosis.

**L111.0** `Complex Sentence` (0.87) → `decomposed`
- original: Contrast dye used in imaging tests (like CT scans): This type of dye can temporarily affect kidney function, which can let metformin build up in your body.
  - S1: Contrast dye used in imaging tests like CT scans can temporarily affect kidney function.
  - S2: This can let metformin build up in your body.

**L111.1** `Compound Sentence` (0.475) → `decomposed`
- original: Your doctor may have you stop taking metformin around the time of the test and restart it once your kidney function is confirmed to be back to normal.
- pronoun resolved: Your doctor may have you stop taking metformin around the time of the test and restart metformin once your kidney function is confirmed to be back to normal.
  - edits: “it” → “metformin”
  - S1: Your doctor may have you stop taking metformin around the time of the test.
  - S2: Your doctor may have you restart metformin once your kidney function is confirmed to be back to normal.

## Metformin for Weight Loss: What the Research Shows

**L114.0** `Incomplete Sentence` (0.951) → `excluded_incomplete`
- original: Does metformin work for weight loss?

**L114.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L115.0** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Yes.

**L115.1** `Compound-Complex Sentence` (0.775) → `decomposed`
- original: Metformin can lead to a modest weight loss, though results vary, and it's generally smaller amount of weight loss than what's seen with medications specifically approved for weight loss.
  - S1: Metformin can lead to a modest weight loss.
  - S2: Results vary.
  - S3: The weight loss from Metformin is generally smaller than what is seen with medications specifically approved for weight loss.

**L116.0** `Complex Sentence` (0.929) → `decomposed`
- original: In the landmark Diabetes Prevention Program (DPP), a randomized controlled trial in people at high risk for diabetes, participants taking metformin lost more weight than those on placebo.
  - S1: In the landmark Diabetes Prevention Program (DPP), participants taking metformin lost more weight than those on placebo.
  - S2: The DPP was a randomized controlled trial in people at high risk for diabetes.

**L116.1** `Compound Sentence` (0.97) → `decomposed`
- original: Metformin patients lost 2.7% of body weight after one year, compared to 0.43% for placebo, and 2.1% after two years compared to essentially no change (0.02%) for placebo.
  - S1: Metformin patients lost 2.7% of body weight after one year.
  - S2: This was compared to 0.43% for placebo.
  - S3: Metformin patients also lost 2.1% of body weight after two years.
  - S4: This was compared to essentially no change (0.02%) for placebo.

**L116.2** `Complex Sentence` (0.895) → `decomposed`
- original: Looking at it another way, 29% of people on metformin lost at least 5% of their starting body weight after one year, versus just 13% on placebo, a gap that held up at the two-year mark (26% vs. 14%).
- pronoun resolved: Looking at it another way, 29% of people on metformin lost at least 5% of people's starting body weight after one year, versus just 13% on placebo, a gap that held up at the two-year mark (26% vs. 14%).
  - edits: “their” → “people's”
  - S1: 29% of people on metformin lost at least 5% of their starting body weight after one year.
  - S2: Just 13% of people on placebo lost at least 5% of their starting body weight after one year.
  - S3: This gap held up at the two-year mark.
  - S4: At the two-year mark, 26% of people on metformin lost at least 5% of their starting body weight.
  - S5: At the two-year mark, 14% of people on placebo lost at least 5% of their starting body weight.

**L117.0** `Simple Sentence` (0.988) → `passthrough`
- original: Metformin is not FDA-approved for weight loss.

## How does metformin help PCOS?

**L120.0** `Complex Sentence` (0.944) → `decomposed`
- original: Metformin is prescribed to manage polycystic ovary syndrome (PCOS) because it improves how the body responds to insulin.
- pronoun resolved: Metformin is prescribed to manage polycystic ovary syndrome (PCOS) because Metformin improves how the body responds to insulin.
  - edits: “it” → “Metformin”
  - S1: Metformin is prescribed to manage polycystic ovary syndrome (PCOS).
  - S2: Metformin improves how the body responds to insulin.

**L120.1** `Compound-Complex Sentence` (0.668) → `decomposed`
- original: PCOS affects about 1 in 10 women of reproductive age and is often marked by insulin resistance, in which the body doesn't respond well to insulin, prompting the pancreas to produce more.
  - S1: PCOS affects about 1 in 10 women of reproductive age.
  - S2: PCOS is often marked by insulin resistance.
  - S3: In insulin resistance, the body doesn't respond well to insulin.
  - S4: This lack of response prompts the pancreas to produce more insulin.

**L120.2** `Complex Sentence` (0.614) → `decomposed`
- original: This excess insulin drives up androgen (male hormone) production, worsening symptoms like irregular periods, infertility, acne, and excess hair growth.
  - S1: This excess insulin drives up androgen production.
  - S2: Androgen is a male hormone.
  - S3: This process worsens symptoms like irregular periods, infertility, acne, and excess hair growth.

**L120.3** `Compound-Complex Sentence` (0.866) → `decomposed`
- original: Metformin helps by lowering insulin levels, decreasing the liver's glucose production, improving glucose uptake by muscles, and reducing circulating androgen levels as well, which can support more regular ovulation and menstrual cycles.
  - S1: Metformin helps by lowering insulin levels.
  - S2: Metformin helps by decreasing the liver's glucose production.
  - S3: Metformin helps by improving glucose uptake by muscles.
  - S4: Metformin helps by reducing circulating androgen levels.
  - S5: Reducing circulating androgen levels can support more regular ovulation.
  - S6: Reducing circulating androgen levels can support more regular menstrual cycles.

**L121.0** `Compound-Complex Sentence` (0.865) → `decomposed`
- original: Although metformin is not FDA-approved to treat PCOS, it's widely prescribed as an off-label treatment, particularly for those with insulin resistance or fertility difficulties, and it's backed by extensive research and clinical guidelines.
  - S1: Metformin is not FDA-approved to treat PCOS.
  - S2: Metformin is widely prescribed as an off-label treatment.
  - S3: Metformin is prescribed particularly for those with insulin resistance.
  - S4: Metformin is prescribed particularly for those with fertility difficulties.
  - S5: Metformin is backed by extensive research.
  - S6: Metformin is backed by clinical guidelines.

**L121.1** `Compound-Complex Sentence` (0.853) → `decomposed`
- original: Beyond helping regulate cycles and support ovulation, metformin may also help reduce androgen-related symptoms such as acne and excess hair growth, and can aid with weight management for those affected by PCOS-related weight gain.
  - S1: Metformin helps regulate cycles.
  - S2: Metformin supports ovulation.
  - S3: Metformin may help reduce androgen-related symptoms.
  - S4: Androgen-related symptoms include acne.
  - S5: Androgen-related symptoms include excess hair growth.
  - S6: Metformin can aid with weight management.
  - S7: This weight management aid is for those affected by PCOS-related weight gain.

## Popular FAQ

**L124.0** `Incomplete Sentence` (0.611) → `excluded_incomplete`
- original: Q: When is the best time to take metformin?

**L124.1** `Complex Sentence` (0.617) → `decomposed`
- original: A: Metformin should be taken after having a meal or eating food, especially when you are first starting treatment.
  - S1: Metformin should be taken after having a meal or eating food.
  - S2: This is especially important when you are first starting treatment.

**L124.2** `Simple Sentence` (0.97) → `passthrough`
- original: This can help reduce any stomach side effects.

**L125.0** `Simple Sentence` (0.511) → `passthrough`
- original: Q: Can you take metformin and Ozempic together?

**L125.1** `Simple Sentence` (0.488) → `passthrough`
- original: A: Yes, metformin and Ozempic (semaglutide) are often used together under a healthcare provider’s guidance to manage type 2 diabetes.

**L125.2** `Compound-Complex Sentence` (0.839) → `decomposed`
- original: They work through different mechanisms to lower blood sugar and may also help with weight management, but both have specific safety considerations such as Ozempic’s boxed thyroid warning and metformin’s kidney function requirements.
- pronoun resolved: Metformin and Ozempic work through different mechanisms to lower blood sugar and may also help with weight management, but both have specific safety considerations such as Ozempic’s boxed thyroid warning and metformin’s kidney function requirements.
  - edits: “They” → “Metformin and Ozempic”
  - S1: Metformin works through a specific mechanism to lower blood sugar.
  - S2: Ozempic works through a different mechanism to lower blood sugar.
  - S3: Metformin and Ozempic may also help with weight management.
  - S4: Both drugs have specific safety considerations.
  - S5: Ozempic has a boxed thyroid warning.
  - S6: Metformin has kidney function requirements.

**L126.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Q: How long does metformin take to work?

**L126.1** `Compound Sentence` (0.491) → `decomposed`
- original: A: Metformin will usually start lowering your blood sugar (glucose) levels in the first week of treatment, but it may take 2 to 3 months to see its full effect.
- pronoun resolved: A: Metformin will usually start lowering your blood sugar (glucose) levels in the first week of treatment, but Metformin may take 2 to 3 months to see Metformin's full effect.
  - edits: “it” → “Metformin”; “its” → “Metformin's”
  - S1: Metformin will usually start lowering your blood sugar (glucose) levels in the first week of treatment.
  - S2: Metformin may take 2 to 3 months to see Metformin's full effect.

**L126.2** `Compound Sentence` (0.943) → `decomposed`
- original: Metformin is a preferred initial oral treatment for people with type 2 diabetes, and is usually taken on a long-term basis.
  - S1: Metformin is a preferred initial oral treatment for people with type 2 diabetes.
  - S2: It is usually taken on a long-term basis.

**L126.3** `Simple Sentence` (0.716) → `passthrough`
- original: It may be combined with other blood glucose-lowering treatments, if needed.
- pronoun resolved: Metformin may be combined with other blood glucose-lowering treatments, if needed.
  - edits: “It” → “Metformin”

**L127.0** `Incomplete Sentence` (0.943) → `excluded_incomplete`
- original: Q: What is the safest diabetes medication?

**L127.1** `Simple Sentence` (0.975) → `passthrough`
- original: A: Metformin is widely considered the safest first-line medication for type 2 diabetes.

**L127.2** `Complex Sentence` (0.934) → `decomposed`
- original: With decades of clinical use and extensive safety data, it remains the preferred initial treatment according to the American Diabetes Association (ADA).
- pronoun resolved: With decades of clinical use and extensive safety data, Metformin remains the preferred initial treatment according to the American Diabetes Association (ADA).
  - edits: “it” → “Metformin”
  - S1: Metformin remains the preferred initial treatment.
  - S2: This preference is according to the American Diabetes Association (ADA).
  - S3: Metformin has decades of clinical use.
  - S4: Metformin has extensive safety data.

**L127.3** `Complex Sentence` (0.497) → `decomposed`
- original: However, the safest medication for any individual depends on their specific health profile, age, kidney function, and treatment goals.
  - S1: However, the safest medication for any individual depends on their specific health profile.
  - S2: The safest medication also depends on their age.
  - S3: The safest medication also depends on their kidney function.
  - S4: The safest medication also depends on their treatment goals.

**L128.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Q: Why does metformin cause diarrhea?

**L128.1** `Complex Sentence` (0.873) → `decomposed`
- original: A: Metformin causes diarrhea by changing gut bacteria, affecting bile acid absorption, blocking water absorption in the intestines, and increasing gut-stimulating hormones.
  - S1: Metformin causes diarrhea.
  - S2: Metformin changes gut bacteria.
  - S3: Metformin affects bile acid absorption.
  - S4: Metformin blocks water absorption in the intestines.
  - S5: Metformin increases gut-stimulating hormones.

**L128.2** `Simple Sentence` (0.985) → `passthrough`
- original: These combined effects make stools looser and more frequent.

**L129.0** `Incomplete Sentence` (0.81) → `excluded_incomplete`
- original: Q: Can you take metformin without food?

**L129.1** `Complex Sentence` (0.663) → `decomposed`
- original: A: If you take metformin without food you may end up with an upset stomach, especially if you are just starting treatment.
  - S1: If you take metformin without food, you may end up with an upset stomach.
  - S2: This is especially true if you are just starting treatment.

**L129.2** `Compound Sentence` (0.861) → `decomposed`
- original: Nausea and vomiting are some of the most common side effects with metformin and can occur in over 30% of patients.
  - S1: Nausea and vomiting are some of the most common side effects with metformin.
  - S2: They can occur in over 30% of patients.

**L130.0** `Incomplete Sentence` (0.928) → `excluded_incomplete`
- original: Q: Does metformin lower A1C, if so how much?

**L130.1** `Complex Sentence` (0.941) → `decomposed`
- original: A: When metformin is used alone as a single agent, it lowers A1C by about 1 to 1.5 percentage points (1-1.5%) on average, at standard therapeutic doses.
- pronoun resolved: A: When metformin is used alone as a single agent, metformin lowers A1C by about 1 to 1.5 percentage points (1-1.5%) on average, at standard therapeutic doses.
  - edits: “it” → “metformin”
  - S1: Metformin lowers A1C by about 1 to 1.5 percentage points on average.
  - S2: This occurs when metformin is used alone as a single agent.
  - S3: This effect is seen at standard therapeutic doses.

**L130.2** `Simple Sentence` (0.991) → `passthrough`
- original: A1C is a measure of longer-term blood sugar control.

**L130.3** `Compound-Complex Sentence` (0.495) → `decomposed`
- original: In most patients, metformin is suggested as the initial treatment for type 2 diabetes, but its glucose-lowering effect may not be adequate for all patients if used alone.
- pronoun resolved: In most patients, metformin is suggested as the initial treatment for type 2 diabetes, but metformin's glucose-lowering effect may not be adequate for all patients if used alone.
  - edits: “its” → “metformin's”
  - S1: In most patients, metformin is suggested as the initial treatment for type 2 diabetes.
  - S2: Metformin's glucose-lowering effect may not be adequate for all patients if used alone.

**L131.0** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: Q: Does metformin cause weight loss?

**L131.1** `Complex Sentence` (0.814) → `decomposed`
- original: A: Metformin is generally considered weight neutral or modestly weight reducing, with average losses around 1–3 kg (2–7 lb) over several months in people with type 2 diabetes or obesity.
  - S1: Metformin is generally considered weight neutral or modestly weight reducing.
  - S2: Average losses are around 1–3 kg (2–7 lb) over several months.
  - S3: This applies to people with type 2 diabetes or obesity.

**L131.2** `Compound Sentence` (0.963) → `decomposed`
- original: Many people lose little or no weight, and the effect varies widely between individuals.
  - S1: Many people lose little or no weight.
  - S2: The effect varies widely between individuals.

**L132.0** `Incomplete Sentence` (0.891) → `excluded_incomplete`
- original: Q: What are the symptoms of Metformin related lactic acidosis?

**L132.1** `Complex Sentence` (0.746) → `decomposed`
- original: A: Signs or symptoms of lactic acidosis may include feeling very weak or tired, unusual muscle pain or weakness, unusual sleepiness, trouble breathing, stomach discomfort, nausea, vomiting, diarrhea, feeling cold, dizziness, and changes in your heartbeat.
  - S1: Signs or symptoms of lactic acidosis may include feeling very weak or tired.
  - S2: They may include unusual muscle pain or weakness.
  - S3: They may include unusual sleepiness.
  - S4: They may include trouble breathing.
  - S5: They may include stomach discomfort.
  - S6: They may include nausea.
  - S7: They may include vomiting.
  - S8: They may include diarrhea.
  - S9: They may include feeling cold.
  - S10: They may include dizziness.
  - S11: They may include changes in your heartbeat.
