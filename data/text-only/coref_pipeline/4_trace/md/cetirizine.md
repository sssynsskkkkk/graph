# Cetirizine — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/cetirizine.txt` · 94 sentences · 23 changed by pronoun resolution · 152 sentences sent to EDC

## What is cetirizine?

**L5.0** `Simple Sentence` (0.97) → `passthrough`
- original: Cetirizine is a second generation antihistamine that reduces the natural chemical histamine in the body.

**L5.1** `Simple Sentence` (0.966) → `passthrough`
- original: Histamine can produce symptoms of sneezing, itching, watery eyes, and runny nose.

**L6.0** `Simple Sentence` (0.787) → `passthrough`
- original: Cetirizine is used to treat cold or allergy symptoms such as sneezing, itching, watery eyes, or runny nose.

**L7.0** `Compound-Complex Sentence` (0.81) → `decomposed` · repaired
- original: Cetirizine is also used to treat an allergic reaction, itching and swelling caused by chronic urticaria (hives) and minimizes or eliminates the symptoms of perennial allergic rhinitis, seasonal allergic rhinitis, chronic idiopathic urticaria, allergic asthma, physical urticaria, and atopic dermatitis.
  - S1: Cetirizine is used to treat an allergic reaction.
  - S2: Cetirizine treats itching caused by chronic urticaria.
  - S3: Cetirizine treats swelling caused by chronic urticaria.
  - S4: Cetirizine minimizes the symptoms of perennial allergic rhinitis.
  - S5: Cetirizine eliminates the symptoms of perennial allergic rhinitis.
  - S6: Cetirizine minimizes the symptoms of seasonal allergic rhinitis.
  - S7: Cetirizine eliminates the symptoms of seasonal allergic rhinitis.
  - S8: Cetirizine minimizes the symptoms of chronic idiopathic urticaria.
  - S9: Cetirizine eliminates the symptoms of chronic idiopathic urticaria.
  - S10: Cetirizine minimizes the symptoms of allergic asthma.
  - S11: Cetirizine eliminates the symptoms of allergic asthma.
  - S12: Cetirizine minimizes the symptoms of physical urticaria.
  - S13: Cetirizine eliminates the symptoms of physical urticaria.
  - S14: Cetirizine minimizes the symptoms of atopic dermatitis.
  - S15: Cetirizine eliminates the symptoms of atopic dermatitis.

## Warnings

**L10.0** `Simple Sentence` (0.988) → `passthrough`
- original: Cetirizine can cause side effects that may impair your thinking or reactions.

**L10.1** `Incomplete Sentence` (0.686) → `excluded_incomplete`
- original: Be careful if you drive or do anything that requires you to be awake and alert.

**L10.2** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Avoid drinking alcohol.

**L10.3** `Simple Sentence` (0.989) → `passthrough`
- original: It can increase some of the side effects of cetirizine.
- pronoun resolved: Cetirizine can increase some of the side effects of cetirizine.
  - edits: “It” → “Cetirizine”

**L11.0** `Compound Sentence` (0.28) → `decomposed`
- original: Tell your doctor if you regularly use other medicines that make you sleepy (such as other cold or allergy medicine, narcotic pain medicine, sleeping pills, muscle relaxers, and medicine for seizures, depression, or anxiety).
  - S1: Tell your doctor if you regularly use other medicines that make you sleepy.
  - S2: Examples of such medicines include other cold or allergy medicine, narcotic pain medicine, sleeping pills, muscle relaxers, and medicine for seizures, depression, or anxiety.

**L11.1** `Simple Sentence` (0.991) → `passthrough`
- original: They can add to sleepiness caused by cetirizine.
- pronoun resolved: Other medicines can add to sleepiness caused by cetirizine.
  - edits: “They” → “Other medicines”

