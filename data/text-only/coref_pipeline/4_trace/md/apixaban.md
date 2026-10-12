# Apixaban — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/apixaban.txt` · 96 sentences · 7 changed by pronoun resolution · 150 sentences sent to EDC

## What is apixaban?

**L5.0** `Complex Sentence` (0.77) → `decomposed`
- original: Apixaban is used to lower the risk of stroke and blood clots in adults with a heart rhythm disorder called atrial fibrillation not caused by a heart valve problem.
  - S1: Apixaban is used to lower the risk of stroke and blood clots.
  - S2: It is used in adults with a heart rhythm disorder called atrial fibrillation.
  - S3: The atrial fibrillation is not caused by a heart valve problem.

**L6.0** `Complex Sentence` (0.57) → `decomposed`
- original: Apixaban is also used in adults to treat blood clots in the legs (DVT) or lungs (PE) and to lower your risk of happening again after you have received treatment for blood clots.
  - S1: Apixaban is used in adults to treat blood clots in the legs (DVT) or lungs (PE).
  - S2: Apixaban is used to lower the risk of blood clots happening again.
  - S3: This risk reduction occurs after you have received treatment for blood clots.

**L7.0** `Complex Sentence` (0.902) → `decomposed`
- original: Apixaban is also used in adults after hip or knee replacement surgery to prevent clots that can occur in the legs (deep vein thrombosis, DVT) or in the lungs (pulmonary embolism, PE).
  - S1: Apixaban is used in adults after hip or knee replacement surgery.
  - S2: It is used to prevent clots that can occur in the legs or in the lungs.
  - S3: Clots in the legs are known as deep vein thrombosis (DVT).
  - S4: Clots in the lungs are known as pulmonary embolism (PE).

**L8.0** `Complex Sentence` (0.877) → `decomposed`
- original: Apixaban is also used in children from birth to less than 18 years of age to treat blood clots in the legs (DVT) or lungs (PE) and lower the risk of happening again after receiving treatment for at least 5 days.
  - S1: Apixaban is used in children from birth to less than 18 years of age.
  - S2: It is used to treat blood clots in the legs (DVT) or lungs (PE).
  - S3: It is used to lower the risk of clots happening again.
  - S4: This is done after receiving treatment for at least 5 days.

**L9.0** `Simple Sentence` (0.947) → `passthrough`
- original: Apixaban is not approved for use in children who weigh less than 5.7 pounds (2.6 kg).

**L10.0** `Simple Sentence` (0.984) → `passthrough`
- original: Apixaban may also be used for purposes not listed in this medication guide.

## Apixaban side effects

**L13.0** `Simple Sentence` (0.363) → `passthrough`
- original: Get emergency medical help if you have signs of an allergic reaction: hives, difficult breathing, swelling of your face, lips, tongue, or throat.

**L14.0** `Complex Sentence` (0.431) → `decomposed`
- original: Also seek emergency medical attention if you have symptoms of a spinal blood clot: back pain, numbness, tingling, muscle weakness in your lower body, or loss of bladder or bowel control.
  - S1: Also seek emergency medical attention if you have symptoms of a spinal blood clot.
  - S2: Symptoms of a spinal blood clot include back pain, numbness, tingling, muscle weakness in your lower body, or loss of bladder or bowel control.

**L15.0** `Simple Sentence` (0.982) → `passthrough`
- original: Apixaban can cause you to bleed more easily.

**L15.1** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Call your doctor at once if you have signs of bleeding such as:

**L16.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: bruising or bleeding that will not stop, unusual bleeding (nosebleeds, bleeding gums, vaginal bleeding);

**L17.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: unexpected pain, joint pain or swelling;

**L18.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: headache, dizziness, weakness, feeling like you might pass out;

**L19.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: urine that looks red, pink, or brown; or

**L20.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: bloody or tarry stools, coughing up blood or vomit that looks like coffee grounds.

**L21.0** `Simple Sentence` (0.949) → `passthrough`
- original: Common side effects of apixaban may include:

