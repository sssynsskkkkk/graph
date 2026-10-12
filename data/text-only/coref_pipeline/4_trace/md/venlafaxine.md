# Venlafaxine — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/venlafaxine.txt` · 124 sentences · 7 changed by pronoun resolution · 202 sentences sent to EDC

## What is venlafaxine?

**L5.0** `Simple Sentence` (0.989) → `passthrough`
- original: Venlafaxine is used in adults to treat major depressive disorder.

**L5.1** `Complex Sentence` (0.848) → `decomposed`
- original: Venlafaxine extended-release (long-acting) capsules are also used to treat generalized anxiety disorder (GAD; excessive worrying that is difficult to control), social anxiety disorder (extreme fear of interacting with others or performing in front of others that interferes with normal life), and panic disorder (sudden, unexpected attacks of extreme fear and worry about these attacks).
  - S1: Venlafaxine extended-release capsules are used to treat generalized anxiety disorder.
  - S2: Generalized anxiety disorder is excessive worrying that is difficult to control.
  - S3: Venlafaxine extended-release capsules are also used to treat social anxiety disorder.
  - S4: Social anxiety disorder is extreme fear of interacting with others or performing in front of others that interferes with normal life.
  - S5: Venlafaxine extended-release capsules are also used to treat panic disorder.
  - S6: Panic disorder is sudden, unexpected attacks of extreme fear and worry about these attacks.

**L6.0** `Simple Sentence` (0.984) → `passthrough`
- original: Venlafaxine belongs to a class of medications called selective serotonin and norepinephrine reuptake inhibitors (SNRIs).

**L6.1** `Complex Sentence` (0.771) → `decomposed`
- original: Venlafaxine works by increasing the amounts of serotonin and norepinephrine, natural substances in the brain that help maintain mental balance.
  - S1: Venlafaxine works by increasing the amounts of serotonin and norepinephrine.
  - S2: Serotonin and norepinephrine are natural substances in the brain.
  - S3: These substances help maintain mental balance.

## Warnings

**L9.0** `Simple Sentence` (0.96) → `passthrough`
- original: You should not take venlafaxine if you have uncontrolled narrow-angle glaucoma.

**L10.0** `Compound Sentence` (0.521) → `decomposed`
- original: Do not use venlafaxine within 7 days before or 14 days after you have used an MAO inhibitor, such as isocarboxazid, linezolid, methylene blue injection, phenelzine, or tranylcypromine.
  - S1: Do not use venlafaxine within 7 days before you have used an MAO inhibitor.
  - S2: Do not use venlafaxine within 14 days after you have used an MAO inhibitor.
  - S3: Examples of MAO inhibitors include isocarboxazid, linezolid, methylene blue injection, phenelzine, and tranylcypromine.

**L11.0** `Simple Sentence` (0.982) → `passthrough`
- original: Some young people have thoughts about suicide when first taking an antidepressant.

**L11.1** `Incomplete Sentence` (0.9) → `excluded_incomplete`
- original: Stay alert to changes in your mood or symptoms.

**L11.2** `Compound-Complex Sentence` (0.424) → `decomposed`
- original: Report any new or worsening symptoms to your doctor, such as: mood or behavioral changes, anxiety, panic attacks, trouble sleeping, or if you feel impulsive, irritable, agitated, hostile, aggressive, restless, hyperactive (mentally or physically), more depressed, or have thoughts about suicide or hurting yourself.
  - S1: Report any new or worsening symptoms to your doctor.
  - S2: Mood or behavioral changes are new or worsening symptoms.
  - S3: Anxiety is a new or worsening symptom.
  - S4: Panic attacks are new or worsening symptoms.
  - S5: Trouble sleeping is a new or worsening symptom.
  - S6: Feeling impulsive is a new or worsening symptom.
  - S7: Feeling irritable is a new or worsening symptom.
  - S8: Feeling agitated is a new or worsening symptom.
  - S9: Feeling hostile is a new or worsening symptom.
  - S10: Feeling aggressive is a new or worsening symptom.
  - S11: Feeling restless is a new or worsening symptom.
  - S12: Feeling hyperactive mentally is a new or worsening symptom.
  - S13: Feeling hyperactive physically is a new or worsening symptom.
  - S14: Feeling more depressed is a new or worsening symptom.
  - S15: Having thoughts about suicide is a new or worsening symptom.
  - S16: Having thoughts about hurting yourself is a new or worsening symptom.