**L12.0** `Compound Sentence` (0.36) → `decomposed`
- original: Call your doctor if your symptoms do not improve, if they get worse, or if you also have a fever.
- pronoun resolved: Call your doctor if your symptoms do not improve, if symptoms get worse, or if you also have a fever.
  - edits: “they” → “symptoms”
  - S1: Call your doctor if your symptoms do not improve.
  - S2: Call your doctor if symptoms get worse.
  - S3: Call your doctor if you also have a fever.

**L13.0** `Complex Sentence` (0.661) → `decomposed`
- original: If you are taking cetirizine for hives, get emergency medical help immediately if you have trouble swallowing, dizziness, swelling of the tongue or around the mouth, trouble speaking, drooling, or wheezing.
  - S1: If you are taking cetirizine for hives, get emergency medical help immediately if you have trouble swallowing.
  - S2: Get emergency medical help immediately if you have dizziness.
  - S3: Get emergency medical help immediately if you have swelling of the tongue.
  - S4: Get emergency medical help immediately if you have swelling around the mouth.
  - S5: Get emergency medical help immediately if you have trouble speaking.
  - S6: Get emergency medical help immediately if you have drooling.
  - S7: Get emergency medical help immediately if you have wheezing.

**L13.1** `Simple Sentence` (0.988) → `passthrough`
- original: Cetirizine is not a substitute for an epinephrine injector.

**L13.2** `Simple Sentence` (0.695) → `passthrough`
- original: Do not use cetirizine to prevent hives from known causes such as foods, insect stings, or medicines.

**L13.3** `Compound Sentence` (0.396) → `decomposed`
- original: Call your doctor if your hives do not improve after 3 days, if they last more than 6 weeks, or if they are an unusual color, look bruised or blistered, or do not itch.
- pronoun resolved: Call your doctor if your hives do not improve after 3 days, if hives last more than 6 weeks, or if hives are an unusual color, look bruised or blistered, or do not itch.
  - edits: “they” → “hives”; “they” → “hives”
  - S1: Call your doctor if your hives do not improve after 3 days.
  - S2: Call your doctor if hives last more than 6 weeks.
  - S3: Call your doctor if hives are an unusual color.
  - S4: Call your doctor if hives look bruised.
  - S5: Call your doctor if hives are blistered.
  - S6: Call your doctor if hives do not itch.

**L14.0** `Complex Sentence` (0.847) → `decomposed`
- original: Rarely, some people have reported severe itching when stopping cetirizine after daily, long-term use of at least a few months or several years.
  - S1: Rarely, some people have reported severe itching when stopping cetirizine.
  - S2: This occurred after daily, long-term use of at least a few months or several years.

**L14.1** `Simple Sentence` (0.415) → `passthrough`
- original: If you experience widespread, severe itching on stopping this medication, contact your healthcare provider.

## Before taking this medicine

**L17.0** `Simple Sentence` (0.417) → `passthrough`
- original: You should not use this medication if you are allergic to cetirizine, levocetirizine, hydroxyzine, or any of the ingredients in the product.
- pronoun resolved: You should not use Cetirizine if you are allergic to cetirizine, levocetirizine, hydroxyzine, or any of the ingredients in the product.
  - edits: “this medication” → “Cetirizine”

**L18.0** `Simple Sentence` (0.388) → `passthrough`
- original: Before taking cetirizine, tell your doctor about all of your medical conditions or if you have ever had kidney or liver disease.

**L19.0** `Incomplete Sentence` (0.839) → `excluded_incomplete`
- original: Ask a health professional before using this medicine if you are pregnant.
- pronoun resolved: Ask a health professional before using Cetirizine if you are pregnant.
  - edits: “this medicine” → “Cetirizine”

**L19.1** `Simple Sentence` (0.987) → `passthrough`
- original: Cetirizine is not recommended if you are breast-feeding.

**L20.0** `Simple Sentence` (0.983) → `passthrough`
- original: Cetirizine is indicated for chronic idiopathic urticaria in adults and children 6 months of age and older.

