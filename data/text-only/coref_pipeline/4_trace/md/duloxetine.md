# Duloxetine — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/duloxetine.txt` · 137 sentences · 7 changed by pronoun resolution · 214 sentences sent to EDC

## What is duloxetine?

**L5.0** `Simple Sentence` (0.964) → `passthrough`
- original: Duloxetine is a selective serotonin and norepinephrine reuptake inhibitor antidepressant (SSNRI).

**L5.1** `Simple Sentence` (0.97) → `passthrough`
- original: Duloxetine affects chemicals in the brain that may be unbalanced in people with depression.

**L6.0** `Simple Sentence` (0.989) → `passthrough`
- original: Duloxetine is used to treat major depressive disorder in adults.

**L6.1** `Simple Sentence` (0.904) → `passthrough`
- original: It is also used to treat general anxiety disorder in adults and children who are at least 7 years old.
- pronoun resolved: Duloxetine is also used to treat general anxiety disorder in adults and children who are at least 7 years old.
  - edits: “It” → “Duloxetine”

**L7.0** `Compound Sentence` (0.638) → `decomposed`
- original: Duloxetine is also used in adults to treat nerve pain caused by diabetes (diabetic neuropathy), or chronic muscle or joint pain (such as low back pain and osteoarthritis pain).
  - S1: Duloxetine is also used in adults to treat nerve pain caused by diabetes (diabetic neuropathy).
  - S2: It is also used to treat chronic muscle or joint pain (such as low back pain and osteoarthritis pain).

**L8.0** `Simple Sentence` (0.796) → `passthrough`
- original: Some brands of duloxetine are also used to treat fibromyalgia (a chronic pain disorder).

**L8.1** `Simple Sentence` (0.99) → `passthrough`
- original: Drizalma is for treating fibromyalgia only in adults.

**L8.2** `Simple Sentence` (0.983) → `passthrough`
- original: Cymbalta may be used to treat fibromyalgia in adults and children at least 13 years old.

## Warnings

**L11.0** `Compound Sentence` (0.569) → `decomposed`
- original: Do not take duloxetine within 5 days before or 14 days after you have used an MAO inhibitor, such as isocarboxazid, linezolid, methylene blue injection, phenelzine, tranylcypromine, and others.
  - S1: Do not take duloxetine within 5 days before or 14 days after you have used an MAO inhibitor.
  - S2: Examples of MAO inhibitors include isocarboxazid, linezolid, methylene blue injection, phenelzine, tranylcypromine, and others.

**L11.1** `Simple Sentence` (0.94) → `passthrough`
- original: A dangerous drug interaction could occur.

**L12.0** `Simple Sentence` (0.976) → `passthrough`
- original: People with depression or mental illness may have thoughts about suicide.

**L12.1** `Simple Sentence` (0.532) → `passthrough`
- original: Some young people may have increased suicidal thoughts when first starting a medicine to treat depression.

**L12.2** `Incomplete Sentence` (0.732) → `excluded_incomplete`
- original: Tell your doctor right away if you have any sudden changes in mood or behavior, or thoughts about suicide.

**L13.0** `Simple Sentence` (0.59) → `passthrough`
- original: Do not stop using duloxetine without first talking to your doctor.

## Before taking this medicine

**L16.0** `Simple Sentence` (0.989) → `passthrough`
- original: You should not use duloxetine if you are allergic to it.
- pronoun resolved: You should not use duloxetine if you are allergic to duloxetine.
  - edits: “it.” → “duloxetine.”

**L17.0** `Compound Sentence` (0.539) → `decomposed`
- original: Do not take duloxetine within 5 days before or 14 days after you have used an MAO inhibitor, such as isocarboxazid, linezolid, methylene blue injection, phenelzine, or tranylcypromine.
  - S1: Do not take duloxetine within 5 days before you have used an MAO inhibitor.
  - S2: Do not take duloxetine within 14 days after you have used an MAO inhibitor.
  - S3: Examples of MAO inhibitors include isocarboxazid, linezolid, methylene blue injection, phenelzine, and tranylcypromine.

