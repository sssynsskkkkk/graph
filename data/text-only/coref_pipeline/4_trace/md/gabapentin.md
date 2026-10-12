# Gabapentin — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/gabapentin.txt` · 234 sentences · 23 changed by pronoun resolution · 363 sentences sent to EDC

## What is gabapentin?

**L5.0** `Complex Sentence` (0.564) → `decomposed`
- original: Gabapentin is a prescription medicine used to treat partial seizures, nerve pain from shingles (postherpetic neuralgia), and restless legs syndrome (Horizant brand only).
  - S1: Gabapentin is a prescription medicine.
  - S2: Gabapentin is used to treat partial seizures.
  - S3: Gabapentin is used to treat nerve pain from shingles.
  - S4: Gabapentin is used to treat restless legs syndrome.
  - S5: The restless legs syndrome treatment is for the Horizant brand only.

**L5.1** `Compound Sentence` (0.614) → `decomposed`
- original: It may also be prescribed off-label for other conditions including diabetic nerve pain, anxiety, and fibromyalgia.
- pronoun resolved: Gabapentin may also be prescribed off-label for other conditions including diabetic nerve pain, anxiety, and fibromyalgia.
  - edits: “It” → “Gabapentin”
  - S1: Gabapentin may also be prescribed off-label for other conditions.
  - S2: These conditions include diabetic nerve pain, anxiety, and fibromyalgia.

**L5.2** `Simple Sentence` (0.798) → `passthrough`
- original: Gabapentin is thought to work by calming overactive nerve signals in the brain and nervous system.

**L5.3** `Simple Sentence` (0.973) → `passthrough`
- original: It is an anticonvulsant and nerve pain medication from the drug class gabapentinoids
- pronoun resolved: Gabapentin is an anticonvulsant and nerve pain medication from the drug class gabapentinoids
  - edits: “It” → “Gabapentin”

**L6.0** `Compound Sentence` (0.43) → `decomposed`
- original: Gabapentin brand names are Neurontin, Gralise, Horizant, and Relgaabi, which may not be interchangeable.
  - S1: Gabapentin brand names are Neurontin, Gralise, Horizant, and Relgaabi.
  - S2: These brand names may not be interchangeable.

**L7.0** `Compound-Complex Sentence` (0.878) → `decomposed`
- original: Gabapentin is not a federally controlled substance, but some states classify it as Schedule V and others require gabapentin prescriptions to be reported to their prescription drug monitoring program (PDMP).
- pronoun resolved: Gabapentin is not a federally controlled substance, but some states classify Gabapentin as Schedule V and others require gabapentin prescriptions to be reported to their prescription drug monitoring program (PDMP).
  - edits: “it” → “Gabapentin”
  - S1: Gabapentin is not a federally controlled substance.
  - S2: Some states classify Gabapentin as Schedule V.
  - S3: Other states require gabapentin prescriptions to be reported to their prescription drug monitoring program.
  - S4: This program is known as the PDMP.

**L7.1** `Simple Sentence` (0.953) → `passthrough`
- original: Rules on refills and quantity limits vary by state.

**L8.0** `Compound Sentence` (0.486) → `decomposed`
- original: The most common side effects of gabapentin are dizziness, drowsiness (somnolence), and swelling in the hands or feet (peripheral edema).
  - S1: The most common side effects of gabapentin are dizziness.
  - S2: They include drowsiness (somnolence).
  - S3: They also include swelling in the hands or feet (peripheral edema).

**L8.1** `Compound Sentence` (0.947) → `decomposed`
- original: These often improve as your body adjusts, but do not drive until you know how gabapentin affects you.
- pronoun resolved: Side effects often improve as your body adjusts, but do not drive until you know how gabapentin affects you.
  - edits: “These” → “Side effects”
  - S1: Side effects often improve as your body adjusts.
  - S2: Do not drive until you know how gabapentin affects you.

## What is gabapentin used for?

**L11.0** `Compound Sentence` (0.732) → `decomposed`
- original: Gabapentin is FDA-approved to treat partial onset seizures in patients 3 years and older (used with other seizure medicines) and nerve pain from shingles (postherpetic neuralgia) in adults.
  - S1: Gabapentin is FDA-approved to treat partial onset seizures in patients 3 years and older.
  - S2: It is used with other seizure medicines.
  - S3: Gabapentin is FDA-approved to treat nerve pain from shingles (postherpetic neuralgia) in adults.

**L11.1** `Compound Sentence` (0.508) → `decomposed`
- original: A related product, gabapentin enacarbil (Horizant), is approved for moderate to severe restless legs syndrome in adults.
  - S1: A related product, gabapentin enacarbil (Horizant), is approved for moderate to severe restless legs syndrome in adults.

**L12.0** `Compound Sentence` (0.968) → `decomposed`
- original: The approved uses depend on the specific product, and no single gabapentin product is approved for all of these conditions.
  - S1: The approved uses depend on the specific product.
  - S2: No single gabapentin product is approved for all of these conditions.

**L12.1** `Simple Sentence` (0.661) → `passthrough`
- original: See the table below for a breakdown by brand.

## Gabapentin off-label uses

**L15.0** `Compound Sentence` (0.866) → `decomposed`
- original: Doctors also prescribe gabapentin off-label for other types of nerve pain, including diabetic nerve pain (diabetic neuropathy), and for anxiety, fibromyalgia, hot flashes, and alcohol withdrawal.
  - S1: Doctors also prescribe gabapentin off-label for other types of nerve pain.
  - S2: This includes diabetic nerve pain (diabetic neuropathy).
  - S3: Doctors also prescribe it for anxiety.
  - S4: They prescribe it for fibromyalgia.
  - S5: They prescribe it for hot flashes.
  - S6: They prescribe it for alcohol withdrawal.

**L15.1** `Simple Sentence` (0.545) → `passthrough`
- original: Off-label means that the condition it is being prescribed for is not an FDA-approved indication.
- pronoun resolved: Off-label means that the condition Gabapentin is being prescribed for is not an FDA-approved indication.
  - edits: “it” → “Gabapentin”

