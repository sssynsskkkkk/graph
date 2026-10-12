# Methylphenidate — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/methylphenidate.txt` · 118 sentences · 7 changed by pronoun resolution · 170 sentences sent to EDC

## What is methylphenidate?

**L5.0** `Simple Sentence` (0.982) → `passthrough`
- original: Methylphenidate is a central nervous system stimulant.

**L5.1** `Simple Sentence` (0.902) → `passthrough`
- original: It affects chemicals in the brain and nerves that contribute to hyperactivity and impulse control.
- pronoun resolved: Methylphenidate affects chemicals in the brain and nerves that contribute to hyperactivity and impulse control.
  - edits: “It” → “Methylphenidate”

**L6.0** `Simple Sentence` (0.766) → `passthrough`
- original: Methylphenidate is used to treat attention deficit disorder (ADD), attention deficit hyperactivity disorder (ADHD), and narcolepsy.

**L7.0** `Complex Sentence` (0.728) → `decomposed`
- original: Methylphenidate should be used as a part of a total treatment program for ADHD that may include counseling or other therapies.
  - S1: Methylphenidate should be used as a part of a total treatment program for ADHD.
  - S2: The program may include counseling.
  - S3: The program may include other therapies.

## Warnings

**L10.0** `Simple Sentence` (0.988) → `passthrough`
- original: Methylphenidate may be habit-forming.

**L10.1** `Simple Sentence` (0.981) → `passthrough`
- original: Misuse can cause addiction, overdose, or death.

**L10.2** `Incomplete Sentence` (0.926) → `excluded_incomplete`
- original: Tell your doctor if you have had problems with drug or alcohol abuse.

**L11.0** `Simple Sentence` (0.76) → `passthrough`
- original: Stimulants have caused stroke, heart attack, and sudden death in people with high blood pressure, heart disease, or a heart defect.

**L12.0** `Compound Sentence` (0.482) → `decomposed`
- original: Do not use methylphenidate if you have used an MAO inhibitor in the past 14 days, such as isocarboxazid, linezolid, methylene blue injection, phenelzine, rasagiline, selegiline, or tranylcypromine.
  - S1: Do not use methylphenidate if you have used an MAO inhibitor in the past 14 days.
  - S2: Examples of such inhibitors include isocarboxazid, linezolid, methylene blue injection, phenelzine, rasagiline, selegiline, or tranylcypromine.

**L13.0** `Complex Sentence` (0.726) → `decomposed`
- original: Methylphenidate may cause new or worsening psychosis (unusual thoughts or behavior), especially if you have a history of depression, mental illness, or bipolar disorder.
  - S1: Methylphenidate may cause new or worsening psychosis.
  - S2: Psychosis involves unusual thoughts or behavior.
  - S3: This risk is especially high if you have a history of depression, mental illness, or bipolar disorder.

**L14.0** `Simple Sentence` (0.85) → `passthrough`
- original: You may have blood circulation problems that can cause numbness, pain, or discoloration in your fingers or toes.

**L15.0** `Compound Sentence` (0.405) → `decomposed`
- original: Call your doctor right away if you have: signs of heart problems - chest pain, feeling light-headed or short of breath; signs of psychosis - paranoia, aggression, new behavior problems, seeing or hearing things that are not real; signs of circulation problems - unexplained wounds on your fingers or toes.
  - S1: Call your doctor right away if you have signs of heart problems.
  - S2: Signs of heart problems include chest pain, feeling light-headed, or being short of breath.
  - S3: Call your doctor right away if you have signs of psychosis.
  - S4: Signs of psychosis include paranoia, aggression, new behavior problems, or seeing or hearing things that are not real.
  - S5: Call your doctor right away if you have signs of circulation problems.
  - S6: Signs of circulation problems include unexplained wounds on your fingers or toes.

**L16.0** `Incomplete Sentence` (0.953) → `excluded_incomplete`
- original: Tell your doctor if you have a history of drug or alcohol addiction.

**L16.1** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Keep the medication where others cannot get to it.

## Before taking this medicine

