# Pantoprazole — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/pantoprazole.txt` · 151 sentences · 14 changed by pronoun resolution · 231 sentences sent to EDC

## What is pantoprazole?

**L5.0** `Simple Sentence` (0.978) → `passthrough`
- original: Pantoprazole is a proton pump inhibitor that decreases the amount of acid produced in the stomach.

**L6.0** `Complex Sentence` (0.708) → `decomposed`
- original: Pantoprazole is used to treat erosive esophagitis (damage to the esophagus from stomach acid caused by gastroesophageal reflux disease, or GERD) in adults and children who are at least 5 years old.
  - S1: Pantoprazole is used to treat erosive esophagitis.
  - S2: Erosive esophagitis is damage to the esophagus from stomach acid.
  - S3: This damage is caused by gastroesophageal reflux disease, or GERD.
  - S4: Pantoprazole is used in adults and children who are at least 5 years old.

**L6.1** `Simple Sentence` (0.964) → `passthrough`
- original: Pantoprazole is usually given for up to 8 weeks at a time while your esophagus heals.

**L7.0** `Simple Sentence` (0.967) → `passthrough`
- original: Pantoprazole is also used to treat Zollinger-Ellison syndrome and other conditions involving excess stomach acid.

## Warnings

**L10.0** `Simple Sentence` (0.974) → `passthrough`
- original: Pantoprazole is not for the immediate relief of heartburn symptoms.

**L11.0** `Simple Sentence` (0.98) → `passthrough`
- original: Heartburn is often confused with the first symptoms of a heart attack.

**L11.1** `Incomplete Sentence` (0.498) → `excluded_incomplete`
- original: Seek emergency medical attention if you have chest pain or heavy feeling, pain spreading to the arm or shoulder, nausea, sweating, and a general ill feeling.

**L12.0** `Complex Sentence` (0.926) → `decomposed`
- original: Long-term treatment with pantoprazole may also make it harder for your body to absorb vitamin B-12, resulting in a deficiency of this vitamin.
  - S1: Long-term treatment with pantoprazole may make it harder for your body to absorb vitamin B-12.
  - S2: This difficulty in absorption may result in a deficiency of vitamin B-12.

**L12.1** `Incomplete Sentence` (0.951) → `excluded_incomplete`
- original: Talk with your doctor if you need long-term pantoprazole treatment and you have concerns about vitamin B-12 deficiency.

**L13.0** `Simple Sentence` (0.99) → `passthrough`
- original: Pantoprazole can cause kidney problems.

**L13.1** `Incomplete Sentence` (0.757) → `excluded_incomplete`
- original: Tell your doctor if you are urinating less than usual, or if you have blood in your urine.

**L14.0** `Simple Sentence` (0.99) → `passthrough`
- original: Diarrhea may be a sign of a new infection.

**L14.1** `Incomplete Sentence` (0.812) → `excluded_incomplete`
- original: Call your doctor if you have diarrhea that is watery or has blood in it.

**L15.0** `Simple Sentence` (0.991) → `passthrough`
- original: Pantoprazole may cause new or worsening symptoms of lupus.

**L15.1** `Incomplete Sentence` (0.645) → `excluded_incomplete`
- original: Tell your doctor if you have joint pain and a skin rash on your cheeks or arms that worsens in sunlight.

**L16.0** `Simple Sentence` (0.938) → `passthrough`
- original: You may be more likely to have a broken bone while taking this medicine long term or more than once per day.

## Before taking this medicine

**L19.0** `Simple Sentence` (0.991) → `passthrough`
- original: Heartburn can mimic early symptoms of a heart attack.

**L19.1** `Incomplete Sentence` (0.774) → `excluded_incomplete`
- original: Get emergency medical help if you have chest pain that spreads to your jaw or shoulder and you feel anxious or light-headed.

**L20.0** `Incomplete Sentence` (0.969) → `excluded_incomplete`
- original: You should not use this medicine if:
- pronoun resolved: You should not use Pantoprazole if:
  - edits: “this medicine” → “Pantoprazole”

**L21.0** `Simple Sentence` (0.833) → `passthrough`
- original: you also take medicine that contains rilpivirine (Edurant, Complera, Juluca, Odefsey);