## Are gabapentin brands interchangeable?

**L18.0** `Compound Sentence` (0.964) → `decomposed`
- original: Different brands of gabapentin are not interchangeable, and they are FDA-approved for different conditions.
- pronoun resolved: Different brands of gabapentin are not interchangeable, and Different brands of gabapentin are FDA-approved for different conditions.
  - edits: “they” → “Different brands of gabapentin”
  - S1: Different brands of gabapentin are not interchangeable.
  - S2: Different brands of gabapentin are FDA-approved for different conditions.

**L18.1** `Incomplete Sentence` (0.966) → `excluded_incomplete`
- original: Use only the brand and form of gabapentin your doctor has prescribed.

**L18.2** `Incomplete Sentence` (0.879) → `excluded_incomplete`
- original: Check your medicine each time you get a refill to make sure you receive the correct form.

**L19.0** `Compound Sentence` (0.422) → `decomposed`
- original: Important: Gralise and Horizant are not substitutes for Neurontin or generic gabapentin, even at the same milligram dose.
  - S1: Gralise and Horizant are not substitutes for Neurontin or generic gabapentin.
  - S2: This is true even at the same milligram dose.

**L19.1** `Compound Sentence` (0.955) → `decomposed`
- original: The release profile differs, and switching without a prescriber's instruction can significantly change blood levels.
  - S1: The release profile differs.
  - S2: Switching without a prescriber's instruction can significantly change blood levels.

**L20.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Brand (form) | Partial onset seizures (add-on) | Postherpetic neuralgia | Restless legs syndrome

**L21.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Neurontin (immediate-release capsule, tablet, oral solution) | Adults and children 3 years and older | Adults | Not approved

**L22.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Generic gabapentin (immediate-release) | Adults and children 3 years and older | Adults | Not approved

**L23.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Relgaabi (immediate-release capsule) | Adults and children 3 years and older | Adults | Not approved

**L24.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Gralise (once-daily extended-release tablet) | Not approved | Adults | Not approved

**L25.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Horizant (gabapentin enacarbil, extended-release tablet) | Not approved | Adults | Adults (moderate to severe primary RLS)

**L26.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: Sources: FDA prescribing information for Neurontin, Gralise, and Horizant; Relgaabi prescribing information (DailyMed)

## How does gabapentin work?

**L29.0** `Simple Sentence` (0.982) → `passthrough`
- original: Gabapentin works by calming overactive electrical signals in the brain and nervous system.

**L29.1** `Complex Sentence` (0.865) → `decomposed`
- original: It does this by binding to the alpha-2-delta subunit of calcium channels in nerve cells, which is thought to normalize chemical signals nerves send to each other and results in a calmer, less excitable nerve circuit.
- pronoun resolved: Gabapentin does this by binding to the alpha-2-delta subunit of calcium channels in nerve cells, which is thought to normalize chemical signals nerves send to each other and results in a calmer, less excitable nerve circuit.
  - edits: “It” → “Gabapentin”
  - S1: Gabapentin does this by binding to the alpha-2-delta subunit of calcium channels in nerve cells.
  - S2: This subunit is thought to normalize chemical signals nerves send to each other.
  - S3: This results in a calmer, less excitable nerve circuit.

**L30.0** `Simple Sentence` (0.979) → `passthrough`
- original: That same effect helps in different ways depending on what gabapentin is treating:

**L31.0** `Simple Sentence` (0.94) → `passthrough`
- original: Epilepsy - dampens the runaway electrical firing that causes seizures.

**L32.0** `Simple Sentence` (0.632) → `passthrough`
- original: Postherpetic neuralgia (shingles nerve pain) - reduces the abnormal pain signals from nerves damaged by shingles.

**L33.0** `Compound Sentence` (0.498) → `decomposed`
- original: Restless legs syndrome (gabapentin enacarbil / Horizant) - the exact mechanism is less clear, but the same calming effect on overactive nerves is thought to ease the urge-to-move sensation.
  - S1: Restless legs syndrome (gabapentin enacarbil / Horizant) has an exact mechanism that is less clear.
  - S2: The same calming effect on overactive nerves is thought to ease the urge-to-move sensation.

**L34.0** `Simple Sentence` (0.953) → `passthrough`
- original: Gabapentin is not an opioid, sedative, or anti-inflammatory painkiller.

**L34.1** `Compound-Complex Sentence` (0.853) → `decomposed`
- original: It works directly on the nerves, which is why it helps nerve-related pain and why it isn't useful for everyday pain like headaches or sprains.
- pronoun resolved: Gabapentin works directly on the nerves, which is why Gabapentin helps nerve-related pain and why Gabapentin isn't useful for everyday pain like headaches or sprains.
  - edits: “It” → “Gabapentin”; “it” → “Gabapentin”; “it” → “Gabapentin”
  - S1: Gabapentin works directly on the nerves.
  - S2: Gabapentin helps nerve-related pain.
  - S3: Gabapentin isn't useful for everyday pain like headaches or sprains.

**L34.2** `Simple Sentence` (0.959) → `passthrough`
- original: Most people need 1 to 2 weeks of regular dosing for the full effect to build up.

## How long does it take for gabapentin to work?

**L37.0** `Compound Sentence` (0.962) → `decomposed`
- original: Gabapentin can start working for pain after 1 week in some people, but usually takes several weeks to reach its full effect.
- pronoun resolved: Gabapentin can start working for pain after 1 week in some people, but usually takes several weeks to reach Gabapentin's full effect.
  - edits: “its” → “Gabapentin's”
  - S1: Gabapentin can start working for pain after 1 week in some people.
  - S2: It usually takes several weeks to reach Gabapentin's full effect.

**L37.1** `Compound Sentence` (0.861) → `decomposed`
- original: It works differently than other pain medicines, so you need to take it regularly over several weeks for the full pain-relieving effect to develop.
- pronoun resolved: Gabapentin works differently than other pain medicines, so you need to take Gabapentin regularly over several weeks for the full pain-relieving effect to develop.
  - edits: “It” → “Gabapentin”; “it” → “Gabapentin”
  - S1: Gabapentin works differently than other pain medicines.
  - S2: You need to take Gabapentin regularly over several weeks for the full pain-relieving effect to develop.