**L22.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: bleeding, including heavy menstrual bleeding; or

**L23.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: headache, vomiting.

**L24.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L24.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L24.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## Warnings

**L27.0** `Incomplete Sentence` (0.625) → `excluded_incomplete`
- original: Do not stop taking apixaban unless your doctor tells you to.

**L27.1** `Simple Sentence` (0.988) → `passthrough`
- original: Stopping suddenly can increase your risk of blood clot or stroke.

**L28.0** `Simple Sentence` (0.99) → `passthrough`
- original: Some drugs can increase your risk of bleeding when used with apixaban.

**L28.1** `Incomplete Sentence` (0.967) → `excluded_incomplete`
- original: Tell your doctor about all other medicines you use.

**L29.0** `Compound-Complex Sentence` (0.419) → `decomposed`
- original: Call your doctor at once if you have signs of bleeding such as: easy bruising, unusual bleeding, unexpected pain or swelling, feeling very weak or dizzy, bleeding gums, nosebleeds, heavy menstrual bleeding, blood in your urine or stools, coughing up blood or vomit that looks like coffee grounds, or any bleeding that will not stop.
  - S1: Call your doctor at once if you have signs of bleeding.
  - S2: Easy bruising is a sign of bleeding.
  - S3: Unusual bleeding is a sign of bleeding.
  - S4: Unexpected pain is a sign of bleeding.
  - S5: Unexpected swelling is a sign of bleeding.
  - S6: Feeling very weak is a sign of bleeding.
  - S7: Feeling dizzy is a sign of bleeding.
  - S8: Bleeding gums are a sign of bleeding.
  - S9: Nosebleeds are a sign of bleeding.
  - S10: Heavy menstrual bleeding is a sign of bleeding.
  - S11: Blood in your urine is a sign of bleeding.
  - S12: Blood in your stools is a sign of bleeding.
  - S13: Coughing up blood is a sign of bleeding.
  - S14: Vomit that looks like coffee grounds is a sign of bleeding.
  - S15: Any bleeding that will not stop is a sign of bleeding.

**L30.0** `Complex Sentence` (0.489) → `decomposed`
- original: Apixaban can cause a very serious blood clot around your spinal cord if you undergo a spinal tap or receive spinal anesthesia (epidural).
  - S1: Apixaban can cause a very serious blood clot around your spinal cord.
  - S2: This can happen if you undergo a spinal tap.
  - S3: This can also happen if you receive spinal anesthesia (epidural).

**L30.1** `Incomplete Sentence` (0.891) → `excluded_incomplete`
- original: Tell any doctor who treats you that you are taking apixaban.

## Before taking this medicine

**L33.0** `Simple Sentence` (0.819) → `passthrough`
- original: You should not take apixaban if you are allergic to it or if you have active bleeding from any cause.
- pronoun resolved: You should not take apixaban if you are allergic to apixaban or if you have active bleeding from any cause.
  - edits: “it” → “apixaban”

**L34.0** `Complex Sentence` (0.372) → `decomposed`
- original: Apixaban can cause a serious blood clot if you undergo a procedure such as a spinal tap or receive spinal anesthesia (epidural).
  - S1: Apixaban can cause a serious blood clot.
  - S2: This can happen if you undergo a procedure.
  - S3: The procedure could be a spinal tap.
  - S4: The procedure could be receiving spinal anesthesia.
  - S5: Spinal anesthesia is also known as epidural.

**L34.1** `Simple Sentence` (0.989) → `passthrough`
- original: This type of blood clot could cause permanent or long-term paralysis.

**L35.0** `Simple Sentence` (0.974) → `passthrough`
- original: Apixaban can make it easier for you to bleed, even from a minor injury.

**L35.1** `Incomplete Sentence` (0.811) → `excluded_incomplete`
- original: Call your doctor if you have any bleeding that will not stop.

**L36.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Tell your doctor if you have or have ever had:

**L37.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: artificial heart valve;

**L38.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: a history of problems with your spine, a spinal surgery, or difficult or repeated spinal taps;

**L39.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: bleeding problems;

**L40.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: plan for surgery, or a medical or a dental procedure;

**L41.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: a thin tube (catheter) placed in your back to give you certain medicine;

**L42.0** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: antiphospholipid syndrome, an immune system disorder that increases the risk of blood clots; or

**L43.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: liver or kidney disease.

**L44.0** `Simple Sentence` (0.984) → `passthrough`
- original: It is not known if apixaban will harm an unborn baby.

**L44.1** `Simple Sentence` (0.979) → `passthrough`
- original: Taking apixaban during pregnancy may cause bleeding in the mother or the unborn baby.

**L44.2** `Incomplete Sentence` (0.915) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or plan to become pregnant.

**L45.0** `Incomplete Sentence` (0.816) → `excluded_incomplete`
- original: Do not breastfeed while taking apixaban.

## How should I take apixaban?

**L48.0** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L48.1** `Simple Sentence` (0.984) → `passthrough`
- original: Your doctor may occasionally change your dose.

**L48.2** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Use the medicine exactly as directed.
- pronoun resolved: Use Apixaban exactly as directed.
  - edits: “the medicine” → “Apixaban”

**L49.0** `Simple Sentence` (0.989) → `passthrough`
- original: Apixaban is usually taken twice per day.

**L50.0** `Incomplete Sentence` (0.96) → `excluded_incomplete`
- original: Read and carefully follow any Instructions for Use provided with your medicine.

**L50.1** `Complex Sentence` (0.655) → `decomposed`
- original: If you cannot swallow a tablet whole, you may crush it and mix the medicine with a small amount of applesauce, apple juice, or water.
  - S1: If you cannot swallow a tablet whole, you may crush it.
  - S2: You may mix the medicine with a small amount of applesauce, apple juice, or water.

**L51.0** `Complex Sentence` (0.883) → `decomposed`
- original: If your child is prescribed the tablets for oral suspension, it should be mixed with water, infant formula, apple juice, or apple sauce.
  - S1: If your child is prescribed the tablets for oral suspension, it should be mixed with water.
  - S2: It should be mixed with infant formula.
  - S3: It should be mixed with apple juice.
  - S4: It should be mixed with apple sauce.

**L51.1** `Incomplete Sentence` (0.952) → `excluded_incomplete`
- original: Do not swallow the tablet.

**L52.0** `Complex Sentence` (0.842) → `decomposed`
- original: If your child is taking capsules for oral suspension, the capsule should be opened and mixed with water or infant formula only.
  - S1: If your child is taking capsules for oral suspension, the capsule should be opened.
  - S2: The capsule should be mixed with water or infant formula only.

**L52.1** `Incomplete Sentence` (0.951) → `excluded_incomplete`
- original: Do not swallow the capsule.

**L53.0** `Simple Sentence` (0.985) → `passthrough`
- original: Mixed medicine should be used right away.

**L53.1** `Simple Sentence` (0.987) → `passthrough`
- original: Apixaban may also be given through a feeding tube.

**L54.0** `Compound Sentence` (0.535) → `decomposed`
- original: apixaban can also make it easier for you to bleed, even from a minor injury such as a fall or a bump on the head.
  - S1: Apixaban can make it easier for you to bleed.
  - S2: This can happen even from a minor injury such as a fall or a bump on the head.

**L54.1** `Compound Sentence` (0.375) → `decomposed`
- original: Tell your doctor or seek emergency medical attention if you fall or hit your head, or have any bleeding that will not stop.
  - S1: Tell your doctor or seek emergency medical attention if you fall or hit your head.
  - S2: Tell your doctor or seek emergency medical attention if you have any bleeding that will not stop.

