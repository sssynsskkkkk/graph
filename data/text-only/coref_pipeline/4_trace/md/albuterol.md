# Albuterol Inhalation — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/albuterol.txt` · 110 sentences · 12 changed by pronoun resolution · 152 sentences sent to EDC

## What is albuterol inhalation?

**L5.0** `Complex Sentence` (0.507) → `decomposed`
- original: Albuterol is a bronchodilator that relaxes muscles in the airways and increases air flow to the lungs.
  - S1: Albuterol is a bronchodilator.
  - S2: Albuterol relaxes muscles in the airways.
  - S3: Albuterol increases air flow to the lungs.

**L6.0** `Complex Sentence` (0.887) → `decomposed`
- original: Albuterol inhalation is used to treat or prevent bronchospasm, or narrowing of the airways in the lungs, in people with asthma or certain types of chronic obstructive pulmonary disease (COPD).
  - S1: Albuterol inhalation is used to treat or prevent bronchospasm.
  - S2: Bronchospasm is the narrowing of the airways in the lungs.
  - S3: Albuterol inhalation is used in people with asthma.
  - S4: Albuterol inhalation is used in people with certain types of chronic obstructive pulmonary disease (COPD).

**L6.1** `Simple Sentence` (0.977) → `passthrough`
- original: It is also used to prevent exercise-induced bronchospasm.
- pronoun resolved: Albuterol is also used to prevent exercise-induced bronchospasm.
  - edits: “It” → “Albuterol”

**L7.0** `Simple Sentence` (0.98) → `passthrough`
- original: Albuterol inhalation is for use in adults and children who are at least 2 years old.

**L7.1** `Incomplete Sentence` (0.929) → `excluded_incomplete`
- original: Always follow your doctor's directions when giving albuterol to a child.

## Warnings

**L10.0** `Simple Sentence` (0.981) → `passthrough`
- original: It is important to keep albuterol on hand at all times.

**L10.1** `Incomplete Sentence` (0.913) → `excluded_incomplete`
- original: Get your prescription refilled before you run out of medicine completely.

**L10.2** `Incomplete Sentence` (0.905) → `excluded_incomplete`
- original: Keep using all of your other medications as prescribed by your doctor.

**L11.0** `Incomplete Sentence` (0.929) → `excluded_incomplete`
- original: Talk with your doctor if any of your asthma medications do not seem to work as well in treating or preventing attacks.

**L11.1** `Simple Sentence` (0.368) → `passthrough`
- original: If it seems like you need to use more of any of your medications in a 24-hour period, talk with your doctor.
- pronoun resolved: If albuterol seems like you need to use more of any of your medications in a 24-hour period, talk with your doctor.
  - edits: “it” → “albuterol”

**L11.2** `Simple Sentence` (0.981) → `passthrough`
- original: An increased need for medication could be an early sign of a serious asthma attack.

**L12.0** `Incomplete Sentence` (0.966) → `excluded_incomplete`
- original: Only use albuterol as prescribed by your physician.

**L12.1** `Simple Sentence` (0.99) → `passthrough`
- original: An overdose of albuterol can be fatal.

**L12.2** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

## Before taking this medicine

**L15.0** `Simple Sentence` (0.989) → `passthrough`
- original: You should not use this medicine if you are allergic to albuterol.
- pronoun resolved: You should not use Albuterol if you are allergic to albuterol.
  - edits: “this medicine” → “Albuterol”

**L15.1** `Simple Sentence` (0.974) → `passthrough`
- original: You should not use ProAir RespiClick or ProAir Digihaler if you are allergic to milk proteins.

**L16.0** `Simple Sentence` (0.758) → `passthrough`
- original: To make sure albuterol inhalation is safe for you, tell your doctor if you have:

**L17.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: heart disease, high blood pressure, congestive heart failure;

**L18.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a heart rhythm disorder;

**L19.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a seizure disorder such as epilepsy;

