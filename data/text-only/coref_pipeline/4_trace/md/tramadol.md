# Tramadol — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/tramadol.txt` · 258 sentences · 31 changed by pronoun resolution · 432 sentences sent to EDC

## What is tramadol?

**L5.0** `Complex Sentence` (0.878) → `decomposed`
- original: Tramadol is an opioid agonist that may be used to treat moderate to moderately severe chronic pain in adults, when other pain treatments such as non-opioid pain medicines do not treat your pain well enough, or you cannot tolerate them.
  - S1: Tramadol is an opioid agonist.
  - S2: Tramadol may be used to treat moderate to moderately severe chronic pain in adults.
  - S3: It is used when other pain treatments such as non-opioid pain medicines do not treat your pain well enough.
  - S4: It is also used when you cannot tolerate other pain treatments.

**L6.0** `Simple Sentence` (0.941) → `passthrough`
- original: Extended-release forms of tramadol may be used in adults who require around-the-clock treatment of their pain for an extended period.

**L7.0** `Simple Sentence` (0.982) → `passthrough`
- original: An opioid pain medicine such as tramadol can put you at risk for overdose and death.

**L7.1** `Complex Sentence` (0.947) → `decomposed`
- original: Even if you take your dose correctly as prescribed, you are at risk for opioid addiction, abuse, and misuse that can lead to death.
  - S1: You are at risk for opioid addiction, abuse, and misuse that can lead to death.
  - S2: This risk exists even if you take your dose correctly as prescribed.

**L8.0** `Simple Sentence` (0.703) → `passthrough`
- original: Brands of tramadol include ConZip, Qdolo, Ryzolt, Ultram, Ultram ER, and Ultracet.

**L8.1** `Compound Sentence` (0.745) → `decomposed`
- original: Many have been discontinued, but generic tramadol is still available.
  - S1: Many have been discontinued.
  - S2: Generic tramadol is still available.

**L9.0** `Complex Sentence` (0.881) → `decomposed`
- original: Taking tramadol in combination with other pain-relieving medicines such as acetaminophen, ibuprofen, or aspirin can provide better pain relief than just taking one pain-relieving medicine by itself (see Can you take tramadol in combination with acetaminophen, ibuprofen, or aspirin?)
  - S1: Taking tramadol in combination with other pain-relieving medicines can provide better pain relief.
  - S2: The other pain-relieving medicines include acetaminophen, ibuprofen, or aspirin.
  - S3: Taking just one pain-relieving medicine by itself provides less relief.
  - S4: See Can you take tramadol in combination with acetaminophen, ibuprofen, or aspirin?

**L10.0** `Simple Sentence` (0.96) → `passthrough`
- original: Tramadol first gained FDA approval on March 3, 1995.

**L10.1** `Compound Sentence` (0.803) → `decomposed`
- original: Originally, it was classified as a non-controlled substance, but it was reclassified in 2014 to Schedule IV of the Controlled Substances Act with restrictions on its prescribing.
- pronoun resolved: Originally, tramadol was classified as a non-controlled substance, but tramadol was reclassified in 2014 to Schedule IV of the Controlled Substances Act with restrictions on tramadol's prescribing.
  - edits: “it” → “tramadol”; “it” → “tramadol”; “its” → “tramadol's”
  - S1: Originally, tramadol was classified as a non-controlled substance.
  - S2: Tramadol was reclassified in 2014 to Schedule IV of the Controlled Substances Act with restrictions on tramadol's prescribing.

**L10.2** `Simple Sentence` (0.688) → `passthrough`
- original: Tramadol is an opioid (see Is tramadol an opioid?

**L10.3** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: ).

**L11.0** `Simple Sentence` (0.788) → `passthrough`
- original: A person's genetics can affect the pain-relieving properties of tramadol (see How do genetics affect tramadol?

**L11.1** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: ).

## Tramadol uses

**L14.0** `Complex Sentence` (0.569) → `decomposed`
- original: Tramadol is used for the management of moderate to moderately severe pain in adults, including postoperative pain (pain after surgery).
  - S1: Tramadol is used for the management of moderate to moderately severe pain in adults.
  - S2: This includes postoperative pain.
  - S3: Postoperative pain is pain after surgery.

**L15.0** `Compound Sentence` (0.893) → `decomposed`
- original: Tramadol treats pain severe enough to require opioids and may be used as an alternative to other forms of pain relief that did not relieve pain well enough or were not tolerated.
  - S1: Tramadol treats pain severe enough to require opioids.
  - S2: It may be used as an alternative to other forms of pain relief.
  - S3: Those other forms did not relieve pain well enough or were not tolerated.

**L16.0** `Complex Sentence` (0.64) → `decomposed`
- original: Tramadol extended-release capsules may be used by adults who require around-the-clock treatment of their moderate to moderately severe chronic pain for an extended time.
  - S1: Tramadol extended-release capsules may be used by adults.
  - S2: The adults require around-the-clock treatment of their moderate to moderately severe chronic pain.
  - S3: The treatment is for an extended time.

**L17.0** `Compound Sentence` (0.462) → `decomposed`
- original: Tramadol should not be used in children younger than 12 years old, or anyone younger than 18 years old with other risk factors (such as breathing problems), or who have recently had surgery to remove their tonsils or adenoids.
  - S1: Tramadol should not be used in children younger than 12 years old.
  - S2: It should not be used in anyone younger than 18 years old with other risk factors, such as breathing problems.
  - S3: It should not be used in anyone who has recently had surgery to remove their tonsils or adenoids.

**L18.0** `Simple Sentence` (0.948) → `passthrough`
- original: Extended-release tramadol (Ultram ER) should not be given to anyone younger than 18 years.

## Is Tramadol an opioid?

**L21.0** `Simple Sentence` (0.973) → `passthrough`
- original: Yes, tramadol is an opioid.

**L21.1** `Simple Sentence` (0.376) → `passthrough`
- original: The opioid activity of tramadol is due to its binding to mu-opioid receptors.
- pronoun resolved: The opioid activity of tramadol is due to tramadol's binding to mu-opioid receptors.
  - edits: “its” → “tramadol's”

## Important Information About Tramadol

**L24.0** `Incomplete Sentence` (0.735) → `excluded_incomplete`
- original: Get emergency help or call 911 right away if you take too many tramadol (overdose).

**L24.1** `Complex Sentence` (0.888) → `decomposed`
- original: When you first start taking tramadol, when your dose is changed, or if you take too much (overdose), serious or life-threatening breathing problems that can lead to death may occur.
  - S1: Serious or life-threatening breathing problems that can lead to death may occur.
  - S2: These problems may occur when you first start taking tramadol.
  - S3: These problems may occur when your dose is changed.
  - S4: These problems may occur if you take too much (overdose).

**L24.2** `Incomplete Sentence` (0.784) → `excluded_incomplete`
- original: Ask your healthcare provider about medicines like naloxone or nalmefene that can be used in an emergency to reverse an opioid overdose.

**L25.0** `Complex Sentence` (0.639) → `decomposed`
- original: Taking tramadol with other opioid medicines, benzodiazepines, gabapentinoids (gabapentin or pregabalin), alcohol, or other central nervous system depressants (including street drugs) can cause severe drowsiness, decreased awareness, breathing problems, coma, and death.
  - S1: Taking tramadol with other opioid medicines, benzodiazepines, gabapentinoids, alcohol, or other central nervous system depressants can cause severe drowsiness, decreased awareness, breathing problems, coma, and death.
  - S2: Other central nervous system depressants include street drugs.
  - S3: Gabapentinoids include gabapentin or pregabalin.

**L26.0** `Incomplete Sentence` (0.781) → `excluded_incomplete`
- original: Do not take tramadol with any other medicine that contains tramadol.

