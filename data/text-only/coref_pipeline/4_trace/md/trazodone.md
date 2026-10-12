# Trazodone — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/trazodone.txt` · 130 sentences · 20 changed by pronoun resolution · 206 sentences sent to EDC

## What is trazodone?

**L5.0** `Simple Sentence` (0.948) → `passthrough`
- original: Trazodone is an antidepressant that belongs to a group of drugs called serotonin receptor antagonists and reuptake inhibitors (SARIs).

**L5.1** `Complex Sentence` (0.945) → `decomposed`
- original: While trazodone is not a true member of the selective serotonin reuptake inhibitors (SSRIs) class of antidepressants, it does still share many properties of the SSRIs.
- pronoun resolved: While trazodone is not a true member of the selective serotonin reuptake inhibitors (SSRIs) class of antidepressants, Trazodone does still share many properties of the SSRIs.
  - edits: “it” → “Trazodone”
  - S1: Trazodone is not a true member of the selective serotonin reuptake inhibitors (SSRIs) class of antidepressants.
  - S2: Trazodone shares many properties of the SSRIs.

**L6.0** `Simple Sentence` (0.99) → `passthrough`
- original: Trazodone is used to treat major depressive disorder.

**L7.0** `Complex Sentence` (0.64) → `decomposed`
- original: It may help to improve your mood, appetite, and energy level as well as decrease anxiety and insomnia related to depression.
- pronoun resolved: Trazodone may help to improve your mood, appetite, and energy level as well as decrease anxiety and insomnia related to depression.
  - edits: “It” → “Trazodone”
  - S1: Trazodone may help to improve your mood.
  - S2: Trazodone may help to improve your appetite.
  - S3: Trazodone may help to improve your energy level.
  - S4: Trazodone may help to decrease anxiety related to depression.
  - S5: Trazodone may help to decrease insomnia related to depression.

**L8.0** `Simple Sentence` (0.84) → `passthrough`
- original: Trazodone works by helping to restore the balance of a certain natural chemical (serotonin) in the brain.

## Warnings

**L11.0** `Compound Sentence` (0.591) → `decomposed`
- original: You should not use trazodone if you are allergic to it, or if you are being treated with methylene blue injection.
- pronoun resolved: You should not use trazodone if you are allergic to trazodone, or if you are being treated with methylene blue injection.
  - edits: “it,” → “trazodone,”
  - S1: You should not use trazodone if you are allergic to trazodone.
  - S2: You should not use trazodone if you are being treated with methylene blue injection.

**L12.0** `Simple Sentence` (0.78) → `passthrough`
- original: Do not use this medicine if you have taken an MAO inhibitor in the past 14 days.
- pronoun resolved: Do not use trazodone if you have taken an MAO inhibitor in the past 14 days.
  - edits: “this medicine” → “trazodone”

**L12.1** `Simple Sentence` (0.94) → `passthrough`
- original: A dangerous drug interaction could occur.

**L12.2** `Simple Sentence` (0.967) → `passthrough`
- original: MAO inhibitors include isocarboxazid, linezolid, phenelzine, tranylcypromine and others.

**L13.0** `Simple Sentence` (0.982) → `passthrough`
- original: Some young people have thoughts about suicide when first taking an antidepressant.

**L13.1** `Simple Sentence` (0.937) → `passthrough`
- original: Your doctor will need to check your progress at regular visits while you are using trazodone.

**L13.2** `Simple Sentence` (0.57) → `passthrough`
- original: Your family or other caregivers should also be alert to changes in your mood or symptoms.

**L14.0** `Compound-Complex Sentence` (0.427) → `decomposed`
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

**L15.0** `Incomplete Sentence` (0.584) → `excluded_incomplete`
- original: Do not give this medicine to anyone younger than 18 years old without the advice of a doctor.
- pronoun resolved: Do not give trazodone to anyone younger than 18 years old without the advice of a doctor.
  - edits: “this medicine” → “trazodone”

**L15.1** `Simple Sentence` (0.991) → `passthrough`
- original: Trazodone is not approved for use in children.

## Before taking this medicine

**L18.0** `Simple Sentence` (0.988) → `passthrough`
- original: You should not use trazodone if you are allergic to it.
- pronoun resolved: You should not use trazodone if you are allergic to trazodone.
  - edits: “it.” → “trazodone.”

