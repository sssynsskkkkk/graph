# Ondansetron — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/ondansetron.txt` · 133 sentences · 15 changed by pronoun resolution · 260 sentences sent to EDC

## What is ondansetron?

**L5.0** `Simple Sentence` (0.943) → `passthrough`
- original: Ondansetron blocks the actions of chemicals in the body that can trigger nausea and vomiting.

**L6.0** `Complex Sentence` (0.464) → `decomposed`
- original: Ondansetron is used to prevent nausea and vomiting that may be caused by surgery, cancer chemotherapy, or radiation treatment.
  - S1: Ondansetron is used to prevent nausea and vomiting.
  - S2: Nausea and vomiting may be caused by surgery, cancer chemotherapy, or radiation treatment.

**L7.0** `Simple Sentence` (0.989) → `passthrough`
- original: Ondansetron may be used for purposes not listed in this medication guide.

## Warnings

**L10.0** `Simple Sentence` (0.983) → `passthrough`
- original: You should not use ondansetron if you are also using apomorphine (Apokyn).

**L11.0** `Complex Sentence` (0.735) → `decomposed`
- original: You should not use ondansetron if you are allergic to it or to similar medicines such as dolasetron (Anzemet), granisetron (Kytril), or palonosetron (Aloxi).
- pronoun resolved: You should not use ondansetron if you are allergic to ondansetron or to similar medicines such as dolasetron (Anzemet), granisetron (Kytril), or palonosetron (Aloxi).
  - edits: “it” → “ondansetron”
  - S1: You should not use ondansetron if you are allergic to ondansetron.
  - S2: You should not use ondansetron if you are allergic to similar medicines.
  - S3: Similar medicines include dolasetron (Anzemet), granisetron (Kytril), or palonosetron (Aloxi).

**L12.0** `Simple Sentence` (0.46) → `passthrough`
- original: Before taking ondansetron, tell your doctor if you have liver disease, or a personal or family history of Long QT syndrome.

**L13.0** `Simple Sentence` (0.991) → `passthrough`
- original: Ondansetron orally disintegrating tablets may contain phenylalanine.

**L13.1** `Incomplete Sentence` (0.863) → `excluded_incomplete`
- original: Tell your doctor if you have phenylketonuria (PKU).

**L14.0** `Complex Sentence` (0.647) → `decomposed`
- original: Serious side effects of ondansetron include blurred vision or temporary vision loss (lasting from only a few minutes to several hours), slow heart rate, trouble breathing, anxiety, agitation, shivering, feeling like you might pass out, and urinating less than usual or not at all.
  - S1: Serious side effects of ondansetron include blurred vision or temporary vision loss.
  - S2: The vision loss lasts from only a few minutes to several hours.
  - S3: Serious side effects of ondansetron include slow heart rate.
  - S4: Serious side effects of ondansetron include trouble breathing.
  - S5: Serious side effects of ondansetron include anxiety.
  - S6: Serious side effects of ondansetron include agitation.
  - S7: Serious side effects of ondansetron include shivering.
  - S8: Serious side effects of ondansetron include feeling like you might pass out.
  - S9: Serious side effects of ondansetron include urinating less than usual or not at all.

**L14.1** `Compound Sentence` (0.539) → `decomposed`
- original: Stop taking this medicine and call your doctor at once if you have any of these side effects.
- pronoun resolved: Stop taking ondansetron and call your doctor at once if you have any of these side effects.
  - edits: “this medicine” → “ondansetron”
  - S1: Stop taking ondansetron.
  - S2: Call your doctor at once if you have any of these side effects.

**L14.2** `Simple Sentence` (0.99) → `passthrough`
- original: Ondansetron may impair your thinking or reactions.

**L14.3** `Incomplete Sentence` (0.688) → `excluded_incomplete`
- original: Be careful if you drive or do anything that requires you to be alert.

## Before taking ondansetron

**L17.0** `Incomplete Sentence` (0.975) → `excluded_incomplete`
- original: You should not use ondansetron if:

**L18.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: you are also using apomorphine (Apokyn); or

**L19.0** `Simple Sentence` (0.978) → `passthrough`
- original: you are allergic to ondansetron or similar medicines (dolasetron, granisetron, palonosetron).

**L20.0** `Simple Sentence` (0.576) → `passthrough`
- original: To make sure ondansetron is safe for you, tell your doctor if you have:

**L21.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: liver disease;

**L22.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: an electrolyte imbalance (such as low levels of potassium or magnesium in your blood);

**L23.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: congestive heart failure, slow heartbeats;

**L24.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a personal or family history of long QT syndrome; or