## Warnings

**L40.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Respiratory depression.

**L40.1** `Compound-Complex Sentence` (0.786) → `decomposed`
- original: Gabapentin can cause life-threatening breathing problems (respiratory depression), especially if you already have a breathing disorder (such as COPD), are elderly, or if you use other medicines that can make you drowsy or slow your breathing, such as opioids or CNS depressants.
  - S1: Gabapentin can cause life-threatening breathing problems.
  - S2: These breathing problems are called respiratory depression.
  - S3: Respiratory depression is especially likely if you already have a breathing disorder.
  - S4: COPD is an example of a breathing disorder.
  - S5: Respiratory depression is especially likely if you are elderly.
  - S6: Respiratory depression is especially likely if you use other medicines that can make you drowsy or slow your breathing.
  - S7: Opioids are examples of medicines that can make you drowsy or slow your breathing.
  - S8: CNS depressants are examples of medicines that can make you drowsy or slow your breathing.

**L40.2** `Incomplete Sentence` (0.955) → `excluded_incomplete`
- original: Seek emergency medical attention if you have very slow breathing.

**L41.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Suicidal thoughts or behaviors.

**L41.1** `Simple Sentence` (0.972) → `passthrough`
- original: Some people have thoughts about suicide while taking and after discontinuing this medicine.
- pronoun resolved: Some people have thoughts about suicide while taking and after discontinuing Gabapentin.
  - edits: “this medicine.” → “Gabapentin.”

**L41.2** `Incomplete Sentence` (0.9) → `excluded_incomplete`
- original: Stay alert to changes in your mood or symptoms.

**L41.3** `Incomplete Sentence` (0.732) → `excluded_incomplete`
- original: Tell your doctor right away if you have any sudden changes in mood or behavior, or thoughts about suicide.

**L42.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Abrupt or rapid discontinuation.

**L42.1** `Simple Sentence` (0.986) → `passthrough`
- original: Seizures may occur if you stop using gabapentin suddenly.

**L42.2** `Incomplete Sentence` (0.714) → `excluded_incomplete`
- original: Ask your doctor before stopping the medicine.
- pronoun resolved: Ask your doctor before stopping Gabapentin.
  - edits: “the medicine.” → “Gabapentin.”

**L42.3** `Simple Sentence` (0.881) → `passthrough`
- original: Stopping abruptly can cause withdrawal symptoms such as anxiety, trouble sleeping, nausea, pain, and sweating.

**L43.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Sleepiness, sedation, and dizziness.

**L43.1** `Incomplete Sentence` (0.937) → `excluded_incomplete`
- original: Avoid driving or participating in hazardous activities until you know how gabapentin will affect you.

**L43.2** `Simple Sentence` (0.961) → `passthrough`
- original: Dizziness or drowsiness can cause falls, accidents, or severe injuries.

**L44.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Brand substitution.

**L44.1** `Simple Sentence` (0.986) → `passthrough`
- original: Brands of gabapentin may not be interchangeable.

## Gabapentin side effects

**L47.0** `Compound Sentence` (0.536) → `decomposed`
- original: The most common side effects of gabapentin are dizziness, drowsiness (somnolence), swelling in the hands or feet (peripheral edema), and tiredness.
  - S1: The most common side effects of gabapentin are dizziness.
  - S2: They include drowsiness (somnolence).
  - S3: They include swelling in the hands or feet (peripheral edema).
  - S4: They include tiredness.

**L48.0** `Simple Sentence` (0.925) → `passthrough`
- original: Other common gabapentin side effects may include:

**L49.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: unsteadiness, poor coordination, or jerky movements

**L50.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: nausea or vomiting

**L51.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: headache

**L52.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: trouble speaking

**L53.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: blurred or double vision

**L54.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: tremor

**L55.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: signs of infection such as fever, chills, or sore throat

**L56.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious side effects:

**L57.0** `Compound Sentence` (0.406) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to gabapentin: hives, difficult breathing, or swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to gabapentin.
  - S2: These signs include hives.
  - S3: These signs include difficult breathing.
  - S4: These signs include swelling of your face, lips, tongue, or throat.

**L58.0** `Incomplete Sentence` (0.953) → `excluded_incomplete`
- original: Seek medical treatment if you have a serious drug reaction that can affect many parts of your body.

**L58.1** `Simple Sentence` (0.476) → `passthrough`
- original: Symptoms may include skin rash, fever, swollen glands, muscle aches, severe weakness, unusual bruising, or yellowing of your skin or eyes.

**L59.0** `Compound-Complex Sentence` (0.61) → `decomposed`
- original: Tell your doctor right away if you have new or sudden changes in mood or behavior, including new or worse depression or anxiety, panic attacks, trouble sleeping, or if you feel impulsive, irritable, agitated, hostile, aggressive, restless, more active or talkative, or have thoughts about suicide or hurting yourself, while taking this medicine and after stopping it.
- pronoun resolved: Tell your doctor right away if you have new or sudden changes in mood or behavior, including new or worse depression or anxiety, panic attacks, trouble sleeping, or if you feel impulsive, irritable, agitated, hostile, aggressive, restless, more active or talkative, or have thoughts about suicide or hurting yourself, while taking Gabapentin and after stopping it.
  - edits: “this medicine” → “Gabapentin”
  - S1: Tell your doctor right away if you have new or sudden changes in mood or behavior.
  - S2: New or sudden changes in mood or behavior include new or worse depression or anxiety.
  - S3: New or sudden changes in mood or behavior include panic attacks.
  - S4: New or sudden changes in mood or behavior include trouble sleeping.
  - S5: New or sudden changes in mood or behavior include feeling impulsive, irritable, agitated, hostile, aggressive, restless, more active, or talkative.
  - S6: New or sudden changes in mood or behavior include thoughts about suicide or hurting yourself.
  - S7: These changes may occur while taking Gabapentin.
  - S8: These changes may occur after stopping Gabapentin.