**L22.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: if you had breathing problems, kidney problems, or a severe allergic reaction after taking pantoprazole in the past; or

**L23.0** `Simple Sentence` (0.825) → `passthrough`
- original: you are allergic to pantoprazole or similar medicines (lansoprazole, omeprazole, Nexium, Prevacid, Prilosec, and others).

**L24.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Tell your doctor if you have ever had:

**L25.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: low levels of magnesium, calcium, or potassium in your blood;

**L26.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: lupus; or

**L27.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: osteoporosis or low bone mineral density.

**L28.0** `Simple Sentence` (0.948) → `passthrough`
- original: You may be more likely to have a broken bone while using pantoprazole long-term or more than once per day.

**L28.1** `Incomplete Sentence` (0.944) → `excluded_incomplete`
- original: Talk with your doctor about ways to keep your bones healthy, especially if you are an adult over 50.

**L29.0** `Simple Sentence` (0.991) → `passthrough`
- original: This medicine may harm an unborn baby.

**L29.1** `Incomplete Sentence` (0.915) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or plan to become pregnant.

**L30.0** `Simple Sentence` (0.99) → `passthrough`
- original: Pantoprazole can pass into breast milk.

**L30.1** `Incomplete Sentence` (0.97) → `excluded_incomplete`
- original: Talk with your doctor about the best way to feed your baby if you take this medicine.
- pronoun resolved: Talk with your doctor about the best way to feed your baby if you take Pantoprazole.
  - edits: “this medicine.” → “Pantoprazole.”

**L31.0** `Simple Sentence` (0.988) → `passthrough`
- original: Pantoprazole is not approved for use by anyone younger than 5 years old.

## How should I use pantoprazole?

**L34.0** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Take pantoprazole exactly as prescribed by your doctor.

**L34.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L34.2** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Use the medicine exactly as directed.

**L35.0** `Incomplete Sentence` (0.952) → `excluded_incomplete`
- original: Use the lowest dose for the shortest amount of time needed to treat your condition.

**L36.0** `Simple Sentence` (0.951) → `passthrough`
- original: Pantoprazole is taken by mouth (oral) or given as an infusion into a vein (injection).

**L36.1** `Simple Sentence` (0.982) → `passthrough`
- original: A healthcare provider may teach you how to properly use the injection by yourself.

**L37.0** `Simple Sentence` (0.986) → `passthrough`
- original: Pantoprazole tablets are taken by mouth, with or without food.

**L37.1** `Simple Sentence` (0.984) → `passthrough`
- original: The oral granules should be taken 30 minutes before a meal.

**L38.0** `Incomplete Sentence` (0.83) → `excluded_incomplete`
- original: Do not crush, chew, or break the tablet or oral granules.

**L38.1** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Swallow the tablet whole.

**L39.0** `Simple Sentence` (0.958) → `passthrough`
- original: The oral granules should be mixed with applesauce or apple juice when taken by mouth.

**L39.1** `Simple Sentence` (0.82) → `passthrough`
- original: If giving through a nasogastric (NG) or gastrostomy tube, mix only with apple juice.

**L40.0** `Incomplete Sentence` (0.96) → `excluded_incomplete`
- original: Read and carefully follow any Instructions for Use provided with your medicine.

**L40.1** `Incomplete Sentence` (0.897) → `excluded_incomplete`
- original: Ask your doctor or pharmacist if you have any questions.

**L41.0** `Incomplete Sentence` (0.801) → `excluded_incomplete`
- original: Use this medicine for the full prescribed length of time, even if your symptoms quickly improve.

**L42.0** `Incomplete Sentence` (0.735) → `excluded_incomplete`
- original: Call your doctor if your symptoms do not improve or if they get worse while you are using this medicine.
- pronoun resolved: Call your doctor if your symptoms do not improve or if symptoms get worse while you are using this medicine.
  - edits: “they” → “symptoms”

**L43.0** `Simple Sentence` (0.99) → `passthrough`
- original: Pantoprazole can cause false results with certain medical tests.

**L43.1** `Incomplete Sentence` (0.959) → `excluded_incomplete`
- original: Tell the doctor or laboratory staff that you are using this medicine.