**L26.1** `Simple Sentence` (0.428) → `passthrough`
- original: Check the label of every pain medicine you take, as some combination products contain tramadol.

**L27.0** `Simple Sentence` (0.978) → `passthrough`
- original: You should be given a Medication Guide each time you fill a tramadol prescription.

**L27.1** `Incomplete Sentence` (0.958) → `excluded_incomplete`
- original: Read it every time, even if you have taken tramadol before, because the information may have changed.
- pronoun resolved: Read tramadol every time, even if you have taken tramadol before, because the information may have changed.
  - edits: “it” → “tramadol”

**L27.2** `Compound Sentence` (0.535) → `decomposed`
- original: Your healthcare provider or pharmacist should also go through the risks of tramadol and how to take it safely with you, and explain what to do in an emergency.
- pronoun resolved: Your healthcare provider or pharmacist should also go through the risks of tramadol and how to take tramadol safely with you, and explain what to do in an emergency.
  - edits: “it” → “tramadol”
  - S1: Your healthcare provider or pharmacist should also go through the risks of tramadol and how to take tramadol safely with you.
  - S2: They should also explain what to do in an emergency.

**L28.0** `Incomplete Sentence` (0.938) → `excluded_incomplete`
- original: Never give anyone else your tramadol.

**L28.1** `Simple Sentence` (0.955) → `passthrough`
- original: They could die from taking it.
- pronoun resolved: Anyone else could die from taking tramadol.
  - edits: “They” → “Anyone else”; “it.” → “tramadol.”

**L28.2** `Simple Sentence` (0.979) → `passthrough`
- original: Selling or giving away tramadol is against the law.

**L29.0** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Store tramadol securely, out of sight and reach of children, and in a location not accessible by others, including visitors to the home.

## Tramadol side effects

**L32.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Common side effects:

**L33.0** `Simple Sentence` (0.976) → `passthrough`
- original: The most common side effects of tramadol are:

**L34.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: dizziness or vertigo

**L35.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: nausea

**L36.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: constipation

**L37.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: headache

**L38.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: drowsiness

**L39.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: vomiting

**L40.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: itching.

**L41.0** `Simple Sentence` (0.969) → `passthrough`
- original: Dry mouth is also commonly reported with the extended-release forms of tramadol.

**L42.0** `Simple Sentence` (0.692) → `passthrough`
- original: A person's genetics can affect their response to tramadol, including their risk of side effects (see How do genetics affect tramadol?

**L42.1** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: ).

**L43.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious tramadol side effects and warnings:

**L44.0** `Simple Sentence` (0.958) → `passthrough`
- original: Tramadol may cause serious side effects, some of which may be fatal.

**L45.0** `Simple Sentence` (0.784) → `passthrough`
- original: Tramadol can slow or stop your breathing and may be habit-forming.

**L45.1** `Complex Sentence` (0.523) → `decomposed`
- original: MISUSE OF THIS MEDICINE CAN CAUSE ADDICTION, OVERDOSE, OR DEATH, especially in a child or other person using the medicine without a prescription.
  - S1: Misuse of this medicine can cause addiction, overdose, or death.
  - S2: This risk is especially high in a child.
  - S3: This risk is especially high in other people using the medicine without a prescription.

**L45.2** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: Keep this medicine where others cannot get to it.

**L45.3** `Incomplete Sentence` (0.429) → `excluded_incomplete`
- original: Do not take more tramadol than prescribed, as an overdose can be fatal.

**L45.4** `Simple Sentence` (0.979) → `passthrough`
- original: Selling or giving away this medicine is against the law.
- pronoun resolved: Selling or giving away tramadol is against the law.
  - edits: “this medicine” → “tramadol”

**L46.0** `Complex Sentence` (0.468) → `decomposed`
- original: A person caring for you should give naloxone and seek emergency medical attention if you have slow breathing with long pauses, blue-colored lips, or if you find it hard to wake up.
  - S1: A person caring for you should give naloxone.
  - S2: A person caring for you should seek emergency medical attention.
  - S3: You should receive these actions if you have slow breathing with long pauses.
  - S4: You should receive these actions if you have blue-colored lips.
  - S5: You should receive these actions if you find it hard to wake up.

**L46.1** `Complex Sentence` (0.591) → `decomposed`
- original: Serious breathing problems may be more likely in older adults and people who are debilitated or have wasting syndrome or chronic breathing disorders.
  - S1: Serious breathing problems may be more likely in older adults.
  - S2: Serious breathing problems may be more likely in people who are debilitated.
  - S3: Serious breathing problems may be more likely in people who have wasting syndrome.
  - S4: Serious breathing problems may be more likely in people who have chronic breathing disorders.

**L47.0** `Complex Sentence` (0.38) → `decomposed` · repaired
- original: Call your doctor at once if you have: noisy breathing, sighing, shallow breathing, breathing that stops during sleep a slow heart rate or weak pulse a light-headed feeling, like you might pass out seizure (convulsions) or low cortisol levels (symptoms include nausea, vomiting, loss of appetite, dizziness, worsening tiredness or weakness) low sodium levels (hyponatremia).
  - S1: Call your doctor at once if you have noisy breathing.
  - S2: Call your doctor at once if you have sighing.
  - S3: Call your doctor at once if you have shallow breathing.
  - S4: Call your doctor at once if you have breathing that stops during sleep.
  - S5: Call your doctor at once if you have a slow heart rate.
  - S6: Call your doctor at once if you have a weak pulse.
  - S7: Call your doctor at once if you have a light-headed feeling.
  - S8: Call your doctor at once if you have a light-headed feeling like you might pass out.
  - S9: Call your doctor at once if you have a seizure.
  - S10: Call your doctor at once if you have convulsions.
  - S11: Call your doctor at once if you have low cortisol levels.
  - S12: Low cortisol levels include symptoms such as nausea.
  - S13: Low cortisol levels include symptoms such as vomiting.
  - S14: Low cortisol levels include symptoms such as loss of appetite.
  - S15: Low cortisol levels include symptoms such as dizziness.
  - S16: Low cortisol levels include symptoms such as worsening tiredness.
  - S17: Low cortisol levels include symptoms such as weakness.
  - S18: Call your doctor at once if you have low sodium levels.
  - S19: Low sodium levels are also known as hyponatremia.

**L47.1** `Simple Sentence` (0.802) → `passthrough`
- original: Symptoms include headache, confusion, weakness, unsteadiness, or feeling sick low blood sugar (hypoglycemia).

**L47.2** `Simple Sentence` (0.967) → `passthrough`
- original: Symptoms include shakiness, sweating, hunger, confusion, or a fast heartbeat.

**L48.0** `Complex Sentence` (0.519) → `decomposed`
- original: Seek medical attention right away if you have symptoms of serotonin syndrome, such as agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness, twitching, loss of coordination, nausea, vomiting, or diarrhea.
  - S1: Seek medical attention right away if you have symptoms of serotonin syndrome.
  - S2: Symptoms of serotonin syndrome include agitation, hallucinations, fever, sweating, shivering, fast heart rate, muscle stiffness, twitching, loss of coordination, nausea, vomiting, or diarrhea.

**L49.0** `Simple Sentence` (0.991) → `passthrough`
- original: Seizures have been reported in patients taking tramadol.

**L49.1** `Simple Sentence` (0.979) → `passthrough`
- original: Your risk of seizures is higher if you are taking higher doses than recommended.

**L49.2** `Compound Sentence` (0.781) → `decomposed`
- original: Seizure risk is also higher in those with epilepsy or a history of seizures, and in those taking certain antidepressants, other opioids, MAO inhibitors, or other medicines that lower the seizure threshold.
  - S1: Seizure risk is also higher in those with epilepsy or a history of seizures.
  - S2: Seizure risk is also higher in those taking certain antidepressants, other opioids, MAO inhibitors, or other medicines that lower the seizure threshold.