**L19.0** `Simple Sentence` (0.949) → `passthrough`
- original: You should not use methylphenidate if you are allergic to it, or if you have:
- pronoun resolved: You should not use methylphenidate if you are allergic to methylphenidate, or if you have:
  - edits: “it,” → “methylphenidate,”

**L20.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: glaucoma:

**L21.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: pheochromocytoma (tumor of the adrenal gland);

**L22.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: severe high blood pressure or a heart problem;

**L23.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: overactive thyroid;

**L24.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: a personal or family history of tics (muscle twitches) or Tourette's syndrome; or

**L25.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: severe anxiety, tension, or agitation (stimulant medicine can make these symptoms worse).

**L26.0** `Simple Sentence` (0.984) → `passthrough`
- original: Stimulants have caused stroke, heart attack, and sudden death in certain people.

**L26.1** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: Tell your doctor if you have:

**L27.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: heart problems or a congenital heart defect;

**L28.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: high blood pressure; or

**L29.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a family history of heart disease or sudden death.

**L30.0** `Simple Sentence` (0.577) → `passthrough`
- original: Do not use methylphenidate if you have used an MAO inhibitor in the past 14 days.

**L30.1** `Simple Sentence` (0.94) → `passthrough`
- original: A dangerous drug interaction could occur.

**L30.2** `Simple Sentence` (0.954) → `passthrough`
- original: MAO inhibitors include isocarboxazid, linezolid, methylene blue injection, phenelzine, and tranylcypromine.

**L31.0** `Incomplete Sentence` (0.404) → `excluded_incomplete`
- original: Tell your doctor if you also use opioid medicine, herbal products, or medicine for depression, mental illness, Parkinson's disease, migraine headaches, serious infections, or prevention of nausea and vomiting.

**L31.1** `Simple Sentence` (0.988) → `passthrough`
- original: An interaction with methylphenidate could cause a serious condition called serotonin syndrome.

**L32.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Tell your doctor if you or anyone in your family has ever had:

**L33.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: depression, mental illness, bipolar disorder, psychosis, or suicidal thoughts or actions;

**L34.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: blood circulation problems in the hands or feet;

**L35.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: alcoholism or drug addiction; or

**L36.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: if you take Adhansia - an allergy to aspirin or yellow food dye.

**L37.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: phenylketonuria (PKU), as some chewable tablets contain phenylalanine.

**L38.0** `Incomplete Sentence` (0.585) → `excluded_incomplete`
- original: To make sure methylphenidate is safe for you, tell your doctor if you have::

**L39.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: problems with the esophagus, stomach, or intestines; or

**L40.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: seizures, epilepsy, or an abnormal brain wave test (EEG).

**L41.0** `Simple Sentence` (0.984) → `passthrough`
- original: Becoming dependent on methylphenidate during pregnancy can cause premature birth or low birth weight.

**L41.1** `Incomplete Sentence` (0.915) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or plan to become pregnant.

**L41.2** `Complex Sentence` (0.674) → `decomposed`
- original: If you are pregnant, your name may be listed on a pregnancy registry to track the effects of methylphenidate on the baby.
  - S1: If you are pregnant, your name may be listed on a pregnancy registry.
  - S2: The registry tracks the effects of methylphenidate on the baby.

**L42.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Ask a doctor if it is safe to breastfeed while using this medicine.
- pronoun resolved: Ask a doctor if it is safe to breastfeed while using methylphenidate.
  - edits: “this medicine.” → “methylphenidate.”

**L42.1** `Complex Sentence` (0.688) → `decomposed`
- original: If you are breastfeeding, tell your doctor if you notice symptoms in the baby such as agitation, sleep problems, feeding problems, or reduced weight gain.
  - S1: If you are breastfeeding, tell your doctor if you notice symptoms in the baby.
  - S2: The symptoms include agitation, sleep problems, feeding problems, or reduced weight gain.

**L43.0** `Simple Sentence` (0.988) → `passthrough`
- original: methylphenidate is not approved for use by anyone younger than 6 years old.