**L55.0** `Complex Sentence` (0.553) → `decomposed`
- original: If you have a planned surgery or dental procedure, your doctor may tell you to stop taking apixaban for a short time.
  - S1: If you have a planned surgery or dental procedure, your doctor may tell you to stop taking apixaban.
  - S2: Your doctor may tell you to stop taking apixaban for a short time.
  - S3: You may need to stop taking apixaban for a short time before a planned surgery or dental procedure.

**L56.0** `Simple Sentence` (0.985) → `passthrough`
- original: Doses are based on weight in children and teenagers.

**L56.1** `Simple Sentence` (0.931) → `passthrough`
- original: Your child's dose may change if the child gains or loses weight.

**L57.0** `Simple Sentence` (0.931) → `passthrough`
- original: If your child vomits within 30 minutes after taking apixaban, take another dose.

**L57.1** `Complex Sentence` (0.659) → `decomposed`
- original: If the child vomits after more than 30 minutes of taking apixaban, do not take another dose and give the next dose as scheduled.
  - S1: If the child vomits after more than 30 minutes of taking apixaban.
  - S2: Do not take another dose.
  - S3: Give the next dose as scheduled.

**L58.0** `Simple Sentence` (0.483) → `passthrough`
- original: Do not change your dose or stop taking apixaban unless your doctor tells you to.

**L58.1** `Complex Sentence` (0.604) → `decomposed`
- original: If you stop taking apixaban for any reason, your doctor may prescribe another medicine to prevent blood clots.
  - S1: If you stop taking apixaban for any reason.
  - S2: Your doctor may prescribe another medicine.
  - S3: The medicine is to prevent blood clots.

**L58.2** `Incomplete Sentence` (0.971) → `excluded_incomplete`
- original: Keep all follow-up visits with your healthcare provider.

**L59.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Store at room temperature away from moisture and heat.

## What happens if I miss a dose?

**L62.0** `Incomplete Sentence` (0.86) → `excluded_incomplete`
- original: Take a missed dose as soon as you remember it on the same day.
- pronoun resolved: Take a missed dose as soon as you remember a missed dose on the same day.
  - edits: “it” → “a missed dose”

**L62.1** `Incomplete Sentence` (0.56) → `excluded_incomplete`
- original: Take your next dose at the regular time and stay on your twice-daily schedule.

**L62.2** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

**L63.0** `Incomplete Sentence` (0.913) → `excluded_incomplete`
- original: Get your prescription refilled before you run out of medicine completely.

## What happens if I overdose?

**L66.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

## What should I avoid while taking apixaban?

**L69.0** `Incomplete Sentence` (0.958) → `excluded_incomplete`
- original: Avoid activities that may increase your risk of bleeding or injury.

**L69.1** `Incomplete Sentence` (0.931) → `excluded_incomplete`
- original: Use extra care while shaving or brushing your teeth.

## What other drugs will affect apixaban?

**L72.0** `Simple Sentence` (0.978) → `passthrough`
- original: Sometimes it is not safe to use certain medicines at the same time.

**L72.1** `Complex Sentence` (0.909) → `decomposed`
- original: Some drugs can affect your blood levels of other drugs you use, which may increase side effects or make the medicines less effective.
  - S1: Some drugs can affect your blood levels of other drugs you use.
  - S2: This may increase side effects.
  - S3: This may make the medicines less effective.

**L73.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Tell your doctor about all your current medicines.

**L73.1** `Simple Sentence` (0.989) → `passthrough`
- original: Many drugs can affect apixaban, especially:

**L74.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: a blood thinner or any other medicines to treat or prevent blood clots such as enoxaparin, warfarin, heparin, clopidogrel, dipyridamole, prasugrel, and others;

**L75.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: an antidepressant; or

**L76.0** `Incomplete Sentence` (0.819) → `excluded_incomplete`
- original: NSAIDs (nonsteroidal anti-inflammatory drugs) --aspirin, ibuprofen (Advil, Motrin), naproxen (Aleve), celecoxib, diclofenac, indomethacin, meloxicam, and others.