**L50.0** `Compound-Complex Sentence` (0.612) → `decomposed`
- original: You should not take tramadol if you have significant breathing problems, acute or severe asthma in a setting where you cannot be monitored, a blockage in your stomach or intestines, or if you have taken an MAO inhibitor in the past 14 days (isocarboxazid, linezolid, methylene blue injection, phenelzine, tranylcypromine, and others).
  - S1: You should not take tramadol if you have significant breathing problems.
  - S2: You should not take tramadol if you have acute or severe asthma in a setting where you cannot be monitored.
  - S3: You should not take tramadol if you have a blockage in your stomach or intestines.
  - S4: You should not take tramadol if you have taken an MAO inhibitor in the past 14 days.
  - S5: Examples of MAO inhibitors include isocarboxazid, linezolid, methylene blue injection, phenelzine, and tranylcypromine.

**L50.1** `Complex Sentence` (0.363) → `decomposed`
- original: Tell your doctor before starting tramadol if you have a head injury or increased pressure inside your skull, as tramadol should be used with particular care in these situations.
  - S1: Tell your doctor before starting tramadol if you have a head injury or increased pressure inside your skull.
  - S2: Tramadol should be used with particular care in these situations.

**L51.0** `Compound Sentence` (0.912) → `decomposed`
- original: Prescribers are advised not to prescribe tramadol for people who are suicidal or prone to addiction, and to use it with caution in people taking tranquilizers or antidepressants, or drinking heavily.
- pronoun resolved: Prescribers are advised not to prescribe tramadol for people who are suicidal or prone to addiction, and to use tramadol with caution in people taking tranquilizers or antidepressants, or drinking heavily.
  - edits: “it” → “tramadol”
  - S1: Prescribers are advised not to prescribe tramadol for people who are suicidal or prone to addiction.
  - S2: Prescribers are advised to use tramadol with caution in people taking tranquilizers or antidepressants.
  - S3: Prescribers are advised to use tramadol with caution in people drinking heavily.

**L51.1** `Complex Sentence` (0.754) → `decomposed`
- original: If you are struggling with thoughts of harming yourself, or with your use of any medicine, tell your healthcare provider so they can help you find the right treatment and support.
- pronoun resolved: If you are struggling with thoughts of harming yourself, or with your use of any medicine, tell your healthcare provider so healthcare provider can help you find the right treatment and support.
  - edits: “they” → “healthcare provider”
  - S1: If you are struggling with thoughts of harming yourself, or with your use of any medicine, tell your healthcare provider.
  - S2: The healthcare provider can help you find the right treatment and support.

**L52.0** `Compound Sentence` (0.537) → `decomposed`
- original: Fatal side effects can occur if you use this medicine with alcohol, or with other drugs that cause drowsiness or slow your breathing.
- pronoun resolved: Fatal side effects can occur if you use tramadol with alcohol, or with other drugs that cause drowsiness or slow your breathing.
  - edits: “this medicine” → “tramadol”
  - S1: Fatal side effects can occur if you use tramadol with alcohol.
  - S2: Fatal side effects can occur if you use tramadol with other drugs that cause drowsiness or slow your breathing.

**L52.1** `Simple Sentence` (0.85) → `passthrough`
- original: People taking extended-release forms of tramadol should not consume alcohol-containing beverages at the same time.

**L52.2** `Simple Sentence` (0.974) → `passthrough`
- original: Alcohol is also not advised with immediate-release forms of tramadol.

**L53.0** `Complex Sentence` (0.437) → `decomposed`
- original: Serious allergic reactions, including anaphylaxis, have occurred with tramadol, some of which caused death.
  - S1: Serious allergic reactions have occurred with tramadol.
  - S2: Some of these reactions included anaphylaxis.
  - S3: Some of these reactions caused death.

**L53.1** `Simple Sentence` (0.982) → `passthrough`
- original: People who are allergic to other opioids are at higher risk.

**L53.2** `Compound Sentence` (0.857) → `decomposed`
- original: Other hypersensitivity reactions include itching, hives, narrowing of the airways, swelling of the face and airways (angioedema), and serious skin reactions such as Stevens-Johnson Syndrome.
  - S1: Other hypersensitivity reactions include itching.
  - S2: They include hives.
  - S3: They include narrowing of the airways.
  - S4: They include swelling of the face and airways (angioedema).
  - S5: They include serious skin reactions such as Stevens-Johnson Syndrome.

**L53.3** `Compound-Complex Sentence` (0.34) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to tramadol (symptoms include hives, difficulty breathing, swelling in your face or throat) or a severe skin reaction (fever, sore throat, burning in your eyes, skin pain, a red or purple skin rash that spreads and causes blistering and peeling).
  - S1: Get emergency medical help if you have signs of an allergic reaction to tramadol.
  - S2: Symptoms of an allergic reaction to tramadol include hives.
  - S3: Symptoms of an allergic reaction to tramadol include difficulty breathing.
  - S4: Symptoms of an allergic reaction to tramadol include swelling in your face.
  - S5: Symptoms of an allergic reaction to tramadol include swelling in your throat.
  - S6: Get emergency medical help if you have a severe skin reaction.
  - S7: Symptoms of a severe skin reaction include fever.
  - S8: Symptoms of a severe skin reaction include a sore throat.
  - S9: Symptoms of a severe skin reaction include burning in your eyes.
  - S10: Symptoms of a severe skin reaction include skin pain.
  - S11: Symptoms of a severe skin reaction include a red or purple skin rash that spreads.
  - S12: Symptoms of a severe skin reaction include blistering.
  - S13: Symptoms of a severe skin reaction include peeling.

**L54.0** `Complex Sentence` (0.624) → `decomposed`
- original: Tramadol may make pain worse rather than better in some people, an effect called opioid-induced hyperalgesia.
  - S1: Tramadol may make pain worse rather than better in some people.
  - S2: This effect is called opioid-induced hyperalgesia.

**L54.1** `Compound Sentence` (0.381) → `decomposed`
- original: Talk to your doctor if the pain you have increases, if you feel more sensitive to pain, or if you have new pain after taking tramadol.
  - S1: Talk to your doctor if the pain you have increases.
  - S2: Talk to your doctor if you feel more sensitive to pain.
  - S3: Talk to your doctor if you have new pain after taking tramadol.

**L55.0** `Simple Sentence` (0.643) → `passthrough`
- original: Tramadol extended-release capsules and tablets may complicate a healthcare provider’s clinical assessment of an acute abdominal condition.

**L55.1** `Simple Sentence` (0.961) → `passthrough`
- original: They are not recommended for people with severe liver or severe kidney impairment.

**L56.0** `Complex Sentence` (0.827) → `decomposed`
- original: Taking tramadol during pregnancy may cause life-threatening withdrawal symptoms in the newborn, known as neonatal opioid withdrawal syndrome (NOWS).
  - S1: Taking tramadol during pregnancy may cause life-threatening withdrawal symptoms in the newborn.
  - S2: These symptoms are known as neonatal opioid withdrawal syndrome (NOWS).

**L57.0** `Complex Sentence` (0.472) → `decomposed`
- original: Some people are “ultra-rapid metabolizers” of tramadol because of a variation in an enzyme called CYP2D6.
  - S1: Some people are "ultra-rapid metabolizers" of tramadol.
  - S2: This is because of a variation in an enzyme.
  - S3: The enzyme is called CYP2D6.

