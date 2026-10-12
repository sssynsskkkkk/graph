# Hydrocodone and Acetaminophen — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/hydrocodone-acetaminophen.txt` · 115 sentences · 5 changed by pronoun resolution · 163 sentences sent to EDC

## What is hydrocodone + acetaminophen?

**L5.0** `Complex Sentence` (0.518) → `decomposed`
- original: Hydrocodone and acetaminophen is a strong prescription combination pain medicine containing an opioid, hydrocodone, in addition to acetaminophen, which is used to manage moderate to moderately severe pain, when other pain treatments such as non-opioid pain medicines do not treat your pain well enough, or you cannot tolerate them.
- pronoun resolved: Hydrocodone and acetaminophen is a strong prescription combination pain medicine containing an opioid, hydrocodone, in addition to acetaminophen, which is used to manage moderate to moderately severe pain, when other pain treatments such as non-opioid pain medicines do not treat your pain well enough, or you cannot tolerate non-opioid pain medicines.
  - edits: “them.” → “non-opioid pain medicines.”
  - S1: Hydrocodone and acetaminophen is a strong prescription combination pain medicine.
  - S2: The medicine contains an opioid, hydrocodone.
  - S3: The medicine also contains acetaminophen.
  - S4: Acetaminophen is used to manage moderate to moderately severe pain.
  - S5: The medicine is used when other pain treatments do not treat your pain well enough.
  - S6: The medicine is also used when you cannot tolerate non-opioid pain medicines.

**L6.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: An opioid pain medicine that can put you at risk for overdose and death.

**L6.1** `Complex Sentence` (0.947) → `decomposed`
- original: Even if you take your dose correctly as prescribed, you are at risk for opioid addiction, abuse, and misuse that can lead to death.
  - S1: You are at risk for opioid addiction, abuse, and misuse that can lead to death.
  - S2: This risk exists even if you take your dose correctly as prescribed.

**L6.2** `Simple Sentence` (0.986) → `passthrough`
- original: Hydrocodone and acetaminophen is a Schedule II controlled substance.

**L7.0** `Compound Sentence` (0.914) → `decomposed`
- original: All branded hydrocodone and acetaminophen (Norco, Vicodin, Lortab, Hycet, Lorcet, Verdrocet, Xodol, Zamicet) have been discontinued, but generic hydrocodone and acetaminophen tablets and oral solution is still available.
  - S1: All branded hydrocodone and acetaminophen (Norco, Vicodin, Lortab, Hycet, Lorcet, Verdrocet, Xodol, Zamicet) have been discontinued.
  - S2: Generic hydrocodone and acetaminophen tablets and oral solution is still available.

**L8.0** `Simple Sentence` (0.921) → `passthrough`
- original: Hydrocodone and acetaminophen first gained FDA approval on May 3, 1982.

## Important information about hydrocodone and acetaminophen

**L11.0** `Incomplete Sentence` (0.579) → `excluded_incomplete`
- original: Get emergency help right away if you take too many hydrocodone and acetaminophen tablets or oral solution (overdose).

**L11.1** `Complex Sentence` (0.711) → `decomposed`
- original: When you first start taking hydrocodone and acetaminophen, when your dose is changed, or if you take too much (overdose), serious or life-threatening breathing problems that can lead to death may occur.
  - S1: Serious or life-threatening breathing problems that can lead to death may occur.
  - S2: These problems may occur when you first start taking hydrocodone and acetaminophen.
  - S3: These problems may occur when your dose is changed.
  - S4: These problems may occur if you take too much (overdose).

**L12.0** `Incomplete Sentence` (0.736) → `excluded_incomplete`
- original: Never give anyone else your hydrocodone and acetaminophen.

**L12.1** `Simple Sentence` (0.99) → `passthrough`
- original: They could die from taking them.
- pronoun resolved: Hydrocodone and acetaminophen could die from taking hydrocodone and acetaminophen.
  - edits: “They” → “Hydrocodone and acetaminophen”; “them.” → “hydrocodone and acetaminophen.”

**L12.2** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: Store hydrocodone and acetaminophen away from children and in a safe place to prevent stealing or abuse.

**L12.3** `Simple Sentence` (0.983) → `passthrough`
- original: Selling or giving away hydrocodone and acetaminophen products is against the law.

