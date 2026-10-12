# Omeprazole — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/omeprazole.txt` · 152 sentences · 27 changed by pronoun resolution · 216 sentences sent to EDC

## What is omeprazole?

**L5.0** `Complex Sentence` (0.815) → `decomposed`
- original: Omeprazole is used to treat excess stomach acid in conditions such as stomach ulcers, heartburn or gastroesophageal reflux disease (GERD), active duodenal ulcer, Zollinger-Ellison syndrome and erosive esophagitis.
  - S1: Omeprazole is used to treat excess stomach acid.
  - S2: It is used in conditions such as stomach ulcers, heartburn, or gastroesophageal reflux disease (GERD).
  - S3: It is used in active duodenal ulcer, Zollinger-Ellison syndrome, and erosive esophagitis.

**L6.0** `Complex Sentence` (0.851) → `decomposed`
- original: Omeprazole may also be given together with antibiotics to treat gastric ulcers caused by infection with Helicobacter pylori (H. pylori), in adult patients.
  - S1: Omeprazole may be given together with antibiotics.
  - S2: This combination is used to treat gastric ulcers.
  - S3: The ulcers are caused by infection with Helicobacter pylori (H. pylori).
  - S4: The treatment is for adult patients.

**L7.0** `Complex Sentence` (0.954) → `decomposed`
- original: Omeprazole is a proton pump inhibitor (PPI) that works by blocking the acid pump in your stomach, reducing how much acid it makes and giving irritated or damaged tissue a chance to heal.
- pronoun resolved: Omeprazole is a proton pump inhibitor (PPI) that works by blocking the acid pump in your stomach, reducing how much acid Omeprazole makes and giving irritated or damaged tissue a chance to heal.
  - edits: “it” → “Omeprazole”
  - S1: Omeprazole is a proton pump inhibitor (PPI).
  - S2: Omeprazole works by blocking the acid pump in your stomach.
  - S3: This action reduces how much acid Omeprazole makes.
  - S4: This gives irritated or damaged tissue a chance to heal.

**L8.0** `Compound Sentence` (0.579) → `decomposed`
- original: Omeprazole brand names are Prilosec, Prilosec OTC, and generic brands are available.
  - S1: Omeprazole brand names are Prilosec, Prilosec OTC.
  - S2: Generic brands are available.

**L9.0** `Simple Sentence` (0.968) → `passthrough`
- original: Omeprazole is available over the counter (OTC) and as a prescription medication.

## What is omeprazole used for?

**L12.0** `Incomplete Sentence` (0.688) → `excluded_incomplete`
- original: Over-the-counter omeprazole is used for:

**L13.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: frequent heartburn that occurs 2 or more days a week in adults 18 years and older

**L14.0** `Simple Sentence` (0.981) → `passthrough`
- original: It is taken as a 14-day course, once a day for 14 days in a row.
- pronoun resolved: Omeprazole is taken as a 14-day course, once a day for 14 days in a row.
  - edits: “It” → “Omeprazole”

**L14.1** `Compound Sentence` (0.951) → `decomposed`
- original: It may take 1 to 4 days to reach its full effect, so it is not used for immediate relief of symptoms.
- pronoun resolved: It may take 1 to 4 days to reach its full effect, so omeprazole is not used for immediate relief of symptoms.
  - edits: “it” → “omeprazole”
  - S1: It may take 1 to 4 days to reach its full effect.
  - S2: Omeprazole is not used for immediate relief of symptoms.

**L14.2** `Compound Sentence` (0.938) → `decomposed`
- original: Do not take it for longer than 14 days, and do not start another 14-day course within 4 months, unless your doctor tells you to.
- pronoun resolved: Do not take omeprazole for longer than 14 days, and do not start another 14-day course within 4 months, unless your doctor tells you to.
  - edits: “it” → “omeprazole”
  - S1: Do not take omeprazole for longer than 14 days.
  - S2: Do not start another 14-day course within 4 months.
  - S3: Do this unless your doctor tells you to.

**L15.0** `Incomplete Sentence` (0.94) → `excluded_incomplete`
- original: Prescription omeprazole can be used for:

**L16.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: active duodenal ulcer (a sore in the first part of the small intestine) in adults

**L17.0** `Incomplete Sentence` (0.935) → `excluded_incomplete`
- original: Helicobacter pylori (H. pylori) infection in adults, taken together with antibiotics, to reduce the risk of a duodenal ulcer coming back

**L18.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: active benign gastric ulcer (a non-cancerous sore in the stomach lining) in adults

**L19.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: symptoms of gastroesophageal reflux disease (GERD), such as heartburn, in adults and children 1 year of age and older

**L20.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: erosive esophagitis (EE) caused by acid reflux in adults and children 1 month of age and older

**L21.0** `Simple Sentence` (0.636) → `passthrough`
- original: keeping erosive esophagitis healed after treatment, in adults and children 1 year of age and older

**L22.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: pathological hypersecretory conditions (conditions in which the stomach makes too much acid) in adults, including Zollinger-Ellison syndrome

## Warnings

**L25.0** `Simple Sentence` (0.989) → `passthrough`
- original: Omeprazole can cause kidney problems.

**L25.1** `Incomplete Sentence` (0.757) → `excluded_incomplete`
- original: Tell your doctor if you are urinating less than usual, or if you have blood in your urine.

**L26.0** `Simple Sentence` (0.99) → `passthrough`
- original: Diarrhea may be a sign of a new infection.

**L26.1** `Incomplete Sentence` (0.687) → `excluded_incomplete`
- original: Call your doctor right away if you have watery stools or stomach pain that does not go away.

**L26.2** `Simple Sentence` (0.94) → `passthrough`
- original: You may or may not have a fever.

**L27.0** `Simple Sentence` (0.955) → `passthrough`
- original: Omeprazole is not to be used for the immediate relief of heartburn symptoms.

**L28.0** `Simple Sentence` (0.991) → `passthrough`
- original: Omeprazole may cause new or worsening symptoms of lupus.

**L28.1** `Incomplete Sentence` (0.645) → `excluded_incomplete`
- original: Tell your doctor if you have joint pain and a skin rash on your cheeks or arms that worsens in sunlight.

**L29.0** `Simple Sentence` (0.96) → `passthrough`
- original: You may be more likely to have a broken bone while taking this medicine long term or more than once per day.
- pronoun resolved: You may be more likely to have a broken bone while taking Omeprazole long term or more than once per day.
  - edits: “this medicine” → “Omeprazole”

## Before taking this medicine

**L32.0** `Simple Sentence` (0.991) → `passthrough`
- original: Heartburn can mimic early symptoms of a heart attack.

**L32.1** `Incomplete Sentence` (0.733) → `excluded_incomplete`
- original: Get emergency medical help if you have chest pain that spreads to your jaw or shoulder and you feel sweaty or light-headed.

**L33.0** `Incomplete Sentence` (0.912) → `excluded_incomplete`
- original: You should not use omeprazole if you are allergic to it, or if:
- pronoun resolved: You should not use omeprazole if you are allergic to omeprazole, or if:
  - edits: “it,” → “omeprazole,”

**L34.0** `Simple Sentence` (0.727) → `passthrough`
- original: you are also allergic to medicines like omeprazole, such as esomeprazole, lansoprazole, pantoprazole, rabeprazole, Nexium, Prevacid, Protonix, and others;

**L35.0** `Incomplete Sentence` (0.862) → `excluded_incomplete`
- original: you had breathing problems, kidney problems, or a severe allergic reaction after taking omeprazole in the past; or

**L36.0** `Simple Sentence` (0.677) → `passthrough`
- original: you also take HIV medication that contains rilpivirine (such as Complera, Edurant, Odefsey, Juluca).

**L37.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Ask a doctor or pharmacist if this medicine is safe to use if you have:
- pronoun resolved: Ask a doctor or pharmacist if Omeprazole is safe to use if you have:
  - edits: “this medicine” → “Omeprazole”

**L38.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: trouble or pain with swallowing;

