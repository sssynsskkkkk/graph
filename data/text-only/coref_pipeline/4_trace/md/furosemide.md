# Furosemide — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/furosemide.txt` · 174 sentences · 24 changed by pronoun resolution · 245 sentences sent to EDC

## What is furosemide?

**L5.0** `Complex Sentence` (0.731) → `decomposed`
- original: Furosemide is a loop diuretic used to treat fluid retention (edema) in people with congestive heart failure, liver disease, or a chronic kidney disorder such as nephrotic syndrome.
  - S1: Furosemide is a loop diuretic.
  - S2: Furosemide is used to treat fluid retention (edema).
  - S3: It is used in people with congestive heart failure.
  - S4: It is used in people with liver disease.
  - S5: It is used in people with a chronic kidney disorder such as nephrotic syndrome.

**L5.1** `Simple Sentence` (0.973) → `passthrough`
- original: Furosemide is also used to treat high blood pressure (hypertension).

**L6.0** `Complex Sentence` (0.613) → `decomposed`
- original: Furosemide works by increasing the amount of urine the body makes, which helps reduce swelling and symptoms of fluid retention and helps lower high blood pressure.
  - S1: Furosemide works by increasing the amount of urine the body makes.
  - S2: This helps reduce swelling and symptoms of fluid retention.
  - S3: It also helps lower high blood pressure.

**L6.1** `Simple Sentence` (0.964) → `passthrough`
- original: Furosemide tablets are sometimes called water pills as they increase how much you urinate.

**L7.0** `Simple Sentence` (0.986) → `passthrough`
- original: Furosemide is also known as frusemide in some countries.

**L7.1** `Compound-Complex Sentence` (0.469) → `decomposed`
- original: It has been available in the United States since the 1960s and comes as tablets (Lasix), an oral liquid, an intravenous solution, and subcutaneous injections and infusions that can be given at home (Furoscix, Lasix ONYU).
- pronoun resolved: Furosemide has been available in the United States since the 1960s and comes as tablets (Lasix), an oral liquid, an intravenous solution, and subcutaneous injections and infusions that can be given at home (Furoscix, Lasix ONYU).
  - edits: “It” → “Furosemide”
  - S1: Furosemide has been available in the United States since the 1960s.
  - S2: Furosemide comes as tablets.
  - S3: Furosemide comes as an oral liquid.
  - S4: Furosemide comes as an intravenous solution.
  - S5: Furosemide comes as subcutaneous injections and infusions.
  - S6: Subcutaneous injections and infusions can be given at home.
  - S7: Subcutaneous injections and infusions are available under the brand names Furoscix and Lasix ONYU.

## Furosemide side effects

**L10.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Common side effects:

**L11.0** `Simple Sentence` (0.926) → `passthrough`
- original: Common furosemide side effects may include:

**L12.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: diarrhea, constipation, loss of appetite

**L13.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: numbness or tingling

**L14.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: headache, dizziness

**L15.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: blurred vision

**L16.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: redness, bruising, swelling, or pain where a subcutaneous dose is given.

**L17.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious furosemide side effects:

**L18.0** `Compound Sentence` (0.359) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to furosemide (hives, difficult breathing, swelling in your face or throat) or a severe skin reaction (fever, sore throat, burning eyes, skin pain, red or purple skin rash with blistering and peeling).
  - S1: Get emergency medical help if you have signs of an allergic reaction to furosemide, such as hives, difficult breathing, or swelling in your face or throat.
  - S2: Get emergency medical help if you have a severe skin reaction, such as fever, sore throat, burning eyes, skin pain, or a red or purple skin rash with blistering and peeling.

**L19.0** `Simple Sentence` (0.989) → `passthrough`
- original: Furosemide may cause other serious side effects.

**L19.1** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L20.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a light-headed feeling, like you might pass out

**L21.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: ringing in your ears, hearing loss

**L22.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: muscle spasms or contractions

**L23.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: pale skin, easy bruising, unusual bleeding

**L24.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: high blood sugar, with increased thirst, increased urination, dry mouth, or fruity breath odor

**L25.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: kidney problems, with swelling, urinating less, feeling tired or short of breath

