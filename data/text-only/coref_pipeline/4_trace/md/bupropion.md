# Bupropion — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/bupropion.txt` · 198 sentences · 30 changed by pronoun resolution · 318 sentences sent to EDC

## What is bupropion?

**L5.0** `Simple Sentence` (0.978) → `passthrough`
- original: Bupropion is an antidepressant medication used to treat depression and seasonal affective disorder.

**L5.1** `Simple Sentence` (0.983) → `passthrough`
- original: It also supports smoking cessation and weight management.
- pronoun resolved: Bupropion also supports smoking cessation and weight management.
  - edits: “It” → “Bupropion”

**L5.2** `Compound Sentence` (0.958) → `decomposed`
- original: Bupropion is the active ingredient in Wellbutrin and Zyban, Auvelity contains bupropion and dextromethorphan, and Contrave contains bupropion and naltrexone.
  - S1: Bupropion is the active ingredient in Wellbutrin and Zyban.
  - S2: Auvelity contains bupropion and dextromethorphan.
  - S3: Contrave contains bupropion and naltrexone.

**L5.3** `Compound Sentence` (0.964) → `decomposed`
- original: Bupropion improves mood regulation and nicotine cravings and, when combined with naltrexone, helps reduce food intake.
  - S1: Bupropion improves mood regulation.
  - S2: Bupropion improves nicotine cravings.
  - S3: When combined with naltrexone, bupropion helps reduce food intake.

**L6.0** `Complex Sentence` (0.805) → `decomposed`
- original: Bupropion is thought to work by changing levels of certain chemicals in the brain, including noradrenaline and dopamine.
  - S1: Bupropion is thought to work by changing levels of certain chemicals in the brain.
  - S2: These chemicals include noradrenaline and dopamine.

**L7.0** `Simple Sentence` (0.962) → `passthrough`
- original: Bupropion first became an FDA-approved medicine on 30 December 1985.

## What is bupropion used to treat?

**L10.0** `Simple Sentence` (0.99) → `passthrough`
- original: The brands of bupropion are FDA-approved for specific conditions.

**L11.0** `Simple Sentence` (0.989) → `passthrough`
- original: Wellbutrin SR is used to treat major depressive disorder.

**L12.0** `Simple Sentence` (0.985) → `passthrough`
- original: Wellbutrin XL is used to treat MDD and seasonal affective disorder (SAD).

**L13.0** `Simple Sentence` (0.991) → `passthrough`
- original: Aplenzin is used to treat MDD and SAD.

**L14.0** `Simple Sentence` (0.984) → `passthrough`
- original: Zyban (discontinued) was used to help stop smoking.

**L15.0** `Simple Sentence` (0.987) → `passthrough`
- original: Auvelity (bupropion with dextromethorphan) is used to treat MDD in adults.

**L16.0** `Simple Sentence` (0.98) → `passthrough`
- original: Contrave (bupropion and naltrexone) is used for weight management for specific patients.

**L17.0** `Compound Sentence` (0.793) → `decomposed`
- original: The information on this page is only about bupropion, and not bupropion with dextromethorphan (Auvelity) or bupropion with naltrexone (Contrave).
  - S1: The information on this page is only about bupropion.
  - S2: It is not about bupropion with dextromethorphan (Auvelity).
  - S3: It is not about bupropion with naltrexone (Contrave).

## Bupropion side effects

**L20.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Common bupropion side effects:

**L21.0** `Simple Sentence` (0.779) → `passthrough`
- original: The most common side effects may include:

**L22.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: dry mouth, sore throat, stuffy nose;

**L23.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: ringing in the ears;

**L24.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: blurred vision;

**L25.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: nausea, vomiting, stomach pain, loss of appetite, constipation;

**L26.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: sleep problems (insomnia);

**L27.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: tremors, sweating, feeling anxious or nervous;

**L28.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: fast heartbeats;

**L29.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: confusion, agitation, hostility;

**L30.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: rash;

**L31.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: weight loss;

**L32.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: increased urination;

**L33.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: headache, dizziness; or muscle or joint pain.

**L34.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious bupropion side effects:

**L35.0** `Compound Sentence` (0.379) → `decomposed`
- original: Get emergency medical help if you have any of these signs of an allergic reaction to bupropion: (hives, itching, fever, swollen glands, difficult breathing, swelling in your face or throat) or a severe skin reaction (fever, sore throat, burning eyes, skin pain, red or purple skin rash with blistering and peeling).
  - S1: Get emergency medical help if you have any of these signs of an allergic reaction to bupropion: hives, itching, fever, swollen glands, difficult breathing, or swelling in your face or throat.
  - S2: Get emergency medical help if you have a severe skin reaction: fever, sore throat, burning eyes, skin pain, or a red or purple skin rash with blistering and peeling.

**L36.0** `Compound-Complex Sentence` (0.434) → `decomposed`
- original: Report any new or worsening symptoms to your doctor, such as: mood or behavior changes, anxiety, depression, panic attacks, trouble sleeping, or if you feel impulsive, irritable, agitated, hostile, aggressive, restless, hyperactive (mentally or physically), more depressed, or have thoughts about suicide or hurting yourself.
  - S1: Report any new or worsening symptoms to your doctor.
  - S2: Mood or behavior changes are new or worsening symptoms.
  - S3: Anxiety is a new or worsening symptom.
  - S4: Depression is a new or worsening symptom.
  - S5: Panic attacks are new or worsening symptoms.
  - S6: Trouble sleeping is a new or worsening symptom.
  - S7: Feeling impulsive is a new or worsening symptom.
  - S8: Feeling irritable is a new or worsening symptom.
  - S9: Feeling agitated is a new or worsening symptom.
  - S10: Feeling hostile is a new or worsening symptom.
  - S11: Feeling aggressive is a new or worsening symptom.
  - S12: Feeling restless is a new or worsening symptom.
  - S13: Feeling hyperactive mentally is a new or worsening symptom.
  - S14: Feeling hyperactive physically is a new or worsening symptom.
  - S15: Feeling more depressed is a new or worsening symptom.
  - S16: Having thoughts about suicide is a new or worsening symptom.
  - S17: Having thoughts about hurting yourself is a new or worsening symptom.