## How should I take methylphenidate?

**L46.0** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Take methylphenidate exactly as prescribed by your doctor.

**L46.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L46.2** `Simple Sentence` (0.984) → `passthrough`
- original: Your doctor may occasionally change your dose.

**L47.0** `Simple Sentence` (0.988) → `passthrough`
- original: Methylphenidate may be habit-forming.

**L47.1** `Simple Sentence` (0.981) → `passthrough`
- original: Misuse can cause addiction, overdose, or death.

**L47.2** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Keep the medication where others cannot get to it.

**L47.3** `Simple Sentence` (0.981) → `passthrough`
- original: Selling or giving away this medicine is against the law.

**L48.0** `Simple Sentence` (0.746) → `passthrough`
- original: Your dose needs may change if you switch to a different brand, strength, or form of this medicine.

**L48.1** `Incomplete Sentence` (0.936) → `excluded_incomplete`
- original: Avoid medication errors by using only the medicine your doctor prescribes.

**L49.0** `Simple Sentence` (0.987) → `passthrough`
- original: Most brands of methylphenidate are taken 1 or 2 times during the day.

**L49.1** `Simple Sentence` (0.953) → `passthrough`
- original: Jornay PM is for use only at night between 6:30 and 9:30 pm.

**L50.0** `Compound Sentence` (0.481) → `decomposed`
- original: You may take methylphenidate with or without food, but take it the same way each time.
- pronoun resolved: You may take methylphenidate with or without food, but take methylphenidate the same way each time.
  - edits: “it” → “methylphenidate”
  - S1: You may take methylphenidate with or without food.
  - S2: Take methylphenidate the same way each time.

**L51.0** `Simple Sentence` (0.349) → `passthrough`
- original: Swallow the extended-release capsule or tablet whole and do not crush, chew, or break it.

**L52.0** `Complex Sentence` (0.549) → `decomposed`
- original: If you cannot swallow an extended-release CAPSULE whole, open it and mix the medicine with soft food such as applesauce, pudding or yogurt.
  - S1: If you cannot swallow an extended-release CAPSULE whole, open it.
  - S2: Mix the medicine with soft food.
  - S3: Examples of soft food include applesauce, pudding, or yogurt.

**L52.1** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Swallow the mixture right away WITHOUT CHEWING.

**L53.0** `Compound Sentence` (0.689) → `decomposed`
- original: You must chew the chewable tablet well and swallow it with at least 8 ounces (a full glass) of water or other liquid to prevent choking.
- pronoun resolved: You must chew the chewable tablet well and swallow chewable tablet with at least 8 ounces (a full glass) of water or other liquid to prevent choking.
  - edits: “it” → “chewable tablet”
  - S1: You must chew the chewable tablet well.
  - S2: You must swallow the chewable tablet with at least 8 ounces (a full glass) of water or other liquid.
  - S3: This is done to prevent choking.

**L54.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Measure liquid medicine with the supplied measuring device (not a kitchen spoon).

**L55.0** `Incomplete Sentence` (0.851) → `excluded_incomplete`
- original: Allow the orally disintegrating tablet to dissolve in your mouth without chewing.

**L56.0** `Compound Sentence` (0.625) → `decomposed`
- original: Apply the skin patch to your hip area 2 hours before an effect is needed and remove it within 9 hours.
- pronoun resolved: Apply the skin patch to your hip area 2 hours before an effect is needed and remove patch within 9 hours.
  - edits: “it” → “patch”
  - S1: Apply the skin patch to your hip area 2 hours before an effect is needed.
  - S2: Remove the patch within 9 hours.

**L56.1** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Do not wear the patch longer than 9 hours a day.

**L56.2** `Incomplete Sentence` (0.913) → `excluded_incomplete`
- original: Avoid exposing the patch to direct external heat sources, such as hair dryers, heating pads, or electric blankets.

**L57.0** `Incomplete Sentence` (0.955) → `excluded_incomplete`
- original: Tell your doctor if you have a planned surgery.