**L44.0** `Compound Sentence` (0.95) → `decomposed`
- original: Pantoprazole may also affect a drug-screening urine test and you may have false results.
  - S1: Pantoprazole may also affect a drug-screening urine test.
  - S2: You may have false results.

**L44.1** `Incomplete Sentence` (0.971) → `excluded_incomplete`
- original: Tell the laboratory staff that you use this medicine.

**L45.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Store this medicine at room temperature away from moisture, heat, and light.
- pronoun resolved: Store Pantoprazole at room temperature away from moisture, heat, and light.
  - edits: “this medicine” → “Pantoprazole”

## Dosing information

**L48.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Erosive Esophagitis:

**L49.0** `Compound Sentence` (0.846) → `decomposed`
- original: Treatment of Erosive Esophagitis: 40 mg orally once a day for up to 8 weeks; however an additional 8 weeks may be considered for patients who have not healed after the initial treatment.
  - S1: Treatment of Erosive Esophagitis involves taking 40 mg orally once a day for up to 8 weeks.
  - S2: However, an additional 8 weeks may be considered for patients who have not healed after the initial treatment.

**L49.1** `Simple Sentence` (0.981) → `passthrough`
- original: Safety and efficacy beyond 16 weeks of therapy have not been established.

**L49.2** `Incomplete Sentence` (0.94) → `excluded_incomplete`
- original: Maintenance of Healing of Erosive Esophagitis: 40 mg orally once a day.

**L49.3** `Simple Sentence` (0.99) → `passthrough`
- original: Controlled studies have been limited to 12 months of pantoprazole therapy.

**L50.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Gastroesophageal Reflux Disease:

**L51.0** `Simple Sentence` (0.675) → `passthrough`
- original: Parenteral: 40 mg once a day for 7 to 10 days, administered via intravenous infusion over a period of 15 minutes.

**L51.1** `Simple Sentence` (0.744) → `passthrough`
- original: Intravenous therapy should be discontinued as soon as the patient is able to resume oral therapy.

**L51.2** `Compound Sentence` (0.518) → `decomposed`
- original: Oral: 40 mg orally once a day, for short-term administration (up to 8 weeks); however an additional 8 weeks may be considered for patients who have not healed after the initial treatment.
  - S1: Oral: 40 mg orally once a day, for short-term administration (up to 8 weeks).
  - S2: However, an additional 8 weeks may be considered for patients who have not healed after the initial treatment.

**L51.3** `Simple Sentence` (0.981) → `passthrough`
- original: Safety and efficacy beyond 16 weeks of therapy have not been established.

**L52.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Duodenal Ulcer:

**L53.0** `Compound Sentence` (0.676) → `decomposed`
- original: Study (n=54) 40 mg orally once a day, dose was increased every 12 weeks by 40 mg increments to a maximum of 120 mg per day, for 28 weeks.
  - S1: Study (n=54) took 40 mg orally once a day.
  - S2: The dose was increased every 12 weeks by 40 mg increments.
  - S3: The maximum dose was 120 mg per day.
  - S4: The study lasted for 28 weeks.

**L53.1** `Complex Sentence` (0.949) → `decomposed`
- original: Data have revealed that monotherapy with daily doses of 40 mg have been associated with complete duodenal ulcer healing in up to 87% and 94% of patients after 4 weeks and 8 weeks respectively.
  - S1: Data have revealed that monotherapy with daily doses of 40 mg have been associated with complete duodenal ulcer healing.
  - S2: Healing was observed in up to 87% of patients after 4 weeks.
  - S3: Healing was observed in up to 94% of patients after 8 weeks.

**L54.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Gastric Ulcer:

**L55.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: 40 mg orally once a day.

**L55.1** `Complex Sentence` (0.949) → `decomposed`
- original: Data have revealed that monotherapy with daily doses of 40 mg have been associated with complete gastric ulcer healing in up to 87% and 97% of patients after 4 weeks and 8 weeks respectively.
  - S1: Data have revealed that monotherapy with daily doses of 40 mg have been associated with complete gastric ulcer healing.
  - S2: This healing occurred in up to 87% of patients after 4 weeks.
  - S3: This healing occurred in up to 97% of patients after 8 weeks.

**L56.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Helicobacter pylori Infection:

