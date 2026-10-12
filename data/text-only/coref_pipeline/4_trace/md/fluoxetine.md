# Fluoxetine — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/fluoxetine.txt` · 266 sentences · 40 changed by pronoun resolution · 409 sentences sent to EDC

## What is Fluoxetine?

**L5.0** `Simple Sentence` (0.542) → `passthrough`
- original: Fluoxetine is a prescription antidepressant used to treat major depressive disorder, obsessive-compulsive disorder (OCD), bulimia nervosa, and panic disorder.

**L5.1** `Complex Sentence` (0.906) → `decomposed`
- original: When used together with olanzapine (Zyprexa), it is also used to treat depressive episodes associated with bipolar I disorder and treatment-resistant depression.
- pronoun resolved: When used together with olanzapine (Zyprexa), Fluoxetine is also used to treat depressive episodes associated with bipolar I disorder and treatment-resistant depression.
  - edits: “it” → “Fluoxetine”
  - S1: Fluoxetine is used to treat depressive episodes associated with bipolar I disorder.
  - S2: Fluoxetine is used to treat treatment-resistant depression.
  - S3: These uses occur when Fluoxetine is used together with olanzapine (Zyprexa).

**L6.0** `Simple Sentence` (0.983) → `passthrough`
- original: Fluoxetine belongs to a class of antidepressants called selective serotonin reuptake inhibitors (SSRIs).

**L7.0** `Compound Sentence` (0.96) → `decomposed`
- original: The original brand name of fluoxetine is Prozac, and it's now available as a generic.
  - S1: The original brand name of fluoxetine is Prozac.
  - S2: It is now available as a generic.

## What Is Fluoxetine Used For?

**L10.0** `Simple Sentence` (0.965) → `passthrough`
- original: Fluoxetine is FDA-approved to treat the following conditions:

**L11.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Major depressive disorder (MDD) for acute and maintenance treatment in adults and children aged 8 years and older

**L12.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Obsessive-compulsive disorder (OCD) for acute and maintenance treatment in adults and children aged 7 years and older

**L13.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Bulimia nervosa for acute and maintenance treatment of binge-eating and purging in adults with moderate to severe bulimia

**L14.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Panic disorder for the treatment of panic attacks in adults

**L15.0** `Simple Sentence` (0.858) → `passthrough`
- original: When used in combination with olanzapine, fluoxetine is also FDA-approved for:

**L16.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Acute treatment of depressive episodes associated with Bipolar I disorder (depressive episodes) in adults and children aged 10 years and older

**L17.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Treatment-resistant depression for adults who have not responded to at least two adequate antidepressant trials

**L18.0** `Compound Sentence` (0.906) → `decomposed`
- original: Fluoxetine alone is not approved for bipolar I depressive episodes or treatment-resistant depression - olanzapine must be used in combination for these indications.
  - S1: Fluoxetine alone is not approved for bipolar I depressive episodes or treatment-resistant depression.
  - S2: Olanzapine must be used in combination for these indications.

## How does fluoxetine (Prozac) work?

**L21.0** `Complex Sentence` (0.913) → `decomposed`
- original: Fluoxetine works by blocking the reabsorption (reuptake) of serotonin in the brain, leaving more of it active between nerve cells.
- pronoun resolved: Fluoxetine works by blocking the reabsorption (reuptake) of serotonin in the brain, leaving more of serotonin active between nerve cells.
  - edits: “it” → “serotonin”
  - S1: Fluoxetine works by blocking the reabsorption of serotonin in the brain.
  - S2: This process leaves more serotonin active between nerve cells.
  - S3: The reabsorption of serotonin is also known as reuptake.

**L21.1** `Simple Sentence` (0.925) → `passthrough`
- original: Serotonin is a neurotransmitter that helps regulate mood, emotions, and sleep.

**L21.2** `Complex Sentence` (0.868) → `decomposed`
- original: By increasing the availability of serotonin, fluoxetine can relieve symptoms of depression, anxiety, and OCD.
  - S1: Fluoxetine can relieve symptoms of depression, anxiety, and OCD.
  - S2: Fluoxetine relieves these symptoms by increasing the availability of serotonin.

**L22.0** `Simple Sentence` (0.983) → `passthrough`
- original: Fluoxetine belongs to a class of antidepressants called selective serotonin reuptake inhibitors (SSRIs).

**L22.1** `Complex Sentence` (0.919) → `decomposed`
- original: SSRIs are one of the most commonly prescribed antidepressant classes because they are generally well-tolerated and effective across a range of conditions.
- pronoun resolved: SSRIs are one of the most commonly prescribed antidepressant classes because SSRIs are generally well-tolerated and effective across a range of conditions.
  - edits: “they” → “SSRIs”
  - S1: SSRIs are one of the most commonly prescribed antidepressant classes.
  - S2: SSRIs are generally well-tolerated.
  - S3: SSRIs are effective across a range of conditions.

**L23.0** `Simple Sentence` (0.83) → `passthrough`
- original: Most people need to take fluoxetine for 4 to 6 weeks before feeling the full effects.

## Fluoxetine Side Effects

**L26.0** `Simple Sentence` (0.987) → `passthrough`
- original: Like all medications, Prozac can cause side effects.

**L26.1** `Compound Sentence` (0.964) → `decomposed`
- original: Not everyone experiences them, and many improve after the first few weeks as your body adjusts to the medication.
- pronoun resolved: Not everyone experiences side effects, and many improve after the first few weeks as your body adjusts to the medication.
  - edits: “them,” → “side effects,”
  - S1: Not everyone experiences side effects.
  - S2: Many improve after the first few weeks as your body adjusts to the medication.

**L26.2** `Incomplete Sentence` (0.778) → `excluded_incomplete`
- original: Tell your doctor if any side effects bother you or do not go away.

**L27.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Common Fluoxetine Side Effects:

**L28.0** `Simple Sentence` (0.973) → `passthrough`
- original: The most commonly reported side effects of fluoxetine (Prozac) include:

**L29.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Nausea

**L30.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Trouble sleeping (insomnia)

**L31.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Drowsiness or sleepiness

**L32.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Anxiety or feeling nervous or on edge

**L33.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Trembling or shaking (tremor)

**L34.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Excessive sweating

**L35.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Loss of appetite

**L36.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Diarrhea

**L37.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Dry mouth

**L38.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Indigestion or upset stomach

**L39.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Weakness or fatigue

**L40.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Sore throat

**L41.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Sinus congestion or infection

**L42.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Flu-like symptoms

**L43.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Skin rash

**L44.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Flushing or feeling of warmth

**L45.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Yawning

**L46.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Unusual or vivid dreams

**L47.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Decreased sex drive

**L48.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Difficulty getting or keeping an erection

**L49.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Delayed or abnormal ejaculation

**L50.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious side effects:

**L51.0** `Compound Sentence` (0.395) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to this medicine (hives, difficult breathing, swelling in your face or throat) or a severe skin reaction (fever, sore throat, burning eyes, skin pain, red or purple skin rash with blistering and peeling).
- pronoun resolved: Get emergency medical help if you have signs of an allergic reaction to Fluoxetine (hives, difficult breathing, swelling in your face or throat) or a severe skin reaction (fever, sore throat, burning eyes, skin pain, red or purple skin rash with blistering and peeling).
  - edits: “this medicine” → “Fluoxetine”
  - S1: Get emergency medical help if you have signs of an allergic reaction to Fluoxetine, such as hives, difficult breathing, or swelling in your face or throat.
  - S2: Get emergency medical help if you have a severe skin reaction, such as fever, sore throat, burning eyes, skin pain, or a red or purple skin rash with blistering and peeling.

