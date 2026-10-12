# Escitalopram — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/escitalopram.txt` · 120 sentences · 9 changed by pronoun resolution · 197 sentences sent to EDC

## What is escitalopram?

**L5.0** `Simple Sentence` (0.962) → `passthrough`
- original: Escitalopram is an antidepressant belonging to a group of drugs called selective serotonin reuptake inhibitors (SSRIs).

**L5.1** `Simple Sentence` (0.895) → `passthrough`
- original: It affects chemicals in the brain that may be unbalanced in people with depression or anxiety.
- pronoun resolved: Escitalopram affects chemicals in the brain that may be unbalanced in people with depression or anxiety.
  - edits: “It” → “Escitalopram”

**L6.0** `Simple Sentence` (0.973) → `passthrough`
- original: Escitalopram is used to treat major depressive disorder in adults and adolescents at least 12 years old.

**L7.0** `Simple Sentence` (0.958) → `passthrough`
- original: Escitalopram is also used to treat anxiety in adults and children at least 7 years old.

## Warnings

**L10.0** `Simple Sentence` (0.954) → `passthrough`
- original: You should not use escitalopram you also take pimozide or citalopram (Celexa).

**L11.0** `Compound Sentence` (0.555) → `decomposed`
- original: Do not use escitalopram within 14 days before or 14 days after you have used an MAO inhibitor, such as isocarboxazid, linezolid, methylene blue injection, phenelzine, rasagiline, selegiline, or tranylcypromine.
  - S1: Do not use escitalopram within 14 days before you have used an MAO inhibitor.
  - S2: Do not use escitalopram within 14 days after you have used an MAO inhibitor.
  - S3: Examples of MAO inhibitors include isocarboxazid, linezolid, methylene blue injection, phenelzine, rasagiline, selegiline, and tranylcypromine.

**L12.0** `Simple Sentence` (0.982) → `passthrough`
- original: Some young people have thoughts about suicide when first taking an antidepressant.

**L12.1** `Incomplete Sentence` (0.9) → `excluded_incomplete`
- original: Stay alert to changes in your mood or symptoms.

**L12.2** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Report any new or worsening symptoms to your doctor.

**L13.0** `Complex Sentence` (0.607) → `decomposed`
- original: Seek medical attention right away if you have symptoms of serotonin syndrome, such as: agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness, twitching, loss of coordination, nausea, vomiting, or diarrhea.
  - S1: Seek medical attention right away if you have symptoms of serotonin syndrome.
  - S2: Symptoms of serotonin syndrome include agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness, twitching, loss of coordination, nausea, vomiting, or diarrhea.

**L14.0** `Simple Sentence` (0.658) → `passthrough`
- original: Do not stop using escitalopram without first asking your doctor.

## Before taking this medicine

**L17.0** `Simple Sentence` (0.63) → `passthrough`
- original: You should not use this medicine if you are allergic to escitalopram or citalopram (Celexa), or if:
- pronoun resolved: You should not use Escitalopram if you are allergic to escitalopram or citalopram (Celexa), or if:
  - edits: “this medicine” → “Escitalopram”

**L18.0** `Simple Sentence` (0.974) → `passthrough`
- original: you also take pimozide.

**L19.0** `Incomplete Sentence` (0.541) → `excluded_incomplete`
- original: Do not use escitalopram within 14 days before or 14 days after you have used an MAO inhibitor.

**L19.1** `Simple Sentence` (0.94) → `passthrough`
- original: A dangerous drug interaction could occur.

**L19.2** `Simple Sentence` (0.925) → `passthrough`
- original: MAO inhibitors include isocarboxazid, linezolid, phenelzine, rasagiline, selegiline, and tranylcypromine.

