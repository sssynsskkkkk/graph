# Adderall — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/adderall.txt` · 210 sentences · 30 changed by pronoun resolution · 307 sentences sent to EDC

## What is Adderall?

**L5.0** `Complex Sentence` (0.699) → `decomposed`
- original: Adderall (mixed amphetamine and dextroamphetamine salts) is a central nervous system stimulant used to treat attention deficit hyperactivity disorder (ADHD) and a sleep disorder called narcolepsy.
  - S1: Adderall is a central nervous system stimulant.
  - S2: Adderall is used to treat attention deficit hyperactivity disorder (ADHD).
  - S3: Adderall is used to treat a sleep disorder called narcolepsy.
  - S4: Adderall contains mixed amphetamine and dextroamphetamine salts.

**L5.1** `Complex Sentence` (0.932) → `decomposed`
- original: Adderall contains a combination of amphetamine and dextroamphetamine, which affect chemicals in the brain and nerves that contribute to hyperactivity and impulse control.
  - S1: Adderall contains a combination of amphetamine and dextroamphetamine.
  - S2: These substances affect chemicals in the brain and nerves.
  - S3: These chemicals contribute to hyperactivity and impulse control.

**L6.0** `Simple Sentence` (0.956) → `passthrough`
- original: For ADHD, Adderall is used in children 3 to 17 years of age and in adults.

**L6.1** `Simple Sentence` (0.891) → `passthrough`
- original: It may help increase attention and decrease impulsiveness and hyperactivity.
- pronoun resolved: Adderall may help increase attention and decrease impulsiveness and hyperactivity.
  - edits: “It” → “Adderall”

**L7.0** `Simple Sentence` (0.978) → `passthrough`
- original: For narcolepsy, Adderall is used in people 6 years and older.

**L8.0** `Complex Sentence` (0.605) → `decomposed`
- original: It is not known if Adderall is safe and effective for ADHD in children under 3 years of age or for narcolepsy in children under 6 years of age.
  - S1: It is not known if Adderall is safe and effective for ADHD in children under 3 years of age.
  - S2: It is not known if Adderall is safe and effective for narcolepsy in children under 6 years of age.

**L9.0** `Complex Sentence` (0.948) → `decomposed`
- original: Adderall is a federally controlled substance (CII) because it contains amphetamine, which can be a target for people who abuse prescription medicines or street drugs.
- pronoun resolved: Adderall is a federally controlled substance (CII) because Adderall contains amphetamine, which can be a target for people who abuse prescription medicines or street drugs.
  - edits: “it” → “Adderall”
  - S1: Adderall is a federally controlled substance (CII).
  - S2: Adderall contains amphetamine.
  - S3: Amphetamine can be a target for people who abuse prescription medicines or street drugs.

**L9.1** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Keep Adderall in a safe place to protect it from theft.
- pronoun resolved: Keep Adderall in a safe place to protect Adderall from theft.
  - edits: “it” → “Adderall”

**L9.2** `Incomplete Sentence` (0.743) → `excluded_incomplete`
- original: Never give your Adderall to anyone else, because it may cause death or harm them.
- pronoun resolved: Never give your Adderall to anyone else, because Adderall may cause death or harm them.
  - edits: “it” → “Adderall”

**L9.3** `Simple Sentence` (0.983) → `passthrough`
- original: Selling or giving away Adderall is against the law.

**L10.0** `Simple Sentence` (0.973) → `passthrough`
- original: Adderall may also be used for purposes not listed in this medication guide.

**L11.0** `Simple Sentence` (0.83) → `passthrough`
- original: Adderall (mixed amphetamine and dextroamphetamine salts) was FDA-approved on January 19, 1960.

**L11.1** `Simple Sentence` (0.986) → `passthrough`
- original: Extended-release formulations of Adderall (Adderall XR) are only used to treat ADHD.

## Warnings

**L14.0** `Simple Sentence` (0.978) → `passthrough`
- original: Adderall has a Boxed Warning for abuse, misuse, and addiction.

**L15.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Abuse, misuse, and addiction:

**L16.0** `Compound Sentence` (0.939) → `decomposed`
- original: Adderall has a high chance of abuse and misuse and may lead to substance use problems, including addiction.
  - S1: Adderall has a high chance of abuse and misuse.
  - S2: It may lead to substance use problems, including addiction.

**L16.1** `Simple Sentence` (0.768) → `passthrough`
- original: Misuse and abuse of Adderall, other amphetamine-containing medicines, and methylphenidate-containing medicines can lead to overdose and death.

**L16.2** `Compound Sentence` (0.589) → `decomposed`
- original: The risk of overdose and death is increased with higher doses or when the medicine is used in ways that are not approved, such as snorting or injection.
  - S1: The risk of overdose and death is increased with higher doses.
  - S2: The risk of overdose and death is increased when the medicine is used in ways that are not approved.
  - S3: Examples of unapproved use include snorting or injection.

**L17.0** `Simple Sentence` (0.925) → `passthrough`
- original: Adderall may lead to physical dependence after prolonged use, even if taken as directed.

**L17.1** `Compound Sentence` (0.806) → `decomposed`
- original: Your healthcare provider should check you or your child for the risk of abuse, misuse, and addiction before starting treatment and will monitor you or your child during treatment.
  - S1: Your healthcare provider should check you or your child for the risk of abuse, misuse, and addiction before starting treatment.
  - S2: Your healthcare provider will monitor you or your child during treatment.

**L17.2** `Incomplete Sentence` (0.822) → `excluded_incomplete`
- original: Tell your healthcare provider if you or your child has ever abused or been dependent on alcohol, prescription medicines, or street drugs.

