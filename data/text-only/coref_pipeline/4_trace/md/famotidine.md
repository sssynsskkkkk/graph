# Famotidine — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/famotidine.txt` · 90 sentences · 15 changed by pronoun resolution · 129 sentences sent to EDC

## What is famotidine?

**L5.0** `Simple Sentence` (0.921) → `passthrough`
- original: Famotidine is a histamine-2 blocker that works by decreasing the amount of acid the stomach produces.

**L6.0** `Simple Sentence` (0.984) → `passthrough`
- original: Famotidine is used to treat and prevent ulcers in the stomach and intestines.

**L6.1** `Simple Sentence` (0.609) → `passthrough`
- original: It also treats conditions in which the stomach produces too much acid, such as Zollinger-Ellison syndrome.
- pronoun resolved: Famotidine also treats conditions in which the stomach produces too much acid, such as Zollinger-Ellison syndrome.
  - edits: “It” → “Famotidine”

**L7.0** `Complex Sentence` (0.56) → `decomposed`
- original: Famotidine also treats gastroesophageal reflux disease (GERD) and other conditions in which acid backs up from the stomach into the esophagus, causing heartburn.
  - S1: Famotidine treats gastroesophageal reflux disease (GERD).
  - S2: Famotidine treats other conditions in which acid backs up from the stomach into the esophagus.
  - S3: This acid backup causes heartburn.

**L8.0** `Complex Sentence` (0.629) → `decomposed`
- original: The Zantac 360 brand of this medicine does not contain ranitidine, a medicine that was withdrawn from market in the United States.
- pronoun resolved: The Zantac 360 brand of Famotidine does not contain ranitidine, a medicine that was withdrawn from market in the United States.
  - edits: “this medicine” → “Famotidine”
  - S1: The Zantac 360 brand of Famotidine does not contain ranitidine.
  - S2: Ranitidine is a medicine.
  - S3: Ranitidine was withdrawn from market in the United States.

## Warnings

**L11.0** `Complex Sentence` (0.635) → `decomposed`
- original: Before taking famotidine, tell your doctor if you have kidney or liver disease, a history of Long QT syndrome, stomach cancer or other problems, or asthma, COPD, or other breathing problems.
  - S1: Before taking famotidine, tell your doctor if you have kidney or liver disease.
  - S2: Tell your doctor if you have a history of Long QT syndrome.
  - S3: Tell your doctor if you have stomach cancer or other problems.
  - S4: Tell your doctor if you have asthma, COPD, or other breathing problems.

**L12.0** `Simple Sentence` (0.932) → `passthrough`
- original: Famotidine may be only part of a complete program of treatment that also includes changes in diet or lifestyle habits.

**L12.1** `Incomplete Sentence` (0.969) → `excluded_incomplete`
- original: Follow your doctor's instructions very closely.

**L13.0** `Simple Sentence` (0.98) → `passthrough`
- original: Heartburn is often confused with the first symptoms of a heart attack.

**L13.1** `Incomplete Sentence` (0.247) → `excluded_incomplete`
- original: Seek emergency medical attention if you have chest pain or heavy feeling, pain spreading to the jaw, arm or shoulder, nausea, sweating, anxiety, light-headedness and a general ill feeling.

**L14.0** `Compound Sentence` (0.478) → `decomposed`
- original: Do not use over-the-counter famotidine without a doctor's advice if you have trouble or pain swallowing food, vomiting with blood, or bloody or black stools.
  - S1: Do not use over-the-counter famotidine without a doctor's advice if you have trouble or pain swallowing food.
  - S2: Do not use over-the-counter famotidine without a doctor's advice if you are vomiting with blood.
  - S3: Do not use over-the-counter famotidine without a doctor's advice if you have bloody or black stools.

**L14.1** `Simple Sentence` (0.98) → `passthrough`
- original: These may be signs of a serious condition.

## Before taking this medicine

**L17.0** `Complex Sentence` (0.748) → `decomposed`
- original: You should not use this medicine if you are allergic to famotidine or similar medicines such as ranitidine (Zantac), cimetidine (Tagamet), or nizatidine (Axid).
- pronoun resolved: You should not use Famotidine if you are allergic to famotidine or similar medicines such as ranitidine (Zantac), cimetidine (Tagamet), or nizatidine (Axid).
  - edits: “this medicine” → “Famotidine”
  - S1: You should not use Famotidine if you are allergic to famotidine.
  - S2: You should not use Famotidine if you are allergic to similar medicines.
  - S3: Similar medicines include ranitidine (Zantac), cimetidine (Tagamet), or nizatidine (Axid).

