# Hydroxyzine — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/hydroxyzine.txt` · 201 sentences · 36 changed by pronoun resolution · 290 sentences sent to EDC

## What is hydroxyzine?

**L5.0** `Complex Sentence` (0.755) → `decomposed`
- original: Hydroxyzine is a prescription antihistamine used to treat anxiety and tension, itching from allergic skin conditions, and sedation before and after general anesthesia.
  - S1: Hydroxyzine is a prescription antihistamine.
  - S2: It is used to treat anxiety and tension.
  - S3: It is used to treat itching from allergic skin conditions.
  - S4: It is used for sedation before and after general anesthesia.

**L6.0** `Simple Sentence` (0.909) → `passthrough`
- original: It comes in three oral forms:
- pronoun resolved: Hydroxyzine comes in three oral forms:
  - edits: “It” → “Hydroxyzine”

**L7.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Hydroxyzine hydrochloride (HCl) tablets in 10 mg, 25 mg, and 50 mg strengths

**L8.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Hydroxyzine hydrochloride oral solution (a syrup) containing 10 mg in each 5 mL

**L9.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Hydroxyzine pamoate capsules in 25 mg

**L10.0** `Simple Sentence` (0.975) → `passthrough`
- original: There is also a hydroxyzine hydrochloride injection.

**L10.1** `Compound Sentence` (0.664) → `decomposed`
- original: It is given into a muscle by a healthcare professional and is never given into a vein or under the skin.
- pronoun resolved: Hydroxyzine is given into a muscle by a healthcare professional and is never given into a vein or under the skin.
  - edits: “It” → “Hydroxyzine”
  - S1: Hydroxyzine is given into a muscle by a healthcare professional.
  - S2: It is never given into a vein or under the skin.

**L11.0** `Simple Sentence` (0.901) → `passthrough`
- original: Hydroxyzine is not chemically related to benzodiazepines, phenothiazines, reserpine, or meprobamate.

## What is hydroxyzine used for?

**L14.0** `Simple Sentence` (0.987) → `passthrough`
- original: Hydroxyzine taken by mouth is approved for three uses.

**L14.1** `Simple Sentence` (0.984) → `passthrough`
- original: These are the same for hydroxyzine HCl and hydroxyzine pamoate.
- pronoun resolved: Three uses are the same for hydroxyzine HCl and hydroxyzine pamoate.
  - edits: “These” → “Three uses”

**L15.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Anxiety and tension.

**L15.1** `Incomplete Sentence` (0.837) → `excluded_incomplete`
- original: For symptomatic relief of anxiety and tension linked to psychoneurosis, and as an add-on treatment in physical illnesses where anxiety is present.

**L16.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Itching from allergic skin conditions.

**L16.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: For managing itching (pruritus) caused by allergic conditions such as long-term hives (chronic urticaria), eczema-type rashes, and rashes caused by contact with an irritant.

**L16.2** `Simple Sentence` (0.979) → `passthrough`
- original: It is also used for itching caused by histamine release.
- pronoun resolved: Hydroxyzine is also used for itching caused by histamine release.
  - edits: “It” → “Hydroxyzine”

**L17.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Sedation around surgery.

**L17.1** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: As a sedative given before a procedure (premedication) and after general anesthesia.

**L18.0** `Compound Sentence` (0.758) → `decomposed`
- original: The injection is also approved for nausea and vomiting and is usually given in hospital or clinic settings.
  - S1: The injection is also approved for nausea and vomiting.
  - S2: It is usually given in hospital or clinic settings.

**L18.1** `Simple Sentence` (0.983) → `passthrough`
- original: It should not be used for nausea and vomiting caused by pregnancy.
- pronoun resolved: Hydroxyzine should not be used for nausea and vomiting caused by pregnancy.
  - edits: “It” → “Hydroxyzine”

**L19.0** `Simple Sentence` (0.984) → `passthrough`
- original: Hydroxyzine has not been studied for long-term use in anxiety.

**L19.1** `Complex Sentence` (0.49) → `decomposed`
- original: Studies have not assessed whether it still works as an anti-anxiety medicine beyond four months.
- pronoun resolved: Studies have not assessed whether Hydroxyzine still works as an anti-anxiety medicine beyond four months.
  - edits: “it” → “Hydroxyzine”
  - S1: Studies have not assessed whether Hydroxyzine still works as an anti-anxiety medicine.
  - S2: The assessment period is beyond four months.

**L19.2** `Simple Sentence` (0.966) → `passthrough`
- original: Your doctor should review from time to time whether you still need it.

## What is the difference between hydroxyzine hydrochloride and hydroxyzine pamoate?

**L22.0** `Simple Sentence` (0.954) → `passthrough`
- original: Hydroxyzine hydrochloride (HCl) and hydroxyzine pamoate are two salt forms of the same active medicine.

**L22.1** `Complex Sentence` (0.885) → `decomposed`
- original: Taken by mouth, FDA-approved labeling gives them the same approved uses, the same doses, the same warnings, and the same side effects.
- pronoun resolved: Taken by mouth, FDA-approved labeling gives Hydroxyzine hydrochloride and hydroxyzine pamoate the same approved uses, the same doses, the same warnings, and the same side effects.
  - edits: “them” → “Hydroxyzine hydrochloride and hydroxyzine pamoate”
  - S1: FDA-approved labeling gives Hydroxyzine hydrochloride and hydroxyzine pamoate the same approved uses.
  - S2: FDA-approved labeling gives them the same doses.
  - S3: FDA-approved labeling gives them the same warnings.
  - S4: FDA-approved labeling gives them the same side effects.
  - S5: These drugs are taken by mouth.