**L21.0** `Simple Sentence` (0.984) → `passthrough`
- original: Older adults may need to take a lower than normal dose.

**L21.1** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Follow your doctor's instructions.

## How should I take cetirizine?

**L24.0** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Take cetirizine exactly as directed on the label, or as prescribed by your doctor.

**L24.1** `Incomplete Sentence` (0.937) → `excluded_incomplete`
- original: Do not use it in larger amounts or for longer than recommended.
- pronoun resolved: Do not use cetirizine in larger amounts or for longer than recommended.
  - edits: “it” → “cetirizine”

**L25.0** `Simple Sentence` (0.979) → `passthrough`
- original: You may take cetirizine with or without food.

**L26.0** `Simple Sentence` (0.983) → `passthrough`
- original: The chewable tablet must be chewed before you swallow it.
- pronoun resolved: The chewable tablet must be chewed before you swallow chewable tablet.
  - edits: “it.” → “chewable tablet.”

**L27.0** `Simple Sentence` (0.499) → `passthrough`
- original: Oral doses: measure liquid medicine (oral solution) with a special dose-measuring spoon or cup, not a regular table spoon.

**L27.1** `Simple Sentence` (0.75) → `passthrough`
- original: If you do not have a dose-measuring device, ask your pharmacist for one.

**L28.0** `Compound Sentence` (0.36) → `decomposed`
- original: Call your doctor if your symptoms do not improve, if they get worse, or if you also have a fever.
- pronoun resolved: Call your doctor if your symptoms do not improve, if symptoms get worse, or if you also have a fever.
  - edits: “they” → “symptoms”
  - S1: Call your doctor if your symptoms do not improve.
  - S2: Call your doctor if symptoms get worse.
  - S3: Call your doctor if you also have a fever.

**L28.1** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Store cetirizine at room temperature away from moisture and heat.

## What happens if I miss a dose?

**L31.0** `Incomplete Sentence` (0.926) → `excluded_incomplete`
- original: Take the missed dose as soon as you remember.

**L31.1** `Compound Sentence` (0.503) → `decomposed`
- original: If it is almost time for your next dose, wait until then to take the medicine and skip the missed dose.
- pronoun resolved: If it is almost time for your next dose, wait until then to take Cetirizine and skip the missed dose.
  - edits: “the medicine” → “Cetirizine”
  - S1: If it is almost time for your next dose, wait until then to take Cetirizine.
  - S2: Skip the missed dose.

**L31.2** `Incomplete Sentence` (0.849) → `excluded_incomplete`
- original: Do not take extra medicine or add extra doses to make up the missed dose.

## What happens if I overdose?

**L34.0** `Incomplete Sentence` (0.954) → `excluded_incomplete`
- original: Seek emergency medical attention if you think you have used too much of this medicine.

**L35.0** `Simple Sentence` (0.436) → `passthrough`
- original: Overdose symptoms may include feeling restless or nervous, and then feeling drowsy.

## What should I avoid?

**L38.0** `Compound Sentence` (0.28) → `decomposed`
- original: Tell your doctor if you regularly use other medicines that make you sleepy (such as other cold or allergy medicine, narcotic pain medicine, sleeping pills, muscle relaxers, and medicine for seizures, depression, or anxiety).
  - S1: Tell your doctor if you regularly use other medicines that make you sleepy.
  - S2: Examples of such medicines include other cold or allergy medicine, narcotic pain medicine, sleeping pills, muscle relaxers, and medicine for seizures, depression, or anxiety.

**L38.1** `Simple Sentence` (0.991) → `passthrough`
- original: They can add to sleepiness caused by cetirizine.
- pronoun resolved: Other medicines can add to sleepiness caused by cetirizine.
  - edits: “They” → “Other medicines”

**L39.0** `Simple Sentence` (0.988) → `passthrough`
- original: Cetirizine can cause side effects that may impair your thinking or reactions.