**L52.0** `Compound-Complex Sentence` (0.433) → `decomposed`
- original: Report any new or worsening symptoms to your doctor, such as mood or behavior changes, anxiety, panic attacks, trouble sleeping, or if you feel impulsive, irritable, agitated, hostile, aggressive, restless, hyperactive (mentally or physically), more depressed, or have thoughts about suicide or hurting yourself.
  - S1: Report any new or worsening symptoms to your doctor.
  - S2: Report mood changes to your doctor.
  - S3: Report behavior changes to your doctor.
  - S4: Report anxiety to your doctor.
  - S5: Report panic attacks to your doctor.
  - S6: Report trouble sleeping to your doctor.
  - S7: Report feelings of impulsivity to your doctor.
  - S8: Report feelings of irritability to your doctor.
  - S9: Report feelings of agitation to your doctor.
  - S10: Report feelings of hostility to your doctor.
  - S11: Report feelings of aggression to your doctor.
  - S12: Report feelings of restlessness to your doctor.
  - S13: Report feelings of hyperactivity (mentally or physically) to your doctor.
  - S14: Report increased depression to your doctor.
  - S15: Report thoughts about suicide to your doctor.
  - S16: Report thoughts about hurting yourself to your doctor.

**L53.0** `Simple Sentence` (0.988) → `passthrough`
- original: This medicine may cause serious side effects.
- pronoun resolved: Fluoxetine may cause serious side effects.
  - edits: “This medicine” → “Fluoxetine”

**L53.1** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L54.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: blurred vision, tunnel vision, eye pain or swelling, or seeing halos around lights;

**L55.0** `Incomplete Sentence` (0.916) → `excluded_incomplete`
- original: fast or pounding heartbeats, fluttering in your chest, shortness of breath, and sudden dizziness (like you might pass out);

**L56.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: low levels of sodium in the body - headache, confusion, slurred speech, severe weakness, vomiting, loss of coordination, feeling unsteady; or

**L57.0** `Incomplete Sentence` (0.669) → `excluded_incomplete`
- original: severe nervous system reaction - very stiff (rigid) muscles, high fever, sweating, confusion, fast or uneven heartbeats, tremors, feeling like you might pass out.

**L58.0** `Complex Sentence` (0.607) → `decomposed`
- original: Seek medical attention right away if you have symptoms of serotonin syndrome, such as: agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness, twitching, loss of coordination, nausea, vomiting, or diarrhea.
  - S1: Seek medical attention right away if you have symptoms of serotonin syndrome.
  - S2: Symptoms of serotonin syndrome include agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness, twitching, loss of coordination, nausea, vomiting, or diarrhea.

**L59.0** `Compound Sentence` (0.545) → `decomposed`
- original: This is not a complete list of side effects, and others may occur.
  - S1: This is not a complete list of side effects.
  - S2: Others may occur.

**L59.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L59.2** `Simple Sentence` (0.97) → `passthrough`
- original: You may report side effects to the FDA at 1-800-FDA-1088.

## Who Should Not Take This Medicine?

**L62.0** `Incomplete Sentence` (0.887) → `excluded_incomplete`
- original: Do not take fluoxetine if any of the following apply to you.

**L62.1** `Incomplete Sentence` (0.89) → `excluded_incomplete`
- original: Tell your doctor or pharmacist about all medications you currently take or have recently stopped taking.

**L63.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Do not take fluoxetine if you:

**L64.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Are allergic to fluoxetine or any of its ingredients

**L65.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Currently take a monoamine oxidase inhibitor (MAOI), including the antibiotic linezolid.

**L65.1** `Simple Sentence` (0.669) → `passthrough`
- original: If you are unsure whether your medication is an MAOI, ask your doctor or pharmacist

**L66.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Stopped taking an MAOI in the last 2 weeks

**L67.0** `Incomplete Sentence` (0.91) → `excluded_incomplete`
- original: Currently take pimozide (Orap) as this combination can cause a serious, potentially life-threatening irregular heart rhythm

**L68.0** `Simple Sentence` (0.851) → `passthrough`
- original: Currently taking thioridazine (Mellaril) as this combination can cause a dangerous irregular heart rhythm

**L69.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Important timing rules with MAOIs and thioridazine:

**L70.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Wait at least 2 weeks after stopping an MAOI before starting fluoxetine

**L71.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Wait at least 5 weeks after stopping fluoxetine before starting an MAOI or thioridazine

## Warnings

**L74.0** `Simple Sentence` (0.556) → `passthrough`
- original: Like all medications, Prozac carries some important warnings you should be aware of before and during treatment.

**L74.1** `Incomplete Sentence` (0.909) → `excluded_incomplete`
- original: Contact your doctor right away if you experience any of the following.

**L75.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Boxed warning:

**L76.0** `Simple Sentence` (0.706) → `passthrough`
- original: Fluoxetine carries a boxed warning, the FDA's most serious warning, regarding suicidal thoughts and behavior.

**L76.1** `Complex Sentence` (0.943) → `decomposed`
- original: Antidepressants, including fluoxetine, may increase the risk of suicidal thoughts in children, adolescents, and young adult s, particularly in the first few months of treatment or when your dose is changed.
  - S1: Antidepressants may increase the risk of suicidal thoughts in children, adolescents, and young adults.
  - S2: Fluoxetine is an antidepressant.
  - S3: The risk is particularly high in the first few months of treatment.
  - S4: The risk is also high when the dose is changed.

**L76.2** `Compound Sentence` (0.953) → `decomposed`
- original: This risk was not seen in adults over 24, and adults 65 and older actually showed a reduced risk.
  - S1: This risk was not seen in adults over 24.
  - S2: Adults 65 and older actually showed a reduced risk.

**L77.0** `Compound Sentence` (0.944) → `decomposed`
- original: Anyone starting this medicine should be closely monitored for worsening mood or new or worsening suicidal thoughts, and families and caregivers should stay in regular contact with the prescriber.
- pronoun resolved: Anyone starting Fluoxetine should be closely monitored for worsening mood or new or worsening suicidal thoughts, and families and caregivers should stay in regular contact with the prescriber.
  - edits: “this medicine” → “Fluoxetine”
  - S1: Anyone starting Fluoxetine should be closely monitored for worsening mood or new or worsening suicidal thoughts.
  - S2: Families and caregivers should stay in regular contact with the prescriber.

**L78.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Other warnings:

**L79.0** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: Serotonin syndrome: A potentially life-threatening condition that can occur when serotonin builds up to dangerous levels.

**L79.1** `Compound Sentence` (0.898) → `decomposed`
- original: This can occur when taken alone, but is more likely when taken with other serotonergic medications.
  - S1: This can occur when taken alone.
  - S2: It is more likely when taken with other serotonergic medications.

**L79.2** `Incomplete Sentence` (0.462) → `excluded_incomplete`
- original: Seek emergency care immediately if you experience agitation, hallucinations, rapid heartbeat, high fever, muscle rigidity, tremor, or seizures.