**L17.1** `Simple Sentence` (0.94) → `passthrough`
- original: A dangerous drug interaction could occur.

**L18.0** `Incomplete Sentence` (0.427) → `excluded_incomplete`
- original: Tell your doctor if you also use stimulant medicine, opioid medicine, herbal products, or medicine for depression, mental illness, Parkinson's disease, migraine headaches, serious infections, or prevention of nausea and vomiting.

**L18.1** `Simple Sentence` (0.989) → `passthrough`
- original: An interaction with duloxetine could cause a serious condition called serotonin syndrome.

**L19.0** `Simple Sentence` (0.989) → `passthrough`
- original: Duloxetine is not approved for use by anyone younger than 7 years old.

**L20.0** `Simple Sentence` (0.68) → `passthrough`
- original: To make sure duloxetine is safe for you, tell your doctor if you have:

**L21.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: heart problems, high blood pressure;

**L22.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: liver or kidney disease;

**L23.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: slow digestion;

**L24.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a seizure;

**L25.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: bleeding problems;

**L26.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: sexual problems;

**L27.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: narrow-angle glaucoma;

**L28.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: bipolar disorder (manic depression);

**L29.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: drug addiction or suicidal thoughts;

**L30.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: if you drink large amounts of alcohol;

**L31.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: diabetes;

**L32.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: low sodium levels in your blood.

**L33.0** `Simple Sentence` (0.976) → `passthrough`
- original: People with depression or mental illness may have thoughts about suicide.

**L33.1** `Simple Sentence` (0.532) → `passthrough`
- original: Some young people may have increased suicidal thoughts when first starting a medicine to treat depression.

**L33.2** `Incomplete Sentence` (0.9) → `excluded_incomplete`
- original: Stay alert to changes in your mood or symptoms.

**L33.3** `Simple Sentence` (0.957) → `passthrough`
- original: Your family or caregivers should also watch for sudden changes in your behavior.

**L34.0** `Compound Sentence` (0.96) → `decomposed`
- original: Taking an SNRI antidepressant during late pregnancy could increase your risk of excessive bleeding after you give birth, and may cause serious medical complications in the baby.
  - S1: Taking an SNRI antidepressant during late pregnancy could increase your risk of excessive bleeding after you give birth.
  - S2: It may cause serious medical complications in the baby.

**L34.1** `Complex Sentence` (0.54) → `decomposed`
- original: However, stopping the medicine may not be safe if you have a relapse of depression.
- pronoun resolved: However, stopping Duloxetine may not be safe if you have a relapse of depression.
  - edits: “the medicine” → “Duloxetine”
  - S1: However, stopping Duloxetine may not be safe.
  - S2: This is the case if you have a relapse of depression.

**L34.2** `Simple Sentence` (0.494) → `passthrough`
- original: Do not start or stop duloxetine without asking your doctor.

**L35.0** `Complex Sentence` (0.686) → `decomposed`
- original: If you are pregnant, your name may be listed on a pregnancy registry to track the effects of duloxetine on the baby.
  - S1: If you are pregnant, your name may be listed on a pregnancy registry.
  - S2: The registry is used to track the effects of duloxetine on the baby.

**L35.1** `Compound Sentence` (0.499) → `decomposed`
- original: Talk to your doctor about registering with the National Pregnancy Registry for Antidepressants at 1-866-961-2388 or visit online at https://womensmentalhealth.org/research/pregnancyregistry/.
  - S1: Talk to your doctor about registering with the National Pregnancy Registry for Antidepressants at 1-866-961-2388.
  - S2: You can also visit online at https://womensmentalhealth.org/research/pregnancyregistry/.

