# Flonase Nasal Spray — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/flonase.txt` · 141 sentences · 15 changed by pronoun resolution · 193 sentences sent to EDC

## What is Flonase?

**L5.0** `Simple Sentence` (0.983) → `passthrough`
- original: Flonase is a nasal spray containing fluticasone propionate.

**L5.1** `Simple Sentence` (0.945) → `passthrough`
- original: Fluticasone propionate is a corticosteroid that reduces inflammation in the lining of the nose.

**L6.0** `Complex Sentence` (0.62) → `decomposed`
- original: Flonase Nasal Spray is used to treat nasal congestion, sneezing, runny nose, and itchy or watery eyes caused by seasonal or year-round allergies.
  - S1: Flonase Nasal Spray is used to treat nasal congestion, sneezing, runny nose, and itchy or watery eyes.
  - S2: These symptoms are caused by seasonal or year-round allergies.

**L7.0** `Compound Sentence` (0.743) → `decomposed`
- original: Flonase Allergy Relief is for use in adults and children who are at least 4 years old and is available without a prescription.
  - S1: Flonase Allergy Relief is for use in adults and children who are at least 4 years old.
  - S2: It is available without a prescription.

**L7.1** `Compound Sentence` (0.587) → `decomposed`
- original: Children's Flonase Allergy Relief contains the same medicine and is also for ages 4 and older.
  - S1: Children's Flonase Allergy Relief contains the same medicine.
  - S2: It is also for ages 4 and older.

**L8.0** `Compound Sentence` (0.823) → `decomposed`
- original: Flonase Sensimist contains fluticasone furoate rather than fluticasone propionate and is approved for use in adults and children 2 years of age and older.
  - S1: Flonase Sensimist contains fluticasone furoate rather than fluticasone propionate.
  - S2: It is approved for use in adults and children 2 years of age and older.

**L8.1** `Simple Sentence` (0.986) → `passthrough`
- original: Children's Flonase Sensimist is also for ages 2 and older.

**L8.2** `Simple Sentence` (0.923) → `passthrough`
- original: In Flonase Sensimist labeling, relief of itchy, watery eyes applies to ages 12 and older.

**L9.0** `Simple Sentence` (0.853) → `passthrough`
- original: The brand-name prescription version of Flonase nasal spray has been discontinued in the United States.

**L9.1** `Compound Sentence` (0.962) → `decomposed`
- original: Generic fluticasone propionate nasal spray is still available by prescription, and over-the-counter Flonase products and store brands remain on the market.
  - S1: Generic fluticasone propionate nasal spray is still available by prescription.
  - S2: Over-the-counter Flonase products and store brands remain on the market.

**L10.0** `Compound Sentence` (0.489) → `decomposed`
- original: Some products sold under the Flonase brand name are not nasal sprays and do not contain fluticasone.
  - S1: Some products sold under the Flonase brand name are not nasal sprays.
  - S2: They do not contain fluticasone.

**L10.1** `Compound Sentence` (0.967) → `decomposed`
- original: Flonase Headache & Allergy Relief caplets contain acetaminophen, chlorpheniramine, and phenylephrine, and Flonase Nighttime Allergy Relief tablets contain triprolidine.
  - S1: Flonase Headache & Allergy Relief caplets contain acetaminophen, chlorpheniramine, and phenylephrine.
  - S2: Flonase Nighttime Allergy Relief tablets contain triprolidine.

**L10.2** `Incomplete Sentence` (0.963) → `excluded_incomplete`
- original: Check the active ingredients on the carton before use.

## Warnings

**L13.0** `Complex Sentence` (0.726) → `decomposed`
- original: Before using Flonase Nasal Spray, tell your doctor if you have glaucoma or cataracts, liver disease, diabetes, herpes simplex virus of your eyes, tuberculosis or any other infection, sores or ulcers inside your nose, or if you have recently had injury of or surgery on your nose.
  - S1: Before using Flonase Nasal Spray, tell your doctor if you have glaucoma or cataracts.
  - S2: Tell your doctor if you have liver disease.
  - S3: Tell your doctor if you have diabetes.
  - S4: Tell your doctor if you have herpes simplex virus of your eyes.
  - S5: Tell your doctor if you have tuberculosis or any other infection.
  - S6: Tell your doctor if you have sores or ulcers inside your nose.
  - S7: Tell your doctor if you have recently had injury of or surgery on your nose.