**L26.0** `Incomplete Sentence` (0.915) → `excluded_incomplete`
- original: signs of liver or pancreas problems, such as loss of appetite, upper stomach pain that may spread to your back, nausea or vomiting, dark urine, or jaundice (yellowing of the skin or eyes)

**L27.0** `Incomplete Sentence` (0.973) → `excluded_incomplete`
- original: signs of an electrolyte imbalance, such as increased thirst or urination, constipation, muscle weakness, leg cramps, numbness or tingling, feeling jittery, or fluttering in your chest.

**L28.0** `Compound Sentence` (0.545) → `decomposed`
- original: This is not a complete list of side effects, and others may occur.
  - S1: This is not a complete list of side effects.
  - S2: Others may occur.

**L28.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L28.2** `Simple Sentence` (0.97) → `passthrough`
- original: You may report side effects to the FDA at 1-800-FDA-1088.

## Warnings

**L31.0** `Simple Sentence` (0.982) → `passthrough`
- original: You should not use furosemide if you are unable to urinate.

**L32.0** `Simple Sentence` (0.98) → `passthrough`
- original: Using more than your recommended dose will not make this medicine more effective.
- pronoun resolved: Using more than your recommended dose will not make furosemide more effective.
  - edits: “this medicine” → “furosemide”

**L32.1** `Simple Sentence` (0.987) → `passthrough`
- original: High doses of this medicine may cause irreversible hearing loss.
- pronoun resolved: High doses of furosemide may cause irreversible hearing loss.
  - edits: “this medicine” → “furosemide”

**L33.0** `Complex Sentence` (0.82) → `decomposed`
- original: Before using this medicine, tell your doctor if you have kidney disease, enlarged prostate, urination problems, cirrhosis or other liver disease, an electrolyte imbalance, high cholesterol, gout, lupus, diabetes, or an allergy to sulfa drugs.
- pronoun resolved: Before using furosemide, tell your doctor if you have kidney disease, enlarged prostate, urination problems, cirrhosis or other liver disease, an electrolyte imbalance, high cholesterol, gout, lupus, diabetes, or an allergy to sulfa drugs.
  - edits: “this medicine,” → “furosemide,”
  - S1: Before using furosemide, tell your doctor if you have kidney disease.
  - S2: Tell your doctor if you have enlarged prostate.
  - S3: Tell your doctor if you have urination problems.
  - S4: Tell your doctor if you have cirrhosis.
  - S5: Tell your doctor if you have other liver disease.
  - S6: Tell your doctor if you have an electrolyte imbalance.
  - S7: Tell your doctor if you have high cholesterol.
  - S8: Tell your doctor if you have gout.
  - S9: Tell your doctor if you have lupus.
  - S10: Tell your doctor if you have diabetes.
  - S11: Tell your doctor if you have an allergy to sulfa drugs.

**L34.0** `Incomplete Sentence` (0.522) → `excluded_incomplete`
- original: Tell your doctor if you have recently had an MRI (magnetic resonance imaging) or any type of scan using a radioactive dye that is injected into your veins.

**L34.1** `Incomplete Sentence` (0.948) → `excluded_incomplete`
- original: Do not take more of this medication than is recommended.
- pronoun resolved: Do not take more of furosemide than is recommended.
  - edits: “this medication” → “furosemide”

**L35.0** `Simple Sentence` (0.711) → `passthrough`
- original: If you are being treated for high blood pressure, keep using this medicine even if you feel fine.
- pronoun resolved: If you are being treated for high blood pressure, keep using furosemide even if you feel fine.
  - edits: “this medicine” → “furosemide”

**L35.1** `Simple Sentence` (0.988) → `passthrough`
- original: High blood pressure often has no symptoms.

**L36.0** `Complex Sentence` (0.934) → `decomposed`
- original: Furosemide is a potent diuretic which, if given in excessive amounts, can lead to a profound diuresis with water and electrolyte depletion.
  - S1: Furosemide is a potent diuretic.
  - S2: If given in excessive amounts, furosemide can lead to a profound diuresis.
  - S3: This diuresis can cause water and electrolyte depletion.