**L20.0** `Complex Sentence` (0.456) → `decomposed`
- original: Be sure your doctor knows if you also take stimulant medicine, opioid medicine, herbal products, or medicine for depression, mental illness, Parkinson's disease, migraine headaches, serious infections, or prevention of nausea and vomiting.
  - S1: Be sure your doctor knows if you also take stimulant medicine.
  - S2: Be sure your doctor knows if you also take opioid medicine.
  - S3: Be sure your doctor knows if you also take herbal products.
  - S4: Be sure your doctor knows if you also take medicine for depression.
  - S5: Be sure your doctor knows if you also take medicine for mental illness.
  - S6: Be sure your doctor knows if you also take medicine for Parkinson's disease.
  - S7: Be sure your doctor knows if you also take medicine for migraine headaches.
  - S8: Be sure your doctor knows if you also take medicine for serious infections.
  - S9: Be sure your doctor knows if you also take medicine for prevention of nausea and vomiting.

**L20.1** `Complex Sentence` (0.699) → `decomposed`
- original: These medicines may interact with escitalopram and cause a serious condition called serotonin syndrome.
- pronoun resolved: Stimulant medicine, opioid medicine, herbal products, or medicine may interact with escitalopram and cause a serious condition called serotonin syndrome.
  - edits: “These medicines” → “Stimulant medicine, opioid medicine, herbal products, or medicine”
  - S1: Stimulant medicine, opioid medicine, herbal products, or medicine may interact with escitalopram.
  - S2: This interaction may cause a serious condition called serotonin syndrome.

**L21.0** `Simple Sentence` (0.717) → `passthrough`
- original: To make sure escitalopram is safe for you, tell your doctor if you have ever had:

**L22.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: liver or kidney disease;

**L23.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: seizures;

**L24.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: low levels of sodium in your blood;

**L25.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: heart disease, high blood pressure;

**L26.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a stroke;

**L27.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: bleeding problems;

**L28.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: sexual problems;

**L29.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: bipolar disorder (manic depression); or

**L30.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: drug addiction or suicidal thoughts.

**L31.0** `Simple Sentence` (0.982) → `passthrough`
- original: Some young people have thoughts about suicide when first taking an antidepressant.

**L31.1** `Simple Sentence` (0.977) → `passthrough`
- original: Your doctor should check your progress at regular visits.

**L31.2** `Simple Sentence` (0.57) → `passthrough`
- original: Your family or other caregivers should also be alert to changes in your mood or symptoms.

**L32.0** `Simple Sentence` (0.987) → `passthrough`
- original: Escitalopram is not approved for use by anyone younger than 7 years old.

**L33.0** `Incomplete Sentence` (0.885) → `excluded_incomplete`
- original: Ask your doctor about taking this medicine if you are pregnant.
- pronoun resolved: Ask your doctor about taking Escitalopram if you are pregnant.
  - edits: “this medicine” → “Escitalopram”

**L33.1** `Compound Sentence` (0.969) → `decomposed`
- original: Taking an SSRI antidepressant during late pregnancy may cause serious medical complications in the baby, and may increase your risk of heavy bleeding after delivery.
  - S1: Taking an SSRI antidepressant during late pregnancy may cause serious medical complications in the baby.
  - S2: It may increase your risk of heavy bleeding after delivery.

**L33.2** `Compound Sentence` (0.342) → `decomposed`
- original: However, you may have a relapse of depression if you stop taking your antidepressant.
  - S1: However, you may have a relapse of depression.
  - S2: This happens if you stop taking your antidepressant.

**L33.3** `Incomplete Sentence` (0.861) → `excluded_incomplete`
- original: Tell your doctor right away if you become pregnant.

**L33.4** `Simple Sentence` (0.748) → `passthrough`
- original: Do not start or stop taking this medicine without your doctor's advice.
- pronoun resolved: Do not start or stop taking Escitalopram without your doctor's advice.
  - edits: “this medicine” → “Escitalopram”

**L34.0** `Complex Sentence` (0.681) → `decomposed`
- original: If you are pregnant, your name may be listed on a pregnancy registry to track the effects of escitalopram on the baby.
  - S1: If you are pregnant, your name may be listed on a pregnancy registry.
  - S2: The registry tracks the effects of escitalopram on the baby.