**L18.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Heart-related risks:

**L19.0** `Simple Sentence` (0.76) → `passthrough`
- original: Stimulants have caused stroke, heart attack, and sudden death in people with high blood pressure, heart disease, or a heart defect.

**L19.1** `Compound Sentence` (0.945) → `decomposed`
- original: Your healthcare provider should check you or your child carefully for heart problems before starting Adderall and should check blood pressure and heart rate regularly during treatment.
  - S1: Your healthcare provider should check you or your child carefully for heart problems before starting Adderall.
  - S2: Your healthcare provider should check blood pressure and heart rate regularly during treatment.

**L20.0** `Compound Sentence` (0.374) → `decomposed`
- original: Call your healthcare provider right away or go to the nearest hospital emergency room if you or your child have any signs of heart problems, such as chest pain, shortness of breath, or fainting during treatment.
  - S1: Call your healthcare provider right away or go to the nearest hospital emergency room if you or your child have any signs of heart problems.
  - S2: These signs include chest pain, shortness of breath, or fainting during treatment.

**L21.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Mental (psychiatric) problems:

**L22.0** `Compound Sentence` (0.835) → `decomposed`
- original: Adderall may cause new or worse behavior and thought problems, new or worse bipolar illness, or new psychotic symptoms (such as hearing voices, or seeing or believing things that are not real) or new manic symptoms.
  - S1: Adderall may cause new or worse behavior and thought problems.
  - S2: Adderall may cause new or worse bipolar illness.
  - S3: Adderall may cause new psychotic symptoms, such as hearing voices, or seeing or believing things that are not real.
  - S4: Adderall may cause new manic symptoms.

**L22.1** `Simple Sentence` (0.756) → `passthrough`
- original: This is more likely if you have a history of depression, mental illness, or bipolar disorder.

**L22.2** `Incomplete Sentence` (0.461) → `excluded_incomplete`
- original: Tell your healthcare provider about any mental problems you or your child have, or about a family history of suicide, bipolar illness, or depression.

**L23.0** `Complex Sentence` (0.369) → `decomposed`
- original: Call your healthcare provider right away if you or your child have any new or worsening mental symptoms during treatment, especially hearing voices, seeing or believing things that are not real, or new manic symptoms.
  - S1: Call your healthcare provider right away if you or your child have any new or worsening mental symptoms during treatment.
  - S2: This is especially important if you experience hearing voices.
  - S3: It is also important if you see or believe things that are not real.
  - S4: It is also important if you have new manic symptoms.

**L24.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Circulation problems:

**L25.0** `Simple Sentence` (0.85) → `passthrough`
- original: You may have blood circulation problems that can cause numbness, pain, or discoloration in your fingers or toes.

**L25.1** `Incomplete Sentence` (0.681) → `excluded_incomplete`
- original: Call your doctor right away if you have unexplained wounds appearing on your fingers or toes during treatment.

**L26.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Other warnings:

**L27.0** `Compound Sentence` (0.706) → `decomposed`
- original: Do not use Adderall if you have used an MAO inhibitor in the past 14 days, such as isocarboxazid, linezolid, phenelzine, rasagiline, selegiline, or tranylcypromine, or if you have received a methylene blue injection.
  - S1: Do not use Adderall if you have used an MAO inhibitor in the past 14 days.
  - S2: Examples of MAO inhibitors include isocarboxazid, linezolid, phenelzine, rasagiline, selegiline, and tranylcypromine.
  - S3: Do not use Adderall if you have received a methylene blue injection.

**L27.1** `Simple Sentence` (0.94) → `passthrough`
- original: A dangerous drug interaction could occur.

**L28.0** `Complex Sentence` (0.718) → `decomposed`
- original: You may not be able to use Adderall if you have glaucoma, an overactive thyroid, severe anxiety or agitation, moderate to severe high blood pressure, heart disease or coronary artery disease, vascular disease, or a history of drug or alcohol addiction.
  - S1: You may not be able to use Adderall if you have glaucoma.
  - S2: You may not be able to use Adderall if you have an overactive thyroid.
  - S3: You may not be able to use Adderall if you have severe anxiety or agitation.
  - S4: You may not be able to use Adderall if you have moderate to severe high blood pressure.
  - S5: You may not be able to use Adderall if you have heart disease or coronary artery disease.
  - S6: You may not be able to use Adderall if you have vascular disease.
  - S7: You may not be able to use Adderall if you have a history of drug or alcohol addiction.

## Adderall side effects

**L31.0** `Compound Sentence` (0.327) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to Adderall: hives, difficult breathing, or swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to Adderall.
  - S2: These signs include hives.
  - S3: These signs include difficult breathing.
  - S4: These signs include swelling of your face, lips, tongue, or throat.

**L32.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious side effects:

**L33.0** `Simple Sentence` (0.989) → `passthrough`
- original: Adderall may cause serious side effects.

**L33.1** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L34.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: signs of heart problems, such as chest pain, trouble breathing, or feeling like you might pass out

**L35.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: signs of psychosis, such as hallucinations, new behavior problems, aggression, hostility, or paranoia

**L36.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: signs of circulation problems, such as numbness, pain, a cold feeling, unexplained wounds, or skin color changes (pale, red, or blue appearance) in your fingers or toes

**L37.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a seizure

**L38.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: muscle twitches (tics)

**L39.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: changes in your vision.

**L40.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: See warnings above.

**L41.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Slowing of growth (height and weight) in children:

**L42.0** `Compound Sentence` (0.803) → `decomposed`
- original: Children should have their height and weight checked often during treatment, and your healthcare provider may stop treatment if your child is not growing or gaining weight as expected.
  - S1: Children should have their height and weight checked often during treatment.
  - S2: Your healthcare provider may stop treatment if your child is not growing or gaining weight as expected.

**L43.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serotonin syndrome:

**L44.0** `Compound Sentence` (0.558) → `decomposed`
- original: This problem may happen when Adderall is taken with certain other medicines and may be life-threatening.
  - S1: This problem may happen when Adderall is taken with certain other medicines.
  - S2: This problem may be life-threatening.

**L44.1** `Compound Sentence` (0.534) → `decomposed`
- original: Stop taking Adderall and get medical help right away if you develop agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness, twitching, loss of coordination, nausea, vomiting, or diarrhea.
  - S1: Stop taking Adderall.
  - S2: Get medical help right away if you develop agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness, twitching, loss of coordination, nausea, vomiting, or diarrhea.

**L45.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Common side effects:

**L46.0** `Complex Sentence` (0.442) → `decomposed`
- original: Common side effects of Adderall may include stomach pain, loss of appetite, weight loss, mood changes, feeling nervous, fast heart rate, headache, dizziness, sleep problems (insomnia), and dry mouth.
  - S1: Common side effects of Adderall may include stomach pain.
  - S2: Common side effects of Adderall may include loss of appetite.
  - S3: Common side effects of Adderall may include weight loss.
  - S4: Common side effects of Adderall may include mood changes.
  - S5: Common side effects of Adderall may include feeling nervous.
  - S6: Common side effects of Adderall may include fast heart rate.
  - S7: Common side effects of Adderall may include headache.
  - S8: Common side effects of Adderall may include dizziness.
  - S9: Common side effects of Adderall may include sleep problems (insomnia).
  - S10: Common side effects of Adderall may include dry mouth.

**L47.0** `Compound Sentence` (0.545) → `decomposed`
- original: This is not a complete list of side effects, and others may occur.
  - S1: This is not a complete list of side effects.
  - S2: Others may occur.

**L47.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L47.2** `Simple Sentence` (0.97) → `passthrough`
- original: You may report side effects to the FDA at 1-800-FDA-1088.

## Before taking this medicine

**L50.0** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Do not take Adderall if you or your child:

**L51.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: are allergic to amphetamine products or any of the ingredients in Adderall (see ingredients below)

**L52.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: are taking, or have taken within the past 14 days, an MAO inhibitor, including the antibiotic linezolid or the intravenous medicine methylene blue.

**L53.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: have a rare adrenal gland tumor called pheochromocytoma.

**L54.0** `Simple Sentence` (0.394) → `passthrough`
- original: Before taking Adderall, tell your healthcare provider about all your medical conditions including if you or anyone in your family has ever had:

**L55.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: heart problems, heart disease, heart defects, or high blood pressure, or a family history of sudden death or heart problems

**L56.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: mental problems including psychosis, mania, bipolar illness, or depression, or a family history of suicide, bipolar illness, or depression

**L57.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: kidney or liver problems

**L58.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: seizures or an abnormal brain wave test (EEG)

**L59.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: circulation problems in the fingers or toes

**L60.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: repeated movements or sounds (tics) or Tourette's syndrome, or a family history of tics or Tourette's syndrome.

**L61.0** `Incomplete Sentence` (0.865) → `excluded_incomplete`
- original: Also tell your doctor if you are pregnant, intending to become pregnant, or breastfeeding.

**L62.0** `Simple Sentence` (0.832) → `passthrough`
- original: Taking Adderall during pregnancy can cause premature birth, low birth weight, or withdrawal symptoms in the newborn baby.

**L62.1** `Incomplete Sentence` (0.933) → `excluded_incomplete`
- original: Tell your healthcare provider if you are pregnant or plan to become pregnant.

**L62.2** `Simple Sentence` (0.406) → `passthrough`
- original: There is a pregnancy registry that collects information about the health of females exposed to Adderall and their babies.
- pronoun resolved: There is a pregnancy registry that collects information about the health of females exposed to Adderall and females's babies.
  - edits: “their” → “females's”

**L63.0** `Simple Sentence` (0.924) → `passthrough`
- original: Adderall passes into breast milk and may harm a nursing baby.

**L63.1** `Simple Sentence` (0.983) → `passthrough`
- original: You should not breastfeed during treatment with Adderall.

**L63.2** `Incomplete Sentence` (0.946) → `excluded_incomplete`
- original: Talk to your healthcare provider about the best way to feed the baby during treatment.

## How should I take Adderall?

**L66.0** `Incomplete Sentence` (0.979) → `excluded_incomplete`
- original: Take Adderall exactly as prescribed by your healthcare provider.

**L66.1** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Follow all directions on your prescription label.

**L66.2** `Simple Sentence` (0.984) → `passthrough`
- original: Your doctor may occasionally change your dose.

**L66.3** `Incomplete Sentence` (0.905) → `excluded_incomplete`
- original: Do not take this medicine in larger or smaller amounts or for longer than recommended.
- pronoun resolved: Do not take Adderall in larger or smaller amounts or for longer than recommended.
  - edits: “this medicine” → “Adderall”

**L67.0** `Simple Sentence` (0.975) → `passthrough`
- original: The first dose of the day is usually taken when you first wake up.

**L67.1** `Simple Sentence` (0.985) → `passthrough`
- original: Taking this medicine in the afternoon may cause trouble sleeping.
- pronoun resolved: Taking Adderall in the afternoon may cause trouble sleeping.
  - edits: “this medicine” → “Adderall”