**L36.1** `Compound Sentence` (0.964) → `decomposed`
- original: Careful medical supervision is required, and the dose schedule must be adjusted to the individual patient's needs.
  - S1: Careful medical supervision is required.
  - S2: The dose schedule must be adjusted to the individual patient's needs.

**L37.0** `Incomplete Sentence` (0.967) → `excluded_incomplete`
- original: Tell your doctor about all your other medicines.

**L37.1** `Simple Sentence` (0.988) → `passthrough`
- original: Some drugs should not be used with furosemide.

## Before taking this medicine

**L40.0** `Simple Sentence` (0.877) → `passthrough`
- original: You should not use furosemide if you are allergic to it or are unable to urinate.
- pronoun resolved: You should not use furosemide if you are allergic to furosemide or are unable to urinate.
  - edits: “it” → “furosemide”

**L41.0** `Simple Sentence` (0.769) → `passthrough`
- original: To make sure furosemide is safe for you, tell your doctor if you have ever had:

**L42.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: an electrolyte imbalance (such as low levels of potassium or magnesium in your blood)

**L43.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: enlarged prostate, bladder obstruction, or other urination problems

**L44.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: gout

**L45.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: lupus

**L46.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: diabetes

**L47.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: an allergy to sulfa drugs

**L48.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: kidney disease

**L49.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: cirrhosis or other liver disease.

**L50.0** `Incomplete Sentence` (0.575) → `excluded_incomplete`
- original: Tell your doctor if you have an MRI (magnetic resonance imaging) or any type of scan using a radioactive dye that is injected into a vein.

**L50.1** `Simple Sentence` (0.991) → `passthrough`
- original: Contrast dyes and furosemide can harm your kidneys.

**L51.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Subcutaneous furosemide given at home:

**L52.0** `Simple Sentence` (0.983) → `passthrough`
- original: Two brands of furosemide are designed to be given under the skin at home rather than in hospital.

**L53.0** `Complex Sentence` (0.435) → `decomposed`
- original: Furoscix is used to treat edema in adults with chronic heart failure or chronic kidney disease, including the nephrotic syndrome, and in children weighing 43 kg (94.7 lb) or more.
  - S1: Furoscix is used to treat edema in adults with chronic heart failure or chronic kidney disease.
  - S2: This includes the nephrotic syndrome.
  - S3: It is also used in children weighing 43 kg (94.7 lb) or more.

**L53.1** `Simple Sentence` (0.905) → `passthrough`
- original: It comes in two forms:
- pronoun resolved: Furoscix comes in two forms:
  - edits: “It” → “Furoscix”

**L54.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: the Furoscix ReadyFlow, a prefilled autoinjector that delivers 80 mg of furosemide in about 10 seconds.

**L54.1** `Simple Sentence` (0.989) → `passthrough`
- original: It can be used in adults and in children weighing 43 kg or more.
- pronoun resolved: Furoscix can be used in adults and in children weighing 43 kg or more.
  - edits: “It” → “Furoscix”

**L55.0** `Incomplete Sentence` (0.949) → `excluded_incomplete`
- original: the Furoscix On-Body Infusor, a wearable device that delivers 30 mg of furosemide over the first hour and then 12.5 mg per hour for the next 4 hours, giving 80 mg over about 5 hours.

**L55.1** `Simple Sentence` (0.989) → `passthrough`
- original: It can be used in adults and in children weighing 43 kg or more.
- pronoun resolved: Furoscix can be used in adults and in children weighing 43 kg or more.
  - edits: “It” → “Furoscix”

**L56.0** `Simple Sentence` (0.845) → `passthrough`
- original: Do not use the Furoscix On-Body Infusor if you are allergic to medical adhesives.

**L56.1** `Simple Sentence` (0.989) → `passthrough`
- original: The Furoscix ReadyFlow contains benzyl alcohol as a preservative.

**L57.0** `Complex Sentence` (0.642) → `decomposed`
- original: Lasix ONYU is a pre-programmed infusor containing furosemide that is FDA-approved for the treatment of edema in adults with chronic heart failure.
  - S1: Lasix ONYU is a pre-programmed infusor.
  - S2: The infusor contains furosemide.
  - S3: The infusor is FDA-approved for the treatment of edema in adults with chronic heart failure.