**L37.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L38.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a seizure (convulsions);

**L39.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: confusion, unusual changes in mood or behavior;

**L40.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: blurred vision, tunnel vision, eye pain or swelling, or seeing halos around lights;

**L41.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: fast or irregular heartbeats; or

**L42.0** `Incomplete Sentence` (0.893) → `excluded_incomplete`
- original: a manic episode - racing thoughts, increased energy, reckless behavior, feeling extremely happy or irritable, talking more than usual, severe problems with sleep.

**L43.0** `Compound Sentence` (0.545) → `decomposed`
- original: This is not a complete list of side effects, and others may occur.
  - S1: This is not a complete list of side effects.
  - S2: Others may occur.

**L43.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L43.2** `Simple Sentence` (0.97) → `passthrough`
- original: You may report side effects to the FDA at 1-800-FDA-1088.

## Warnings

**L46.0** `Complex Sentence` (0.541) → `decomposed`
- original: You should not take bupropion if you have seizures, an eating disorder, or suddenly stopped using alcohol, seizure medication, or sedatives.
  - S1: You should not take bupropion if you have seizures.
  - S2: You should not take bupropion if you have an eating disorder.
  - S3: You should not take bupropion if you suddenly stopped using alcohol.
  - S4: You should not take bupropion if you suddenly stopped using seizure medication.
  - S5: You should not take bupropion if you suddenly stopped using sedatives.

**L46.1** `Compound-Complex Sentence` (0.439) → `decomposed`
- original: You should not take two medicines together that contain bupropion for example, if you take Wellbutrin for depression, you should not also take Contrave for weight control or Aplenzin for depression.
  - S1: You should not take two medicines together that contain bupropion.
  - S2: Wellbutrin is used for depression.
  - S3: Contrave is used for weight control.
  - S4: Aplenzin is used for depression.
  - S5: If you take Wellbutrin for depression, you should not also take Contrave for weight control.
  - S6: If you take Wellbutrin for depression, you should not also take Aplenzin for depression.

**L47.0** `Compound Sentence` (0.527) → `decomposed`
- original: Do not use bupropion within 14 days before or 14 days after you have used a MAO inhibitors, such as isocarboxazid, linezolid, methylene blue injection, phenelzine, rasagiline, selegiline, or tranylcypromine.
  - S1: Do not use bupropion within 14 days before you have used a MAO inhibitor.
  - S2: Do not use bupropion within 14 days after you have used a MAO inhibitor.
  - S3: Examples of MAO inhibitors include isocarboxazid, linezolid, methylene blue injection, phenelzine, rasagiline, selegiline, and tranylcypromine.

**L48.0** `Simple Sentence` (0.96) → `passthrough`
- original: Some young people (up to 24 years of age) have thoughts about suicide when first taking this medicine.

**L48.1** `Incomplete Sentence` (0.9) → `excluded_incomplete`
- original: Stay alert to changes in your mood or symptoms.

**L48.2** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Report any new or worsening symptoms to your doctor.

**L49.0** `Compound-Complex Sentence` (0.548) → `decomposed`
- original: You should know that your mental health may change in unexpected ways when you take bupropion or other antidepressants even if you are an adult over age 24 or if you do not have a mental illness and you are taking bupropion to treat a different type of condition.
  - S1: You should know that your mental health may change in unexpected ways.
  - S2: This change may happen when you take bupropion.
  - S3: This change may happen when you take other antidepressants.
  - S4: This can occur even if you are an adult over age 24.
  - S5: This can occur even if you do not have a mental illness.
  - S6: This can occur even if you are taking bupropion to treat a different type of condition.

**L49.1** `Compound Sentence` (0.588) → `decomposed`
- original: You may become suicidal, especially at the beginning of your treatment and any time that your dose is increased or decreased.
  - S1: You may become suicidal.
  - S2: This may happen especially at the beginning of your treatment.
  - S3: It may also happen any time that your dose is increased or decreased.

**L49.2** `Complex Sentence` (0.808) → `decomposed`
- original: You, your family, or your caregiver should call your doctor right away if you experience any of the following symptoms: new or worsening depression; thinking about harming or killing yourself, or planning or trying to do so; extreme worry; agitation; panic attacks; difficulty falling asleep or staying asleep; aggressive behavior; irritability; acting without thinking; severe restlessness; and frenzied abnormal excitement.
  - S1: You, your family, or your caregiver should call your doctor right away.
  - S2: You should call if you experience new or worsening depression.
  - S3: You should call if you are thinking about harming or killing yourself.
  - S4: You should call if you are planning or trying to harm or kill yourself.
  - S5: You should call if you experience extreme worry.
  - S6: You should call if you experience agitation.
  - S7: You should call if you experience panic attacks.
  - S8: You should call if you have difficulty falling asleep or staying asleep.
  - S9: You should call if you experience aggressive behavior.
  - S10: You should call if you experience irritability.
  - S11: You should call if you act without thinking.
  - S12: You should call if you experience severe restlessness.
  - S13: You should call if you experience frenzied abnormal excitement.