**L57.1** `Complex Sentence` (0.932) → `decomposed`
- original: Their bodies convert tramadol into its active form faster than usual, which can produce dangerously high opioid levels even at a normal dose.
- pronoun resolved: People's bodies convert tramadol into tramadol's active form faster than usual, which can produce dangerously high opioid levels even at a normal dose.
  - edits: “Their” → “People's”; “its” → “tramadol's”
  - S1: People's bodies convert tramadol into tramadol's active form faster than usual.
  - S2: This can produce dangerously high opioid levels.
  - S3: This can occur even at a normal dose.

**L57.2** `Complex Sentence` (0.638) → `decomposed`
- original: Life-threatening breathing problems and deaths have occurred in children for this reason, including after surgery to remove the tonsils or adenoids.
  - S1: Life-threatening breathing problems and deaths have occurred in children for this reason.
  - S2: This has happened including after surgery to remove the tonsils or adenoids.

**L57.3** `Compound Sentence` (0.765) → `decomposed`
- original: Tramadol should not be given to a child younger than 12 years old, or to anyone younger than 18 years old who has recently had surgery to remove the tonsils or adenoids.
  - S1: Tramadol should not be given to a child younger than 12 years old.
  - S2: It should not be given to anyone younger than 18 years old who has recently had surgery to remove the tonsils or adenoids.

**L57.4** `Simple Sentence` (0.976) → `passthrough`
- original: Extended-release tramadol should not be given to anyone younger than 18 years.

**L58.0** `Simple Sentence` (0.974) → `passthrough`
- original: Tramadol may cause drowsiness or affect your ability to drive or perform hazardous tasks.

**L58.1** `Incomplete Sentence` (0.845) → `excluded_incomplete`
- original: Do not perform these tasks if tramadol causes confusion, mental impairment, or drowsiness.

**L59.0** `Simple Sentence` (0.957) → `passthrough`
- original: Tramadol can cause withdrawal symptom s if stopped suddenly after being taken for a long period of time.

**L59.1** `Simple Sentence` (0.954) → `passthrough`
- original: Symptoms may include restlessness, drug craving, anxiety, and sweating.

**L59.2** `Complex Sentence` (0.445) → `decomposed`
- original: Do not stop taking tramadol suddenly without talking to your healthcare provider, as stopping abruptly can cause serious withdrawal symptoms and uncontrolled pain (see How long does tramadol withdrawal last?
  - S1: Do not stop taking tramadol suddenly without talking to your healthcare provider.
  - S2: Stopping abruptly can cause serious withdrawal symptoms.
  - S3: Stopping abruptly can cause uncontrolled pain.
  - S4: See How long does tramadol withdrawal last?

**L59.3** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: ).

**L60.0** `Compound Sentence` (0.545) → `decomposed`
- original: This is not a complete list of side effects, and others may occur.
  - S1: This is not a complete list of side effects.
  - S2: Others may occur.

**L60.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L60.2** `Simple Sentence` (0.97) → `passthrough`
- original: You may report side effects to the FDA at 1-800-FDA-1088.

## Before taking this medicine

**L63.0** `Incomplete Sentence` (0.976) → `excluded_incomplete`
- original: Do not take tramadol if you are:

**L64.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: are allergic to tramadol, to any of the other ingredients in your product, or to other opioids

**L65.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: have significant breathing problems (respiratory depression)

**L66.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: have acute or severe asthma and are somewhere you cannot be monitored, or where resuscitation equipment is not available

**L67.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: have a known or suspected blockage of the stomach or intestines, including paralytic ileus

**L68.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: have taken a monoamine oxidase inhibitor (MAOI) in the past 14 days (such as isocarboxazid, linezolid, methylene blue injection, phenelzine, or tranylcypromine)

**L69.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: are younger than 12 years of age

**L70.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: are younger than 18 years of age and have recently had surgery to remove your tonsils or adenoids.

**L71.0** `Simple Sentence` (0.99) → `passthrough`
- original: Seizures have occurred in some people taking tramadol.

**L71.1** `Simple Sentence` (0.986) → `passthrough`
- original: Your seizure risk may be higher if you have ever had:

**L72.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a head injury, epilepsy, or other seizure disorder

**L73.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: drug or alcohol addiction or

**L74.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: a metabolic disorder.

**L75.0** `Incomplete Sentence` (0.771) → `excluded_incomplete`
- original: To make sure tramadol is safe for you, tell your doctor if you have a history of:

**L76.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Head injury or seizures

**L77.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Problems urinating

**L78.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Liver, kidney, or thyroid problems

**L79.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Pancrease or gallbladder problems, including pancreatitis or surgery on your pancreas

**L80.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: A serious infection

**L81.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Abuse of street or prescription drugs, alcohol addiction, opioid overdose, or mental health problems.

**L82.0** `Compound Sentence` (0.597) → `decomposed`
- original: Also tell your doctor if you are dehydrated, are eating less or have changed your diet, are on a low-sodium (salt) diet, drink a lot of alcohol, or are planning to have surgery.
  - S1: Also tell your doctor if you are dehydrated.
  - S2: Also tell your doctor if you are eating less.
  - S3: Also tell your doctor if you have changed your diet.
  - S4: Also tell your doctor if you are on a low-sodium (salt) diet.
  - S5: Also tell your doctor if you drink a lot of alcohol.
  - S6: Also tell your doctor if you are planning to have surgery.

**L83.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Tell your healthcare provider if you are:

**L84.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Living in a household where there are small children or someone who has abused street or prescription drugs

**L85.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Taking prescription or over-the-counter medicines, vitamins, or herbal supplements.

**L85.1** `Simple Sentence` (0.988) → `passthrough`
- original: Taking tramadol with certain other medicines can cause serious side effects that could lead to death

**L86.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Notice your pain getting worse.

**L86.1** `Simple Sentence` (0.475) → `passthrough`
- original: If your pain gets worse after you take tramadol, do not take more tramadol without first talking to your doctor.

**L86.2** `Compound Sentence` (0.381) → `decomposed`
- original: Talk to your doctor if the pain you have increases, if you feel more sensitive to pain, or if you have new pain after taking tramadol.
  - S1: Talk to your doctor if the pain you have increases.
  - S2: Talk to your doctor if you feel more sensitive to pain.
  - S3: Talk to your doctor if you have new pain after taking tramadol.

**L87.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Important Information Guiding Use in Pediatric Patients:

**L88.0** `Incomplete Sentence` (0.749) → `excluded_incomplete`
- original: Do not give tramadol to a child younger than 12 years of age or extended-release tramadol to anyone under 18 years.

**L89.0** `Simple Sentence` (0.736) → `passthrough`
- original: Do not give tramadol to a child younger than 18 years of age after surgery to remove the tonsils and/or adenoids.

**L90.0** `Incomplete Sentence` (0.926) → `excluded_incomplete`
- original: Avoid giving tramadol to children between 12 and 18 years of age who have risk factors for breathing problems.

**L90.1** `Compound Sentence` (0.507) → `decomposed`
- original: These include having recently had surgery, obstructive sleep apnea, obesity, severe lung disease, neuromuscular disease, and taking other medicines that can slow breathing.
  - S1: These include having recently had surgery.
  - S2: These include obstructive sleep apnea.
  - S3: These include obesity.
  - S4: These include severe lung disease.
  - S5: These include neuromuscular disease.
  - S6: These include taking other medicines that can slow breathing.

**L91.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Pregnancy:

**L92.0** `Compound Sentence` (0.654) → `decomposed`
- original: Tramadol may harm an unborn baby and is not usually recommended during pregnancy.
  - S1: Tramadol may harm an unborn baby.
  - S2: It is not usually recommended during pregnancy.

**L92.1** `Simple Sentence` (0.66) → `passthrough`
- original: Use of tramadol for an extended period of time during pregnancy can cause withdrawal symptoms in your newborn baby that could be life-threatening if not recognized and treated.