**L18.0** `Simple Sentence` (0.739) → `passthrough`
- original: To make sure this medicine is safe for you, tell your doctor or pharmacist if you have ever had:
- pronoun resolved: To make sure Famotidine is safe for you, tell your doctor or pharmacist if you have ever had:
  - edits: “this medicine” → “Famotidine”

**L19.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: kidney disease;

**L20.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: liver disease;

**L21.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: cancer stomach; or

**L22.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: long QT syndrome (in you or a family member).

**L23.0** `Incomplete Sentence` (0.552) → `excluded_incomplete`
- original: Ask a doctor before using famotidine if you are pregnant or breastfeeding.

**L24.0** `Simple Sentence` (0.958) → `passthrough`
- original: Famotidine injection may contain an ingredient that can cause serious side effects or death in very young or premature babies.

**L24.1** `Incomplete Sentence` (0.721) → `excluded_incomplete`
- original: Do not give this injection to a newborn or premature baby.
- pronoun resolved: Do not give Famotidine injection to a newborn or premature baby.
  - edits: “this” → “Famotidine”

## How should I take famotidine?

**L27.0** `Incomplete Sentence` (0.949) → `excluded_incomplete`
- original: Use famotidine exactly as directed on the label, or as prescribed by your doctor.

**L28.0** `Simple Sentence` (0.99) → `passthrough`
- original: Famotidine oral is taken by mouth.

**L29.0** `Simple Sentence` (0.987) → `passthrough`
- original: Famotidine injection is given as an infusion into a vein.

**L29.1** `Simple Sentence` (0.937) → `passthrough`
- original: A healthcare provider will give you this injection if you are unable to take the medicine by mouth.
- pronoun resolved: A healthcare provider will give you Famotidine if you are unable to take the medicine by mouth.
  - edits: “this injection” → “Famotidine”

**L30.0** `Simple Sentence` (0.986) → `passthrough`
- original: You may take famotidine oral with or without food.

**L31.0** `Incomplete Sentence` (0.974) → `excluded_incomplete`
- original: Shake the bottle of Pepcid suspension (liquid) vigorously for 5 to 10 seconds prior to each use.

**L31.1** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Measure the liquid medicine carefully.

**L31.2** `Incomplete Sentence` (0.955) → `excluded_incomplete`
- original: Use the dosing syringe provided, or use a medicine dose-measuring device (not a kitchen spoon).

**L32.0** `Compound Sentence` (0.96) → `decomposed`
- original: Most ulcers heal within 4 weeks of treatment, but it may take up to 8 weeks of using this medicine before your ulcer heals.
- pronoun resolved: Most ulcers heal within 4 weeks of treatment, but ulcers may take up to 8 weeks of using this medicine before your ulcer heals.
  - edits: “it” → “ulcers”
  - S1: Most ulcers heal within 4 weeks of treatment.
  - S2: Ulcers may take up to 8 weeks of using this medicine before your ulcer heals.

**L32.1** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Keep using the medication as directed.

**L33.0** `Incomplete Sentence` (0.429) → `excluded_incomplete`
- original: Call your doctor if the condition you are treating with this medicine does not improve, or if it gets worse while using this medicine.
- pronoun resolved: Call your doctor if the condition you are treating with this medicine does not improve, or if condition gets worse while using this medicine.
  - edits: “it” → “condition”

**L34.0** `Simple Sentence` (0.932) → `passthrough`
- original: Famotidine may be only part of a complete program of treatment that also includes changes in diet or lifestyle habits.

**L34.1** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Follow all instructions of your doctor or dietitian.

**L35.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Store at room temperature away from moisture, heat, and light.

**L35.1** `Incomplete Sentence` (0.94) → `excluded_incomplete`
- original: Do not allow the liquid medicine to freeze.

**L36.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Throw away any unused liquid that is older than 30 days.

## What happens if I miss a dose?

**L39.0** `Compound Sentence` (0.555) → `decomposed`
- original: Take the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - S1: Take the medicine as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L39.1** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

## What happens if I overdose?

**L42.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

## What to avoid

**L45.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Avoid drinking alcohol.

**L45.1** `Simple Sentence` (0.99) → `passthrough`
- original: It can increase the risk of damage to your stomach.
- pronoun resolved: Drinking alcohol can increase the risk of damage to your stomach.
  - edits: “It” → “Drinking alcohol”

**L46.0** `Incomplete Sentence` (0.968) → `excluded_incomplete`
- original: Avoid taking other stomach acid reducers unless your doctor has told you to.

**L46.1** `Compound Sentence` (0.524) → `decomposed`
- original: However, you may take an antacid (such as Maalox, Mylanta, Gaviscon, Milk of Magnesia, Rolaids, or Tums) with famotidine.
  - S1: However, you may take an antacid with famotidine.
  - S2: Examples of antacids include Maalox, Mylanta, Gaviscon, Milk of Magnesia, Rolaids, and Tums.

