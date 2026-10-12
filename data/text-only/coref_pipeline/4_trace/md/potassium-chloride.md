# Potassium Chloride — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/potassium-chloride.txt` · 97 sentences · 4 changed by pronoun resolution · 138 sentences sent to EDC

## What is potassium chloride?

**L5.0** `Complex Sentence` (0.496) → `decomposed`
- original: Potassium is a mineral that is found in many foods and is needed for several functions of your body, especially the beating of your heart.
  - S1: Potassium is a mineral.
  - S2: Potassium is found in many foods.
  - S3: Potassium is needed for several functions of your body.
  - S4: These functions include the beating of your heart.

**L6.0** `Simple Sentence` (0.948) → `passthrough`
- original: Potassium chloride is used to prevent or to treat low blood levels of potassium (hypokalemia).

**L7.0** `Compound Sentence` (0.655) → `decomposed`
- original: Potassium levels can be low as a result of a disease or from taking certain medicines, or after a prolonged illness with diarrhea or vomiting.
  - S1: Potassium levels can be low as a result of a disease.
  - S2: Potassium levels can be low from taking certain medicines.
  - S3: Potassium levels can be low after a prolonged illness with diarrhea or vomiting.

## Warnings

**L10.0** `Compound Sentence` (0.629) → `decomposed`
- original: You should not use potassium chloride if you have high levels of potassium in your blood (hyperkalemia), or if you also take a "potassium-sparing" diuretic.
  - S1: You should not use potassium chloride if you have high levels of potassium in your blood (hyperkalemia).
  - S2: You should not use potassium chloride if you also take a "potassium-sparing" diuretic.

**L11.0** `Complex Sentence` (0.794) → `decomposed`
- original: To be sure potassium chloride is helping your condition, your blood may need to be tested often.
  - S1: To be sure potassium chloride is helping your condition.
  - S2: Your blood may need to be tested often.

**L11.1** `Complex Sentence` (0.625) → `decomposed`
- original: Your heart rate may also be checked using an electrocardiograph or ECG (sometimes called an EKG) to measure electrical activity of the heart.
  - S1: Your heart rate may also be checked.
  - S2: The heart rate can be checked using an electrocardiograph or ECG.
  - S3: An electrocardiograph or ECG is sometimes called an EKG.
  - S4: The device is used to measure electrical activity of the heart.

**L11.2** `Simple Sentence` (0.967) → `passthrough`
- original: This test will help your doctor determine how long to treat you with potassium.

**L11.3** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: Do not miss any scheduled appointments.

**L12.0** `Compound Sentence` (0.721) → `decomposed`
- original: Serious side effects of potassium include uneven heartbeat, muscle weakness or limp feeling, severe stomach pain, and numbness or tingling in your hands, feet, or mouth.
  - S1: Serious side effects of potassium include uneven heartbeat.
  - S2: They include muscle weakness or limp feeling.
  - S3: They include severe stomach pain.
  - S4: They include numbness or tingling in your hands, feet, or mouth.

**L13.0** `Simple Sentence` (0.657) → `passthrough`
- original: Do not stop taking this medicine without first talking to your doctor.

**L13.1** `Simple Sentence` (0.834) → `passthrough`
- original: If you stop taking this medicine suddenly, your condition may become worse.

**L14.0** `Incomplete Sentence` (0.514) → `excluded_incomplete`
- original: Do not crush, chew, or suck on an extended-release tablet or capsule.

**L14.1** `Incomplete Sentence` (0.966) → `excluded_incomplete`
- original: Swallow the pill whole unless your doctor or pharmacist tells you your specific tablet can be broken.

**L14.2** `Simple Sentence` (0.973) → `passthrough`
- original: Crushing or chewing the pill may cause too much of the drug to be released at one time.

**L14.3** `Simple Sentence` (0.98) → `passthrough`
- original: Sucking on a tablet can irritate your mouth or throat.

**L14.4** `Incomplete Sentence` (0.969) → `excluded_incomplete`
- original: Take potassium chloride with food or just after a meal.

## Before taking this medicine