**L80.0** `Complex Sentence` (0.405) → `decomposed`
- original: Severe allergic reactions: Stop taking this medicine and seek emergency help if you develop trouble breathing, facial swelling, hives, or blistering rash.
- pronoun resolved: Severe allergic reactions: Stop taking Fluoxetine and seek emergency help if you develop trouble breathing, facial swelling, hives, or blistering rash.
  - edits: “this medicine” → “Fluoxetine”
  - S1: Severe allergic reactions require stopping Fluoxetine and seeking emergency help.
  - S2: Stop taking Fluoxetine if you develop trouble breathing.
  - S3: Stop taking Fluoxetine if you develop facial swelling.
  - S4: Stop taking Fluoxetine if you develop hives.
  - S5: Stop taking Fluoxetine if you develop a blistering rash.

**L81.0** `Complex Sentence` (0.907) → `decomposed`
- original: Abnormal bleeding: This medicine may increase the risk of bleeding or bruising, particularly if taken with blood thinners (such as warfarin), NSAIDs (such as ibuprofen or naproxen), or aspirin.
- pronoun resolved: Abnormal bleeding: Fluoxetine may increase the risk of bleeding or bruising, particularly if taken with blood thinners (such as warfarin), NSAIDs (such as ibuprofen or naproxen), or aspirin.
  - edits: “This medicine” → “Fluoxetine”
  - S1: Abnormal bleeding may occur with fluoxetine.
  - S2: Fluoxetine may increase the risk of bleeding or bruising.
  - S3: This risk is particularly high if fluoxetine is taken with blood thinners.
  - S4: Examples of blood thinners include warfarin.
  - S5: The risk is also increased if taken with NSAIDs.
  - S6: Examples of NSAIDs include ibuprofen or naproxen.
  - S7: The risk is further increased if taken with aspirin.

**L82.0** `Complex Sentence` (0.841) → `decomposed`
- original: Eye problems (angle-closure glaucoma): This medicine can cause angle-closure glaucoma with symptoms of eye pain, vision changes, or swelling around the eye in some people.
- pronoun resolved: Eye problems (angle-closure glaucoma): Fluoxetine can cause angle-closure glaucoma with symptoms of eye pain, vision changes, or swelling around the eye in some people.
  - edits: “This medicine” → “Fluoxetine”
  - S1: Eye problems include angle-closure glaucoma.
  - S2: Fluoxetine can cause angle-closure glaucoma.
  - S3: Symptoms of angle-closure glaucoma include eye pain, vision changes, or swelling around the eye.
  - S4: These symptoms occur in some people.

**L82.1** `Simple Sentence` (0.543) → `passthrough`
- original: An eye exam before starting treatment may be recommended for some people to assess their risk.

**L83.0** `Complex Sentence` (0.46) → `decomposed`
- original: Seizures: Tell your doctor if you have a history of seizures before starting this medicine, or have conditions that potentially increase your risk of seizures
  - S1: Tell your doctor if you have a history of seizures before starting this medicine.
  - S2: Tell your doctor if you have conditions that potentially increase your risk of seizures.

**L84.0** `Complex Sentence` (0.708) → `decomposed`
- original: Manic episodes Fluoxetine may trigger mania, including racing thoughts, reckless behavior, drastically reduced need for sleep, and unusual bursts of energy or irritability.
  - S1: Manic episodes may be triggered by Fluoxetine.
  - S2: These episodes include racing thoughts.
  - S3: They also include reckless behavior.
  - S4: They include a drastically reduced need for sleep.
  - S5: They include unusual bursts of energy or irritability.

**L85.0** `Complex Sentence` (0.565) → `decomposed`
- original: Changes in appetite or weight: Weight and appetite changes can occur, with some patients having significant weight loss.
  - S1: Changes in appetite or weight can occur.
  - S2: Weight and appetite changes can occur.
  - S3: Some patients have significant weight loss.

**L85.1** `Simple Sentence` (0.813) → `passthrough`
- original: Children and adolescents should have their height and weight monitored regularly during treatment.

**L86.0** `Simple Sentence` (0.847) → `passthrough`
- original: Low sodium (hyponatremia): Low blood sodium levels can occur, particularly in older adults.

**L86.1** `Simple Sentence` (0.965) → `passthrough`
- original: Symptoms include headache, weakness, confusion, and difficulty concentrating.

**L87.0** `Complex Sentence` (0.869) → `decomposed`
- original: Heart rhythm changes (QT prolongation): Fluoxetine can affect the heart's electrical activity, potentially causing a serious and life-threatening irregular heartbeat.
  - S1: Heart rhythm changes include QT prolongation.
  - S2: Fluoxetine can affect the heart's electrical activity.
  - S3: This effect can potentially cause a serious and life-threatening irregular heartbeat.

**L87.1** `Incomplete Sentence` (0.868) → `excluded_incomplete`
- original: Seek medical attention if you experience a fast, slow, or irregular heartbeat, shortness of breath, or fainting.

**L88.0** `Simple Sentence` (0.986) → `passthrough`
- original: Sexual dysfunction: SSRIs, including fluoxetine, commonly affect sexual function.

**L88.1** `Simple Sentence` (0.73) → `passthrough`
- original: In men, this may include delayed or absent ejaculation or erectile problems.
- pronoun resolved: In men, Sexual dysfunction may include delayed or absent ejaculation or erectile problems.
  - edits: “this” → “Sexual dysfunction”

**L88.2** `Simple Sentence` (0.743) → `passthrough`
- original: In women, it may include decreased libido or difficulty reaching orgasm.
- pronoun resolved: In women, Sexual dysfunction may include decreased libido or difficulty reaching orgasm.
  - edits: “it” → “Sexual dysfunction”

**L88.3** `Incomplete Sentence` (0.869) → `excluded_incomplete`
- original: Talk to your doctor if this occurs, as treatment options are available.

**L89.0** `Simple Sentence` (0.862) → `passthrough`
- original: Drowsiness and impaired concentration: This medicine may affect your ability to think clearly, make decisions, or react quickly.
- pronoun resolved: Drowsiness and impaired concentration: Fluoxetine may affect your ability to think clearly, make decisions, or react quickly.
  - edits: “This medicine” → “Fluoxetine”

**L89.1** `Incomplete Sentence` (0.809) → `excluded_incomplete`
- original: Use caution when driving or operating machinery until you know how this medication affects you.
- pronoun resolved: Use caution when driving or operating machinery until you know how Fluoxetine affects you.
  - edits: “this medication” → “Fluoxetine”

**L90.0** `Simple Sentence` (0.983) → `passthrough`
- original: Anxiety and Insomnia: May occur in some patients while taking this medicine.
- pronoun resolved: Anxiety and Insomnia: May occur in some patients while taking Fluoxetine.
  - edits: “this medicine.” → “Fluoxetine.”

**L91.0** `Compound Sentence` (0.833) → `decomposed`
- original: Blood sugar changes: People with diabetes may experience low blood sugar while taking this medicine, and high blood sugar when it is stopped.
- pronoun resolved: Blood sugar changes: People with diabetes may experience low blood sugar while taking Fluoxetine, and high blood sugar when Fluoxetine is stopped.
  - edits: “this medicine,” → “Fluoxetine,”; “it” → “Fluoxetine”
  - S1: People with diabetes may experience low blood sugar while taking Fluoxetine.
  - S2: They may experience high blood sugar when Fluoxetine is stopped.

**L91.1** `Simple Sentence` (0.975) → `passthrough`
- original: Your doctor may need to adjust your diabetes medications.

## Before taking this medicine