**L23.0** `Simple Sentence` (0.768) → `passthrough`
- original: The injection is the exception.

**L23.1** `Compound Sentence` (0.94) → `decomposed`
- original: It is a hydroxyzine HCl product; there is no pamoate injection, and it has its own approved uses, doses, and warnings.
  - S1: It is a hydroxyzine HCl product.
  - S2: There is no pamoate injection.
  - S3: It has its own approved uses, doses, and warnings.

**L24.0** `Incomplete Sentence` (0.966) → `excluded_incomplete`
- original: The practical differences are:

**L25.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Form.

**L25.1** `Simple Sentence` (0.969) → `passthrough`
- original: Hydroxyzine hydrochloride comes as tablets and as an oral solution.

**L25.2** `Simple Sentence` (0.988) → `passthrough`
- original: Hydroxyzine pamoate comes as capsules.

**L26.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: How they dissolve.
- pronoun resolved: How Hydroxyzine hydrochloride and Hydroxyzine pamoate dissolve.
  - edits: “they” → “Hydroxyzine hydrochloride and Hydroxyzine pamoate”

**L26.1** `Simple Sentence` (0.982) → `passthrough`
- original: Hydroxyzine hydrochloride is very soluble in water.

**L26.2** `Simple Sentence` (0.982) → `passthrough`
- original: Hydroxyzine pamoate is practically insoluble in water.

**L27.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: How the strength is measured.

**L27.1** `Simple Sentence` (0.968) → `passthrough`
- original: Hydroxyzine pamoate capsules are labeled by the amount of hydroxyzine HCl they are equivalent to.
- pronoun resolved: Hydroxyzine pamoate capsules are labeled by the amount of hydroxyzine HCl Hydroxyzine pamoate capsules are equivalent to.
  - edits: “they” → “Hydroxyzine pamoate capsules”

**L27.2** `Simple Sentence` (0.944) → `passthrough`
- original: A 25 mg pamoate capsule delivers the same amount of active medicine as a hydroxyzine hydrochloride 25 mg tablet.

**L28.0** `Simple Sentence` (0.957) → `passthrough`
- original: The two salts also had different brand names.

**L28.1** `Compound Sentence` (0.949) → `decomposed`
- original: Vistaril was the brand name for hydroxyzine pamoate, and Atarax was the brand name for hydroxyzine hydrochloride.
  - S1: Vistaril was the brand name for hydroxyzine pamoate.
  - S2: Atarax was the brand name for hydroxyzine hydrochloride.

**L28.2** `Compound Sentence` (0.959) → `decomposed`
- original: Both brands have been discontinued in the United States, and hydroxyzine is now available as a generic medicine.
  - S1: Both brands have been discontinued in the United States.
  - S2: Hydroxyzine is now available as a generic medicine.

**L29.0** `Incomplete Sentence` (0.965) → `excluded_incomplete`
- original: Is hydroxyzine pamoate stronger or longer lasting than hydroxyzine hydrochloride?

**L29.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L30.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: No.

**L30.1** `Compound Sentence` (0.793) → `decomposed`
- original: You may read that hydroxyzine pamoate works better for anxiety, lasts longer, or reaches the brain more effectively than hydroxyzine hydrochloride.
  - S1: You may read that hydroxyzine pamoate works better for anxiety.
  - S2: You may read that hydroxyzine pamoate lasts longer.
  - S3: You may read that hydroxyzine pamoate reaches the brain more effectively than hydroxyzine hydrochloride.

**L30.2** `Simple Sentence` (0.989) → `passthrough`
- original: FDA-approved labeling does not support this.

**L31.0** `Complex Sentence` (0.781) → `decomposed`
- original: Labeling for both salt forms states that hydroxyzine's effects are usually noticed within 15 to 30 minutes of a dose taken by mouth.
  - S1: Labeling for both salt forms states that hydroxyzine's effects are usually noticed within 15 to 30 minutes.
  - S2: The effects are noticed after a dose taken by mouth.

**L31.1** `Simple Sentence` (0.962) → `passthrough`
- original: Both are approved for the same three uses.

**L31.2** `Compound Sentence` (0.93) → `decomposed`
- original: Both carry the same doses, which are 50 to 100 mg four times a day for anxiety in adults, and 25 mg three or four times a day for itching.
  - S1: Both carry the same doses.
  - S2: The doses are 50 to 100 mg four times a day for anxiety in adults.
  - S3: The doses are 25 mg three or four times a day for itching.

**L31.3** `Simple Sentence` (0.978) → `passthrough`
- original: No FDA labeling describes a difference in how strongly or how long either form works.

**L32.0** `Complex Sentence` (0.801) → `decomposed`
- original: The reason the doses match is that hydroxyzine pamoate capsules are labeled by their hydroxyzine hydrochloride equivalent.
- pronoun resolved: The reason the doses match is that hydroxyzine pamoate capsules are labeled by hydroxyzine pamoate capsules's hydroxyzine hydrochloride equivalent.
  - edits: “their” → “hydroxyzine pamoate capsules's”
  - S1: The reason the doses match is that hydroxyzine pamoate capsules are labeled by their hydroxyzine hydrochloride equivalent.
  - S2: Hydroxyzine pamoate capsules are labeled by their hydroxyzine hydrochloride equivalent.

**L32.1** `Simple Sentence` (0.965) → `passthrough`
- original: A 25 mg pamoate capsule and a 25 mg hydrochloride tablet deliver the same amount of active medicine.