**L68.0** `Simple Sentence` (0.986) → `passthrough`
- original: Adderall can be taken with or without food.

**L69.0** `Incomplete Sentence` (0.938) → `excluded_incomplete`
- original: Do not crush or chew an extended-release capsule.

**L69.1** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Swallow it whole.

**L69.2** `Complex Sentence` (0.723) → `decomposed`
- original: To make swallowing easier, you may open the capsule and sprinkle the medicine into a spoonful of applesauce, then swallow all of the mixture right away without chewing.
- pronoun resolved: To make swallowing easier, you may open the capsule and sprinkle Adderall into a spoonful of applesauce, then swallow all of the mixture right away without chewing.
  - edits: “the medicine” → “Adderall”
  - S1: To make swallowing easier, you may open the capsule.
  - S2: You may sprinkle Adderall into a spoonful of applesauce.
  - S3: Then swallow all of the mixture right away.
  - S4: Do not chew the mixture.

**L69.3** `Compound Sentence` (0.889) → `decomposed`
- original: Do not divide the medicine in the capsule, and do not save the mixture for later use.
- pronoun resolved: Do not divide Adderall in the capsule, and do not save the mixture for later use.
  - edits: “the medicine” → “Adderall”
  - S1: Do not divide Adderall in the capsule.
  - S2: Do not save the mixture for later use.

**L70.0** `Simple Sentence` (0.986) → `passthrough`
- original: Adderall may be habit-forming.

**L70.1** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Never share this medicine with another person, especially someone with a history of drug abuse or addiction.
- pronoun resolved: Never share Adderall with another person, especially someone with a history of drug abuse or addiction.
  - edits: “this medicine” → “Adderall”

**L70.2** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Keep the medicine where others cannot get to it.
- pronoun resolved: Keep Adderall where others cannot get to it.
  - edits: “the medicine” → “Adderall”

**L71.0** `Simple Sentence` (0.855) → `passthrough`
- original: While using this medicine, your doctor will need to check your progress at regular visits.
- pronoun resolved: While using Adderall, your doctor will need to check your progress at regular visits.
  - edits: “this medicine,” → “Adderall,”

**L71.1** `Compound Sentence` (0.832) → `decomposed`
- original: Adderall can cause unusual results with certain medical tests, so tell any doctor who treats you that you are using this medicine.
- pronoun resolved: Adderall can cause unusual results with certain medical tests, so tell any doctor who treats you that you are using Adderall.
  - edits: “this medicine.” → “Adderall.”
  - S1: Adderall can cause unusual results with certain medical tests.
  - S2: Tell any doctor who treats you that you are using Adderall.

**L71.2** `Simple Sentence` (0.799) → `passthrough`
- original: Your healthcare provider may tell you to stop taking this medicine for a short time before you get certain imaging tests.
- pronoun resolved: Your healthcare provider may tell you to stop taking Adderall for a short time before you get certain imaging tests.
  - edits: “this medicine” → “Adderall”

## Dosing information

**L74.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual adult dose for ADHD:

**L75.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Immediate-release (IR):

**L76.0** `Incomplete Sentence` (0.94) → `excluded_incomplete`
- original: Initial dose: 5 mg orally 1 or 2 times a day.

**L77.0** `Simple Sentence` (0.606) → `passthrough`
- original: Maintenance dose: the daily dose may be raised in 5 mg increments at weekly intervals until an optimal response is obtained.

**L78.0** `Simple Sentence` (0.715) → `passthrough`
- original: Maximum dose: only in rare cases will it be necessary to exceed 40 mg per day.
- pronoun resolved: Maximum dose: only in rare cases will Maximum dose be necessary to exceed 40 mg per day.
  - edits: “it” → “Maximum dose”

**L79.0** `Compound Sentence` (0.701) → `decomposed`
- original: The first dose should be given upon awakening, with 1 to 2 additional doses at intervals of 4 to 6 hours.
  - S1: The first dose should be given upon awakening.
  - S2: One to two additional doses should be given at intervals of 4 to 6 hours.

**L80.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Extended-release (XR), for patients starting treatment for the first time or switching from another medication:

**L81.0** `Incomplete Sentence` (0.894) → `excluded_incomplete`
- original: Initial dose: 20 mg orally once a day.

**L82.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual adult dose for narcolepsy:

**L83.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Immediate-release (IR):

**L84.0** `Incomplete Sentence` (0.935) → `excluded_incomplete`
- original: Initial dose: 10 mg orally per day in divided doses.

**L85.0** `Simple Sentence` (0.609) → `passthrough`
- original: Maintenance dose: the daily dose may be raised in 10 mg increments at weekly intervals until an optimal response is obtained.

**L86.0** `Compound Sentence` (0.499) → `decomposed`
- original: The usual dose is 5 to 60 mg per day in divided doses, depending on the individual patient response.
  - S1: The usual dose is 5 to 60 mg per day in divided doses.
  - S2: This depends on the individual patient response.

**L87.0** `Compound Sentence` (0.692) → `decomposed`
- original: The first dose should be given on awakening, with 1 to 2 additional doses at intervals of 4 to 6 hours.
  - S1: The first dose should be given on awakening.
  - S2: One to two additional doses should be given at intervals of 4 to 6 hours.

**L88.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual pediatric dose for ADHD:

**L89.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Immediate-release (IR), ages 3 to 5 years:

**L90.0** `Incomplete Sentence` (0.951) → `excluded_incomplete`
- original: Initial dose: 2.5 mg orally per day.

