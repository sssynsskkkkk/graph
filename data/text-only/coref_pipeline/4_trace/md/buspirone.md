# Buspirone — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/buspirone.txt` · 71 sentences · 5 changed by pronoun resolution · 97 sentences sent to EDC

## What is buspirone?

**L5.0** `Complex Sentence` (0.802) → `decomposed`
- original: Buspirone is an anti-anxiety medicine that affects chemicals in the brain that may be unbalanced in people with anxiety.
  - S1: Buspirone is an anti-anxiety medicine.
  - S2: Buspirone affects chemicals in the brain.
  - S3: These chemicals may be unbalanced in people with anxiety.

**L6.0** `Complex Sentence` (0.592) → `decomposed`
- original: Buspirone is used to treat symptoms of anxiety, such as fear, tension, irritability, dizziness, pounding heartbeat, and other physical symptoms.
  - S1: Buspirone is used to treat symptoms of anxiety.
  - S2: These symptoms include fear, tension, and irritability.
  - S3: These symptoms also include dizziness and pounding heartbeat.
  - S4: Other physical symptoms are also treated.

**L7.0** `Compound Sentence` (0.877) → `decomposed`
- original: Buspirone is not an anti-psychotic medication and should not be used in place of medication prescribed by your doctor for psychotic disorders.
  - S1: Buspirone is not an anti-psychotic medication.
  - S2: It should not be used in place of medication prescribed by your doctor for psychotic disorders.

## Warnings

**L10.0** `Simple Sentence` (0.721) → `passthrough`
- original: Do not use buspirone if you have taken an MAO inhibitor in the past 14 days.

**L10.1** `Simple Sentence` (0.94) → `passthrough`
- original: A dangerous drug interaction could occur.

**L10.2** `Simple Sentence` (0.882) → `passthrough`
- original: MAO inhibitors include isocarboxazid, linezolid, methylene blue injection, phenelzine, rasagiline, selegiline, and tranylcypromine.

## Before taking this medicine

**L13.0** `Simple Sentence` (0.988) → `passthrough`
- original: You should not use buspirone if you are allergic to it.
- pronoun resolved: You should not use buspirone if you are allergic to buspirone.
  - edits: “it.” → “buspirone.”

**L14.0** `Simple Sentence` (0.721) → `passthrough`
- original: Do not use buspirone if you have taken an MAO inhibitor in the past 14 days.

**L14.1** `Simple Sentence` (0.94) → `passthrough`
- original: A dangerous drug interaction could occur.

**L14.2** `Simple Sentence` (0.882) → `passthrough`
- original: MAO inhibitors include isocarboxazid, linezolid, methylene blue injection, phenelzine, rasagiline, selegiline, and tranylcypromine.

**L15.0** `Simple Sentence` (0.858) → `passthrough`
- original: To make sure this medicine is safe for you, tell your doctor if you have any of these conditions:

**L16.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: kidney disease; or

**L17.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: liver disease.

**L18.0** `Incomplete Sentence` (0.915) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or plan to become pregnant.

**L18.1** `Simple Sentence` (0.988) → `passthrough`
- original: This medicine should be used during pregnancy only if clearly needed.

**L19.0** `Simple Sentence` (0.99) → `passthrough`
- original: It is not known whether buspirone passes into breast milk.

**L19.1** `Simple Sentence` (0.986) → `passthrough`
- original: You should avoid breast-feeding while using this medicine.

**L20.0** `Compound Sentence` (0.942) → `decomposed`
- original: Buspirone is not FDA-approved for use by anyone younger than 18 years old, but this medicine has been used in children and adolescents under close medical supervision and at the appropriate dosage.
  - S1: Buspirone is not FDA-approved for use by anyone younger than 18 years old.
  - S2: This medicine has been used in children and adolescents under close medical supervision and at the appropriate dosage.

## How should I take buspirone?

**L23.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Take buspirone exactly as it was prescribed for you.
- pronoun resolved: Take buspirone exactly as buspirone was prescribed for you.
  - edits: “it” → “buspirone”

**L23.1** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Follow all directions on your prescription label.

