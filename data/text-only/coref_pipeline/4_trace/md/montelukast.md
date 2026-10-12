# Montelukast — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/montelukast.txt` · 70 sentences · 8 changed by pronoun resolution · 113 sentences sent to EDC

## What is montelukast?

**L5.0** `Compound Sentence` (0.884) → `decomposed`
- original: Montelukast helps to reduce inflammation and may be used to prevent asthma attacks in adults and children at least 2 years old.
  - S1: Montelukast helps to reduce inflammation.
  - S2: It may be used to prevent asthma attacks in adults and children at least 2 years old.

**L6.0** `Complex Sentence` (0.885) → `decomposed`
- original: Montelukast is also used to prevent exercise-induced bronchoconstriction (a narrowing of the air passages in the lungs due to exercise that is also known as exercise-induced asthma) in adults and children who are at least 6 years old.
  - S1: Montelukast is used to prevent exercise-induced bronchoconstriction.
  - S2: Exercise-induced bronchoconstriction is a narrowing of the air passages in the lungs due to exercise.
  - S3: It is also known as exercise-induced asthma.
  - S4: Montelukast is used in adults and children who are at least 6 years old.

**L7.0** `Complex Sentence` (0.865) → `decomposed`
- original: For adults and children at least 2 years old with symptoms of seasonal allergic rhinitis, and people over 6 months old with perennial (year-round) allergies, montelukast may be considered when other treatments have not worked.
  - S1: Montelukast may be considered for adults and children at least 2 years old with symptoms of seasonal allergic rhinitis.
  - S2: Montelukast may be considered for people over 6 months old with perennial (year-round) allergies.
  - S3: This consideration applies when other treatments have not worked.

**L8.0** `Complex Sentence` (0.78) → `decomposed`
- original: If you already take montelukast regularly to prevent asthma or allergy symptoms, do not take an extra dose to treat exercise-induced bronchoconstriction.
  - S1: If you already take montelukast regularly to prevent asthma or allergy symptoms.
  - S2: Do not take an extra dose.
  - S3: Do not take an extra dose to treat exercise-induced bronchoconstriction.

**L9.0** `Compound Sentence` (0.844) → `decomposed`
- original: Montelukast is not a fast-acting rescue medicine for asthma attacks and needs to be taken daily to work properly.
  - S1: Montelukast is not a fast-acting rescue medicine for asthma attacks.
  - S2: It needs to be taken daily to work properly.

**L10.0** `Simple Sentence` (0.978) → `passthrough`
- original: Montelukast was FDA-approved in 1998.

## Warnings

**L13.0** `Compound Sentence` (0.47) → `decomposed`
- original: Stop taking montelukast and call your doctor right away if you have any unusual changes in mood or behavior (such as agitation, confusion, depression, sleep problems, compulsive behaviors, hallucinations, or suicidal thoughts or actions).
  - S1: Stop taking montelukast and call your doctor right away if you have any unusual changes in mood or behavior.
  - S2: Such changes include agitation, confusion, depression, sleep problems, compulsive behaviors, hallucinations, or suicidal thoughts or actions.

**L14.0** `Compound Sentence` (0.473) → `decomposed`
- original: Tell your doctor right away if you have signs of blood vessel inflammation: flu-like symptoms, severe sinus pain, a skin rash, numbness or a "pins and needles" feeling in your arms or legs.
  - S1: Tell your doctor right away if you have signs of blood vessel inflammation.
  - S2: These signs include flu-like symptoms.
  - S3: These signs include severe sinus pain.
  - S4: These signs include a skin rash.
  - S5: These signs include numbness or a "pins and needles" feeling in your arms or legs.

## Before taking this medicine

**L17.0** `Simple Sentence` (0.989) → `passthrough`
- original: You should not use montelukast if you are allergic to it.
- pronoun resolved: You should not use montelukast if you are allergic to montelukast.
  - edits: “it.” → “montelukast.”

**L18.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Tell your doctor if you have ever had:

**L19.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: mental illness or psychosis; or

**L20.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: asthma, or a history of severe allergic reaction (sneezing, runny or stuffy nose, wheezing, shortness of breath) after taking aspirin or another NSAID.

**L21.0** `Compound Sentence` (0.78) → `decomposed`
- original: The chewable montelukast tablet may contain phenylalanine and could be harmful if you have phenylketonuria (PKU).
  - S1: The chewable montelukast tablet may contain phenylalanine.
  - S2: It could be harmful if you have phenylketonuria (PKU).

**L22.0** `Incomplete Sentence` (0.952) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or breastfeeding.

**L23.0** `Incomplete Sentence` (0.542) → `excluded_incomplete`
- original: Do not give this medicine to a child without a doctor's advice.

## How should I take montelukast?

**L26.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: Take montelukast exactly as prescribed by your doctor and read all medication guides or instruction sheets about montelukast.

**L27.0** `Simple Sentence` (0.99) → `passthrough`
- original: Montelukast is not a fast-acting rescue medicine for asthma attacks.

**L27.1** `Incomplete Sentence` (0.829) → `excluded_incomplete`
- original: Seek medical attention if your breathing problems get worse quickly, or if you think your medications are not working.