**L57.0** `Complex Sentence` (0.46) → `decomposed`
- original: Study (n=242) - Triple therapy: 40 mg orally twice daily for 7 days, commonly in conjunction with clarithromycin and either amoxicillin or metronidazole to eradicate Helicobacter pylori, followed with 40 mg pantoprazole orally once daily until day 28.
  - S1: A study with 242 participants was conducted.
  - S2: Triple therapy was administered at 40 mg orally twice daily for 7 days.
  - S3: This therapy was commonly used in conjunction with clarithromycin and either amoxicillin or metronidazole.
  - S4: The goal was to eradicate Helicobacter pylori.
  - S5: Pantoprazole was administered at 40 mg orally once daily until day 28.

**L57.1** `Simple Sentence` (0.989) → `passthrough`
- original: Triple therapy has resulted in eradication rates of greater than 95%.

**L57.2** `Compound Sentence` (0.491) → `decomposed`
- original: The QUADRATE Study (n=405) - Quadruple therapy: 40 mg orally twice daily for 7 days, concomitantly with bismuth subcitrate and tetracycline, both four times daily, and metronidazole 200 mg three times daily and 400 mg at bedtime.
  - S1: The QUADRATE Study (n=405) involves quadruple therapy.
  - S2: This therapy consists of 40 mg of the primary drug taken orally twice daily for 7 days.
  - S3: It is administered concomitantly with bismuth subcitrate, taken four times daily.
  - S4: It is also administered concomitantly with tetracycline, taken four times daily.
  - S5: It includes metronidazole 200 mg taken three times daily.
  - S6: It includes metronidazole 400 mg taken at bedtime.

**L57.3** `Simple Sentence` (0.986) → `passthrough`
- original: Helicobacter Pylori eradication was achieved in 82% of patients.

**L58.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Zollinger-Ellison Syndrome:

**L59.0** `Incomplete Sentence` (0.838) → `excluded_incomplete`
- original: Parenteral: 80 mg every 12 hours, administered by 15-minute infusion.

**L59.1** `Compound Sentence` (0.463) → `decomposed`
- original: Daily doses higher than 240 mg administered in equally divided doses by 15-minute infusion, or administered for more than 6 days have not been studied.
  - S1: Daily doses higher than 240 mg administered in equally divided doses by 15-minute infusion have not been studied.
  - S2: Doses administered for more than 6 days have not been studied.

**L59.2** `Incomplete Sentence` (0.952) → `excluded_incomplete`
- original: Oral: 40 mg twice daily, to a maximum of 240 mg per day.

**L59.3** `Simple Sentence` (0.987) → `passthrough`
- original: Some patients have received treatment with pantoprazole for more than 2 years.

**L60.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Stress Ulcer Prophylaxis:

**L61.0** `Compound Sentence` (0.434) → `decomposed`
- original: Study (n=21) - Stress Ulcer bleeding prophylaxis in the Critical Care Setting: 80 mg twice daily, as a bolus infusion over a period of 15 minutes, to a maximum daily dose of 240 mg, divided into three equal doses.
  - S1: The study included 21 participants.
  - S2: The study focused on stress ulcer bleeding prophylaxis in the critical care setting.
  - S3: The prophylaxis was administered as 80 mg twice daily.
  - S4: The dose was given as a bolus infusion over a period of 15 minutes.
  - S5: The maximum daily dose was 240 mg.
  - S6: The daily dose was divided into three equal doses.

**L61.1** `Complex Sentence` (0.644) → `decomposed`
- original: Study (n=20) - Peptic Ulcer rebleeding prophylaxis after hemostasis in the Critical Care Setting: 80 mg IV bolus, followed by continuous infusion of 8 mg/hr for 3 days, after which therapy may be continued with an oral PPI.
  - S1: A study with 20 participants investigated peptic ulcer rebleeding prophylaxis after hemostasis in the critical care setting.
  - S2: The treatment involved an 80 mg IV bolus.
  - S3: This was followed by a continuous infusion of 8 mg/hr for 3 days.
  - S4: After this period, therapy may be continued with an oral PPI.

**L62.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Peptic Ulcer:

**L63.0** `Compound Sentence` (0.434) → `decomposed`
- original: Study (n=21) - Stress Ulcer bleeding prophylaxis in the Critical Care Setting: 80 mg twice daily, as a bolus infusion over a period of 15 minutes, to a maximum daily dose of 240 mg, divided into three equal doses.
  - S1: The study included 21 participants.
  - S2: The study focused on stress ulcer bleeding prophylaxis in the critical care setting.
  - S3: The prophylaxis was administered as 80 mg twice daily.
  - S4: The dose was given as a bolus infusion over a period of 15 minutes.
  - S5: The maximum daily dose was 240 mg.
  - S6: The daily dose was divided into three equal doses.

**L63.1** `Complex Sentence` (0.644) → `decomposed`
- original: Study (n=20) - Peptic Ulcer rebleeding prophylaxis after hemostasis in the Critical Care Setting: 80 mg IV bolus, followed by continuous infusion of 8 mg/hr for 3 days, after which therapy may be continued with an oral PPI.
  - S1: A study with 20 participants investigated peptic ulcer rebleeding prophylaxis after hemostasis in the critical care setting.
  - S2: The treatment involved an 80 mg IV bolus.
  - S3: This was followed by a continuous infusion of 8 mg/hr for 3 days.
  - S4: After this period, therapy may be continued with an oral PPI.

## What happens if I miss a dose?

**L66.0** `Compound Sentence` (0.562) → `decomposed`
- original: Use the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - S1: Use the medicine as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L66.1** `Incomplete Sentence` (0.946) → `excluded_incomplete`
- original: Do not use two doses at one time.

## What happens if I overdose?

**L69.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

## What should I avoid while using pantoprazole?

**L72.0** `Simple Sentence` (0.562) → `passthrough`
- original: This medicine can cause diarrhea, which may be a sign of a new infection.
- pronoun resolved: Pantoprazole can cause diarrhea, which may be a sign of a new infection.
  - edits: “This medicine” → “Pantoprazole”

**L72.1** `Simple Sentence` (0.849) → `passthrough`
- original: If you have diarrhea that is watery or bloody, call your doctor.

**L72.2** `Incomplete Sentence` (0.678) → `excluded_incomplete`
- original: Do not use anti-diarrhea medicine unless your doctor tells you to.

## Pantoprazole side effects

**L75.0** `Compound Sentence` (0.467) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to pantoprazole: hives; difficulty breathing; swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to pantoprazole.
  - S2: Signs of an allergic reaction to pantoprazole include hives.
  - S3: Signs of an allergic reaction to pantoprazole include difficulty breathing.
  - S4: Signs of an allergic reaction to pantoprazole include swelling of your face, lips, tongue, or throat.

**L76.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L77.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: severe stomach pain, diarrhea that is watery or bloody;

**L78.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: sudden pain or trouble moving your hip, wrist, or back;

**L79.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: bruising or swelling where intravenous pantoprazole was injected;

**L80.0** `Incomplete Sentence` (0.96) → `excluded_incomplete`
- original: kidney problems - fever, rash, nausea, loss of appetite, joint pain, urinating less than usual, blood in your urine, weight gain;

**L81.0** `Incomplete Sentence` (0.941) → `excluded_incomplete`
- original: low magnesium - dizziness, fast or irregular heart rate, tremors (shaking) or jerking muscle movements, feeling jittery, muscle cramps, muscle spasms in your hands and feet, cough or choking feeling; or

**L82.0** `Incomplete Sentence` (0.963) → `excluded_incomplete`
- original: new or worsening symptoms of lupus - joint pain, and a skin rash on your cheeks or arms that worsens in sunlight.

**L83.0** `Incomplete Sentence` (0.963) → `excluded_incomplete`
- original: severe skin reactions - fever, chills, body aches, shortness of breath, enlarged lymph nodes, or a skin rash that blisters, peels, or bleeds;

**L84.0** `Simple Sentence` (0.984) → `passthrough`
- original: Taking pantoprazole long-term may cause you to develop stomach growths called fundic gland polyps.

**L84.1** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Talk with your doctor about this risk.

**L85.0** `Simple Sentence` (0.858) → `passthrough`
- original: If you use pantoprazole for longer than 3 years, you could develop a vitamin B-12 deficiency.

**L85.1** `Incomplete Sentence` (0.945) → `excluded_incomplete`
- original: Talk to your doctor about how to manage this condition if you develop it.