**L49.3** `Complex Sentence` (0.544) → `decomposed`
- original: Be sure that your family or caregiver knows which symptoms may be serious so they can call the doctor if you are unable to seek treatment on your own.
- pronoun resolved: Be sure that your family or caregiver knows which symptoms may be serious so family or caregiver can call the doctor if you are unable to seek treatment on your own.
  - edits: “they” → “family or caregiver”
  - S1: Be sure that your family or caregiver knows which symptoms may be serious.
  - S2: The family or caregiver can call the doctor if you are unable to seek treatment on your own.

**L50.0** `Simple Sentence` (0.912) → `passthrough`
- original: This medicine may cause seizures, especially in people with certain medical conditions or when using certain drugs.

**L50.1** `Incomplete Sentence` (0.944) → `excluded_incomplete`
- original: Tell your doctor about all of your medical conditions and the drugs you use.

**L51.0** `Complex Sentence` (0.876) → `decomposed`
- original: Bupropion can cause mild pupillary dilation, which can lead to an episode of angle-closure glaucoma in susceptible individuals.
  - S1: Bupropion can cause mild pupillary dilation.
  - S2: This dilation can lead to an episode of angle-closure glaucoma.
  - S3: This occurs in susceptible individuals.

**L51.1** `Simple Sentence` (0.988) → `passthrough`
- original: Angle-closure glaucoma has occurred in patients with untreated anatomically narrow angles treated with antidepressants.

## Before taking this medicine

**L54.0** `Simple Sentence` (0.678) → `passthrough`
- original: Do not use this medicine if you have used an MAO inhibitor in the past 14 days.
- pronoun resolved: Do not use Bupropion if you have used an MAO inhibitor in the past 14 days.
  - edits: “this medicine” → “Bupropion”

**L54.1** `Simple Sentence` (0.94) → `passthrough`
- original: A dangerous drug interaction could occur.

**L54.2** `Simple Sentence` (0.836) → `passthrough`
- original: MAO inhibitors include isocarboxazid, linezolid, methylene blue injection, phenelzine, rasagiline, selegiline, tranylcypromine, and others.

**L55.0** `Simple Sentence` (0.969) → `passthrough`
- original: You should not take this medicine if you are allergic to it or if you have ever had:
- pronoun resolved: You should not take Bupropion if you are allergic to Bupropion or if you have ever had:
  - edits: “this medicine” → “Bupropion”; “it” → “Bupropion”

**L56.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: a seizure disorder;

**L57.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: an eating disorder such as anorexia or bulimia; or

**L58.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: if you have suddenly stopped using alcohol, seizure medication, or a sedative (such as Xanax, Valium, Fiorinal, Klonopin, and others).

**L59.0** `Simple Sentence` (0.491) → `passthrough`
- original: Do not take this medicine to treat more than one condition at a time.
- pronoun resolved: Do not take Bupropion to treat more than one condition at a time.
  - edits: “this medicine” → “Bupropion”

**L59.1** `Complex Sentence` (0.606) → `decomposed`
- original: If you take bupropion for depression, do not also take this medicine to quit smoking or for weight management.
- pronoun resolved: If you take bupropion for depression, do not also take Bupropion to quit smoking or for weight management.
  - edits: “this medicine” → “Bupropion”
  - S1: If you take bupropion for depression, do not also take Bupropion to quit smoking.
  - S2: If you take bupropion for depression, do not also take Bupropion for weight management.

**L60.0** `Incomplete Sentence` (0.944) → `excluded_incomplete`
- original: Tell your doctor about all of your medical conditions and the drugs you use.

**L61.0** `Simple Sentence` (0.807) → `passthrough`
- original: To make sure this medicine is safe for you, tell your doctor if you have ever had:
- pronoun resolved: To make sure Bupropion is safe for you, tell your doctor if you have ever had:
  - edits: “this medicine” → “Bupropion”

**L62.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: a head injury, seizures, or brain or spinal cord tumor;

**L63.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: narrow-angle glaucoma;

**L64.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: heart disease, high blood pressure, or a heart attack;

**L65.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: diabetes;

**L66.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: kidney or liver disease (especially cirrhosis);

**L67.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: depression, bipolar disorder or other mental illness; or

**L68.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: if you drink alcohol.

**L69.0** `Simple Sentence` (0.982) → `passthrough`
- original: Some young people have thoughts about suicide when first taking an antidepressant.

**L69.1** `Simple Sentence` (0.938) → `passthrough`
- original: Your doctor will need to check your progress at regular visits while you are using this medicine.
- pronoun resolved: Your doctor will need to check your progress at regular visits while you are using Bupropion.
  - edits: “this medicine.” → “Bupropion.”

**L69.2** `Simple Sentence` (0.57) → `passthrough`
- original: Your family or other caregivers should also be alert to changes in your mood or symptoms.

**L70.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Pregnancy:

**L71.0** `Incomplete Sentence` (0.857) → `excluded_incomplete`
- original: Talk to your healthcare provider if you are pregnant or plan to become pregnant about the risk to your unborn baby.

**L71.1** `Simple Sentence` (0.986) → `passthrough`
- original: It is not known whether this medicine will harm an unborn baby.
- pronoun resolved: It is not known whether Bupropion will harm an unborn baby.
  - edits: “this medicine” → “Bupropion”

**L71.2** `Incomplete Sentence` (0.861) → `excluded_incomplete`
- original: Tell your doctor right away if you become pregnant.