**L17.0** `Incomplete Sentence` (0.793) → `excluded_incomplete`
- original: You should not use potassium chloride if you are allergic to it, or if:
- pronoun resolved: You should not use potassium chloride if you are allergic to potassium chloride, or if:
  - edits: “it,” → “potassium chloride,”

**L18.0** `Incomplete Sentence` (0.971) → `excluded_incomplete`
- original: you have high levels of potassium in your blood (hyperkalemia); or

**L19.0** `Simple Sentence` (0.891) → `passthrough`
- original: you take a "potassium-sparing" diuretic (water pill) such as amiloride, spironolactone, or triamterene.

**L20.0** `Simple Sentence` (0.59) → `passthrough`
- original: To make sure this medicine is safe for you, tell your doctor if you have ever had:

**L21.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: kidney disease;

**L22.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: cirrhosis or other liver disease;

**L23.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: an adrenal gland disorder;

**L24.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a large tissue injury such as a severe burn;

**L25.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: severe dehydration;

**L26.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: diabetes;

**L27.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: heart disease or high blood pressure;

**L28.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: stomach or intestinal bleeding;

**L29.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a blockage in your stomach or intestines; or

**L30.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: chronic diarrhea (such as ulcerative colitis, Crohn's disease).

**L31.0** `Simple Sentence` (0.982) → `passthrough`
- original: It is not known whether this medicine will harm an unborn baby.

**L31.1** `Simple Sentence` (0.99) → `passthrough`
- original: Your dose needs may be different during pregnancy.

**L31.2** `Incomplete Sentence` (0.952) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or breastfeeding.

**L32.0** `Incomplete Sentence` (0.655) → `excluded_incomplete`
- original: Do not give this medicine to a child without medical advice.

## How should I take potassium chloride?

**L35.0** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: Take potassium chloride exactly as prescribed by your doctor.

**L35.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L35.2** `Simple Sentence` (0.984) → `passthrough`
- original: Your doctor may occasionally change your dose.

**L36.0** `Incomplete Sentence` (0.96) → `excluded_incomplete`
- original: Read and carefully follow any Instructions for Use provided with your medicine.

**L36.1** `Incomplete Sentence` (0.902) → `excluded_incomplete`
- original: Ask your doctor or pharmacist if you do not understand these instructions.

**L37.0** `Incomplete Sentence` (0.948) → `excluded_incomplete`
- original: Take potassium chloride with a full glass of water.

**L37.1** `Incomplete Sentence` (0.969) → `excluded_incomplete`
- original: Take potassium chloride with food or just after a meal.

**L38.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Measure liquid medicine with the dosing syringe provided, or with a special dose-measuring spoon or medicine cup.

**L38.1** `Simple Sentence` (0.75) → `passthrough`
- original: If you do not have a dose-measuring device, ask your pharmacist for one.

**L39.0** `Incomplete Sentence` (0.793) → `excluded_incomplete`
- original: Do not crush, chew, or suck on a tablet or capsule.

**L39.1** `Simple Sentence` (0.972) → `passthrough`
- original: Sucking on the pill could irritate your mouth or throat.

**L40.0** `Incomplete Sentence` (0.862) → `excluded_incomplete`
- original: Call your doctor if you have trouble swallowing a potassium chloride capsule or tablet.

**L40.1** `Compound Sentence` (0.826) → `decomposed`
- original: You may be able to dissolve the tablet in water, or mix the medicine from a capsule with soft food.
  - S1: You may be able to dissolve the tablet in water.
  - S2: You may be able to mix the medicine from a capsule with soft food.

**L40.2** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Carefully follow your doctor's instructions.

**L41.0** `Incomplete Sentence` (0.943) → `excluded_incomplete`
- original: Mix the powder form of this medicine with at least 4 ounces (one-half cup) of cold water or fruit juice before taking.

**L41.1** `Incomplete Sentence` (0.972) → `excluded_incomplete`
- original: Drink the mixture slowly, over 5 to 10 minutes in all.

**L41.2** `Simple Sentence` (0.374) → `passthrough`
- original: To make sure you get the entire dose, add a little more water to the same glass, swirl gently and drink right away.

**L42.0** `Simple Sentence` (0.585) → `passthrough`
- original: To be sure this medicine is helping your condition, you may need frequent blood tests.

**L42.1** `Compound Sentence` (0.928) → `decomposed`
- original: You may not notice any change in your symptoms, but your blood work will help your doctor determine how long to treat you with potassium chloride.
  - S1: You may not notice any change in your symptoms.
  - S2: Your blood work will help your doctor determine how long to treat you with potassium chloride.

**L42.2** `Simple Sentence` (0.427) → `passthrough`
- original: Your heart function may need to be checked using an electrocardiograph or ECG (sometimes called an EKG).

**L42.3** `Complex Sentence` (0.938) → `decomposed`
- original: Even if you have no symptoms, tests can help your doctor determine if this medicine is effective.
- pronoun resolved: Even if you have no symptoms, tests can help your doctor determine if potassium chloride is effective.
  - edits: “this medicine” → “potassium chloride”
  - S1: Tests can help your doctor determine if potassium chloride is effective.
  - S2: This is true even if you have no symptoms.

**L43.0** `Simple Sentence` (0.979) → `passthrough`
- original: Your treatment may include a special diet.

**L43.1** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Follow the diet plan created for you by your doctor or nutrition counselor.

**L43.2** `Incomplete Sentence` (0.823) → `excluded_incomplete`
- original: Get familiar with the list of foods you should eat or avoid to help control your condition.

**L44.0** `Complex Sentence` (0.425) → `decomposed`
- original: Potassium-rich foods include: squash, baked potatoes (skin on), spinach, lentils, broccoli, Brussels sprouts, zucchini, kidney or navy beans, raisins, watermelon, orange juice, bananas, cantaloupe, and low-fat milk or yogurt.
  - S1: Potassium-rich foods include squash.
  - S2: Potassium-rich foods include baked potatoes with skin on.
  - S3: Potassium-rich foods include spinach.
  - S4: Potassium-rich foods include lentils.
  - S5: Potassium-rich foods include broccoli.
  - S6: Potassium-rich foods include Brussels sprouts.
  - S7: Potassium-rich foods include zucchini.
  - S8: Potassium-rich foods include kidney or navy beans.
  - S9: Potassium-rich foods include raisins.
  - S10: Potassium-rich foods include watermelon.
  - S11: Potassium-rich foods include orange juice.
  - S12: Potassium-rich foods include bananas.
  - S13: Potassium-rich foods include cantaloupe.
  - S14: Potassium-rich foods include low-fat milk or yogurt.

**L44.1** `Incomplete Sentence` (0.946) → `excluded_incomplete`
- original: Consume only the daily amounts recommended by your doctor or nutrition counselor.

**L45.0** `Simple Sentence` (0.969) → `passthrough`
- original: Some tablets are made with a shell that is not absorbed or melted in the body.

**L45.1** `Simple Sentence` (0.984) → `passthrough`
- original: Part of this shell may appear in your stool.

**L45.2** `Simple Sentence` (0.931) → `passthrough`
- original: This is normal and will not make the medicine less effective.
- pronoun resolved: Shell is normal and will not make the medicine less effective.
  - edits: “This” → “Shell”

**L46.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Store at room temperature away from moisture and heat.

**L46.1** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: Keep the medication in a closed container.

## What happens if I miss a dose?

**L49.0** `Incomplete Sentence` (0.926) → `excluded_incomplete`
- original: Take the missed dose as soon as you remember.

**L49.1** `Incomplete Sentence` (0.89) → `excluded_incomplete`
- original: Skip the missed dose if it is almost time for your next scheduled dose.

**L49.2** `Incomplete Sentence` (0.748) → `excluded_incomplete`
- original: Do not take extra medicine to make up the missed dose.

## What happens if I overdose?

**L52.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L53.0** `Simple Sentence` (0.829) → `passthrough`
- original: Overdose symptoms may include irregular heartbeats, chest pain, or muscle weakness.

## What to avoid

**L56.0** `Incomplete Sentence` (0.96) → `excluded_incomplete`
- original: Avoid taking supplements or using other products that contain potassium without first asking your doctor.

**L56.1** `Simple Sentence` (0.986) → `passthrough`
- original: Salt substitutes or low-salt dietary products often contain potassium.

**L56.2** `Simple Sentence` (0.981) → `passthrough`
- original: If you take certain products together you may accidentally get too much potassium.

**L56.3** `Incomplete Sentence` (0.95) → `excluded_incomplete`
- original: Read the label of any other medicine you are using to see if it contains potassium.

## Potassium chloride side effects

**L59.0** `Compound Sentence` (0.35) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to potassium chloride: hives; difficult breathing; swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to potassium chloride.
  - S2: Signs of an allergic reaction to potassium chloride include hives.
  - S3: Signs of an allergic reaction to potassium chloride include difficult breathing.
  - S4: Signs of an allergic reaction to potassium chloride include swelling of your face, lips, tongue, or throat.

**L60.0** `Incomplete Sentence` (0.808) → `excluded_incomplete`
- original: Stop using this medicine and call your doctor at once if you have:

**L61.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: severe throat irritation;

**L62.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: stomach bloating, severe vomiting, severe stomach pain;

**L63.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: high potassium level - nausea, weakness, tingly feeling, chest pain, irregular heartbeats, loss of movement; or

**L64.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: signs of stomach bleeding - bloody or tarry stools, coughing up blood or vomit that looks like coffee grounds.

**L65.0** `Simple Sentence` (0.933) → `passthrough`
- original: Common potassium chloride side effects may include:

**L66.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: nausea, vomiting, diarrhea;

**L67.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: gas, stomach pain; or

**L68.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: the appearance of a potassium chloride tablet in your stool.

**L69.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L69.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L69.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## What other drugs will affect potassium chloride?

**L72.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Tell your doctor about all your current medicines and any you start or stop using, especially:

**L73.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a diuretic or "water pill"; or

**L74.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: heart or blood pressure medication.

**L75.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: NSAIDs (nonsteroidal anti-inflammatory drugs) such as aspirin, ibuprofen, naproxen, celecoxib, diclofenac, indomethacin, or meloxicam.

**L76.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L76.1** `Complex Sentence` (0.706) → `decomposed`
- original: Other drugs may interact with potassium chloride, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may interact with potassium chloride.
  - S2: These drugs include prescription and over-the-counter medicines.
  - S3: These drugs also include vitamins and herbal products.

**L76.2** `Simple Sentence` (0.986) → `passthrough`
- original: Not all possible interactions are listed in this medication guide.

## Popular FAQ

**L79.0** `Incomplete Sentence` (0.806) → `excluded_incomplete`
- original: Q: Can you eat bananas when taking losartan?

**L79.1** `Simple Sentence` (0.622) → `passthrough`
- original: A: Most people taking losartan can eat bananas, or any other food naturally high in potassium.

**L79.2** `Compound-Complex Sentence` (0.611) → `decomposed`
- original: But people with poor kidney function, heart failure, a history of high potassium, or who also take certain diuretics, such as spironolactone, should be cautious about eating foods high in potassium and ask their doctor to monitor their potassium levels.
- pronoun resolved: But people with poor kidney function, heart failure, a history of high potassium, or who also take certain diuretics, such as spironolactone, should be cautious about eating foods high in potassium and ask people's doctor to monitor people's potassium levels.
  - edits: “their” → “people's”; “their” → “people's”
  - S1: People with poor kidney function should be cautious about eating foods high in potassium.
  - S2: People with heart failure should be cautious about eating foods high in potassium.
  - S3: People with a history of high potassium should be cautious about eating foods high in potassium.
  - S4: People who take certain diuretics, such as spironolactone, should be cautious about eating foods high in potassium.
  - S5: People with poor kidney function should ask their doctor to monitor their potassium levels.
  - S6: People with heart failure should ask their doctor to monitor their potassium levels.
  - S7: People with a history of high potassium should ask their doctor to monitor their potassium levels.
  - S8: People who take certain diuretics, such as spironolactone, should ask their doctor to monitor their potassium levels.