**L86.0** `Simple Sentence` (0.944) → `passthrough`
- original: Common pantoprazole side effects may include:

**L87.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: headache, dizziness;

**L88.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: stomach pain, gas, nausea, vomiting, diarrhea;

**L89.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: joint pain; or

**L90.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: fever, rash, or cold symptoms (most common in children).

**L91.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L91.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L91.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## What other drugs will affect pantoprazole?

**L94.0** `Incomplete Sentence` (0.967) → `excluded_incomplete`
- original: Tell your doctor about all your other medicines.

**L94.1** `Simple Sentence` (0.982) → `passthrough`
- original: Some may interact with pantoprazole, especially:

**L95.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: digoxin;

**L96.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: methotrexate; or

**L97.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a diuretic or "water pill."

**L98.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L98.1** `Complex Sentence` (0.593) → `decomposed`
- original: Other drugs may affect pantoprazole, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may affect pantoprazole.
  - S2: These other drugs include prescription and over-the-counter medicines.
  - S3: These other drugs also include vitamins and herbal products.

**L98.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.

## Popular FAQ

**L101.0** `Incomplete Sentence` (0.914) → `excluded_incomplete`
- original: Q: How long does pantoprazole take to work?

**L101.1** `Complex Sentence` (0.468) → `decomposed`
- original: A: Pantoprazole starts to work within 2 and a half (2.5) hours – this is the time it takes for it to block the secretion of acid in the stomach - and lasts for 24 hours.
- pronoun resolved: A: Pantoprazole starts to work within 2 and a half (2.5) hours – this is the time Pantoprazole takes for Pantoprazole to block the secretion of acid in the stomach - and lasts for 24 hours.
  - edits: “it” → “Pantoprazole”; “it” → “Pantoprazole”
  - S1: Pantoprazole starts to work within 2.5 hours.
  - S2: This is the time Pantoprazole takes to block the secretion of acid in the stomach.
  - S3: Pantoprazole lasts for 24 hours.

**L101.2** `Compound Sentence` (0.946) → `decomposed`
- original: Pantoprazole does not provide fast-acting relief from indigestion, acid reflux, or dyspepsia symptoms like antacids such as Tums or Maalox do, and will not treat current symptoms.
  - S1: Pantoprazole does not provide fast-acting relief from indigestion, acid reflux, or dyspepsia symptoms.
  - S2: Antacids such as Tums or Maalox provide fast-acting relief from indigestion, acid reflux, or dyspepsia symptoms.
  - S3: Pantoprazole will not treat current symptoms.

**L101.3** `Compound Sentence` (0.563) → `decomposed`
- original: It may take up to 4 weeks for pantoprazole to work properly so you may still have some symptoms during this time.
- pronoun resolved: Pantoprazole may take up to 4 weeks for pantoprazole to work properly so you may still have some symptoms during this time.
  - edits: “It” → “Pantoprazole”
  - S1: Pantoprazole may take up to 4 weeks to work properly.
  - S2: You may still have some symptoms during this time.

**L102.0** `Incomplete Sentence` (0.972) → `excluded_incomplete`
- original: Q: Pantoprazole vs. omeprazole: What's the difference between them?

**L102.1** `Complex Sentence` (0.931) → `decomposed`
- original: A: Pantoprazole and omeprazole are both proton pump inhibitors (PPIs) that reduce stomach acid and show similar effectiveness for healing acid‑related conditions such as erosive esophagitis.
  - S1: Pantoprazole and omeprazole are both proton pump inhibitors (PPIs).
  - S2: These PPIs reduce stomach acid.
  - S3: They show similar effectiveness for healing acid‑related conditions.
  - S4: An example of such a condition is erosive esophagitis.

**L102.2** `Complex Sentence` (0.516) → `decomposed`
- original: Their main differences relate to FDA‑approved uses, availability (omeprazole is OTC; pantoprazole is prescription), timing with food, and the option for intravenous (IV) pantoprazole in the hospital setting.
- pronoun resolved: Pantoprazole and omeprazole's main differences relate to FDA‑approved uses, availability (omeprazole is OTC; pantoprazole is prescription), timing with food, and the option for intravenous (IV) pantoprazole in the hospital setting.
  - edits: “Their” → “Pantoprazole and omeprazole's”
  - S1: Pantoprazole and omeprazole's main differences relate to FDA‑approved uses.
  - S2: The differences also relate to availability.
  - S3: Omeprazole is OTC.
  - S4: Pantoprazole is prescription.
  - S5: The differences also relate to timing with food.
  - S6: The differences also relate to the option for intravenous (IV) pantoprazole in the hospital setting.