**L92.2** `Simple Sentence` (0.919) → `passthrough`
- original: Neonatal seizures, neonatal withdrawal syndrome, fetal death, and stillbirth have all been reported.

**L92.3** `Simple Sentence` (0.977) → `passthrough`
- original: Tramadol is also not recommended during or immediately before labor.

**L92.4** `Simple Sentence` (0.958) → `passthrough`
- original: It should only be used in pregnancy if the benefits outweigh the risks.

**L92.5** `Complex Sentence` (0.852) → `decomposed`
- original: If you are already taking tramadol and become pregnant, do not stop taking it without talking to your healthcare provider, as stopping suddenly can be harmful to you both.
- pronoun resolved: If you are already taking tramadol and become pregnant, do not stop taking tramadol without talking to your healthcare provider, as stopping suddenly can be harmful to you both.
  - edits: “it” → “tramadol”
  - S1: If you are already taking tramadol and become pregnant, do not stop taking tramadol without talking to your healthcare provider.
  - S2: Stopping tramadol suddenly can be harmful to you both.

**L93.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Breastfeeding:

**L94.0** `Compound Sentence` (0.529) → `decomposed`
- original: Breastfeeding is not recommended while taking tramadol, as it may harm your baby.
- pronoun resolved: Breastfeeding is not recommended while taking tramadol, as tramadol may harm your baby.
  - edits: “it” → “tramadol”
  - S1: Breastfeeding is not recommended while taking tramadol.
  - S2: Tramadol may harm your baby.

**L94.1** `Complex Sentence` (0.939) → `decomposed`
- original: Mothers who are ultra-rapid metabolizers of tramadol can have higher than expected levels of its active form in their breast milk, which can be dangerous for a breastfed infant.
- pronoun resolved: Mothers who are ultra-rapid metabolizers of tramadol can have higher than expected levels of tramadol's active form in their breast milk, which can be dangerous for a breastfed infant.
  - edits: “its” → “tramadol's”
  - S1: Mothers who are ultra-rapid metabolizers of tramadol can have higher than expected levels of tramadol's active form in their breast milk.
  - S2: This can be dangerous for a breastfed infant.

**L94.2** `Incomplete Sentence` (0.966) → `excluded_incomplete`
- original: Carefully observe infants for increased sleepiness (more than usual), breathing difficulties, or limpness.

**L94.3** `Incomplete Sentence` (0.894) → `excluded_incomplete`
- original: Seek immediate medical care if you notice these signs.

## How should I take tramadol?

**L97.0** `Incomplete Sentence` (0.886) → `excluded_incomplete`
- original: Do not change your dose.

**L97.1** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Take tramadol exactly as prescribed by your healthcare provider.

**L97.2** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Use the lowest dose possible for the shortest time needed.

**L97.3** `Incomplete Sentence` (0.873) → `excluded_incomplete`
- original: Tell your doctor if you feel an increased urge to take more of this medicine.
- pronoun resolved: Tell your doctor if you feel an increased urge to take more of tramadol.
  - edits: “this medicine.” → “tramadol.”

**L98.0** `Simple Sentence` (0.855) → `passthrough`
- original: For acute (short-term) pain, you may only need to take tramadol for a few days.

**L98.1** `Simple Sentence` (0.949) → `passthrough`
- original: You may have some tramadol left over that you did not use.

**L98.2** `Simple Sentence` (0.472) → `passthrough`
- original: See disposal information at the bottom of this section for directions on how to safely dispose of tramadol.

**L99.0** `Incomplete Sentence` (0.976) → `excluded_incomplete`
- original: Take your prescribed dose as indicated by your healthcare provider.

**L99.1** `Incomplete Sentence` (0.976) → `excluded_incomplete`
- original: Take your prescribed dose as indicated by your healthcare provider.

**L99.2** `Complex Sentence` (0.821) → `decomposed`
- original: After your dose has been settled, immediate-release tramadol is usually taken as 50 mg to 100 mg (one or two 50 mg tablets) every 4 to 6 hours as needed for pain.
  - S1: Immediate-release tramadol is usually taken as 50 mg to 100 mg.
  - S2: This dosage corresponds to one or two 50 mg tablets.
  - S3: The medication is taken every 4 to 6 hours as needed for pain.
  - S4: This dosing schedule occurs after your dose has been settled.

**L99.3** `Compound Sentence` (0.693) → `decomposed`
- original: Do not take more than your prescribed dose, and do not take more than 400 mg of tramadol in one day.
  - S1: Do not take more than your prescribed dose.
  - S2: Do not take more than 400 mg of tramadol in one day.

**L99.4** `Compound Sentence` (0.639) → `decomposed`
- original: For immediate-release tramadol, that is eight 50 mg tablets a day, taken in divided doses, or 80 mL of the 5 mg/mL oral solution.
  - S1: For immediate-release tramadol, the dosage is eight 50 mg tablets a day.
  - S2: These tablets are taken in divided doses.
  - S3: Alternatively, the dosage is 80 mL of the 5 mg/mL oral solution.

**L99.5** `Simple Sentence` (0.882) → `passthrough`
- original: Extended-release tramadol has a lower daily limit of 300 mg, taken as one dose once a day.

**L99.6** `Incomplete Sentence` (0.951) → `excluded_incomplete`
- original: Always check the strength printed on your own bottle or packet.

**L99.7** `Incomplete Sentence` (0.839) → `excluded_incomplete`
- original: Do not take tramadol together with any other medicine that contains tramadol.

**L100.0** `Simple Sentence` (0.716) → `passthrough`
- original: If you miss a dose, take your next dose at your usual time.

**L101.0** `Incomplete Sentence` (0.938) → `excluded_incomplete`
- original: Swallow the capsule or tablet whole to avoid exposure to a potentially fatal overdose.

**L101.1** `Incomplete Sentence` (0.892) → `excluded_incomplete`
- original: Do not crush, chew, break, open, or dissolve.

**L102.0** `Incomplete Sentence` (0.683) → `excluded_incomplete`
- original: Never crush or break a tramadol tablet to inhale the powder or mix it into a liquid to inject the drug into your vein.
- pronoun resolved: Never crush or break a tramadol tablet to inhale the powder or mix tramadol tablet into a liquid to inject tramadol into your vein.
  - edits: “it” → “tramadol tablet”; “the drug” → “tramadol”

**L102.1** `Simple Sentence` (0.969) → `passthrough`
- original: This practice has resulted in death.

**L103.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: May be taken with or without food.

**L104.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: If you take the oral solution:

**L105.0** `Compound Sentence` (0.877) → `decomposed`
- original: Tramadol oral solution is measured in millilitres (mL), not milligrams (mg), and contains 5 mg of tramadol in every 1 mL.
  - S1: Tramadol oral solution is measured in millilitres (mL), not milligrams (mg).
  - S2: It contains 5 mg of tramadol in every 1 mL.

**L105.1** `Simple Sentence` (0.986) → `passthrough`
- original: Confusing the two units can cause a fatal overdose.

**L105.2** `Compound Sentence` (0.878) → `decomposed`
- original: Always measure your dose with a graduated oral syringe or measuring cup marked in mL, which your pharmacy can supply, and never with a household teaspoon or tablespoon.
  - S1: Always measure your dose with a graduated oral syringe or measuring cup marked in mL.
  - S2: Your pharmacy can supply these tools.
  - S3: Never measure your dose with a household teaspoon or tablespoon.

**L105.3** `Complex Sentence` (0.591) → `decomposed`
- original: If your prescription is written in milligrams, ask your pharmacist to confirm how many millilitres that is before you take your first dose.
  - S1: If your prescription is written in milligrams, ask your pharmacist to confirm how many millilitres that is.
  - S2: Do this before you take your first dose.