**L60.0** `Simple Sentence` (0.797) → `passthrough`
- original: Gabapentin can slow or stop your breathing, especially if you have recently used an opioid medicine or alcohol.

**L60.1** `Complex Sentence` (0.522) → `decomposed`
- original: A person caring for you should seek emergency medical attention if you have slow breathing with long pauses, blue-colored lips, or if you are hard to wake up.
  - S1: A person caring for you should seek emergency medical attention.
  - S2: You should seek attention if you have slow breathing with long pauses.
  - S3: You should seek attention if you have blue-colored lips.
  - S4: You should seek attention if you are hard to wake up.

**L61.0** `Simple Sentence` (0.989) → `passthrough`
- original: Some side effects are more likely in children taking gabapentin.

**L61.1** `Incomplete Sentence` (0.476) → `excluded_incomplete`
- original: Call your doctor if the child has behavior changes, memory problems, trouble concentrating, or is restless, hostile, or aggressive.

**L62.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L63.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: drowsiness, dizziness, or weakness

**L64.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: problems with balance or muscle movement

**L65.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: increased seizures

**L66.0** `Compound Sentence` (0.545) → `decomposed`
- original: This is not a complete list of side effects, and others may occur.
  - S1: This is not a complete list of side effects.
  - S2: Others may occur.

**L66.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L66.2** `Simple Sentence` (0.97) → `passthrough`
- original: You may report side effects to the FDA at 1-800-FDA-1088.

## Does gabapentin cause weight gain?

**L69.0** `Compound Sentence` (0.711) → `decomposed`
- original: Gabapentin can cause weight gain, although it is not common.
- pronoun resolved: Gabapentin can cause weight gain, although Gabapentin is not common.
  - edits: “it” → “Gabapentin”
  - S1: Gabapentin can cause weight gain.
  - S2: Gabapentin is not common.

**L69.1** `Simple Sentence` (0.969) → `passthrough`
- original: In clinical trials, a small number of people (roughly 2 in 100) gained weight while taking it.
- pronoun resolved: In clinical trials, a small number of people (roughly 2 in 100) gained weight while taking Gabapentin.
  - edits: “it.” → “Gabapentin.”

**L69.2** `Complex Sentence` (0.638) → `decomposed`
- original: Gabapentin can also cause swelling in the legs, feet, or hands (peripheral edema), which may add to weight changes and becomes more common with age.
  - S1: Gabapentin can also cause swelling in the legs, feet, or hands.
  - S2: This swelling is known as peripheral edema.
  - S3: The swelling may add to weight changes.
  - S4: The swelling becomes more common with age.

## Before taking this medicine

**L72.0** `Simple Sentence` (0.987) → `passthrough`
- original: You should not take gabapentin if you are allergic to it.
- pronoun resolved: You should not take gabapentin if you are allergic to Gabapentin.
  - edits: “it.” → “Gabapentin.”

**L73.0** `Simple Sentence` (0.813) → `passthrough`
- original: To make sure this medicine is safe for you, tell your doctor if you have ever had:
- pronoun resolved: To make sure Gabapentin is safe for you, tell your doctor if you have ever had:
  - edits: “this medicine” → “Gabapentin”

**L74.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: breathing problems

**L75.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: diabetes

**L76.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: depression, a mood disorder, or suicidal thoughts or actions

**L77.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a history of alcohol use or drug addiction

**L78.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a seizure

**L79.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: (for patients with restless legs syndrome) if you are a day sleeper or work a night shift

**L80.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: kidney disease, or if you are on dialysis

**L81.0** `Simple Sentence` (0.987) → `passthrough`
- original: Some people have thoughts about suicide while taking seizure medicine.

**L81.1** `Simple Sentence` (0.991) → `passthrough`
- original: Children taking gabapentin may have behavior changes.

**L81.2** `Incomplete Sentence` (0.9) → `excluded_incomplete`
- original: Stay alert to changes in your mood or symptoms.

**L81.3** `Simple Sentence` (0.957) → `passthrough`
- original: Your family or caregivers should also watch for sudden changes in your behavior.

**L82.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Pregnancy:

**L83.0** `Simple Sentence` (0.98) → `passthrough`
- original: It is not known if gabapentin will harm an unborn baby.

**L83.1** `Incomplete Sentence` (0.915) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or plan to become pregnant.

**L83.2** `Complex Sentence` (0.534) → `decomposed`
- original: Do not start or stop seizure medication during pregnancy without your doctor's advice, because having a seizure during pregnancy could harm both mother and baby.
  - S1: Do not start or stop seizure medication during pregnancy without your doctor's advice.
  - S2: Having a seizure during pregnancy could harm both mother and baby.

**L83.3** `Complex Sentence` (0.681) → `decomposed`
- original: If you are pregnant, your name may be listed on a pregnancy registry to track the effects of gabapentin on the baby.
  - S1: If you are pregnant, your name may be listed on a pregnancy registry.
  - S2: The registry is used to track the effects of gabapentin on the baby.

**L84.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Breastfeeding:

**L85.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Ask a doctor if it is safe to breastfeed while using gabapentin.

## How should I take gabapentin?

**L88.0** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Take gabapentin exactly as prescribed by your doctor.

**L88.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L88.2** `Simple Sentence` (0.984) → `passthrough`
- original: Your doctor may occasionally change your dose.

**L88.3** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Never take gabapentin in larger amounts, or for longer, than prescribed.

**L89.0** `Simple Sentence` (0.611) → `passthrough`
- original: Your dose needs may change if you switch to a different brand, strength, or form of this medicine.
- pronoun resolved: Your dose needs may change if you switch to a different brand, strength, or form of gabapentin.
  - edits: “this medicine.” → “gabapentin.”

**L89.1** `Incomplete Sentence` (0.936) → `excluded_incomplete`
- original: Avoid medication errors by using only the medicine your doctor prescribes.