**L25.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a blockage in your digestive tract (stomach or intestines).

**L26.0** `Simple Sentence` (0.991) → `passthrough`
- original: Ondansetron is not expected to harm an unborn baby.

**L26.1** `Incomplete Sentence` (0.964) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant.

**L27.0** `Complex Sentence` (0.456) → `decomposed`
- original: It is not known whether ondansetron passes into breast milk or if it could harm a nursing baby.
- pronoun resolved: It is not known whether ondansetron passes into breast milk or if ondansetron could harm a nursing baby.
  - edits: “it” → “ondansetron”
  - S1: It is not known whether ondansetron passes into breast milk.
  - S2: It is not known if ondansetron could harm a nursing baby.

**L27.1** `Incomplete Sentence` (0.945) → `excluded_incomplete`
- original: Tell your doctor if you are breast-feeding a baby.

**L28.0** `Simple Sentence` (0.987) → `passthrough`
- original: Ondansetron is not approved for use by anyone younger than 1 month old.

**L29.0** `Simple Sentence` (0.991) → `passthrough`
- original: Ondansetron orally disintegrating tablets may contain phenylalanine.

**L29.1** `Incomplete Sentence` (0.863) → `excluded_incomplete`
- original: Tell your doctor if you have phenylketonuria (PKU).

## How should I take ondansetron?

**L32.0** `Incomplete Sentence` (0.976) → `excluded_incomplete`
- original: Take ondansetron exactly as prescribed by your doctor.

**L32.1** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Follow all directions on your prescription label.

**L32.2** `Incomplete Sentence` (0.946) → `excluded_incomplete`
- original: Do not take this medicine in larger or smaller amounts or for longer than recommended.
- pronoun resolved: Do not take ondansetron in larger or smaller amounts or for longer than recommended.
  - edits: “this medicine” → “ondansetron”

**L33.0** `Simple Sentence` (0.99) → `passthrough`
- original: Ondansetron can be taken with or without food.

**L34.0** `Simple Sentence` (0.925) → `passthrough`
- original: The first dose is usually taken before the start of your surgery, chemotherapy, or radiation treatment.

**L34.1** `Incomplete Sentence` (0.925) → `excluded_incomplete`
- original: Follow your doctor's dosing instructions very carefully.

**L35.0** `Incomplete Sentence` (0.926) → `excluded_incomplete`
- original: Take the ondansetron regular tablet with a full glass of water.

**L36.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: To take the orally disintegrating tablet (Zofran ODT):

**L37.0** `Incomplete Sentence` (0.805) → `excluded_incomplete`
- original: Keep the tablet in its blister pack until you are ready to take it.

**L37.1** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Open the package and peel back the foil.

**L37.2** `Simple Sentence` (0.69) → `passthrough`
- original: Do not push a tablet through the foil or you may damage the tablet.

**L38.0** `Incomplete Sentence` (0.571) → `excluded_incomplete`
- original: Use dry hands to remove the tablet and place it in your mouth.

**L39.0** `Incomplete Sentence` (0.958) → `excluded_incomplete`
- original: Do not swallow the tablet whole.

**L39.1** `Incomplete Sentence` (0.945) → `excluded_incomplete`
- original: Allow it to dissolve in your mouth without chewing.

**L40.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Swallow several times as the tablet dissolves.

**L41.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: To use ondansetron oral soluble film (strip) (Zuplenz):

**L42.0** `Incomplete Sentence` (0.623) → `excluded_incomplete`
- original: Keep the strip in the foil pouch until you are ready to use the medicine.

**L43.0** `Simple Sentence` (0.637) → `passthrough`
- original: Using dry hands, remove the strip and place it on your tongue.
- pronoun resolved: Using dry hands, remove the strip and place strip on your tongue.
  - edits: “it” → “strip”

**L43.1** `Simple Sentence` (0.949) → `passthrough`
- original: It will begin to dissolve right away.
- pronoun resolved: Strip will begin to dissolve right away.
  - edits: “It” → “Strip”

**L44.0** `Incomplete Sentence` (0.976) → `excluded_incomplete`
- original: Do not swallow the strip whole.

**L44.1** `Incomplete Sentence` (0.969) → `excluded_incomplete`
- original: Allow it to dissolve in your mouth without chewing.
- pronoun resolved: Allow strip to dissolve in your mouth without chewing.
  - edits: “it” → “strip”

**L45.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Swallow several times after the strip dissolves.

**L45.1** `Simple Sentence` (0.955) → `passthrough`
- original: If desired, you may drink liquid to help swallow the dissolved strip.