**L106.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Notes:

**L107.0** `Simple Sentence` (0.983) → `passthrough`
- original: You may have withdrawal symptoms if you stop using tramadol suddenly.

**L107.1** `Incomplete Sentence` (0.859) → `excluded_incomplete`
- original: Ask your doctor before stopping the medicine.
- pronoun resolved: Ask your doctor before stopping tramadol.
  - edits: “the medicine.” → “tramadol.”

**L108.0** `Incomplete Sentence` (0.784) → `excluded_incomplete`
- original: Ask your healthcare provider about medicines like naloxone or nalmefene that can be used in an emergency to reverse an opioid overdose.

**L109.0** `Incomplete Sentence` (0.97) → `excluded_incomplete`
- original: Do not keep leftover tramadol.

**L109.1** `Simple Sentence` (0.975) → `passthrough`
- original: Just one dose can cause death if someone uses it accidentally or improperly.
- pronoun resolved: Just one dose can cause death if someone uses leftover tramadol accidentally or improperly.
  - edits: “it” → “leftover tramadol”

**L109.2** `Incomplete Sentence` (0.973) → `excluded_incomplete`
- original: Ask your pharmacist where to locate a drug take-back disposal program.

**L109.3** `Compound Sentence` (0.512) → `decomposed`
- original: If there is no take-back program, mix the leftover medicine with cat litter or coffee grounds in a sealed plastic bag and throw the bag in the trash.
  - S1: If there is no take-back program, mix the leftover medicine with cat litter or coffee grounds in a sealed plastic bag.
  - S2: Throw the bag in the trash.

**L110.0** `Incomplete Sentence` (0.767) → `excluded_incomplete`
- original: Call your healthcare provider if the dose you are taking does not control your pain.

**L111.0** `Simple Sentence` (0.483) → `passthrough`
- original: If you have been taking tramadol regularly, do not stop taking tramadol without talking to your healthcare provider.

## Dosing Information

**L114.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Adult Tramadol Dosage for Pain:

**L115.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Immediate-release formulations (tablets and oral solution)

**L116.0** `Compound Sentence` (0.765) → `decomposed`
- original: Treatment usually starts at 25 mg a day, increasing by 25 mg every 3 days to reach 100 mg a day (25 mg four times a day).
  - S1: Treatment usually starts at 25 mg a day.
  - S2: The dosage increases by 25 mg every 3 days.
  - S3: This process continues until the target of 100 mg a day (25 mg four times a day) is reached.

**L116.1** `Compound Sentence` (0.943) → `decomposed`
- original: Doses of 25 mg are measured using the oral solution, as immediate-release tramadol tablets are only available as 50 mg.
  - S1: Doses of 25 mg are measured using the oral solution.
  - S2: Immediate-release tramadol tablets are only available as 50 mg.

**L117.0** `Complex Sentence` (0.913) → `decomposed`
- original: For the immediate-release tablets, a common starting dose is one 50 mg tablet a day to see how well you tolerate it, or the dose prescribed by your doctor.
- pronoun resolved: For the immediate-release tablets, a common starting dose is one 50 mg tablet a day to see how well you tolerate 50 mg tablet, or the dose prescribed by your doctor.
  - edits: “it,” → “50 mg tablet,”
  - S1: For the immediate-release tablets, a common starting dose is one 50 mg tablet a day.
  - S2: This dose is used to see how well you tolerate 50 mg tablet.
  - S3: Alternatively, the dose prescribed by your doctor may be used.

**L118.0** `Complex Sentence` (0.643) → `decomposed`
- original: If needed, the total daily dose can then be increased by 50 mg every 3 days as tolerated, to reach 200 mg a day (one 50 mg tablet four times a day).
  - S1: If needed, the total daily dose can be increased by 50 mg every 3 days as tolerated.
  - S2: The increase continues to reach 200 mg a day.
  - S3: This target dose is equivalent to one 50 mg tablet four times a day.

**L119.0** `Complex Sentence` (0.643) → `decomposed`
- original: After this titration, 50 mg to 100 mg (one or two 50 mg tablets) can be taken every 4 to 6 hours as needed for pain.
  - S1: After this titration, 50 mg to 100 mg can be taken every 4 to 6 hours as needed for pain.
  - S2: This amount corresponds to one or two 50 mg tablets.

**L120.0** `Compound Sentence` (0.751) → `decomposed`
- original: The maximum is 400 mg a day: eight 50 mg tablets in divided doses, or 80 mL of the 5 mg/mL oral solution.
  - S1: The maximum is 400 mg a day.
  - S2: This is eight 50 mg tablets in divided doses.
  - S3: Alternatively, it is 80 mL of the 5 mg/mL oral solution.

**L121.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Extended-release capsules and tablets

**L122.0** `Simple Sentence` (0.987) → `passthrough`
- original: Tramadol ER 100 mg once a day (one 100 mg tablet or capsule) at approximately the same time each day.

**L123.0** `Incomplete Sentence` (0.737) → `excluded_incomplete`
- original: Can be increased by 100 mg every 5 days if needed, to a maximum of 300 mg a day, taken as one dose once a day.

**L124.0** `Compound Sentence` (0.917) → `decomposed`
- original: Extended-release tramadol is not intended for as-needed pain relief, and should not be taken with any other tramadol product.
  - S1: Extended-release tramadol is not intended for as-needed pain relief.
  - S2: It should not be taken with any other tramadol product.

**L125.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Dosage in kidney or liver impairment

**L126.0** `Compound Sentence` (0.494) → `decomposed`
- original: Severe kidney impairment: for immediate-release tramadol, doses are spaced 12 hours apart, and the maximum is 200 mg a day (four 50 mg tablets, given as two 100 mg doses 12 hours apart).
  - S1: Severe kidney impairment requires specific dosing adjustments for immediate-release tramadol.
  - S2: For this condition, doses are spaced 12 hours apart.
  - S3: The maximum daily dose is 200 mg.
  - S4: This maximum consists of four 50 mg tablets.
  - S5: These tablets are given as two 100 mg doses.
  - S6: The doses are administered 12 hours apart.

**L127.0** `Complex Sentence` (0.82) → `decomposed`
- original: Severe liver impairment: for immediate-release tramadol, the recommended dose is 50 mg (one 50 mg tablet) every 12 hours, which is 100 mg a day.
  - S1: Severe liver impairment is a condition.
  - S2: For immediate-release tramadol, the recommended dose is 50 mg (one 50 mg tablet) every 12 hours.
  - S3: This is 100 mg a day.

**L128.0** `Simple Sentence` (0.953) → `passthrough`
- original: Extended-release tramadol is not recommended for people with severe kidney or severe liver impairment.

**L129.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Dosage in older adults

**L130.0** `Compound Sentence` (0.537) → `decomposed`
- original: No separate maximum dose applies on the basis of age, but tramadol should be started at the low end of the dosing range and increased slowly, with frequent review for drowsiness and breathing problems.
  - S1: No separate maximum dose applies on the basis of age.
  - S2: Tramadol should be started at the low end of the dosing range.
  - S3: The dose should be increased slowly.
  - S4: Frequent review is needed for drowsiness and breathing problems.

**L131.0** `Complex Sentence` (0.578) → `decomposed`
- original: Side effects that led people to stop treatment were more common over the age of 75, mostly stomach and bowel effects, such as constipation.
  - S1: Side effects that led people to stop treatment were more common over the age of 75.
  - S2: These side effects were mostly stomach and bowel effects.
  - S3: Examples included constipation.

**L131.1** `Compound-Complex Sentence` (0.87) → `decomposed`
- original: Kidney function also tends to decline with age, which affects how tramadol is cleared, so your doctor may take this into account when choosing your dose.
  - S1: Kidney function tends to decline with age.
  - S2: Declining kidney function affects how tramadol is cleared.
  - S3: Your doctor may take kidney function into account when choosing your dose.