**L90.0** `Simple Sentence` (0.99) → `passthrough`
- original: Neurontin can be taken with or without food.

**L91.0** `Simple Sentence` (0.973) → `passthrough`
- original: Gralise should be taken with food, with the evening meal.

**L92.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Swallow Gralise and Horizant tablets whole.

**L92.1** `Incomplete Sentence` (0.918) → `excluded_incomplete`
- original: Do not crush, break, chew, or dissolve them.

**L93.0** `Compound Sentence` (0.607) → `decomposed`
- original: If you break a scored Neurontin tablet and take only half, take the other half at your next dose, and use it within 28 days.
- pronoun resolved: If you break a scored Neurontin tablet and take only half, take the other half at your next dose, and use Neurontin tablet within 28 days.
  - edits: “it” → “Neurontin tablet”
  - S1: If you break a scored Neurontin tablet and take only half, take the other half at your next dose.
  - S2: Use Neurontin tablet within 28 days.

**L94.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: Measure liquid medicine with the supplied measuring device, not a kitchen spoon.

**L95.0** `Simple Sentence` (0.985) → `passthrough`
- original: Doses are based on weight in children.

**L95.1** `Simple Sentence` (0.931) → `passthrough`
- original: Your child's dose may change if the child gains or loses weight.

**L96.0** `Incomplete Sentence` (0.662) → `excluded_incomplete`
- original: Do not stop taking gabapentin suddenly.

**L96.1** `Simple Sentence` (0.987) → `passthrough`
- original: Stopping suddenly may cause increased seizures or withdrawal symptoms.

**L96.2** `Incomplete Sentence` (0.957) → `excluded_incomplete`
- original: Follow your doctor's instructions about tapering your dose, usually gradually over at least a week.

**L97.0** `Simple Sentence` (0.99) → `passthrough`
- original: This medicine can affect the results of certain medical tests.

**L97.1** `Incomplete Sentence` (0.917) → `excluded_incomplete`
- original: Tell any doctor who treats you that you are using gabapentin.

**L97.2** `Compound Sentence` (0.963) → `decomposed`
- original: Your kidney function may need to be checked, and your dose may change based on the results.
  - S1: Your kidney function may need to be checked.
  - S2: Your dose may change based on the results.

**L98.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Store tablets and capsules at room temperature away from moisture and heat.

**L98.1** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Store the liquid medicine in the refrigerator; do not freeze.

**L98.2** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Follow all storage instructions provided.

**L98.3** `Simple Sentence` (0.983) → `passthrough`
- original: Your pharmacist can provide more information about how to store this medicine.

## What strengths does gabapentin come in?

**L101.0** `Simple Sentence` (0.802) → `passthrough`
- original: Gabapentin is available as capsules, tablets, extended-release tablets, and an oral solution.

**L101.1** `Compound Sentence` (0.828) → `decomposed`
- original: Strengths vary by product, and different products are not interchangeable.
  - S1: Strengths vary by product.
  - S2: Different products are not interchangeable.

**L102.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Neurontin and generic gabapentin

**L103.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: oral capsules 100 mg, 300 mg, 400 mg

**L104.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: oral tablets 600 mg, 800 mg

**L105.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: oral solution 250 mg/5 mL

**L106.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Relgaabi

**L107.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: oral capsules 100 mg, 200 mg, 300 mg, 400 mg

**L108.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Gralise

**L109.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: extended-release tablets 300 mg, 450 mg, 600 mg, 750 mg, and 900 mg

**L110.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Horizant (gabapentin enacarbil)

**L111.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: extended-release tablets 300 mg, 600 mg

**L112.0** `Compound-Complex Sentence` (0.812) → `decomposed`
- original: Note: The Horizant strengths refer to gabapentin enacarbil, not gabapentin itself, so Horizant doses do not correspond milligram-for-milligram to other gabapentin products.
  - S1: Note: The Horizant strengths refer to gabapentin enacarbil.
  - S2: The Horizant strengths do not refer to gabapentin itself.
  - S3: Therefore, Horizant doses do not correspond milligram-for-milligram to other gabapentin products.

## Gabapentin dosing information

**L115.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Take gabapentin exactly as prescribed.

**L115.1** `Simple Sentence` (0.952) → `passthrough`
- original: Your dose may differ from the ranges shown here.

**L116.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Usual Gabapentin Dose for Epilepsy (immediate-release):

**L117.0** `Compound Sentence` (0.437) → `decomposed`
- original: Patients 12 years and older Dose: starting dose gabapentin 300 mg 3 times a day, which may be titrated up to a maximum dose of 600 mg 3 times a day if needed.
  - S1: Patients 12 years and older Dose: starting dose gabapentin 300 mg 3 times a day.
  - S2: This dose may be titrated up to a maximum dose of 600 mg 3 times a day if needed.

**L118.0** `Simple Sentence` (0.777) → `passthrough`
- original: Patients 3 to 11 years of age Dose: the starting dose range is 10 to 15 mg/kg/day, given in 3 divided doses.

**L118.1** `Compound Sentence` (0.962) → `decomposed`
- original: The recommended dose in patients 3 to 4 years of age is 40 mg/kg/day, and in patients 5 to 11 years of age is 25 to 35 mg/kg/day, given in 3 divided doses.
  - S1: The recommended dose in patients 3 to 4 years of age is 40 mg/kg/day.
  - S2: In patients 5 to 11 years of age, the dose is 25 to 35 mg/kg/day.
  - S3: This dose is given in 3 divided doses.

**L118.2** `Simple Sentence` (0.974) → `passthrough`
- original: The recommended maintenance dose is reached by upward titration over approximately 3 days.

**L119.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Less than 3 years: Not recommended

**L120.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Note:

**L121.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Leave no more than 12 hours between doses

**L122.0** `Simple Sentence` (0.987) → `passthrough`
- original: Dose should be adjusted in patients with reduced kidney function.

**L122.1** `Simple Sentence` (0.986) → `passthrough`
- original: Your doctor will determine your dose based on your kidney function.