**L94.0** `Compound-Complex Sentence` (0.4) → `decomposed`
- original: Tell your doctor about all your medical conditions and medications before starting fluoxetine (Prozac), as some may interact with it or affect whether it is safe for you.
- pronoun resolved: Tell your doctor about all your medical conditions and medications before starting fluoxetine (Prozac), as some may interact with fluoxetine or affect whether it is safe for you.
  - edits: “it” → “fluoxetine”
  - S1: Tell your doctor about all your medical conditions.
  - S2: Tell your doctor about all your medications.
  - S3: Do this before starting fluoxetine (Prozac).
  - S4: Some medical conditions may interact with fluoxetine.
  - S5: Some medications may interact with fluoxetine.
  - S6: Some conditions or medications may affect whether fluoxetine is safe for you.

**L95.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Tell your doctor if you take any of the following medications or supplements:

**L96.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Triptans (for migraine)

**L97.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: Antidepressants or mood stabilizers, including SSRIs, SNRIs, tricyclics, MAOIs, lithium, buspirone, or antipsychotics

**L98.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Amphetamines

**L99.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Opioid pain medications, including tramadol, fentanyl, meperidine, or methadone

**L100.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Over-the-counter supplements such as St. John's Wort or tryptophan

**L101.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Electroconvulsive therapy (ECT)

**L102.0** `Complex Sentence` (0.47) → `decomposed`
- original: Many of these combinations can increase the risk of serotonin syndrome, a potentially serious condition.
  - S1: Many of these combinations can increase the risk of serotonin syndrome.
  - S2: Serotonin syndrome is a potentially serious condition.

**L103.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Tell your doctor if you have or have had any of the following:

**L104.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Liver, kidney, or heart problems

**L105.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Seizures or epilepsy

**L106.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Bipolar disorder or mania

**L107.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Low sodium levels in the blood

**L108.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: A stroke or high blood pressure

**L109.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Bleeding problems

**L110.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Pregnancy

**L111.0** `Incomplete Sentence` (0.799) → `excluded_incomplete`
- original: Tell your healthcare provider if you are pregnant, become pregnant, or plan to become pregnant while taking fluoxetine tablets.

**L111.1** `Compound-Complex Sentence` (0.871) → `decomposed`
- original: Using fluoxetine later in pregnancy may increase the risk of complications in the newborn, including problems that need a longer hospital stay, breathing support, or tube feeding, and a serious lung condition called persistent pulmonary hypertension of the newborn (PPHN).
  - S1: Using fluoxetine later in pregnancy may increase the risk of complications in the newborn.
  - S2: Some complications require a longer hospital stay.
  - S3: Some complications require breathing support.
  - S4: Some complications require tube feeding.
  - S5: A serious complication is a lung condition called persistent pulmonary hypertension of the newborn (PPHN).

**L111.2** `Compound-Complex Sentence` (0.475) → `decomposed`
- original: Untreated depression also carries risks in pregnancy, so discuss the benefits and risks of treatment with your healthcare provider rather than stopping on your own.
  - S1: Untreated depression carries risks in pregnancy.
  - S2: Discuss the benefits and risks of treatment with your healthcare provider.
  - S3: Do not stop treatment on your own.

**L112.0** `Complex Sentence` (0.911) → `decomposed`
- original: If you become pregnant while taking fluoxetine tablets, ask your healthcare provider about joining the National Pregnancy Registry for Antidepressants, which tracks pregnancy outcomes in women who take these medicines.
  - S1: If you become pregnant while taking fluoxetine tablets, ask your healthcare provider about joining the National Pregnancy Registry for Antidepressants.
  - S2: The registry tracks pregnancy outcomes in women who take these medicines.

**L112.1** `Simple Sentence` (0.921) → `passthrough`
- original: You can enroll by calling 1-866-961-2388 or visiting womensmentalhealth.org.

**L113.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Breastfeeding:

**L114.0** `Simple Sentence` (0.989) → `passthrough`
- original: Fluoxetine passes into breast milk.

**L114.1** `Compound Sentence` (0.7) → `decomposed`
- original: Tell your healthcare provider if you are breastfeeding or plan to breastfeed, and discuss the best way to feed your baby while you are taking fluoxetine tablets.
  - S1: Tell your healthcare provider if you are breastfeeding or plan to breastfeed.
  - S2: Discuss the best way to feed your baby while you are taking fluoxetine tablets.

**L114.2** `Compound Sentence` (0.509) → `decomposed`
- original: If you do breastfeed, watch your baby for agitation, irritability, poor feeding, or poor weight gain, and seek medical advice if you notice any of these.
  - S1: If you do breastfeed, watch your baby for agitation, irritability, poor feeding, or poor weight gain.
  - S2: Seek medical advice if you notice any of these.

## How should I take fluoxetine?

**L117.0** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: Take fluoxetine exactly as prescribed by your doctor.

**L117.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L117.2** `Simple Sentence` (0.984) → `passthrough`
- original: Your doctor may occasionally change your dose.

**L118.0** `Compound Sentence` (0.408) → `decomposed`
- original: Swallow the delayed-release capsule whole and do not crush, chew, break, or open it.
  - S1: Swallow the delayed-release capsule whole.
  - S2: Do not crush, chew, break, or open it.

**L119.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Measure liquid medicine carefully.

**L119.1** `Incomplete Sentence` (0.955) → `excluded_incomplete`
- original: Use the dosing syringe provided, or use a medicine dose-measuring device (not a kitchen spoon).

**L120.0** `Simple Sentence` (0.969) → `passthrough`
- original: It may take up to 4 weeks before your symptoms improve.

**L120.1** `Compound Sentence` (0.517) → `decomposed`
- original: Keep using the medication as directed and tell your doctor if your symptoms do not improve.
  - S1: Keep using the medication as directed.
  - S2: Tell your doctor if your symptoms do not improve.

**L121.0** `Compound Sentence` (0.357) → `decomposed`
- original: Tell your doctor if you have any changes in sexual function, such as loss of interest in sex, trouble having an orgasm, or (in men) problems with erections or ejaculation.
  - S1: Tell your doctor if you have any changes in sexual function.
  - S2: Such changes include loss of interest in sex.
  - S3: Such changes include trouble having an orgasm.
  - S4: Such changes include problems with erections or ejaculation in men.

**L121.1** `Simple Sentence` (0.983) → `passthrough`
- original: Some sexual problems can be treated.

**L122.0** `Compound Sentence` (0.727) → `decomposed`
- original: Do not stop using fluoxetine suddenly, or you could have unpleasant withdrawal symptoms.
  - S1: Do not stop using fluoxetine suddenly.
  - S2: You could have unpleasant withdrawal symptoms.

**L122.1** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Ask your doctor how to safely stop using fluoxetine.

**L123.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Store at room temperature away from moisture and heat.

## Fluoxetine Dosing Information

**L126.0** `Compound Sentence` (0.919) → `decomposed`
- original: Fluoxetine (Prozac) is taken orally, and your doctor will determine the right dose for you based on your condition, age, and response to treatment.
  - S1: Fluoxetine (Prozac) is taken orally.
  - S2: Your doctor will determine the right dose for you based on your condition, age, and response to treatment.

**L126.1** `Compound Sentence` (0.479) → `decomposed`
- original: Always follow your doctor's instructions, do not change your dose or stop taking this medicine without speaking to them first.
- pronoun resolved: Always follow your doctor's instructions, do not change your dose or stop taking this medicine without speaking to doctor first.
  - edits: “them” → “doctor”
  - S1: Always follow your doctor's instructions.
  - S2: Do not change your dose or stop taking this medicine without speaking to your doctor first.