**L46.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Wash your hands after using Zuplenz.

**L47.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Measure liquid medicine with the dosing syringe provided, or with a special dose-measuring spoon or medicine cup.

**L47.1** `Simple Sentence` (0.75) → `passthrough`
- original: If you do not have a dose-measuring device, ask your pharmacist for one.

**L48.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Store at room temperature away from moisture, heat, and light.

**L48.1** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Store liquid medicine in an upright position.

## What happens if I miss a dose?

**L51.0** `Incomplete Sentence` (0.926) → `excluded_incomplete`
- original: Take the missed dose as soon as you remember.

**L51.1** `Incomplete Sentence` (0.89) → `excluded_incomplete`
- original: Skip the missed dose if it is almost time for your next scheduled dose.

**L51.2** `Incomplete Sentence` (0.748) → `excluded_incomplete`
- original: Do not take extra medicine to make up the missed dose.

## What happens if I overdose?

**L54.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L55.0** `Compound Sentence` (0.45) → `decomposed`
- original: Overdose symptoms may include sudden loss of vision, severe constipation, feeling light-headed, or fainting.
  - S1: Overdose symptoms may include sudden loss of vision.
  - S2: Overdose symptoms may include severe constipation.
  - S3: Overdose symptoms may include feeling light-headed.
  - S4: Overdose symptoms may include fainting.

## What to avoid

**L58.0** `Simple Sentence` (0.99) → `passthrough`
- original: Ondansetron may impair your thinking or reactions.

**L58.1** `Incomplete Sentence` (0.688) → `excluded_incomplete`
- original: Be careful if you drive or do anything that requires you to be alert.

## Ondansetron side effects

**L61.0** `Compound Sentence` (0.504) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to ondansetron: rash, hives; fever, chills, difficult breathing; swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to ondansetron.
  - S2: These signs include a rash and hives.
  - S3: These signs also include fever and chills.
  - S4: These signs also include difficult breathing.
  - S5: These signs also include swelling of your face, lips, tongue, or throat.

**L62.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L63.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: severe constipation, stomach pain, or bloating;

**L64.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: sudden chest pain or chest tightness, severe dizziness, fainting, fast or pounding heartbeats;

**L65.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: fast or pounding heartbeats;

**L66.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: jaundice (yellowing of the skin or eyes);

**L67.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: blurred vision or temporary vision loss (lasting from only a few minutes to several hours);

**L68.0** `Incomplete Sentence` (0.969) → `excluded_incomplete`
- original: high levels of serotonin in the body--agitation, hallucinations, fever, fast heart rate, overactive reflexes, nausea, vomiting, diarrhea, loss of coordination, fainting.

**L69.0** `Simple Sentence` (0.959) → `passthrough`
- original: Common ondansetron side effects may include:

**L70.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: diarrhea or constipation;

**L71.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: headache;

**L72.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: drowsiness; or

**L73.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: tired feeling.

**L74.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L74.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L74.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## Dosing information

**L77.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Usual Adult Dose of Ondansetron for Nausea/Vomiting -- Chemotherapy Induced:

**L78.0** `Compound-Complex Sentence` (0.8) → `decomposed` · repaired
- original: Oral: Highly Emetogenic Cancer Chemotherapy (HEC): -Recommended dose: 24 mg orally 30 minutes before the start of single-day HEC (including cisplatin doses of 50 mg/m2 or greater) Moderately Emetogenic Cancer Chemotherapy (MEC): -Recommended dose: 8 mg orally twice a day, with the first dose administered 30 minutes before the start of chemotherapy and the subsequent dose 8 hours later; then 8 mg orally 2 times a day (every 12 hours) for 1 to 2 days after the completion of chemotherapy Parenteral: -Recommended dose: 0.15 mg/kg IV, with the first dose (infused over 15 minutes) 30 minutes before the start of emetogenic chemotherapy and subsequent doses given 4 and 8 hours after the first dose.
  - S1: Oral administration is recommended for Highly Emetogenic Cancer Chemotherapy (HEC).
  - S2: The recommended oral dose for HEC is 24 mg.
  - S3: This dose should be taken 30 minutes before the start of single-day HEC.
  - S4: This recommendation includes cisplatin doses of 50 mg/m2 or greater.
  - S5: Oral administration is recommended for Moderately Emetogenic Cancer Chemotherapy (MEC).
  - S6: The recommended oral dose for MEC is 8 mg.
  - S7: The first dose of 8 mg should be taken twice a day.
  - S8: The first dose is administered 30 minutes before the start of chemotherapy.
  - S9: The subsequent dose is administered 8 hours later.
  - S10: After the initial doses, 8 mg is taken orally 2 times a day.
  - S11: These subsequent doses are given every 12 hours.
  - S12: This regimen continues for 1 to 2 days after the completion of chemotherapy.
  - S13: Parenteral administration is recommended.
  - S14: The recommended parenteral dose is 0.15 mg/kg IV.
  - S15: The first dose is infused over 15 minutes.
  - S16: The first dose is given 30 minutes before the start of emetogenic chemotherapy.
  - S17: Subsequent doses are given 4 and 8 hours after the first dose.