**L123.0** `Incomplete Sentence` (0.613) → `excluded_incomplete`
- original: Use: Adjunctive therapy in the treatment of partial onset seizures, with and without secondary generalization, in patients 3 years of age and older.

**L124.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Usual Adult Dose for Postherpetic Neuralgia (immediate-release):

**L125.0** `Compound Sentence` (0.708) → `decomposed`
- original: Initial dose: gabapentin 300 mg orally on day one, 300 mg orally 2 times a day on day two, then 300 mg orally 3 times a day on day three, then titrate up as needed for pain relief
  - S1: The initial dose is gabapentin 300 mg orally on day one.
  - S2: On day two, the dose is 300 mg orally 2 times a day.
  - S3: On day three, the dose is 300 mg orally 3 times a day.
  - S4: The dose is then titrated up as needed for pain relief.

**L126.0** `Incomplete Sentence` (0.919) → `excluded_incomplete`
- original: Maximum Gabapentin dose in 24 hours: 1800 mg per day (600 mg orally 3 times a day) Notes:

**L127.0** `Simple Sentence` (0.977) → `passthrough`
- original: Doses above 1,800 mg a day did not add benefit in studies.

**L128.0** `Simple Sentence` (0.99) → `passthrough`
- original: Dose should be modified in renal impairment.

**L129.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Usual Adult Dose for Postherpetic Neuralgia (extended release - Gralise):

**L130.0** `Simple Sentence` (0.958) → `passthrough`
- original: Maintenance dose: Gralise should be titrated to 1800 mg orally once daily with the evening meal.

**L130.1** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Recommended titration schedule:

**L131.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: Day 1: 300 mg orally with the evening meal

**L132.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Day 2: 600 mg orally with the evening meal

**L133.0** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Days 3 through 6: 900 mg orally with the evening meal

**L134.0** `Incomplete Sentence` (0.968) → `excluded_incomplete`
- original: Days 7 through 10: 1200 mg orally with the evening meal

**L135.0** `Incomplete Sentence` (0.945) → `excluded_incomplete`
- original: Days 11 through 14: 1500 mg orally with the evening meal

**L136.0** `Incomplete Sentence` (0.956) → `excluded_incomplete`
- original: Day 15: 1800 mg orally with the evening meal

**L137.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Notes

**L138.0** `Complex Sentence` (0.812) → `decomposed`
- original: Gralise is not interchangeable with other gabapentin products because of differing pharmacokinetic profiles that affect the frequency of administration.
  - S1: Gralise is not interchangeable with other gabapentin products.
  - S2: This is because of differing pharmacokinetic profiles.
  - S3: These profiles affect the frequency of administration.

**L139.0** `Simple Sentence` (0.99) → `passthrough`
- original: Dose should be modified in renal impairment.

**L140.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Usual Adult Dose of Gabapentin enacarbil (Horizant) for Postherpetic Neuralgia:

**L141.0** `Incomplete Sentence` (0.823) → `excluded_incomplete`
- original: Initial dose: 600 mg orally once each morning on days 1 to 3 Maintenance dose: 600 mg orally 2 times a day (1200 mg/day total) from day 4 onward

**L142.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Notes:

**L143.0** `Simple Sentence` (0.816) → `passthrough`
- original: Doses above 1200 mg a day did not add benefit and caused more side effects

**L144.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Take with food and swallow tablets whole; do not crush or chew

**L145.0** `Simple Sentence` (0.988) → `passthrough`
- original: Horizant is not interchangeable with other gabapentin products

**L146.0** `Simple Sentence` (0.939) → `passthrough`
- original: Dose should be modified in renal impairment

**L147.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Usual Adult Dose of Gabapentin enacarbil (Horizant) for Restless Legs Syndrome:

**L148.0** `Compound Sentence` (0.516) → `decomposed`
- original: Gabapentin enacarbil (Horizant) dose: 600 mg orally once daily with food at about 5 PM Use: For the treatment of moderate-to-severe primary Restless Legs Syndrome (RLS) in adults
  - S1: Gabapentin enacarbil (Horizant) dose: 600 mg orally once daily with food at about 5 PM.
  - S2: Use: For the treatment of moderate-to-severe primary Restless Legs Syndrome (RLS) in adults.

**L149.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Notes:

**L150.0** `Simple Sentence` (0.853) → `passthrough`
- original: A 1200 mg dose gave no added benefit and caused more side effects

**L151.0** `Simple Sentence` (0.99) → `passthrough`
- original: Dose should be modified in renal impairment.

## What happens if I miss a dose?

**L154.0** `Compound Sentence` (0.555) → `decomposed`
- original: Take the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - S1: Take the medicine as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L154.1** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

**L155.0** `Compound Sentence` (0.461) → `decomposed`
- original: If you take Horizant: skip the missed dose and take your next dose at the regular time.
  - S1: If you take Horizant, skip the missed dose.
  - S2: Take your next dose at the regular time.

**L155.1** `Incomplete Sentence` (0.946) → `excluded_incomplete`
- original: Do not use two doses at one time.

## What happens if I overdose?

**L158.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L158.1** `Simple Sentence` (0.984) → `passthrough`
- original: An overdose can be fatal.

**L159.0** `Compound Sentence` (0.468) → `decomposed`
- original: Overdose symptoms may include slow breathing, double vision, tremor, slurred speech, drowsiness, change in your mental state, dizziness, tiredness, or diarrhea.
  - S1: Overdose symptoms may include slow breathing.
  - S2: Overdose symptoms may include double vision.
  - S3: Overdose symptoms may include tremor.
  - S4: Overdose symptoms may include slurred speech.
  - S5: Overdose symptoms may include drowsiness.
  - S6: Overdose symptoms may include a change in your mental state.
  - S7: Overdose symptoms may include dizziness.
  - S8: Overdose symptoms may include tiredness.
  - S9: Overdose symptoms may include diarrhea.

## What should I avoid while taking gabapentin?