**L91.0** `Simple Sentence` (0.557) → `passthrough`
- original: Maintenance dose: the daily dose may be raised in 2.5 mg increments at weekly intervals until an optimal response is obtained.

**L92.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Immediate-release (IR), ages 6 to 17 years:

**L93.0** `Incomplete Sentence` (0.94) → `excluded_incomplete`
- original: Initial dose: 5 mg orally 1 or 2 times a day.

**L94.0** `Simple Sentence` (0.606) → `passthrough`
- original: Maintenance dose: the daily dose may be raised in 5 mg increments at weekly intervals until an optimal response is obtained.

**L95.0** `Simple Sentence` (0.715) → `passthrough`
- original: Maximum dose: only in rare cases will it be necessary to exceed 40 mg per day.
- pronoun resolved: Maximum dose: only in rare cases will Maximum dose be necessary to exceed 40 mg per day.
  - edits: “it” → “Maximum dose”

**L96.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Extended-release (XR), ages 6 to 12 years:

**L97.0** `Incomplete Sentence` (0.847) → `excluded_incomplete`
- original: Initial dose: 5 or 10 mg orally once a day in the morning.

**L98.0** `Simple Sentence` (0.948) → `passthrough`
- original: Maintenance dose: the daily dose may be raised in 5 to 10 mg increments at weekly intervals.

**L99.0** `Incomplete Sentence` (0.961) → `excluded_incomplete`
- original: Maximum dose: 30 mg per day.

**L100.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Extended-release (XR), ages 13 to 17 years:

**L101.0** `Incomplete Sentence` (0.904) → `excluded_incomplete`
- original: Initial dose: 10 mg orally once a day.

**L102.0** `Simple Sentence` (0.865) → `passthrough`
- original: Maintenance dose: may be increased to 20 mg per day after one week if symptoms are not adequately controlled.

**L103.0** `Incomplete Sentence` (0.961) → `excluded_incomplete`
- original: Maximum dose: 30 mg per day.

**L104.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual pediatric dose for narcolepsy:

**L105.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Immediate-release (IR), ages 6 to 11 years:

**L106.0** `Incomplete Sentence` (0.935) → `excluded_incomplete`
- original: Initial dose: 5 mg orally per day in divided doses.

**L107.0** `Simple Sentence` (0.606) → `passthrough`
- original: Maintenance dose: the daily dose may be raised in 5 mg increments at weekly intervals until an optimal response is obtained.

**L108.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Immediate-release (IR), ages 12 years and older:

**L109.0** `Incomplete Sentence` (0.935) → `excluded_incomplete`
- original: Initial dose: 10 mg orally per day in divided doses.

**L110.0** `Simple Sentence` (0.609) → `passthrough`
- original: Maintenance dose: the daily dose may be raised in 10 mg increments at weekly intervals until an optimal response is obtained.

**L111.0** `Simple Sentence` (0.989) → `passthrough`
- original: Narcolepsy rarely occurs in children under 12 years of age.

## What happens if I miss a dose?

**L114.0** `Incomplete Sentence` (0.712) → `excluded_incomplete`
- original: Take the missed dose as soon as you remember, but not late in the day.

**L114.1** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Skip the missed dose if it is almost evening.

**L114.2** `Incomplete Sentence` (0.83) → `excluded_incomplete`
- original: Do not take extra medicine to make up for the missed dose.

## What happens if I overdose?

**L117.0** `Compound Sentence` (0.443) → `decomposed`
- original: If you or your child takes too much Adderall, call your healthcare provider or the Poison Help line at 1-800-222-1222, or go to the nearest hospital emergency room right away.
  - S1: If you or your child takes too much Adderall, call your healthcare provider or the Poison Help line at 1-800-222-1222.
  - S2: If you or your child takes too much Adderall, go to the nearest hospital emergency room right away.

**L117.1** `Simple Sentence` (0.987) → `passthrough`
- original: An overdose of Adderall could be fatal.

**L118.0** `Compound Sentence` (0.497) → `decomposed`
- original: Overdose symptoms may include restlessness, tremor, muscle twitches, rapid breathing, confusion, hallucinations, panic, aggressiveness, muscle pain or weakness, and dark colored urine.
  - S1: Overdose symptoms may include restlessness.
  - S2: Overdose symptoms may include tremor.
  - S3: Overdose symptoms may include muscle twitches.
  - S4: Overdose symptoms may include rapid breathing.
  - S5: Overdose symptoms may include confusion.
  - S6: Overdose symptoms may include hallucinations.
  - S7: Overdose symptoms may include panic.
  - S8: Overdose symptoms may include aggressiveness.
  - S9: Overdose symptoms may include muscle pain or weakness.
  - S10: Overdose symptoms may include dark colored urine.

**L118.1** `Simple Sentence` (0.974) → `passthrough`
- original: These symptoms may be followed by depression and tiredness.

**L118.2** `Simple Sentence` (0.625) → `passthrough`
- original: Other symptoms include nausea, vomiting, diarrhea, stomach pain, uneven heartbeats, feeling light-headed, fainting, seizure, or coma.

## What to avoid

**L121.0** `Simple Sentence` (0.986) → `passthrough`
- original: This medicine may impair your thinking or reactions.
- pronoun resolved: Adderall may impair your thinking or reactions.
  - edits: “This medicine” → “Adderall”

**L121.1** `Incomplete Sentence` (0.688) → `excluded_incomplete`
- original: Be careful if you drive or do anything that requires you to be alert.

**L122.0** `Incomplete Sentence` (0.921) → `excluded_incomplete`
- original: Avoid drinking fruit juices or taking vitamin C at the same time you take Adderall.