**L20.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: diabetes;

**L21.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: overactive thyroid; or

**L22.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: low levels of potassium in your blood.

**L23.0** `Incomplete Sentence` (0.915) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or plan to become pregnant.

**L23.1** `Simple Sentence` (0.983) → `passthrough`
- original: It is not known whether albuterol will harm an unborn baby.

**L23.2** `Complex Sentence` (0.894) → `decomposed`
- original: However, having uncontrolled asthma during pregnancy may increase the risk of premature birth, low birth weight, or eclampsia (dangerously high blood pressure that can lead to medical problems in both mother and baby).
  - S1: However, having uncontrolled asthma during pregnancy may increase the risk of premature birth.
  - S2: It may also increase the risk of low birth weight.
  - S3: It may also increase the risk of eclampsia.
  - S4: Eclampsia is dangerously high blood pressure.
  - S5: Eclampsia can lead to medical problems in both mother and baby.

**L23.3** `Simple Sentence` (0.796) → `passthrough`
- original: The benefit of preventing bronchospasm may outweigh any risks to the baby.

**L24.0** `Complex Sentence` (0.774) → `decomposed`
- original: If you are pregnant, your name may be listed on a pregnancy registry to track the effects of albuterol on the baby.
  - S1: If you are pregnant, your name may be listed on a pregnancy registry.
  - S2: The registry is used to track the effects of albuterol on the baby.

**L25.0** `Simple Sentence` (0.986) → `passthrough`
- original: It may not be safe to breastfeed while using this medicine.
- pronoun resolved: Pregnancy registry may not be safe to breastfeed while using this medicine.
  - edits: “It” → “Pregnancy registry”

**L25.1** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Ask your doctor about any risk.

## How should I use albuterol inhalation?

**L28.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: Use albuterol inhalation exactly as prescribed by your doctor.

**L28.1** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Follow all directions on your prescription label.

**L28.2** `Incomplete Sentence` (0.888) → `excluded_incomplete`
- original: Do not use albuterol inhalation in larger or smaller amounts or for longer than recommended.

**L29.0** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Read all patient information, medication guides, and instruction sheets provided to you.

**L29.1** `Incomplete Sentence` (0.897) → `excluded_incomplete`
- original: Ask your doctor or pharmacist if you have any questions.

**L30.0** `Simple Sentence` (0.955) → `passthrough`
- original: You may need to prime your albuterol inhaler device before the first use.

**L30.1** `Simple Sentence` (0.97) → `passthrough`
- original: Your medicine comes with directions for priming if needed.

**L30.2** `Simple Sentence` (0.978) → `passthrough`
- original: You may also need to shake your albuterol device just before each use.

**L31.0** `Simple Sentence` (0.975) → `passthrough`
- original: Keeping your inhaler clean is important to ensure you are receiving the medication.

**L31.1** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Clean the plastic actuator with the canister removed at least once a week.

**L31.2** `Simple Sentence` (0.973) → `passthrough`
- original: Your medicine comes with directions for properly cleaning your device.

**L32.0** `Incomplete Sentence` (0.969) → `excluded_incomplete`
- original: Follow all medication instructions very carefully.

**L33.0** `Incomplete Sentence` (0.543) → `excluded_incomplete`
- original: Do not allow a young child to use albuterol inhalation without help from an adult.

**L34.0** `Simple Sentence` (0.98) → `passthrough`
- original: The usual dose of albuterol inhalation is 2 inhalations every 4 to 6 hours.

**L34.1** `Simple Sentence` (0.831) → `passthrough`
- original: To prevent exercise-induced bronchospasm, use 2 inhalations 15 to 30 minutes before you exercise.

**L34.2** `Simple Sentence` (0.953) → `passthrough`
- original: The effects of albuterol inhalation should last about 4 to 6 hours.