**L58.0** `Compound Sentence` (0.919) → `decomposed`
- original: Subcutaneous furosemide is not for use in an emergency, and it is not for long-term use.
- pronoun resolved: Subcutaneous furosemide is not for use in an emergency, and Subcutaneous furosemide is not for long-term use.
  - edits: “it” → “Subcutaneous furosemide”
  - S1: Subcutaneous furosemide is not for use in an emergency.
  - S2: Subcutaneous furosemide is not for long-term use.

**L58.1** `Simple Sentence` (0.982) → `passthrough`
- original: It should be replaced with oral diuretics as soon as practical.
- pronoun resolved: Subcutaneous furosemide should be replaced with oral diuretics as soon as practical.
  - edits: “It” → “Subcutaneous furosemide”

**L59.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Pregnancy:

**L60.0** `Simple Sentence` (0.98) → `passthrough`
- original: It is not known if furosemide will harm an unborn baby.

**L60.1** `Incomplete Sentence` (0.915) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or plan to become pregnant.

**L61.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Breastfeeding:

**L62.0** `Simple Sentence` (0.989) → `passthrough`
- original: It may not be safe to breastfeed while using furosemide.
- pronoun resolved: Furosemide may not be safe to breastfeed while using furosemide.
  - edits: “It” → “Furosemide”

**L62.1** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Ask your doctor about any risk.

**L62.2** `Simple Sentence` (0.991) → `passthrough`
- original: Furosemide may slow breast milk production.

## How should I use furosemide?

**L65.0** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Take or administer furosemide exactly as prescribed by your doctor.

**L65.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L66.0** `Simple Sentence` (0.989) → `passthrough`
- original: Furosemide oral tablets and liquid are taken by mouth.

**L66.1** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: Measure liquid medicine with the supplied measuring device, not a kitchen spoon.

**L67.0** `Simple Sentence` (0.977) → `passthrough`
- original: Furosemide injection is given in a muscle, under the skin, or in a vein.

**L67.1** `Simple Sentence` (0.934) → `passthrough`
- original: A healthcare provider will give you this injection if you are unable to take the medicine by mouth.

**L68.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Using subcutaneous furosemide at home:

**L69.0** `Compound Sentence` (0.957) → `decomposed`
- original: You or your caregiver should be trained before your first dose, and you should read the Instructions for Use that comes with your prescription.
  - S1: You or your caregiver should be trained before your first dose.
  - S2: You should read the Instructions for Use that comes with your prescription.

**L69.1** `Incomplete Sentence` (0.32) → `excluded_incomplete`
- original: Wash your hands first, and check that the liquid is clear and colorless to slightly yellow.

**L69.2** `Incomplete Sentence` (0.667) → `excluded_incomplete`
- original: Do not use it if you see particles or if it is cloudy or discolored.
- pronoun resolved: Do not use liquid if you see particles or if liquid is cloudy or discolored.
  - edits: “it” → “liquid”; “it” → “liquid”

**L70.0** `Compound Sentence` (0.914) → `decomposed`
- original: Subcutaneous furosemide is given into the abdomen only, and you should use a different spot on the abdomen each time.
  - S1: Subcutaneous furosemide is given into the abdomen only.
  - S2: You should use a different spot on the abdomen each time.

**L71.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Furoscix ReadyFlow autoinjector

**L72.0** `Incomplete Sentence` (0.4) → `excluded_incomplete`
- original: Choose a site at least two inches from your belly button, avoiding skin that is broken or irritated and any scars or stretch marks.

**L72.1** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: Clean it and let it dry.

**L73.0** `Compound Sentence` (0.436) → `decomposed`
- original: Pull the blue cap straight off, then press the device firmly against your skin and hold it there for about 10 seconds, until the yellow plunger rod stops moving and fills the viewing window.
- pronoun resolved: Pull the blue cap straight off, then press the device firmly against your skin and hold device there for about 10 seconds, until the yellow plunger rod stops moving and fills the viewing window.
  - edits: “it” → “device”
  - S1: Pull the blue cap straight off.
  - S2: Press the device firmly against your skin.
  - S3: Hold the device there for about 10 seconds.
  - S4: Continue holding until the yellow plunger rod stops moving and fills the viewing window.