## What happens if I miss a dose?

**L134.0** `Compound Sentence` (0.334) → `decomposed`
- original: Since tramadol is used for pain, you are unlikely to miss a dose.
  - S1: Tramadol is used for pain.
  - S2: You are unlikely to miss a dose.

**L134.1** `Incomplete Sentence` (0.877) → `excluded_incomplete`
- original: Skip any missed dose if it is almost time for your next dose.

**L134.2** `Incomplete Sentence` (0.946) → `excluded_incomplete`
- original: Do not use two doses at one time.

## What happens if I overdose?

**L137.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L137.1** `Compound Sentence` (0.423) → `decomposed`
- original: An overdose can be fatal, especially in a child or other person using the medicine without a prescription.
  - S1: An overdose can be fatal.
  - S2: This is especially true in a child or other person using the medicine without a prescription.

**L137.2** `Simple Sentence` (0.508) → `passthrough`
- original: Overdose symptoms may include severe drowsiness, pinpoint pupils, slow breathing, or no breathing.

**L138.0** `Compound Sentence` (0.695) → `decomposed`
- original: Your doctor may recommend you get naloxone (a medicine to reverse an opioid overdose) and keep it with you at all times.
- pronoun resolved: Your doctor may recommend you get naloxone (a medicine to reverse an opioid overdose) and keep naloxone with you at all times.
  - edits: “it” → “naloxone”
  - S1: Your doctor may recommend you get naloxone.
  - S2: Naloxone is a medicine to reverse an opioid overdose.
  - S3: You should keep naloxone with you at all times.

**L138.1** `Simple Sentence` (0.927) → `passthrough`
- original: A person caring for you can give naloxone if you stop breathing or don't wake up.

**L138.2** `Compound Sentence` (0.816) → `decomposed`
- original: Your caregiver must still get emergency medical help and may need to perform CPR (cardiopulmonary resuscitation) on you while waiting for help to arrive.
  - S1: Your caregiver must still get emergency medical help.
  - S2: Your caregiver may need to perform CPR (cardiopulmonary resuscitation) on you while waiting for help to arrive.

**L139.0** `Simple Sentence` (0.977) → `passthrough`
- original: Anyone can buy naloxone from a pharmacy or local health department.

**L139.1** `Incomplete Sentence` (0.901) → `excluded_incomplete`
- original: Make sure any person caring for you knows where you keep naloxone and how to use it.

## What should I avoid while taking tramadol?

**L142.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Do not drink alcohol or use prescription or over-the-counter medicines that contain alcohol.

**L142.1** `Simple Sentence` (0.977) → `passthrough`
- original: Dangerous side effects or death could occur.

**L143.0** `Incomplete Sentence` (0.959) → `excluded_incomplete`
- original: Avoid driving or hazardous activities until you know how tramadol will affect you.

**L143.1** `Simple Sentence` (0.961) → `passthrough`
- original: Dizziness or drowsiness can cause falls, accidents, or severe injuries.

## What other drugs will affect tramadol?

**L146.0** `Simple Sentence` (0.924) → `passthrough`
- original: You may have breathing problems or withdrawal symptoms if you start or stop taking certain other medicines.

**L146.1** `Compound Sentence` (0.85) → `decomposed`
- original: Tramadol is broken down by two liver enzymes called CYP3A4 and CYP2D6, and medicines that block or speed up these enzymes change how much tramadol and how much of its active form are in your body.
- pronoun resolved: Tramadol is broken down by two liver enzymes called CYP3A4 and CYP2D6, and medicines that block or speed up these enzymes change how much tramadol and how much of tramadol's active form are in your body.
  - edits: “its” → “tramadol's”
  - S1: Tramadol is broken down by two liver enzymes called CYP3A4 and CYP2D6.
  - S2: Medicines that block or speed up these enzymes change how much tramadol and how much of tramadol's active form are in your body.

**L146.2** `Complex Sentence` (0.892) → `decomposed`
- original: Because starting one of these medicines and stopping one both shift the balance, tell your doctor whenever you begin or finish a course of an antibiotic, antifungal medication, heart or blood pressure medication, seizure medication, or medicine to treat HIV or hepatitis C.
  - S1: Starting one of these medicines and stopping one both shift the balance.
  - S2: Tell your doctor whenever you begin or finish a course of an antibiotic, antifungal medication, heart or blood pressure medication, seizure medication, or medicine to treat HIV or hepatitis C.

**L147.0** `Simple Sentence` (0.987) → `passthrough`
- original: Many other drugs can be dangerous when used with tramadol.

**L147.1** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Tell your doctor if you also use:

**L148.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: medicine for allergies, asthma, blood pressure, motion sickness, irritable bowel, or overactive bladder

**L149.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: other opioid medicines

**L150.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: buprenorphine, butorphanol, nalbuphine, or pentazocine.

**L150.1** `Compound-Complex Sentence` (0.629) → `decomposed`
- original: These opioids work differently and can block tramadol's pain-relieving effect or bring on sudden withdrawal symptoms, so they are generally not taken with tramadol
- pronoun resolved: These opioids work differently and can block tramadol's pain-relieving effect or bring on sudden withdrawal symptoms, so opioids are generally not taken with tramadol
  - edits: “they” → “opioids”
  - S1: These opioids work differently.
  - S2: These opioids can block tramadol's pain-relieving effect.
  - S3: These opioids can bring on sudden withdrawal symptoms.
  - S4: Opioids are generally not taken with tramadol.

**L151.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a benzodiazepine sedative like Valium, Klonopin, or Xanax

**L152.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: sleep medicine, muscle relaxers, or other drugs that make you drowsy

**L153.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: drugs that affect serotonin, such as antidepressants, stimulants, or medicine for migraines or Parkinson's disease

**L154.0** `Incomplete Sentence` (0.855) → `excluded_incomplete`
- original: carbamazepine, which is not recommended with tramadol because it can significantly reduce tramadol's pain-relieving effect and add to the risk of seizures
- pronoun resolved: carbamazepine, which is not recommended with tramadol because carbamazepine can significantly reduce tramadol's pain-relieving effect and add to the risk of seizures
  - edits: “it” → “carbamazepine”

**L155.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: digoxin or warfarin, which need extra monitoring when taken with tramadol.

**L156.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L156.1** `Complex Sentence` (0.551) → `decomposed`
- original: Other drugs may interact with tramadol, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may interact with tramadol.
  - S2: These drugs include prescription and over-the-counter medicines.
  - S3: These drugs also include vitamins and herbal products.

**L156.2** `Simple Sentence` (0.949) → `passthrough`
- original: Not all possible interactions are listed here.

## Storage

**L159.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Store at room temperature away from moisture and heat and out of reach of children.

**L159.1** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Do not share with others.

## Popular FAQ

**L162.0** `Simple Sentence` (0.907) → `passthrough`
- original: Q: Can You Take Tramadol with Acetaminophen, Ibuprofen, or Aspirin?

**L162.1** `Compound-Complex Sentence` (0.711) → `decomposed`
- original: A: Yes, for most people, tramadol can be safely combined with acetaminophen, ibuprofen, or aspirin, and doing so can provide better pain relief than either medicine alone.
  - S1: Tramadol can be safely combined with acetaminophen.
  - S2: Tramadol can be safely combined with ibuprofen.
  - S3: Tramadol can be safely combined with aspirin.
  - S4: Combining tramadol with these medicines provides better pain relief.
  - S5: This relief is better than using either medicine alone.

**L162.2** `Simple Sentence` (0.934) → `passthrough`
- original: However, there are important age restrictions and clinical considerations to be aware of.