**L36.0** `Complex Sentence` (0.495) → `decomposed`
- original: If you are breastfeeding, tell your doctor if you notice drowsiness, feeding problems, and slow weight gain in the nursing baby.
  - S1: If you are breastfeeding, tell your doctor.
  - S2: Tell your doctor if you notice drowsiness in the nursing baby.
  - S3: Tell your doctor if you notice feeding problems in the nursing baby.
  - S4: Tell your doctor if you notice slow weight gain in the nursing baby.

## How should I take duloxetine?

**L39.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Take duloxetine exactly as prescribed by your doctor.

**L39.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L39.2** `Simple Sentence` (0.984) → `passthrough`
- original: Your doctor may occasionally change your dose.

**L40.0** `Compound Sentence` (0.938) → `decomposed`
- original: Taking duloxetine in higher doses or more often than prescribed will not make it more effective, and may increase side effects.
  - S1: Taking duloxetine in higher doses or more often than prescribed will not make it more effective.
  - S2: It may increase side effects.

**L41.0** `Incomplete Sentence` (0.702) → `excluded_incomplete`
- original: Swallow the capsule whole and do not crush, chew, break, or open it.

**L42.0** `Simple Sentence` (0.978) → `passthrough`
- original: You may take duloxetine with or without food.

**L43.0** `Simple Sentence` (0.978) → `passthrough`
- original: Your blood pressure will need to be checked often.

**L44.0** `Compound Sentence` (0.357) → `decomposed`
- original: Tell your doctor if you have any changes in sexual function, such as loss of interest in sex, trouble having an orgasm, or (in men) problems with erections or ejaculation.
  - S1: Tell your doctor if you have any changes in sexual function.
  - S2: Such changes include loss of interest in sex.
  - S3: Such changes include trouble having an orgasm.
  - S4: Such changes include problems with erections or ejaculation in men.

**L44.1** `Simple Sentence` (0.983) → `passthrough`
- original: Some sexual problems can be treated.

**L45.0** `Simple Sentence` (0.986) → `passthrough`
- original: Your symptoms may not improve for up to 4 weeks.

**L46.0** `Compound Sentence` (0.817) → `decomposed`
- original: Do not stop using duloxetine suddenly, or you could have unpleasant symptoms (such as agitation, confusion, tingling or electric shock feelings).
  - S1: Do not stop using duloxetine suddenly.
  - S2: You could have unpleasant symptoms.
  - S3: These symptoms include agitation, confusion, tingling, or electric shock feelings.

**L46.1** `Incomplete Sentence` (0.812) → `excluded_incomplete`
- original: Ask your doctor before stopping the medicine.

**L47.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Store at room temperature away from moisture and heat.

## Dosing information

**L50.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Depression:

**L51.0** `Compound Sentence` (0.58) → `decomposed`
- original: Initial dose: 20 mg to 30 mg orally 2 times a day Maintenance dose: 60 mg per day, given either once a day OR 30 mg orally 2 times a day Maximum dose: 120 mg/day.
  - S1: Initial dose: 20 mg to 30 mg orally 2 times a day.
  - S2: Maintenance dose: 60 mg per day, given either once a day or 30 mg orally 2 times a day.
  - S3: Maximum dose: 120 mg/day.

**L52.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Fibromyalgia:

**L53.0** `Simple Sentence` (0.705) → `passthrough`
- original: Initial dose: 30 mg orally once a day for at least 1 week Maintenance dose: 30 to 60 mg orally once a day.

**L54.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Generalized Anxiety Disorder:

**L55.0** `Compound Sentence` (0.578) → `decomposed`
- original: Initial dose: 60 mg orally once a day Maintenance dose: 60 to 120 mg orally once a day Maximum dose: 120 mg/day.
  - S1: Initial dose: 60 mg orally once a day.
  - S2: Maintenance dose: 60 to 120 mg orally once a day.
  - S3: Maximum dose: 120 mg/day.

**L56.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Pain:

**L57.0** `Simple Sentence` (0.612) → `passthrough`
- original: Initial dose: 30 to 60 mg orally once a day Maintenance dose: 60 mg orally once a day.

**L58.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Neuropathic Pain:

**L59.0** `Simple Sentence` (0.612) → `passthrough`
- original: Initial dose: 30 to 60 mg orally once a day Maintenance dose: 60 mg orally once a day.

**L60.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Chronic Pain:

**L61.0** `Simple Sentence` (0.612) → `passthrough`
- original: Initial dose: 30 to 60 mg orally once a day Maintenance dose: 60 mg orally once a day.

**L62.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Geriatric Dose for Generalized Anxiety Disorder:

**L63.0** `Compound Sentence` (0.414) → `decomposed`
- original: Initial dose: 30 mg orally once a day for at least 2 weeks Maintenance dose: 60 mg orally once a day Maximum dose: 120 mg/day.
  - S1: The initial dose is 30 mg orally once a day for at least 2 weeks.
  - S2: The maintenance dose is 60 mg orally once a day.
  - S3: The maximum dose is 120 mg/day.

**L64.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Pediatric Dose for Generalized Anxiety Disorder:

**L65.0** `Incomplete Sentence` (0.483) → `excluded_incomplete`
- original: 7 to 17 years: -Initial dose: 30 mg orally once a day for at least 2 weeks -Maintenance dose: 30 to 60 mg orally once a day -Maximum dose: 120 mg/day.

**L66.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Pediatric Dose for Fibromyalgia:

**L67.0** `Simple Sentence` (0.376) → `passthrough`
- original: 13 years and older: -Initial dose: 30 mg orally once a day for at least 1 week -Maintenance dose: 30 to 60 mg orally once a day.

## What happens if I miss a dose?

**L70.0** `Compound Sentence` (0.555) → `decomposed`
- original: Take the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - S1: Take the medicine as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L70.1** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

## What happens if I overdose?

**L73.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L74.0** `Compound Sentence` (0.534) → `decomposed`
- original: Overdose symptoms may include vomiting, dizziness or drowsiness, seizures, fast heartbeats, fainting, or coma.
  - S1: Overdose symptoms may include vomiting.
  - S2: Overdose symptoms may include dizziness.
  - S3: Overdose symptoms may include drowsiness.
  - S4: Overdose symptoms may include seizures.
  - S5: Overdose symptoms may include fast heartbeats.
  - S6: Overdose symptoms may include fainting.
  - S7: Overdose symptoms may include coma.

## What should I avoid while taking duloxetine?

**L77.0** `Simple Sentence` (0.476) → `passthrough`
- original: Ask your doctor before taking a nonsteroidal anti-inflammatory drug (NSAID) such as aspirin, ibuprofen, naproxen, Advil, Aleve, Motrin, and others.

**L77.1** `Simple Sentence` (0.986) → `passthrough`
- original: Using an NSAID with duloxetine may cause you to bruise or bleed easily.

**L78.0** `Incomplete Sentence` (0.966) → `excluded_incomplete`
- original: Avoid driving or hazardous activity until you know how duloxetine will affect you.

**L78.1** `Simple Sentence` (0.878) → `passthrough`
- original: Your reactions could be impaired.

**L78.2** `Simple Sentence` (0.944) → `passthrough`
- original: Dizziness or fainting can cause falls, accidents, or severe injuries.

**L79.0** `Incomplete Sentence` (0.599) → `excluded_incomplete`
- original: Avoid getting up too fast from a sitting or lying position, or you may feel dizzy.

**L80.0** `Simple Sentence` (0.871) → `passthrough`
- original: Drinking alcohol may increase your risk of liver damage, especially if you take Drizalma.

## Duloxetine side effects