**L12.0** `Simple Sentence` (0.662) → `passthrough`
- original: Do not stop using venlafaxine without first talking to your doctor.

**L13.0** `Incomplete Sentence` (0.487) → `excluded_incomplete`
- original: Do not give this medicine to anyone younger than 18 years old without the advice of a doctor.
- pronoun resolved: Do not give Venlafaxine to anyone younger than 18 years old without the advice of a doctor.
  - edits: “this medicine” → “Venlafaxine”

**L13.1** `Simple Sentence` (0.989) → `passthrough`
- original: Venlafaxine is not FDA approved for use in children.

## Before taking this medicine

**L16.0** `Simple Sentence` (0.872) → `passthrough`
- original: You should not take venlafaxine if you are allergic to it or to desvenlafaxine (Pristiq).
- pronoun resolved: You should not take venlafaxine if you are allergic to venlafaxine or to desvenlafaxine (Pristiq).
  - edits: “it” → “venlafaxine”

**L17.0** `Simple Sentence` (0.582) → `passthrough`
- original: Do not use venlafaxine if you have used an MAO inhibitor in the past 14 days.

**L17.1** `Simple Sentence` (0.94) → `passthrough`
- original: A dangerous drug interaction could occur.

**L17.2** `Simple Sentence` (0.954) → `passthrough`
- original: MAO inhibitors include isocarboxazid, linezolid, methylene blue injection, phenelzine, and tranylcypromine.

**L18.0** `Incomplete Sentence` (0.427) → `excluded_incomplete`
- original: Tell your doctor if you also use stimulant medicine, opioid medicine, herbal products, or medicine for depression, mental illness, Parkinson's disease, migraine headaches, serious infections, or prevention of nausea and vomiting.

**L18.1** `Simple Sentence` (0.989) → `passthrough`
- original: An interaction with venlafaxine could cause a serious condition called serotonin syndrome.

**L19.0** `Simple Sentence` (0.608) → `passthrough`
- original: To make sure venlafaxine is safe for you, tell your doctor if you have ever had:

**L20.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: bipolar disorder (manic depression);

**L21.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: heart disease, high blood pressure, high cholesterol or triglycerides, or a stroke;

**L22.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: diabetes;

**L23.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: lung disease;

**L24.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: glaucoma;

**L25.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a thyroid disorder;

**L26.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a seizure;

**L27.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: sexual problems;

**L28.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: bleeding problems;

**L29.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: low blood levels of sodium; or

**L30.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: liver or kidney disease.

**L31.0** `Simple Sentence` (0.532) → `passthrough`
- original: Some young people may have increased suicidal thoughts when first starting a medicine to treat depression.

**L31.1** `Incomplete Sentence` (0.9) → `excluded_incomplete`
- original: Stay alert to changes in your mood or symptoms.

**L31.2** `Simple Sentence` (0.957) → `passthrough`
- original: Your family or caregivers should also watch for sudden changes in your behavior.

**L32.0** `Compound Sentence` (0.964) → `decomposed`
- original: Taking this medicine during pregnancy could harm the baby, and taking it in the month before delivery may increase your risk of severe bleeding after childbirth.
- pronoun resolved: Taking this medicine during pregnancy could harm the baby, and taking venlafaxine in the month before delivery may increase your risk of severe bleeding after childbirth.
  - edits: “it” → “venlafaxine”
  - S1: Taking this medicine during pregnancy could harm the baby.
  - S2: Taking venlafaxine in the month before delivery may increase your risk of severe bleeding after childbirth.

**L32.1** `Simple Sentence` (0.964) → `passthrough`
- original: However, stopping the medicine may not be safe for you.
- pronoun resolved: However, stopping venlafaxine may not be safe for you.
  - edits: “the medicine” → “venlafaxine”

**L32.2** `Simple Sentence` (0.603) → `passthrough`
- original: Do not start or stop venlafaxine without asking your doctor.