**L14.0** `Compound Sentence` (0.966) → `decomposed`
- original: You may start to feel relief on the first day, but it can take several days of regular once-daily use before you get the full effect.
- pronoun resolved: You may start to feel relief on the first day, but Flonase can take several days of regular once-daily use before you get the full effect.
  - edits: “it” → “Flonase”
  - S1: You may start to feel relief on the first day.
  - S2: Flonase can take several days of regular once-daily use before you get the full effect.

**L14.1** `Compound Sentence` (0.354) → `decomposed`
- original: Tell your doctor if your symptoms do not improve within 7 days, or if you develop new symptoms such as severe facial pain or thick nasal discharge.
  - S1: Tell your doctor if your symptoms do not improve within 7 days.
  - S2: Tell your doctor if you develop new symptoms such as severe facial pain or thick nasal discharge.

**L15.0** `Simple Sentence` (0.992) → `passthrough`
- original: Corticosteroids can affect the way your immune system responds to infection.

**L15.1** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Avoid being near people who are sick or have infections.

**L15.2** `Incomplete Sentence` (0.556) → `excluded_incomplete`
- original: Stop use and ask a doctor if you have, or come into contact with someone who has, chickenpox, measles, or tuberculosis.

**L16.0** `Compound Sentence` (0.738) → `decomposed`
- original: Do not administer Flonase Allergy Relief Nasal Spray to a child younger than 4 years old, or Flonase Sensimist to a child younger than 2 years.
  - S1: Do not administer Flonase Allergy Relief Nasal Spray to a child younger than 4 years old.
  - S2: Do not administer Flonase Sensimist to a child younger than 2 years.

**L16.1** `Simple Sentence` (0.993) → `passthrough`
- original: Corticosteroid medication can affect growth in children.

**L16.2** `Incomplete Sentence` (0.95) → `excluded_incomplete`
- original: Talk with your doctor if you think your child is not growing at a normal rate while using this medicine.
- pronoun resolved: Talk with your doctor if you think your child is not growing at a normal rate while using Flonase.
  - edits: “this medicine.” → “Flonase.”

## Before taking this medicine

**L19.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: Do not use Flonase nasal spray:

**L20.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: if you are allergic to fluticasone or to any of the other ingredients

**L21.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: to treat asthma

**L22.0** `Simple Sentence` (0.556) → `passthrough`
- original: if you have had an injury to your nose, or surgery on your nose, that is not fully healed.

**L23.0** `Simple Sentence` (0.483) → `passthrough`
- original: To make sure Flonase is safe for you, tell your doctor if you have ever had:

**L24.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: sores or ulcers inside your nose;

**L25.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: injury of or surgery on your nose;

**L26.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: glaucoma or cataracts;

**L27.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: liver disease;

**L28.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: diabetes;

**L29.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: a weak immune system; or

**L30.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: any type of infection (bacterial, fungal, viral, or parasitic).

**L31.0** `Compound Sentence` (0.436) → `decomposed`
- original: If you use Flonase without a prescription and you have any medical conditions, ask a doctor or pharmacist if this medicine is safe for you.
- pronoun resolved: If you use Flonase without a prescription and you have any medical conditions, ask a doctor or pharmacist if Flonase is safe for you.
  - edits: “this medicine” → “Flonase”
  - S1: If you use Flonase without a prescription and you have any medical conditions, ask a doctor or pharmacist.
  - S2: Ask a doctor or pharmacist if Flonase is safe for you.

**L32.0** `Incomplete Sentence` (0.952) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or breastfeeding.

## How should I use Flonase Nasal Spray?

**L35.0** `Incomplete Sentence` (0.96) → `excluded_incomplete`
- original: Use Flonase exactly as directed on the label, or as prescribed by your doctor.

**L35.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L36.0** `Incomplete Sentence` (0.599) → `excluded_incomplete`
- original: Do not share this medicine with another person, even if they have the same symptoms you have.
- pronoun resolved: Do not share this medicine with another person, even if person have the same symptoms you have.
  - edits: “they” → “person”

**L36.1** `Simple Sentence` (0.979) → `passthrough`
- original: Sharing a bottle can spread germs.

**L37.0** `Compound Sentence` (0.965) → `decomposed`
- original: Your dose will depend on the fluticasone brand or strength you use, and your dose may change once your symptoms improve.
  - S1: Your dose will depend on the fluticasone brand or strength you use.
  - S2: Your dose may change once your symptoms improve.