**L35.0** `Complex Sentence` (0.489) → `decomposed`
- original: If you are breastfeeding, tell your doctor if you notice drowsiness, agitation, feeding problems, or poor weight gain in the nursing baby.
  - S1: If you are breastfeeding, tell your doctor.
  - S2: Tell your doctor if you notice drowsiness, agitation, feeding problems, or poor weight gain in the nursing baby.
  - S3: The symptoms to report are drowsiness, agitation, feeding problems, or poor weight gain in the nursing baby.

## How should I take escitalopram?

**L38.0** `Incomplete Sentence` (0.973) → `excluded_incomplete`
- original: Take escitalopram exactly as prescribed by your doctor.

**L38.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L38.2** `Simple Sentence` (0.984) → `passthrough`
- original: Your doctor may occasionally change your dose.

**L39.0** `Incomplete Sentence` (0.967) → `excluded_incomplete`
- original: Take escitalopram at the same time each day, with or without food.

**L40.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Measure liquid medicine carefully.

**L40.1** `Incomplete Sentence` (0.955) → `excluded_incomplete`
- original: Use the dosing syringe provided, or use a medicine dose-measuring device (not a kitchen spoon).

**L41.0** `Simple Sentence` (0.969) → `passthrough`
- original: It may take up to 4 weeks before your symptoms improve.

**L41.1** `Compound Sentence` (0.416) → `decomposed`
- original: Keep using the medication as directed and tell your doctor if your symptoms do not improve.
- pronoun resolved: Keep using escitalopram as directed and tell your doctor if your symptoms do not improve.
  - edits: “the medication” → “escitalopram”
  - S1: Keep using escitalopram as directed.
  - S2: Tell your doctor if your symptoms do not improve.

**L42.0** `Compound Sentence` (0.357) → `decomposed`
- original: Tell your doctor if you have any changes in sexual function, such as loss of interest in sex, trouble having an orgasm, or (in men) problems with erections or ejaculation.
  - S1: Tell your doctor if you have any changes in sexual function.
  - S2: Such changes include loss of interest in sex.
  - S3: Such changes include trouble having an orgasm.
  - S4: Such changes include problems with erections or ejaculation in men.

**L42.1** `Simple Sentence` (0.983) → `passthrough`
- original: Some sexual problems can be treated.

**L43.0** `Simple Sentence` (0.946) → `passthrough`
- original: Your doctor will need to check your progress on a regular basis.

**L43.1** `Simple Sentence` (0.976) → `passthrough`
- original: A child taking escitalopram should be checked for height and weight gain.

**L44.0** `Compound Sentence` (0.746) → `decomposed`
- original: Do not stop using escitalopram suddenly, or you could have unpleasant withdrawal symptoms.
  - S1: Do not stop using escitalopram suddenly.
  - S2: You could have unpleasant withdrawal symptoms.

**L44.1** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Follow your doctor's instructions about tapering your dose.

**L45.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: Store escitalopram at room temperature away from moisture and heat.

## Dosing information

**L48.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Generalized Anxiety Disorder:

**L49.0** `Compound-Complex Sentence` (0.799) → `decomposed`
- original: Initial dose: 10 mg orally once a day; increase if necessary after at least 1 week of treatment to 20 mg once a day Maintenance dose: 10 to 20 mg orally once a day Maximum dose: 20 mg orally once a day Comment: Treatment should be periodically reassessed to determine the need for ongoing treatment; efficacy beyond 8 weeks has not been systematically studied.
  - S1: The initial dose is 10 mg orally once a day.
  - S2: The dose may be increased if necessary after at least 1 week of treatment.
  - S3: The increased dose is 20 mg once a day.
  - S4: The maintenance dose is 10 to 20 mg orally once a day.
  - S5: The maximum dose is 20 mg orally once a day.
  - S6: Treatment should be periodically reassessed.
  - S7: The reassessment determines the need for ongoing treatment.
  - S8: Efficacy beyond 8 weeks has not been systematically studied.

**L49.1** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Use: Acute treatment of generalized anxiety disorder

**L50.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Depression:

**L51.0** `Complex Sentence` (0.463) → `decomposed`
- original: Initial dose: 10 mg orally once a day; increase if necessary after at least 1 week of treatment to 20 mg once a day Maintenance dose: 10 to 20 mg orally once a day Maximum dose: 20 mg orally once a day Comments: -Acute episodes may require several months or longer of sustained pharmacological therapy beyond response to the acute episode.
  - S1: Initial dose: 10 mg orally once a day.
  - S2: Increase the dose if necessary after at least 1 week of treatment to 20 mg once a day.
  - S3: Maintenance dose: 10 to 20 mg orally once a day.
  - S4: Maximum dose: 20 mg orally once a day.
  - S5: Acute episodes may require several months or longer of sustained pharmacological therapy beyond response to the acute episode.

**L51.1** `Simple Sentence` (0.941) → `passthrough`
- original: -Patients should be periodically reassessed to determine the need for maintenance treatment.

**L51.2** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Use: Acute and maintenance treatment of major depressive disorder

**L52.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Geriatric Dose for Depression:

**L53.0** `Incomplete Sentence` (0.935) → `excluded_incomplete`
- original: Recommended dose: 10 mg orally once a day Use: Acute and maintenance treatment of major depressive disorder

**L54.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Pediatric Dose for Depression:

**L55.0** `Complex Sentence` (0.577) → `decomposed`
- original: 12 years and older: -Initial dose: 10 mg orally once a day; increase if necessary after at least 3 weeks of treatment to 20 mg once a day -Maintenance dose: 10 to 20 mg orally once a day -Maximum dose: 20 mg orally once a day Comments: -Acute episodes may require several months or longer of sustained pharmacological therapy beyond response to the acute episode.
  - S1: This recommendation applies to individuals 12 years and older.
  - S2: The initial dose is 10 mg orally once a day.
  - S3: The dose may be increased to 20 mg once a day if necessary after at least 3 weeks of treatment.
  - S4: The maintenance dose is 10 to 20 mg orally once a day.
  - S5: The maximum dose is 20 mg orally once a day.
  - S6: Acute episodes may require several months or longer of sustained pharmacological therapy beyond response to the acute episode.

**L55.1** `Simple Sentence` (0.941) → `passthrough`
- original: -Patients should be periodically reassessed to determine the need for maintenance treatment.

**L55.2** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Use: Acute and maintenance treatment of major depressive disorder

## What happens if I miss a dose?

**L58.0** `Compound Sentence` (0.555) → `decomposed`
- original: Take the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - S1: Take the medicine as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L58.1** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

## What happens if I overdose?

**L61.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

## What to avoid

**L64.0** `Simple Sentence` (0.366) → `passthrough`
- original: Ask your doctor before taking a nonsteroidal anti-inflammatory drug (NSAID) such as aspirin, ibuprofen (Advil, Motrin), naproxen (Aleve), celecoxib (Celebrex), diclofenac, indomethacin, meloxicam, and others.

**L64.1** `Simple Sentence` (0.985) → `passthrough`
- original: Using an NSAID with escitalopram may cause you to bruise or bleed easily.

**L65.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Avoid alcohol.

**L66.0** `Incomplete Sentence` (0.957) → `excluded_incomplete`
- original: Avoid driving or hazardous activity until you know how escitalopram will affect you.

**L66.1** `Simple Sentence` (0.878) → `passthrough`
- original: Your reactions could be impaired.

## Escitalopram side effects

**L69.0** `Compound Sentence` (0.459) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to escitalopram: skin rash or hives; difficulty breathing; swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to escitalopram.
  - S2: These signs include a skin rash or hives.
  - S3: These signs also include difficulty breathing.
  - S4: These signs also include swelling of your face, lips, tongue, or throat.

**L70.0** `Compound-Complex Sentence` (0.427) → `decomposed`
- original: Report any new or worsening symptoms to your doctor, such as: mood or behavior changes, anxiety, panic attacks, trouble sleeping, or if you feel impulsive, irritable, agitated, hostile, aggressive, restless, hyperactive (mentally or physically), more depressed, or have thoughts about suicide or hurting yourself.
  - S1: Report any new or worsening symptoms to your doctor.
  - S2: Mood or behavior changes are new or worsening symptoms.
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