**L71.3** `Simple Sentence` (0.672) → `passthrough`
- original: Do not start or stop taking bupropion without your doctor's advice.

**L72.0** `Complex Sentence` (0.5) → `decomposed`
- original: If you become pregnant during treatment, talk to your healthcare provider about registering with the National Pregnancy Registry for Antidepressants.
  - S1: If you become pregnant during treatment, talk to your healthcare provider.
  - S2: The healthcare provider can discuss registering with the National Pregnancy Registry for Antidepressants.
  - S3: The National Pregnancy Registry is for antidepressants.

**L72.1** `Simple Sentence` (0.95) → `passthrough`
- original: You can register by calling 1-844-405-6185.

**L73.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Breastfeeding:

**L74.0** `Incomplete Sentence` (0.592) → `excluded_incomplete`
- original: Tell your healthcare provider if you are breastfeeding or plan to breastfeed while taking this medicine.
- pronoun resolved: Tell your healthcare provider if you are breastfeeding or plan to breastfeed while taking Bupropion.
  - edits: “this medicine.” → “Bupropion.”

**L74.1** `Compound Sentence` (0.961) → `decomposed`
- original: This medicine passes into breast milk, and there have been reports of seizures in breastfed infants.
- pronoun resolved: Bupropion passes into breast milk, and there have been reports of seizures in breastfed infants.
  - edits: “This medicine” → “Bupropion”
  - S1: Bupropion passes into breast milk.
  - S2: There have been reports of seizures in breastfed infants.

**L74.2** `Incomplete Sentence` (0.902) → `excluded_incomplete`
- original: Talk to your healthcare provider about the best way to feed your baby during treatment with this medicine.
- pronoun resolved: Talk to your healthcare provider about the best way to feed your baby during treatment with Bupropion.
  - edits: “this medicine.” → “Bupropion.”

## How should I take bupropion?

**L77.0** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: Take bupropion exactly as prescribed by your doctor.

**L77.1** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Follow all directions on your prescription label.

**L77.2** `Incomplete Sentence` (0.87) → `excluded_incomplete`
- original: Do not take this medicine in larger or smaller amounts or for longer than recommended.
- pronoun resolved: Do not take bupropion in larger or smaller amounts or for longer than recommended.
  - edits: “this medicine” → “bupropion”

**L77.3** `Simple Sentence` (0.99) → `passthrough`
- original: Too much of this medicine can increase your risk of a seizure.
- pronoun resolved: Too much of bupropion can increase your risk of a seizure.
  - edits: “this medicine” → “bupropion”

**L78.0** `Incomplete Sentence` (0.939) → `excluded_incomplete`
- original: Do not crush, chew, or break tablets.

**L78.1** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Swallow the tablet whole.

**L79.0** `Incomplete Sentence` (0.831) → `excluded_incomplete`
- original: Take bupropion with food if the medication upsets your stomach.

**L80.0** `Simple Sentence` (0.761) → `passthrough`
- original: If you have trouble falling asleep or staying asleep, do not take tablets too close to bedtime.

**L81.0** `Simple Sentence` (0.677) → `passthrough`
- original: Your doctor will probably start you on a low dose of this medicine and gradually increase your dose.
- pronoun resolved: Your doctor will probably start you on a low dose of bupropion and gradually increase your dose.
  - edits: “this medicine” → “bupropion”

**L82.0** `Simple Sentence` (0.955) → `passthrough`
- original: It may take 4 weeks or longer before you feel the full benefit of this medicine.
- pronoun resolved: It may take 4 weeks or longer before you feel the full benefit of bupropion.
  - edits: “this medicine.” → “bupropion.”

**L82.1** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Continue to take your tablets even if you feel well.

**L82.2** `Simple Sentence` (0.803) → `passthrough`
- original: Do not stop taking this medicine without talking to your doctor.
- pronoun resolved: Do not stop taking bupropion without talking to your doctor.
  - edits: “this medicine” → “bupropion”

**L82.3** `Simple Sentence` (0.974) → `passthrough`
- original: Your doctor may decrease your dose gradually.

**L83.0** `Simple Sentence` (0.522) → `passthrough`
- original: You should not change your dose or stop using bupropion suddenly unless you have a seizure while taking this medicine.
- pronoun resolved: You should not change your dose or stop using bupropion suddenly unless you have a seizure while taking bupropion.
  - edits: “this medicine.” → “bupropion.”

**L83.1** `Simple Sentence` (0.988) → `passthrough`
- original: Stopping suddenly can cause unpleasant withdrawal symptoms.

**L84.0** `Incomplete Sentence` (0.976) → `excluded_incomplete`
- original: Ask your doctor how to stop using bupropion safely.

**L85.0** `Complex Sentence` (0.608) → `decomposed`
- original: Some people taking bupropion have severe high blood pressure, especially when using a nicotine replacement product (patch or gum).
  - S1: Some people taking bupropion have severe high blood pressure.
  - S2: This is especially true when using a nicotine replacement product.
  - S3: The nicotine replacement product can be a patch or gum.

**L85.1** `Simple Sentence` (0.965) → `passthrough`
- original: Your blood pressure may need to be checked before and during treatment with this medicine.
- pronoun resolved: Your blood pressure may need to be checked before and during treatment with bupropion.
  - edits: “this medicine.” → “bupropion.”

**L86.0** `Simple Sentence` (0.99) → `passthrough`
- original: This medicine can cause you to have a false positive drug screening test (amphetamines).
- pronoun resolved: Bupropion can cause you to have a false positive drug screening test (amphetamines).
  - edits: “This medicine” → “Bupropion”

