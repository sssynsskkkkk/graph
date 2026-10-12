# Clopidogrel — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/clopidogrel.txt` · 82 sentences · 4 changed by pronoun resolution · 123 sentences sent to EDC

## What is clopidogrel?

**L5.0** `Complex Sentence` (0.843) → `decomposed`
- original: Clopidogrel is used to lower your risk of having a stroke, blood clot, or serious heart problem after you've had a heart attack, severe chest pain (angina), or circulation problems.
  - S1: Clopidogrel is used to lower your risk of having a stroke, blood clot, or serious heart problem.
  - S2: This is done after you've had a heart attack, severe chest pain (angina), or circulation problems.

**L6.0** `Simple Sentence` (0.982) → `passthrough`
- original: Clopidogrel may also be used for purposes not listed in this medication guide.

## Clopidogrel side effects

**L9.0** `Incomplete Sentence` (0.452) → `excluded_incomplete`
- original: Get emergency medical help if you have signs of an allergic reaction: hives; difficult breathing; swelling of your face, lips, tongue, or throat.

**L10.0** `Simple Sentence` (0.685) → `passthrough`
- original: Clopidogrel increases your risk of bleeding, which can be severe or life-threatening.

**L10.1** `Compound Sentence` (0.446) → `decomposed`
- original: Call your doctor or seek emergency medical attention if you have bleeding that will not stop, if you have blood in your urine, black or bloody stools, or if you cough up blood or vomit that looks like coffee grounds.
  - S1: Call your doctor or seek emergency medical attention if you have bleeding that will not stop.
  - S2: Call your doctor or seek emergency medical attention if you have blood in your urine.
  - S3: Call your doctor or seek emergency medical attention if you have black or bloody stools.
  - S4: Call your doctor or seek emergency medical attention if you cough up blood or vomit that looks like coffee grounds.

**L11.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Also call your doctor at once if you have:

**L12.0** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: nosebleeds, pale skin, easy bruising, purple spots under your skin or in your mouth;

**L13.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: jaundice (yellowing of your skin or eyes);

**L14.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: fast heartbeats, shortness of breath;

**L15.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: headache, fever, weakness, feeling tired;

**L16.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: little or no urination;

**L17.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a seizure;

**L18.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: low blood sugar --headache, hunger, sweating, irritability, dizziness, fast heart rate, and feeling anxious or shaky; or

**L19.0** `Incomplete Sentence` (0.938) → `excluded_incomplete`
- original: signs of a blood clot --sudden numbness or weakness, confusion, problems with vision or speech.

**L20.0** `Simple Sentence` (0.952) → `passthrough`
- original: Common side effects of clopidogrel may include:

**L21.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: bleeding.

**L22.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L22.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L22.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## Warnings

**L25.0** `Simple Sentence` (0.503) → `passthrough`
- original: You should not use clopidogrel if you have any active bleeding such as a stomach ulcer or bleeding in the brain.

**L26.0** `Simple Sentence` (0.685) → `passthrough`
- original: Clopidogrel increases your risk of bleeding, which can be severe or life-threatening.

**L26.1** `Compound Sentence` (0.446) → `decomposed`
- original: Call your doctor or seek emergency medical attention if you have bleeding that will not stop, if you have blood in your urine, black or bloody stools, or if you cough up blood or vomit that looks like coffee grounds.
  - S1: Call your doctor or seek emergency medical attention if you have bleeding that will not stop.
  - S2: Call your doctor or seek emergency medical attention if you have blood in your urine.
  - S3: Call your doctor or seek emergency medical attention if you have black or bloody stools.
  - S4: Call your doctor or seek emergency medical attention if you cough up blood or vomit that looks like coffee grounds.

**L27.0** `Simple Sentence` (0.492) → `passthrough`
- original: Do not stop taking clopidogrel without first talking to your doctor, even if you have signs of bleeding.

**L27.1** `Simple Sentence` (0.987) → `passthrough`
- original: Stopping clopidogrel may increase your risk of a heart attack or stroke.

## Before taking this medicine

**L30.0** `Simple Sentence` (0.952) → `passthrough`
- original: You should not use clopidogrel if you are allergic to it, or if you have:
- pronoun resolved: You should not use clopidogrel if you are allergic to clopidogrel, or if you have:
  - edits: “it,” → “clopidogrel,”

**L31.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: any active bleeding; or

**L32.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a stomach ulcer or bleeding in the brain (such as from a head injury).

**L33.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Tell your doctor if you have ever had:

**L34.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: an ulcer in your stomach or intestines; or

**L35.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a bleeding disorder or blood clotting disorder.

**L36.0** `Complex Sentence` (0.595) → `decomposed`
- original: Clopidogrel may not work as well if you have certain genetic factors that affect the breakdown of this medicine in your body.
  - S1: Clopidogrel may not work as well.
  - S2: This may happen if you have certain genetic factors.
  - S3: These genetic factors affect the breakdown of this medicine in your body.