**L78.1** `Compound Sentence` (0.479) → `decomposed`
- original: -Maximum dose: 16 mg per dose Comments: -Multi-day, single-dose administration of 24 mg orally for HEC has not been studied.
  - S1: The maximum dose is 16 mg per dose.
  - S2: Multi-day, single-dose administration of 24 mg orally for HEC has not been studied.

**L78.2** `Simple Sentence` (0.94) → `passthrough`
- original: -The injection formulation should be diluted prior to IV administration.

**L78.3** `Simple Sentence` (0.461) → `passthrough`
- original: Uses: -Prevention of nausea and vomiting associated with HEC or MEC -Prevention of nausea and vomiting associated with initial and repeat courses of emetogenic chemotherapy

**L79.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Usual Adult Dose of Ondansetron for Nausea/Vomiting:

**L80.0** `Compound-Complex Sentence` (0.8) → `decomposed` · repaired
- original: Oral: Highly Emetogenic Cancer Chemotherapy (HEC): -Recommended dose: 24 mg orally 30 minutes before the start of single-day HEC (including cisplatin doses of 50 mg/m2 or greater) Moderately Emetogenic Cancer Chemotherapy (MEC): -Recommended dose: 8 mg orally twice a day, with the first dose administered 30 minutes before the start of chemotherapy and the subsequent dose 8 hours later; then 8 mg orally 2 times a day (every 12 hours) for 1 to 2 days after the completion of chemotherapy Parenteral: -Recommended dose: 0.15 mg/kg IV, with the first dose (infused over 15 minutes) 30 minutes before the start of emetogenic chemotherapy and subsequent doses given 4 and 8 hours after the first dose.
  - S1: Oral administration is recommended for Highly Emetogenic Cancer Chemotherapy (HEC).
  - S2: The recommended oral dose for HEC is 24 mg.
  - S3: This dose should be taken 30 minutes before the start of single-day HEC.
  - S4: This recommendation includes cisplatin doses of 50 mg/m2 or greater.
  - S5: Oral administration is recommended for Moderately Emetogenic Cancer Chemotherapy (MEC).
  - S6: The recommended oral dose for MEC is 8 mg.
  - S7: The first dose of 8 mg should be taken twice a day.
  - S8: The first dose is administered 30 minutes before the start of chemotherapy.
  - S9: The subsequent dose is administered 8 hours later.
  - S10: After the initial doses, 8 mg is taken orally 2 times a day.
  - S11: These subsequent doses are given every 12 hours.
  - S12: This regimen continues for 1 to 2 days after the completion of chemotherapy.
  - S13: Parenteral administration is recommended.
  - S14: The recommended parenteral dose is 0.15 mg/kg IV.
  - S15: The first dose is infused over 15 minutes.
  - S16: The first dose is given 30 minutes before the start of emetogenic chemotherapy.
  - S17: Subsequent doses are given 4 and 8 hours after the first dose.

**L80.1** `Compound Sentence` (0.479) → `decomposed`
- original: -Maximum dose: 16 mg per dose Comments: -Multi-day, single-dose administration of 24 mg orally for HEC has not been studied.
  - S1: The maximum dose is 16 mg per dose.
  - S2: Multi-day, single-dose administration of 24 mg orally for HEC has not been studied.

**L80.2** `Simple Sentence` (0.94) → `passthrough`
- original: -The injection formulation should be diluted prior to IV administration.

**L80.3** `Simple Sentence` (0.461) → `passthrough`
- original: Uses: -Prevention of nausea and vomiting associated with HEC or MEC -Prevention of nausea and vomiting associated with initial and repeat courses of emetogenic chemotherapy

**L81.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Usual Adult Dose of Ondansetron for Nausea/Vomiting -- Postoperative:

**L82.0** `Compound-Complex Sentence` (0.577) → `decomposed`
- original: Oral: -Recommended dose: 16 mg orally 1 hour before the induction of anesthesia Parenteral: -Recommended dose: 4 mg IV (undiluted) immediately before induction of anesthesia or postoperatively (nausea and/or vomiting within 2 hours after surgery) -Alternative route: 4 mg IM (undiluted) Comment: -Administration of a second dose does not provide additional control of nausea and vomiting.
  - S1: The recommended oral dose is 16 mg.
  - S2: The oral dose should be taken 1 hour before the induction of anesthesia.
  - S3: The recommended parenteral dose is 4 mg IV.
  - S4: The IV dose should be undiluted.
  - S5: The IV dose should be given immediately before induction of anesthesia.
  - S6: The IV dose can also be given postoperatively.
  - S7: Postoperative administration is for nausea and/or vomiting within 2 hours after surgery.
  - S8: An alternative route is 4 mg IM.
  - S9: The IM dose should be undiluted.
  - S10: Administration of a second dose does not provide additional control of nausea and vomiting.

**L82.1** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Use: -Prevention of postoperative nausea and vomiting

**L83.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Usual Adult Dose for Nausea/Vomiting--Radiation Induced:

**L84.0** `Compound-Complex Sentence` (0.746) → `decomposed` · repaired
- original: Recommended dose: 8 mg orally 3 times a day -Total Body Irradiation: 8 mg orally 1 to 2 hours before each fraction of radiotherapy administered each day -Single High-dose Fraction Radiotherapy to the Abdomen: 8 mg orally 1 to 2 hours before radiotherapy, with subsequent doses every 8 hours after the first dose for 1 to 2 days after the completion of radiotherapy -Daily Fractionated Radiotherapy to the Abdomen: 8 mg orally 1 to 2 hours before radiotherapy, with subsequent doses every 8 hours after the first dose for each day radiotherapy is given Use: -Prevention of nausea and vomiting associated with radiotherapy, either as total body irradiation, single high-dose fraction, or daily fractions to the abdomen
  - S1: The recommended dose is 8 mg orally 3 times a day.
  - S2: For total body irradiation, the dose is 8 mg orally 1 to 2 hours before each fraction of radiotherapy administered each day.
  - S3: For single high-dose fraction radiotherapy to the abdomen, the dose is 8 mg orally 1 to 2 hours before radiotherapy.
  - S4: For single high-dose fraction radiotherapy to the abdomen, subsequent doses are 8 mg orally every 8 hours after the first dose for 1 to 2 days after the completion of radiotherapy.
  - S5: For daily fractionated radiotherapy to the abdomen, the dose is 8 mg orally 1 to 2 hours before radiotherapy.
  - S6: For daily fractionated radiotherapy to the abdomen, subsequent doses are 8 mg orally every 8 hours after the first dose for each day radiotherapy is given.
  - S7: The use of this medication is for the prevention of nausea and vomiting associated with radiotherapy.
  - S8: This prevention applies to total body irradiation.
  - S9: This prevention applies to single high-dose fraction radiotherapy.
  - S10: This prevention applies to daily fractions to the abdomen.

**L85.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Usual Pediatric Dose for Nausea/Vomiting -- Postoperative:

**L86.0** `Compound-Complex Sentence` (0.537) → `decomposed`
- original: Parenteral: 1 month to 12 years: Less than 40 kg: -Recommended dose: 0.1 mg/kg IV over 2 to 5 minutes immediately prior to/following anesthesia induction or postoperatively (nausea and/or vomiting occurring shortly after surgery) 40 kg and greater: -Recommended dose: 4 mg IV over 2 to 5 minutes immediately prior to/following anesthesia induction or postoperatively (nausea and/or vomiting occurring shortly after surgery) Use: -Prevention of postoperative nausea and vomiting
  - S1: Parenteral administration is recommended for patients aged 1 month to 12 years weighing less than 40 kg.
  - S2: The recommended dose for this group is 0.1 mg/kg IV over 2 to 5 minutes.
  - S3: This dose is administered immediately prior to or following anesthesia induction.
  - S4: This dose is also administered postoperatively if nausea and/or vomiting occur shortly after surgery.
  - S5: Parenteral administration is recommended for patients weighing 40 kg and greater.
  - S6: The recommended dose for this group is 4 mg IV over 2 to 5 minutes.
  - S7: This dose is administered immediately prior to or following anesthesia induction.
  - S8: This dose is also administered postoperatively if nausea and/or vomiting occur shortly after surgery.
  - S9: The use of this medication is for the prevention of postoperative nausea and vomiting.

**L87.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Usual Pediatric Dose for Nausea/Vomiting -- Chemotherapy Induced:

**L88.0** `Compound-Complex Sentence` (0.787) → `decomposed` · repaired
- original: Oral: 4 to 11 years: -Recommended dose: 4 mg orally 3 times a day, with the first dose administered 30 minutes before the start of chemotherapy, and subsequent doses 4 and 8 hours after the first dose; then 4 mg orally 3 times a day (every 8 hours) for 1 to 2 days after the completion of chemotherapy 12 years and older: -Recommended dose: 8 mg orally twice a day, with the first dose administered 30 minutes before the start of chemotherapy and the subsequent dose 8 hours later; then 8 mg orally 2 times a day (every 12 hours) for 1 to 2 days after the completion of chemotherapy Parenteral: 6 months to 18 years: -Recommended dose: 0.15 mg/kg IV, with the first dose (infused over 15 minutes) 30 minutes before the start of emetogenic chemotherapy, and subsequent doses given 4 and 8 hours after the first dose -Maximum dose: 16 mg (per dose) Comments: -The injection formulation should be diluted in 50 mL prior to IV administration.
  - S1: The recommended oral dose for children aged 4 to 11 years is 4 mg taken three times a day.
  - S2: The first oral dose for this age group is administered 30 minutes before the start of chemotherapy.
  - S3: Subsequent oral doses for this age group are given 4 and 8 hours after the first dose.
  - S4: After the initial doses, the oral regimen continues as 4 mg three times a day every 8 hours.
  - S5: This continued oral dosing lasts for 1 to 2 days after the completion of chemotherapy.
  - S6: The recommended oral dose for individuals 12 years and older is 8 mg taken twice a day.
  - S7: The first oral dose for this age group is administered 30 minutes before the start of chemotherapy.
  - S8: The subsequent oral dose for this age group is given 8 hours later.
  - S9: After the initial doses, the oral regimen continues as 8 mg twice a day every 12 hours.
  - S10: This continued oral dosing lasts for 1 to 2 days after the completion of chemotherapy.
  - S11: The recommended parenteral dose for children aged 6 months to 18 years is 0.15 mg/kg given intravenously.
  - S12: The first parenteral dose is infused over 15 minutes.
  - S13: The first parenteral dose is administered 30 minutes before the start of emetogenic chemotherapy.
  - S14: Subsequent parenteral doses are given 4 and 8 hours after the first dose.
  - S15: The maximum parenteral dose per administration is 16 mg.
  - S16: The injection formulation should be diluted in 50 mL prior to intravenous administration.

**L88.1** `Simple Sentence` (0.845) → `passthrough`
- original: -This drug should be used to prevent nausea and vomiting associated with moderately to highly emetogenic chemotherapy.
- pronoun resolved: -Ondansetron should be used to prevent nausea and vomiting associated with moderately to highly emetogenic chemotherapy.
  - edits: “-This drug” → “-Ondansetron”

**L88.2** `Simple Sentence` (0.543) → `passthrough`
- original: Uses: -Prevention of nausea and vomiting associated with moderately emetogenic cancer chemotherapy -Prevention of nausea and vomiting associated with initial and repeat courses of emetogenic chemotherapy

## What other drugs will affect ondansetron?

**L91.0** `Complex Sentence` (0.938) → `decomposed`
- original: Ondansetron can cause a serious heart problem, especially if you use certain medicines at the same time, including antibiotics, antidepressants, heart rhythm medicine, antipsychotic medicines, and medicines to treat cancer, malaria, HIV or AIDS.
  - S1: Ondansetron can cause a serious heart problem.
  - S2: This risk is especially high if you use certain medicines at the same time.
  - S3: These medicines include antibiotics, antidepressants, heart rhythm medicine, antipsychotic medicines, and medicines to treat cancer, malaria, HIV or AIDS.

**L91.1** `Incomplete Sentence` (0.799) → `excluded_incomplete`
- original: Tell your doctor about all medicines you use, and those you start or stop using during your treatment with ondansetron.

**L92.0** `Complex Sentence` (0.913) → `decomposed`
- original: Taking ondansetron while you are using certain other medicines can cause high levels of serotonin to build up in your body, a condition called "serotonin syndrome," which can be fatal.
  - S1: Taking ondansetron while using certain other medicines can cause high levels of serotonin to build up in your body.
  - S2: This condition is called "serotonin syndrome."
  - S3: Serotonin syndrome can be fatal.

**L92.1** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Tell your doctor if you also use:

**L93.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: medicine to treat depression;

**L94.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: medicine to treat a psychiatric disorder;

**L95.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a narcotic (opioid) medication; or

**L96.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: medicine to prevent nausea and vomiting.