**L39.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: bloody or black stools, vomit that looks like blood or coffee grounds;

**L40.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: heartburn that has lasted for over 3 months;

**L41.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: frequent chest pain, heartburn with wheezing;

**L42.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: unexplained weight loss;

**L43.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: nausea or vomiting, stomach pain;

**L44.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: liver disease;

**L45.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: low levels of magnesium, calcium, or potassium in your blood; or

**L46.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: osteoporosis or low bone mineral density (osteopenia).

**L47.0** `Simple Sentence` (0.473) → `passthrough`
- original: You may be more likely to have a broken bone in your hip, wrist, or spine while taking a proton pump inhibitor long-term or more than once per day.

**L47.1** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: Talk with your doctor about ways to keep your bones healthy.

**L48.0** `Incomplete Sentence` (0.61) → `excluded_incomplete`
- original: Ask a doctor before using this medicine if you are pregnant or breastfeeding.
- pronoun resolved: Ask a doctor before using Omeprazole if you are pregnant or breastfeeding.
  - edits: “this medicine” → “Omeprazole”

**L49.0** `Incomplete Sentence` (0.637) → `excluded_incomplete`
- original: Do not give this medicine to a child without medical advice.
- pronoun resolved: Do not give Omeprazole to a child without medical advice.
  - edits: “this medicine” → “Omeprazole”

## How should I take omeprazole?

**L52.0** `Incomplete Sentence` (0.889) → `excluded_incomplete`
- original: Take omeprazole exactly as directed on the label, or as prescribed by your doctor.

**L52.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L53.0** `Incomplete Sentence` (0.946) → `excluded_incomplete`
- original: Use Prilosec OTC (over-the-counter) exactly as directed on the label, or as prescribed by your doctor.

**L54.0** `Incomplete Sentence` (0.96) → `excluded_incomplete`
- original: Read and carefully follow any Instructions for Use provided with your medicine.

**L54.1** `Incomplete Sentence` (0.902) → `excluded_incomplete`
- original: Ask your doctor or pharmacist if you do not understand these instructions.

**L55.0** `Incomplete Sentence` (0.968) → `excluded_incomplete`
- original: Shake the oral suspension (liquid) before you measure a dose.

**L55.1** `Incomplete Sentence` (0.955) → `excluded_incomplete`
- original: Use the dosing syringe provided, or use a medicine dose-measuring device (not a kitchen spoon).

**L56.0** `Compound Sentence` (0.393) → `decomposed`
- original: If you cannot swallow a capsule whole, open it and sprinkle the medicine into a spoonful of applesauce.
  - S1: If you cannot swallow a capsule whole, open it.
  - S2: Sprinkle the medicine into a spoonful of applesauce.

**L56.1** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Swallow the mixture right away without chewing.

**L56.2** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Do not save it for later use.

**L57.0** `Simple Sentence` (0.975) → `passthrough`
- original: You must dissolve omeprazole powder in a small amount of water.

**L57.1** `Complex Sentence` (0.394) → `decomposed`
- original: This mixture can either be swallowed or given through a nasogastric (NG) feeding tube using a catheter-tipped syringe.
  - S1: This mixture can be swallowed.
  - S2: This mixture can be given through a nasogastric (NG) feeding tube.
  - S3: The mixture is given using a catheter-tipped syringe.

**L58.0** `Incomplete Sentence` (0.801) → `excluded_incomplete`
- original: Use this medicine for the full prescribed length of time, even if your symptoms quickly improve.

**L59.0** `Simple Sentence` (0.989) → `passthrough`
- original: OTC omeprazole should be taken for only 14 days in a row.

**L59.1** `Simple Sentence` (0.972) → `passthrough`
- original: It may take 1 to 4 days before your symptoms improve.

**L59.2** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Allow at least 4 months to pass before you start a new 14-day course of treatment.

**L60.0** `Incomplete Sentence` (0.757) → `excluded_incomplete`
- original: Call your doctor if your symptoms do not improve, or if they get worse.

**L61.0** `Simple Sentence` (0.987) → `passthrough`
- original: Some conditions are treated with a combination of omeprazole and antibiotics.