**L162.0** `Incomplete Sentence` (0.971) → `excluded_incomplete`
- original: Avoid driving or hazardous activities until you know how gabapentin will affect you.

**L162.1** `Simple Sentence` (0.961) → `passthrough`
- original: Dizziness or drowsiness can cause falls, accidents, or severe injuries.

**L163.0** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: Avoid taking antacids at the same time as gabapentin.

**L164.0** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Do not drink alcohol.

**L164.1** `Simple Sentence` (0.97) → `passthrough`
- original: Dangerous side effects could occur.

## What other drugs will affect gabapentin?

**L167.0** `Complex Sentence` (0.585) → `decomposed`
- original: Taking gabapentin with other medicines that make you drowsy or slow your breathing can cause dangerous side effects, including life-threatening breathing problems.
  - S1: Taking gabapentin with other medicines can cause dangerous side effects.
  - S2: These other medicines make you drowsy or slow your breathing.
  - S3: The side effects include life-threatening breathing problems.

**L167.1** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Ask your doctor before using gabapentin with:

**L168.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: opioid pain medicines such as hydrocodone, oxycodone, morphine, or buprenorphine

**L169.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: sleeping pills such as zolpidem

**L170.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: anxiety medicines such as lorazepam and other benzodiazepines

**L171.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: muscle relaxers, sedatives, or other seizure medicines that cause drowsiness

**L172.0** `Incomplete Sentence` (0.966) → `excluded_incomplete`
- original: Avoid drinking alcohol while taking gabapentin, because it can add to these effects.
- pronoun resolved: Avoid drinking alcohol while taking gabapentin, because alcohol can add to these effects.
  - edits: “it” → “alcohol”

**L173.0** `Simple Sentence` (0.992) → `passthrough`
- original: Some medicines change the amount of gabapentin in your body:

**L174.0** `Simple Sentence` (0.964) → `passthrough`
- original: Antacids that contain aluminum or magnesium (such as Maalox) can reduce gabapentin absorption.

**L174.1** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Take gabapentin at least 2 hours after an antacid.

**L175.0** `Complex Sentence` (0.906) → `decomposed`
- original: Morphine can increase gabapentin levels, which may increase drowsiness and the risk of breathing problems.
  - S1: Morphine can increase gabapentin levels.
  - S2: This may increase drowsiness.
  - S3: This may also increase the risk of breathing problems.

**L175.1** `Simple Sentence` (0.957) → `passthrough`
- original: Your doctor may adjust your dose.

**L176.0** `Complex Sentence` (0.81) → `decomposed`
- original: Gabapentin does not usually interact with other seizure medicines, such as phenytoin, carbamazepine, valproic acid, or phenobarbital, because it is not broken down by the liver.
- pronoun resolved: Gabapentin does not usually interact with other seizure medicines, such as phenytoin, carbamazepine, valproic acid, or phenobarbital, because Gabapentin is not broken down by the liver.
  - edits: “it” → “Gabapentin”
  - S1: Gabapentin does not usually interact with other seizure medicines.
  - S2: Examples of these medicines include phenytoin, carbamazepine, valproic acid, or phenobarbital.
  - S3: This is because Gabapentin is not broken down by the liver.

**L176.1** `Simple Sentence` (0.985) → `passthrough`
- original: Your doctor can still check for interactions with your specific medicines.

**L177.0** `Incomplete Sentence` (0.902) → `excluded_incomplete`
- original: Tell your doctor about all your current medicines, including prescription and over-the-counter medicines, vitamins, and herbal products.

**L177.1** `Simple Sentence` (0.986) → `passthrough`
- original: This list does not include all possible drug interactions.

## Popular FAQ

**L180.0** `Compound-Complex Sentence` (0.481) → `decomposed`
- original: Q: Gabapentin for dogs: uses, dosage and side effects A: Gabapentin is commonly prescribed by veterinarians to treat dogs with chronic pain (such as arthritis, back pain, or nerve pain) or to relieve fear or anxiety associated with stressful events (such as car or plane travel, situations with loud noises [such as fireworks], or visits to the vets or the groomers).
  - S1: Gabapentin is commonly prescribed by veterinarians to treat dogs with chronic pain.
  - S2: Chronic pain in dogs includes arthritis, back pain, or nerve pain.
  - S3: Gabapentin is commonly prescribed by veterinarians to relieve fear or anxiety in dogs.
  - S4: Fear or anxiety in dogs is associated with stressful events.
  - S5: Stressful events include car or plane travel.
  - S6: Stressful events include situations with loud noises.
  - S7: Loud noises include fireworks.
  - S8: Stressful events include visits to the vets.
  - S9: Stressful events include visits to the groomers.

**L181.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Q: Lyrica vs Gabapentin: What's the difference?

**L181.1** `Compound-Complex Sentence` (0.86) → `decomposed`
- original: A: Both Lyrica (pregabalin) and gabapentin (Neurontin) are both anticonvulsants and gabapentinoids used to treat nerve pain and seizures, but they differ significantly in potency, absorption speed, and regulatory status.
- pronoun resolved: A: Both Lyrica (pregabalin) and gabapentin (Neurontin) are both anticonvulsants and gabapentinoids used to treat nerve pain and seizures, but Both Lyrica (pregabalin) and gabapentin (Neurontin) differ significantly in potency, absorption speed, and regulatory status.
  - edits: “they” → “Both Lyrica (pregabalin) and gabapentin (Neurontin)”
  - S1: Lyrica (pregabalin) is an anticonvulsant and gabapentinoid.
  - S2: Gabapentin (Neurontin) is an anticonvulsant and gabapentinoid.
  - S3: Lyrica (pregabalin) and gabapentin (Neurontin) are used to treat nerve pain.
  - S4: Lyrica (pregabalin) and gabapentin (Neurontin) are used to treat seizures.
  - S5: Lyrica (pregabalin) and gabapentin (Neurontin) differ significantly in potency.
  - S6: Lyrica (pregabalin) and gabapentin (Neurontin) differ significantly in absorption speed.
  - S7: Lyrica (pregabalin) and gabapentin (Neurontin) differ significantly in regulatory status.