**L37.1** `Incomplete Sentence` (0.964) → `excluded_incomplete`
- original: Follow all dosing instructions very carefully.

**L38.0** `Simple Sentence` (0.946) → `passthrough`
- original: A child using the nasal spray should be supervised by an adult.

**L39.0** `Incomplete Sentence` (0.96) → `excluded_incomplete`
- original: Read and carefully follow any Instructions for Use provided with your medicine.

**L39.1** `Incomplete Sentence` (0.902) → `excluded_incomplete`
- original: Ask your doctor or pharmacist if you do not understand these instructions.

**L40.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Shake the bottle before each use.

**L40.1** `Compound Sentence` (0.964) → `decomposed`
- original: Flonase Allergy Relief should be shaken gently, and Flonase Sensimist should be shaken vigorously.
  - S1: Flonase Allergy Relief should be shaken gently.
  - S2: Flonase Sensimist should be shaken vigorously.

**L41.0** `Incomplete Sentence` (0.9) → `excluded_incomplete`
- original: Use this product only once a day and do not use more than directed.

**L41.1** `Incomplete Sentence` (0.913) → `excluded_incomplete`
- original: Avoid getting the spray in your eyes or mouth.

**L42.0** `Simple Sentence` (0.666) → `passthrough`
- original: If you switched to fluticasone from another steroid medicine, you should not stop using it suddenly.
- pronoun resolved: If you switched to fluticasone from another steroid medicine, you should not stop using steroid medicine suddenly.
  - edits: “it” → “steroid medicine”

**L42.1** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Follow your doctor's instructions about tapering your dose.

**L43.0** `Simple Sentence` (0.936) → `passthrough`
- original: Storage differs between products.

**L43.1** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Store Flonase Allergy Relief and Children's Flonase Allergy Relief between 4°C and 30°C (39°F and 86°F).

**L43.2** `Incomplete Sentence` (0.651) → `excluded_incomplete`
- original: Store Flonase Sensimist between 15°C and 30°C (59°F and 86°F), and do not refrigerate or freeze it.
- pronoun resolved: Store Flonase Sensimist between 15°C and 30°C (59°F and 86°F), and do not refrigerate or freeze Flonase Sensimist.
  - edits: “it.” → “Flonase Sensimist.”

**L44.0** `Incomplete Sentence` (0.841) → `excluded_incomplete`
- original: Throw the bottle away once you have used the number of sprays stated on the carton, even if there is still liquid in the bottle.

**L44.1** `Simple Sentence` (0.603) → `passthrough`
- original: The correct amount of medicine in each spray cannot be assured after the labeled number of sprays has been used.

**L44.2** `Compound Sentence` (0.449) → `decomposed`
- original: Bottle sizes vary between products and pack sizes, ranging from 30 to 144 metered sprays.
  - S1: Bottle sizes vary between products and pack sizes.
  - S2: They range from 30 to 144 metered sprays.

**L45.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Dosing information:

**L46.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Usual Adult Dose for Rhinitis (adults and children 12 years of age and older):

**L47.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Flonase Allergy Relief Nasal Spray (fluticasone propionate 50 mcg per spray):

**L48.0** `Incomplete Sentence` (0.898) → `excluded_incomplete`
- original: Week 1: use 2 sprays in each nostril once daily

**L49.0** `Simple Sentence` (0.71) → `passthrough`
- original: Week 2 through 6 months: use 1 or 2 sprays in each nostril once daily, as needed to treat your symptoms

**L50.0** `Incomplete Sentence` (0.963) → `excluded_incomplete`
- original: After 6 months of daily use: ask your doctor if you can keep using this medicine

**L51.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Flonase Sensimist Nasal Spray (fluticasone furoate 27.5 mcg per spray):

**L52.0** `Incomplete Sentence` (0.898) → `excluded_incomplete`
- original: Week 1: use 2 sprays in each nostril once daily

**L53.0** `Simple Sentence` (0.71) → `passthrough`
- original: Week 2 through 6 months: use 1 or 2 sprays in each nostril once daily, as needed to treat your symptoms

**L54.0** `Incomplete Sentence` (0.974) → `excluded_incomplete`
- original: After 6 months of daily use: ask your doctor if you can keep using this medicine
- pronoun resolved: After 6 months of daily use: ask your doctor if you can keep using Flonase Sensimist Nasal Spray
  - edits: “this medicine” → “Flonase Sensimist Nasal Spray”