**L61.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Use all medications as directed.

**L62.0** `Simple Sentence` (0.99) → `passthrough`
- original: This medicine can affect the results of certain medical tests.

**L62.1** `Incomplete Sentence` (0.903) → `excluded_incomplete`
- original: Tell any doctor who treats you that you are using this medicine.
- pronoun resolved: Tell any doctor who treats you that you are using omeprazole.
  - edits: “this medicine.” → “omeprazole.”

**L63.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Store at room temperature away from moisture and heat.

## How long does omeprazole take to work?

**L66.0** `Compound Sentence` (0.921) → `decomposed`
- original: Omeprazole usually takes 1 to 4 days of once-daily dosing to reach its full effect, and some people get complete relief of their symptoms within 24 hours.
- pronoun resolved: Omeprazole usually takes 1 to 4 days of once-daily dosing to reach Omeprazole's full effect, and some people get complete relief of their symptoms within 24 hours.
  - edits: “its” → “Omeprazole's”
  - S1: Omeprazole usually takes 1 to 4 days of once-daily dosing to reach Omeprazole's full effect.
  - S2: Some people get complete relief of their symptoms within 24 hours.

**L66.1** `Compound Sentence` (0.94) → `decomposed`
- original: It begins reducing stomach acid within about 1 hour of the first dose, but it is not designed to relieve heartburn right away.
- pronoun resolved: Omeprazole begins reducing stomach acid within about 1 hour of the first dose, but Omeprazole is not designed to relieve heartburn right away.
  - edits: “It” → “Omeprazole”; “it” → “Omeprazole”
  - S1: Omeprazole begins reducing stomach acid within about 1 hour of the first dose.
  - S2: Omeprazole is not designed to relieve heartburn right away.

**L67.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: What to expect after you start taking omeprazole:

**L68.0** `Simple Sentence` (0.988) → `passthrough`
- original: Within 1 hour: omeprazole starts to reduce acid production in your stomach

**L69.0** `Simple Sentence` (0.982) → `passthrough`
- original: Around 2 hours: a single dose reaches its strongest acid-lowering effect
- pronoun resolved: Around 2 hours: a single dose reaches Omeprazole's strongest acid-lowering effect
  - edits: “its” → “Omeprazole's”

**L70.0** `Simple Sentence` (0.978) → `passthrough`
- original: Within 24 hours: some people get complete relief of their symptoms

**L71.0** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: 1 to 4 days: most people feel the full benefit

**L72.0** `Simple Sentence` (0.956) → `passthrough`
- original: About 4 days: the acid-lowering effect reaches its maximum with once-daily dosing
- pronoun resolved: About 4 days: the acid-lowering effect reaches Omeprazole's maximum with once-daily dosing
  - edits: “its” → “Omeprazole's”

**L73.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: How fast does omeprazole start working?

**L73.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L74.0** `Compound Sentence` (0.965) → `decomposed`
- original: Omeprazole starts working within about 1 hour, and a single dose has its strongest effect at around 2 hours.
- pronoun resolved: Omeprazole starts working within about 1 hour, and a single dose has Omeprazole's strongest effect at around 2 hours.
  - edits: “its” → “Omeprazole's”
  - S1: Omeprazole starts working within about 1 hour.
  - S2: A single dose has Omeprazole's strongest effect at around 2 hours.

**L74.1** `Compound Sentence` (0.484) → `decomposed`
- original: This is when the medicine begins lowering acid production, which is not the same as when your heartburn or acid reflux symptoms stop.
- pronoun resolved: Omeprazole is when the medicine begins lowering acid production, which is not the same as when your heartburn or acid reflux symptoms stop.
  - edits: “This” → “Omeprazole”
  - S1: Omeprazole is when the medicine begins lowering acid production.
  - S2: This is not the same as when your heartburn or acid reflux symptoms stop.

**L75.0** `Simple Sentence` (0.986) → `passthrough`
- original: Omeprazole does not work immediately on symptoms you are already feeling.