**L33.0** `Simple Sentence` (0.526) → `passthrough`
- original: If you feel that one form suits you better than the other, tell your doctor.

**L33.1** `Simple Sentence` (0.986) → `passthrough`
- original: People can respond differently to the same medicine.

## How does hydroxyzine work?

**L36.0** `Complex Sentence` (0.878) → `decomposed`
- original: Hydroxyzine is thought to work by quieting activity in certain deeper regions of the brain, below the outer layer known as the cortex.
  - S1: Hydroxyzine is thought to work by quieting activity in certain deeper regions of the brain.
  - S2: These regions are located below the outer layer known as the cortex.

**L36.1** `Complex Sentence` (0.752) → `decomposed`
- original: It is not a cortical depressant, meaning it does not work by slowing down the outer layer of the brain the way some other sedatives do.
- pronoun resolved: Hydroxyzine is not a cortical depressant, meaning Hydroxyzine does not work by slowing down the outer layer of the brain the way some other sedatives do.
  - edits: “It” → “Hydroxyzine”; “it” → “Hydroxyzine”
  - S1: Hydroxyzine is not a cortical depressant.
  - S2: This means Hydroxyzine does not work by slowing down the outer layer of the brain.
  - S3: Some other sedatives work by slowing down the outer layer of the brain.

**L37.0** `Simple Sentence` (0.554) → `passthrough`
- original: Hydroxyzine also blocks histamine, a chemical your body releases during an allergic reaction.

**L37.1** `Simple Sentence` (0.987) → `passthrough`
- original: This is what relieves itching.
- pronoun resolved: Blocks histamine is what relieves itching.
  - edits: “This” → “Blocks histamine”

**L38.0** `Compound Sentence` (0.497) → `decomposed`
- original: Laboratory and clinical studies have also shown that hydroxyzine relaxes skeletal muscle, widens the airways (bronchodilation), and reduces pain.
  - S1: Laboratory and clinical studies have also shown that hydroxyzine relaxes skeletal muscle.
  - S2: Hydroxyzine widens the airways (bronchodilation).
  - S3: Hydroxyzine reduces pain.

**L38.1** `Simple Sentence` (0.922) → `passthrough`
- original: These are effects that have been observed rather than uses the medicine is approved for.
- pronoun resolved: These are effects that have been observed rather than uses Hydroxyzine is approved for.
  - edits: “the medicine” → “Hydroxyzine”

**L39.0** `Simple Sentence` (0.906) → `passthrough`
- original: Hydroxyzine has also been shown to reduce nausea and vomiting.

**L39.1** `Simple Sentence` (0.516) → `passthrough`
- original: This is an approved use for the injection, but not for the forms taken by mouth.
- pronoun resolved: Reduce nausea and vomiting is an approved use for the injection, but not for the forms taken by mouth.
  - edits: “This” → “Reduce nausea and vomiting”

## How do I take hydroxyzine?

**L42.0** `Incomplete Sentence` (0.952) → `excluded_incomplete`
- original: Take hydroxyzine exactly as your doctor prescribes.

**L42.1** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Follow all directions on your prescription label.

**L42.2** `Compound Sentence` (0.593) → `decomposed`
- original: Do not take more or less than prescribed, and do not take it for longer than your doctor tells you to.
- pronoun resolved: Do not take more or less than prescribed, and do not take hydroxyzine for longer than your doctor tells you to.
  - edits: “it” → “hydroxyzine”
  - S1: Do not take more or less than prescribed.
  - S2: Do not take hydroxyzine for longer than your doctor tells you to.

**L43.0** `Simple Sentence` (0.955) → `passthrough`
- original: Your doctor may adjust your dose depending on how well you respond to treatment.

**L44.0** `Complex Sentence` (0.604) → `decomposed`
- original: If you are taking the oral solution, measure your dose with the dosing syringe provided, a dose-measuring spoon, or a medicine cup.
  - S1: If you are taking the oral solution, measure your dose with the dosing syringe provided.
  - S2: You can also measure your dose with a dose-measuring spoon.
  - S3: You can also measure your dose with a medicine cup.

**L44.1** `Incomplete Sentence` (0.853) → `excluded_incomplete`
- original: Do not use a kitchen spoon, because it will not give an accurate dose.
- pronoun resolved: Do not use a kitchen spoon, because kitchen spoon will not give an accurate dose.
  - edits: “it” → “kitchen spoon”

**L44.2** `Incomplete Sentence` (0.888) → `excluded_incomplete`
- original: Ask your pharmacist for a measuring device if you do not have one.

**L45.0** `Incomplete Sentence` (0.837) → `excluded_incomplete`
- original: Call your doctor if your anxiety does not improve or if it gets worse.
- pronoun resolved: Call your doctor if your anxiety does not improve or if anxiety gets worse.
  - edits: “it” → “anxiety”

## What is the usual dosage of hydroxyzine?

**L48.0** `Simple Sentence` (0.96) → `passthrough`
- original: The dose depends on what you are being treated for.

**L48.1** `Compound Sentence` (0.532) → `decomposed`
- original: The same doses apply to hydroxyzine hydrochloride tablets, hydroxyzine hydrochloride oral solution, and hydroxyzine pamoate capsules.
  - S1: The same doses apply to hydroxyzine hydrochloride tablets.
  - S2: The same doses apply to hydroxyzine hydrochloride oral solution.
  - S3: The same doses apply to hydroxyzine pamoate capsules.

**L49.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Dosage for anxiety and tension:

**L50.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Adults: 50 to 100 mg four times a day

**L51.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Children under 6 years: 50 mg a day, split into smaller doses

