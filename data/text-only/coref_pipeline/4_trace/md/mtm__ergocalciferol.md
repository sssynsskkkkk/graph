# Ergocalciferol — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/mtm__ergocalciferol.txt` · 85 sentences · 2 changed by pronoun resolution · 110 sentences sent to EDC

## What is ergocalciferol?

**L5.0** `Simple Sentence` (0.991) → `passthrough`
- original: Ergocalciferol is vitamin D2.

**L5.1** `Simple Sentence` (0.991) → `passthrough`
- original: Vitamin D helps your body absorb calcium.

**L6.0** `Simple Sentence` (0.862) → `passthrough`
- original: Ergocalciferol is used to treat hypoparathyroidism (decreased functioning of the parathyroid glands).

**L7.0** `Complex Sentence` (0.589) → `decomposed`
- original: Ergocalciferol is also used to treat rickets (softening of the bones caused by vitamin D deficiency) or low levels of phosphate in the blood (hypophosphatemia).
  - S1: Ergocalciferol is also used to treat rickets.
  - S2: Rickets is the softening of the bones caused by vitamin D deficiency.
  - S3: Ergocalciferol is also used to treat low levels of phosphate in the blood.
  - S4: Low levels of phosphate in the blood are known as hypophosphatemia.

**L8.0** `Simple Sentence` (0.979) → `passthrough`
- original: Ergocalciferol may also be used for purposes not listed in this medication guide.

## Ergocalciferol side effects

**L11.0** `Incomplete Sentence` (0.452) → `excluded_incomplete`
- original: Get emergency medical help if you have signs of an allergic reaction: hives; difficult breathing; swelling of your face, lips, tongue, or throat.

**L12.0** `Incomplete Sentence` (0.939) → `excluded_incomplete`
- original: Stop taking ergocalciferol and call your doctor at once if you have:

**L13.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: chest pain, feeling short of breath;

**L14.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: growth problems (in a child taking ergocalciferol); or

**L15.0** `Simple Sentence` (0.816) → `passthrough`
- original: early signs of vitamin D overdose --weakness, metallic taste in your mouth, weight loss, muscle or bone pain, constipation, nausea, and vomiting.

**L16.0** `Compound Sentence` (0.877) → `decomposed`
- original: Less serious side effects may be more likely, and you may have none at all.
  - S1: Less serious side effects may be more likely.
  - S2: You may have none at all.

**L17.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L17.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L17.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## Warnings

**L20.0** `Compound-Complex Sentence` (0.674) → `decomposed`
- original: You should not take ergocalciferol if you have had an allergic reaction to vitamin D, or if you have high levels of calcium or vitamin D in your body, or any condition that makes it hard for your body to absorb nutrients from food (malabsorption).
  - S1: You should not take ergocalciferol if you have had an allergic reaction to vitamin D.
  - S2: You should not take ergocalciferol if you have high levels of calcium in your body.
  - S3: You should not take ergocalciferol if you have high levels of vitamin D in your body.
  - S4: You should not take ergocalciferol if you have a condition that makes it hard for your body to absorb nutrients from food.
  - S5: Malabsorption is a condition that makes it hard for your body to absorb nutrients from food.

**L21.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Use only the recommended dose of ergocalciferol.

**L21.1** `Simple Sentence` (0.984) → `passthrough`
- original: An overdose could cause serious or life-threatening side effects.

## Before taking this medicine

**L24.0** `Simple Sentence` (0.661) → `passthrough`
- original: You should not take ergocalciferol if you have had an allergic reaction to vitamin D, or if you have:

**L25.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: high levels of vitamin D in your body (hypervitaminosis D);

**L26.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: high levels of calcium in your blood (hypercalcemia); or

**L27.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: any condition that makes it hard for your body to absorb nutrients from food (malabsorption).

**L28.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Tell your doctor if you have ever had:

**L29.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: heart disease;

**L30.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: kidney disease; or

**L31.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: an electrolyte imbalance.

**L32.0** `Complex Sentence` (0.618) → `decomposed`
- original: Certain forms of ergocalciferol may contain ingredients you should know about, such as peanut or soybean oil, sugar, aspartame (phenylalanine), or certain food dyes.
  - S1: Certain forms of ergocalciferol may contain ingredients you should know about.
  - S2: These ingredients include peanut or soybean oil, sugar, aspartame (phenylalanine), or certain food dyes.

**L32.1** `Simple Sentence` (0.522) → `passthrough`
- original: Ask a doctor before using ergocalciferol if you have allergies, diabetes, or phenylketonuria (PKU).

**L33.0** `Compound Sentence` (0.969) → `decomposed`
- original: Too much vitamin D could harm an unborn baby, and your dose needs may be different during pregnancy.
  - S1: Too much vitamin D could harm an unborn baby.
  - S2: Your dose needs may be different during pregnancy.

**L33.1** `Incomplete Sentence` (0.936) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or if you become pregnant while taking ergocalciferol.

**L34.0** `Compound Sentence` (0.755) → `decomposed`
- original: Ergocalciferol can pass into breast milk and may cause side effects in the nursing baby.
  - S1: Ergocalciferol can pass into breast milk.
  - S2: It may cause side effects in the nursing baby.

**L34.1** `Incomplete Sentence` (0.961) → `excluded_incomplete`
- original: Tell your doctor if you are breast-feeding.

**L35.0** `Incomplete Sentence` (0.775) → `excluded_incomplete`
- original: Do not give ergocalciferol to a child without medical advice.

**L35.1** `Simple Sentence` (0.963) → `passthrough`
- original: Your child's dose will depend on age, weight, diet, and other factors.