**L75.1** `Complex Sentence` (0.782) → `decomposed`
- original: It is a proton pump inhibitor (PPI), which means it reduces how much acid your stomach makes rather than neutralizing acid that is already there.
- pronoun resolved: It is a proton pump inhibitor (PPI), which means Omeprazole reduces how much acid your stomach makes rather than neutralizing acid that is already there.
  - edits: “it” → “Omeprazole”
  - S1: It is a proton pump inhibitor (PPI).
  - S2: Omeprazole reduces how much acid your stomach makes.
  - S3: Omeprazole does not neutralize acid that is already there.

## What happens if I miss a dose?

**L78.0** `Compound Sentence` (0.555) → `decomposed`
- original: Take the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - S1: Take the medicine as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L78.1** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

## What happens if I overdose?

**L81.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

## What to avoid

**L84.0** `Simple Sentence` (0.722) → `passthrough`
- original: Omeprazole can cause diarrhea, which may be a sign of a new infection.

**L84.1** `Simple Sentence` (0.351) → `passthrough`
- original: If you have diarrhea that is watery or bloody, call your doctor before using anti-diarrhea medicine.

## Omeprazole side effects

**L87.0** `Compound Sentence` (0.43) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to omeprazole: hives; difficulty breathing; swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to omeprazole.
  - S2: Signs of an allergic reaction to omeprazole include hives.
  - S3: Signs of an allergic reaction to omeprazole include difficulty breathing.
  - S4: Signs of an allergic reaction to omeprazole include swelling of your face, lips, tongue, or throat.

**L88.0** `Incomplete Sentence` (0.899) → `excluded_incomplete`
- original: Stop using this medicine and call your doctor at once if you have:
- pronoun resolved: Stop using Omeprazole and call your doctor at once if you have:
  - edits: “this medicine” → “Omeprazole”

**L89.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: severe stomach pain, diarrhea that is watery or bloody;

**L90.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: new or unusual pain in your wrist, thigh, hip, or back;

**L91.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: seizure (convulsions);

**L92.0** `Incomplete Sentence` (0.96) → `excluded_incomplete`
- original: kidney problems - fever, rash, nausea, loss of appetite, joint pain, urinating less than usual, blood in your urine, weight gain;

**L93.0** `Incomplete Sentence` (0.935) → `excluded_incomplete`
- original: low magnesium - seizures, dizziness, irregular heartbeats, feeling jittery, muscle aches or weakness, muscle cramps, muscle spasms, or spasms of the hands, feet, or voice;

**L94.0** `Incomplete Sentence` (0.963) → `excluded_incomplete`
- original: new or worsening symptoms of lupus - joint pain, and a skin rash on your cheeks or arms that worsens in sunlight.

**L95.0** `Incomplete Sentence` (0.705) → `excluded_incomplete`
- original: severe skin reactions - skin rash with blistering, peeling, or bleeding, fever, chills, body aches, shortness of breath, or enlarged lymph nodes.

**L96.0** `Simple Sentence` (0.985) → `passthrough`
- original: Taking omeprazole long-term may cause you to develop stomach growths called fundic gland polyps.

**L96.1** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Talk with your doctor about this risk.

**L97.0** `Simple Sentence` (0.882) → `passthrough`
- original: If you use this medicine for longer than 3 years, you could develop a vitamin B-12 deficiency.

**L97.1** `Compound Sentence` (0.447) → `decomposed`
- original: Talk to your doctor if you develop symptoms such as shortness of breath, lightheadedness, irregular heartbeat, muscle weakness, pale skin, feeling tired, mood changes, and tingling or numbness in the arms and legs.
  - S1: Talk to your doctor if you develop symptoms.
  - S2: These symptoms include shortness of breath, lightheadedness, irregular heartbeat, muscle weakness, pale skin, feeling tired, mood changes, and tingling or numbness in the arms and legs.

**L98.0** `Simple Sentence` (0.95) → `passthrough`
- original: Common side effects of omeprazole may include:

**L99.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: cold symptoms such as stuffy nose, sneezing, sore throat (especially in children);

**L100.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: fever (especially in children);