## Famotidine side effects

**L49.0** `Compound Sentence` (0.46) → `decomposed`
- original: Get emergency medical help if you have any signs of an allergic reaction to famotidine: hives; difficult breathing; swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have any signs of an allergic reaction to famotidine.
  - S2: Signs of an allergic reaction to famotidine include hives.
  - S3: Signs of an allergic reaction to famotidine also include difficult breathing.
  - S4: Signs of an allergic reaction to famotidine also include swelling of your face, lips, tongue, or throat.

**L50.0** `Incomplete Sentence` (0.912) → `excluded_incomplete`
- original: Stop using this medicine and call your doctor at once if you have:
- pronoun resolved: Stop using Famotidine and call your doctor at once if you have:
  - edits: “this medicine” → “Famotidine”

**L51.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: confusion, hallucinations, agitation, lack of energy;

**L52.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a seizure;

**L53.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: fast or pounding heartbeats, sudden dizziness (like you might pass out).

**L54.0** `Simple Sentence` (0.844) → `passthrough`
- original: Some side effects may be more likely in older adults and in people who have severe kidney disease.

**L55.0** `Simple Sentence` (0.931) → `passthrough`
- original: Common famotidine side effects may include:

**L56.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: headache;

**L57.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: dizziness; or

**L58.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: constipation or diarrhea.

**L59.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L59.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L59.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## What other drugs will interact with famotidine?

**L62.0** `Simple Sentence` (0.991) → `passthrough`
- original: Famotidine oral can make it harder for your body to absorb other medicines you take by mouth.

**L62.1** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Tell your doctor if you are taking:

**L63.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: cefditoren;

**L64.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: dasatinib;

**L65.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: delavirdine;

**L66.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: fosamprenavir; or

**L67.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: tizanidine.

**L68.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L68.1** `Complex Sentence` (0.513) → `decomposed`
- original: Other drugs may interact with famotidine, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may interact with famotidine.
  - S2: These include prescription and over-the-counter medicines.
  - S3: These also include vitamins and herbal products.

**L68.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.

## Popular FAQ

**L71.0** `Incomplete Sentence` (0.954) → `excluded_incomplete`
- original: Q: How long does it take for famotidine to work?

**L71.1** `Simple Sentence` (0.986) → `passthrough`
- original: A: Famotidine starts to block stomach acid within 15 minutes to 1 hour of taking the medicine.

**L71.2** `Compound Sentence` (0.791) → `decomposed`
- original: The maximum effect usually occurs within 1 to 3 hours, and lasts for 10 to 12 hours after a single dose.
  - S1: The maximum effect usually occurs within 1 to 3 hours.
  - S2: It lasts for 10 to 12 hours after a single dose.

**L71.3** `Simple Sentence` (0.917) → `passthrough`
- original: It will also work to prevent heartburn if taken 10 to 60 minutes before a meal.
- pronoun resolved: Famotidine will also work to prevent heartburn if taken 10 to 60 minutes before a meal.
  - edits: “It” → “Famotidine”

**L71.4** `Incomplete Sentence` (0.961) → `excluded_incomplete`
- original: Do not take more than 2 tablets in 24 hours.

**L72.0** `Incomplete Sentence` (0.838) → `excluded_incomplete`
- original: Q: Is it better to take famotidine in the morning or at night?
- pronoun resolved: Q: Is famotidine better to take famotidine in the morning or at night?
  - edits: “it” → “famotidine”

**L72.1** `Complex Sentence` (0.836) → `decomposed`
- original: A: In general, you can take over-the-counter (OTC) famotidine (Pepcid AC, Zantac 360) at any time of the day or night to help treat heartburn symptoms.
  - S1: You can take over-the-counter (OTC) famotidine at any time of the day or night.
  - S2: Famotidine is also known as Pepcid AC or Zantac 360.
  - S3: Taking famotidine helps treat heartburn symptoms.

**L72.2** `Complex Sentence` (0.951) → `decomposed`
- original: Studies have shown it is best to take OTC famotidine 1 hour before an evening meal to help prevent heartburn and indigestion in the evening and during bedtime which may interfere with your sleep.
  - S1: Studies have shown it is best to take OTC famotidine 1 hour before an evening meal.
  - S2: This helps prevent heartburn and indigestion in the evening and during bedtime.
  - S3: These symptoms may interfere with your sleep.

**L72.3** `Incomplete Sentence` (0.887) → `excluded_incomplete`
- original: Talk to your healthcare provider if your symptoms are severe or ongoing after 14 days.

**L73.0** `Incomplete Sentence` (0.878) → `excluded_incomplete`
- original: Q: How much famotidine can I take in one day?