**L97.0** `Simple Sentence` (0.928) → `passthrough`
- original: This list is not complete and many other drugs can interact with ondansetron.

**L97.1** `Incomplete Sentence` (0.491) → `excluded_incomplete`
- original: This includes prescription and over-the-counter medicines, vitamins, and herbal products.
- pronoun resolved: List includes prescription and over-the-counter medicines, vitamins, and herbal products.
  - edits: “This” → “List”

**L97.2** `Incomplete Sentence` (0.956) → `excluded_incomplete`
- original: Give a list of all your medicines to any healthcare provider who treats you.

## Popular FAQ

**L100.0** `Incomplete Sentence` (0.853) → `excluded_incomplete`
- original: Q: How long before a meal should you take ondansetron?

**L100.1** `Compound-Complex Sentence` (0.779) → `decomposed`
- original: A: If you are taking ondansetron for nausea that occurs with meals, then the standard tablet should be taken half an hour to 1 hour before meals, and the orally disintegrating tablet or oral soluble film can be taken 15 minutes before meals.
  - S1: You are taking ondansetron for nausea that occurs with meals.
  - S2: The standard tablet should be taken half an hour to 1 hour before meals.
  - S3: The orally disintegrating tablet can be taken 15 minutes before meals.
  - S4: The oral soluble film can be taken 15 minutes before meals.

**L100.2** `Complex Sentence` (0.9) → `decomposed`
- original: However, if you are taking ondansetron for constant, all day nausea then it should be taken at regular intervals during the day as prescribed, with or without food.
- pronoun resolved: However, if you are taking ondansetron for constant, all day nausea then ondansetron should be taken at regular intervals during the day as prescribed, with or without food.
  - edits: “it” → “ondansetron”
  - S1: However, if you are taking ondansetron for constant, all day nausea.
  - S2: Then ondansetron should be taken at regular intervals during the day as prescribed.
  - S3: It should be taken with or without food.

**L101.0** `Incomplete Sentence` (0.723) → `excluded_incomplete`
- original: Q: How often can you take ondansetron?

**L101.1** `Compound-Complex Sentence` (0.591) → `decomposed`
- original: A: You can take ondansetron more frequently initially, for example, if you are taking it to prevent or treat nausea of vomiting from chemotherapy you can take 4mg then follow up with another 4mg dose at 4 and 8 hours after the first dose.
- pronoun resolved: A: You can take ondansetron more frequently initially, for example, if you are taking ondansetron to prevent or treat nausea of vomiting from chemotherapy you can take 4mg then follow up with another 4mg dose at 4 and 8 hours after the first dose.
  - edits: “it” → “ondansetron”
  - S1: You can take ondansetron more frequently initially.
  - S2: You can take ondansetron to prevent or treat nausea or vomiting from chemotherapy.
  - S3: You can take 4mg of ondansetron.
  - S4: You can take another 4mg dose at 4 hours after the first dose.
  - S5: You can take another 4mg dose at 8 hours after the first dose.

**L101.2** `Simple Sentence` (0.955) → `passthrough`
- original: The following day you should only take it every 8 hours (3 times a day).
- pronoun resolved: The following day you should only take ondansetron every 8 hours (3 times a day).
  - edits: “it” → “ondansetron”

**L101.3** `Complex Sentence` (0.661) → `decomposed`
- original: If you continue taking ondansetron more frequently than this you are at higher risk of side effects such as constipation, headache, or heart effects.
  - S1: You are at higher risk of side effects if you continue taking ondansetron more frequently than this.
  - S2: The side effects include constipation, headache, or heart effects.

**L102.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Q: Chemo side effects: What should I expect and how to cope?

**L102.1** `Simple Sentence` (0.964) → `passthrough`
- original: A: Chemotherapy is a drug treatment used to kill fast-growing cancer cells in your body.

**L102.2** `Complex Sentence` (0.96) → `decomposed`
- original: While chemotherapy is an effective treatment for many types of cancer, it can also damage healthy cells that divide quickly, such as those in your hair follicles, digestive tract, and bone marrow.
- pronoun resolved: While chemotherapy is an effective treatment for many types of cancer, chemotherapy can also damage healthy cells that divide quickly, such as those in your hair follicles, digestive tract, and bone marrow.
  - edits: “it” → “chemotherapy”
  - S1: Chemotherapy is an effective treatment for many types of cancer.
  - S2: Chemotherapy can also damage healthy cells that divide quickly.
  - S3: Examples of these cells include those in your hair follicles, digestive tract, and bone marrow.