**L52.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Children 6 years and over: 50 to 100 mg a day, split into smaller doses

**L53.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Dosage for itching:

**L54.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Adults: 25 mg three or four times a day

**L55.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Children under 6 years: 50 mg a day, split into smaller doses

**L56.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Children 6 years and over: 50 to 100 mg a day, split into smaller doses

**L57.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Dosage for sedation before and after surgery:

**L58.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Adults: 50 to 100 mg

**L59.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Children: 0.6 mg for each kilogram of body weight

**L60.0** `Complex Sentence` (0.506) → `decomposed`
- original: If treatment is started with an injection into a muscle, later doses can be given by mouth.
  - S1: Treatment can be started with an injection into a muscle.
  - S2: Later doses can be given by mouth.

**L61.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Dosage in older adults:

**L62.0** `Simple Sentence` (0.987) → `passthrough`
- original: Doctors usually start older adults on a low dose.

**L62.1** `Compound Sentence` (0.906) → `decomposed`
- original: Sedating medicines can cause confusion and too much sedation in older people, so your doctor will watch you closely.
  - S1: Sedating medicines can cause confusion and too much sedation in older people.
  - S2: Your doctor will watch you closely.

**L62.2** `Compound Sentence` (0.958) → `decomposed`
- original: Kidney, liver, and heart function often decline with age, and how much hydroxyzine leaves the body through the kidneys has not been established.
  - S1: Kidney, liver, and heart function often decline with age.
  - S2: How much hydroxyzine leaves the body through the kidneys has not been established.

## How long does hydroxyzine take to work?

**L65.0** `Simple Sentence` (0.98) → `passthrough`
- original: Hydroxyzine usually starts working within 15 to 30 minutes of taking it by mouth.
- pronoun resolved: Hydroxyzine usually starts working within 15 to 30 minutes of taking Hydroxyzine by mouth.
  - edits: “it” → “Hydroxyzine”

**L65.1** `Simple Sentence` (0.988) → `passthrough`
- original: It is absorbed quickly from the digestive system.
- pronoun resolved: Hydroxyzine is absorbed quickly from the digestive system.
  - edits: “It” → “Hydroxyzine”

**L65.2** `Simple Sentence` (0.954) → `passthrough`
- original: This is the same for tablets, oral solution, and pamoate capsules.
- pronoun resolved: Hydroxyzine is the same for tablets, oral solution, and pamoate capsules.
  - edits: “This” → “Hydroxyzine”

## What are the side effects of hydroxyzine?

**L68.0** `Simple Sentence` (0.92) → `passthrough`
- original: The most common side effects of hydroxyzine are drowsiness, dry mouth, and headache.

**L68.1** `Simple Sentence` (0.618) → `passthrough`
- original: These are usually mild and do not last long.
- pronoun resolved: Drowsiness, dry mouth, and headache are usually mild and do not last long.
  - edits: “These” → “Drowsiness, dry mouth, and headache”

**L69.0** `Simple Sentence` (0.91) → `passthrough`
- original: A skin rash is different.

**L69.1** `Complex Sentence` (0.837) → `decomposed`
- original: If you develop a rash while taking hydroxyzine, stop taking it and call your doctor, because a rash can be the first sign of a serious reaction.
- pronoun resolved: If you develop a rash while taking hydroxyzine, stop taking hydroxyzine and call your doctor, because a rash can be the first sign of a serious reaction.
  - edits: “it” → “hydroxyzine”
  - S1: If you develop a rash while taking hydroxyzine, stop taking hydroxyzine and call your doctor.
  - S2: A rash can be the first sign of a serious reaction.

**L70.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Common side effects:

**L71.0** `Simple Sentence` (0.954) → `passthrough`
- original: Common hydroxyzine side effects include dry mouth, headache, and drowsiness.

**L71.1** `Compound Sentence` (0.896) → `decomposed`
- original: The drowsiness is usually temporary and may go away after a few days of treatment or when the dose is lowered.
  - S1: The drowsiness is usually temporary.
  - S2: It may go away after a few days of treatment.
  - S3: It may go away when the dose is lowered.

**L72.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious side effects:

**L73.0** `Compound Sentence` (0.398) → `decomposed`
- original: Stop taking hydroxyzine and call your doctor right away if you develop a skin rash, if a skin condition you are treating gets worse, or if you have any other sign of an allergic reaction.
  - S1: Stop taking hydroxyzine and call your doctor right away if you develop a skin rash.
  - S2: Stop taking hydroxyzine and call your doctor right away if a skin condition you are treating gets worse.
  - S3: Stop taking hydroxyzine and call your doctor right away if you have any other sign of an allergic reaction.

**L74.0** `Simple Sentence` (0.368) → `passthrough`
- original: In rare cases, hydroxyzine can cause a serious skin reaction called acute generalized exanthematous pustulosis (AGEP).

**L74.1** `Simple Sentence` (0.48) → `passthrough`
- original: Signs include fever together with many small, shallow, pus-filled spots appearing across large areas of swollen, red skin.

**L74.2** `Complex Sentence` (0.828) → `decomposed`
- original: If you have had AGEP or another allergic reaction to hydroxyzine, you should also avoid cetirizine and levocetirizine, because a similar reaction can happen with those medicines.
- pronoun resolved: If you have had AGEP or another allergic reaction to hydroxyzine, you should also avoid cetirizine and levocetirizine, because a similar reaction can happen with cetirizine and levocetirizine.
  - edits: “those medicines.” → “cetirizine and levocetirizine.”
  - S1: If you have had AGEP or another allergic reaction to hydroxyzine, you should also avoid cetirizine and levocetirizine.
  - S2: This is because a similar reaction can happen with cetirizine and levocetirizine.