**L55.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Pediatric Dose for Rhinitis:

**L56.0** `Compound Sentence` (0.433) → `decomposed`
- original: 4 to 11 years: Flonase Allergy Relief or Children's Flonase Allergy Relief (fluticasone propionate 50 mcg per spray): 1 spray in each nostril once daily.
  - S1: The recommended age group is 4 to 11 years.
  - S2: The medication is Flonase Allergy Relief or Children's Flonase Allergy Relief (fluticasone propionate 50 mcg per spray).
  - S3: The dosage is 1 spray in each nostril once daily.

**L57.0** `Simple Sentence` (0.619) → `passthrough`
- original: 2 to 11 years: Flonase Sensimist or Children's Flonase Sensimist (fluticasone furoate 27.5 mcg per spray): 1 spray in each nostril once daily.

**L58.0** `Simple Sentence` (0.544) → `passthrough`
- original: Under 4 years: do not use fluticasone propionate nasal spray.

**L59.0** `Simple Sentence` (0.615) → `passthrough`
- original: Under 2 years: do not use fluticasone furoate nasal spray.

**L60.0** `Simple Sentence` (0.984) → `passthrough`
- original: An adult should supervise a child using the spray.

**L60.1** `Simple Sentence` (0.979) → `passthrough`
- original: Children should use it for the shortest amount of time necessary to achieve symptom relief.

**L60.2** `Incomplete Sentence` (0.935) → `excluded_incomplete`
- original: Talk to your child's doctor if your child needs to use the spray for longer than two months a year.

**L61.0** `Incomplete Sentence` (0.971) → `excluded_incomplete`
- original: What happens if I miss a dose?

**L61.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L62.0** `Compound Sentence` (0.562) → `decomposed`
- original: Use the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - S1: Use the medicine as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L62.1** `Incomplete Sentence` (0.946) → `excluded_incomplete`
- original: Do not use two doses at one time.

**L63.0** `Incomplete Sentence` (0.942) → `excluded_incomplete`
- original: What happens if I overdose?

**L63.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L64.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L65.0** `Simple Sentence` (0.982) → `passthrough`
- original: An overdose of Flonase is not expected to produce life-threatening symptoms.

**L65.1** `Complex Sentence` (0.953) → `decomposed`
- original: Using more than the recommended dose, or using it for longer than directed, may increase the chance of corticosteroid-related side effects such as cataracts or glaucoma, adrenal gland problems, an increased risk of infection, sores inside the nose, or slower growth in children.
- pronoun resolved: Using more than the recommended dose, or using Flonase for longer than directed, may increase the chance of corticosteroid-related side effects such as cataracts or glaucoma, adrenal gland problems, an increased risk of infection, sores inside the nose, or slower growth in children.
  - edits: “it” → “Flonase”
  - S1: Using more than the recommended dose may increase the chance of corticosteroid-related side effects.
  - S2: Using Flonase for longer than directed may increase the chance of corticosteroid-related side effects.
  - S3: These side effects include cataracts or glaucoma.
  - S4: These side effects include adrenal gland problems.
  - S5: These side effects include an increased risk of infection.
  - S6: These side effects include sores inside the nose.
  - S7: These side effects include slower growth in children.

## What should I avoid while using Flonase?

**L68.0** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Avoid getting the spray in your eyes or mouth.
- pronoun resolved: Avoid getting Flonase in your eyes or mouth.
  - edits: “the spray” → “Flonase”

**L68.1** `Simple Sentence` (0.597) → `passthrough`
- original: If this does happen, rinse with water.
- pronoun resolved: If getting the spray in your eyes or mouth does happen, rinse with water.
  - edits: “this” → “getting the spray in your eyes or mouth”

**L69.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Avoid being near people who are sick or have infections.

**L69.1** `Incomplete Sentence` (0.69) → `excluded_incomplete`
- original: Call your doctor for preventive treatment if you are exposed to chickenpox or measles.

## Flonase side effects

**L72.0** `Compound Sentence` (0.521) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to Flonase: hives, rash; feeling light-headed; difficult breathing; swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to Flonase.
  - S2: Signs of an allergic reaction include hives and rash.
  - S3: Signs of an allergic reaction include feeling light-headed.
  - S4: Signs of an allergic reaction include difficult breathing.
  - S5: Signs of an allergic reaction include swelling of your face, lips, tongue, or throat.