## Side Effects

**L15.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Common Side Effects:

**L16.0** `Complex Sentence` (0.484) → `decomposed`
- original: The possible side effects of hydrocodone and acetaminophen are constipation, nausea, sleepiness, vomiting, tiredness, headache, dizziness, and abdominal pain.
  - S1: The possible side effects of hydrocodone and acetaminophen are constipation, nausea, sleepiness, vomiting, tiredness, headache, dizziness, and abdominal pain.

**L16.1** `Incomplete Sentence` (0.457) → `excluded_incomplete`
- original: Call your healthcare provider if you have any of these symptoms and they are severe.
- pronoun resolved: Call your healthcare provider if you have any of these symptoms and symptoms are severe.
  - edits: “they” → “symptoms”

**L17.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Get emergency medical help if you have:

**L18.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Trouble breathing

**L19.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Shortness of breath

**L20.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Fast heartbeat

**L21.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Chest pain

**L22.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Swelling of your face, tongue, or throat

**L23.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Extreme drowsiness

**L24.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Light-headedness when changing positions

**L25.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Feeling faint

**L26.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Agitation

**L27.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: High body temperature

**L28.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Trouble walking

**L29.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Stiff muscles

**L30.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Mental changes such as confusion.

**L31.0** `Simple Sentence` (0.97) → `passthrough`
- original: These are not all the possible side effects of hydrocodone and acetaminophen.

**L31.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L31.2** `Simple Sentence` (0.97) → `passthrough`
- original: You may report side effects to the FDA at 1-800-FDA-1088.

## Before Taking

**L34.0** `Incomplete Sentence` (0.967) → `excluded_incomplete`
- original: Do not take hydrocodone and acetaminophen if you have:

**L35.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Severe asthma, trouble breathing, or other lung problems

**L36.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: A bowel blockage or a narrowing of the stomach or intestines

**L37.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Signs of an allergy, such as a rash

**L38.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Are allergic to any of its ingredients.

**L39.0** `Simple Sentence` (0.541) → `passthrough`
- original: Before taking hydrocodone and acetaminophen, tell your healthcare provider if you have a history of:

**L40.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Head injury, seizures

**L41.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Liver, kidney, thyroid problems

**L42.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Problems urinating

**L43.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Pancreas or gallbladder problems

**L44.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Abuse of street or prescription drugs, alcohol addiction, or mental health problems.

**L45.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Tell your healthcare provider if you are:

**L46.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Pregnant or planning to become pregnant.

**L46.1** `Complex Sentence` (0.472) → `decomposed`
- original: Prolonged use of hydrocodone and acetaminophen during pregnancy can cause withdrawal symptoms in your newborn baby that could be life-threatening if not recognized and treated
  - S1: Prolonged use of hydrocodone and acetaminophen during pregnancy can cause withdrawal symptoms in your newborn baby.
  - S2: These symptoms could be life-threatening if not recognized and treated.

**L47.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Breastfeeding.

**L47.1** `Simple Sentence` (0.958) → `passthrough`
- original: Hydrocodone and acetaminophen pass into breast milk and may harm your baby.

**L47.2** `Incomplete Sentence` (0.966) → `excluded_incomplete`
- original: Carefully observe infants for increased sleepiness (more than usual), breathing difficulties, or limpness.

**L47.3** `Incomplete Sentence` (0.894) → `excluded_incomplete`
- original: Seek immediate medical care if you notice these signs.

**L48.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Taking prescription or over-the-counter medicines, vitamins, or herbal supplements.

**L48.1** `Simple Sentence` (0.881) → `passthrough`
- original: Taking hydrocodone and acetaminophen with certain other medicines can cause serious side effects that could lead to death.

## How Do I Take Hydrocodone and Acetaminophen

**L51.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: When taking hydrocodone and acetaminophen:

**L52.0** `Incomplete Sentence` (0.886) → `excluded_incomplete`
- original: Do not change your dose.

**L52.1** `Incomplete Sentence` (0.966) → `excluded_incomplete`
- original: Take hydrocodone and acetaminophen exactly as prescribed by your healthcare provider.