**L36.1** `Simple Sentence` (0.977) → `passthrough`
- original: Your doctor may perform a blood test to make sure clopidogrel is right for you.

**L37.0** `Simple Sentence` (0.99) → `passthrough`
- original: This medicine is not expected to harm an unborn baby.

**L37.1** `Simple Sentence` (0.714) → `passthrough`
- original: However, taking clopidogrel within 1 week before childbirth can cause bleeding in the mother.

**L37.2** `Incomplete Sentence` (0.915) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or plan to become pregnant.

**L38.0** `Simple Sentence` (0.975) → `passthrough`
- original: You should not breastfeed while using this medicine.

## How should I take clopidogrel?

**L41.0** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L41.1** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Use these medicines exactly as directed.

**L42.0** `Simple Sentence` (0.987) → `passthrough`
- original: Clopidogrel can be taken with or without food.

**L43.0** `Simple Sentence` (0.987) → `passthrough`
- original: Clopidogrel is sometimes taken together with aspirin.

**L43.1** `Incomplete Sentence` (0.94) → `excluded_incomplete`
- original: Take aspirin only if your doctor tells you to.

**L44.0** `Compound Sentence` (0.945) → `decomposed`
- original: Clopidogrel keeps your blood from coagulating (clotting) and can make it easier for you to bleed, even from a minor injury.
  - S1: Clopidogrel keeps your blood from coagulating (clotting).
  - S2: It can make it easier for you to bleed, even from a minor injury.

**L44.1** `Incomplete Sentence` (0.645) → `excluded_incomplete`
- original: Contact your doctor or seek emergency medical attention if you have any bleeding that will not stop.

**L45.0** `Simple Sentence` (0.752) → `passthrough`
- original: You may need to stop using clopidogrel for a short time before a surgery, medical procedure, or dental work.

**L45.1** `Simple Sentence` (0.963) → `passthrough`
- original: Any healthcare provider who treats you should know that you are taking clopidogrel.

**L46.0** `Simple Sentence` (0.492) → `passthrough`
- original: Do not stop taking clopidogrel without first talking to your doctor, even if you have signs of bleeding.

**L46.1** `Simple Sentence` (0.981) → `passthrough`
- original: Stopping the medicine could increase your risk of a heart attack or stroke.

**L47.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Store at room temperature away from moisture and heat.

## Clopidogrel dosing information

**L50.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Acute Coronary Syndrome:

**L51.0** `Compound Sentence` (0.589) → `decomposed`
- original: Unstable Angina (UA)/Non-ST-Elevation Myocardial Infarction (NSTEMI): -Loading dose: 300 mg orally once -Maintenance dose: 75 mg orally once a day -Duration of therapy: Optimal duration unknown.
  - S1: Unstable Angina (UA)/Non-ST-Elevation Myocardial Infarction (NSTEMI) has a loading dose of 300 mg orally once.
  - S2: The maintenance dose is 75 mg orally once a day.
  - S3: The duration of therapy is optimal unknown.

**L51.1** `Compound Sentence` (0.427) → `decomposed`
- original: ST-Elevation Myocardial Infarction (STEMI): -Loading dose: 300 mg orally once (OPTIONAL) -Maintenance dose: 75 mg orally once a day, with or without thrombolytics -Duration of therapy: Optimal duration unknown.
  - S1: ST-Elevation Myocardial Infarction (STEMI) has an optional loading dose of 300 mg orally once.
  - S2: The maintenance dose is 75 mg orally once a day, with or without thrombolytics.
  - S3: The optimal duration of therapy is unknown.

**L51.2** `Simple Sentence` (0.929) → `passthrough`
- original: Comments: -Administer this drug in combination with aspirin 75 mg to 325 mg orally once a day.
- pronoun resolved: Comments: -Administer Clopidogrel in combination with aspirin 75 mg to 325 mg orally once a day.
  - edits: “this drug” → “Clopidogrel”

**L51.3** `Complex Sentence` (0.693) → `decomposed`
- original: -The benefit of this drug for patients who undergo primary percutaneous coronary intervention is unknown.
- pronoun resolved: -The benefit of Clopidogrel for patients who undergo primary percutaneous coronary intervention is unknown.
  - edits: “this drug” → “Clopidogrel”
  - S1: The benefit of Clopidogrel is unknown.
  - S2: This applies to patients who undergo primary percutaneous coronary intervention.

**L51.4** `Complex Sentence` (0.633) → `decomposed`
- original: Uses: Prevention of atherothrombotic events in patients with non-ST-segment elevation acute coronary syndrome (UA, NSTEMI, those who are to be managed medically, those who are to be managed with coronary revascularization) and STEMI.
  - S1: Uses include prevention of atherothrombotic events.
  - S2: This applies to patients with non-ST-segment elevation acute coronary syndrome.
  - S3: This includes patients with UA.
  - S4: This includes patients with NSTEMI.
  - S5: This includes those who are to be managed medically.
  - S6: This includes those who are to be managed with coronary revascularization.
  - S7: This also applies to patients with STEMI.