**L127.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Major Depressive Disorder (MDD):

**L128.0** `Simple Sentence` (0.977) → `passthrough`
- original: Adults: Treatment typically starts at 20 mg once daily in the morning.

**L128.1** `Simple Sentence` (0.965) → `passthrough`
- original: Your doctor may increase the dose after several weeks if needed.

**L128.2** `Simple Sentence` (0.986) → `passthrough`
- original: The maximum dose is 80 mg/day.

**L129.0** `Simple Sentence` (0.975) → `passthrough`
- original: Children and adolescents (aged 8 and older): Treatment starts at 10 mg or 20 mg per day.

**L129.1** `Simple Sentence` (0.651) → `passthrough`
- original: In lower-weight children, the starting dose and target dose may remain at 10 mg/day.

**L130.0** `Compound Sentence` (0.408) → `decomposed`
- original: With all patients, the full effect of fluoxetine for depression may take 4 weeks or longer.
  - S1: With all patients, the full effect of fluoxetine for depression may take 4 weeks or longer.

**L131.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Obsessive Compulsive Disorder (OCD):

**L132.0** `Compound Sentence` (0.484) → `decomposed`
- original: Adult dose: Treatment starts at 20 mg once daily in the morning and may be increased after several weeks if there is a lack of clinical improvement.
  - S1: Adult dose: Treatment starts at 20 mg once daily in the morning.
  - S2: It may be increased after several weeks if there is a lack of clinical improvement.

**L132.1** `Simple Sentence` (0.977) → `passthrough`
- original: The recommended dose range is 20 mg to 60 mg per day.

**L132.2** `Simple Sentence` (0.982) → `passthrough`
- original: Full therapeutic effect may take 5 weeks or longer.

**L133.0** `Simple Sentence` (0.794) → `passthrough`
- original: Adolescents and higher-weight children (aged 7 and older): Treatment starts at 10 mg/day, increasing to 20 mg/day after 2 weeks.

**L133.1** `Simple Sentence` (0.344) → `passthrough`
- original: Additional dose increases may be considered after several more weeks if insufficient clinical improvement is observed.

**L133.2** `Simple Sentence` (0.977) → `passthrough`
- original: The recommended dose range is 20 mg to 60 mg per day.

**L134.0** `Simple Sentence` (0.452) → `passthrough`
- original: Lower-weight children: Treatment starts at 10 mg/day with dose increases after several more weeks if there is a lack of clinical improvement.

**L134.1** `Compound Sentence` (0.892) → `decomposed`
- original: The recommended dose range of 20 mg to 30 mg per day, although experience with daily doses greater than 20 mg is very minimal,
  - S1: The recommended dose range is 20 mg to 30 mg per day.
  - S2: Experience with daily doses greater than 20 mg is very minimal.

**L135.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Bulimia Nervosa:

**L136.0** `Simple Sentence` (0.978) → `passthrough`
- original: Adult dose: The recommended dose is 60 mg once daily in the morning.

**L136.1** `Simple Sentence` (0.978) → `passthrough`
- original: Your doctor may gradually increase your dose to this level over several days.

**L136.2** `Complex Sentence` (0.418) → `decomposed`
- original: Clinical trials showed that the 60 mg dose was effective in reducing binge-eating and purging behaviors.
  - S1: Clinical trials showed that the 60 mg dose was effective.
  - S2: The 60 mg dose was effective in reducing binge-eating and purging behaviors.

**L137.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Panic Disorder:

**L138.0** `Simple Sentence` (0.947) → `passthrough`
- original: Adult dose: Treatment starts at 10 mg/day, increasing to 20 mg/day after one week.

**L138.1** `Simple Sentence` (0.969) → `passthrough`
- original: Your doctor may adjust the dose after several weeks if needed.

**L138.2** `Compound Sentence` (0.962) → `decomposed`
- original: Clinical trials used a dose range of 10 mg/day to 60 mg/day, but the most commonly used dose in clinical trials was 20 mg/day.
  - S1: Clinical trials used a dose range of 10 mg/day to 60 mg/day.
  - S2: The most commonly used dose in clinical trials was 20 mg/day.

**L139.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: General Dosing Notes:

**L140.0** `Simple Sentence` (0.973) → `passthrough`
- original: Fluoxetine is usually taken in the morning to minimize the risk of sleep disturbances

**L141.0** `Compound Sentence` (0.599) → `decomposed`
- original: It may take several weeks to feel the full benefit of fluoxetine, do not stop taking it without talking to your doctor first
- pronoun resolved: It may take several weeks to feel the full benefit of fluoxetine, do not stop taking fluoxetine without talking to your doctor first
  - edits: “it” → “fluoxetine”
  - S1: It may take several weeks to feel the full benefit of fluoxetine.
  - S2: Do not stop taking fluoxetine without talking to your doctor first.

**L142.0** `Simple Sentence` (0.974) → `passthrough`
- original: Your doctor will periodically reassess whether you need to continue treatment

**L143.0** `Compound Sentence` (0.662) → `decomposed`
- original: Older adults may need a lower dose or may take fluoxetine less frequently than younger adults
  - S1: Older adults may need a lower dose.
  - S2: Older adults may take fluoxetine less frequently than younger adults.

**L144.0** `Simple Sentence` (0.967) → `passthrough`
- original: People with liver problems may also require a lower or less frequent dose

**L145.0** `Complex Sentence` (0.684) → `decomposed`
- original: If you have other medical conditions or take multiple medications, your doctor may need to adjust your fluoxetine dose accordingly
  - S1: Your doctor may need to adjust your fluoxetine dose accordingly.
  - S2: This is needed if you have other medical conditions.
  - S3: This is also needed if you take multiple medications.

## What happens if I miss a dose?

**L148.0** `Compound Sentence` (0.555) → `decomposed`
- original: Take the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - S1: Take the medicine as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L148.1** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

## What happens if I overdose?

**L151.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

## What to avoid

**L154.0** `Simple Sentence` (0.99) → `passthrough`
- original: Drinking alcohol can increase certain side effects of fluoxetine.

**L155.0** `Incomplete Sentence` (0.971) → `excluded_incomplete`
- original: Avoid driving or hazardous activity until you know how fluoxetine will affect you.

**L155.1** `Simple Sentence` (0.878) → `passthrough`
- original: Your reactions could be impaired.

## What other drugs will affect fluoxetine?

**L158.0** `Simple Sentence` (0.977) → `passthrough`
- original: Using fluoxetine with other drugs that make you drowsy can worsen this effect.

**L158.1** `Incomplete Sentence` (0.573) → `excluded_incomplete`
- original: Ask your doctor before using opioid medication, a sleeping pill, a muscle relaxer, or medicine for anxiety or seizures.

**L159.0** `Simple Sentence` (0.366) → `passthrough`
- original: Ask your doctor before taking a nonsteroidal anti-inflammatory drug (NSAID) such as aspirin, ibuprofen (Advil, Motrin), naproxen (Aleve), celecoxib (Celebrex), diclofenac, indomethacin, meloxicam, and others.

**L159.1** `Simple Sentence` (0.985) → `passthrough`
- original: Using an NSAID with fluoxetine may cause you to bruise or bleed easily.