**L35.0** `Incomplete Sentence` (0.941) → `excluded_incomplete`
- original: Seek medical attention if you think your asthma medications are not working as well.

**L35.1** `Simple Sentence` (0.981) → `passthrough`
- original: An increased need for medication could be an early sign of a serious asthma attack.

**L36.0** `Compound Sentence` (0.665) → `decomposed`
- original: Use the dose counter on your albuterol inhaler device and get your prescription refilled before you run out of medicine completely.
  - S1: Use the dose counter on your albuterol inhaler device.
  - S2: Get your prescription refilled before you run out of medicine completely.

**L36.1** `Incomplete Sentence` (0.884) → `excluded_incomplete`
- original: Always use the new inhaler device provided with your refill.

**L36.2** `Incomplete Sentence` (0.77) → `excluded_incomplete`
- original: Do not float a medicine canister in water to see if it is empty.
- pronoun resolved: Do not float a medicine canister in water to see if medicine canister is empty.
  - edits: “it” → “medicine canister”

**L37.0** `Simple Sentence` (0.975) → `passthrough`
- original: ProAir HFA, Proventil HFA, or Ventolin HFA must be shaken before each use.

**L37.1** `Simple Sentence` (0.936) → `passthrough`
- original: You do not need to shake ProAir RespiClick before using.

**L38.0** `Incomplete Sentence` (0.957) → `excluded_incomplete`
- original: Follow all product instructions on how to clean your albuterol inhaler device and mouthpiece.

**L38.1** `Simple Sentence` (0.508) → `passthrough`
- original: Do not wash or put any part of the ProAir RespiClick inhaler device in water.

**L38.2** `Incomplete Sentence` (0.973) → `excluded_incomplete`
- original: Replace your inhaler if it is washed or placed in water.

**L38.3** `Simple Sentence` (0.561) → `passthrough`
- original: If the mouthpiece needs cleaning, gently wipe it with a dry cloth or tissue.
- pronoun resolved: If the mouthpiece needs cleaning, gently wipe mouthpiece with a dry cloth or tissue.
  - edits: “it” → “mouthpiece”

**L38.4** `Incomplete Sentence` (0.961) → `excluded_incomplete`
- original: Do not use a spacer or volume holding chamber with ProAir RespiClick.

**L39.0** `Simple Sentence` (0.99) → `passthrough`
- original: Asthma is often treated with a combination of drugs.

**L39.1** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Use all medications as directed by your doctor.

**L39.2** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Read the medication guide or patient instructions provided with each medication.

**L39.3** `Simple Sentence` (0.54) → `passthrough`
- original: Do not change your doses or medication schedule without your doctor's advice.

**L40.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Store at room temperature away from moisture, heat, or cold temperatures.

**L41.0** `Incomplete Sentence` (0.973) → `excluded_incomplete`
- original: Keep the albuterol canister away from open flame or high heat, such as in a car on a hot day.

**L41.1** `Simple Sentence` (0.958) → `passthrough`
- original: The canister may explode if it gets too hot.
- pronoun resolved: The canister may explode if canister gets too hot.
  - edits: “it” → “canister”

**L41.2** `Incomplete Sentence` (0.619) → `excluded_incomplete`
- original: Do not puncture or burn an empty inhaler canister.

## What happens if I miss a dose?

**L44.0** `Incomplete Sentence` (0.944) → `excluded_incomplete`
- original: Use the missed dose as soon as you remember.

**L44.1** `Incomplete Sentence` (0.89) → `excluded_incomplete`
- original: Skip the missed dose if it is almost time for your next scheduled dose.

**L44.2** `Incomplete Sentence` (0.852) → `excluded_incomplete`
- original: Do not use extra medicine to make up the missed dose.

## What happens if I overdose?

**L47.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L47.1** `Simple Sentence` (0.99) → `passthrough`
- original: An overdose of albuterol can be fatal.