**L122.1** `Simple Sentence` (0.987) → `passthrough`
- original: These can make your body absorb less of the medicine.

## What other drugs will affect Adderall?

**L125.0** `Incomplete Sentence` (0.903) → `excluded_incomplete`
- original: Ask your doctor before using a stomach acid medicine (including Alka-Seltzer or sodium bicarbonate).

**L125.1** `Compound Sentence` (0.727) → `decomposed`
- original: Some of these medicines can change the way your body absorbs Adderall and may increase side effects.
- pronoun resolved: Some of stomach acid medicine can change the way your body absorbs Adderall and may increase side effects.
  - edits: “these medicines” → “stomach acid medicine”
  - S1: Some of stomach acid medicine can change the way your body absorbs Adderall.
  - S2: It may increase side effects.

**L126.0** `Simple Sentence` (0.384) → `passthrough`
- original: Some medicines can interact with amphetamine and dextroamphetamine and cause a serious condition called serotonin syndrome.

**L126.1** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Tell your doctor about all your current medicines and any you start or stop using, especially:

**L127.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: selective serotonin reuptake inhibitors (SSRIs) and serotonin norepinephrine reuptake inhibitors (SNRIs)

**L128.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: tricyclic antidepressants

**L129.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: medicines used to treat migraine headaches, called triptans

**L130.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: lithium, buspirone, tramadol, fentanyl, or tryptophan

**L131.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: St. John's Wort

**L132.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: blood pressure medicine

**L133.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: heartburn medicine

**L134.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: a blood thinner such as warfarin

**L135.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: cold or allergy medicine that contains a decongestant

**L136.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: opioid (narcotic) medicine

**L137.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: seizure medicine.

**L138.0** `Compound Sentence` (0.965) → `decomposed`
- original: This list is not complete, and many other drugs can interact with Adderall, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: This list is not complete.
  - S2: Many other drugs can interact with Adderall.
  - S3: These include prescription and over-the-counter medicines, vitamins, and herbal products.

**L138.1** `Incomplete Sentence` (0.956) → `excluded_incomplete`
- original: Give a list of all your medicines to any healthcare provider who treats you.

**L138.2** `Simple Sentence` (0.801) → `passthrough`
- original: Do not start any new medicine during treatment with Adderall without talking to your healthcare provider first.

## How should I store and dispose of Adderall?

**L141.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: Store Adderall at room temperature between 68°F and 77°F (20°C and 25°C).

**L142.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Protect Adderall from light.

**L143.0** `Incomplete Sentence` (0.633) → `excluded_incomplete`
- original: Store Adderall in a safe place, such as a locked cabinet, and keep it out of the reach of children.
- pronoun resolved: Store Adderall in a safe place, such as a locked cabinet, and keep Adderall out of the reach of children.
  - edits: “it” → “Adderall”

**L144.0** `Incomplete Sentence` (0.972) → `excluded_incomplete`
- original: Dispose of remaining, unused, or expired Adderall through a medicine take-back program at a US Drug Enforcement Administration (DEA) authorized collection site.

**L144.1** `Complex Sentence` (0.629) → `decomposed`
- original: If no take-back program or DEA-authorized collector is available, mix Adderall with an undesirable, nontoxic substance such as dirt, cat litter, or used coffee grounds to make it less appealing to children and pets.
  - S1: If no take-back program or DEA-authorized collector is available, mix Adderall with an undesirable, nontoxic substance.
  - S2: The substance should be such as dirt, cat litter, or used coffee grounds.
  - S3: This makes it less appealing to children and pets.

**L144.2** `Incomplete Sentence` (0.788) → `excluded_incomplete`
- original: Place the mixture in a sealed container such as a plastic bag and throw it away in the household trash.
- pronoun resolved: Place the mixture in a sealed container such as a plastic bag and throw mixture away in the household trash.
  - edits: “it” → “mixture”

**L144.3** `Incomplete Sentence` (0.607) → `excluded_incomplete`
- original: Visit www.fda.gov/drugdisposal for more information on disposing of unused medicines.

## Adderall ingredients

**L147.0** `Incomplete Sentence` (0.713) → `excluded_incomplete`
- original: Active ingredients: dextroamphetamine saccharate, amphetamine aspartate, dextroamphetamine sulfate, and amphetamine sulfate.

**L148.0** `Simple Sentence` (0.377) → `passthrough`
- original: Inactive ingredients: colloidal silicon dioxide, compressible sugar (sucrose and maltodextrin), corn starch, magnesium stearate, microcrystalline cellulose, and saccharin sodium.

**L148.1** `Simple Sentence` (0.722) → `passthrough`
- original: The 5 mg tablet is white to off-white and contains no color additives.

**L148.2** `Simple Sentence` (0.98) → `passthrough`
- original: The 7.5 mg and 10 mg tablets also contain FD&C Blue #1 Aluminum Lake.

**L148.3** `Simple Sentence` (0.974) → `passthrough`
- original: The 12.5 mg, 15 mg, 20 mg, and 30 mg tablets also contain FD&C Yellow #6 Aluminum Lake.

## Manufacturer

**L151.0** `Simple Sentence` (0.964) → `passthrough`
- original: Adderall is manufactured for Teva Pharmaceuticals, Parsippany, NJ 07054.

**L151.1** `Simple Sentence` (0.869) → `passthrough`
- original: For more information about Adderall, contact Teva at 1-888-838-2872.

## Popular FAQ

**L154.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Q: How long does Adderall stay in your system (urine drug test)?