**L58.0** `Simple Sentence` (0.968) → `passthrough`
- original: Your treatment may also include counseling or other treatments.

**L59.0** `Simple Sentence` (0.946) → `passthrough`
- original: Your doctor will need to check your progress on a regular basis.

**L59.1** `Simple Sentence` (0.945) → `passthrough`
- original: Your heart and blood pressure may also need to be checked often.

**L60.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Store tightly closed at room temperature, away from moisture, heat, and light.

**L60.1** `Incomplete Sentence` (0.916) → `excluded_incomplete`
- original: Keep your medicine in a place where no one can use it improperly.

**L61.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Do not keep leftover medicine.

**L61.1** `Incomplete Sentence` (0.973) → `excluded_incomplete`
- original: Ask your pharmacist about a drug take-back program.

**L61.2** `Compound Sentence` (0.562) → `decomposed`
- original: You may also mix the leftover medicine with cat litter or coffee grounds in a sealed plastic bag and throw the bag in the trash.
  - S1: You may also mix the leftover medicine with cat litter or coffee grounds in a sealed plastic bag.
  - S2: You may throw the bag in the trash.

## What happens if I miss a dose?

**L64.0** `Compound Sentence` (0.555) → `decomposed`
- original: Take the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - S1: Take the medicine as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L64.1** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

## What happens if I overdose?

**L67.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L67.1** `Simple Sentence` (0.985) → `passthrough`
- original: An overdose of methylphenidate could be fatal.

**L68.0** `Complex Sentence` (0.792) → `decomposed` · repaired
- original: Overdose symptoms may include nausea, dry mouth, vomiting, diarrhea, anxiety, agitation, restlessness, tremor, muscle twitches, rapid breathing, confusion, hallucinations, dilated pupils, muscle pain or weakness, fever, sweating, headache, pounding in your neck or ears, fast or pounding heartbeats, feeling light-headed, fainting, seizure (convulsions), or coma.
  - S1: Overdose symptoms may include nausea.
  - S2: Overdose symptoms may include dry mouth.
  - S3: Overdose symptoms may include vomiting.
  - S4: Overdose symptoms may include diarrhea.
  - S5: Overdose symptoms may include anxiety.
  - S6: Overdose symptoms may include agitation.
  - S7: Overdose symptoms may include restlessness.
  - S8: Overdose symptoms may include tremor.
  - S9: Overdose symptoms may include muscle twitches.
  - S10: Overdose symptoms may include rapid breathing.
  - S11: Overdose symptoms may include confusion.
  - S12: Overdose symptoms may include hallucinations.
  - S13: Overdose symptoms may include dilated pupils.
  - S14: Overdose symptoms may include muscle pain.
  - S15: Overdose symptoms may include muscle weakness.
  - S16: Overdose symptoms may include fever.
  - S17: Overdose symptoms may include sweating.
  - S18: Overdose symptoms may include headache.
  - S19: Overdose symptoms may include pounding in your neck or ears.
  - S20: Overdose symptoms may include fast or pounding heartbeats.
  - S21: Overdose symptoms may include feeling light-headed.
  - S22: Overdose symptoms may include fainting.
  - S23: Overdose symptoms may include seizure (convulsions).
  - S24: Overdose symptoms may include coma.

## What should I avoid while taking methylphenidate?

**L71.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Avoid drinking alcohol.

**L72.0** `Incomplete Sentence` (0.958) → `excluded_incomplete`
- original: Avoid driving or hazardous activity until you know how methylphenidate will affect you.

**L72.1** `Simple Sentence` (0.878) → `passthrough`
- original: Your reactions could be impaired.

## Methylphenidate side effects

**L75.0** `Compound Sentence` (0.442) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to methylphenidate: hives; difficulty breathing; swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to methylphenidate.
  - S2: Signs of an allergic reaction to methylphenidate include hives.
  - S3: Signs of an allergic reaction to methylphenidate include difficulty breathing.
  - S4: Signs of an allergic reaction to methylphenidate include swelling of your face, lips, tongue, or throat.