**L86.1** `Simple Sentence` (0.544) → `passthrough`
- original: If you provide a urine sample for drug screening, tell the laboratory staff you are taking this medicine.
- pronoun resolved: If you provide a urine sample for drug screening, tell the laboratory staff you are taking bupropion.
  - edits: “this medicine.” → “bupropion.”

**L87.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: For smoking cessation.

**L88.0** `Complex Sentence` (0.895) → `decomposed`
- original: If you take bupropion to help you stop smoking, you may continue to smoke for about 1 week after you start the medicine.
  - S1: If you take bupropion to help you stop smoking, you may continue to smoke for about 1 week.
  - S2: This may happen after you start the medicine.

**L88.1** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Set a date to quit smoking during the second week of treatment.

**L88.2** `Incomplete Sentence` (0.828) → `excluded_incomplete`
- original: Talk to your doctor if you are having trouble quitting after you have used bupropion for at least 7 to 12 weeks.

**L89.0** `Simple Sentence` (0.492) → `passthrough`
- original: Your doctor may prescribe a nicotine replacement product (such as patches or gum) to help you stop smoking.

**L89.1** `Incomplete Sentence` (0.802) → `excluded_incomplete`
- original: Start using the nicotine replacement product on the same day you stop (quit) smoking or using tobacco products.

**L90.0** `Complex Sentence` (0.846) → `decomposed`
- original: You may have nicotine withdrawal symptoms when you stop smoking, including increased appetite, weight gain, trouble sleeping, trouble concentrating, slower heart rate, having the urge to smoke, and feeling anxious, restless, depressed, angry, frustrated, or irritated.
  - S1: You may have nicotine withdrawal symptoms when you stop smoking.
  - S2: These symptoms include increased appetite.
  - S3: These symptoms include weight gain.
  - S4: These symptoms include trouble sleeping.
  - S5: These symptoms include trouble concentrating.
  - S6: These symptoms include a slower heart rate.
  - S7: These symptoms include having the urge to smoke.
  - S8: These symptoms include feeling anxious, restless, depressed, angry, frustrated, or irritated.

**L90.1** `Simple Sentence` (0.974) → `passthrough`
- original: These symptoms may occur with or without using medication such as bupropion.

**L91.0** `Simple Sentence` (0.52) → `passthrough`
- original: Smoking cessation may also cause new or worsening mental health problems, such as depression.

## Bupropion hydrochloride dosing information

**L94.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Bupropion Dose for Depression:

**L95.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Immediate-release tablets:

**L96.0** `Compound Sentence` (0.613) → `decomposed`
- original: Initial dose: 100 mg orally twice a day, increase if necessary after 3 days to 100 mg orally three times a day.
  - S1: The initial dose is 100 mg orally twice a day.
  - S2: If necessary, increase the dose after 3 days to 100 mg orally three times a day.

**L97.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Maintenance dose: 100 mg orally three times a day

**L98.0** `Compound Sentence` (0.589) → `decomposed`
- original: Maximum dose: 450 mg/day in up to 4 divided doses; single doses should not exceed 150 mg
  - S1: The maximum dose is 450 mg/day in up to 4 divided doses.
  - S2: Single doses should not exceed 150 mg.

**L99.0** `Simple Sentence` (0.981) → `passthrough`
- original: Immediate-release tablets should be given at least 6 hours apart.

**L100.0** `Simple Sentence` (0.891) → `passthrough`
- original: Dose increases of the immediate-release tablet should not exceed 100 mg per day in a 3-day period.

**L101.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Sustained-release tablets:

**L102.0** `Compound Sentence` (0.684) → `decomposed`
- original: Initial dose: 150 mg orally once a day in the morning, increase if necessary after 3 days to 150 mg orally twice a day.
  - S1: The initial dose is 150 mg orally once a day in the morning.
  - S2: If necessary, increase the dose after 3 days to 150 mg orally twice a day.

**L103.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Maintenance dose: 150 mg orally twice a day

**L104.0** `Simple Sentence` (0.523) → `passthrough`
- original: Maximum dose: 400 mg/day; maximum single dose should not exceed 200 mg

**L105.0** `Simple Sentence` (0.985) → `passthrough`
- original: Sustained-release oral tablets should be given at least 8 hours apart

**L106.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Extended-release tablets:

**L107.0** `Compound Sentence` (0.697) → `decomposed`
- original: Initial dose: 150 mg orally once a day in the morning, increase if necessary after 4 days to 300 mg orally once a day.
  - S1: The initial dose is 150 mg orally once a day in the morning.
  - S2: If necessary, increase the dose to 300 mg orally once a day after 4 days.

**L108.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Maintenance dose: 300 mg orally once a day

**L109.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Maximum dose: 450 mg/day

**L110.0** `Simple Sentence` (0.987) → `passthrough`
- original: Extended-release oral tablets should be given at least 24 hours apart

**L111.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Comments:

**L112.0** `Complex Sentence` (0.938) → `decomposed`
- original: So as not to exceed the maximum single dose of 150 mg for immediate-release tablets, a dose of 100 mg orally four times a day (using the 100 mg tablet) may be administered.
  - S1: A dose of 100 mg orally four times a day may be administered.
  - S2: This dose uses the 100 mg tablet.
  - S3: This is done so as not to exceed the maximum single dose of 150 mg for immediate-release tablets.