**L28.0** `Simple Sentence` (0.971) → `passthrough`
- original: Montelukast is usually taken once every evening, with or without food.

**L29.0** `Compound Sentence` (0.88) → `decomposed`
- original: For exercise-induced bronchoconstriction, take a single dose at least 2 hours before exercise, and do not take another dose for at least 24 hours.
  - S1: For exercise-induced bronchoconstriction, take a single dose at least 2 hours before exercise.
  - S2: Do not take another dose for at least 24 hours.

**L30.0** `Incomplete Sentence` (0.975) → `excluded_incomplete`
- original: Swallow the regular tablet whole, with a glass of water.

**L31.0** `Simple Sentence` (0.976) → `passthrough`
- original: You must chew the chewable tablet before you swallow it.

**L32.0** `Compound Sentence` (0.552) → `decomposed`
- original: Place the oral granules directly in your mouth and swallow, or mix them with applesauce, mashed carrots, rice, or ice cream.
- pronoun resolved: Place the oral granules directly in your mouth and swallow, or mix oral granules with applesauce, mashed carrots, rice, or ice cream.
  - edits: “them” → “oral granules”
  - S1: Place the oral granules directly in your mouth and swallow.
  - S2: You can mix oral granules with applesauce, mashed carrots, rice, or ice cream.

**L32.1** `Simple Sentence` (0.967) → `passthrough`
- original: The granules may also be mixed with baby formula or breast milk.

**L32.2** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Do not use any other type of liquid.

**L32.3** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Use the mixture within 15 minutes.

**L32.4** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Do not save for later use.

**L33.0** `Complex Sentence` (0.901) → `decomposed`
- original: If you also use an oral steroid medication, you should not stop using it suddenly when you start taking montelukast.
- pronoun resolved: If you also use an oral steroid medication, you should not stop using oral steroid medication suddenly when you start taking montelukast.
  - edits: “it” → “oral steroid medication”
  - S1: You should not stop using oral steroid medication suddenly.
  - S2: This applies if you also use an oral steroid medication.
  - S3: This is when you start taking montelukast.

**L33.1** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Follow your doctor's instructions about tapering your dose.

**L34.0** `Simple Sentence` (0.619) → `passthrough`
- original: Do not change your dose or stop using asthma medication without your doctor's advice.

**L35.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Store montelukast at room temperature away from moisture and heat.

**L35.1** `Simple Sentence` (0.95) → `passthrough`
- original: Do not open a packet of montelukast oral granules until you are ready to use them.
- pronoun resolved: Do not open a packet of montelukast oral granules until you are ready to use montelukast oral granules.
  - edits: “them.” → “montelukast oral granules.”

## What happens if I miss a dose of montelukast?

**L38.0** `Compound Sentence` (0.59) → `decomposed`
- original: If you miss a dose of montelukast, skip the missed dose and use your next dose at the regular time.
  - S1: If you miss a dose of montelukast, skip the missed dose.
  - S2: Use your next dose at the regular time.

**L38.1** `Incomplete Sentence` (0.946) → `excluded_incomplete`
- original: Do not use two doses at one time.

## What happens if I overdose?

**L41.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

## What should I avoid while taking montelukast?

**L44.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Avoid situations or activities that may trigger an asthma attack.

**L45.0** `Complex Sentence` (0.876) → `decomposed`
- original: If your asthma symptoms get worse when you take aspirin, avoid taking aspirin or other NSAIDs (nonsteroidal anti-inflammatory drugs) such as ibuprofen (Advil, Motrin), naproxen (Aleve), celecoxib, diclofenac, indomethacin, meloxicam, and others.
  - S1: If your asthma symptoms get worse when you take aspirin, avoid taking aspirin.
  - S2: Avoid taking other NSAIDs (nonsteroidal anti-inflammatory drugs).
  - S3: Examples of NSAIDs include ibuprofen (Advil, Motrin), naproxen (Aleve), celecoxib, diclofenac, indomethacin, meloxicam, and others.

## Montelukast side effects

**L48.0** `Compound Sentence` (0.474) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to montelukast: hives, blisters, severe itching; difficult breathing; swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to montelukast.
  - S2: Signs of an allergic reaction to montelukast include hives, blisters, and severe itching.
  - S3: Signs of an allergic reaction to montelukast also include difficult breathing.
  - S4: Signs of an allergic reaction to montelukast also include swelling of your face, lips, tongue, or throat.

**L49.0** `Compound Sentence` (0.473) → `decomposed`
- original: Tell your doctor right away if you have signs of blood vessel inflammation: flu-like symptoms, severe sinus pain, a skin rash, numbness or a "pins and needles" feeling in your arms or legs.
  - S1: Tell your doctor right away if you have signs of blood vessel inflammation.
  - S2: These signs include flu-like symptoms.
  - S3: These signs include severe sinus pain.
  - S4: These signs include a skin rash.
  - S5: These signs include numbness or a "pins and needles" feeling in your arms or legs.

**L50.0** `Simple Sentence` (0.987) → `passthrough`
- original: Some people using montelukast have had new or worsening mental problems.