**L71.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L72.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: blurred vision, tunnel vision, eye pain or swelling, or seeing halos around lights;

**L73.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: racing thoughts, unusual risk-taking behavior, feelings of extreme happiness or sadness;

**L74.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: pain or burning when you urinate;

**L75.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: (in a child taking escitalopram) slow growth or weight gain;

**L76.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: low levels of sodium in the body - headache, confusion, slurred speech, severe weakness, vomiting, loss of coordination, feeling unsteady; or

**L77.0** `Incomplete Sentence` (0.669) → `excluded_incomplete`
- original: severe nervous system reaction - very stiff (rigid) muscles, high fever, sweating, confusion, fast or uneven heartbeats, tremors, feeling like you might pass out.

**L78.0** `Complex Sentence` (0.607) → `decomposed`
- original: Seek medical attention right away if you have symptoms of serotonin syndrome, such as: agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness, twitching, loss of coordination, nausea, vomiting, or diarrhea.
  - S1: Seek medical attention right away if you have symptoms of serotonin syndrome.
  - S2: Symptoms of serotonin syndrome include agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness, twitching, loss of coordination, nausea, vomiting, or diarrhea.

**L79.0** `Simple Sentence` (0.946) → `passthrough`
- original: Common escitalopram side effects may include:

**L80.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: painful urination;

**L81.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: dizziness, drowsiness, tiredness, weakness;

**L82.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: feeling anxious or agitated;

**L83.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: increased muscle movements, feeling shaky;

**L84.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: sleep problems (insomnia);

**L85.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: sweating, dry mouth, increased thirst, loss of appetite;

**L86.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: nausea, constipation;

**L87.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: yawning;

**L88.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: nosebleed, heavy menstrual periods; or

**L89.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: decreased sex drive, impotence, or difficulty having an orgasm.

**L90.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L90.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L90.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## What other drugs will affect escitalopram?

**L93.0** `Simple Sentence` (0.977) → `passthrough`
- original: Using escitalopram with other drugs that make you drowsy can worsen this effect.

**L93.1** `Incomplete Sentence` (0.573) → `excluded_incomplete`
- original: Ask your doctor before using opioid medication, a sleeping pill, a muscle relaxer, or medicine for anxiety or seizures.

**L94.0** `Incomplete Sentence` (0.666) → `excluded_incomplete`
- original: Tell your doctor about all your current medicines, especially a blood thinner such as warfarin, Coumadin, or Jantoven.

**L95.0** `Compound Sentence` (0.966) → `decomposed`
- original: Many drugs may interact with escitalopram, and some drugs should not be used at the same time.
  - S1: Many drugs may interact with escitalopram.
  - S2: Some drugs should not be used at the same time.

**L95.1** `Incomplete Sentence` (0.904) → `excluded_incomplete`
- original: Tell your doctor about all your current medicines and any medicine you start or stop using.

**L95.2** `Simple Sentence` (0.849) → `passthrough`
- original: This includes prescription and over-the-counter medicines, vitamins, and herbal products.

**L95.3** `Simple Sentence` (0.949) → `passthrough`
- original: Not all possible interactions are listed here.

## Popular FAQ

**L98.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Q: Why does Lexapro (escitalopram) cause weight gain?

**L98.1** `Compound-Complex Sentence` (0.802) → `decomposed`
- original: Complete Patient Guide A: Lexapro weight gain affects up 25 % to 41% of patients who take this antidepressant medication, although weight gain tends to be minimal, with an average gain of approximately 1 % to 3.7%.
  - S1: Complete Patient Guide A discusses Lexapro weight gain.
  - S2: Lexapro weight gain affects up to 25% of patients who take this antidepressant medication.
  - S3: Lexapro weight gain affects up to 41% of patients who take this antidepressant medication.
  - S4: Although weight gain tends to be minimal, with an average gain of approximately 1% to 3.7%.