**L39.1** `Incomplete Sentence` (0.686) → `excluded_incomplete`
- original: Be careful if you drive or do anything that requires you to be awake and alert.

**L40.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Avoid drinking alcohol.

**L40.1** `Simple Sentence` (0.989) → `passthrough`
- original: It can increase some of the side effects of cetirizine.
- pronoun resolved: Alcohol can increase some of the side effects of cetirizine.
  - edits: “It” → “Alcohol”

## Cetirizine acute and common side effects

**L43.0** `Compound Sentence` (0.406) → `decomposed`
- original: Get emergency medical help if you have any serious adverse effects or any of these signs of an allergic reaction: chronic idiopathic urticaria (hives); difficulty breathing; swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have any serious adverse effects.
  - S2: Get emergency medical help if you have any of these signs of an allergic reaction.
  - S3: These signs include chronic idiopathic urticaria (hives).
  - S4: These signs include difficulty breathing.
  - S5: These signs include swelling of your face, lips, tongue, or throat.

**L43.1** `Simple Sentence` (0.494) → `passthrough`
- original: Stop using cetirizine and call your doctor at once if you have any of these serious side effects:

**L44.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: fast, pounding, or uneven heartbeat;

**L45.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: weakness, tremors (uncontrolled shaking), or sleep problems (insomnia);

**L46.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: severe restless feeling, hyperactivity;

**L47.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: confusion;

**L48.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: problems with vision; or

**L49.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: urinating less than usual or not at all.

**L50.0** `Simple Sentence` (0.937) → `passthrough`
- original: Less serious cetirizine side effects may include:

**L51.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: dizziness, drowsiness;

**L52.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: tired feeling;

**L53.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: dry mouth;

**L54.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: sore throat, cough;

**L55.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: nausea, constipation; or

**L56.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: headache.

**L57.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L57.1** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Tell your doctor about any unusual or bothersome side effect.

## What other drugs will affect cetirizine?

**L60.0** `Simple Sentence` (0.989) → `passthrough`
- original: There may be other drugs that can interact with cetirizine.

**L60.1** `Incomplete Sentence` (0.891) → `excluded_incomplete`
- original: Tell your doctor about all your prescription and over-the-counter medications, vitamins, minerals, herbal products, and drugs prescribed by other doctors.

**L60.2** `Incomplete Sentence` (0.522) → `excluded_incomplete`
- original: Do not start a new medication without telling your doctor.

## Popular FAQ

**L63.0** `Simple Sentence` (0.923) → `passthrough`
- original: Q: Can you take Benadryl and cetirizine together?

**L63.1** `Complex Sentence` (0.836) → `decomposed`
- original: A: Benadryl should not be taken at the same time as cetirizine because it can increase side effects such as dizziness, drowsiness, and difficulty concentrating.
- pronoun resolved: A: Benadryl should not be taken at the same time as cetirizine because cetirizine can increase side effects such as dizziness, drowsiness, and difficulty concentrating.
  - edits: “it” → “cetirizine”
  - S1: Benadryl should not be taken at the same time as cetirizine.
  - S2: Cetirizine can increase side effects.
  - S3: These side effects include dizziness, drowsiness, and difficulty concentrating.

**L63.2** `Complex Sentence` (0.607) → `decomposed`
- original: Some people, especially the elderly or children, may also find their thinking, judgement, and coordination impaired.
  - S1: Some people may find their thinking, judgement, and coordination impaired.
  - S2: The elderly may find their thinking, judgement, and coordination impaired.
  - S3: Children may find their thinking, judgement, and coordination impaired.

**L63.3** `Complex Sentence` (0.645) → `decomposed`
- original: You should also not drink alcohol while taking either of these medications because it can make these side effects worse.
- pronoun resolved: You should also not drink alcohol while taking either of Benadryl because it can make these side effects worse.
  - edits: “these medications” → “Benadryl”
  - S1: You should not drink alcohol while taking Benadryl.
  - S2: You should not drink alcohol while taking either of the medications.
  - S3: Drinking alcohol can make the side effects worse.