**L103.0** `Simple Sentence` (0.877) → `passthrough`
- original: Q: Can you take pantoprazole 40 mg twice a day?

**L103.1** `Complex Sentence` (0.815) → `decomposed`
- original: A: The usual dosage for pantoprazole 40mg is 40mg once a day if you are buying it without a prescription or a physician's evaluation of your symptoms.
- pronoun resolved: A: The usual dosage for pantoprazole 40mg is 40mg once a day if you are buying pantoprazole without a prescription or a physician's evaluation of your symptoms.
  - edits: “it” → “pantoprazole”
  - S1: The usual dosage for pantoprazole 40mg is 40mg once a day.
  - S2: This applies if you are buying pantoprazole without a prescription.
  - S3: This also applies if you are buying pantoprazole without a physician's evaluation of your symptoms.

**L103.2** `Compound-Complex Sentence` (0.744) → `decomposed`
- original: The only conditions that pantoprazole 40mg twice a day is recommended for are those characterized by excessively high gastric acid secretion such as Zollinger Ellison syndrome, and if you have these conditions then you should be under the care of a physician.
  - S1: Pantoprazole 40mg twice a day is recommended only for conditions characterized by excessively high gastric acid secretion.
  - S2: Zollinger Ellison syndrome is a condition characterized by excessively high gastric acid secretion.
  - S3: If you have conditions characterized by excessively high gastric acid secretion, you should be under the care of a physician.
  - S4: You should be under the care of a physician if you have Zollinger Ellison syndrome.

**L103.3** `Complex Sentence` (0.94) → `decomposed`
- original: Studies have shown that for reflux, dyspepsia, or GERD, dosages higher than 40mg did not offer any further significant lowering of stomach acid than 40mg dosages.
  - S1: Studies have shown that for reflux, dyspepsia, or GERD, dosages higher than 40mg did not offer any further significant lowering of stomach acid.
  - S2: The comparison was made against 40mg dosages.

**L104.0** `Incomplete Sentence` (0.889) → `excluded_incomplete`
- original: Q: How long can I take pantoprazole?

**L104.1** `Complex Sentence` (0.674) → `decomposed`
- original: A: You should only take pantoprazole for up to 8 weeks if you are buying it without a prescription or a physician evaluation of your symptoms.
- pronoun resolved: A: You should only take pantoprazole for up to 8 weeks if you are buying pantoprazole without a prescription or a physician evaluation of your symptoms.
  - edits: “it” → “pantoprazole”
  - S1: You should only take pantoprazole for up to 8 weeks.
  - S2: This applies if you are buying pantoprazole without a prescription.
  - S3: This also applies if you are buying pantoprazole without a physician evaluation of your symptoms.

**L104.2** `Compound-Complex Sentence` (0.504) → `decomposed`
- original: This is because certain stomach symptoms that persist for more than 4 to 8 weeks should be investigated by a doctor, as they may be a sign of something more serious, such as cancer.
- pronoun resolved: This is because certain stomach symptoms that persist for more than 4 to 8 weeks should be investigated by a doctor, as stomach symptoms may be a sign of something more serious, such as cancer.
  - edits: “they” → “stomach symptoms”
  - S1: Certain stomach symptoms persist for more than 4 to 8 weeks.
  - S2: These symptoms should be investigated by a doctor.
  - S3: Stomach symptoms may be a sign of something more serious.
  - S4: Something more serious may be cancer.

**L104.3** `Complex Sentence` (0.691) → `decomposed`
- original: Pantoprazole is very good at relieving and hiding serious stomach symptoms, which may make you think you don’t need to see a physician.
  - S1: Pantoprazole is very good at relieving and hiding serious stomach symptoms.
  - S2: These symptoms may make you think you don't need to see a physician.