**L73.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L74.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: severe or frequent nosebleeds;

**L75.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: a constant whistling sound from your nose, which may be a sign of damage inside your nose;

**L76.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: noisy breathing, runny nose, or crusting around your nostrils;

**L77.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: redness, sores, or white patches in your mouth or throat;

**L78.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: fever, chills, body aches;

**L79.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: new changes to your vision, blurred vision, eye pain, or seeing halos around lights;

**L80.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: any wound that will not heal; or

**L81.0** `Incomplete Sentence` (0.974) → `excluded_incomplete`
- original: signs of a hormonal disorder: worsening tiredness or muscle weakness, feeling light-headed, nausea, vomiting.

**L82.0** `Simple Sentence` (0.993) → `passthrough`
- original: Steroid medicine can affect growth in children.

**L82.1** `Incomplete Sentence` (0.869) → `excluded_incomplete`
- original: Tell your doctor if your child is not growing at a normal rate while using this medicine.
- pronoun resolved: Tell your doctor if your child is not growing at a normal rate while using Steroid medicine.
  - edits: “this” → “Steroid”

**L83.0** `Simple Sentence` (0.935) → `passthrough`
- original: Common Flonase side effects may include:

**L84.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: minor nosebleed, burning or itching in your nose;

**L85.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: stinging or sneezing for a few seconds right after use;

**L86.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: sores or white patches inside or around your nose;

**L87.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: cough, trouble breathing;

**L88.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: headache, back pain;

**L89.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: sinus pain, sore throat, fever; or

**L90.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: nausea, vomiting.

**L91.0** `Compound Sentence` (0.545) → `decomposed`
- original: This is not a complete list of side effects, and others may occur.
  - S1: This is not a complete list of side effects.
  - S2: Others may occur.

**L91.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L91.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## What other drugs will affect Flonase?

**L94.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: Tell your doctor or pharmacist about all your other medicines, especially:

**L95.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: an antifungal medicine, such as ketoconazole tablets;

**L96.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: an antiviral medicine to treat hepatitis C or HIV/AIDS, such as ritonavir; or

**L97.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: another steroid medicine for asthma, allergies or skin rash.

**L98.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L98.1** `Complex Sentence` (0.629) → `decomposed`
- original: Other drugs may interact with fluticasone nasal, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may interact with fluticasone nasal.
  - S2: These include prescription and over-the-counter medicines.
  - S3: These also include vitamins and herbal products.

**L98.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.

## Popular FAQ

**L101.0** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Q: What are the risks of using Flonase long-term?

**L101.1** `Complex Sentence` (0.767) → `decomposed`
- original: A: Using Flonase (fluticasone) longer than the label recommends can raise your risk of nosebleeds, nose sores, and a yeast infection in your nose or throat.
  - S1: Using Flonase (fluticasone) longer than the label recommends can raise your risk of nosebleeds.
  - S2: It can also raise your risk of nose sores.
  - S3: It can also raise your risk of a yeast infection in your nose or throat.

**L101.2** `Compound Sentence` (0.76) → `decomposed`
- original: Rarer, body-wide risks include glaucoma or cataracts, bone loss, adrenal gland problems, and slower growth in children.
  - S1: Rarer, body-wide risks include glaucoma or cataracts.
  - S2: Rarer, body-wide risks include bone loss.
  - S3: Rarer, body-wide risks include adrenal gland problems.
  - S4: Rarer, body-wide risks include slower growth in children.

**L101.3** `Simple Sentence` (0.98) → `passthrough`
- original: Most people who use it as directed have no serious problems.
- pronoun resolved: Most people who use Flonase as directed have no serious problems.
  - edits: “it” → “Flonase”

**L101.4** `Simple Sentence` (0.971) → `passthrough`
- original: Adults should ask a doctor before going past 6 months of daily use.

**L101.5** `Simple Sentence` (0.986) → `passthrough`
- original: Children ages 4 to 11 should not use it more than 2 months a year
- pronoun resolved: Children ages 4 to 11 should not use Flonase more than 2 months a year
  - edits: “it” → “Flonase”

**L102.0** `Incomplete Sentence` (0.926) → `excluded_incomplete`
- original: Q: How often can you use Flonase nasal spray?