**L53.0** `Incomplete Sentence` (0.806) → `excluded_incomplete`
- original: Take your prescribed dose every four to six hours at the same time every day.

**L53.1** `Incomplete Sentence` (0.863) → `excluded_incomplete`
- original: Do not take more than your prescribed dose.

**L53.2** `Simple Sentence` (0.716) → `passthrough`
- original: If you miss a dose, take your next dose at your usual time.

**L54.0** `Complex Sentence` (0.578) → `decomposed`
- original: If taking the oral solution, always use a graduated oral syringe or measuring cup to correctly measure your dose.
  - S1: If taking the oral solution, always use a graduated oral syringe or measuring cup.
  - S2: This is done to correctly measure your dose.

**L54.1** `Incomplete Sentence` (0.744) → `excluded_incomplete`
- original: Never use a household teaspoon or tablespoon to measure your medicine.

**L55.0** `Compound Sentence` (0.366) → `decomposed`
- original: Call your healthcare provider if the dose you are taking does not control your pain, if your pain gets worse, if you feel more sensitive to pain, or if you have new pain.
  - S1: Call your healthcare provider if the dose you are taking does not control your pain.
  - S2: Call your healthcare provider if your pain gets worse.
  - S3: Call your healthcare provider if you feel more sensitive to pain.
  - S4: Call your healthcare provider if you have new pain.

**L55.1** `Simple Sentence` (0.602) → `passthrough`
- original: Do not take more medicine without first talking to your healthcare provider.

**L56.0** `Complex Sentence` (0.561) → `decomposed`
- original: If you have been taking hydrocodone and acetaminophen regularly, do not stop taking it without talking to your healthcare provider.
- pronoun resolved: If you have been taking hydrocodone and acetaminophen regularly, do not stop taking hydrocodone without talking to your healthcare provider.
  - edits: “it” → “hydrocodone”
  - S1: If you have been taking hydrocodone and acetaminophen regularly.
  - S2: Do not stop taking hydrocodone without talking to your healthcare provider.

**L57.0** `Simple Sentence` (0.792) → `passthrough`
- original: After you stop taking hydrocodone and acetaminophen, flush any unused tablets or oral solution down the toilet.

## What Should I Avoid While Taking Hydrocodone and Acetaminophen

**L60.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: While taking hydrocodone and acetaminophen, DO NOT:

**L61.0** `Incomplete Sentence` (0.972) → `excluded_incomplete`
- original: Drive or operate heavy machinery until you know how hydrocodone and acetaminophen affects you.

**L61.1** `Simple Sentence` (0.97) → `passthrough`
- original: Hydrocodone and acetaminophen can make you sleepy, dizzy, or lightheaded.

**L62.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Drink alcohol or use prescription or over-the-counter medicines that contain alcohol.

**L62.1** `Simple Sentence` (0.975) → `passthrough`
- original: Using products containing alcohol during treatment with hydrocodone and acetaminophen may cause you to overdose and die.

## Dosing Information

**L65.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Adult Dose of Hydrocodone And Acetaminophen for Moderate to Severe Pain:

**L66.0** `Incomplete Sentence` (0.695) → `excluded_incomplete`
- original: Hydrocodone 2.5 mg-acetaminophen 325 mg per tablet, Hydrocodone 5 mg-acetaminophen 325 mg per tablet:

**L67.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Initial dose: 1 to 2 tablets every 4 to 6 hours as needed for pain

**L68.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Maximum dose: 8 tablets/24 hours

**L69.0** `Incomplete Sentence` (0.671) → `excluded_incomplete`
- original: Hydrocodone 7.5 mg-acetaminophen 325 mg, Hydrocodone 10 mg-acetaminophen 325 mg per tablet:

**L70.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Initial dose: 1 tablet every 4 to 6 hours as needed for pain

**L71.0** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: Maximum dose: 6 tablets/24 hours

**L72.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Hydrocodone 7.5 mg-acetaminophen 325 mg per 15 mL oral solution:

**L73.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Initial dose: 15 mL every 4 to 6 hours as needed for pain

**L74.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Maximum dose: 90 mL/24 hours

**L75.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Hydrocodone 10 mg-acetaminophen 300 mg per 15 mL oral solution:

**L76.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Initial dose: 11.25 mL every 4 to 6 hours as needed for pain