**L64.0** `Simple Sentence` (0.516) → `passthrough`
- original: Q: Can cetirizine raise blood pressure?

**L64.1** `Compound Sentence` (0.915) → `decomposed`
- original: A: Cetirizine does not increase blood pressure and blood pressure is not listed as a side effect in the product information.
  - S1: Cetirizine does not increase blood pressure.
  - S2: Blood pressure is not listed as a side effect in the product information.

**L64.2** `Compound Sentence` (0.868) → `decomposed`
- original: But cetirizine can be found in combination with other medications, such as pseudoephedrine in products such as Zyrtec-D, and pseudoephedrine does increase blood pressure.
  - S1: But cetirizine can be found in combination with other medications.
  - S2: Such medications include pseudoephedrine in products such as Zyrtec-D.
  - S3: Pseudoephedrine does increase blood pressure.

**L65.0** `Simple Sentence` (0.8) → `passthrough`
- original: Q: Is it OK to take antihistamines every day?
- pronoun resolved: Q: Is cetirizine OK to take antihistamines every day?
  - edits: “it” → “cetirizine”

**L65.1** `Compound Sentence` (0.423) → `decomposed`
- original: A: Yes, most people can take antihistamines every day, if they have daily symptoms of their allergies.
- pronoun resolved: A: Yes, most people can take antihistamines every day, if people have daily symptoms of people's allergies.
  - edits: “they” → “people”; “their” → “people's”
  - S1: Yes, most people can take antihistamines every day.
  - S2: This is possible if people have daily symptoms of allergies.

**L65.2** `Complex Sentence` (0.476) → `decomposed`
- original: If you have chronic allergies with daily symptoms, you may take a daily antihistamine.
  - S1: You may take a daily antihistamine.
  - S2: This applies if you have chronic allergies with daily symptoms.

**L66.0** `Incomplete Sentence` (0.937) → `excluded_incomplete`
- original: Q: Should cetirizine be taken at bedtime or upon awakening?

**L66.1** `Simple Sentence` (0.982) → `passthrough`
- original: A: Cetirizine can be taken at any time of day.

**L66.2** `Compound Sentence` (0.84) → `decomposed`
- original: Most people do not feel drowsy when taking cetirizine, so they often take it in the morning.
- pronoun resolved: Most people do not feel drowsy when taking cetirizine, so they often take cetirizine in the morning.
  - edits: “it” → “cetirizine”
  - S1: Most people do not feel drowsy when taking cetirizine.
  - S2: Therefore, they often take cetirizine in the morning.

**L66.3** `Simple Sentence` (0.956) → `passthrough`
- original: However, a small number of people do experience sedation.

**L66.4** `Simple Sentence` (0.625) → `passthrough`
- original: If cetirizine makes you feel drowsy, it is best to take it in the evening.
- pronoun resolved: If cetirizine makes you feel drowsy, it is best to take cetirizine in the evening.
  - edits: “it” → “cetirizine”

**L67.0** `Incomplete Sentence` (0.916) → `excluded_incomplete`
- original: Q: Which antihistamines make you drowsy?

**L67.1** `Complex Sentence` (0.743) → `decomposed`
- original: A: First-generation antihistamines, like Benadryl (diphenhydramine) and Chlor-Trimeton (chlorpheniramine), often cause sedation.
  - S1: First-generation antihistamines often cause sedation.
  - S2: Benadryl (diphenhydramine) is a first-generation antihistamine.
  - S3: Chlor-Trimeton (chlorpheniramine) is a first-generation antihistamine.

**L67.2** `Simple Sentence` (0.957) → `passthrough`
- original: This can include drowsiness, fatigue, and reduced alertness or concentration.
- pronoun resolved: First-generation antihistamines can include drowsiness, fatigue, and reduced alertness or concentration.
  - edits: “This” → “First-generation antihistamines”