**L75.0** `Complex Sentence` (0.926) → `decomposed`
- original: Hydroxyzine has also been linked to a heart rhythm problem called QT prolongation, which can lead to a serious irregular heartbeat known as Torsade de Pointes.
  - S1: Hydroxyzine has also been linked to a heart rhythm problem called QT prolongation.
  - S2: QT prolongation can lead to a serious irregular heartbeat known as Torsade de Pointes.

**L76.0** `Simple Sentence` (0.537) → `passthrough`
- original: Other reported side effects include:

**L77.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: tremor or seizures (convulsions), which are rare and have usually happened at doses much higher than recommended

**L78.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: hallucinations (seeing or hearing things that are not there)

**L79.0** `Incomplete Sentence` (0.975) → `excluded_incomplete`
- original: skin reactions including rash, hives, itching, and fixed drug eruptions, which are rashes that come back in the same spot each time the medicine is taken

**L80.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: allergic reaction

**L81.0** `Simple Sentence` (0.987) → `passthrough`
- original: Serious breathing problems have not been reported at recommended doses.

**L82.0** `Complex Sentence` (0.71) → `decomposed`
- original: If you are given hydroxyzine by injection, tell your healthcare provider straight away about severe pain, swelling, or skin changes where the injection was given.
  - S1: If you are given hydroxyzine by injection, tell your healthcare provider straight away.
  - S2: Tell your healthcare provider about severe pain, swelling, or skin changes.
  - S3: These symptoms occur where the injection was given.

**L82.1** `Complex Sentence` (0.811) → `decomposed`
- original: In rare cases, the injection has caused serious damage to the surrounding tissue, including tissue death (necrosis) and gangrene, which has needed surgery to treat.
  - S1: In rare cases, the injection has caused serious damage to the surrounding tissue.
  - S2: The damage included tissue death (necrosis) and gangrene.
  - S3: The damage has needed surgery to treat.

**L83.0** `Compound Sentence` (0.483) → `decomposed`
- original: This is not a complete list of side effects, and others may happen.
  - S1: This is not a complete list of side effects.
  - S2: Others may happen.

**L83.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L83.2** `Simple Sentence` (0.97) → `passthrough`
- original: You may report side effects to the FDA at 1-800-FDA-1088.

## Does hydroxyzine cause weight gain?

**L86.0** `Simple Sentence` (0.957) → `passthrough`
- original: Weight gain is not among the side effects reported in FDA-approved labeling for hydroxyzine.

**L86.1** `Compound Sentence` (0.562) → `decomposed`
- original: It does not appear in the labeling for the tablets, the oral solution, the pamoate capsules, or the injection.
- pronoun resolved: Weight gain does not appear in the labeling for the tablets, the oral solution, the pamoate capsules, or the injection.
  - edits: “It” → “Weight gain”
  - S1: Weight gain does not appear in the labeling for the tablets.
  - S2: Weight gain does not appear in the labeling for the oral solution.
  - S3: Weight gain does not appear in the labeling for the pamoate capsules.
  - S4: Weight gain does not appear in the labeling for the injection.

**L87.0** `Simple Sentence` (0.943) → `passthrough`
- original: This does not mean weight changes are impossible for every person.

**L87.1** `Simple Sentence` (0.592) → `passthrough`
- original: If your weight changes while you are taking hydroxyzine, tell your doctor.

## Who should not take hydroxyzine?

**L90.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Do not take hydroxyzine if you:

**L91.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: are allergic to hydroxyzine or to any ingredient in the medicine

**L92.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: are allergic to cetirizine or levocetirizine

**L93.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: have a prolonged QT interval, a heart rhythm finding seen on an electrocardiogram (ECG)

**L94.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: are in early pregnancy

**L95.0** `Simple Sentence` (0.907) → `passthrough`
- original: In animal studies, hydroxyzine caused birth defects in rats and mice at doses well above those used in people.

**L95.1** `Compound Sentence` (0.939) → `decomposed`
- original: There is not enough information in humans to know whether hydroxyzine is safe in early pregnancy, so it should not be used at that time.
- pronoun resolved: There is not enough information in humans to know whether hydroxyzine is safe in early pregnancy, so hydroxyzine should not be used at that time.
  - edits: “it” → “hydroxyzine”
  - S1: There is not enough information in humans to know whether hydroxyzine is safe in early pregnancy.
  - S2: Therefore, hydroxyzine should not be used at that time.

## What should I tell my doctor before taking hydroxyzine?

**L98.0** `Incomplete Sentence` (0.681) → `excluded_incomplete`
- original: Tell your doctor if you have anything that raises your risk of a heart rhythm problem called QT prolongation.

**L98.1** `Incomplete Sentence` (0.764) → `excluded_incomplete`
- original: This includes:
- pronoun resolved: QT prolongation includes:
  - edits: “This” → “QT prolongation”

**L99.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: congenital long QT syndrome, a heart rhythm condition you are born with

**L100.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: a family history of long QT syndrome

**L101.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: a recent heart attack

**L102.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: heart failure that is not well controlled

**L103.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: a slow or irregular heartbeat (bradyarrhythmia)

**L104.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: other conditions that make heart rhythm problems more likely

**L105.0** `Simple Sentence` (0.989) → `passthrough`
- original: Hydroxyzine should not be given to women who are breastfeeding.