**L83.0** `Compound Sentence` (0.381) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to duloxetine (hives, difficult breathing, swelling in your face or throat) or a severe skin reaction (fever, sore throat, burning eyes, skin pain, red or purple skin rash with blistering and peeling).
  - S1: Get emergency medical help if you have signs of an allergic reaction to duloxetine.
  - S2: Signs of an allergic reaction to duloxetine include hives, difficult breathing, and swelling in your face or throat.
  - S3: Get emergency medical help if you have a severe skin reaction.
  - S4: Signs of a severe skin reaction include fever, sore throat, burning eyes, skin pain, and a red or purple skin rash with blistering and peeling.

**L84.0** `Compound-Complex Sentence` (0.564) → `decomposed` · repaired
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

**L85.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L86.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: pounding heartbeats or fluttering in your chest;

**L87.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a light-headed feeling, like you might pass out;

**L88.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: easy bruising, unusual bleeding;

**L89.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: vision changes;

**L90.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: painful or difficult urination;

**L91.0** `Incomplete Sentence` (0.95) → `excluded_incomplete`
- original: liver problems - right-sided upper stomach pain, itching, dark urine, jaundice (yellowing of the skin or eyes);

**L92.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: low blood sodium - headache, confusion, problems with thinking or memory, weakness, feeling unsteady; or

**L93.0** `Incomplete Sentence` (0.95) → `excluded_incomplete`
- original: manic episodes - racing thoughts, increased energy, decreased need for sleep, risk-taking behavior, being agitated or talkative.

**L94.0** `Complex Sentence` (0.607) → `decomposed`
- original: Seek medical attention right away if you have symptoms of serotonin syndrome, such as: agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness, twitching, loss of coordination, nausea, vomiting, or diarrhea.
  - S1: Seek medical attention right away if you have symptoms of serotonin syndrome.
  - S2: Symptoms of serotonin syndrome include agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness, twitching, loss of coordination, nausea, vomiting, or diarrhea.

**L95.0** `Simple Sentence` (0.939) → `passthrough`
- original: Common duloxetine side effects may include:

**L96.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: drowsiness, dizziness, or fatigue;

**L97.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: nausea, constipation, loss of appetite;

**L98.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: dry mouth; or

**L99.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: increased sweating.

**L100.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L100.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L100.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## What other drugs will affect duloxetine?

**L103.0** `Simple Sentence` (0.975) → `passthrough`
- original: Sometimes it is not safe to use certain medications at the same time.

**L103.1** `Complex Sentence` (0.897) → `decomposed`
- original: Some drugs can affect your blood levels of other drugs you take, which may increase side effects or make the medications less effective.
- pronoun resolved: Some drugs can affect your blood levels of other drugs you take, which may increase side effects or make certain medications less effective.
  - edits: “the” → “certain”
  - S1: Some drugs can affect your blood levels of other drugs you take.
  - S2: This may increase side effects.
  - S3: This may make certain medications less effective.

**L104.0** `Simple Sentence` (0.476) → `passthrough`
- original: Ask your doctor before taking a nonsteroidal anti-inflammatory drug (NSAID) such as aspirin, ibuprofen, naproxen, Advil, Aleve, Motrin, and others.

**L104.1** `Simple Sentence` (0.986) → `passthrough`
- original: Using an NSAID with duloxetine may cause you to bruise or bleed easily.

**L105.0** `Simple Sentence` (0.991) → `passthrough`
- original: Many drugs can interact with duloxetine.

**L105.1** `Simple Sentence` (0.849) → `passthrough`
- original: This includes prescription and over-the-counter medicines, vitamins, and herbal products.

**L105.2** `Simple Sentence` (0.949) → `passthrough`
- original: Not all possible interactions are listed here.

**L105.3** `Incomplete Sentence` (0.967) → `excluded_incomplete`
- original: Tell your doctor about all other medicines you use.

## Popular FAQ

**L108.0** `Incomplete Sentence` (0.972) → `excluded_incomplete`
- original: Q: What helps with Cymbalta withdrawal symptoms?