**L181.2** `Compound-Complex Sentence` (0.886) → `decomposed`
- original: Lyrica is generally more potent, faster-acting (peaks in approximately 1 hour), and is a Schedule V controlled substance, whereas gabapentin peaks in 3 to 4 hours, is less regulated in most states, and is usually cheaper.
  - S1: Lyrica is generally more potent.
  - S2: Lyrica is faster-acting.
  - S3: Lyrica peaks in approximately 1 hour.
  - S4: Lyrica is a Schedule V controlled substance.
  - S5: Gabapentin peaks in 3 to 4 hours.
  - S6: Gabapentin is less regulated in most states.
  - S7: Gabapentin is usually cheaper.

**L182.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Q: How long does gabapentin withdrawal last?

**L182.1** `Compound-Complex Sentence` (0.655) → `decomposed`
- original: A: Case reports have shown that gabapentin withdrawal often lasts for 5 to 10 days, but some people have taken as long as 18 weeks to completely taper off gabapentin while managing withdrawal symptoms.
  - S1: Case reports have shown that gabapentin withdrawal often lasts for 5 to 10 days.
  - S2: Some people have taken as long as 18 weeks to completely taper off gabapentin.
  - S3: These people managed withdrawal symptoms during the tapering process.

**L182.2** `Compound Sentence` (0.676) → `decomposed`
- original: The symptoms and how long they last depend on how much of the drug you are taking and for how long you’ve been taking it.
  - S1: The symptoms depend on how much of the drug you are taking.
  - S2: The symptoms depend on how long you've been taking it.
  - S3: How long the symptoms last depends on how much of the drug you are taking.
  - S4: How long the symptoms last depends on how long you've been taking it.

**L183.0** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Q: Is gabapentin considered a painkiller?

**L183.1** `Complex Sentence` (0.381) → `decomposed`
- original: A: Gabapentin (Neurontin, Gralise, Horizant) is commonly used to treat some types of nerve pain but is classified as an anticonvulsant medicine, not as an opioid or narcotic painkiller.
  - S1: Gabapentin is commonly used to treat some types of nerve pain.
  - S2: Gabapentin is classified as an anticonvulsant medicine.
  - S3: Gabapentin is not classified as an opioid or narcotic painkiller.

**L183.2** `Complex Sentence` (0.607) → `decomposed`
- original: Gabapentin is used to treat nerve pain that can occur due to an outbreak of shingles, restless legs syndrome (RLS), and some forms of epilepsy.
  - S1: Gabapentin is used to treat nerve pain.
  - S2: Nerve pain can occur due to an outbreak of shingles.
  - S3: Nerve pain can occur due to restless legs syndrome (RLS).
  - S4: Nerve pain can occur due to some forms of epilepsy.

**L184.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: Q: Is gabapentin safe for cats?

**L184.1** `Simple Sentence` (0.937) → `passthrough`
- original: A: Yes, Gabapentin is safe for cats when prescribed by a veterinarian.

**L184.2** `Complex Sentence` (0.453) → `decomposed`
- original: This medication is commonly used to treat cat pain, anxiety, and feline hyperesthesia syndrome with minimal side effects.
  - S1: This medication is commonly used to treat cat pain.
  - S2: This medication is commonly used to treat anxiety.
  - S3: This medication is commonly used to treat feline hyperesthesia syndrome.
  - S4: The medication has minimal side effects.

**L184.3** `Compound Sentence` (0.665) → `decomposed`
- original: Mild sedation and drowsiness are the most common reactions, which typically improve with continued use.
  - S1: Mild sedation and drowsiness are the most common reactions.
  - S2: These reactions typically improve with continued use.

**L185.0** `Incomplete Sentence` (0.941) → `excluded_incomplete`
- original: Q: Does gabapentin help treat nerve pain?

**L185.1** `Complex Sentence` (0.834) → `decomposed`
- original: A: Gabapentin can help relieve nerve pain in some people with postherpetic neuralgia (shingles nerve pain) and diabetic peripheral neuropathy (diabetic foot pain).
  - S1: Gabapentin can help relieve nerve pain in some people.
  - S2: It helps people with postherpetic neuralgia (shingles nerve pain).
  - S3: It helps people with diabetic peripheral neuropathy (diabetic foot pain).

**L186.0** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Q: How long does it take gabapentin to work?

**L186.1** `Compound Sentence` (0.7) → `decomposed`
- original: A: It can take several weeks for gabapentin to reach its full effect, but this depends on the condition being treated and your individual response to the drug.
  - S1: It can take several weeks for gabapentin to reach its full effect.
  - S2: This depends on the condition being treated and your individual response to the drug.

**L187.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Q: Does gabapentin cause weight gain?

**L187.1** `Compound Sentence` (0.936) → `decomposed`
- original: A: Gabapentin may cause weight gain, but it is an uncommon side effect.
  - S1: Gabapentin may cause weight gain.
  - S2: It is an uncommon side effect.

**L187.2** `Simple Sentence` (0.985) → `passthrough`
- original: Studies have shown that a small number of people taking gabapentin weight gain.

**L187.3** `Simple Sentence` (0.948) → `passthrough`
- original: People who do gain weight may gain about 5 pounds after 6 weeks of use.

**L188.0** `Incomplete Sentence` (0.797) → `excluded_incomplete`
- original: Q: Does gabapentin help you sleep?

**L188.1** `Simple Sentence` (0.966) → `passthrough`
- original: A: Gabapentin is a prescription medication that may help you sleep.

**L188.2** `Complex Sentence` (0.725) → `decomposed`
- original: That may be why it has been prescribed for people with insomnia, even though it is not approved for that use.
- pronoun resolved: That may be why Gabapentin has been prescribed for people with insomnia, even though Gabapentin is not approved for that use.
  - edits: “it” → “Gabapentin”; “it” → “Gabapentin”
  - S1: That may be why Gabapentin has been prescribed for people with insomnia.
  - S2: Gabapentin is not approved for that use.