**L112.1** `Complex Sentence` (0.575) → `decomposed`
- original: Patients who are taking 300 mg/day for at least 2 weeks (OR are currently taking 450 mg/day) of any formulation may be switched to the extended-release 450 mg dose.
  - S1: Patients may be switched to the extended-release 450 mg dose.
  - S2: This applies to patients taking 300 mg/day for at least 2 weeks.
  - S3: This also applies to patients currently taking 450 mg/day.
  - S4: These patients may be taking any formulation.

**L112.2** `Simple Sentence` (0.972) → `passthrough`
- original: Bupropion hydrobromide 174 mg oral tablet is equivalent to bupropion hydrochloride 150 mg.

**L112.3** `Complex Sentence` (0.703) → `decomposed`
- original: Patients should be periodically reviewed to determine the need for maintenance treatment and the appropriate dose for such treatment.
  - S1: Patients should be periodically reviewed.
  - S2: The review should determine the need for maintenance treatment.
  - S3: The review should determine the appropriate dose for such treatment.

**L113.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Bupropion Dose for Seasonal Affective Disorder:

**L114.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Extended-release tablets:

**L115.0** `Incomplete Sentence` (0.541) → `excluded_incomplete`
- original: Initial dose: 150 mg orally once a day in the morning, increased if necessary after 7 days to 300 mg orally once a day

**L116.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Maintenance dose: 150 to 300 mg orally once a day

**L117.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Maximum dose: 300 mg/day

**L118.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Comments:

**L119.0** `Compound Sentence` (0.858) → `decomposed`
- original: Treatment should be initiated in the autumn prior to the onset of depressive symptoms, continued through the winter season, and discontinued in early spring.
  - S1: Treatment should be initiated in the autumn prior to the onset of depressive symptoms.
  - S2: Treatment should be continued through the winter season.
  - S3: Treatment should be discontinued in early spring.

**L119.1** `Complex Sentence` (0.943) → `decomposed`
- original: If bupropion hydrochloride 300 mg orally per day is not tolerated, it should be reduced to 150 mg once a day before discontinuing treatment.
- pronoun resolved: If bupropion hydrochloride 300 mg orally per day is not tolerated, bupropion hydrochloride 300 mg orally per day should be reduced to 150 mg once a day before discontinuing treatment.
  - edits: “it” → “bupropion hydrochloride 300 mg orally per day”
  - S1: If bupropion hydrochloride 300 mg orally per day is not tolerated.
  - S2: Bupropion hydrochloride 300 mg orally per day should be reduced to 150 mg once a day.
  - S3: This reduction should occur before discontinuing treatment.

**L119.2** `Complex Sentence` (0.81) → `decomposed`
- original: Patients taking bupropion hydrochloride 300 mg orally per day during the autumn-winter season should have their dose tapered to 150 mg once a day for 2 weeks prior to discontinuation.
- pronoun resolved: Patients taking bupropion hydrochloride 300 mg orally per day during the autumn-winter season should have Patients's dose tapered to 150 mg once a day for 2 weeks prior to discontinuation.
  - edits: “their” → “Patients's”
  - S1: Patients taking bupropion hydrochloride 300 mg orally per day during the autumn-winter season should have their dose tapered.
  - S2: The dose should be tapered to 150 mg once a day.
  - S3: This tapering should occur for 2 weeks prior to discontinuation.

**L119.3** `Complex Sentence` (0.905) → `decomposed`
- original: The timing of initiation and treatment duration for seasonal affective disorder should be individualized according to the patient's historical pattern of seasonal major depressive episodes.
  - S1: The timing of initiation and treatment duration for seasonal affective disorder should be individualized.
  - S2: The individualization should be according to the patient's historical pattern.
  - S3: The pattern refers to seasonal major depressive episodes.

**L120.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose for Smoking Cessation:

**L121.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Sustained-release tablets:

**L122.0** `Incomplete Sentence` (0.858) → `excluded_incomplete`
- original: Initial dose: 150 mg orally once a day for 3 days, increased to 150 mg orally twice a day

**L123.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Maintenance dose: 150 mg orally twice a day

**L124.0** `Incomplete Sentence` (0.55) → `excluded_incomplete`
- original: Maximum dose: 300 mg/day; maximum single dose should not exceed 150 mg

**L125.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Duration of therapy: 7 to 12 weeks

**L126.0** `Compound Sentence` (0.818) → `decomposed`
- original: Comments: Begin dosing one week before quit day; the target stop date should be set within the first 2 weeks of treatment, preferably in the second week.
  - S1: Begin dosing one week before quit day.
  - S2: The target stop date should be set within the first 2 weeks of treatment.
  - S3: Preferably, the target stop date should be set in the second week.

**L126.1** `Simple Sentence` (0.972) → `passthrough`
- original: There should be an interval of at least 8 hours between doses.

**L126.2** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: May be used with a nicotine transdermal system.

**L126.3** `Compound Sentence` (0.806) → `decomposed`
- original: If there is no effect after 12 weeks, treatment should be discontinued; longer treatment should be guided by the relative benefits and risks for the individual patient.
  - S1: If there is no effect after 12 weeks, treatment should be discontinued.
  - S2: Longer treatment should be guided by the relative benefits and risks for the individual patient.

## What happens if I miss a dose?

**L129.0** `Simple Sentence` (0.483) → `passthrough`
- original: Skip the missed dose and take your next dose at the regular time.

**L129.1** `Incomplete Sentence` (0.748) → `excluded_incomplete`
- original: Do not take an extra dose to make up for the missed dose.

**L129.2** `Simple Sentence` (0.987) → `passthrough`
- original: Taking too much bupropion can increase your chance of having a seizure.