**L154.1** `Simple Sentence` (0.98) → `passthrough`
- original: A: It would take just over 2 days for a dose to be out of your system.
- pronoun resolved: A: Adderall would take just over 2 days for a dose to be out of your system.
  - edits: “It” → “Adderall”

**L154.2** `Simple Sentence` (0.824) → `passthrough`
- original: You should allow for longer (7 days) if you have taken Adderall frequently and at high doses.

**L155.0** `Compound-Complex Sentence` (0.761) → `decomposed`
- original: Q: Adderall vs Vyvanse: Key Differences, Effectiveness, and Cost Comparison A: The primary difference between Adderall and Vyvanse lies in their composition: Adderall contains a mixture of four different amphetamine salts, while Vyvanse contains only one type of amphetamine salt called lisdexamfetamine.
- pronoun resolved: Q: Adderall vs Vyvanse: Key Differences, Effectiveness, and Cost Comparison A: The primary difference between Adderall and Vyvanse lies in Adderall and Vyvanse's composition: Adderall contains a mixture of four different amphetamine salts, while Vyvanse contains only one type of amphetamine salt called lisdexamfetamine.
  - edits: “their” → “Adderall and Vyvanse's”
  - S1: The primary difference between Adderall and Vyvanse lies in their composition.
  - S2: Adderall contains a mixture of four different amphetamine salts.
  - S3: Vyvanse contains only one type of amphetamine salt.
  - S4: That one type of amphetamine salt is called lisdexamfetamine.

**L155.1** `Simple Sentence` (0.899) → `passthrough`
- original: Lisdexamfetamine (Vyvanse) is a prodrug that converts into dexamphetamine once absorbed by the body.

**L155.2** `Compound Sentence` (0.406) → `decomposed`
- original: Adderall's four amphetamine salts include dextroamphetamine saccharate, amphetamine aspartate, dextroamphetamine sulfate, and amphetamine sulfate.
  - S1: Adderall's four amphetamine salts include dextroamphetamine saccharate.
  - S2: They include amphetamine aspartate.
  - S3: They include dextroamphetamine sulfate.
  - S4: They include amphetamine sulfate.

**L156.0** `Incomplete Sentence` (0.945) → `excluded_incomplete`
- original: Q: How should Adderall make you feel, with or without ADHD?

**L156.1** `Complex Sentence` (0.763) → `decomposed`
- original: A: People taking Adderall for ADHD typically notice improved focus and attention and reduced impulsivity.
  - S1: People taking Adderall for ADHD typically notice improved focus and attention.
  - S2: People taking Adderall for ADHD typically notice reduced impulsivity.

**L156.2** `Complex Sentence` (0.526) → `decomposed`
- original: In people without ADHD, it can also enhance focus, alertness, and energy levels.
- pronoun resolved: In people without ADHD, Adderall can also enhance focus, alertness, and energy levels.
  - edits: “it” → “Adderall”
  - S1: In people without ADHD, Adderall can enhance focus.
  - S2: In people without ADHD, Adderall can enhance alertness.
  - S3: In people without ADHD, Adderall can enhance energy levels.

**L157.0** `Incomplete Sentence` (0.817) → `excluded_incomplete`
- original: Q: How long does Adderall last in your system?

**L157.1** `Simple Sentence` (0.754) → `passthrough`
- original: A: When taken as prescribed, the effects of Adderall last for about 4 to 6 hours.

**L157.2** `Complex Sentence` (0.788) → `decomposed`
- original: The effects of Adderall XR last for up to 12 hours because this brand of Adderall is designed for slow and sustained release.
  - S1: The effects of Adderall XR last for up to 12 hours.
  - S2: This is because this brand of Adderall is designed for slow and sustained release.

**L158.0** `Incomplete Sentence` (0.951) → `excluded_incomplete`
- original: Q: Modafinil (Provigil) vs Adderall: What's the difference?

**L158.1** `Complex Sentence` (0.904) → `decomposed`
- original: A: Modafinil and Adderall are both classified as CNS stimulants but have different chemical structures, which means there are differences in their addiction potential and risk of side effects.
  - S1: Modafinil and Adderall are both classified as CNS stimulants.
  - S2: They have different chemical structures.
  - S3: This means there are differences in their addiction potential and risk of side effects.

**L158.2** `Compound Sentence` (0.964) → `decomposed`
- original: Modafinil and Adderall both have stimulant-type effects, but modafinil is a much milder stimulant than Adderall.
  - S1: Modafinil and Adderall both have stimulant-type effects.
  - S2: Modafinil is a much milder stimulant than Adderall.

**L159.0** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: Q: Focalin vs Adderall: What's the difference?

**L159.1** `Compound Sentence` (0.635) → `decomposed`
- original: A: Focalin contains dexmethylphenidate whereas Adderall contains a mixture of amphetamine salts (MAS).
  - S1: Focalin contains dexmethylphenidate.
  - S2: Adderall contains a mixture of amphetamine salts.

**L159.2** `Compound-Complex Sentence` (0.914) → `decomposed`
- original: Both have a high potential for abuse and dependence, although the risk may be perceived as higher with Adderall because it is more popular; however, this does not mean Focalin is less likely to cause tolerance or dependence.
- pronoun resolved: Both have a high potential for abuse and dependence, although the risk may be perceived as higher with Adderall because Adderall is more popular; however, this does not mean Focalin is less likely to cause tolerance or dependence.
  - edits: “it” → “Adderall”
  - S1: Both Adderall and Focalin have a high potential for abuse and dependence.
  - S2: The risk of abuse and dependence may be perceived as higher with Adderall.
  - S3: Adderall is more popular than Focalin.
  - S4: This perception does not mean Focalin is less likely to cause tolerance or dependence.