**L163.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Q: How much tramadol should I give my dog?

**L163.1** `Simple Sentence` (0.977) → `passthrough`
- original: A: How much tramadol you give your dog depends on the size of your dog.

**L163.2** `Simple Sentence` (0.92) → `passthrough`
- original: Smaller dogs do not need as much tramadol as larger dogs need to relieve pain.

**L163.3** `Simple Sentence` (0.954) → `passthrough`
- original: If you give too much tramadol your dog is likely to have more severe side effects.

**L163.4** `Simple Sentence` (0.722) → `passthrough`
- original: The tramadol dosage for dogs is usually between 0.45 to 1.8 mg per pound of body weight (1mg to 4 mg/kg).

**L163.5** `Simple Sentence` (0.984) → `passthrough`
- original: The frequency varies depending on what you are giving it for.
- pronoun resolved: The frequency varies depending on what you are giving tramadol for.
  - edits: “it” → “tramadol”

**L163.6** `Compound Sentence` (0.964) → `decomposed`
- original: For general pain, it is given every 8 to 12 hours, but for cancer-related pain, it can be administered every 6 hours.
- pronoun resolved: For general pain, tramadol is given every 8 to 12 hours, but for cancer-related pain, tramadol can be administered every 6 hours.
  - edits: “it” → “tramadol”; “it” → “tramadol”
  - S1: For general pain, tramadol is given every 8 to 12 hours.
  - S2: For cancer-related pain, tramadol can be administered every 6 hours.

**L164.0** `Incomplete Sentence` (0.962) → `excluded_incomplete`
- original: Q: How long does it take for tramadol to start working?

**L164.1** `Complex Sentence` (0.799) → `decomposed`
- original: A: Tramadol generally starts to relieve pain within an hour in its fast-acting forms, which are used for short-term pain management.
  - S1: Tramadol generally starts to relieve pain within an hour.
  - S2: This applies to its fast-acting forms.
  - S3: These forms are used for short-term pain management.

**L164.2** `Compound Sentence` (0.585) → `decomposed`
- original: With slow-release or extended-release (ER) forms, the drug may take longer to start because it’s gradually released over 12 or 24 hours, but pain relief lasts longer.
- pronoun resolved: With slow-release or extended-release (ER) forms, Tramadol may take longer to start because it’s gradually released over 12 or 24 hours, but pain relief lasts longer.
  - edits: “the drug” → “Tramadol”
  - S1: With slow-release or extended-release (ER) forms, Tramadol may take longer to start because it's gradually released over 12 or 24 hours.
  - S2: Pain relief lasts longer.

**L165.0** `Incomplete Sentence` (0.958) → `excluded_incomplete`
- original: Q: How long does tramadol withdrawal last?

**L165.1** `Simple Sentence` (0.949) → `passthrough`
- original: A: Symptoms of tramadol withdrawal can start 8-24 hours after the last dose.

**L165.2** `Simple Sentence` (0.979) → `passthrough`
- original: Untreated, withdrawal symptoms usually last for 4-10 days.

**L165.3** `Simple Sentence` (0.991) → `passthrough`
- original: Withdrawal is caused by stopping the drug suddenly.
- pronoun resolved: Withdrawal is caused by stopping tramadol suddenly.
  - edits: “the drug” → “tramadol”

**L166.0** `Incomplete Sentence` (0.935) → `excluded_incomplete`
- original: Q: Is tramadol stronger than codeine?

**L166.1** `Compound Sentence` (0.922) → `decomposed`
- original: A: Both tramadol and codeine are prescription painkillers used to treat moderate pain, and they are generally considered comparable in terms of pain relief.
- pronoun resolved: A: Both tramadol and codeine are prescription painkillers used to treat moderate pain, and tramadol and codeine are generally considered comparable in terms of pain relief.
  - edits: “they” → “tramadol and codeine”
  - S1: Both tramadol and codeine are prescription painkillers used to treat moderate pain.
  - S2: Tramadol and codeine are generally considered comparable in terms of pain relief.

**L166.2** `Compound Sentence` (0.857) → `decomposed`
- original: Tramadol is sometimes considered slightly more effective for moderate to moderately severe pain due to its dual mechanism of action, but both are classified as "weak" opioids.
- pronoun resolved: Tramadol is sometimes considered slightly more effective for moderate to moderately severe pain due to Tramadol's dual mechanism of action, but both are classified as "weak" opioids.
  - edits: “its” → “Tramadol's”
  - S1: Tramadol is sometimes considered slightly more effective for moderate to moderately severe pain.
  - S2: This is due to Tramadol's dual mechanism of action.
  - S3: Both are classified as "weak" opioids.

**L167.0** `Incomplete Sentence` (0.615) → `excluded_incomplete`
- original: Q: How long does tramadol stay in your system?

**L167.1** `Compound Sentence` (0.893) → `decomposed`
- original: A: Tramadol is eliminated from your system within roughly 2 days of taking the drug, but this does not mean that it can no longer be detected by certain drug tests.
- pronoun resolved: A: Tramadol is eliminated from your system within roughly 2 days of taking tramadol, but this does not mean that tramadol can no longer be detected by certain drug tests.
  - edits: “the drug,” → “tramadol,”; “it” → “tramadol”
  - S1: Tramadol is eliminated from your system within roughly 2 days of taking tramadol.
  - S2: This does not mean that tramadol can no longer be detected by certain drug tests.

**L168.0** `Simple Sentence` (0.804) → `passthrough`
- original: Q: Can you take ibuprofen 800 mg with tramadol 50 mg?

**L168.1** `Simple Sentence` (0.931) → `passthrough`
- original: A: Yes, you can take these medications together.

**L168.2** `Compound Sentence` (0.917) → `decomposed`
- original: Tramadol is safe to take with ibuprofen and may be used to provide additional pain relief.
  - S1: Tramadol is safe to take with ibuprofen.
  - S2: It may be used to provide additional pain relief.

**L168.3** `Complex Sentence` (0.681) → `decomposed`
- original: But be aware 800mg ibuprofen is a high dose of ibuprofen that may cause gastrointestinal side effects such as abdominal pain or reflux if taken long term.
  - S1: But be aware 800mg ibuprofen is a high dose of ibuprofen.
  - S2: This high dose may cause gastrointestinal side effects.
  - S3: These side effects include abdominal pain or reflux.
  - S4: These effects may occur if taken long term.

**L169.0** `Incomplete Sentence` (0.962) → `excluded_incomplete`
- original: Q: Is tramadol an anti-inflammatory or muscle relaxant?

**L169.1** `Simple Sentence` (0.89) → `passthrough`
- original: A: No, Tramadol is not an anti-inflammatory drug or muscle relaxer.

**L169.2** `Complex Sentence` (0.536) → `decomposed`
- original: Because it’s not an anti-inflammatory drug, it likely won’t reduce any swelling you have when taken alone.
- pronoun resolved: Because it’s not an anti-inflammatory drug, Tramadol likely won’t reduce any swelling you have when taken alone.
  - edits: “it” → “Tramadol”
  - S1: Tramadol likely won't reduce any swelling you have when taken alone.
  - S2: This is because it's not an anti-inflammatory drug.

**L170.0** `Incomplete Sentence` (0.81) → `excluded_incomplete`
- original: Q: Does tramadol raise or lower blood pressure?

**L170.1** `Simple Sentence` (0.989) → `passthrough`
- original: A: Tramadol has been linked to both high blood pressure and low blood pressure.

**L170.2** `Simple Sentence` (0.588) → `passthrough`
- original: But, neither adverse reaction is common when the medicine is taken as directed.
- pronoun resolved: But, neither adverse reaction is common when Tramadol is taken as directed.
  - edits: “the medicine” → “Tramadol”