## What happens if I overdose?

**L132.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L132.1** `Simple Sentence` (0.987) → `passthrough`
- original: An overdose of bupropion can be fatal.

**L132.2** `Simple Sentence` (0.431) → `passthrough`
- original: Overdose symptoms may include muscle stiffness, hallucinations, fast or uneven heartbeat, shallow breathing, or fainting.

## What to avoid

**L135.0** `Simple Sentence` (0.991) → `passthrough`
- original: Drinking alcohol with bupropion may increase your risk of seizures.

**L135.1** `Simple Sentence` (0.879) → `passthrough`
- original: If you drink alcohol regularly, talk with your doctor before changing the amount you drink.

**L135.2** `Compound Sentence` (0.579) → `decomposed`
- original: This medicine can also cause seizures in people who drink a lot of alcohol and then suddenly quit drinking when they start using the medication.
- pronoun resolved: Bupropion can also cause seizures in people who drink a lot of alcohol and then suddenly quit drinking when people start using the medication.
  - edits: “This medicine” → “Bupropion”; “they” → “people”
  - S1: Bupropion can also cause seizures in people who drink a lot of alcohol and then suddenly quit drinking.
  - S2: This risk occurs when people start using the medication.

**L136.0** `Simple Sentence` (0.988) → `passthrough`
- original: Bupropion may impair your thinking or reactions.

**L136.1** `Incomplete Sentence` (0.688) → `excluded_incomplete`
- original: Be careful if you drive or do anything that requires you to be alert.

## What other drugs will affect bupropion?

**L139.0** `Simple Sentence` (0.808) → `passthrough`
- original: You may have a higher risk of seizures if you use certain other medicines while taking bupropion.

**L140.0** `Simple Sentence` (0.99) → `passthrough`
- original: Many drugs can interact with bupropion.

**L140.1** `Incomplete Sentence` (0.845) → `excluded_incomplete`
- original: Tell your doctor about all medicines you use, and those you start or stop using during your treatment.

**L140.2** `Simple Sentence` (0.849) → `passthrough`
- original: This includes prescription and over-the-counter medicines, vitamins, and herbal products.

**L141.0** `Simple Sentence` (0.974) → `passthrough`
- original: Some examples of drugs that interact with bupropion are:

**L142.0** `Simple Sentence` (0.986) → `passthrough`
- original: Digoxin: May decrease plasma digoxin levels.

**L142.1** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Monitor digoxin levels

**L143.0** `Simple Sentence` (0.987) → `passthrough`
- original: MAOIs: Increased risk of hypertensive reactions can occur when used concomitantly with this medication.
- pronoun resolved: MAOIs: Increased risk of hypertensive reactions can occur when used concomitantly with Bupropion.
  - edits: “this medication.” → “Bupropion.”

**L144.0** `Simple Sentence` (0.984) → `passthrough`
- original: Drugs that lower seizure threshold: Dose bupropion with caution.

**L145.0** `Compound-Complex Sentence` (0.829) → `decomposed`
- original: Medicines that are CYP2B6 inducers: Dose increase may be necessary if coadministered with CYP2B6 inducers (e.g., ritonavir, lopinavir, efavirenz, carbamazepine, phenobarbital, and phenytoin) based on clinical response, but should not exceed the maximum recommended dose.
  - S1: Medicines that are CYP2B6 inducers may require a dose increase if coadministered with other CYP2B6 inducers.
  - S2: Examples of CYP2B6 inducers include ritonavir, lopinavir, efavirenz, carbamazepine, phenobarbital, and phenytoin.
  - S3: Dose increases should be based on clinical response.
  - S4: Dose increases should not exceed the maximum recommended dose.

**L146.0** `Complex Sentence` (0.422) → `decomposed`
- original: Medicines that are CYP2B6 inhibitors: Dose adjustment may be necessary if coadministered with CYP2B6 inhibitors (e.g., ticlopidine or clopidogrel).
  - S1: Medicines that are CYP2B6 inhibitors may require dose adjustment if coadministered with CYP2B6 inhibitors.
  - S2: Examples of CYP2B6 inhibitors include ticlopidine or clopidogrel.

**L147.0** `Complex Sentence` (0.724) → `decomposed`
- original: Medicines metabolized by CYP2D6: Bupropion inhibits CYP2D6 and can increase concentrations of antidepressants (e.g., venlafaxine, nortriptyline, imipramine, desipramine, paroxetine, fluoxetine, sertraline), antipsychotics (e.g., haloperidol, risperidone, thioridazine), beta-blockers (e.g., metoprolol), and Type 1C antiarrhythmics (e.g., propafenone, flecainide).
  - S1: Bupropion inhibits CYP2D6.
  - S2: Bupropion can increase concentrations of antidepressants.
  - S3: Examples of antidepressants include venlafaxine, nortriptyline, imipramine, desipramine, paroxetine, fluoxetine, and sertraline.
  - S4: Bupropion can increase concentrations of antipsychotics.
  - S5: Examples of antipsychotics include haloperidol, risperidone, and thioridazine.
  - S6: Bupropion can increase concentrations of beta-blockers.
  - S7: An example of a beta-blocker is metoprolol.
  - S8: Bupropion can increase concentrations of Type 1C antiarrhythmics.
  - S9: Examples of Type 1C antiarrhythmics include propafenone and flecainide.
  - S10: These medicines are metabolized by CYP2D6.