**L74.0** `Compound Sentence` (0.379) → `decomposed`
- original: If you lift the device away before the window is completely yellow, you may not get the full dose.
  - S1: If you lift the device away before the window is completely yellow, you may not get the full dose.

**L74.1** `Compound Sentence` (0.442) → `decomposed`
- original: Call your healthcare provider if this happens, and do not use a second device unless you are told to.
  - S1: Call your healthcare provider if this happens.
  - S2: Do not use a second device unless you are told to.

**L75.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Furoscix On-Body Infusor and Lasix ONYU Infusor

**L76.0** `Compound Sentence` (0.733) → `decomposed`
- original: The infusion takes about 5 hours, so plan to stay somewhere you can relax and reach a bathroom.
  - S1: The infusion takes about 5 hours.
  - S2: So, plan to stay somewhere you can relax and reach a bathroom.

**L77.0** `Compound Sentence` (0.665) → `decomposed`
- original: Apply the device to a flat, clean, hairless area of the abdomen below the rib cage and above the belt line, and press it firmly into place.
- pronoun resolved: Apply the device to a flat, clean, hairless area of the abdomen below the rib cage and above the belt line, and press device firmly into place.
  - edits: “it” → “device”
  - S1: Apply the device to a flat, clean, hairless area of the abdomen below the rib cage and above the belt line.
  - S2: Press the device firmly into place.

**L77.1** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Do not remove and reapply it.

**L78.0** `Incomplete Sentence` (0.647) → `excluded_incomplete`
- original: Limit your activity while wearing it and avoid bending as much as you can.
- pronoun resolved: Limit your activity while wearing device and avoid bending as much as you can.
  - edits: “it” → “device”

**L78.1** `Incomplete Sentence` (0.974) → `excluded_incomplete`
- original: Do not exercise or do anything that might knock it off.
- pronoun resolved: Do not exercise or do anything that might knock device off.
  - edits: “it” → “device”

**L79.0** `Incomplete Sentence` (0.914) → `excluded_incomplete`
- original: Do not get the infusor wet.

**L79.1** `Compound Sentence` (0.937) → `decomposed`
- original: Do not bathe, shower, or swim while wearing it, and do not apply lotions or creams to the area where it is placed.
- pronoun resolved: Do not bathe, shower, or swim while wearing device, and do not apply lotions or creams to the area where device is placed.
  - edits: “it,” → “device,”; “it” → “device”
  - S1: Do not bathe, shower, or swim while wearing device.
  - S2: Do not apply lotions or creams to the area where device is placed.

**L80.0** `Compound Sentence` (0.961) → `decomposed`
- original: Traveling by car or airplane while wearing the infusor is not recommended, and the Furoscix On-Body Infusor cannot be used in an MRI setting.
  - S1: Traveling by car or airplane while wearing the infusor is not recommended.
  - S2: The Furoscix On-Body Infusor cannot be used in an MRI setting.

**L81.0** `Incomplete Sentence` (0.513) → `excluded_incomplete`
- original: Do not use the infusor within 12 inches of mobile phones, tablets, computers, or wireless accessories such as a remote control or Bluetooth device.

**L82.0** `Simple Sentence` (0.961) → `passthrough`
- original: Your healthcare provider will show you what the indicator light and alarms mean.

**L82.1** `Complex Sentence` (0.648) → `decomposed`
- original: You must use the infusor in a setting where you can detect and respond to these alarms to ensure you receive the full dose.
  - S1: You must use the infusor in a setting where you can detect and respond to these alarms.
  - S2: You must use the infusor in a setting where you can detect and respond to these alarms to ensure you receive the full dose.

**L82.2** `Compound Sentence` (0.496) → `decomposed`
- original: If the device falls off, or the light blinks red, call your healthcare provider and do not reuse it.
  - S1: If the device falls off, call your healthcare provider.
  - S2: If the light blinks red, call your healthcare provider.
  - S3: Do not reuse the device.

**L83.0** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: Dispose of used autoinjectors, infusors, and cartridges in a sharps container.

**L83.1** `Compound Sentence` (0.775) → `decomposed`
- original: Do not put them in household trash and do not recycle them.
- pronoun resolved: Do not put autoinjectors, infusors, and cartridges in household trash and do not recycle them.
  - edits: “them” → “autoinjectors, infusors, and cartridges”
  - S1: Do not put autoinjectors, infusors, and cartridges in household trash.
  - S2: Do not recycle them.