**L23.2** `Simple Sentence` (0.957) → `passthrough`
- original: Your doctor may occasionally change your dose to make sure you get the best results.

**L23.3** `Incomplete Sentence` (0.903) → `excluded_incomplete`
- original: Do not take this medicine in larger or smaller amounts or for longer than recommended.

**L24.0** `Simple Sentence` (0.892) → `passthrough`
- original: You may take buspirone with or without food but take it the same way each time.
- pronoun resolved: You may take buspirone with or without food but take buspirone the same way each time.
  - edits: “it” → “buspirone”

**L25.0** `Complex Sentence` (0.816) → `decomposed`
- original: Some buspirone tablets are scored so you can break the tablet into 2 or 3 pieces in order to take a smaller amount of the medicine at each dose.
  - S1: Some buspirone tablets are scored.
  - S2: You can break the tablet into 2 or 3 pieces.
  - S3: This allows you to take a smaller amount of the medicine at each dose.

**L25.1** `Simple Sentence` (0.451) → `passthrough`
- original: Do not use a tablet if it has not been broken correctly and the piece is too big or too small.

**L25.2** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Follow your doctor's instructions about how much of the tablet to take.

**L26.0** `Complex Sentence` (0.801) → `decomposed`
- original: If you have difficulty swallowing capsules, you may open the capsule and sprinkle the medicine into a small amount (about 1 to 2 tablespoons) of applesauce.
  - S1: If you have difficulty swallowing capsules, you may open the capsule.
  - S2: You may sprinkle the medicine into a small amount of applesauce.
  - S3: The small amount of applesauce should be about 1 to 2 tablespoons.

**L26.1** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Swallow the mixture right away without chewing.

**L27.0** `Complex Sentence` (0.939) → `decomposed`
- original: If you have switched to buspirone from another anxiety medication, you may need to slowly decrease your dose of the other medication rather than stopping suddenly.
  - S1: You may need to slowly decrease your dose of the other medication.
  - S2: You should not stop the other medication suddenly.
  - S3: This applies if you have switched to buspirone from another anxiety medication.

**L27.1** `Simple Sentence` (0.815) → `passthrough`
- original: Some anxiety medications can cause withdrawal symptoms when you stop taking them suddenly after long-term use.

**L28.0** `Simple Sentence` (0.99) → `passthrough`
- original: This medication can cause false positive results with certain medical tests.

**L28.1** `Simple Sentence` (0.962) → `passthrough`
- original: You may need to stop using the medicine for at least 48 hours before your test.

**L28.2** `Incomplete Sentence` (0.909) → `excluded_incomplete`
- original: Tell any doctor who treats you that you are using buspirone.

**L29.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Store at room temperature away from moisture, heat, and light.

## What happens if I miss a dose?

**L32.0** `Incomplete Sentence` (0.926) → `excluded_incomplete`
- original: Take the missed dose as soon as you remember.

**L32.1** `Incomplete Sentence` (0.89) → `excluded_incomplete`
- original: Skip the missed dose if it is almost time for your next scheduled dose.

**L32.2** `Incomplete Sentence` (0.748) → `excluded_incomplete`
- original: Do not take extra medicine to make up the missed dose.

## What happens if I overdose?

**L35.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

## What should I avoid?

**L38.0** `Simple Sentence` (0.989) → `passthrough`
- original: This medication may impair your thinking or reactions.
- pronoun resolved: Buspirone may impair your thinking or reactions.
  - edits: “This medication” → “Buspirone”

**L38.1** `Incomplete Sentence` (0.688) → `excluded_incomplete`
- original: Be careful if you drive or do anything that requires you to be alert.

**L39.0** `Simple Sentence` (0.991) → `passthrough`
- original: Drinking alcohol may increase certain side effects of buspirone.

**L40.0** `Simple Sentence` (0.984) → `passthrough`
- original: Grapefruit and grapefruit juice may interact with buspirone and lead to unwanted side effects.

**L40.1** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: Discuss the use of grapefruit products with your doctor.

## Buspirone side effects