## How should I take ergocalciferol?

**L38.0** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L38.1** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Use only the recommended dose of ergocalciferol.

**L39.0** `Compound Sentence` (0.859) → `decomposed`
- original: It may be best to take ergocalciferol after a meal, but you may take ergocalciferol with or without food.
  - S1: It may be best to take ergocalciferol after a meal.
  - S2: You may take ergocalciferol with or without food.

**L40.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Measure liquid medicine carefully.

**L40.1** `Incomplete Sentence` (0.955) → `excluded_incomplete`
- original: Use the dosing syringe provided, or use a medicine dose-measuring device (not a kitchen spoon).

**L41.0** `Simple Sentence` (0.96) → `passthrough`
- original: You will need frequent medical tests.

**L42.0** `Simple Sentence` (0.801) → `passthrough`
- original: Your doctor may begin to reduce your ergocalciferol dose as your condition improves.

**L42.1** `Incomplete Sentence` (0.947) → `excluded_incomplete`
- original: Carefully follow all instructions about adjusting your dose.

**L42.2** `Complex Sentence` (0.74) → `decomposed`
- original: In some cases, there may be a very small difference in amount between safe and dangerous doses of this medicine.
- pronoun resolved: In some cases, there may be a very small difference in amount between safe and dangerous doses of ergocalciferol.
  - edits: “this medicine.” → “ergocalciferol.”
  - S1: In some cases, there may be a very small difference in amount.
  - S2: The difference is between safe and dangerous doses.
  - S3: The doses are of ergocalciferol.

**L43.0** `Simple Sentence` (0.976) → `passthrough`
- original: Your doctor will determine how long to treat you with this medicine.

**L44.0** `Simple Sentence` (0.501) → `passthrough`
- original: Ergocalciferol may be only part of a complete program of treatment that also includes dietary changes and taking calcium and vitamin supplements.

**L44.1** `Incomplete Sentence` (0.969) → `excluded_incomplete`
- original: Follow your doctor's instructions very closely.

**L45.0** `Incomplete Sentence` (0.969) → `excluded_incomplete`
- original: Learn about the foods you should eat to make sure you get enough calcium and vitamin D in your diet.

**L45.1** `Simple Sentence` (0.85) → `passthrough`
- original: Your ergocalciferol dose may need to be adjusted as you make changes to your diet.

**L46.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Store at room temperature away from moisture, heat, and light.

## What happens if I miss a dose?

**L49.0** `Compound Sentence` (0.555) → `decomposed`
- original: Take the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - S1: Take the medicine as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L49.1** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

## What happens if I overdose?

**L52.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L52.1** `Simple Sentence` (0.987) → `passthrough`
- original: An overdose of vitamin D can cause serious or life-threatening side effects.

**L53.0** `Compound Sentence` (0.485) → `decomposed`
- original: Overdose symptoms may include nausea, loss of appetite, thirst, urinating more or less than usual, body aches, stiffness, confusion, or irregular heartbeats.
  - S1: Overdose symptoms may include nausea.
  - S2: Overdose symptoms may include loss of appetite.
  - S3: Overdose symptoms may include thirst.
  - S4: Overdose symptoms may include urinating more or less than usual.
  - S5: Overdose symptoms may include body aches.
  - S6: Overdose symptoms may include stiffness.
  - S7: Overdose symptoms may include confusion.
  - S8: Overdose symptoms may include irregular heartbeats.

## What should I avoid while taking ergocalciferol?

**L56.0** `Incomplete Sentence` (0.489) → `excluded_incomplete`
- original: Ask a doctor or pharmacist before taking any multivitamins, mineral supplements, or antacids while you are taking ergocalciferol.

## What other drugs will affect ergocalciferol?

**L59.0** `Complex Sentence` (0.7) → `decomposed`
- original: Certain medications can make it harder for your body to absorb vitamin D. If you take other medications, take them at least 2 hours before or 2 hours after you take ergocalciferol.
- pronoun resolved: Certain medications can make it harder for your body to absorb vitamin D. If you take other medications, take other medications at least 2 hours before or 2 hours after you take ergocalciferol.
  - edits: “them” → “other medications”
  - S1: Certain medications can make it harder for your body to absorb vitamin D.
  - S2: If you take other medications, take them at least 2 hours before or 2 hours after you take ergocalciferol.

**L60.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Tell your doctor about all your other medicines, especially:

**L61.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a diuretic or "water pill"; or

**L62.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: mineral oil (sometimes taken as a laxative).

**L63.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L63.1** `Complex Sentence` (0.663) → `decomposed`
- original: Other drugs may affect ergocalciferol, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may affect ergocalciferol.
  - S2: These other drugs include prescription and over-the-counter medicines.
  - S3: These other drugs also include vitamins and herbal products.

**L63.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.

**L64.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Check interactions

**L65.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Compare alternatives

**L66.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Pricing & coupons

**L67.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Reviews (34)

**L68.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Drug images

**L69.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Side effects

**L70.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Dosage information

**L71.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: During pregnancy

**L72.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Drug class: vitamins

**L73.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: En español

**L74.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Patient resources:

**L75.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Other brands:

**L76.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Drisdol, Calciferol, Calcidol

**L77.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Professional resources:

**L78.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Ergocalciferol monograph

**L79.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Ergocalciferol (FDA)

**L80.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Vitamin D Ergocalciferol (FDA)

**L81.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Other brands:

**L82.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Drisdol

**L83.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Related treatment guides:

**L84.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Hypoparathyroidism

**L85.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Familial Hypophosphatemia

**L86.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Hypophosphatemia

**L87.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Hypocalcemia