**L84.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: General furosemide dosing information:

**L85.0** `Incomplete Sentence` (0.936) → `excluded_incomplete`
- original: Do not use more than your recommended dose.

**L85.1** `Simple Sentence` (0.987) → `passthrough`
- original: High doses of furosemide may cause irreversible hearing loss.

**L86.0** `Simple Sentence` (0.985) → `passthrough`
- original: Doses are based on weight in children and teenagers.

**L86.1** `Simple Sentence` (0.931) → `passthrough`
- original: Your child's dose may change if the child gains or loses weight.

**L87.0** `Compound Sentence` (0.962) → `decomposed`
- original: This medicine will make you urinate more often, and you may get dehydrated easily.
  - S1: This medicine will make you urinate more often.
  - S2: You may get dehydrated easily.

**L87.1** `Incomplete Sentence` (0.972) → `excluded_incomplete`
- original: Follow your doctor's instructions about using potassium supplements or getting enough salt and potassium in your diet.

**L88.0** `Compound Sentence` (0.943) → `decomposed`
- original: Your blood pressure will need to be checked often, and you may need other medical tests.
  - S1: Your blood pressure will need to be checked often.
  - S2: You may need other medical tests.

**L89.0** `Simple Sentence` (0.891) → `passthrough`
- original: If you have high blood pressure, keep using furosemide even if you feel well.

**L89.1** `Simple Sentence` (0.988) → `passthrough`
- original: High blood pressure often has no symptoms.

**L90.0** `Simple Sentence` (0.727) → `passthrough`
- original: If you need surgery, tell the surgeon ahead of time that you are using furosemide.

## Dosing information

**L93.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Usual adult dose for edema associated with congestive heart failure, cirrhosis of the liver, and chronic renal disease (including nephrotic syndrome):

**L94.0** `Incomplete Sentence` (0.881) → `excluded_incomplete`
- original: Oral: initial dose 20 to 80 mg orally once.

**L94.1** `Complex Sentence` (0.571) → `decomposed`
- original: This may be repeated at the same dose or increased by 20 or 40 mg no sooner than 6 to 8 hours after the previous dose, until the desired diuretic effect has been obtained.
- pronoun resolved: Initial dose may be repeated at the same dose or increased by 20 or 40 mg no sooner than 6 to 8 hours after the previous dose, until the desired diuretic effect has been obtained.
  - edits: “This” → “Initial dose”
  - S1: The initial dose may be repeated.
  - S2: The repeated dose may be the same or increased by 20 or 40 mg.
  - S3: This repetition occurs no sooner than 6 to 8 hours after the previous dose.
  - S4: The process continues until the desired diuretic effect has been obtained.

**L95.0** `Simple Sentence` (0.829) → `passthrough`
- original: Maintenance dose: administer the dose that provided the desired diuretic effect once or twice a day (for example, at 8 am and 2 pm).

**L96.0** `Simple Sentence` (0.728) → `passthrough`
- original: Comments: edema may be most efficiently and safely mobilized by giving this drug on 2 to 4 consecutive days each week.

**L96.1** `Complex Sentence` (0.954) → `decomposed`
- original: When doses greater than 80 mg/day are given for prolonged periods, careful clinical observation and laboratory monitoring are particularly advisable.
  - S1: When doses greater than 80 mg/day are given for prolonged periods.
  - S2: Careful clinical observation and laboratory monitoring are particularly advisable.

**L97.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Usual Furoscix adult and pediatric 43 kg and above dose (ReadyFlow autoinjector):

**L98.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: 80 mg of furosemide given subcutaneously in about 10 seconds.

**L99.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Usual Furoscix adult and pediatric 43 kg and above dose (On-Body Infusor):

**L100.0** `Incomplete Sentence` (0.878) → `excluded_incomplete`
- original: 30 mg of furosemide over the first hour, then 12.5 mg per hour for the subsequent 4 hours.

**L100.1** `Simple Sentence` (0.986) → `passthrough`
- original: This dose is delivered automatically by the On-Body Infusor.