**L102.1** `Complex Sentence` (0.931) → `decomposed`
- original: A: Flonase (fluticasone propionate) nasal spray is used once per day in both adults and children to provide 24-hour relief from allergy symptoms such as sneezing, runny nose, nasal congestion, and itchy, watery eyes.
  - S1: Flonase (fluticasone propionate) nasal spray is used once per day in both adults and children.
  - S2: It is used to provide 24-hour relief from allergy symptoms.
  - S3: These symptoms include sneezing, runny nose, nasal congestion, and itchy, watery eyes.

**L102.2** `Simple Sentence` (0.991) → `passthrough`
- original: Nasal steroids like Flonase are most effective when used on a regular basis.

**L102.3** `Simple Sentence` (0.918) → `passthrough`
- original: It may take 3 to 4 days of regular use for the full effect during allergy season.
- pronoun resolved: Flonase may take 3 to 4 days of regular use for the full effect during allergy season.
  - edits: “It” → “Flonase”

**L103.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Q: Which is stronger, Flonase OTC or prescription?

**L103.1** `Complex Sentence` (0.544) → `decomposed`
- original: A: Over-the-counter (OTC) Flonase Allergy Relief is exactly the same strength, dose and medicine as prescription Flonase.
  - S1: Over-the-counter (OTC) Flonase Allergy Relief is exactly the same strength, dose, and medicine as prescription Flonase.

**L103.2** `Simple Sentence` (0.793) → `passthrough`
- original: Both contain fluticasone propionate 50 micrograms (mcg) per spray, so neither one is “stronger.”

**L103.3** `Compound Sentence` (0.956) → `decomposed`
- original: The brand-name prescription Flonase has been discontinued in the U.S., but OTC Flonase, generic fluticasone, and store brands are still sold.
  - S1: The brand-name prescription Flonase has been discontinued in the U.S.
  - S2: OTC Flonase, generic fluticasone, and store brands are still sold.

**L104.0** `Incomplete Sentence` (0.968) → `excluded_incomplete`
- original: Q: How long does it take for Flonase to work?

**L104.1** `Complex Sentence` (0.944) → `decomposed`
- original: A: While many people feel effects after the first dose, it may take 3 to 4 days of regular use of Flonase nasal spray for the full effect on allergy symptoms.
- pronoun resolved: A: While many people feel effects after the first dose, Flonase may take 3 to 4 days of regular use of Flonase nasal spray for the full effect on allergy symptoms.
  - edits: “it” → “Flonase”
  - S1: Many people feel effects after the first dose.
  - S2: Flonase may take 3 to 4 days of regular use for the full effect.
  - S3: The full effect is on allergy symptoms.

**L104.2** `Complex Sentence` (0.877) → `decomposed`
- original: For this reason, nasal steroids like Flonase are most effective when used on a regular basis for long-term relief.
  - S1: Nasal steroids like Flonase are most effective when used on a regular basis.
  - S2: They are used for long-term relief.
  - S3: This is for this reason.

**L105.0** `Incomplete Sentence` (0.938) → `excluded_incomplete`
- original: Q: Xhance vs Flonase Allergy Relief - What’s the difference?

**L105.1** `Simple Sentence` (0.971) → `passthrough`
- original: A: Xhance is a prescription nasal spray used to treat nasal polyps in adults with or without chronic rhinosinusistis.

**L105.2** `Simple Sentence` (0.95) → `passthrough`
- original: Flonase Allergy Relief is an over-the-counter (OTC) nasal spray for treatment of allergy symptoms in adults and children 4 years and older.

**L106.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Q: Is Flonase Sensimist the same as Veramyst?

**L106.1** `Complex Sentence` (0.458) → `decomposed`
- original: A: Flonase Sensimist (generic name: fluticasone furoate) Allergy Relief is the over-the-counter (OTC) version of Veramyst.
  - S1: Flonase Sensimist is the over-the-counter version of Veramyst.
  - S2: Flonase Sensimist is allergy relief.
  - S3: Flonase Sensimist has the generic name fluticasone furoate.

**L106.2** `Compound Sentence` (0.742) → `decomposed`
- original: Flonase Sensimist contains the same active ingredient and is the same strength as Veramyst, but prescription Veramyst has now been discontinued in the U.S. and is no longer on the market.
  - S1: Flonase Sensimist contains the same active ingredient and is the same strength as Veramyst.
  - S2: Prescription Veramyst has now been discontinued in the U.S.
  - S3: Prescription Veramyst is no longer on the market.