**L19.0** `Simple Sentence` (0.682) → `passthrough`
- original: Do not use this medicine if you have used an MAO inhibitor in the past 14 days.
- pronoun resolved: Do not use Trazodone if you have used an MAO inhibitor in the past 14 days.
  - edits: “this medicine” → “Trazodone”

**L19.1** `Simple Sentence` (0.94) → `passthrough`
- original: A dangerous drug interaction could occur.

**L19.2** `Simple Sentence` (0.934) → `passthrough`
- original: MAO inhibitors include isocarboxazid, linezolid, methylene blue injection, phenelzine, tranylcypromine, and others.

**L20.0** `Simple Sentence` (0.381) → `passthrough`
- original: After you stop taking trazodone, you must wait at least 14 days before you start taking an MAOI.

**L21.0** `Incomplete Sentence` (0.384) → `excluded_incomplete`
- original: Tell your doctor if you also take stimulant medicine, opioid medicine, herbal products, or medicine for depression, mental illness, Parkinson's disease, migraine headaches, serious infections, or prevention of nausea and vomiting.

**L21.1** `Simple Sentence` (0.989) → `passthrough`
- original: An interaction with trazodone could cause a serious condition called serotonin syndrome.

**L22.0** `Simple Sentence` (0.59) → `passthrough`
- original: To make sure this medicine is safe for you, tell your doctor if you have ever had:

**L23.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: liver or kidney disease;

**L24.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: heart disease, or a recent heart attack;

**L25.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a bleeding or blood clotting disorder;

**L26.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: seizures or epilepsy;

**L27.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: narrow-angle glaucoma;

**L28.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: long QT syndrome;

**L29.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: drug addiction or suicidal thoughts; or

**L30.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: bipolar disorder (manic depression).

**L31.0** `Simple Sentence` (0.982) → `passthrough`
- original: Some young people have thoughts about suicide when first taking an antidepressant.

**L31.1** `Simple Sentence` (0.977) → `passthrough`
- original: Your doctor should check your progress at regular visits.

**L31.2** `Simple Sentence` (0.57) → `passthrough`
- original: Your family or other caregivers should also be alert to changes in your mood or symptoms.

**L32.0** `Compound Sentence` (0.956) → `decomposed`
- original: Taking trazodone during pregnancy could harm the baby, but stopping the medicine may not be safe for you.
  - S1: Taking trazodone during pregnancy could harm the baby.
  - S2: Stopping the medicine may not be safe for you.

**L32.1** `Simple Sentence` (0.666) → `passthrough`
- original: Do not start or stop this medicine without asking your doctor.
- pronoun resolved: Do not start or stop Trazodone without asking your doctor.
  - edits: “this medicine” → “Trazodone”

**L33.0** `Complex Sentence` (0.683) → `decomposed`
- original: If you are pregnant, your name may be listed on a pregnancy registry to track the effects of trazodone on the baby.
  - S1: If you are pregnant, your name may be listed on a pregnancy registry.
  - S2: The registry tracks the effects of trazodone on the baby.

**L34.0** `Simple Sentence` (0.988) → `passthrough`
- original: It may not be safe to breast-feed while using this medicine.
- pronoun resolved: Trazodone may not be safe to breast-feed while using Trazodone.
  - edits: “It” → “Trazodone”; “this medicine.” → “Trazodone.”

**L34.1** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Ask your doctor about any risk.

**L35.0** `Simple Sentence` (0.988) → `passthrough`
- original: Trazodone is not approved for use by anyone younger than 18 years old.

## How should I take trazodone?

**L38.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Take trazodone exactly as prescribed by your doctor.

**L38.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L38.2** `Simple Sentence` (0.984) → `passthrough`
- original: Your doctor may occasionally change your dose.

**L39.0** `Incomplete Sentence` (0.973) → `excluded_incomplete`
- original: Take trazodone after a meal or a snack.

**L40.0** `Simple Sentence` (0.978) → `passthrough`
- original: It may take up to 2 weeks before your symptoms improve.
- pronoun resolved: Trazodone may take up to 2 weeks before your symptoms improve.
  - edits: “It” → “Trazodone”