**L105.1** `Compound Sentence` (0.891) → `decomposed`
- original: It is not known whether hydroxyzine passes into breast milk, but many medicines do.
  - S1: It is not known whether hydroxyzine passes into breast milk.
  - S2: Many medicines do.

**L106.0** `Compound Sentence` (0.868) → `decomposed`
- original: The oral solution contains a small amount of alcohol, 0.5% by volume, and is sweetened with sucrose.
  - S1: The oral solution contains a small amount of alcohol, 0.5% by volume.
  - S2: It is sweetened with sucrose.

**L106.1** `Incomplete Sentence` (0.97) → `excluded_incomplete`
- original: Tell your doctor if either of these matters for you.

## Can I drink alcohol while taking hydroxyzine?

**L109.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: No.

**L109.1** `Simple Sentence` (0.986) → `passthrough`
- original: Alcohol's effects may be stronger while you are taking hydroxyzine.

**L109.2** `Simple Sentence` (0.977) → `passthrough`
- original: You should also avoid other medicines that slow down the central nervous system.

## What should I avoid while taking hydroxyzine?

**L112.0** `Simple Sentence` (0.982) → `passthrough`
- original: Hydroxyzine can make you drowsy.

**L112.1** `Incomplete Sentence` (0.669) → `excluded_incomplete`
- original: Do not drive or operate dangerous machinery until you know how it affects you.
- pronoun resolved: Do not drive or operate dangerous machinery until you know how Hydroxyzine affects you.
  - edits: “it” → “Hydroxyzine”

**L113.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Avoid alcohol and other medicines that cause drowsiness.

## Is hydroxyzine a controlled substance?

**L116.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: No.

**L116.1** `Simple Sentence` (0.519) → `passthrough`
- original: Hydroxyzine is not a controlled substance and has no DEA schedule.

**L116.2** `Simple Sentence` (0.981) → `passthrough`
- original: This applies to both hydroxyzine hydrochloride and hydroxyzine pamoate.

## What other drugs affect hydroxyzine?

**L119.0** `Simple Sentence` (0.984) → `passthrough`
- original: Hydroxyzine makes the effects of central nervous system depressants stronger.

**L119.1** `Complex Sentence` (0.726) → `decomposed`
- original: If you take hydroxyzine with any of the following, your doctor may need to lower the dose of the other medicine:
  - S1: If you take hydroxyzine with any of the following, your doctor may need to lower the dose of the other medicine.

**L120.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: narcotic (opioid) pain medicines

**L121.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: non-narcotic pain medicines

**L122.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: barbiturates

**L123.0** `Compound Sentence` (0.676) → `decomposed`
- original: Hydroxyzine may increase the effects of meperidine and barbiturates when used before anesthesia, so your doctor will adjust these doses for you individually.
  - S1: Hydroxyzine may increase the effects of meperidine and barbiturates when used before anesthesia.
  - S2: Your doctor will adjust these doses for you individually.

**L124.0** `Complex Sentence` (0.62) → `decomposed`
- original: Care is needed if you take other medicines that can affect heart rhythm by prolonging the QT interval.
  - S1: Care is needed if you take other medicines.
  - S2: These medicines can affect heart rhythm.
  - S3: They do this by prolonging the QT interval.

**L124.1** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: These include:

**L125.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: heart rhythm medicines such as quinidine, procainamide, amiodarone, and sotalol

**L126.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: certain antipsychotics such as ziprasidone, iloperidone, clozapine, quetiapine, and chlorpromazine

**L127.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: certain antidepressants such as citalopram and fluoxetine

**L128.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: certain antibiotics such as azithromycin, erythromycin, clarithromycin, gatifloxacin, and moxifloxacin

**L129.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: other medicines such as pentamidine, methadone, ondansetron, and droperidol

**L130.0** `Compound Sentence` (0.968) → `decomposed`
- original: Hydroxyzine does not affect atropine or other belladonna alkaloids, and it is not known to interfere with digitalis.
  - S1: Hydroxyzine does not affect atropine or other belladonna alkaloids.
  - S2: It is not known to interfere with digitalis.

**L130.1** `Simple Sentence` (0.989) → `passthrough`
- original: It can be used at the same time as digitalis.
- pronoun resolved: Hydroxyzine can be used at the same time as digitalis.
  - edits: “It” → “Hydroxyzine”

**L131.0** `Incomplete Sentence` (0.831) → `excluded_incomplete`
- original: Tell each of your healthcare providers about all medicines you take, including prescription and over-the-counter medicines, vitamins, and herbal products.

**L131.1** `Simple Sentence` (0.949) → `passthrough`
- original: Not all possible interactions are listed here.

## What happens if I overdose on hydroxyzine?

**L134.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L135.0** `Simple Sentence` (0.974) → `passthrough`
- original: The most common sign of hydroxyzine overdose is heavy sedation.

**L135.1** `Simple Sentence` (0.684) → `passthrough`
- original: Other reported signs include seizures (convulsions), stupor, nausea, and vomiting.

**L136.0** `Compound Sentence` (0.938) → `decomposed`
- original: Overdose can also cause QT prolongation and Torsade de Pointes, so heart monitoring with an ECG is recommended.
  - S1: Overdose can also cause QT prolongation and Torsade de Pointes.
  - S2: Heart monitoring with an ECG is recommended.

**L137.0** `Simple Sentence` (0.989) → `passthrough`
- original: There is no specific antidote for hydroxyzine overdose.

## How should I store hydroxyzine?

**L140.0** `Incomplete Sentence` (0.699) → `excluded_incomplete`
- original: Store hydroxyzine tablets, capsules, and oral solution at room temperature, between 68°F and 77°F (20°C to 25°C).