**L160.0** `Compound-Complex Sentence` (0.628) → `decomposed`
- original: Fluoxetine can cause a serious heart problem, and your risk may be higher if you also use certain other medicines for infections, asthma, heart problems, high blood pressure, depression, mental illness, cancer, malaria, or HIV.
  - S1: Fluoxetine can cause a serious heart problem.
  - S2: Your risk of this heart problem may be higher if you also use certain other medicines.
  - S3: These other medicines are used for infections.
  - S4: These other medicines are used for asthma.
  - S5: These other medicines are used for heart problems.
  - S6: These other medicines are used for high blood pressure.
  - S7: These other medicines are used for depression.
  - S8: These other medicines are used for mental illness.
  - S9: These other medicines are used for cancer.
  - S10: These other medicines are used for malaria.
  - S11: These other medicines are used for HIV.

**L161.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Tell your doctor about all your current medicines.

**L161.1** `Simple Sentence` (0.989) → `passthrough`
- original: Many drugs can affect fluoxetine, especially:

**L162.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: any other antidepressant;

**L163.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: St. John's Wort;

**L164.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: tryptophan (sometimes called L-tryptophan);

**L165.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a blood thinner - warfarin, Coumadin, Jantoven;

**L166.0** `Incomplete Sentence` (0.975) → `excluded_incomplete`
- original: medicine to treat anxiety, mood disorders, thought disorders, or mental illness - amitriptyline, buspirone, desipramine, lithium, nortriptyline, and many others;

**L167.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: medicine to treat ADHD or narcolepsy - Adderall, Concerta, Ritalin, Vyvanse, Zenzedi, and others;

**L168.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: migraine headache medicine - rizatriptan, sumatriptan, zolmitriptan, and others; or

**L169.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: narcotic pain medicine - fentanyl, tramadol.

**L170.0** `Simple Sentence` (0.588) → `passthrough`
- original: This list is not complete and many other drugs may affect fluoxetine.

**L170.1** `Incomplete Sentence` (0.491) → `excluded_incomplete`
- original: This includes prescription and over-the-counter medicines, vitamins, and herbal products.
- pronoun resolved: List includes prescription and over-the-counter medicines, vitamins, and herbal products.
  - edits: “This” → “List”

**L170.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.

## Fluoxetine FAQ

**L173.0** `Incomplete Sentence` (0.961) → `excluded_incomplete`
- original: Is 40mg of fluoxetine a high dose?

**L174.0** `Simple Sentence` (0.802) → `passthrough`
- original: 40mg of fluoxetine is considered a moderate maintenance dose in adults for major depressive disorder (MDD) and OCD.

**L174.1** `Compound Sentence` (0.862) → `decomposed`
- original: The standard starting dose for most conditions is 20mg per day, except for panic disorder, which starts at 10mg.
  - S1: The standard starting dose for most conditions is 20mg per day.
  - S2: The starting dose for panic disorder is 10mg.

**L174.2** `Compound Sentence` (0.803) → `decomposed`
- original: If symptoms have not improved after several weeks, the dose may be increased, up to 40mg for MDD and OCD, or 20mg for panic disorder.
  - S1: If symptoms have not improved after several weeks, the dose may be increased.
  - S2: The dose may be increased up to 40mg for MDD and OCD.
  - S3: The dose may be increased up to 20mg for panic disorder.

**L174.3** `Simple Sentence` (0.98) → `passthrough`
- original: The recommended dose for bulimia is 60mg per day.

**L174.4** `Simple Sentence` (0.915) → `passthrough`
- original: Your doctor will determine the right dose for you based on your condition and response to treatment.

**L175.0** `Incomplete Sentence` (0.954) → `excluded_incomplete`
- original: Does fluoxetine cause weight gain?

**L175.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L176.0** `Simple Sentence` (0.949) → `passthrough`
- original: Fluoxetine is less likely to cause weight gain than many other antidepressants.

**L176.1** `Complex Sentence` (0.905) → `decomposed`
- original: In the short term, it can actually cause mild weight loss due to reduced appetite, which is one of its common side effects.
- pronoun resolved: In the short term, Fluoxetine can actually cause mild weight loss due to reduced appetite, which is one of Fluoxetine's common side effects.
  - edits: “it” → “Fluoxetine”; “its” → “Fluoxetine's”
  - S1: In the short term, Fluoxetine can cause mild weight loss.
  - S2: This weight loss is due to reduced appetite.
  - S3: Reduced appetite is one of Fluoxetine's common side effects.

**L176.2** `Simple Sentence` (0.472) → `passthrough`
- original: However, some people do experience weight changes over longer-term use.

**L176.3** `Complex Sentence` (0.854) → `decomposed`
- original: If you notice significant weight changes while taking this medicine, speak to your doctor, as dose adjustments or alternative treatments may be available.
- pronoun resolved: If you notice significant weight changes while taking Fluoxetine, speak to your doctor, as dose adjustments or alternative treatments may be available.
  - edits: “this medicine,” → “Fluoxetine,”
  - S1: If you notice significant weight changes while taking Fluoxetine, speak to your doctor.
  - S2: Dose adjustments or alternative treatments may be available.

**L177.0** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: How long does fluoxetine take to work?

**L177.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L178.0** `Simple Sentence` (0.83) → `passthrough`
- original: Most people need to take fluoxetine for 4 to 6 weeks before feeling the full effects.

**L178.1** `Compound Sentence` (0.82) → `decomposed`
- original: Some improvement in sleep, appetite, or energy levels may be noticeable within the first 1 to 2 weeks, but mood and motivation typically take longer to improve.
  - S1: Some improvement in sleep, appetite, or energy levels may be noticeable within the first 1 to 2 weeks.
  - S2: Mood and motivation typically take longer to improve.

**L178.2** `Complex Sentence` (0.622) → `decomposed`
- original: For obsessive-compulsive disorder (OCD), it may take 5 weeks or longer to see the full benefit.
- pronoun resolved: For obsessive-compulsive disorder (OCD), obsessive-compulsive disorder (OCD) may take 5 weeks or longer to see the full benefit.
  - edits: “it” → “obsessive-compulsive disorder (OCD)”
  - S1: For obsessive-compulsive disorder (OCD), the full benefit may take 5 weeks or longer to see.
  - S2: Obsessive-compulsive disorder (OCD) is the condition being discussed.

**L178.3** `Complex Sentence` (0.566) → `decomposed`
- original: It is important to keep taking this medicine as prescribed, even if you do not feel immediate improvement.
- pronoun resolved: It is important to keep taking fluoxetine as prescribed, even if you do not feel immediate improvement.
  - edits: “this medicine” → “fluoxetine”
  - S1: It is important to keep taking fluoxetine as prescribed.
  - S2: You should continue even if you do not feel immediate improvement.

**L178.4** `Incomplete Sentence` (0.706) → `excluded_incomplete`
- original: Do not stop without speaking to your doctor first.

**L179.0** `Incomplete Sentence` (0.971) → `excluded_incomplete`
- original: Is fluoxetine a controlled substance?

**L179.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L180.0** `Simple Sentence` (0.917) → `passthrough`
- original: No, fluoxetine is not a controlled substance.

**L180.1** `Complex Sentence` (0.742) → `decomposed`
- original: It is not classified under the DEA Controlled Substances Act, meaning it does not have recognized potential for dependence or abuse in the way that drugs like opioids or benzodiazepines do.
- pronoun resolved: It is not classified under the DEA Controlled Substances Act, meaning fluoxetine does not have recognized potential for dependence or abuse in the way that drugs like opioids or benzodiazepines do.
  - edits: “it” → “fluoxetine”
  - S1: It is not classified under the DEA Controlled Substances Act.
  - S2: This means fluoxetine does not have a recognized potential for dependence or abuse.
  - S3: Drugs like opioids or benzodiazepines do have this potential.