**L40.1** `Compound Sentence` (0.517) → `decomposed`
- original: Keep using the medication as directed and tell your doctor if your symptoms do not improve.
  - S1: Keep using the medication as directed.
  - S2: Tell your doctor if your symptoms do not improve.

**L41.0** `Compound Sentence` (0.898) → `decomposed`
- original: You should not stop using this medicine suddenly, or you could have unpleasant symptoms (such as dizziness, vomiting, agitation, sweating, confusion, numbness, tingling, or electric shock feelings).
- pronoun resolved: You should not stop using trazodone suddenly, or you could have unpleasant symptoms (such as dizziness, vomiting, agitation, sweating, confusion, numbness, tingling, or electric shock feelings).
  - edits: “this medicine” → “trazodone”
  - S1: You should not stop using trazodone suddenly.
  - S2: You could have unpleasant symptoms.
  - S3: These symptoms include dizziness, vomiting, agitation, sweating, confusion, numbness, tingling, or electric shock feelings.

**L41.1** `Incomplete Sentence` (0.974) → `excluded_incomplete`
- original: Ask your doctor how to safely stop using this medicine.
- pronoun resolved: Ask your doctor how to safely stop using trazodone.
  - edits: “this medicine.” → “trazodone.”

**L42.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Store at room temperature away from moisture, heat, and light.

**L42.1** `Simple Sentence` (0.791) → `passthrough`
- original: If you are using the oral solution, throw away any unused medicine 20 days after first opening the bottle.

## Dosing information

**L45.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Depression:

**L46.0** `Complex Sentence` (0.559) → `decomposed`
- original: Initial dose: 150 mg orally per day in divided doses; this may be increased by 50 mg orally per day every 3 to 4 days Maximum dose: -Inpatients: 600 mg/day -Outpatients: 400 mg/day Comments: -Patients should be screened for a personal/family history of bipolar disorder, mania, or hypomania prior to initiating treatment.
- pronoun resolved: Initial dose: 150 mg orally per day in divided doses; Dose may be increased by 50 mg orally per day every 3 to 4 days Maximum dose: -Inpatients: 600 mg/day -Outpatients: 400 mg/day Comments: -Patients should be screened for a personal/family history of bipolar disorder, mania, or hypomania prior to initiating treatment.
  - edits: “this” → “Dose”
  - S1: The initial dose is 150 mg orally per day in divided doses.
  - S2: The dose may be increased by 50 mg orally per day every 3 to 4 days.
  - S3: The maximum dose for inpatients is 600 mg/day.
  - S4: The maximum dose for outpatients is 400 mg/day.
  - S5: Patients should be screened for a personal or family history of bipolar disorder, mania, or hypomania prior to initiating treatment.

**L46.1** `Simple Sentence` (0.944) → `passthrough`
- original: -Patients should be monitored for withdrawal symptoms when discontinuing therapy.

**L46.2** `Complex Sentence` (0.488) → `decomposed`
- original: -After an adequate response has been reached, dosage may be gradually reduced depending on therapeutic response.
  - S1: Dosage may be gradually reduced.
  - S2: The reduction depends on therapeutic response.
  - S3: This occurs after an adequate response has been reached.

**L46.3** `Compound Sentence` (0.7) → `decomposed`
- original: -If drowsiness develops, a major portion of the daily dose may be administered at bedtime or a reduction of dosage may be necessary.
  - S1: If drowsiness develops, a major portion of the daily dose may be administered at bedtime.
  - S2: If drowsiness develops, a reduction of dosage may be necessary.

**L46.4** `Simple Sentence` (0.987) → `passthrough`
- original: -This drug should be taken shortly after a meal or light snack.
- pronoun resolved: -Trazodone should be taken shortly after a meal or light snack.
  - edits: “-This drug” → “-Trazodone”

**L46.5** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Use: Treatment of major depressive disorder (MDD)

## What happens if I miss a dose?

**L49.0** `Compound Sentence` (0.555) → `decomposed`
- original: Take the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - S1: Take the medicine as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L49.1** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

## What happens if I overdose?