**L101.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: stomach pain, gas;

**L102.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: nausea, vomiting, diarrhea; or

**L103.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: headache.

**L104.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L104.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L104.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## What other drugs will affect omeprazole?

**L107.0** `Simple Sentence` (0.975) → `passthrough`
- original: Sometimes it is not safe to use certain medications at the same time.

**L107.1** `Complex Sentence` (0.892) → `decomposed`
- original: Some drugs can affect your blood levels of other drugs you take, which may increase side effects or make the medications less effective.
  - S1: Some drugs can affect your blood levels of other drugs you take.
  - S2: This may increase side effects.
  - S3: This may make the medications less effective.

**L108.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Tell your doctor about all your current medicines.

**L108.1** `Simple Sentence` (0.99) → `passthrough`
- original: Many drugs can affect omeprazole, especially:

**L109.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: digoxin;

**L110.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: clopidogrel;

**L111.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: methotrexate;

**L112.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: St. John's wort;

**L113.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a diuretic or "water pill"; or

**L114.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: an antibiotic - amoxicillin, clarithromycin, rifampin.

**L115.0** `Simple Sentence` (0.512) → `passthrough`
- original: This list is not complete and many other drugs may interact with omeprazole.

**L115.1** `Incomplete Sentence` (0.491) → `excluded_incomplete`
- original: This includes prescription and over-the-counter medicines, vitamins, and herbal products.
- pronoun resolved: List includes prescription and over-the-counter medicines, vitamins, and herbal products.
  - edits: “This” → “List”

**L115.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.

## Popular FAQ

**L118.0** `Incomplete Sentence` (0.877) → `excluded_incomplete`
- original: Q: What foods should I avoid when taking omeprazole?

**L118.1** `Complex Sentence` (0.745) → `decomposed`
- original: A: There are no specific foods that interact with omeprazole, therefore there are no foods that you need to avoid.
  - S1: There are no specific foods that interact with omeprazole.
  - S2: Therefore, there are no foods that you need to avoid.

**L119.0** `Incomplete Sentence` (0.972) → `excluded_incomplete`
- original: Q: Pantoprazole vs. omeprazole: What's the difference between them?

**L119.1** `Complex Sentence` (0.931) → `decomposed`
- original: A: Pantoprazole and omeprazole are both proton pump inhibitors (PPIs) that reduce stomach acid and show similar effectiveness for healing acid‑related conditions such as erosive esophagitis.
  - S1: Pantoprazole and omeprazole are both proton pump inhibitors (PPIs).
  - S2: These PPIs reduce stomach acid.
  - S3: They show similar effectiveness for healing acid‑related conditions.
  - S4: An example of such a condition is erosive esophagitis.

**L119.2** `Complex Sentence` (0.516) → `decomposed`
- original: Their main differences relate to FDA‑approved uses, availability (omeprazole is OTC; pantoprazole is prescription), timing with food, and the option for intravenous (IV) pantoprazole in the hospital setting.
- pronoun resolved: Pantoprazole and omeprazole's main differences relate to FDA‑approved uses, availability (omeprazole is OTC; pantoprazole is prescription), timing with food, and the option for intravenous (IV) pantoprazole in the hospital setting.
  - edits: “Their” → “Pantoprazole and omeprazole's”
  - S1: Pantoprazole and omeprazole's main differences relate to FDA‑approved uses.
  - S2: The differences also relate to availability.
  - S3: Omeprazole is OTC.
  - S4: Pantoprazole is prescription.
  - S5: The differences also relate to timing with food.
  - S6: The differences also relate to the option for intravenous (IV) pantoprazole in the hospital setting.

**L120.0** `Simple Sentence` (0.798) → `passthrough`
- original: Q: How soon after taking levothyroxine can I take omeprazole?

**L120.1** `Compound Sentence` (0.702) → `decomposed`
- original: A: There is a known drug interaction between levothyroxine and omeprazole, but the timing of when you take the two medicines is not relevant.
  - S1: There is a known drug interaction between levothyroxine and omeprazole.
  - S2: The timing of when you take the two medicines is not relevant.