**L102.3** `Complex Sentence` (0.416) → `decomposed`
- original: This widespread effect on healthy tissue is what causes the various side effects associated with chemotherapy treatment.
  - S1: This widespread effect on healthy tissue causes the various side effects.
  - S2: These side effects are associated with chemotherapy treatment.

**L103.0** `Simple Sentence` (0.526) → `passthrough`
- original: Q: Can you take ondansetron while pregnant?

**L103.1** `Compound-Complex Sentence` (0.827) → `decomposed`
- original: A: Although ondansetron is not specifically approved by the FDA to treat nausea and vomiting during pregnancy (NVP), its use is common, and approximately 25% of pregnant women are prescribed ondansetron to treat NVP.
  - S1: Ondansetron is not specifically approved by the FDA to treat nausea and vomiting during pregnancy.
  - S2: The use of ondansetron to treat nausea and vomiting during pregnancy is common.
  - S3: Approximately 25% of pregnant women are prescribed ondansetron to treat nausea and vomiting during pregnancy.

**L103.2** `Complex Sentence` (0.939) → `decomposed`
- original: Overall, studies show the use of ondansetron appears to be associated with an additional 3 instances of oral cleft defects (such as cleft lip or cleft palate) for every 10,000 women exposed to ondansetron during their first trimester.
  - S1: Overall, studies show the use of ondansetron appears to be associated with an additional 3 instances of oral cleft defects.
  - S2: These defects include cleft lip or cleft palate.
  - S3: This association occurs for every 10,000 women exposed to ondansetron during their first trimester.

**L103.3** `Compound Sentence` (0.55) → `decomposed`
- original: There may also be a very slight increased risk of a type of heart defect called a ventricular septal defect, but no apparent increased risk of other birth defects, miscarriage, or fetal death.
  - S1: There may also be a very slight increased risk of a type of heart defect called a ventricular septal defect.
  - S2: There is no apparent increased risk of other birth defects.
  - S3: There is no apparent increased risk of miscarriage.
  - S4: There is no apparent increased risk of fetal death.

**L104.0** `Incomplete Sentence` (0.972) → `excluded_incomplete`
- original: Q: How long does ondansetron take to work?

**L104.1** `Compound Sentence` (0.937) → `decomposed`
- original: A: Oral ondansetron usually starts to work within 30 minutes, though it may take up to two hours to reach full effect.
- pronoun resolved: A: Oral ondansetron usually starts to work within 30 minutes, though Oral ondansetron may take up to two hours to reach full effect.
  - edits: “it” → “Oral ondansetron”
  - S1: Oral ondansetron usually starts to work within 30 minutes.
  - S2: Oral ondansetron may take up to two hours to reach full effect.

**L104.2** `Simple Sentence` (0.772) → `passthrough`
- original: Typical timing is: 30 minutes before chemotherapy, 1 hour before surgery, 1 to 2 hours before radiation therapy.

**L105.0** `Incomplete Sentence` (0.789) → `excluded_incomplete`
- original: Q: Does ondansetron make you sleepy?

**L105.1** `Simple Sentence` (0.964) → `passthrough`
- original: A: Yes, ondansetron (Zofran) might make you feel sleepy or tired.

**L105.2** `Complex Sentence` (0.909) → `decomposed`
- original: Ondansetron injection for the treatment of post-operative nausea and vomiting has been reported to cause drowsiness or sedation in 8% of patients vs. 7% of those using a placebo (an inactive treatment).
  - S1: Ondansetron injection has been reported to cause drowsiness or sedation in 8% of patients.
  - S2: Ondansetron injection is used for the treatment of post-operative nausea and vomiting.
  - S3: 7% of those using a placebo experienced drowsiness or sedation.
  - S4: A placebo is an inactive treatment.

**L105.3** `Complex Sentence` (0.888) → `decomposed`
- original: Malaise (generally feeling unwell) and fatigue (tiredness or lack of energy) have also been reported in 13% of patients (vs. 2% placebo) when it is used orally for the prevention of chemotherapy-induced nausea and vomiting.
- pronoun resolved: Malaise (generally feeling unwell) and fatigue (tiredness or lack of energy) have also been reported in 13% of patients (vs. 2% placebo) when Ondansetron is used orally for the prevention of chemotherapy-induced nausea and vomiting.
  - edits: “it” → “Ondansetron”
  - S1: Malaise and fatigue have also been reported in 13% of patients.
  - S2: Malaise is generally feeling unwell.
  - S3: Fatigue is tiredness or lack of energy.
  - S4: This occurred when Ondansetron was used orally for the prevention of chemotherapy-induced nausea and vomiting.
  - S5: The rate was 2% for the placebo group.