**L43.0** `Compound Sentence` (0.415) → `decomposed`
- original: Get emergency medical help if you have any signs of an allergic reaction to buspirone: hives; difficult breathing; swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have any signs of an allergic reaction to buspirone.
  - S2: Signs of an allergic reaction to buspirone include hives.
  - S3: Signs of an allergic reaction to buspirone include difficult breathing.
  - S4: Signs of an allergic reaction to buspirone include swelling of your face, lips, tongue, or throat.

**L44.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L45.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: chest pain;

**L46.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: shortness of breath; or

**L47.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: a light-headed feeling, like you might pass out.

**L48.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: signs of serotonin syndrome, such as agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness, twitching, loss of coordination, nausea, vomiting, or diarrhea.

**L49.0** `Simple Sentence` (0.879) → `passthrough`
- original: Common buspirone side effects may include:

**L50.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: headache;

**L51.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: dizziness, drowsiness;

**L52.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: sleep problems (insomnia);

**L53.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: nausea, upset stomach; or

**L54.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: feeling nervous or excited.

**L55.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L55.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L55.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## Dosing information

**L58.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Anxiety:

**L59.0** `Incomplete Sentence` (0.843) → `excluded_incomplete`
- original: Initial dose: 7.5 mg orally two times a day or 5 mg 3 times a day.

**L59.1** `Compound Sentence` (0.524) → `decomposed`
- original: Maintenance dose: The daily dose may be increased in 5 mg increments every 2 to 3 days up to 20 to 60 mg/day in divided doses.
  - S1: The daily dose may be increased in 5 mg increments every 2 to 3 days.
  - S2: The daily dose may be increased up to 20 to 60 mg/day.
  - S3: The daily dose is given in divided doses.

**L59.2** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Maximum dose: 60 mg per day

## What other drugs will affect buspirone?

**L62.0** `Simple Sentence` (0.915) → `passthrough`
- original: Taking this medicine with other drugs that make you sleepy or slow your breathing can worsen these effects.
- pronoun resolved: Taking buspirone with other drugs that make you sleepy or slow your breathing can worsen these effects.
  - edits: “this medicine” → “buspirone”

**L62.1** `Simple Sentence` (0.469) → `passthrough`
- original: Ask your doctor before taking buspirone with a sleeping pill, narcotic pain medicine, muscle relaxer, or medicine for anxiety, depression, or seizures.

**L63.0** `Complex Sentence` (0.634) → `decomposed`
- original: Other drugs may interact with buspirone, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may interact with buspirone.
  - S2: These include prescription medicines.
  - S3: These include over-the-counter medicines.
  - S4: These include vitamins.
  - S5: These include herbal products.

**L63.1** `Incomplete Sentence` (0.762) → `excluded_incomplete`
- original: Tell each of your health care providers about all medicines you use now and any medicine you start or stop using.

## Popular FAQ

**L66.0** `Incomplete Sentence` (0.934) → `excluded_incomplete`
- original: Q: How long does it take for buspirone to work?

**L66.1** `Complex Sentence` (0.69) → `decomposed`
- original: A: Buspirone, commonly prescribed for anxiety, is not a fast-acting medication and typically takes 2 to 4 weeks of regular use before most people experience noticeable improvement in symptoms.
  - S1: Buspirone is not a fast-acting medication.
  - S2: Buspirone is commonly prescribed for anxiety.
  - S3: It typically takes 2 to 4 weeks of regular use before most people experience noticeable improvement in symptoms.

**L67.0** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Q: What drugs cause pinpoint pupils?

**L67.1** `Complex Sentence` (0.863) → `decomposed`
- original: A: Pinpoint pupils, medically termed miosis, refer to abnormally small, constricted pupils that do not dilate appropriately in low light.
  - S1: Pinpoint pupils refer to abnormally small, constricted pupils.
  - S2: Pinpoint pupils are medically termed miosis.
  - S3: These pupils do not dilate appropriately in low light.

**L67.2** `Simple Sentence` (0.908) → `passthrough`
- original: This symptom can be caused by opioids, clonidine, buspirone, metoclopramide, and other medications.