**L120.2** `Simple Sentence` (0.986) → `passthrough`
- original: Omeprazole decreases the absorption of your thyroid medication.

**L120.3** `Complex Sentence` (0.944) → `decomposed`
- original: If you need to be on a course of omeprazole while taking levothyroxine, your doctor may order more frequent laboratory testing to confirm you are absorbing enough levothyroxine.
  - S1: If you need to be on a course of omeprazole while taking levothyroxine.
  - S2: Your doctor may order more frequent laboratory testing.
  - S3: The testing is to confirm you are absorbing enough levothyroxine.

**L121.0** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: Q: Should I take omeprazole with or without food?

**L121.1** `Simple Sentence` (0.969) → `passthrough`
- original: A: It is usually best to take Omeprazole 1 hour before meals.
- pronoun resolved: A: Omeprazole is usually best to take Omeprazole 1 hour before meals.
  - edits: “It” → “Omeprazole”

**L121.2** `Complex Sentence` (0.78) → `decomposed`
- original: When omeprazole is taken with food, it reduces the amount of omeprazole that reaches the bloodstream.
- pronoun resolved: When omeprazole is taken with food, omeprazole reduces the amount of omeprazole that reaches the bloodstream.
  - edits: “it” → “omeprazole”
  - S1: Omeprazole reduces the amount of omeprazole that reaches the bloodstream.
  - S2: This occurs when omeprazole is taken with food.

**L122.0** `Simple Sentence` (0.843) → `passthrough`
- original: Q: Can you take an antacid with omeprazole?

**L122.1** `Complex Sentence` (0.844) → `decomposed`
- original: A: You can take an antacid with omeprazole if you are still getting symptoms of indigestion because it can take several days for omeprazole to start working.
- pronoun resolved: A: You can take an antacid with omeprazole if you are still getting symptoms of indigestion because omeprazole can take several days for omeprazole to start working.
  - edits: “it” → “omeprazole”
  - S1: You can take an antacid with omeprazole.
  - S2: You can do this if you are still getting symptoms of indigestion.
  - S3: This is because omeprazole can take several days to start working.

**L122.2** `Compound Sentence` (0.606) → `decomposed`
- original: Take omeprazole as directed (usually taken once daily on an empty stomach), and take antacids as needed to relieve indigestion pain after eating.
  - S1: Take omeprazole as directed.
  - S2: It is usually taken once daily on an empty stomach.
  - S3: Take antacids as needed.
  - S4: This is done to relieve indigestion pain after eating.

**L122.3** `Incomplete Sentence` (0.329) → `excluded_incomplete`
- original: But tell your doctor if several weeks have gone past and omeprazole does not seem to be working or you are still taking antacids.

**L123.0** `Incomplete Sentence` (0.818) → `excluded_incomplete`
- original: Q: Is famotidine safer than omeprazole for heartburn?

**L123.1** `Complex Sentence` (0.695) → `decomposed`
- original: A: For most people with mild, occasional heartburn, famotidine is usually the safer first choice because it works quickly, can be taken as needed, and has fewer long‑term safety concerns than omeprazole.
- pronoun resolved: A: For most people with mild, occasional heartburn, famotidine is usually the safer first choice because famotidine works quickly, can be taken as needed, and has fewer long‑term safety concerns than omeprazole.
  - edits: “it” → “famotidine”
  - S1: For most people with mild, occasional heartburn, famotidine is usually the safer first choice.
  - S2: Famotidine works quickly.
  - S3: Famotidine can be taken as needed.
  - S4: Famotidine has fewer long-term safety concerns than omeprazole.

**L123.2** `Compound-Complex Sentence` (0.834) → `decomposed`
- original: Omeprazole, a stronger acid reducer, may be a better option if you have frequent heartburn two or more days per week or confirmed GERD, but it is linked with more potential risks when used for many months or at high doses.
- pronoun resolved: Omeprazole, a stronger acid reducer, may be a better option if you have frequent heartburn two or more days per week or confirmed GERD, but omeprazole is linked with more potential risks when used for many months or at high doses.
  - edits: “it” → “omeprazole”
  - S1: Omeprazole is a stronger acid reducer.
  - S2: Omeprazole may be a better option if you have frequent heartburn two or more days per week.
  - S3: Omeprazole may be a better option if you have confirmed GERD.
  - S4: Omeprazole is linked with more potential risks when used for many months.
  - S5: Omeprazole is linked with more potential risks when used at high doses.