**L73.1** `Complex Sentence` (0.902) → `decomposed`
- original: A: The maximum daily dose of over-the-counter (OTC) famotidine (Pepcid AC, Zantac 360) in adults and children over 12 years of age is 40 mg per day unless your doctor prescribes it otherwise.
- pronoun resolved: A: The maximum daily dose of over-the-counter (OTC) famotidine (Pepcid AC, Zantac 360) in adults and children over 12 years of age is 40 mg per day unless your doctor prescribes famotidine otherwise.
  - edits: “it” → “famotidine”
  - S1: The maximum daily dose of over-the-counter (OTC) famotidine in adults and children over 12 years of age is 40 mg per day.
  - S2: This applies to Pepcid AC and Zantac 360.
  - S3: The dose may be different if your doctor prescribes famotidine otherwise.

**L73.2** `Simple Sentence` (0.714) → `passthrough`
- original: If your symptoms persist more than 2 weeks, contact your doctor.

**L73.3** `Simple Sentence` (0.896) → `passthrough`
- original: Higher doses may be used for other conditions such as erosive esophagitis or Zollinger-Ellison Syndrome.

**L74.0** `Incomplete Sentence` (0.818) → `excluded_incomplete`
- original: Q: Is famotidine safer than omeprazole for heartburn?

**L74.1** `Complex Sentence` (0.695) → `decomposed`
- original: A: For most people with mild, occasional heartburn, famotidine is usually the safer first choice because it works quickly, can be taken as needed, and has fewer long‑term safety concerns than omeprazole.
- pronoun resolved: A: For most people with mild, occasional heartburn, famotidine is usually the safer first choice because famotidine works quickly, can be taken as needed, and has fewer long‑term safety concerns than omeprazole.
  - edits: “it” → “famotidine”
  - S1: For most people with mild, occasional heartburn, famotidine is usually the safer first choice.
  - S2: Famotidine works quickly.
  - S3: Famotidine can be taken as needed.
  - S4: Famotidine has fewer long-term safety concerns than omeprazole.

**L74.2** `Compound-Complex Sentence` (0.834) → `decomposed`
- original: Omeprazole, a stronger acid reducer, may be a better option if you have frequent heartburn two or more days per week or confirmed GERD, but it is linked with more potential risks when used for many months or at high doses.
- pronoun resolved: Omeprazole, a stronger acid reducer, may be a better option if you have frequent heartburn two or more days per week or confirmed GERD, but Omeprazole is linked with more potential risks when used for many months or at high doses.
  - edits: “it” → “Omeprazole”
  - S1: Omeprazole is a stronger acid reducer.
  - S2: Omeprazole may be a better option if you have frequent heartburn two or more days per week.
  - S3: Omeprazole may be a better option if you have confirmed GERD.
  - S4: Omeprazole is linked with more potential risks when used for many months.
  - S5: Omeprazole is linked with more potential risks when used at high doses.

**L75.0** `Incomplete Sentence` (0.518) → `excluded_incomplete`
- original: Q: Can you take famotidine long term?

**L75.1** `Simple Sentence` (0.625) → `passthrough`
- original: A: Famotidine (brand name: Pepcid AC, Zantac 360) should not be used for longer than 14 days if you are treating heartburn symptoms.

**L75.2** `Complex Sentence` (0.86) → `decomposed`
- original: Famotidine may be used for a longer period under the direction of your healthcare provider for treatment of intestinal or stomach ulcers, gastroesophageal reflux (GERD), erosive esophagitis, or other acid-related conditions.
  - S1: Famotidine may be used for a longer period under the direction of your healthcare provider.
  - S2: It is used for the treatment of intestinal or stomach ulcers.
  - S3: It is used for the treatment of gastroesophageal reflux (GERD).
  - S4: It is used for the treatment of erosive esophagitis.
  - S5: It is used for the treatment of other acid-related conditions.

**L76.0** `Simple Sentence` (0.796) → `passthrough`
- original: Q: Can I take omeprazole in the morning and famotidine at night?

**L76.1** `Compound Sentence` (0.815) → `decomposed`
- original: A: Yes, you could take omeprazole in the morning and famotidine at night but there are not many studies investigating this approach.
  - S1: You could take omeprazole in the morning and famotidine at night.
  - S2: There are not many studies investigating this approach.

**L76.2** `Complex Sentence` (0.968) → `decomposed`
- original: Preliminary results suggest that taking your medication this way may provide superior control of gastric acid secretion at night without compromising the effectiveness of omeprazole in the morning.
  - S1: Preliminary results suggest that taking your medication this way may provide superior control of gastric acid secretion at night.
  - S2: This method does not compromise the effectiveness of omeprazole in the morning.

**L76.3** `Simple Sentence` (0.83) → `passthrough`
- original: More research is needed.