**L33.0** `Complex Sentence` (0.636) → `decomposed`
- original: If you are pregnant, your name may be listed on a pregnancy registry to track the effects of venlafaxine on the baby.
  - S1: If you are pregnant, your name may be listed on a pregnancy registry.
  - S2: The registry is used to track the effects of venlafaxine on the baby.

**L34.0** `Incomplete Sentence` (0.971) → `excluded_incomplete`
- original: Ask a doctor if it is safe to breastfeed while using this medicine.
- pronoun resolved: Ask a doctor if it is safe to breastfeed while using venlafaxine.
  - edits: “this medicine.” → “venlafaxine.”

## How should I take venlafaxine?

**L37.0** `Incomplete Sentence` (0.976) → `excluded_incomplete`
- original: Take venlafaxine as prescribed by your doctor.

**L37.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L37.2** `Simple Sentence` (0.984) → `passthrough`
- original: Your doctor may occasionally change your dose.

**L38.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Take with food at the same time each day.

**L39.0** `Compound Sentence` (0.406) → `decomposed`
- original: Swallow the extended-release capsule or tablet whole and do not crush, chew, break, or open it.
  - S1: Swallow the extended-release capsule or tablet whole.
  - S2: Do not crush, chew, break, or open it.

**L40.0** `Simple Sentence` (0.729) → `passthrough`
- original: If you cannot swallow a capsule whole, open it and mix the medicine with applesauce.

**L40.1** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Swallow the mixture right away without chewing.

**L41.0** `Compound Sentence` (0.357) → `decomposed`
- original: Tell your doctor if you have any changes in sexual function, such as loss of interest in sex, trouble having an orgasm, or (in men) problems with erections or ejaculation.
  - S1: Tell your doctor if you have any changes in sexual function.
  - S2: Such changes include loss of interest in sex.
  - S3: Such changes include trouble having an orgasm.
  - S4: Such changes include problems with erections or ejaculation in men.

**L41.1** `Simple Sentence` (0.983) → `passthrough`
- original: Some sexual problems can be treated.

**L42.0** `Simple Sentence` (0.972) → `passthrough`
- original: Your symptoms may not improve for up to several weeks.

**L42.1** `Compound Sentence` (0.475) → `decomposed`
- original: Do not stop using venlafaxine suddenly, or you could have severe and long-lasting unpleasant symptoms (such as agitation, confusion, tingling or electric shock feelings, aggression, violent behavior, suicidal thoughts, vision changes, or increased blood pressure).
  - S1: Do not stop using venlafaxine suddenly.
  - S2: You could have severe and long-lasting unpleasant symptoms.
  - S3: These symptoms include agitation, confusion, tingling or electric shock feelings, aggression, violent behavior, suicidal thoughts, vision changes, or increased blood pressure.

**L42.2** `Incomplete Sentence` (0.812) → `excluded_incomplete`
- original: Ask your doctor before stopping the medicine.

**L43.0** `Simple Sentence` (0.972) → `passthrough`
- original: Your blood pressure and cholesterol levels may need to be checked often.

**L44.0** `Simple Sentence` (0.989) → `passthrough`
- original: This medicine may cause false results on a drug-screening urine test.

**L44.1** `Incomplete Sentence` (0.962) → `excluded_incomplete`
- original: Tell the laboratory staff that you use venlafaxine.

**L45.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Store at room temperature away from moisture and heat.

## Dosing Information

**L48.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Depression:

**L49.0** `Compound-Complex Sentence` (0.652) → `decomposed` · repaired
- original: Immediate release: -Initial dose: 37.5 mg orally twice a day OR 25 mg orally 3 times a day -Maintenance dose: 75 to 150 mg orally per day, given in divided doses -Maximum dose: ---Moderately depressed outpatients: 225 mg/day ---Severely depressed inpatients: 375 mg/day Extended release: -Initial dose: 75 mg orally once a day -Maintenance dose: 75 to 225 mg orally once a day -Maximum dose: ---Moderately depressed outpatients: 225 mg/day ---Severely depressed inpatients: 375 mg/day Comments: -The daily dosage of immediate-release formulations may be divided into 2 or 3 doses/day.
  - S1: The initial dose of the immediate-release formulation is 37.5 mg orally twice a day.
  - S2: The initial dose of the immediate-release formulation is 25 mg orally three times a day.
  - S3: The maintenance dose of the immediate-release formulation is 75 to 150 mg orally per day.
  - S4: The maintenance dose of the immediate-release formulation is given in divided doses.
  - S5: The maximum daily dose for moderately depressed outpatients on the immediate-release formulation is 225 mg.
  - S6: The maximum daily dose for severely depressed inpatients on the immediate-release formulation is 375 mg.
  - S7: The initial dose of the extended-release formulation is 75 mg orally once a day.
  - S8: The maintenance dose of the extended-release formulation is 75 to 225 mg orally once a day.
  - S9: The maximum daily dose for moderately depressed outpatients on the extended-release formulation is 225 mg.
  - S10: The maximum daily dose for severely depressed inpatients on the extended-release formulation is 375 mg.
  - S11: The daily dosage of immediate-release formulations may be divided into two doses per day.
  - S12: The daily dosage of immediate-release formulations may be divided into three doses per day.

**L49.1** `Complex Sentence` (0.937) → `decomposed`
- original: -Healthcare providers should consider initial extended release doses of 37.5 mg orally once a day for 4 to 7 days (before increasing the dose to 75 mg/day) in patients who may require additional time to adjust to the drug.
  - S1: Healthcare providers should consider initial extended release doses of 37.5 mg orally once a day for 4 to 7 days.
  - S2: This is for patients who may require additional time to adjust to the drug.
  - S3: After this period, the dose should be increased to 75 mg/day.

**L49.2** `Simple Sentence` (0.867) → `passthrough`
- original: -Doses may be increased in daily increments of up to 75 mg orally at intervals of no less than 4 days.

**L49.3** `Compound Sentence` (0.439) → `decomposed`
- original: -Patients should be periodically reassessed for the continued need of maintenance treatment and for the appropriate dose of treatment.
  - S1: Patients should be periodically reassessed for the continued need of maintenance treatment.
  - S2: Patients should be periodically reassessed for the appropriate dose of treatment.

**L49.4** `Simple Sentence` (0.972) → `passthrough`
- original: -Use of doses exceeding 225 mg/day is limited.

**L50.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Generalized Anxiety Disorder:

**L51.0** `Complex Sentence` (0.478) → `decomposed`
- original: Extended release: -Initial dose: 75 mg orally once a day -Maintenance dose: 75 to 225 mg orally once a day -Maximum dose: 225 mg/day Comments: -Healthcare providers should consider initial extended release doses of 37.5 mg orally once a day for 4 to 7 days (before increasing the dose to 75 mg/day) in patients who may require additional time to adjust to the drug.
  - S1: Extended release initial dose is 75 mg orally once a day.
  - S2: Extended release maintenance dose is 75 to 225 mg orally once a day.
  - S3: Extended release maximum dose is 225 mg/day.
  - S4: Healthcare providers should consider initial extended release doses of 37.5 mg orally once a day for 4 to 7 days.
  - S5: This consideration applies to patients who may require additional time to adjust to the drug.
  - S6: The dose should be increased to 75 mg/day after the initial period.

**L51.1** `Simple Sentence` (0.867) → `passthrough`
- original: -Doses may be increased in daily increments of up to 75 mg orally at intervals of no less than 4 days.

**L52.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Social Anxiety Disorder:

**L53.0** `Compound Sentence` (0.782) → `decomposed`
- original: Extended release: 75 mg orally once a day Comment: There is no evidence that doses greater than 75 mg/day confer additional benefit.
  - S1: Extended release: 75 mg orally once a day.
  - S2: There is no evidence that doses greater than 75 mg/day confer additional benefit.

**L54.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Panic Disorder:

**L55.0** `Complex Sentence` (0.484) → `decomposed`
- original: Extended release: -Initial dose: 37.5 mg orally once a day for 7 days, then 75 mg orally once a day thereafter -Maintenance dose: 75 to 225 mg orally once a day -Maximum dose: 225 mg/day Comment: Doses may be increased in daily increments of 75 mg orally at intervals of no less than 7 days.
  - S1: Extended release dosing is described.
  - S2: The initial dose is 37.5 mg orally once a day for 7 days.
  - S3: The dose is then 75 mg orally once a day thereafter.
  - S4: The maintenance dose is 75 to 225 mg orally once a day.
  - S5: The maximum dose is 225 mg/day.
  - S6: Doses may be increased in daily increments of 75 mg orally.
  - S7: Increments occur at intervals of no less than 7 days.