**L108.1** `Complex Sentence` (0.901) → `decomposed`
- original: A: The best way to help with Cymbalta (duloxetine) withdrawal is to stop the medicine slowly, over 2 to 4 weeks or longer, with your prescriber’s help.
  - S1: The best way to help with Cymbalta (duloxetine) withdrawal is to stop the medicine slowly.
  - S2: The medicine should be stopped over 2 to 4 weeks or longer.
  - S3: This process should be done with your prescriber's help.

**L108.2** `Compound Sentence` (0.884) → `decomposed`
- original: A slow, step-down plan (called a taper) gives your brain time to adjust and lowers the chance of symptoms like dizziness, nausea, and headache.
  - S1: A slow, step-down plan (called a taper) gives your brain time to adjust.
  - S2: It lowers the chance of symptoms like dizziness, nausea, and headache.

**L108.3** `Simple Sentence` (0.961) → `passthrough`
- original: While you taper, a few simple steps can ease symptoms.

**L108.4** `Incomplete Sentence` (0.906) → `excluded_incomplete`
- original: Never stop Cymbalta suddenly without talking to your doctor first.

**L109.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: Q: Does Cymbalta cause weight gain?

**L109.1** `Compound Sentence` (0.952) → `decomposed`
- original: A: Cymbalta is more likely to cause weight loss early in the first 8 to 9 weeks of treatment, but result in a modest weight gain after 8 months of treatment.
  - S1: Cymbalta is more likely to cause weight loss early in the first 8 to 9 weeks of treatment.
  - S2: It results in a modest weight gain after 8 months of treatment.

**L109.2** `Complex Sentence` (0.744) → `decomposed`
- original: In general, these weight changes are minimal and may be due to temporary side effects like nausea or loss of appetite, some of the most common side effects of Cymbalta treatment.
  - S1: In general, these weight changes are minimal.
  - S2: These weight changes may be due to temporary side effects.
  - S3: The temporary side effects include nausea or loss of appetite.
  - S4: Nausea or loss of appetite are some of the most common side effects of Cymbalta treatment.

**L110.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Q: How to sleep while taking Cymbalta?

**L110.1** `Simple Sentence` (0.757) → `passthrough`
- original: A: Not being able to sleep (also called insomnia) is one of the most common side effects reported by people taking Cymbalta.

**L110.2** `Compound Sentence` (0.95) → `decomposed`
- original: In some people, this side effect improves after a couple of weeks of taking Cymbalta, but difficulty falling asleep or staying asleep can persist in others.
  - S1: In some people, this side effect improves after a couple of weeks of taking Cymbalta.
  - S2: In others, difficulty falling asleep or staying asleep can persist.

**L110.3** `Simple Sentence` (0.851) → `passthrough`
- original: Here are some ways you can improve sleep while taking Cymbalta: Take your dose of Cymbalta in the morning.

**L110.4** `Compound-Complex Sentence` (0.849) → `decomposed`
- original: Cymbalta may be given once a day or twice a day but for those people experiencing insomnia, it should be taken just once a day in the morning Swallow Cymbalta capsules whole; do not crush, chew, or open up the capsules and sprinkle them on food because this may cause Cymbalta to be absorbed more quickly than intended, increasing the risk of side effects such as insomnia...
- pronoun resolved: Cymbalta may be given once a day or twice a day but for those people experiencing insomnia, Cymbalta should be taken just once a day in the morning Swallow Cymbalta capsules whole; do not crush, chew, or open up the capsules and sprinkle them on food because this may cause Cymbalta to be absorbed more quickly than intended, increasing the risk of side effects such as insomnia...
  - edits: “it” → “Cymbalta”
  - S1: Cymbalta may be given once a day.
  - S2: Cymbalta may be given twice a day.
  - S3: For those people experiencing insomnia, Cymbalta should be taken just once a day.
  - S4: Cymbalta should be taken in the morning for those people experiencing insomnia.
  - S5: Swallow Cymbalta capsules whole.
  - S6: Do not crush Cymbalta capsules.
  - S7: Do not chew Cymbalta capsules.
  - S8: Do not open up Cymbalta capsules.
  - S9: Do not sprinkle Cymbalta capsules on food.
  - S10: Sprinkling Cymbalta capsules on food may cause Cymbalta to be absorbed more quickly than intended.
  - S11: Increased absorption of Cymbalta may increase the risk of side effects such as insomnia.