**L52.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L52.1** `Complex Sentence` (0.531) → `decomposed`
- original: An overdose can be fatal when trazodone is taken with alcohol, barbiturates such as phenobarbital, or sedatives such as diazepam (Valium).
  - S1: An overdose can be fatal when trazodone is taken with alcohol.
  - S2: An overdose can be fatal when trazodone is taken with barbiturates such as phenobarbital.
  - S3: An overdose can be fatal when trazodone is taken with sedatives such as diazepam (Valium).

**L53.0** `Complex Sentence` (0.466) → `decomposed`
- original: Overdose symptoms may include extreme drowsiness, vomiting, penis erection that is painful or prolonged, fast or pounding heartbeat, seizure (black-out or convulsions), or breathing that slows or stops.
  - S1: Overdose symptoms may include extreme drowsiness.
  - S2: Overdose symptoms may include vomiting.
  - S3: Overdose symptoms may include penis erection that is painful or prolonged.
  - S4: Overdose symptoms may include fast or pounding heartbeat.
  - S5: Overdose symptoms may include seizure.
  - S6: Overdose symptoms may include breathing that slows or stops.

## What to avoid

**L56.0** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Do not drink alcohol.

**L56.1** `Simple Sentence` (0.977) → `passthrough`
- original: Dangerous side effects or death could occur.

**L57.0** `Simple Sentence` (0.476) → `passthrough`
- original: Ask your doctor before taking a nonsteroidal anti-inflammatory drug (NSAID) such as aspirin, ibuprofen, naproxen, Advil, Aleve, Motrin, and others.

**L57.1** `Simple Sentence` (0.985) → `passthrough`
- original: Using an NSAID with trazodone may cause you to bruise or bleed easily.

**L58.0** `Incomplete Sentence` (0.964) → `excluded_incomplete`
- original: Avoid driving or hazardous activity until you know how this medicine will affect you.

**L58.1** `Simple Sentence` (0.878) → `passthrough`
- original: Your reactions could be impaired.

**L59.0** `Incomplete Sentence` (0.599) → `excluded_incomplete`
- original: Avoid getting up too fast from a sitting or lying position, or you may feel dizzy.

## Trazodone side effects

**L62.0** `Compound Sentence` (0.485) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to trazodone: hives; difficulty breathing; swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to trazodone.
  - S2: Signs of an allergic reaction to trazodone include hives.
  - S3: Signs of an allergic reaction to trazodone include difficulty breathing.
  - S4: Signs of an allergic reaction to trazodone include swelling of your face, lips, tongue, or throat.

**L63.0** `Compound Sentence` (0.602) → `decomposed`
- original: Stop taking trazodone and call your doctor at once if you have a penis erection that is painful or lasts 6 hours or longer.
  - S1: Stop taking trazodone if you have a painful penis erection.
  - S2: Call your doctor at once if you have a penis erection that lasts 6 hours or longer.

**L63.1** `Compound Sentence` (0.54) → `decomposed`
- original: This is a medical emergency and could lead to a serious condition that must be corrected with surgery.
  - S1: This is a medical emergency.
  - S2: It could lead to a serious condition that must be corrected with surgery.

**L64.0** `Compound-Complex Sentence` (0.427) → `decomposed`
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

**L65.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L66.0** `Incomplete Sentence` (0.916) → `excluded_incomplete`
- original: fast or pounding heartbeats, fluttering in your chest, shortness of breath, and sudden dizziness (like you might pass out);

**L67.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: slow heartbeats;

**L68.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: unusual thoughts or behavior;

**L69.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: easy bruising, unusual bleeding; or

**L70.0** `Incomplete Sentence` (0.956) → `excluded_incomplete`
- original: low levels of sodium in the body - headache, confusion, slurred speech, severe weakness, vomiting, loss of coordination, feeling unsteady.

**L71.0** `Complex Sentence` (0.607) → `decomposed`
- original: Seek medical attention right away if you have symptoms of serotonin syndrome, such as: agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness, twitching, loss of coordination, nausea, vomiting, or diarrhea.
  - S1: Seek medical attention right away if you have symptoms of serotonin syndrome.
  - S2: Symptoms of serotonin syndrome include agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness, twitching, loss of coordination, nausea, vomiting, or diarrhea.

**L72.0** `Simple Sentence` (0.962) → `passthrough`
- original: Common trazodone side effects may include:

**L73.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: drowsiness, dizziness, tiredness;