**L141.0** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: Keep tablets and capsules in a tightly closed, light-resistant container with a child-resistant cap.

**L142.0** `Incomplete Sentence` (0.935) → `excluded_incomplete`
- original: Keep the oral solution in a tightly closed, light-resistant bottle with a child-resistant cap.

**L142.1** `Incomplete Sentence` (0.645) → `excluded_incomplete`
- original: Protect it from light and do not let it freeze.
- pronoun resolved: Protect oral solution from light and do not let oral solution freeze.
  - edits: “it” → “oral solution”; “it” → “oral solution”

**L143.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Keep this and all medicines out of the reach of children.

## Popular FAQ

**L146.0** `Simple Sentence` (0.905) → `passthrough`
- original: Q: Can you take hydroxyzine for anxiety and sleep?

**L146.1** `Complex Sentence` (0.867) → `decomposed`
- original: A: Yes, hydroxyzine can be prescribed short term for anxiety and anxiety‑related trouble sleeping, usually as an “as‑needed” or bridging option rather than a long‑term daily medicine.
  - S1: Hydroxyzine can be prescribed short term for anxiety.
  - S2: It can also be prescribed for anxiety-related trouble sleeping.
  - S3: It is usually used as an "as-needed" or bridging option.
  - S4: It is not typically used as a long-term daily medicine.

**L146.2** `Compound Sentence` (0.903) → `decomposed`
- original: Evidence supports its short‑term anxiolytic and sedating effects, but its effectiveness and safety for chronic use beyond several months are not well established.
- pronoun resolved: Evidence supports hydroxyzine's short‑term anxiolytic and sedating effects, but hydroxyzine's effectiveness and safety for chronic use beyond several months are not well established.
  - edits: “its” → “hydroxyzine's”; “its” → “hydroxyzine's”
  - S1: Evidence supports hydroxyzine's short‑term anxiolytic and sedating effects.
  - S2: Hydroxyzine's effectiveness and safety for chronic use beyond several months are not well established.

**L147.0** `Incomplete Sentence` (0.958) → `excluded_incomplete`
- original: Q: Can Hydroxyzine be Taken Long-term For Anxiety?

**L147.1** `Simple Sentence` (0.908) → `passthrough`
- original: A: Hydroxyzine is intended for short-term anxiety treatment only, typically less than 4 months.

**L147.2** `Complex Sentence` (0.846) → `decomposed`
- original: Long-term hydroxyzine use is considered off-label because no studies have examined the safety of extended use beyond this timeframe.
  - S1: Long-term hydroxyzine use is considered off-label.
  - S2: This is because no studies have examined the safety of extended use beyond this timeframe.

**L147.3** `Complex Sentence` (0.948) → `decomposed`
- original: Some research suggests a link between long-term use of medications with anticholinergic properties, such as hydroxyzine, and dementia, particularly in older adults.
  - S1: Some research suggests a link between long-term use of medications with anticholinergic properties and dementia.
  - S2: The medications include hydroxyzine.
  - S3: The link is particularly observed in older adults.

**L147.4** `Simple Sentence` (0.982) → `passthrough`
- original: Brain fog has also been reported with long-term use.

**L148.0** `Incomplete Sentence` (0.963) → `excluded_incomplete`
- original: Q: How long does hydroxyzine last?

**L148.1** `Compound-Complex Sentence` (0.828) → `decomposed`
- original: A: Hydroxyzine’s noticeable calming and sedating effects typically last about 4–6 hours for most people, even though the drug itself stays in the body much longer due to an elimination half-life usually around 14–25 hours in adults and about 7 hours in children.
- pronoun resolved: A: Hydroxyzine’s noticeable calming and sedating effects typically last about 4–6 hours for most people, even though hydroxyzine itself stays in the body much longer due to an elimination half-life usually around 14–25 hours in adults and about 7 hours in children.
  - edits: “the drug” → “hydroxyzine”
  - S1: Hydroxyzine has noticeable calming and sedating effects.
  - S2: These effects typically last about 4–6 hours for most people.
  - S3: Hydroxyzine itself stays in the body much longer.
  - S4: This is due to an elimination half-life usually around 14–25 hours in adults.
  - S5: The elimination half-life is about 7 hours in children.

**L149.0** `Incomplete Sentence` (0.927) → `excluded_incomplete`
- original: Q: Does Benadryl help with or cause anxiety?

**L149.1** `Compound Sentence` (0.96) → `decomposed`
- original: A: No, Benadryl does not treat anxiety, and in some people it can cause it.
- pronoun resolved: A: No, Benadryl does not treat anxiety, and in some people Benadryl can cause it.
  - edits: “it” → “Benadryl”
  - S1: No, Benadryl does not treat anxiety.
  - S2: In some people, Benadryl can cause anxiety.

**L149.2** `Compound Sentence` (0.911) → `decomposed`
- original: Benadryl (diphenhydramine) is an allergy medicine that often makes people sleepy, so it may feel calming for a few hours.
- pronoun resolved: Benadryl (diphenhydramine) is an allergy medicine that often makes people sleepy, so Benadryl may feel calming for a few hours.
  - edits: “it” → “Benadryl”
  - S1: Benadryl (diphenhydramine) is an allergy medicine that often makes people sleepy.
  - S2: Benadryl may feel calming for a few hours.

**L149.3** `Compound Sentence` (0.964) → `decomposed`
- original: But drowsiness is not the same as treating anxiety, and Benadryl is not FDA-approved for anxiety.
  - S1: But drowsiness is not the same as treating anxiety.
  - S2: Benadryl is not FDA-approved for anxiety.