**L104.4** `Compound Sentence` (0.577) → `decomposed`
- original: Long-term use of pantoprazole has also been associated with vitamin B12 deficiency; low magnesium, calcium, iron, or vitamin C levels; and an increased risk of fractures of the hip, wrist, or spine.
  - S1: Long-term use of pantoprazole has also been associated with vitamin B12 deficiency.
  - S2: It has been associated with low magnesium, calcium, iron, or vitamin C levels.
  - S3: It has been associated with an increased risk of fractures of the hip, wrist, or spine.

**L104.5** `Simple Sentence` (0.934) → `passthrough`
- original: Elderly, the malnourished, or those on dialysis are more at risk.

**L105.0** `Incomplete Sentence` (0.874) → `excluded_incomplete`
- original: Q: Does pantoprazole cause bloating?

**L105.1** `Simple Sentence` (0.978) → `passthrough`
- original: A: Bloating has been reported as a side effect of regular pantoprazole use.

**L105.2** `Complex Sentence` (0.63) → `decomposed`
- original: One study reported bloating in 43% of patients taking a similar proton pump inhibitor to pantoprazole (called esomeprazole) after 8 weeks.
  - S1: One study reported bloating in 43% of patients.
  - S2: The patients were taking a similar proton pump inhibitor to pantoprazole.
  - S3: The inhibitor was called esomeprazole.
  - S4: The bloating occurred after 8 weeks.

**L105.3** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: By 6 months, over 50% reporting bloating.

**L105.4** `Complex Sentence` (0.596) → `decomposed`
- original: Other similar side effects reported with pantoprazole that also can have bloating as a side effect include flatulence, abdominal pain, and diarrhea.
  - S1: Other similar side effects reported with pantoprazole include flatulence, abdominal pain, and diarrhea.
  - S2: Bloating can also be a side effect of pantoprazole.

**L105.5** `Simple Sentence` (0.927) → `passthrough`
- original: Symptoms of bloating include tightness, fullness, or swelling of your stomach area.

**L106.0** `Incomplete Sentence` (0.864) → `excluded_incomplete`
- original: Q: When should you take pantoprazole?

**L106.1** `Simple Sentence` (0.979) → `passthrough`
- original: A: Pantoprazole is usually taken once daily, 30 minutes before a meal.

**L106.2** `Simple Sentence` (0.933) → `passthrough`
- original: It is most often taken before breakfast to control acid and relieve GERD or heartburn symptoms.
- pronoun resolved: Pantoprazole is most often taken before breakfast to control acid and relieve GERD or heartburn symptoms.
  - edits: “It” → “Pantoprazole”

**L106.3** `Compound Sentence` (0.96) → `decomposed`
- original: It may be taken with or without food, but taking it on an empty stomach before eating helps it work more effectively.
- pronoun resolved: Pantoprazole may be taken with or without food, but taking Pantoprazole on an empty stomach before eating helps Pantoprazole work more effectively.
  - edits: “It” → “Pantoprazole”; “it” → “Pantoprazole”; “it” → “Pantoprazole”
  - S1: Pantoprazole may be taken with or without food.
  - S2: Taking Pantoprazole on an empty stomach before eating helps Pantoprazole work more effectively.

**L107.0** `Incomplete Sentence` (0.93) → `excluded_incomplete`
- original: Q: Can pantoprazole cause anxiety?

**L107.1** `Compound Sentence` (0.962) → `decomposed`
- original: A: Pantoprazole is not known to commonly cause anxiety, and most people take it without experiencing mood or anxiety symptoms.
- pronoun resolved: A: Pantoprazole is not known to commonly cause anxiety, and most people take Pantoprazole without experiencing mood or anxiety symptoms.
  - edits: “it” → “Pantoprazole”
  - S1: Pantoprazole is not known to commonly cause anxiety.
  - S2: Most people take Pantoprazole without experiencing mood or anxiety symptoms.

**L107.2** `Complex Sentence` (0.894) → `decomposed`
- original: However, anxiety can be a symptom of low vitamin B12 levels which is a long-term complication of pantoprazole treatment.
  - S1: However, anxiety can be a symptom of low vitamin B12 levels.
  - S2: Low vitamin B12 levels are a long-term complication of pantoprazole treatment.