**L52.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Ischemic Stroke:

**L53.0** `Complex Sentence` (0.642) → `decomposed`
- original: 75 mg orally once a day Uses: Prevention of atherothrombotic events in patients with a history of recent myocardial infarction, recent stroke, or established peripheral arterial disease.
  - S1: 75 mg is taken orally once a day.
  - S2: The uses include prevention of atherothrombotic events.
  - S3: This applies to patients with a history of recent myocardial infarction.
  - S4: This applies to patients with a history of recent stroke.
  - S5: This applies to patients with established peripheral arterial disease.

**L54.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Myocardial Infarction:

**L55.0** `Complex Sentence` (0.642) → `decomposed`
- original: 75 mg orally once a day Uses: Prevention of atherothrombotic events in patients with a history of recent myocardial infarction, recent stroke, or established peripheral arterial disease.
  - S1: 75 mg is taken orally once a day.
  - S2: The uses include prevention of atherothrombotic events.
  - S3: This applies to patients with a history of recent myocardial infarction.
  - S4: This applies to patients with a history of recent stroke.
  - S5: This applies to patients with established peripheral arterial disease.

**L56.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Peripheral Arterial Disease:

**L57.0** `Complex Sentence` (0.642) → `decomposed`
- original: 75 mg orally once a day Uses: Prevention of atherothrombotic events in patients with a history of recent myocardial infarction, recent stroke, or established peripheral arterial disease.
  - S1: 75 mg is taken orally once a day.
  - S2: The uses include prevention of atherothrombotic events.
  - S3: This applies to patients with a history of recent myocardial infarction.
  - S4: This applies to patients with a history of recent stroke.
  - S5: This applies to patients with established peripheral arterial disease.

## What happens if I miss a dose?

**L60.0** `Compound Sentence` (0.555) → `decomposed`
- original: Take the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - S1: Take the medicine as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L60.1** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

## What happens if I overdose?

**L63.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L63.1** `Simple Sentence` (0.989) → `passthrough`
- original: Overdose can cause excessive bleeding.

## What should I avoid while taking clopidogrel?

**L66.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Avoid alcohol.

**L66.1** `Simple Sentence` (0.99) → `passthrough`
- original: It can increase your risk of stomach bleeding.
- pronoun resolved: Alcohol can increase your risk of stomach bleeding.
  - edits: “It” → “Alcohol”

**L67.0** `Incomplete Sentence` (0.958) → `excluded_incomplete`
- original: Avoid activities that may increase your risk of bleeding or injury.

**L67.1** `Incomplete Sentence` (0.593) → `excluded_incomplete`
- original: Use extra care to prevent bleeding while shaving or brushing your teeth.

**L68.0** `Complex Sentence` (0.628) → `decomposed`
- original: If you also take aspirin: Ask a doctor or pharmacist before using medicines for pain, fever, swelling, or cold/flu symptoms.
  - S1: If you also take aspirin.
  - S2: Ask a doctor or pharmacist.
  - S3: Do this before using medicines for pain, fever, swelling, or cold/flu symptoms.

**L68.1** `Compound Sentence` (0.492) → `decomposed`
- original: They may contain ingredients similar to aspirin (such as salicylates, ibuprofen, ketoprofen, or naproxen).
  - S1: They may contain ingredients similar to aspirin.
  - S2: These ingredients include salicylates, ibuprofen, ketoprofen, or naproxen.

**L68.2** `Simple Sentence` (0.991) → `passthrough`
- original: Taking these products together can increase your risk of bleeding.

## What other drugs will affect clopidogrel?

**L71.0** `Simple Sentence` (0.975) → `passthrough`
- original: Sometimes it is not safe to use certain medications at the same time.

**L71.1** `Complex Sentence` (0.892) → `decomposed`
- original: Some drugs can affect your blood levels of other drugs you take, which may increase side effects or make the medications less effective.
  - S1: Some drugs can affect your blood levels of other drugs you take.
  - S2: This may increase side effects.
  - S3: This may make the medications less effective.

**L72.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Tell your doctor about all your other medicines, especially:

**L73.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: a stomach acid reducer such as omeprazole, Nexium, or Prilosec;

**L74.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: an antidepressant such as citalopram, fluoxetine, sertraline, Cymbalta, Effexor, Lexapro, Pristiq, or Prozac;

**L75.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: rifampin;

**L76.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a blood thinner --warfarin, Coumadin, Jantoven; or

**L77.0** `Incomplete Sentence` (0.819) → `excluded_incomplete`
- original: NSAIDs (nonsteroidal anti-inflammatory drugs) --aspirin, ibuprofen (Advil, Motrin), naproxen (Aleve), celecoxib, diclofenac, indomethacin, meloxicam, and others.

**L78.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L78.1** `Complex Sentence` (0.712) → `decomposed`
- original: Other drugs may affect clopidogrel, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may affect clopidogrel.
  - S2: These other drugs include prescription and over-the-counter medicines.
  - S3: These other drugs also include vitamins and herbal products.

**L78.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.