**L150.0** `Incomplete Sentence` (0.979) → `excluded_incomplete`
- original: Q: Hydroxyzine Pamoate vs HCl: What’s the difference?

**L150.1** `Compound-Complex Sentence` (0.674) → `decomposed`
- original: A: Hydroxyzine pamoate and hydroxyzine HCl both deliver the same active drug, hydroxyzine, so their clinical effects (such as sedation, itch relief, and anxiety reduction) are broadly similar.
  - S1: Hydroxyzine pamoate delivers the active drug hydroxyzine.
  - S2: Hydroxyzine HCl delivers the active drug hydroxyzine.
  - S3: Hydroxyzine pamoate and hydroxyzine HCl deliver the same active drug.
  - S4: The clinical effects of hydroxyzine include sedation.
  - S5: The clinical effects of hydroxyzine include itch relief.
  - S6: The clinical effects of hydroxyzine include anxiety reduction.
  - S7: The clinical effects of hydroxyzine pamoate and hydroxyzine HCl are broadly similar.

**L150.2** `Complex Sentence` (0.532) → `decomposed`
- original: The main difference is the salt form (pamoate vs hydrochloride), which influences how the medicine is formulated.
  - S1: The main difference is the salt form.
  - S2: The salt form is pamoate vs hydrochloride.
  - S3: The salt form influences how the medicine is formulated.

**L151.0** `Incomplete Sentence` (0.975) → `excluded_incomplete`
- original: Q: Is hydroxyzine a controlled substance or addictive?

**L151.1** `Compound-Complex Sentence` (0.558) → `decomposed`
- original: A: Hydroxyzine is not classified as a controlled substance in the United States, and current evidence does not show that it causes physical dependence or a characteristic withdrawal syndrome when stopped.
- pronoun resolved: A: Hydroxyzine is not classified as a controlled substance in the United States, and current evidence does not show that hydroxyzine causes physical dependence or a characteristic withdrawal syndrome when stopped.
  - edits: “it” → “hydroxyzine”
  - S1: Hydroxyzine is not classified as a controlled substance in the United States.
  - S2: Current evidence does not show that hydroxyzine causes physical dependence.
  - S3: Current evidence does not show that hydroxyzine causes a characteristic withdrawal syndrome when stopped.

**L151.2** `Compound Sentence` (0.704) → `decomposed`
- original: It is, however, a prescription-only sedating antihistamine that should be taken only under medical supervision.
- pronoun resolved: Hydroxyzine is, however, a prescription-only sedating antihistamine that should be taken only under medical supervision.
  - edits: “It” → “Hydroxyzine”
  - S1: Hydroxyzine is a prescription-only sedating antihistamine.
  - S2: It should be taken only under medical supervision.

**L152.0** `Incomplete Sentence` (0.966) → `excluded_incomplete`
- original: Q: Hydroxyzine vs Benadryl: What’s the difference?

**L152.1** `Compound Sentence` (0.735) → `decomposed`
- original: A: Hydroxyzine and Benadryl (diphenhydramine) are both older, sedating H1 antihistamines, but they are different drugs with different FDA‑approved uses.
- pronoun resolved: A: Hydroxyzine and Benadryl (diphenhydramine) are both older, sedating H1 antihistamines, but Hydroxyzine and Benadryl are different drugs with different FDA‑approved uses.
  - edits: “they” → “Hydroxyzine and Benadryl”
  - S1: Hydroxyzine and Benadryl (diphenhydramine) are both older, sedating H1 antihistamines.
  - S2: Hydroxyzine and Benadryl are different drugs with different FDA‑approved uses.

**L152.2** `Compound Sentence` (0.709) → `decomposed`
- original: Hydroxyzine is available only by prescription in the United States, while diphenhydramine (Benadryl) is sold over the counter (OTC) in many allergy and sleep products.
  - S1: Hydroxyzine is available only by prescription in the United States.
  - S2: Diphenhydramine (Benadryl) is sold over the counter (OTC) in many allergy and sleep products.

**L153.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Q: Can dogs take hydroxyzine?

**L153.1** `Simple Sentence` (0.957) → `passthrough`
- original: A: Yes, dogs can take hydroxyzine.

**L153.2** `Complex Sentence` (0.502) → `decomposed`
- original: Hydroxyzine is an antihistamine that may help treat allergies, anxiety, and motion sickness in dogs.
  - S1: Hydroxyzine is an antihistamine.
  - S2: Hydroxyzine may help treat allergies in dogs.
  - S3: Hydroxyzine may help treat anxiety in dogs.
  - S4: Hydroxyzine may help treat motion sickness in dogs.

**L154.0** `Incomplete Sentence` (0.974) → `excluded_incomplete`
- original: Q: Does hydroxyzine cause weight gain or loss?

**L154.1** `Compound Sentence` (0.87) → `decomposed`
- original: A: Hydroxyzine is not strongly linked to either weight gain or weight loss, and any changes in weight are usually mild and indirect rather than a direct effect of the drug.
  - S1: Hydroxyzine is not strongly linked to either weight gain or weight loss.
  - S2: Any changes in weight are usually mild and indirect rather than a direct effect of the drug.

**L154.2** `Complex Sentence` (0.872) → `decomposed`
- original: In clinical studies, weight changes are uncommon and generally not considered clinically significant compared with other side effects such as drowsiness.
  - S1: In clinical studies, weight changes are uncommon.
  - S2: Weight changes are generally not considered clinically significant.
  - S3: Other side effects such as drowsiness are considered clinically significant.