**L77.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Maximum dose: 67.5 mL/24 hours

**L78.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Comments:

**L79.0** `Complex Sentence` (0.371) → `decomposed`
- original: Doses should be individually titrated to provide adequate analgesia while minimizing adverse reactions.
  - S1: Doses should be individually titrated.
  - S2: The titration should provide adequate analgesia.
  - S3: The titration should minimize adverse reactions.

**L80.0** `Complex Sentence` (0.956) → `decomposed`
- original: Because of the risks of addiction, abuse, and misuse, the lowest effective dose for the shortest duration consistent with individual patient treatment goals should be used.
  - S1: The lowest effective dose should be used.
  - S2: The dose should be used for the shortest duration.
  - S3: The duration should be consistent with individual patient treatment goals.
  - S4: This is because of the risks of addiction, abuse, and misuse.

**L81.0** `Incomplete Sentence` (0.92) → `excluded_incomplete`
- original: Monitor patients closely for respiratory depression within the first 24 to 72 hours of initiating therapy and following any increase in dose.

## What happens if I overdose?

**L84.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L84.1** `Simple Sentence` (0.985) → `passthrough`
- original: An overdose of acetaminophen and hydrocodone can be fatal.

**L85.0** `Complex Sentence` (0.814) → `decomposed`
- original: Acute overdosage with hydrocodone and acetaminophen can cause respiratory depression, sleepiness progressing to near-unconsciousness or coma, floppy muscles, cold and clammy skin, constricted pupils, and, in some cases, pulmonary edema, slow heartbeat, low blood pressure, partial or complete airway obstruction, unusual snoring, and death.
  - S1: Acute overdosage with hydrocodone and acetaminophen can cause respiratory depression.
  - S2: It can cause sleepiness progressing to near-unconsciousness or coma.
  - S3: It can cause floppy muscles.
  - S4: It can cause cold and clammy skin.
  - S5: It can cause constricted pupils.
  - S6: It can cause pulmonary edema in some cases.
  - S7: It can cause a slow heartbeat.
  - S8: It can cause low blood pressure.
  - S9: It can cause partial or complete airway obstruction.
  - S10: It can cause unusual snoring.
  - S11: It can cause death.

**L85.1** `Complex Sentence` (0.892) → `decomposed`
- original: If the patient who has overdosed becomes very low in oxygen, pupils may become very dilated instead of constricted.
  - S1: If the patient who has overdosed becomes very low in oxygen.
  - S2: Pupils may become very dilated instead of constricted.

**L86.0** `Complex Sentence` (0.475) → `decomposed`
- original: Your doctor may recommend that you get naloxone (a medicine to reverse an opioid overdose) and keep it with you at all times.
- pronoun resolved: Your doctor may recommend that you get naloxone (a medicine to reverse an opioid overdose) and keep naloxone with you at all times.
  - edits: “it” → “naloxone”
  - S1: Your doctor may recommend that you get naloxone.
  - S2: Naloxone is a medicine to reverse an opioid overdose.
  - S3: Your doctor may recommend that you keep naloxone with you at all times.

**L86.1** `Simple Sentence` (0.867) → `passthrough`
- original: A person caring for you can give the naloxone if you stop breathing or don't wake up.

**L86.2** `Compound Sentence` (0.816) → `decomposed`
- original: Your caregiver must still get emergency medical help and may need to perform CPR (cardiopulmonary resuscitation) on you while waiting for help to arrive.
  - S1: Your caregiver must still get emergency medical help.
  - S2: Your caregiver may need to perform CPR (cardiopulmonary resuscitation) on you while waiting for help to arrive.

**L87.0** `Simple Sentence` (0.977) → `passthrough`
- original: Anyone can buy naloxone from a pharmacy or local health department.

**L87.1** `Incomplete Sentence` (0.901) → `excluded_incomplete`
- original: Make sure any person caring for you knows where you keep naloxone and how to use it.