**L68.0** `Incomplete Sentence` (0.651) → `excluded_incomplete`
- original: Q: Can you take antihistamines when pregnant?

**L68.1** `Complex Sentence` (0.815) → `decomposed`
- original: A: According to the American College of Obstetricians and Gynecologists (ACOG), several over-the-counter (OTC) antihistamines may be taken during pregnancy.
  - S1: According to the American College of Obstetricians and Gynecologists (ACOG), several over-the-counter (OTC) antihistamines may be taken during pregnancy.

**L68.2** `Compound Sentence` (0.949) → `decomposed`
- original: Older, first-generation antihistamines can be taken, but they may cause drowsiness.
- pronoun resolved: Older, first-generation antihistamines can be taken, but antihistamines may cause drowsiness.
  - edits: “they” → “antihistamines”
  - S1: Older, first-generation antihistamines can be taken.
  - S2: Antihistamines may cause drowsiness.

**L68.3** `Compound Sentence` (0.596) → `decomposed`
- original: Newer, second-generation antihistamines can also be taken and have less risk of drowsiness.
  - S1: Newer, second-generation antihistamines can also be taken.
  - S2: They have less risk of drowsiness.

**L69.0** `Incomplete Sentence` (0.929) → `excluded_incomplete`
- original: Q: How long does it take for cetirizine to work?

**L69.1** `Simple Sentence` (0.444) → `passthrough`
- original: A: Cetirizine is an allergy medicine that usually starts to work within about 20 to 60 minutes after you take it.

**L69.2** `Compound Sentence` (0.481) → `decomposed`
- original: Many people notice less sneezing and itching within the first hour, especially if they take it on an empty stomach.
- pronoun resolved: Many people notice less sneezing and itching within the first hour, especially if they take cetirizine on an empty stomach.
  - edits: “it” → “cetirizine”
  - S1: Many people notice less sneezing and itching within the first hour.
  - S2: This effect is especially noticeable if they take cetirizine on an empty stomach.

**L69.3** `Compound Sentence` (0.953) → `decomposed`
- original: One dose of cetirizine generally provides relief for up to 24 hours, so most people only need to take it once a day.
- pronoun resolved: One dose of cetirizine generally provides relief for up to 24 hours, so most people only need to take cetirizine once a day.
  - edits: “it” → “cetirizine”
  - S1: One dose of cetirizine generally provides relief for up to 24 hours.
  - S2: Most people only need to take cetirizine once a day.

**L70.0** `Incomplete Sentence` (0.507) → `excluded_incomplete`
- original: Q: Does cetirizine make you drowsy?

**L70.1** `Compound Sentence` (0.96) → `decomposed`
- original: A: Cetirizine is considered a non-drowsy (second-generation) antihistamine, but it can still cause drowsiness in some people.
- pronoun resolved: A: Cetirizine is considered a non-drowsy (second-generation) antihistamine, but Cetirizine can still cause drowsiness in some people.
  - edits: “it” → “Cetirizine”
  - S1: Cetirizine is considered a non-drowsy (second-generation) antihistamine.
  - S2: Cetirizine can still cause drowsiness in some people.

**L70.2** `Simple Sentence` (0.922) → `passthrough`
- original: In clinical studies, the chance of feeling sleepy increased with higher doses.

**L71.0** `Incomplete Sentence` (0.565) → `excluded_incomplete`
- original: Q: How long after taking cetirizine can I drink alcohol?

**L71.1** `Complex Sentence` (0.833) → `decomposed`
- original: A: It is best to wait until cetirizine completely leaves your body before you drink alcohol, which may take up to 40 hours (almost 2 days).
  - S1: It is best to wait until cetirizine completely leaves your body before you drink alcohol.
  - S2: Cetirizine may take up to 40 hours to leave your body.
  - S3: This is almost 2 days.