**L77.0** `Simple Sentence` (0.772) → `passthrough`
- original: This list is not complete and many other drugs may affect apixaban.

**L77.1** `Incomplete Sentence` (0.491) → `excluded_incomplete`
- original: This includes prescription and over-the-counter medicines, vitamins, and herbal products.
- pronoun resolved: List includes prescription and over-the-counter medicines, vitamins, and herbal products.
  - edits: “This” → “List”

**L77.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.

## Popular FAQ

**L80.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Q: Xarelto vs Eliquis: How do they compare?
- pronoun resolved: Q: Xarelto vs Eliquis: How do Xarelto vs Eliquis compare?
  - edits: “they” → “Xarelto vs Eliquis”

**L80.1** `Complex Sentence` (0.709) → `decomposed`
- original: A: Xarelto (rivaroxaban) and Eliquis (apixaban) are novel anticoagulants that make blood less likely to clot (also called thinning the blood).
  - S1: Xarelto (rivaroxaban) and Eliquis (apixaban) are novel anticoagulants.
  - S2: These anticoagulants make blood less likely to clot.
  - S3: This process is also called thinning the blood.

**L80.2** `Compound Sentence` (0.939) → `decomposed`
- original: Both belong to the class of medicines known as factor Xa (FXa) inhibitors and they are two of the most popular blood thinners on the market.
  - S1: Both belong to the class of medicines known as factor Xa (FXa) inhibitors.
  - S2: They are two of the most popular blood thinners on the market.

**L80.3** `Compound Sentence` (0.651) → `decomposed`
- original: Either one may be used to reduce the risk of stroke or treat and prevent blood clots in conditions such as DVT.
  - S1: Either one may be used to reduce the risk of stroke.
  - S2: Either one may be used to treat and prevent blood clots in conditions such as DVT.

**L81.0** `Incomplete Sentence` (0.964) → `excluded_incomplete`
- original: Q: What medications are known to cause hair loss?

**L81.1** `Simple Sentence` (0.594) → `passthrough`
- original: A: Medication-induced hair loss represents a significant concern for patients across multiple therapeutic categories.

**L81.2** `Complex Sentence` (0.956) → `decomposed`
- original: While chemotherapy drugs are most commonly associated with severe hair loss, many commonly prescribed medications-including antibiotics, psychiatric drugs, cardiovascular agents, and hormonal therapies-can also cause this distressing side effect.
  - S1: Chemotherapy drugs are most commonly associated with severe hair loss.
  - S2: Many commonly prescribed medications can also cause this distressing side effect.
  - S3: These medications include antibiotics, psychiatric drugs, cardiovascular agents, and hormonal therapies.

**L82.0** `Incomplete Sentence` (0.494) → `excluded_incomplete`
- original: Q: How do you reverse bleeding with Xarelto?

**L82.1** `Simple Sentence` (0.436) → `passthrough`
- original: A: There is no longer an FDA-approved antidote for Xarelto (rivaroxaban) in the United States.

**L82.2** `Complex Sentence` (0.913) → `decomposed`
- original: Andexxa, the only approved reversal drug, was pulled from the U.S. market on December 22, 2025, after the FDA decided its risks outweighed its benefits.
- pronoun resolved: Andexxa, the only approved reversal drug, was pulled from the U.S. market on December 22, 2025, after the FDA decided Andexxa's risks outweighed Andexxa's benefits.
  - edits: “its” → “Andexxa's”; “its” → “Andexxa's”
  - S1: Andexxa was pulled from the U.S. market on December 22, 2025.
  - S2: Andexxa is the only approved reversal drug.
  - S3: The FDA decided Andexxa's risks outweighed Andexxa's benefits.

**L82.3** `Simple Sentence` (0.697) → `passthrough`
- original: For serious bleeding today, hospitals stop the drug, control the bleeding directly.
- pronoun resolved: For serious bleeding today, hospitals stop Andexxa, control the bleeding directly.
  - edits: “the drug,” → “Andexxa,”