## What happens if I miss a dose?

**L58.0** `Compound Sentence` (0.591) → `decomposed`
- original: Take the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
- pronoun resolved: Take Venlafaxine as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - edits: “the medicine” → “Venlafaxine”
  - S1: Take Venlafaxine as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L58.1** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

## What happens if I overdose?

**L61.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

## What should I avoid while taking venlafaxine?

**L64.0** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Do not drink alcohol.

**L65.0** `Simple Sentence` (0.476) → `passthrough`
- original: Ask your doctor before taking a nonsteroidal anti-inflammatory drug (NSAID) such as aspirin, ibuprofen, naproxen, Advil, Aleve, Motrin, and others.

**L65.1** `Simple Sentence` (0.984) → `passthrough`
- original: Using an NSAID with venlafaxine may cause you to bruise or bleed easily.

**L66.0** `Incomplete Sentence` (0.962) → `excluded_incomplete`
- original: Avoid driving or hazardous activity until you know how venlafaxine will affect you.

**L66.1** `Simple Sentence` (0.878) → `passthrough`
- original: Your reactions could be impaired.

## Venlafaxine side effects

**L69.0** `Compound Sentence` (0.4) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to venlafaxine: hives; difficult breathing; swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to venlafaxine.
  - S2: Signs of an allergic reaction to venlafaxine include hives.
  - S3: Signs of an allergic reaction to venlafaxine include difficult breathing.
  - S4: Signs of an allergic reaction to venlafaxine include swelling of your face, lips, tongue, or throat.

**L70.0** `Compound-Complex Sentence` (0.564) → `decomposed` · repaired
- original: Tell your doctor right away if you have new or sudden changes in mood or behavior, including new or worse depression or anxiety, panic attacks, trouble sleeping, or if you feel impulsive, irritable, agitated, hostile, aggressive, restless, more active or talkative, or have thoughts about suicide or hurting yourself.
  - S1: Tell your doctor right away if you have new or sudden changes in mood or behavior.
  - S2: New or sudden changes in mood or behavior include new or worse depression.
  - S3: New or sudden changes in mood or behavior include new or worse anxiety.
  - S4: New or sudden changes in mood or behavior include panic attacks.
  - S5: New or sudden changes in mood or behavior include trouble sleeping.
  - S6: New or sudden changes in mood or behavior include feeling impulsive.
  - S7: New or sudden changes in mood or behavior include feeling irritable.
  - S8: New or sudden changes in mood or behavior include feeling agitated.
  - S9: New or sudden changes in mood or behavior include feeling hostile.
  - S10: New or sudden changes in mood or behavior include feeling aggressive.
  - S11: New or sudden changes in mood or behavior include feeling restless.
  - S12: New or sudden changes in mood or behavior include being more active.
  - S13: New or sudden changes in mood or behavior include being more talkative.
  - S14: New or sudden changes in mood or behavior include thoughts about suicide.
  - S15: New or sudden changes in mood or behavior include thoughts about hurting yourself.

**L71.0** `Simple Sentence` (0.989) → `passthrough`
- original: Venlafaxine may cause serious side effects.

**L71.1** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L72.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: blurred vision, eye pain or redness, seeing halos around lights;

**L73.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: cough, chest tightness, trouble breathing;

**L74.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a seizure (convulsions);

**L75.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: unusual bleeding - nosebleeds, bleeding gums, abnormal vaginal bleeding, any bleeding that will not stop;

**L76.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: low blood sodium - headache, confusion, problems with thinking or memory, weakness, feeling unsteady; or

**L77.0** `Incomplete Sentence` (0.669) → `excluded_incomplete`
- original: severe nervous system reaction - very stiff (rigid) muscles, high fever, sweating, confusion, fast or uneven heartbeats, tremors, feeling like you might pass out.