**L160.0** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: Q: How long does Adderall withdrawal last?

**L160.1** `Complex Sentence` (0.771) → `decomposed`
- original: A: It is difficult to say exactly how long Adderall withdrawal lasts because it depends on the person and the process is different for everyone.
- pronoun resolved: A: It is difficult to say exactly how long Adderall withdrawal lasts because Adderall withdrawal depends on the person and the process is different for everyone.
  - edits: “it” → “Adderall withdrawal”
  - S1: It is difficult to say exactly how long Adderall withdrawal lasts.
  - S2: Adderall withdrawal depends on the person.
  - S3: The process is different for everyone.

**L160.2** `Compound Sentence` (0.886) → `decomposed`
- original: Some people’s withdrawal symptoms may resolve in as little as 5 days, others may still be experiencing symptoms 4 weeks later or even longer.
  - S1: Some people's withdrawal symptoms may resolve in as little as 5 days.
  - S2: Others may still be experiencing symptoms 4 weeks later or even longer.

**L160.3** `Complex Sentence` (0.877) → `decomposed`
- original: People who have taken Adderall for a long time at a high dose should expect withdrawal symptoms to last longer, sometimes several months.
  - S1: People who have taken Adderall for a long time at a high dose should expect withdrawal symptoms.
  - S2: The withdrawal symptoms may last longer.
  - S3: Sometimes the symptoms can last several months.

**L161.0** `Incomplete Sentence` (0.877) → `excluded_incomplete`
- original: Q: How do you get rid of Adderall tongue?

**L161.1** `Complex Sentence` (0.616) → `decomposed`
- original: A: Adderall tongue is a common side effect of Adderall that can detrimentally and seriously affect a person’s quality of life.
  - S1: Adderall tongue is a common side effect of Adderall.
  - S2: Adderall tongue can affect a person's quality of life.
  - S3: The effect can be detrimental and serious.

**L161.2** `Incomplete Sentence` (0.914) → `excluded_incomplete`
- original: To help relieve Adderall tongue stay well-hydrated.

**L161.3** `Compound Sentence` (0.918) → `decomposed`
- original: Adderall and other ADHD medications can cause dehydration, so you need to drink at least 6 to 8 glasses of fluid per day.
  - S1: Adderall and other ADHD medications can cause dehydration.
  - S2: You need to drink at least 6 to 8 glasses of fluid per day.

**L161.4** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Take frequent sips of water rather than drinking a whole glass of water at once.

**L161.5** `Incomplete Sentence` (0.826) → `excluded_incomplete`
- original: Use artificial saliva products (such as sprays or lozenges) – these can help moisten the tissue and last longer than water.
- pronoun resolved: Use artificial saliva products (such as sprays or lozenges) – artificial saliva products can help moisten the tissue and last longer than water.
  - edits: “these” → “artificial saliva products”

**L161.6** `Compound Sentence` (0.951) → `decomposed`
- original: There are many different brands of these available over the counter at drug stores and they can be used multiple times a day.
- pronoun resolved: There are many different brands of these available over the counter at drug stores and artificial saliva products can be used multiple times a day.
  - edits: “they” → “artificial saliva products”
  - S1: There are many different brands of these available over the counter at drug stores.
  - S2: Artificial saliva products can be used multiple times a day.

**L161.7** `Incomplete Sentence` (0.334) → `excluded_incomplete`
- original: Chew sugar-free gum or suck on sugar-free candy – this contains xylitol which increases salivary flow and can help prevent dental decay.

**L161.8** `Incomplete Sentence` (0.874) → `excluded_incomplete`
- original: Avoid sucking candy that contains sugar because this will increase your risk of dental decay
- pronoun resolved: Avoid sucking candy that contains sugar because sucking candy that contains sugar will increase your risk of dental decay
  - edits: “this” → “sucking candy that contains sugar”

**L162.0** `Incomplete Sentence` (0.922) → `excluded_incomplete`
- original: Q: Does Adderall help with anxiety and depression?

**L162.1** `Complex Sentence` (0.935) → `decomposed`
- original: A: Although Adderall is only FDA-approved for the treatment of attention-deficit hyperactivity disorder (ADHD) and narcolepsy, it has been used rarely and off-label to treat depression that has not responded to other treatments.
- pronoun resolved: A: Although Adderall is only FDA-approved for the treatment of attention-deficit hyperactivity disorder (ADHD) and narcolepsy, Adderall has been used rarely and off-label to treat depression that has not responded to other treatments.
  - edits: “it” → “Adderall”
  - S1: Adderall is only FDA-approved for the treatment of attention-deficit hyperactivity disorder (ADHD) and narcolepsy.
  - S2: Adderall has been used rarely and off-label to treat depression.
  - S3: This depression has not responded to other treatments.

**L162.2** `Compound Sentence` (0.886) → `decomposed`
- original: However, this is controversial and there is a lack of good quality evidence to support its use.
- pronoun resolved: However, this is controversial and there is a lack of good quality evidence to support Adderall's use.
  - edits: “its” → “Adderall's”
  - S1: However, this is controversial.
  - S2: There is a lack of good quality evidence to support Adderall's use.

**L162.3** `Compound Sentence` (0.593) → `decomposed`
- original: There is no evidence that Adderall helps with anxiety and in many people with pre-existing mood disorders, Adderall can make depression and/or anxiety worse.
  - S1: There is no evidence that Adderall helps with anxiety.
  - S2: In many people with pre-existing mood disorders, Adderall can make depression and/or anxiety worse.