**L48.0** `Complex Sentence` (0.542) → `decomposed`
- original: Overdose symptoms may include dry mouth, tremors, chest pain, fast or irregular heartbeat, nausea, general ill feeling, seizure (convulsions), feeling light-headed or fainting.
  - S1: Overdose symptoms may include dry mouth.
  - S2: Overdose symptoms may include tremors.
  - S3: Overdose symptoms may include chest pain.
  - S4: Overdose symptoms may include fast or irregular heartbeat.
  - S5: Overdose symptoms may include nausea.
  - S6: Overdose symptoms may include a general ill feeling.
  - S7: Overdose symptoms may include seizure (convulsions).
  - S8: Overdose symptoms may include feeling light-headed or fainting.

## What should I avoid while using albuterol inhalation?

**L51.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Rinse with water if this medicine gets in your eyes.

## Albuterol inhalation side effects

**L54.0** `Compound Sentence` (0.441) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to albuterol: hives; difficult breathing; swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to albuterol.
  - S2: Signs of an allergic reaction to albuterol include hives.
  - S3: Signs of an allergic reaction to albuterol include difficult breathing.
  - S4: Signs of an allergic reaction to albuterol include swelling of your face, lips, tongue, or throat.

**L55.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L56.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: wheezing, choking, or other breathing problems after using this medicine;
- pronoun resolved: wheezing, choking, or other breathing problems after using Albuterol;
  - edits: “this medicine;” → “Albuterol;”

**L57.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: chest pain, fast heart rate, pounding heartbeats or fluttering in your chest;

**L58.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: pain or burning when you urinate;

**L59.0** `Incomplete Sentence` (0.979) → `excluded_incomplete`
- original: increased thirst, increased urination, hunger, dry mouth, fruity breath odor, drowsiness, dry skin, blurred vision, weight loss; or

**L60.0** `Compound Sentence` (0.414) → `decomposed`
- original: signs of low potassium - leg cramps, constipation, irregular heartbeats, fluttering in your chest, extreme thirst, increased urination, numbness or tingling, muscle weakness or limp feeling.
  - S1: Signs of low potassium include leg cramps.
  - S2: Signs of low potassium include constipation.
  - S3: Signs of low potassium include irregular heartbeats.
  - S4: Signs of low potassium include fluttering in your chest.
  - S5: Signs of low potassium include extreme thirst.
  - S6: Signs of low potassium include increased urination.
  - S7: Signs of low potassium include numbness or tingling.
  - S8: Signs of low potassium include muscle weakness or limp feeling.

**L61.0** `Simple Sentence` (0.935) → `passthrough`
- original: Common albuterol side effects may include:

**L62.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: chest pain, fast or pounding heartbeats;

**L63.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: upset stomach, vomiting;

**L64.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: painful urination;

**L65.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: dizziness;

**L66.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: feeling shaky or nervous;

**L67.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: headache, back pain, body aches; or

**L68.0** `Incomplete Sentence` (0.979) → `excluded_incomplete`
- original: cough, sore throat, sinus pain, runny or stuffy nose.

**L69.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L69.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L69.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## What other drugs will affect albuterol inhalation?

**L72.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Tell your doctor about all your current medicines and any you start or stop using, especially:

**L73.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: any other inhaled medicines or bronchodilators;

**L74.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: digoxin;

**L75.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a diuretic or "water pill";

**L76.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: an antidepressant - amitriptyline, desipramine, imipramine, doxepin, nortriptyline, and others;

**L77.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: a beta blocker - atenolol, carvedilol, labetalol, metoprolol, propranolol, sotalol, and others; or

**L78.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: a MAO inhibitor - isocarboxazid, linezolid, phenelzine, rasagiline, selegiline, tranylcypromine, and others or methylene blue injection

**L79.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L79.1** `Complex Sentence` (0.831) → `decomposed`
- original: Other drugs may interact with albuterol inhalation, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may interact with albuterol inhalation.
  - S2: These include prescription and over-the-counter medicines.
  - S3: These also include vitamins and herbal products.