**L98.2** `Complex Sentence` (0.641) → `decomposed`
- original: The weight gain associated with Lexapro occurs primarily due to the drug's mechanism of action on serotonin levels in the brain.
  - S1: The weight gain associated with Lexapro occurs primarily due to the drug's mechanism of action.
  - S2: The mechanism of action involves serotonin levels in the brain.

**L98.3** `Compound-Complex Sentence` (0.907) → `decomposed`
- original: When Lexapro blocks the serotonin transporter, it successfully increases serotonin availability to help treat depression and anxiety, but this same action can trigger unwanted changes in appetite and metabolism.
- pronoun resolved: When Lexapro blocks the serotonin transporter, Lexapro successfully increases serotonin availability to help treat depression and anxiety, but this same action can trigger unwanted changes in appetite and metabolism.
  - edits: “it” → “Lexapro”
  - S1: Lexapro blocks the serotonin transporter.
  - S2: Lexapro increases serotonin availability.
  - S3: Increased serotonin availability helps treat depression and anxiety.
  - S4: Lexapro's action can trigger unwanted changes in appetite and metabolism.

**L99.0** `Simple Sentence` (0.569) → `passthrough`
- original: Q: When's the best time to take Lexapro (escitalopram) - Morning or Night?

**L99.1** `Simple Sentence` (0.818) → `passthrough`
- original: A: Lexapro (escitalopram) is usually taken once a day and can be taken either in the morning or at night.

**L100.0** `Incomplete Sentence` (0.974) → `excluded_incomplete`
- original: Q: How long does it take for Lexapro (escitalopram) to work?

**L100.1** `Complex Sentence` (0.938) → `decomposed`
- original: A: Even though it takes Lexapro only a few hours to increase serotonin levels within the brain, it may take several weeks to start working.
- pronoun resolved: A: Even though Lexapro takes Lexapro only a few hours to increase serotonin levels within the brain, Lexapro may take several weeks to start working.
  - edits: “it” → “Lexapro”; “it” → “Lexapro”
  - S1: Lexapro may take several weeks to start working.
  - S2: Lexapro increases serotonin levels within the brain.
  - S3: Lexapro takes only a few hours to increase serotonin levels within the brain.

**L100.2** `Simple Sentence` (0.923) → `passthrough`
- original: Signs that Lexapro has started working include an improvement in your sleep, energy, or appetite.

**L100.3** `Simple Sentence` (0.975) → `passthrough`
- original: In some, this may happen in as little as 1 to 2 weeks.

**L100.4** `Complex Sentence` (0.745) → `decomposed`
- original: Relief from symptoms, such as a depressed mood or a lack of interest in activities you used to enjoy, may take up to 6 to 8 weeks to fully improve.
  - S1: Relief from symptoms may take up to 6 to 8 weeks to fully improve.
  - S2: The symptoms include a depressed mood.
  - S3: The symptoms include a lack of interest in activities you used to enjoy.

**L101.0** `Incomplete Sentence` (0.945) → `excluded_incomplete`
- original: Q: Does Lexapro (escitalopram) cause night sweats?

**L101.1** `Compound-Complex Sentence` (0.511) → `decomposed`
- original: A: Lexapro can cause night sweats and increased sweating overall (night and day) was one of the most common side effects reported with Lexapro, reported by 3% to 8% (depending on the dose) of people.
  - S1: Lexapro can cause night sweats.
  - S2: Lexapro can cause increased sweating overall.
  - S3: Increased sweating occurs both at night and during the day.
  - S4: Increased sweating was one of the most common side effects reported with Lexapro.
  - S5: Between 3% and 8% of people reported increased sweating as a side effect.
  - S6: The percentage of people reporting increased sweating depends on the dose.

**L101.2** `Complex Sentence` (0.96) → `decomposed`
- original: Although night sweats can be worrisome, they usually diminish with time as your body and brain adjust to the medication.
- pronoun resolved: Although night sweats can be worrisome, night sweats usually diminish with time as your body and brain adjust to the medication.
  - edits: “they” → “night sweats”
  - S1: Night sweats can be worrisome.
  - S2: Night sweats usually diminish with time.
  - S3: Your body and brain adjust to the medication.