**L180.2** `Compound Sentence` (0.912) → `decomposed`
- original: It is, however, a prescription-only medicine, so it still requires a valid prescription from a licensed healthcare provider.
- pronoun resolved: Fluoxetine is, however, a prescription-only medicine, so fluoxetine still requires a valid prescription from a licensed healthcare provider.
  - edits: “It” → “Fluoxetine”; “it” → “fluoxetine”
  - S1: Fluoxetine is, however, a prescription-only medicine.
  - S2: Fluoxetine still requires a valid prescription from a licensed healthcare provider.

**L181.0** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: Is fluoxetine an SSRI?

**L181.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L182.0** `Simple Sentence` (0.967) → `passthrough`
- original: Yes, fluoxetine is a selective serotonin reuptake inhibitor (SSRI).

**L182.1** `Complex Sentence` (0.929) → `decomposed`
- original: SSRIs work by blocking the reabsorption (reuptake) of serotonin in the brain, increasing the amount of serotonin available between nerve cells.
  - S1: SSRIs work by blocking the reabsorption of serotonin in the brain.
  - S2: This process increases the amount of serotonin available between nerve cells.

**L182.2** `Simple Sentence` (0.925) → `passthrough`
- original: Serotonin is a neurotransmitter that helps regulate mood, emotions, and sleep.

**L182.3** `Compound Sentence` (0.885) → `decomposed`
- original: Prozac was one of the first SSRIs approved and remains one of the most widely prescribed antidepressants worldwide.
  - S1: Prozac was one of the first SSRIs approved.
  - S2: It remains one of the most widely prescribed antidepressants worldwide.

**L183.0** `Incomplete Sentence` (0.97) → `excluded_incomplete`
- original: What are the side effects of fluoxetine in females?

**L183.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L184.0** `Compound Sentence` (0.968) → `decomposed`
- original: Females may experience all of the common fluoxetine side effects, but some side effects are particularly relevant to women:
  - S1: Females may experience all of the common fluoxetine side effects.
  - S2: Some side effects are particularly relevant to women.

**L185.0** `Simple Sentence` (0.416) → `passthrough`
- original: Sexual side effects are common, including decreased sex drive (libido) and difficulty reaching orgasm.

**L185.1** `Compound Sentence` (0.867) → `decomposed`
- original: These can affect quality of life and should be discussed with your doctor, as treatment options are available.
- pronoun resolved: Sexual side effects can affect quality of life and should be discussed with your doctor, as treatment options are available.
  - edits: “These” → “Sexual side effects”
  - S1: Sexual side effects can affect quality of life.
  - S2: They should be discussed with your doctor.
  - S3: Treatment options are available.

**L186.0** `Compound Sentence` (0.795) → `decomposed`
- original: Weight changes - it may cause mild weight loss initially, though longer-term weight changes can occur.
- pronoun resolved: Weight changes - Fluoxetine may cause mild weight loss initially, though longer-term weight changes can occur.
  - edits: “it” → “Fluoxetine”
  - S1: Fluoxetine may cause mild weight loss initially.
  - S2: Longer-term weight changes can occur.

**L187.0** `Compound Sentence` (0.726) → `decomposed`
- original: Menstrual changes - some women report changes to their menstrual cycle, though this is not among the most commonly reported side effects.
- pronoun resolved: Menstrual changes - some women report changes to their menstrual cycle, though Menstrual changes is not among the most commonly reported side effects.
  - edits: “this” → “Menstrual changes”
  - S1: Some women report changes to their menstrual cycle.
  - S2: Menstrual changes is not among the most commonly reported side effects.

**L188.0** `Simple Sentence` (0.959) → `passthrough`
- original: Pregnancy - taking this medicine in late pregnancy may increase the risk of certain complications in newborns.
- pronoun resolved: Pregnancy - taking Fluoxetine in late pregnancy may increase the risk of certain complications in newborns.
  - edits: “this medicine” → “Fluoxetine”

**L188.1** `Complex Sentence` (0.899) → `decomposed`
- original: Women who are pregnant, planning to become pregnant, or breastfeeding should discuss the risks and benefits with their doctor before continuing or starting this medicine.
  - S1: Women who are pregnant, planning to become pregnant, or breastfeeding should discuss the risks and benefits with their doctor.
  - S2: These women should do this before continuing or starting this medicine.

**L189.0** `Incomplete Sentence` (0.894) → `excluded_incomplete`
- original: Does fluoxetine (Prozac) help with anxiety?

**L189.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L190.0** `Compound Sentence` (0.553) → `decomposed`
- original: Fluoxetine is not FDA-approved specifically for generalized anxiety disorder, but it is FDA-approved to treat panic disorder, which is a type of anxiety disorder.
- pronoun resolved: Fluoxetine is not FDA-approved specifically for generalized anxiety disorder, but Fluoxetine is FDA-approved to treat panic disorder, which is a type of anxiety disorder.
  - edits: “it” → “Fluoxetine”
  - S1: Fluoxetine is not FDA-approved specifically for generalized anxiety disorder.
  - S2: Fluoxetine is FDA-approved to treat panic disorder.
  - S3: Panic disorder is a type of anxiety disorder.

**L190.1** `Compound Sentence` (0.51) → `decomposed`
- original: It is also approved for obsessive-compulsive disorder (OCD), which has a significant anxiety component.
- pronoun resolved: Fluoxetine is also approved for obsessive-compulsive disorder (OCD), which has a significant anxiety component.
  - edits: “It” → “Fluoxetine”
  - S1: Fluoxetine is also approved for obsessive-compulsive disorder (OCD).
  - S2: OCD has a significant anxiety component.

**L191.0** `Complex Sentence` (0.597) → `decomposed`
- original: Although not FDA-approved for generalized anxiety disorder, it is sometimes prescribed off-label by doctors for anxiety symptoms, as SSRIs are a well-established treatment class for anxiety conditions.
- pronoun resolved: Although not FDA-approved for generalized anxiety disorder, Fluoxetine is sometimes prescribed off-label by doctors for anxiety symptoms, as SSRIs are a well-established treatment class for anxiety conditions.
  - edits: “it” → “Fluoxetine”
  - S1: Fluoxetine is sometimes prescribed off-label by doctors for anxiety symptoms.
  - S2: Fluoxetine is not FDA-approved for generalized anxiety disorder.
  - S3: SSRIs are a well-established treatment class for anxiety conditions.

**L191.1** `Compound Sentence` (0.601) → `decomposed`
- original: Off-label means the drug is being used in a way not specifically approved by the FDA, but supported by clinical evidence.
  - S1: Off-label means the drug is being used in a way not specifically approved by the FDA.
  - S2: It is supported by clinical evidence.

**L192.0** `Compound-Complex Sentence` (0.839) → `decomposed`
- original: If you experience anxiety alongside depression, fluoxetine may help both, as it is FDA-approved for major depressive disorder and depression and anxiety commonly occur together.
- pronoun resolved: If you experience anxiety alongside depression, fluoxetine may help both, as fluoxetine is FDA-approved for major depressive disorder and depression and anxiety commonly occur together.
  - edits: “it” → “fluoxetine”
  - S1: You may experience anxiety alongside depression.
  - S2: Fluoxetine may help both anxiety and depression.
  - S3: Fluoxetine is FDA-approved for major depressive disorder.
  - S4: Depression and anxiety commonly occur together.