**L147.1** `Simple Sentence` (0.979) → `passthrough`
- original: A dose reduction of these medicines may be considered when used with bupropion.
- pronoun resolved: A dose reduction of antidepressants may be considered when used with bupropion.
  - edits: “these medicines” → “antidepressants”

**L148.0** `Simple Sentence` (0.942) → `passthrough`
- original: Dopaminergic drugs (levodopa and amantadine): CNS toxicity can occur when used concomitantly with this medicine.
- pronoun resolved: Dopaminergic drugs (levodopa and amantadine): CNS toxicity can occur when used concomitantly with Bupropion.
  - edits: “this medicine.” → “Bupropion.”

**L149.0** `Simple Sentence` (0.986) → `passthrough`
- original: Not all possible interactions are listed in this medication guide.

## Storage

**L152.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Store at room temperature, 20° to 25°C (68° to 77°F).

**L152.1** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Keep this medicine dry and out of the light.
- pronoun resolved: Keep Bupropion dry and out of the light.
  - edits: “this medicine” → “Bupropion”

## Popular FAQ

**L155.0** `Incomplete Sentence` (0.943) → `excluded_incomplete`
- original: Q: How long does it take Wellbutrin XL/SR (bupropion) to work?

**L155.1** `Compound-Complex Sentence` (0.66) → `decomposed`
- original: A: You may notice an improvement in your sleep, energy and appetite in the first week or two of taking Wellbutrin and this can be an important sign that the drug is working.
- pronoun resolved: A: You may notice an improvement in your sleep, energy and appetite in the first week or two of taking Wellbutrin and improvement in your sleep, energy, and appetite can be an important sign that Wellbutrin is working.
  - edits: “this” → “improvement in your sleep, energy, and appetite”; “the drug” → “Wellbutrin”
  - S1: You may notice an improvement in your sleep, energy, and appetite in the first week or two of taking Wellbutrin.
  - S2: Improvement in sleep, energy, and appetite can be an important sign that Wellbutrin is working.

**L155.2** `Compound Sentence` (0.597) → `decomposed`
- original: But, like other antidepressants, improvements in your mood or motivation may take 6 to 8 weeks to develop.
  - S1: But, like other antidepressants, improvements in your mood or motivation may take 6 to 8 weeks to develop.

**L156.0** `Incomplete Sentence` (0.921) → `excluded_incomplete`
- original: Q: Does Auvelity work better than Wellbutrin?

**L156.1** `Complex Sentence` (0.913) → `decomposed`
- original: A: Auvelity worked significantly better than Wellbutrin (bupropion) at relieving symptoms of depression in a small randomized double-blind, parallel trial that lasted for 6 weeks.
  - S1: Auvelity worked significantly better than Wellbutrin (bupropion) at relieving symptoms of depression.
  - S2: This finding was based on a small randomized double-blind, parallel trial.
  - S3: The trial lasted for 6 weeks.

**L156.2** `Compound-Complex Sentence` (0.462) → `decomposed`
- original: It also had a faster onset of effect, with improvement in the Montgomery-Åsberg Depression Rating Scale (MADRS) score being observed as early as week 1 and differences being statistically significant by week 2.
- pronoun resolved: Auvelity also had a faster onset of effect, with improvement in the Montgomery-Åsberg Depression Rating Scale (MADRS) score being observed as early as week 1 and differences being statistically significant by week 2.
  - edits: “It” → “Auvelity”
  - S1: Auvelity had a faster onset of effect.
  - S2: Improvement in the Montgomery-Åsberg Depression Rating Scale (MADRS) score was observed as early as week 1.
  - S3: Differences were statistically significant by week 2.

**L156.3** `Compound Sentence` (0.674) → `decomposed`
- original: Note that the brand name Wellbutrin has been discontinued, but generic bupropion is still available.
  - S1: Note that the brand name Wellbutrin has been discontinued.
  - S2: Generic bupropion is still available.

**L157.0** `Incomplete Sentence` (0.964) → `excluded_incomplete`
- original: Q: What medications are known to cause hair loss?

**L157.1** `Simple Sentence` (0.594) → `passthrough`
- original: A: Medication-induced hair loss represents a significant concern for patients across multiple therapeutic categories.

**L157.2** `Complex Sentence` (0.956) → `decomposed`
- original: While chemotherapy drugs are most commonly associated with severe hair loss, many commonly prescribed medications-including antibiotics, psychiatric drugs, cardiovascular agents, and hormonal therapies-can also cause this distressing side effect.
  - S1: Chemotherapy drugs are most commonly associated with severe hair loss.
  - S2: Many commonly prescribed medications can also cause this distressing side effect.
  - S3: These medications include antibiotics, psychiatric drugs, cardiovascular agents, and hormonal therapies.

**L158.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Q: How does Zurzuvae differ from traditional antidepressants?

**L158.1** `Compound Sentence` (0.748) → `decomposed`
- original: A: Zurzuvae (zuranolone) differs from traditional antidepressants because it's the first oral treatment approved for postpartum depression (PPD), but it's not approved for major depressive disorder.
  - S1: Zurzuvae (zuranolone) differs from traditional antidepressants because it's the first oral treatment approved for postpartum depression (PPD).
  - S2: It is not approved for major depressive disorder.

**L158.2** `Compound Sentence` (0.925) → `decomposed`
- original: It’s faster-acting than most traditional antidepressants, has a unique mechanism of action and is only taken for 14 days, with symptom improvement starting as early as the third day.
  - S1: It is faster-acting than most traditional antidepressants.
  - S2: It has a unique mechanism of action.
  - S3: It is only taken for 14 days.
  - S4: Symptom improvement starts as early as the third day.