**L88.0** `Complex Sentence` (0.454) → `decomposed`
- original: The first signs of an acetaminophen overdose include loss of appetite, nausea, vomiting, stomach pain, sweating, and confusion or weakness.
  - S1: The first signs of an acetaminophen overdose include loss of appetite.
  - S2: The first signs of an acetaminophen overdose include nausea.
  - S3: The first signs of an acetaminophen overdose include vomiting.
  - S4: The first signs of an acetaminophen overdose include stomach pain.
  - S5: The first signs of an acetaminophen overdose include sweating.
  - S6: The first signs of an acetaminophen overdose include confusion or weakness.

**L88.1** `Compound Sentence` (0.527) → `decomposed`
- original: Later symptoms may include pain in your upper stomach, dark urine, and yellowing of your skin or the whites of your eyes.
  - S1: Later symptoms may include pain in your upper stomach.
  - S2: Later symptoms may include dark urine.
  - S3: Later symptoms may include yellowing of your skin or the whites of your eyes.

## What other drugs will affect hydrocodone and acetaminophen?

**L91.0** `Simple Sentence` (0.924) → `passthrough`
- original: You may have breathing problems or withdrawal symptoms if you start or stop taking certain other medicines.

**L91.1** `Incomplete Sentence` (0.532) → `excluded_incomplete`
- original: Tell your doctor if you also use an antibiotic, antifungal medication, heart or blood pressure medication, seizure medication, or medicine to treat HIV or hepatitis C.

**L92.0** `Simple Sentence` (0.924) → `passthrough`
- original: Opioid medication can interact with many other drugs and cause dangerous side effects or death.

**L92.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Be sure your doctor knows if you also use:

**L93.0** `Incomplete Sentence` (0.971) → `excluded_incomplete`
- original: cold or allergy medicines, bronchodilator asthma/ COPD medication, or a diuretic ("water pill");

**L94.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: medicines for motion sickness, irritable bowel syndrome, or overactive bladder;

**L95.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: other opioids - opioid pain medicine or prescription cough medicine;

**L96.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: a sedative like Valium - diazepam, alprazolam, lorazepam, Xanax, Klonopin, Versed, and others;

**L97.0** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: drugs that make you sleepy or slow your breathing - a sleeping pill, muscle relaxer, medicine to treat mood disorders or mental illness;

**L98.0** `Incomplete Sentence` (0.938) → `excluded_incomplete`
- original: drugs that affect serotonin levels in your body - a stimulant, or medicine for depression, Parkinson's disease, migraine headaches, serious infections, or nausea and vomiting.

**L99.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L99.1** `Complex Sentence` (0.856) → `decomposed`
- original: Other drugs may interact with acetaminophen and hydrocodone, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may interact with acetaminophen and hydrocodone.
  - S2: These drugs include prescription and over-the-counter medicines.
  - S3: These drugs also include vitamins and herbal products.

**L99.2** `Simple Sentence` (0.949) → `passthrough`
- original: Not all possible interactions are listed here.

**L99.3** `Simple Sentence` (0.803) → `passthrough`
- original: To check for interactions with hydrocodone and acetaminophen, click the link below.

**L100.0** `Compound Sentence` (0.674) → `decomposed`
- original: Remember, keep this and all other medicines out of the reach of children, never share your medicines with others, and use acetaminophen or hydrocodone only for the indication prescribed.
  - S1: Remember to keep this and all other medicines out of the reach of children.
  - S2: Never share your medicines with others.
  - S3: Use acetaminophen or hydrocodone only for the indication prescribed.

## Popular FAQ

**L103.0** `Incomplete Sentence` (0.626) → `excluded_incomplete`
- original: Q: What is the difference between Apadaz and Vicodin?

**L103.1** `Compound Sentence` (0.938) → `decomposed`
- original: A: Vicodin contains a combination of acetaminophen and the opioid hydrocodone, whereas Apadaz is a combination of the prodrug, benzhydrocodone and acetaminophen.
  - S1: Vicodin contains a combination of acetaminophen and the opioid hydrocodone.
  - S2: Apadaz is a combination of the prodrug, benzhydrocodone and acetaminophen.

**L103.2** `Compound Sentence` (0.41) → `decomposed`
- original: When ingested, stomach enzymes cleave the benzhydrocodone prodrug and release the active parent drug hydrocodone.
  - S1: When ingested, stomach enzymes cleave the benzhydrocodone prodrug.
  - S2: This process releases the active parent drug hydrocodone.