**L76.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L77.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: signs of heart problems - chest pain, trouble breathing, feeling like you might pass out;

**L78.0** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: signs of psychosis - hallucinations (seeing or hearing things that are not real), new behavior problems, aggression, hostility, paranoia;

**L79.0** `Incomplete Sentence` (0.93) → `excluded_incomplete`
- original: signs of circulation problems - numbness, pain, cold feeling, unexplained wounds, or skin color changes (pale, red, or blue appearance) in your fingers or toes; or

**L80.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: penis erection that is painful or lasts 4 hours or longer.

**L81.0** `Incomplete Sentence` (0.956) → `excluded_incomplete`
- original: signs of skin problems from the patch - swelling or blisters at the application site, or loss of skin color;

**L82.0** `Complex Sentence` (0.607) → `decomposed`
- original: Seek medical attention right away if you have symptoms of serotonin syndrome, such as: agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness, twitching, loss of coordination, nausea, vomiting, or diarrhea.
  - S1: Seek medical attention right away if you have symptoms of serotonin syndrome.
  - S2: Symptoms of serotonin syndrome include agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness, twitching, loss of coordination, nausea, vomiting, or diarrhea.

**L83.0** `Simple Sentence` (0.992) → `passthrough`
- original: Methylphenidate can affect growth in children.

**L83.1** `Simple Sentence` (0.98) → `passthrough`
- original: Your child's height and weight may need to be checked often.

**L83.2** `Incomplete Sentence` (0.911) → `excluded_incomplete`
- original: Tell your doctor if your child is not growing at a normal rate.

**L84.0** `Simple Sentence` (0.878) → `passthrough`
- original: Common methylphenidate side effects may include:

**L85.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: sweating, increased blood pressure;

**L86.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: mood changes, anxiety, feeling nervous or irritable, trouble sleeping;

**L87.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: fast heart rate, pounding heartbeats or fluttering in your chest;

**L88.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: loss of appetite, weight loss;

**L89.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: dry mouth, nausea, vomiting, stomach pain, indigestion; or

**L90.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: headache, dizziness.

**L91.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L91.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L91.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## What other drugs will affect methylphenidate?

**L94.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Tell your doctor about all your other medicines, especially:

**L95.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a blood thinner - warfarin, Coumadin, Jantoven;

**L96.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: blood pressure medication;

**L97.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: an antidepressant;

**L98.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: seizure medication; or

**L99.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: cold or allergy medications that contain decongestants.

**L100.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L100.1** `Complex Sentence` (0.651) → `decomposed`
- original: Other drugs may interact with methylphenidate, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may interact with methylphenidate.
  - S2: These include prescription and over-the-counter medicines.
  - S3: These also include vitamins and herbal products.

**L100.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.

## Popular FAQ

**L103.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Q: What is metilfenidato used for?

**L103.1** `Complex Sentence` (0.937) → `decomposed`
- original: A: Metilfenidato is the Spanish, Italian, and Portuguese translation for methylphenidate which may be used to treat children or adults with attention deficit hyperactivity disorder (ADHD) to help with hyperactivity and impulsive behavior, and allow them to concentrate better.
- pronoun resolved: A: Metilfenidato is the Spanish, Italian, and Portuguese translation for methylphenidate which may be used to treat children or adults with attention deficit hyperactivity disorder (ADHD) to help with hyperactivity and impulsive behavior, and allow children or adults to concentrate better.
  - edits: “them” → “children or adults”
  - S1: Metilfenidato is the Spanish, Italian, and Portuguese translation for methylphenidate.
  - S2: Methylphenidate may be used to treat children or adults with attention deficit hyperactivity disorder (ADHD).
  - S3: It is used to help with hyperactivity and impulsive behavior.
  - S4: It allows children or adults to concentrate better.

**L103.2** `Simple Sentence` (0.977) → `passthrough`
- original: Metilfenidato may also be used to treat adults with narcolepsy.

**L103.3** `Simple Sentence` (0.984) → `passthrough`
- original: Metilfenidato translates to methylphenidate.