**L74.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: swelling;

**L75.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: weight loss;

**L76.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: blurred vision;

**L77.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: diarrhea, constipation; or

**L78.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: stuffy nose.

**L79.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L79.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L79.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## What other drugs will affect trazodone?

**L82.0** `Simple Sentence` (0.973) → `passthrough`
- original: Using trazodone with other drugs that make you drowsy can worsen this effect.

**L82.1** `Incomplete Sentence` (0.573) → `excluded_incomplete`
- original: Ask your doctor before using opioid medication, a sleeping pill, a muscle relaxer, or medicine for anxiety or seizures.

**L83.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Tell your doctor about all your current medicines.

**L83.1** `Simple Sentence` (0.991) → `passthrough`
- original: Many drugs can interact with trazodone, especially:

**L84.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: any other antidepressants;

**L85.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: phenytoin;

**L86.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: St. John's wort;

**L87.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: tramadol;

**L88.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a diuretic or "water pill";

**L89.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: medicine to treat anxiety, mood disorders, or mental illness such as schizophrenia;

**L90.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a blood thinner - warfarin, Coumadin, Jantoven; or

**L91.0** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: migraine headache medicine - sumatriptan, Imitrex, Maxalt, Treximet, and others.

**L92.0** `Simple Sentence` (0.61) → `passthrough`
- original: This list is not complete and many other drugs may interact with trazodone.

**L92.1** `Incomplete Sentence` (0.491) → `excluded_incomplete`
- original: This includes prescription and over-the-counter medicines, vitamins, and herbal products.
- pronoun resolved: List includes prescription and over-the-counter medicines, vitamins, and herbal products.
  - edits: “This” → “List”

**L92.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.

## Popular FAQ

**L95.0** `Incomplete Sentence` (0.964) → `excluded_incomplete`
- original: Q: What are the strongest sleeping pills?

**L95.1** `Simple Sentence` (0.554) → `passthrough`
- original: A: There are many different types of sleeping pills available.

**L95.2** `Compound Sentence` (0.873) → `decomposed`
- original: Some require a prescription, while others are available over the counter.
  - S1: Some require a prescription.
  - S2: Others are available over the counter.

**L95.3** `Simple Sentence` (0.98) → `passthrough`
- original: In general, prescription sleeping pills are stronger than those found over the counter.

**L95.4** `Simple Sentence` (0.922) → `passthrough`
- original: Some strong sleeping pill names include zolpidem, temazepam, and suvorexant.

**L96.0** `Compound Sentence` (0.666) → `decomposed`
- original: Q: Trazodone for dogs: Uses, dosage and side effects A: Trazodone is often used in dogs to relieve anxiety or stress or help your dog (and you!)
  - S1: Trazodone is often used in dogs to relieve anxiety or stress.
  - S2: It is also used to help your dog (and you!).

**L96.1** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: cope with other behavioral issues.

**L97.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Q: Does trazodone cause weight gain?

**L97.1** `Compound Sentence` (0.958) → `decomposed`
- original: A: Trazodone may cause weight gain for some people, but it is not a common side effect of the medication.
- pronoun resolved: A: Trazodone may cause weight gain for some people, but Trazodone is not a common side effect of the medication.
  - edits: “it” → “Trazodone”
  - S1: Trazodone may cause weight gain for some people.
  - S2: Trazodone is not a common side effect of the medication.

**L97.2** `Simple Sentence` (0.988) → `passthrough`
- original: Weight loss was shown to be slightly more common with trazodone.

**L98.0** `Incomplete Sentence` (0.66) → `excluded_incomplete`
- original: Q: Does trazodone make you sleepy?

**L98.1** `Compound Sentence` (0.96) → `decomposed`
- original: A: Trazodone can help you sleep, and sleepiness is a side effect of the medication.
  - S1: Trazodone can help you sleep.
  - S2: Sleepiness is a side effect of the medication.

**L98.2** `Complex Sentence` (0.669) → `decomposed`
- original: Doctors will sometimes prescribe trazodone for insomnia, particularly for people who have both depression and difficulty sleeping.
  - S1: Doctors will sometimes prescribe trazodone for insomnia.
  - S2: This is particularly for people who have both depression and difficulty sleeping.