**L111.0** `Incomplete Sentence` (0.959) → `excluded_incomplete`
- original: Q: How long does it take for Cymbalta to work?

**L111.1** `Compound-Complex Sentence` (0.836) → `decomposed`
- original: A: It may take up to 6 to 8 weeks for the full effects of Cymbalta to be seen, although some improvement in symptoms, such as sleep, energy, or appetite may show an improvement in 1-2 weeks.
- pronoun resolved: A: Cymbalta may take up to 6 to 8 weeks for the full effects of Cymbalta to be seen, although some improvement in symptoms, such as sleep, energy, or appetite may show an improvement in 1-2 weeks.
  - edits: “It” → “Cymbalta”
  - S1: Cymbalta may take up to 6 to 8 weeks for the full effects to be seen.
  - S2: Some improvement in symptoms may show in 1-2 weeks.
  - S3: Improvement in sleep may show in 1-2 weeks.
  - S4: Improvement in energy may show in 1-2 weeks.
  - S5: Improvement in appetite may show in 1-2 weeks.

**L111.2** `Simple Sentence` (0.792) → `passthrough`
- original: Symptoms such as depressed mood and lack of interest in activities may take the full 6-8 weeks to resolve.

**L111.3** `Simple Sentence` (0.504) → `passthrough`
- original: When Cymbalta is used for pain, it generally improves within two weeks.
- pronoun resolved: When Cymbalta is used for pain, Cymbalta generally improves within two weeks.
  - edits: “it” → “Cymbalta”

**L112.0** `Incomplete Sentence` (0.964) → `excluded_incomplete`
- original: Q: What do Cymbalta brain zaps feel like?

**L112.1** `Complex Sentence` (0.888) → `decomposed`
- original: A: People have reported feeling electric shock-like sensations or “brain zaps” when starting Cymbalta (duloxetine) treatment, during treatment, and also when discontinuing it.
  - S1: People have reported feeling electric shock-like sensations or "brain zaps".
  - S2: These sensations occur when starting Cymbalta (duloxetine) treatment.
  - S3: These sensations also occur during treatment.
  - S4: These sensations also occur when discontinuing the treatment.

**L112.2** `Simple Sentence` (0.826) → `passthrough`
- original: Most report feeling these in the brain although some report them in other parts of the body.

**L112.3** `Simple Sentence` (0.973) → `passthrough`
- original: They have been described as feeling like a short, low voltage, electric shock.

**L113.0** `Incomplete Sentence` (0.621) → `excluded_incomplete`
- original: Q: How do you manage neuropathy from chemo?

**L113.1** `Complex Sentence` (0.878) → `decomposed`
- original: A: Chemotherapy-induced peripheral neuropathy (CIPN) is a frequent and often distressing side effect of cancer treatment that affects the nerves.
  - S1: Chemotherapy-induced peripheral neuropathy (CIPN) is a frequent and often distressing side effect of cancer treatment.
  - S2: CIPN affects the nerves.

**L113.2** `Complex Sentence` (0.664) → `decomposed`
- original: Common symptoms of CIPN are numbness, tingling, burning pain, and muscle weakness, which often occur in the hands and feet.
  - S1: Common symptoms of CIPN are numbness, tingling, burning pain, and muscle weakness.
  - S2: These symptoms often occur in the hands and feet.