**L124.0** `Simple Sentence` (0.796) → `passthrough`
- original: Q: Can I take omeprazole in the morning and famotidine at night?

**L124.1** `Compound Sentence` (0.815) → `decomposed`
- original: A: Yes, you could take omeprazole in the morning and famotidine at night but there are not many studies investigating this approach.
  - S1: You could take omeprazole in the morning and famotidine at night.
  - S2: There are not many studies investigating this approach.

**L124.2** `Complex Sentence` (0.968) → `decomposed`
- original: Preliminary results suggest that taking your medication this way may provide superior control of gastric acid secretion at night without compromising the effectiveness of omeprazole in the morning.
  - S1: Preliminary results suggest that taking your medication this way may provide superior control of gastric acid secretion at night.
  - S2: This method does not compromise the effectiveness of omeprazole in the morning.

**L124.3** `Simple Sentence` (0.83) → `passthrough`
- original: More research is needed.

**L125.0** `Simple Sentence` (0.66) → `passthrough`
- original: Q: Is omeprazole (Prilosec) bad for your kidneys?

**L125.1** `Compound Sentence` (0.883) → `decomposed`
- original: A: Omeprazole (Prilosec) is a proton pump inhibitor (PPI) that is used to reduce the amount of acid in your stomach and it can be bad for your kidneys.
- pronoun resolved: A: Omeprazole (Prilosec) is a proton pump inhibitor (PPI) that is used to reduce the amount of acid in your stomach and Omeprazole can be bad for your kidneys.
  - edits: “it” → “Omeprazole”
  - S1: Omeprazole (Prilosec) is a proton pump inhibitor (PPI) that is used to reduce the amount of acid in your stomach.
  - S2: Omeprazole can be bad for your kidneys.

**L125.2** `Compound Sentence` (0.941) → `decomposed`
- original: It can cause acute kidney injury and may also worsen the progression of chronic kidney disease (CKD).
- pronoun resolved: Omeprazole can cause acute kidney injury and may also worsen the progression of chronic kidney disease (CKD).
  - edits: “It” → “Omeprazole”
  - S1: Omeprazole can cause acute kidney injury.
  - S2: Omeprazole may also worsen the progression of chronic kidney disease (CKD).

**L126.0** `Incomplete Sentence` (0.966) → `excluded_incomplete`
- original: Q: Does omeprazole cause cancer?

**L126.1** `Complex Sentence` (0.961) → `decomposed`
- original: A: Long-term use of proton pump inhibitor (PPI) acid-suppressing agents, such as omeprazole, has been associated with an increased risk of stomach cancer (also called gastric cancer).
  - S1: Long-term use of proton pump inhibitor (PPI) acid-suppressing agents has been associated with an increased risk of stomach cancer.
  - S2: Stomach cancer is also called gastric cancer.
  - S3: Omeprazole is an example of a proton pump inhibitor (PPI) acid-suppressing agent.

**L126.2** `Complex Sentence` (0.825) → `decomposed`
- original: This is based on the results of several observational studies and is thought to be because PPIs such as omeprazole are potent gastric acid suppressants that may increase the risk of gastric cancer by causing atrophy (thinning) of the stomach lining, elevating levels of a hormone called gastrin, and an overgrowth of bacteria in the stomach.
  - S1: This is based on the results of several observational studies.
  - S2: It is thought to be because PPIs such as omeprazole are potent gastric acid suppressants.
  - S3: These suppressants may increase the risk of gastric cancer.
  - S4: They may cause atrophy (thinning) of the stomach lining.
  - S5: They may elevate levels of a hormone called gastrin.
  - S6: They may cause an overgrowth of bacteria in the stomach.