**L98.3** `Complex Sentence` (0.441) → `decomposed`
- original: However, the benefit of taking trazodone for insomnia is not well established.
  - S1: However, the benefit of taking trazodone for insomnia is not well established.

**L98.4** `Complex Sentence` (0.9) → `decomposed`
- original: The American Academy of Sleep Medicine recommends that trazodone and other antidepressants only be used for insomnia when other treatments have failed or in patients who also have depression.
  - S1: The American Academy of Sleep Medicine recommends specific usage guidelines for trazodone and other antidepressants.
  - S2: These medications should only be used for insomnia when other treatments have failed.
  - S3: They should also be used for insomnia in patients who have depression.

**L99.0** `Simple Sentence` (0.536) → `passthrough`
- original: Q: How long does trazodone stay in your system?

**L99.1** `Simple Sentence` (0.957) → `passthrough`
- original: A: Trazodone is mostly cleared from a healthy adult’s body within 1 to 3 days after a single dose.

**L99.2** `Compound-Complex Sentence` (0.639) → `decomposed`
- original: Its half-life is 5 to 13 hours, and since it takes about 5.5 half-lives for a drug to leave the system, trazodone is typically eliminated in about 27 to 72 hours.
- pronoun resolved: Trazodone's half-life is 5 to 13 hours, and since Trazodone takes about 5.5 half-lives for a drug to leave the system, trazodone is typically eliminated in about 27 to 72 hours.
  - edits: “Its” → “Trazodone's”; “it” → “Trazodone”
  - S1: Trazodone's half-life is 5 to 13 hours.
  - S2: It takes about 5.5 half-lives for a drug to leave the system.
  - S3: Trazodone is typically eliminated in about 27 to 72 hours.

**L100.0** `Incomplete Sentence` (0.964) → `excluded_incomplete`
- original: Q: Is trazodone a controlled substance or narcotic?

**L100.1** `Compound Sentence` (0.942) → `decomposed`
- original: A: The FDA does not classify trazodone as a controlled substance, and it is not considered a narcotic.
- pronoun resolved: A: The FDA does not classify trazodone as a controlled substance, and trazodone is not considered a narcotic.
  - edits: “it” → “trazodone”
  - S1: The FDA does not classify trazodone as a controlled substance.
  - S2: Trazodone is not considered a narcotic.

**L101.0** `Incomplete Sentence` (0.962) → `excluded_incomplete`
- original: Q: Can trazodone cause a false positive on a drug test?

**L101.1** `Complex Sentence` (0.588) → `decomposed`
- original: A: Yes, trazodone has been shown to cause false positive results on urine drug tests for amphetamines, MDMA, and LSD.
  - S1: Trazodone has been shown to cause false positive results on urine drug tests.
  - S2: The false positive results are for amphetamines, MDMA, and LSD.

**L101.2** `Complex Sentence` (0.949) → `decomposed`
- original: This potential for cross-reactivity is due to one of its primary metabolites, meta-chlorophenylpiperazine (m-CPP), which can interfere with specific immunoassay screenings.
- pronoun resolved: This potential for cross-reactivity is due to one of trazodone's primary metabolites, meta-chlorophenylpiperazine (m-CPP), which can interfere with specific immunoassay screenings.
  - edits: “its” → “trazodone's”
  - S1: This potential for cross-reactivity is due to one of trazodone's primary metabolites.
  - S2: The metabolite is meta-chlorophenylpiperazine (m-CPP).
  - S3: m-CPP can interfere with specific immunoassay screenings.

**L102.0** `Incomplete Sentence` (0.841) → `excluded_incomplete`
- original: Q: How long does it take for trazodone to work?

**L102.1** `Compound Sentence` (0.802) → `decomposed`
- original: A: Trazodone may start to relieve depression 1 to 2 weeks after you begin taking it, but it can take up to 6 weeks for the full benefit of the medication to set in.
- pronoun resolved: A: Trazodone may start to relieve depression 1 to 2 weeks after you begin taking it, but Trazodone can take up to 6 weeks for the full benefit of the medication to set in.
  - edits: “it” → “Trazodone”
  - S1: Trazodone may start to relieve depression 1 to 2 weeks after you begin taking it.
  - S2: Trazodone can take up to 6 weeks for the full benefit of the medication to set in.