**L79.2** `Simple Sentence` (0.986) → `passthrough`
- original: Not all possible interactions are listed in this medication guide.

## Popular FAQ

**L82.0** `Incomplete Sentence` (0.831) → `excluded_incomplete`
- original: Q: Can asthma inhalers cause a sore throat?

**L82.1** `Complex Sentence` (0.394) → `decomposed`
- original: A: Learn why asthma inhalers can cause a sore throat, which types are most likely, how to prevent it, and when to call your doctor for thrush or hoarseness.
- pronoun resolved: A: Learn why asthma inhalers can cause a sore throat, which types are most likely, how to prevent a sore throat, and when to call your doctor for thrush or hoarseness.
  - edits: “it,” → “a sore throat,”
  - S1: Learn why asthma inhalers can cause a sore throat.
  - S2: Learn which types of asthma inhalers are most likely to cause a sore throat.
  - S3: Learn how to prevent a sore throat from asthma inhalers.
  - S4: Learn when to call your doctor for thrush or hoarseness.

**L83.0** `Incomplete Sentence` (0.97) → `excluded_incomplete`
- original: Q: Is Salbutamol the same as Albuterol?

**L83.1** `Compound-Complex Sentence` (0.705) → `decomposed`
- original: A: Salbutamol and albuterol are the same active drug; “salbutamol” is the international generic name, while “albuterol” is the name used mainly in the United States for the same short‑acting beta‑2 agonist bronchodilator.
  - S1: Salbutamol and albuterol are the same active drug.
  - S2: Salbutamol is the international generic name.
  - S3: Albuterol is the name used mainly in the United States.
  - S4: Both names refer to the same short-acting beta-2 agonist bronchodilator.

**L83.2** `Simple Sentence` (0.935) → `passthrough`
- original: They share the same chemical structure, mechanism of action, and clinical uses.
- pronoun resolved: Salbutamol and albuterol share the same chemical structure, mechanism of action, and clinical uses.
  - edits: “They” → “Salbutamol and albuterol”

**L83.3** `Compound Sentence` (0.532) → `decomposed`
- original: Most differences patients notice relate to branding, country naming conventions, or inhaler devices, not the medicine itself.
  - S1: Most differences patients notice relate to branding.
  - S2: Most differences patients notice relate to country naming conventions.
  - S3: Most differences patients notice relate to inhaler devices.
  - S4: Most differences patients notice do not relate to the medicine itself.

**L84.0** `Incomplete Sentence` (0.642) → `excluded_incomplete`
- original: Q: Can you use an expired albuterol inhaler?

**L84.1** `Complex Sentence` (0.428) → `decomposed`
- original: A: An albuterol inhaler should be discarded after it passes its expiration date.
- pronoun resolved: A: An albuterol inhaler should be discarded after an expired albuterol inhaler passes an expired albuterol inhaler's expiration date.
  - edits: “it” → “an expired albuterol inhaler”; “its” → “an expired albuterol inhaler's”
  - S1: An albuterol inhaler should be discarded.
  - S2: This should happen after an expired albuterol inhaler passes its expiration date.

**L84.2** `Complex Sentence` (0.817) → `decomposed`
- original: It should be thrown out even sooner if it has been 13 months since it was removed from its foil packaging.
- pronoun resolved: An expired albuterol inhaler should be thrown out even sooner if it has been 13 months since an expired albuterol inhaler was removed from an expired albuterol inhaler's foil packaging.
  - edits: “It” → “An expired albuterol inhaler”; “it” → “an expired albuterol inhaler”; “its” → “an expired albuterol inhaler's”
  - S1: An expired albuterol inhaler should be thrown out.
  - S2: It should be thrown out even sooner if it has been 13 months since it was removed from the foil packaging.
  - S3: The inhaler was removed from the foil packaging.