**L101.0** `Complex Sentence` (0.399) → `decomposed`
- original: In children weighing at least 43 kg, the device must be applied by a healthcare provider or adult caregiver.
  - S1: The device must be applied by a healthcare provider or adult caregiver.
  - S2: This applies to children weighing at least 43 kg.

**L102.0** `Compound Sentence` (0.782) → `decomposed`
- original: Furoscix is not for chronic use and should be replaced with oral diuretics as soon as practical.
  - S1: Furoscix is not for chronic use.
  - S2: It should be replaced with oral diuretics as soon as practical.

**L102.1** `Complex Sentence` (0.926) → `decomposed`
- original: People with significantly reduced kidney function may need additional diuretic therapy, because both Furoscix devices deliver a fixed 80 mg dose.
  - S1: People with significantly reduced kidney function may need additional diuretic therapy.
  - S2: Both Furoscix devices deliver a fixed 80 mg dose.
  - S3: The therapy is needed because both Furoscix devices deliver a fixed 80 mg dose.

**L103.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual adult furosemide dose for pulmonary edema:

**L104.0** `Incomplete Sentence` (0.944) → `excluded_incomplete`
- original: IV: 40 mg IV slowly over 1 to 2 minutes.

**L104.1** `Complex Sentence` (0.89) → `decomposed`
- original: If a satisfactory response does not occur within one hour, this may be increased to 80 mg IV slowly over 1 to 2 minutes.
- pronoun resolved: If a satisfactory response does not occur within one hour, a satisfactory response may be increased to 80 mg IV slowly over 1 to 2 minutes.
  - edits: “this” → “a satisfactory response”
  - S1: If a satisfactory response does not occur within one hour.
  - S2: A satisfactory response may be increased to 80 mg.
  - S3: The response is administered IV slowly over 1 to 2 minutes.

**L105.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: Use: adjunctive therapy in acute pulmonary edema.

**L105.1** `Simple Sentence` (0.978) → `passthrough`
- original: IV administration is indicated when a rapid onset of diuresis is desired.

**L106.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual adult furosemide dose for hypertension:

**L107.0** `Simple Sentence` (0.492) → `passthrough`
- original: Oral: initial dose 80 mg/day, usually divided into 40 mg orally twice a day.

**L108.0** `Incomplete Sentence` (0.932) → `excluded_incomplete`
- original: Use: treatment of hypertension alone or in combination with other antihypertensive agents.

**L109.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual pediatric furosemide oral dose for edema:

**L110.0** `Incomplete Sentence` (0.948) → `excluded_incomplete`
- original: Initial dose: 2 mg/kg orally once.

**L110.1** `Complex Sentence` (0.918) → `decomposed`
- original: If the diuretic response to the initial dose is not satisfactory, this may be increased by 1 or 2 mg/kg, given no sooner than 6 to 8 hours after the previous dose.
- pronoun resolved: If the diuretic response to the initial dose is not satisfactory, the diuretic response may be increased by 1 or 2 mg/kg, given no sooner than 6 to 8 hours after the previous dose.
  - edits: “this” → “the diuretic response”
  - S1: If the diuretic response to the initial dose is not satisfactory, the diuretic response may be increased by 1 or 2 mg/kg.
  - S2: This increase should be given no sooner than 6 to 8 hours after the previous dose.

**L110.2** `Simple Sentence` (0.981) → `passthrough`
- original: Doses greater than 6 mg/kg body weight are not recommended.

**L111.0** `Incomplete Sentence` (0.891) → `excluded_incomplete`
- original: Maintenance dose: adjust to the minimum effective dose.

**L112.0** `Incomplete Sentence` (0.447) → `excluded_incomplete`
- original: Use: treatment of edema associated with congestive heart failure, cirrhosis of the liver and renal disease, including the nephrotic syndrome, especially when an agent with greater diuretic potential is desired.

## What happens if I miss a dose?

**L115.0** `Compound Sentence` (0.767) → `decomposed`
- original: Furosemide is sometimes used only once, so you may not be on a dosing schedule.
  - S1: Furosemide is sometimes used only once.
  - S2: You may not be on a dosing schedule.