**L50.1** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Stop taking montelukast and call your doctor right away if you have unusual changes in mood or behavior, such as:

**L51.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: agitation, aggression, feeling restless or irritable;

**L52.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: anxiety, depression, confusion, problems with memory or attention;

**L53.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: stuttering, tremors, uncontrolled muscle movements;

**L54.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: suicidal thoughts or actions;

**L55.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: hallucinations, sleep problems, vivid, dreams, sleep-walking; or

**L56.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: compulsive or repetitive behaviors.

**L57.0** `Simple Sentence` (0.964) → `passthrough`
- original: Common side effects of montelukast may include:

**L58.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: stomach pain, diarrhea;

**L59.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: fever or other flu symptoms;

**L60.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: ear pain or full feeling, trouble hearing;

**L61.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: headache; or

**L62.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: cold symptoms such as runny or stuffy nose, sinus pain, cough, sore throat.

**L63.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L63.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L63.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## What other drugs will affect montelukast?

**L66.0** `Complex Sentence` (0.546) → `decomposed`
- original: Other drugs may affect montelukast, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may affect montelukast.
  - S2: These other drugs include prescription and over-the-counter medicines.
  - S3: These other drugs also include vitamins and herbal products.

**L66.1** `Incomplete Sentence` (0.967) → `excluded_incomplete`
- original: Tell your doctor about all other medicines you use.

## Popular FAQ

**L69.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: Q: Why is montelukast usually taken at night?

**L69.1** `Complex Sentence` (0.784) → `decomposed`
- original: A: Montelukast is usually taken in the evening because this is how the medication was studied and proven to be effective in clinical trials.
- pronoun resolved: A: Montelukast is usually taken in the evening because montelukast is how the medication was studied and proven to be effective in clinical trials.
  - edits: “this” → “montelukast”
  - S1: Montelukast is usually taken in the evening.
  - S2: Montelukast was studied in clinical trials.
  - S3: Montelukast was proven to be effective in clinical trials.

**L69.2** `Complex Sentence` (0.896) → `decomposed`
- original: Most clinical trials and prescribing information have traditionally used once‑daily evening dosing for asthma, which is why this schedule is commonly recommended.
  - S1: Most clinical trials and prescribing information have traditionally used once-daily evening dosing for asthma.
  - S2: This is why this schedule is commonly recommended.

**L70.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Q: What is the mechanism of action of montelukast?

**L70.1** `Complex Sentence` (0.641) → `decomposed`
- original: A: Montelukast works by blocking leukotriene D4 and related cysteinyl leukotrienes from binding to the CysLT1 receptor on airway and nasal tissues.
  - S1: Montelukast works by blocking leukotriene D4 and related cysteinyl leukotrienes.
  - S2: These substances bind to the CysLT1 receptor.
  - S3: The CysLT1 receptor is located on airway and nasal tissues.

**L70.2** `Simple Sentence` (0.909) → `passthrough`
- original: This reduces inflammation, swelling, and allergy or asthma symptoms.
- pronoun resolved: Montelukast reduces inflammation, swelling, and allergy or asthma symptoms.
  - edits: “This” → “Montelukast”

**L71.0** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Q: Is montelukast an antihistamine?

**L71.1** `Incomplete Sentence` (0.653) → `excluded_incomplete`
- original: A: Montelukast is not an antihistamine; it belongs to a different drug class.
- pronoun resolved: A: Montelukast is not an antihistamine; Montelukast belongs to a different drug class.
  - edits: “it” → “Montelukast”

**L71.2** `Complex Sentence` (0.877) → `decomposed`
- original: It is a leukotriene receptor antagonist (LTRA), a type of medicine that blocks the effects of leukotrienes (chemicals that contribute to inflammation in asthma and some allergy conditions).
- pronoun resolved: Montelukast is a leukotriene receptor antagonist (LTRA), a type of medicine that blocks the effects of leukotrienes (chemicals that contribute to inflammation in asthma and some allergy conditions).
  - edits: “It” → “Montelukast”
  - S1: Montelukast is a leukotriene receptor antagonist (LTRA).
  - S2: LTRA is a type of medicine.
  - S3: This medicine blocks the effects of leukotrienes.
  - S4: Leukotrienes are chemicals that contribute to inflammation in asthma and some allergy conditions.

**L72.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Q: Is Montelukast used for allergies?

**L72.1** `Simple Sentence` (0.658) → `passthrough`
- original: A: Montelukast is approved to treat allergy-related nasal symptoms in people with seasonal and perennial allergic rhinitis.

**L72.2** `Complex Sentence` (0.955) → `decomposed`
- original: However, because of a boxed warning about potential neuropsychiatric side effects, major guidelines recommend reserving montelukast for patients who do not respond to or cannot tolerate other standard allergy treatments.
  - S1: Major guidelines recommend reserving montelukast for specific patients.
  - S2: These patients are those who do not respond to other standard allergy treatments.
  - S3: These patients are also those who cannot tolerate other standard allergy treatments.
  - S4: This recommendation exists because of a boxed warning.
  - S5: The warning concerns potential neuropsychiatric side effects.