**L78.0** `Complex Sentence` (0.607) → `decomposed`
- original: Seek medical attention right away if you have symptoms of serotonin syndrome, such as: agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness, twitching, loss of coordination, nausea, vomiting, or diarrhea.
  - S1: Seek medical attention right away if you have symptoms of serotonin syndrome.
  - S2: Symptoms of serotonin syndrome include agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness, twitching, loss of coordination, nausea, vomiting, or diarrhea.

**L79.0** `Simple Sentence` (0.962) → `passthrough`
- original: Common venlafaxine side effects may include:

**L80.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: headache, dizziness, drowsiness, tiredness;

**L81.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: ringing in your ears, feeling anxious, nervous, or jittery;

**L82.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: sleep problems, unusual dreams;

**L83.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: tremors;

**L84.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: fast heartbeats;

**L85.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: blurred vision;

**L86.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: nausea, vomiting, diarrhea, constipation;

**L87.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: changes in weight or appetite;

**L88.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: dry mouth, yawning;

**L89.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: increased sweating; or

**L90.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: sexual problems.

**L91.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L91.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L91.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## What other drugs will affect venlafaxine?

**L94.0** `Simple Sentence` (0.978) → `passthrough`
- original: Using venlafaxine with other drugs that make you drowsy can worsen this effect.

**L94.1** `Incomplete Sentence` (0.573) → `excluded_incomplete`
- original: Ask your doctor before using opioid medication, a sleeping pill, a muscle relaxer, or medicine for anxiety or seizures.

**L95.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Tell your doctor about all your current medicines.

**L95.1** `Simple Sentence` (0.99) → `passthrough`
- original: Many drugs can affect venlafaxine, especially:

**L96.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: any other antidepressant, or other medicines containing venlafaxine or desvenlafaxine;

**L97.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: amphetamines;

**L98.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: fentanyl;

**L99.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: cimetidine;

**L100.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: tramadol;

**L101.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: St. John's wort, tryptophan (sometimes called L-tryptophan);

**L102.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: diet pills, weight loss medicine (such as phentermine);

**L103.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: a blood thinner (warfarin, Coumadin, Jantoven);

**L104.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: medicine to treat mood disorders, thought disorders, or mental illness - buspirone, lithium, and many others; or

**L105.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: migraine headache medicine - sumatriptan, zolmitriptan, and others.

**L106.0** `Simple Sentence` (0.725) → `passthrough`
- original: This list is not complete and many other drugs may interact with venlafaxine.

**L106.1** `Incomplete Sentence` (0.491) → `excluded_incomplete`
- original: This includes prescription and over-the-counter medicines, vitamins, and herbal products.
- pronoun resolved: List includes prescription and over-the-counter medicines, vitamins, and herbal products.
  - edits: “This” → “List”

**L106.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.

## Popular FAQ

**L109.0** `Incomplete Sentence` (0.936) → `excluded_incomplete`
- original: Q: How long do venlafaxine withdrawal symptoms last?

**L109.1** `Compound Sentence` (0.755) → `decomposed`
- original: A: Venlafaxine withdrawal symptoms typically last up to 1 to 4 weeks, but may persist even longer.
  - S1: Venlafaxine withdrawal symptoms typically last up to 1 to 4 weeks.
  - S2: They may persist even longer.

**L109.2** `Simple Sentence` (0.96) → `passthrough`
- original: The timing varies widely.

**L109.3** `Simple Sentence` (0.4) → `passthrough`
- original: People who stop suddenly, took higher doses, or used venlafaxine for years may have symptoms for two to three months or longer.

**L110.0** `Incomplete Sentence` (0.958) → `excluded_incomplete`
- original: Q: What drugs can cause serotonin syndrome?

**L110.1** `Complex Sentence` (0.807) → `decomposed`
- original: A: Common drug classes that can cause serotonin syndrome include selective serotonin reuptake inhibitors (SSRIs), monoamine oxidase inhibitors (MAOIs), and opioids like tramadol.
  - S1: Common drug classes that can cause serotonin syndrome include selective serotonin reuptake inhibitors (SSRIs), monoamine oxidase inhibitors (MAOIs), and opioids like tramadol.