**L115.1** `Compound-Complex Sentence` (0.487) → `decomposed`
- original: If you are using the medication regularly, use the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - S1: You are using the medication regularly.
  - S2: Use the medicine as soon as you can.
  - S3: Skip the missed dose if it is almost time for your next dose.

**L115.2** `Incomplete Sentence` (0.946) → `excluded_incomplete`
- original: Do not use two doses at one time.

## What happens if I overdose?

**L118.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L119.0** `Compound Sentence` (0.494) → `decomposed`
- original: Overdose symptoms may include feeling very thirsty or hot, heavy sweating, hot and dry skin, extreme weakness, or fainting.
  - S1: Overdose symptoms may include feeling very thirsty or hot.
  - S2: They may include heavy sweating.
  - S3: They may include hot and dry skin.
  - S4: They may include extreme weakness.
  - S5: They may include fainting.

## What should I avoid while using furosemide?

**L122.0** `Incomplete Sentence` (0.599) → `excluded_incomplete`
- original: Avoid getting up too fast from a sitting or lying position, or you may feel dizzy.

**L123.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Avoid becoming dehydrated.

**L123.1** `Incomplete Sentence` (0.962) → `excluded_incomplete`
- original: Follow your doctor's instructions about the type and amount of liquids you should drink while you are using furosemide.

**L124.0** `Simple Sentence` (0.989) → `passthrough`
- original: Drinking alcohol with this medicine can cause side effects.
- pronoun resolved: Drinking alcohol with Furosemide can cause side effects.
  - edits: “this medicine” → “Furosemide”

**L125.0** `Simple Sentence` (0.984) → `passthrough`
- original: Furosemide could make you sunburn more easily.

**L125.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Avoid sunlight or tanning beds.

**L125.2** `Incomplete Sentence` (0.9) → `excluded_incomplete`
- original: Wear protective clothing and use sunscreen (SPF 30 or higher) when you are outdoors.

**L126.0** `Complex Sentence` (0.796) → `decomposed`
- original: If you have high blood pressure, ask a doctor or pharmacist before taking any medicines that can raise your blood pressure, such as diet pills or cough-and-cold medicine.
  - S1: If you have high blood pressure, ask a doctor or pharmacist before taking any medicines that can raise your blood pressure.
  - S2: Some medicines that can raise your blood pressure include diet pills or cough-and-cold medicine.

## What other drugs will affect furosemide?

**L129.0** `Simple Sentence` (0.978) → `passthrough`
- original: Sometimes it is not safe to use certain medicines at the same time.

**L129.1** `Complex Sentence` (0.909) → `decomposed`
- original: Some drugs can affect your blood levels of other drugs you use, which may increase side effects or make the medicines less effective.
  - S1: Some drugs can affect your blood levels of other drugs you use.
  - S2: This may increase side effects.
  - S3: This may make the medicines less effective.

**L130.0** `Simple Sentence` (0.358) → `passthrough`
- original: If you also take sucralfate, take your furosemide dose 2 hours before or 2 hours after you take sucralfate.

**L131.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Tell your doctor about all your other medicines, especially:

**L132.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: another diuretic (do not use furosemide with ethacrynic acid)

**L133.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: methotrexate

**L134.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: chloral hydrate

**L135.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: lithium

**L136.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: phenytoin

**L137.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: an antibiotic, especially a cephalosporin or an aminoglycoside (avoid using aminoglycosides with furosemide)

**L138.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: cancer medicine, such as cisplatin

**L139.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: cyclosporine

**L140.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: thyroid hormones

**L141.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: heart or blood pressure medicine, including ACE inhibitors and angiotensin receptor blockers

**L142.0** `Incomplete Sentence` (0.95) → `excluded_incomplete`
- original: NSAIDs (nonsteroidal anti-inflammatory drugs), such as aspirin, ibuprofen (Advil, Motrin), naproxen (Aleve), celecoxib, diclofenac, indomethacin, meloxicam, and others.

**L143.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L143.1** `Complex Sentence` (0.691) → `decomposed`
- original: Other drugs may interact with furosemide, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may interact with furosemide.
  - S2: These include prescription and over-the-counter medicines.
  - S3: These also include vitamins and herbal products.

**L143.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.