**L193.0** `Incomplete Sentence` (0.962) → `excluded_incomplete`
- original: Talk to your doctor about whether fluoxetine is appropriate for your anxiety symptoms.

**L194.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: How long does fluoxetine stay in your system?

**L194.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L195.0** `Simple Sentence` (0.987) → `passthrough`
- original: Fluoxetine stays in your system longer than most other antidepressants.

**L195.1** `Compound-Complex Sentence` (0.887) → `decomposed`
- original: After stopping this medicine, it takes approximately 1 to 4 days for the drug itself to be reduced by half, but fluoxetine also converts in the body to an active metabolite called norfluoxetine, which has a much longer half-life of 4 to 16 days.
- pronoun resolved: After stopping this medicine, Fluoxetine takes approximately 1 to 4 days for Fluoxetine itself to be reduced by half, but fluoxetine also converts in the body to an active metabolite called norfluoxetine, which has a much longer half-life of 4 to 16 days.
  - edits: “it” → “Fluoxetine”; “the drug” → “Fluoxetine”
  - S1: After stopping this medicine, Fluoxetine takes approximately 1 to 4 days for Fluoxetine itself to be reduced by half.
  - S2: Fluoxetine converts in the body to an active metabolite called norfluoxetine.
  - S3: Norfluoxetine has a much longer half-life of 4 to 16 days.

**L195.2** `Compound Sentence` (0.416) → `decomposed`
- original: This means this medicine and its active metabolite can remain detectable in your system for up to 5 weeks after your last dose.
- pronoun resolved: This means Fluoxetine and Fluoxetine's active metabolite can remain detectable in your system for up to 5 weeks after your last dose.
  - edits: “this medicine” → “Fluoxetine”; “its” → “Fluoxetine's”
  - S1: This means Fluoxetine can remain detectable in your system for up to 5 weeks after your last dose.
  - S2: Fluoxetine's active metabolite can also remain detectable in your system for up to 5 weeks after your last dose.

**L196.0** `Simple Sentence` (0.915) → `passthrough`
- original: This is clinically important for two reasons:

**L197.0** `Complex Sentence` (0.909) → `decomposed`
- original: Switching medications: If you are switching from fluoxetine to certain other antidepressants, particularly MAOIs, your doctor will require a washout period of at least 5 weeks to allow fluoxetine to fully clear your system and avoid dangerous drug interactions.
  - S1: Switching medications requires a washout period.
  - S2: This applies if you are switching from fluoxetine to certain other antidepressants.
  - S3: These other antidepressants include MAOIs.
  - S4: Your doctor will require a washout period of at least 5 weeks.
  - S5: This period allows fluoxetine to fully clear your system.
  - S6: This avoids dangerous drug interactions.

**L198.0** `Complex Sentence` (0.918) → `decomposed`
- original: Stopping fluoxetine: The long half-life means withdrawal symptoms are generally milder with this medicine than with shorter-acting antidepressants, as the drug tapers itself out of your system gradually.
- pronoun resolved: Stopping fluoxetine: The long half-life means withdrawal symptoms are generally milder with Fluoxetine than with shorter-acting antidepressants, as Fluoxetine tapers itself out of your system gradually.
  - edits: “this medicine” → “Fluoxetine”; “the drug” → “Fluoxetine”
  - S1: Stopping fluoxetine.
  - S2: The long half-life means withdrawal symptoms are generally milder with Fluoxetine than with shorter-acting antidepressants.
  - S3: Fluoxetine tapers itself out of your system gradually.

**L199.0** `Incomplete Sentence` (0.767) → `excluded_incomplete`
- original: Always talk to your doctor before stopping fluoxetine or switching to another medication.

## Popular FAQ

**L202.0** `Incomplete Sentence` (0.89) → `excluded_incomplete`
- original: Q: What does Prozac feel like when it starts working?
- pronoun resolved: Q: What does Prozac feel like when Prozac starts working?
  - edits: “it” → “Prozac”

**L202.1** `Simple Sentence` (0.9) → `passthrough`
- original: A: Most people feel lower levels of anxiety, restlessness and tiredness when Prozac first starts to work.

**L202.2** `Compound Sentence` (0.944) → `decomposed`
- original: Your sleep, energy and appetite may improve over the first month and you may have a better focus on daily tasks.
  - S1: Your sleep, energy and appetite may improve over the first month.
  - S2: You may have a better focus on daily tasks.

**L202.3** `Compound Sentence` (0.424) → `decomposed`
- original: However, a depressed mood can take 6 to 8 weeks to fully respond to treatment.
  - S1: However, a depressed mood can take 6 to 8 weeks to fully respond to treatment.

**L203.0** `Incomplete Sentence` (0.958) → `excluded_incomplete`
- original: Q: What drugs can cause serotonin syndrome?

**L203.1** `Complex Sentence` (0.807) → `decomposed`
- original: A: Common drug classes that can cause serotonin syndrome include selective serotonin reuptake inhibitors (SSRIs), monoamine oxidase inhibitors (MAOIs), and opioids like tramadol.
  - S1: Common drug classes that can cause serotonin syndrome include selective serotonin reuptake inhibitors (SSRIs), monoamine oxidase inhibitors (MAOIs), and opioids like tramadol.

**L204.0** `Complex Sentence` (0.512) → `decomposed`
- original: Q: Prozac vs Zoloft: Understanding the Differences Between Two Popular Antidepressants A: Prozac and Zoloft represent two of the most widely prescribed antidepressant medications in the United States.
  - S1: Prozac and Zoloft represent two of the most widely prescribed antidepressant medications.
  - S2: These medications are in the United States.

**L204.1** `Complex Sentence` (0.92) → `decomposed`
- original: Both medications belong to a class of drugs known as selective serotonin reuptake inhibitors (SSRIs), which have revolutionized depression treatment since their introduction in the late 1980s and early 1990s.
  - S1: Both medications belong to a class of drugs known as selective serotonin reuptake inhibitors (SSRIs).
  - S2: SSRIs have revolutionized depression treatment since their introduction in the late 1980s and early 1990s.

**L205.0** `Incomplete Sentence` (0.961) → `excluded_incomplete`
- original: Q: Is Prozac (fluoxetine) safe for dogs?

**L205.1** `Complex Sentence` (0.942) → `decomposed`
- original: A: Studies have shown fluoxetine (Prozac, Reconcile), when prescribed by your veterinarian, is usually a safe and effective medicine for dogs for the treatment of behavioral disorders like separation anxiety.
  - S1: Studies have shown fluoxetine is usually a safe and effective medicine for dogs.
  - S2: Fluoxetine is used for the treatment of behavioral disorders like separation anxiety.
  - S3: Fluoxetine is safe and effective when prescribed by your veterinarian.

**L205.2** `Simple Sentence` (0.985) → `passthrough`
- original: It is most effective when used in conjunction with a behavior modification plan for your pet.
- pronoun resolved: Fluoxetine is most effective when used in conjunction with a behavior modification plan for your pet.
  - edits: “It” → “Fluoxetine”

**L205.3** `Simple Sentence` (0.76) → `passthrough`
- original: Do not give your dog Prozac or fluoxetine unless it has been prescribed by your veterinarian.
- pronoun resolved: Do not give your dog Prozac or fluoxetine unless Prozac has been prescribed by your veterinarian.
  - edits: “it” → “Prozac”
