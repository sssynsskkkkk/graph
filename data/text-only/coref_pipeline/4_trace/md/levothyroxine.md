# Levothyroxine — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/levothyroxine.txt` · 214 sentences · 33 changed by pronoun resolution · 345 sentences sent to EDC

## What is levothyroxine?

**L5.0** `Simple Sentence` (0.632) → `passthrough`
- original: Levothyroxine is a man-made form of thyroxine (T4), one of the hormones your thyroid gland normally produces.

**L5.1** `Compound Sentence` (0.964) → `decomposed`
- original: It belongs to a class of medications called hormones, and it works by replacing thyroid hormone that your body is not making enough of.
- pronoun resolved: Levothyroxine belongs to a class of medications called hormones, and Levothyroxine works by replacing thyroid hormone that your body is not making enough of.
  - edits: “It” → “Levothyroxine”; “it” → “Levothyroxine”
  - S1: Levothyroxine belongs to a class of medications called hormones.
  - S2: Levothyroxine works by replacing thyroid hormone that your body is not making enough of.

**L6.0** `Simple Sentence` (0.984) → `passthrough`
- original: Levothyroxine is used in adults and children, including newborn babies, to:

**L7.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: treat hypothyroidism (underactive thyroid - a condition where the thyroid gland does not produce enough thyroid hormone).

**L7.1** `Compound Sentence` (0.684) → `decomposed`
- original: It replaces the missing hormone whether the condition was present from birth or developed later, and whether the problem starts in the thyroid gland itself or in the pituitary gland or hypothalamus; and
- pronoun resolved: Levothyroxine replaces the missing hormone whether the condition was present from birth or developed later, and whether the problem starts in the thyroid gland itself or in the pituitary gland or hypothalamus; and
  - edits: “It” → “Levothyroxine”
  - S1: Levothyroxine replaces the missing hormone whether the condition was present from birth or developed later.
  - S2: It replaces the missing hormone whether the problem starts in the thyroid gland itself or in the pituitary gland or hypothalamus.

**L8.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: lower the level of thyroid-stimulating hormone (TSH) in the blood in people being treated for a certain type of thyroid cancer, alongside surgery and radioactive iodine therapy.

**L9.0** `Complex Sentence` (0.587) → `decomposed`
- original: Levothyroxine injection is used in adults to treat myxedema coma, a rare and life-threatening complication of a severely underactive thyroid.
  - S1: Levothyroxine injection is used in adults to treat myxedema coma.
  - S2: Myxedema coma is a rare and life-threatening complication.
  - S3: Myxedema coma is a complication of a severely underactive thyroid.

**L10.0** `Simple Sentence` (0.98) → `passthrough`
- original: Without thyroid hormone, your body cannot function properly.

**L10.1** `Compound Sentence` (0.561) → `decomposed`
- original: This may result in poor growth, slow speech, lack of energy, excessive tiredness, constipation, weight gain, hair loss, dry, thick skin, increased sensitivity to cold, joint and muscle pain, heavy or irregular menstrual periods, and depression.
  - S1: This may result in poor growth.
  - S2: It may result in slow speech.
  - S3: It may result in a lack of energy.
  - S4: It may result in excessive tiredness.
  - S5: It may result in constipation.
  - S6: It may result in weight gain.
  - S7: It may result in hair loss.
  - S8: It may result in dry, thick skin.
  - S9: It may result in increased sensitivity to cold.
  - S10: It may result in joint and muscle pain.
  - S11: It may result in heavy or irregular menstrual periods.
  - S12: It may result in depression.

**L10.2** `Compound Sentence` (0.857) → `decomposed`
- original: When taken correctly, levothyroxine reverses these symptoms, although it may take several weeks before you notice a difference.
- pronoun resolved: When taken correctly, levothyroxine reverses these symptoms, although levothyroxine may take several weeks before you notice a difference.
  - edits: “it” → “levothyroxine”
  - S1: When taken correctly, levothyroxine reverses these symptoms.
  - S2: Levothyroxine may take several weeks before you notice a difference.

**L11.0** `Simple Sentence` (0.99) → `passthrough`
- original: Levothyroxine is usually taken for life.

**L12.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: What levothyroxine is not used for:

**L13.0** `Complex Sentence` (0.553) → `decomposed`
- original: Levothyroxine is not used to shrink benign (noncancerous) thyroid nodules or a nontoxic diffuse goiter in people who get enough iodine in their diet.
  - S1: Levothyroxine is not used to shrink benign thyroid nodules.
  - S2: Levothyroxine is not used to shrink a nontoxic diffuse goiter.
  - S3: This applies to people who get enough iodine in their diet.

**L13.1** `Compound Sentence` (0.965) → `decomposed`
- original: It does not help in these situations, and taking more thyroid hormone than your body needs can cause an overactive thyroid.
- pronoun resolved: Levothyroxine does not help in these situations, and taking more thyroid hormone than your body needs can cause an overactive thyroid.
  - edits: “It” → “Levothyroxine”
  - S1: Levothyroxine does not help in these situations.
  - S2: Taking more thyroid hormone than your body needs can cause an overactive thyroid.

**L13.2** `Complex Sentence` (0.593) → `decomposed`
- original: It is also not used to treat hypothyroidism during the recovery phase of subacute thyroiditis (inflammation of the thyroid gland).
- pronoun resolved: Levothyroxine is also not used to treat hypothyroidism during the recovery phase of subacute thyroiditis (inflammation of the thyroid gland).
  - edits: “It” → “Levothyroxine”
  - S1: Levothyroxine is not used to treat hypothyroidism.
  - S2: This applies during the recovery phase of subacute thyroiditis.
  - S3: Subacute thyroiditis is inflammation of the thyroid gland.

**L14.0** `Simple Sentence` (0.977) → `passthrough`
- original: Levothyroxine is not used to treat obesity or for weight loss.

## Levothyroxine side effects

**L17.0** `Compound Sentence` (0.43) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to levothyroxine: hives, difficult breathing, swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to levothyroxine.
  - S2: Signs of an allergic reaction to levothyroxine include hives, difficult breathing, and swelling of your face, lips, tongue, or throat.

**L17.1** `Compound Sentence` (0.893) → `decomposed`
- original: Allergic reactions are usually caused by the inactive ingredients in a product rather than by levothyroxine itself, so your doctor may suggest trying a different brand or form.
  - S1: Allergic reactions are usually caused by the inactive ingredients in a product rather than by levothyroxine itself.
  - S2: Your doctor may suggest trying a different brand or form.

**L18.0** `Simple Sentence` (0.99) → `passthrough`
- original: Levothyroxine may cause serious side effects.

**L18.1** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L19.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: sudden pain or trouble moving your hip, wrist, or back;

**L20.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: fast or irregular heartbeats, or a pounding heartbeat;

**L21.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: chest pain, pain spreading to your jaw or shoulder;

**L22.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: wheezing or shortness of breath;

**L23.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: swelling in your legs or ankles, or new or worsening breathlessness when lying down;

**L24.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: fever, swollen glands, itching, joint pain, or not feeling well;

**L25.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: nausea, vomiting, or diarrhea;

**L26.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: confusion or feeling disoriented;

**L27.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a seizure; or

**L28.0** `Incomplete Sentence` (0.83) → `excluded_incomplete`
- original: high blood sugar - increased thirst, increased urination, dry mouth, fruity breath odor.

**L29.0** `Simple Sentence` (0.97) → `passthrough`
- original: Common levothyroxine side effects may include:

**L30.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: fever, hot flashes, increased sweating, feeling too hot;

**L31.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: tiredness;

**L32.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: skin rash, flushing, hair loss;

**L33.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: chest pain, fast or irregular heartbeats, shortness of breath;

**L34.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: headache, leg cramps, muscle cramps, muscle pain or weakness;

**L35.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: tremors, feeling nervous, anxious, irritable, or emotional, sleep problems (insomnia);

**L36.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: increased or change in appetite;

**L37.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: weight loss or weight gain;

**L38.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: changes in your menstrual periods, or difficulty getting pregnant; or

**L39.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: stomach cramps, vomiting, diarrhea.

**L40.0** `Complex Sentence` (0.917) → `decomposed`
- original: Most of these side effects happen when the levothyroxine dose is higher than your body needs, which produces symptoms of an overactive thyroid.
  - S1: Most of these side effects happen when the levothyroxine dose is higher than your body needs.
  - S2: This situation produces symptoms of an overactive thyroid.

**L40.1** `Incomplete Sentence` (0.458) → `excluded_incomplete`
- original: Tell your doctor if you have any of them so your dose can be checked.
- pronoun resolved: Tell your doctor if you have any of symptoms so your dose can be checked.
  - edits: “them” → “symptoms”

**L41.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Side effects in children:

**L42.0** `Compound-Complex Sentence` (0.782) → `decomposed`
- original: Children taking levothyroxine may also develop increased pressure around the brain (which can cause headaches, vomiting, or vision changes) or a hip problem called slipped capital femoral epiphysis, which causes hip, groin, or knee pain and limping.
  - S1: Children taking levothyroxine may develop increased pressure around the brain.
  - S2: Increased pressure around the brain can cause headaches.
  - S3: Increased pressure around the brain can cause vomiting.
  - S4: Increased pressure around the brain can cause vision changes.
  - S5: Children taking levothyroxine may develop a hip problem called slipped capital femoral epiphysis.
  - S6: Slipped capital femoral epiphysis causes hip pain.
  - S7: Slipped capital femoral epiphysis causes groin pain.
  - S8: Slipped capital femoral epiphysis causes knee pain.
  - S9: Slipped capital femoral epiphysis causes limping.

**L42.1** `Incomplete Sentence` (0.939) → `excluded_incomplete`
- original: Call your child's doctor about any of these symptoms.

**L43.0** `Compound-Complex Sentence` (0.832) → `decomposed`
- original: Too much levothyroxine in babies can cause the soft spots on the skull to close too early, and in older children it can cause the growth plates to close too early, which may reduce final adult height.
- pronoun resolved: Too much levothyroxine in babies can cause the soft spots on the skull to close too early, and in older children Too much levothyroxine can cause the growth plates to close too early, which may reduce final adult height.
  - edits: “it” → “Too much levothyroxine”
  - S1: Too much levothyroxine in babies can cause the soft spots on the skull to close too early.
  - S2: Too much levothyroxine in older children can cause the growth plates to close too early.
  - S3: Closing of the growth plates may reduce final adult height.

**L43.1** `Simple Sentence` (0.989) → `passthrough`
- original: Too little levothyroxine can affect a child's learning and growth.

**L43.2** `Simple Sentence` (0.975) → `passthrough`
- original: This is why children need regular blood tests and check-ups.

**L44.0** `Compound Sentence` (0.545) → `decomposed`
- original: This is not a complete list of side effects, and others may occur.
  - S1: This is not a complete list of side effects.
  - S2: Others may occur.

**L44.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L44.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## Warnings

**L47.0** `Simple Sentence` (0.982) → `passthrough`
- original: Levothyroxine should not be used to treat obesity or weight problems.

**L47.1** `Complex Sentence` (0.88) → `decomposed`
- original: Dangerous side effects or death can occur from the misuse of this medicine, especially if you are taking any other weight-loss medications or appetite suppressants.
- pronoun resolved: Dangerous side effects or death can occur from the misuse of Levothyroxine, especially if you are taking any other weight-loss medications or appetite suppressants.
  - edits: “this medicine,” → “Levothyroxine,”
  - S1: Dangerous side effects or death can occur from the misuse of Levothyroxine.
  - S2: This risk is especially high if you are taking other weight-loss medications.
  - S3: This risk is especially high if you are taking appetite suppressants.

**L48.0** `Compound Sentence` (0.962) → `decomposed`
- original: Taking more than your recommended dose will not make this medicine more effective, and may cause serious side effects.
- pronoun resolved: Taking more than your recommended dose will not make Levothyroxine more effective, and may cause serious side effects.
  - edits: “this medicine” → “Levothyroxine”
  - S1: Taking more than your recommended dose will not make Levothyroxine more effective.
  - S2: Taking more than your recommended dose may cause serious side effects.

**L49.0** `Complex Sentence` (0.709) → `decomposed`
- original: Levothyroxine has a narrow therapeutic index, which means the difference between too little and too much is small.
  - S1: Levothyroxine has a narrow therapeutic index.
  - S2: This means the difference between too little and too much is small.

**L49.1** `Compound Sentence` (0.813) → `decomposed`
- original: Taking too much or too little over time can affect your heart, bones, blood sugar, cholesterol, digestion, memory and concentration, fertility, and, in children, growth and development.
  - S1: Taking too much or too little over time can affect your heart.
  - S2: It can affect your bones.
  - S3: It can affect your blood sugar.
  - S4: It can affect your cholesterol.
  - S5: It can affect your digestion.
  - S6: It can affect your memory and concentration.
  - S7: It can affect your fertility.
  - S8: In children, it can affect growth and development.

**L49.2** `Simple Sentence` (0.714) → `passthrough`
- original: Your doctor will start you on a suitable dose and adjust it gradually based on blood tests.
- pronoun resolved: Your doctor will start you on a suitable dose and adjust dose gradually based on blood tests.
  - edits: “it” → “dose”

**L50.0** `Simple Sentence` (0.974) → `passthrough`
- original: You may not be able to use levothyroxine if you have certain medical conditions.

**L50.1** `Incomplete Sentence` (0.71) → `excluded_incomplete`
- original: Tell your doctor if you have an untreated or uncontrolled adrenal gland disorder or any heart problems such as a recent heart attack.

**L51.0** `Complex Sentence` (0.89) → `decomposed`
- original: If you have an adrenal gland problem, you will need to start treatment with a steroid (glucocorticoid) medicine before you start levothyroxine.
  - S1: You will need to start treatment with a steroid (glucocorticoid) medicine.
  - S2: You will need to start levothyroxine.
  - S3: You must start the steroid medicine before you start levothyroxine.
  - S4: This is required if you have an adrenal gland problem.

**L51.1** `Simple Sentence` (0.876) → `passthrough`
- original: Starting levothyroxine first can trigger a sudden, serious drop in adrenal hormones known as an adrenal crisis.

**L52.0** `Complex Sentence` (0.792) → `decomposed`
- original: Older adults and people with heart disease are usually started on a lower dose, because too much thyroid hormone can cause an irregular heartbeat (most commonly atrial fibrillation), angina, or other heart problems.
  - S1: Older adults and people with heart disease are usually started on a lower dose.
  - S2: This is because too much thyroid hormone can cause an irregular heartbeat, angina, or other heart problems.
  - S3: The irregular heartbeat is most commonly atrial fibrillation.

**L52.1** `Incomplete Sentence` (0.828) → `excluded_incomplete`
- original: Tell your doctor if you develop chest pain, breathlessness, or a fast or irregular heartbeat.

**L53.0** `Simple Sentence` (0.667) → `passthrough`
- original: Taking more levothyroxine than your body needs over a long period can weaken your bones and lead to a higher risk of fractures.

**L53.1** `Simple Sentence` (0.989) → `passthrough`
- original: This is more likely after menopause.

**L53.2** `Simple Sentence` (0.943) → `passthrough`
- original: Your doctor will aim to give you the lowest dose that controls your thyroid levels.

**L54.0** `Simple Sentence` (0.989) → `passthrough`
- original: Oral levothyroxine should not be used to treat myxedema coma.

**L54.1** `Simple Sentence` (0.981) → `passthrough`
- original: Levothyroxine given into a vein is used instead.

## Before taking this medicine

**L57.0** `Simple Sentence` (0.959) → `passthrough`
- original: You should not use levothyroxine if you have an untreated or uncontrolled adrenal gland disorder.

**L58.0** `Complex Sentence` (0.458) → `decomposed`
- original: You should not use certain liquid or injectable forms of levothyroxine if you are allergic to glycerin or edetate disodium.
  - S1: You should not use certain liquid or injectable forms of levothyroxine.
  - S2: This applies if you are allergic to glycerin.
  - S3: This also applies if you are allergic to edetate disodium.

**L59.0** `Simple Sentence` (0.75) → `passthrough`
- original: To make sure this medicine is safe for you, tell your doctor if you have ever had:
- pronoun resolved: To make sure Levothyroxine is safe for you, tell your doctor if you have ever had:
  - edits: “this medicine” → “Levothyroxine”

**L60.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a thyroid nodule;

**L61.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: thyroiditis (inflammation of the thyroid gland);

**L62.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: heart problems such as a heart attack, stroke, angina, or an irregular heartbeat;

**L63.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a blood clot or a blood clotting disorder;

**L64.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: diabetes (your diabetes medicine may need to be adjusted);

**L65.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: anemia (low red blood cells);

**L66.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: weak bones (osteoporosis), or low bone mineral density;

**L67.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: problems with your pituitary or adrenal gland;

**L68.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: an allergy to any food or drugs;

**L69.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: recently received radiation therapy with iodine (such as I-131); or

**L70.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: kidney disease.

**L71.0** `Incomplete Sentence` (0.915) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or plan to become pregnant.

**L71.1** `Compound Sentence` (0.494) → `decomposed`
- original: Having hypothyroidism during pregnancy may increase the risk of miscarriage, high blood pressure in pregnancy, pre-eclampsia, stillbirth, or premature birth, and untreated hypothyroidism can affect the baby's brain development.
  - S1: Having hypothyroidism during pregnancy may increase the risk of miscarriage.
  - S2: It may also increase the risk of high blood pressure in pregnancy.
  - S3: It may increase the risk of pre-eclampsia.
  - S4: It may increase the risk of stillbirth.
  - S5: It may increase the risk of premature birth.
  - S6: Untreated hypothyroidism can affect the baby's brain development.

**L71.2** `Compound Sentence` (0.972) → `decomposed`
- original: The benefit of treating hypothyroidism outweighs these risks, and levothyroxine should not be stopped during pregnancy.
  - S1: The benefit of treating hypothyroidism outweighs these risks.
  - S2: Levothyroxine should not be stopped during pregnancy.

**L72.0** `Simple Sentence` (0.992) → `passthrough`
- original: Your dose needs are often higher during pregnancy.

**L72.1** `Compound-Complex Sentence` (0.656) → `decomposed`
- original: Your doctor will check your thyroid blood tests as soon as your pregnancy is confirmed and at least once in each trimester, and will usually put you back on your pre-pregnancy dose straight after you give birth, with another blood test 4 to 8 weeks later.
  - S1: Your doctor will check your thyroid blood tests as soon as your pregnancy is confirmed.
  - S2: Your doctor will check your thyroid blood tests at least once in each trimester.
  - S3: Your doctor will usually put you back on your pre-pregnancy dose straight after you give birth.
  - S4: Your doctor will perform another blood test 4 to 8 weeks later.

**L73.0** `Incomplete Sentence` (0.959) → `excluded_incomplete`
- original: Tell your doctor if you are breastfeeding.

**L73.1** `Compound Sentence` (0.929) → `decomposed`
- original: Levothyroxine passes into breast milk, but no harmful effects on breastfed babies have been reported.
  - S1: Levothyroxine passes into breast milk.
  - S2: No harmful effects on breastfed babies have been reported.

**L73.2** `Complex Sentence` (0.463) → `decomposed`
- original: Treating hypothyroidism properly may also help milk supply if it is low.
- pronoun resolved: Treating hypothyroidism properly may also help milk supply if Levothyroxine is low.
  - edits: “it” → “Levothyroxine”
  - S1: Treating hypothyroidism properly may help milk supply.
  - S2: This may happen if Levothyroxine is low.

**L73.3** `Simple Sentence` (0.988) → `passthrough`
- original: Your dose needs may be different while you are nursing.

**L74.0** `Complex Sentence` (0.656) → `decomposed`
- original: You may be more likely to have a broken bone while using levothyroxine, particularly if your dose is higher than you need.
  - S1: You may be more likely to have a broken bone while using levothyroxine.
  - S2: This is particularly true if your dose is higher than you need.

**L74.1** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: Talk with your doctor about ways to keep your bones healthy.

## How should I use levothyroxine?

**L77.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Take levothyroxine exactly as prescribed by your doctor.

**L77.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L77.2** `Simple Sentence` (0.984) → `passthrough`
- original: Your doctor may occasionally change your dose.

**L78.0** `Complex Sentence` (0.789) → `decomposed`
- original: Some brands of levothyroxine have different dosage instructions and/or recommendations of how soon you need to take them before eating food.
- pronoun resolved: Some brands of levothyroxine have different dosage instructions and/or recommendations of how soon you need to take levothyroxine before eating food.
  - edits: “them” → “levothyroxine”
  - S1: Some brands of levothyroxine have different dosage instructions.
  - S2: Some brands of levothyroxine have different recommendations.
  - S3: The recommendations concern how soon you need to take levothyroxine before eating food.

**L78.1** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Always check the instructions on the label.

**L79.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Oral levothyroxine:

**L80.0** `Compound Sentence` (0.771) → `decomposed`
- original: Oral levothyroxine is taken by mouth and is available as tablets, capsules, and an oral solution.
  - S1: Oral levothyroxine is taken by mouth.
  - S2: It is available as tablets, capsules, and an oral solution.

**L81.0** `Incomplete Sentence` (0.863) → `excluded_incomplete`
- original: Keep using this medicine even if you feel well.
- pronoun resolved: Keep using Oral levothyroxine even if you feel well.
  - edits: “this medicine” → “Oral levothyroxine”

**L81.1** `Simple Sentence` (0.959) → `passthrough`
- original: It may take 4 to 6 weeks to get the full benefit of a dose.
- pronoun resolved: Oral levothyroxine may take 4 to 6 weeks to get the full benefit of a dose.
  - edits: “It” → “Oral levothyroxine”

**L82.0** `Compound Sentence` (0.964) → `decomposed`
- original: You will need frequent medical tests, and your next dose may be delayed based on the results.
  - S1: You will need frequent medical tests.
  - S2: Your next dose may be delayed based on the results.

**L83.0** `Simple Sentence` (0.99) → `passthrough`
- original: This medicine can affect the results of certain medical tests.
- pronoun resolved: Oral levothyroxine can affect the results of certain medical tests.
  - edits: “This medicine” → “Oral levothyroxine”

**L83.1** `Incomplete Sentence` (0.862) → `excluded_incomplete`
- original: Tell any doctor who treats you that you are using this medicine.
- pronoun resolved: Tell any doctor who treats you that you are using Oral levothyroxine.
  - edits: “this medicine.” → “Oral levothyroxine.”

**L84.0** `Incomplete Sentence` (0.947) → `excluded_incomplete`
- original: Tell your doctor if you have a planned surgery or dental procedure.

**L85.0** `Compound Sentence` (0.963) → `decomposed`
- original: Taking more than your recommended dose will not make this medicine more effective, and may cause serious side effects.
- pronoun resolved: Taking more than your recommended dose will not make Oral levothyroxine more effective, and may cause serious side effects.
  - edits: “this medicine” → “Oral levothyroxine”
  - S1: Taking more than your recommended dose will not make Oral levothyroxine more effective.
  - S2: Taking more than your recommended dose may cause serious side effects.

**L86.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Tablets and capsules:

**L87.0** `Incomplete Sentence` (0.85) → `excluded_incomplete`
- original: Take levothyroxine tablets and capsules on an empty stomach, at least 30 to 60 minutes before breakfast with a full glass of water.

**L87.1** `Complex Sentence` (0.523) → `decomposed`
- original: A full glass of water is important to avoid choking or gagging, because the tablet can start to break apart quickly.
  - S1: A full glass of water is important.
  - S2: It is important to avoid choking or gagging.
  - S3: The tablet can start to break apart quickly.

**L87.2** `Incomplete Sentence` (0.969) → `excluded_incomplete`
- original: Take the medicine at the same time each day.
- pronoun resolved: Take Oral levothyroxine at the same time each day.
  - edits: “the medicine” → “Oral levothyroxine”

**L88.0** `Incomplete Sentence` (0.702) → `excluded_incomplete`
- original: Swallow the capsule whole and do not crush, chew, break, or open it.

**L88.1** `Incomplete Sentence` (0.901) → `excluded_incomplete`
- original: Tell your doctor if your child cannot swallow a capsule whole.

**L89.0** `Compound-Complex Sentence` (0.711) → `decomposed`
- original: If you cannot swallow a tablet whole, crush the tablet and mix it with 1 or 2 teaspoons of water; give the mixture right away by spoon or dropper and make sure all of it is taken.
- pronoun resolved: If you cannot swallow a tablet whole, crush the tablet and mix it with 1 or 2 teaspoons of water; give the mixture right away by spoon or dropper and make sure all of mixture is taken.
  - edits: “it” → “mixture”
  - S1: You cannot swallow the tablet whole.
  - S2: Crush the tablet.
  - S3: Mix the tablet with 1 or 2 teaspoons of water.
  - S4: Give the mixture right away by spoon or dropper.
  - S5: Make sure all of the mixture is taken.

**L89.1** `Incomplete Sentence` (0.973) → `excluded_incomplete`
- original: Do not save it for later use.
- pronoun resolved: Do not save mixture for later use.
  - edits: “it” → “mixture”

**L89.2** `Incomplete Sentence` (0.561) → `excluded_incomplete`
- original: Do not mix it into soy-based infant formula or other foods that can stop levothyroxine being absorbed.
- pronoun resolved: Do not mix levothyroxine into soy-based infant formula or other foods that can stop levothyroxine being absorbed.
  - edits: “it” → “levothyroxine”

**L90.0** `Incomplete Sentence` (0.582) → `excluded_incomplete`
- original: Keep each tablet or capsule in the blister pack until you are ready to take one.

**L91.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Store at room temperature away from moisture, heat, and light.

**L92.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Oral solution (liquid medicine):

**L93.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Measure liquid medicine with the supplied measuring device (not a kitchen spoon).

**L94.0** `Simple Sentence` (0.985) → `passthrough`
- original: Dosages are based on weight in children and teenagers.

**L94.1** `Simple Sentence` (0.931) → `passthrough`
- original: Your child's dose may change if the child gains or loses weight.

**L95.0** `Simple Sentence` (0.623) → `passthrough`
- original: Your dose needs may change if you switch to a different brand, strength, or form of levothyroxine.

**L95.1** `Incomplete Sentence` (0.936) → `excluded_incomplete`
- original: Avoid medication errors by using only the medicine your doctor prescribes.

**L96.0** `Simple Sentence` (0.731) → `passthrough`
- original: Tirosint-Sol oral solution comes in single-dose ampules and can be administered 15 minutes before eating breakfast.

**L96.1** `Incomplete Sentence` (0.855) → `excluded_incomplete`
- original: Squeeze the liquid directly into your mouth, onto a spoon, or into a glass of water to drink right away.

**L96.2** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Use all ampules within 3 months after opening the foil pouch.

**L97.0** `Simple Sentence` (0.885) → `passthrough`
- original: Ermeza and Thyquidity liquids should be taken on an empty stomach, at least 30 to 60 minutes before breakfast.

**L97.1** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Store them in their original bottle.
- pronoun resolved: Store Ermeza and Thyquidity liquids in Ermeza and Thyquidity liquids's original bottle.
  - edits: “them” → “Ermeza and Thyquidity liquids”; “their” → “Ermeza and Thyquidity liquids's”

**L97.2** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Use Ermeza within 90 days and Thyquidity within 8 weeks of opening the bottle.

**L98.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Store at room temperature away from moisture, heat, and light.

**L99.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Intravenous levothyroxine:

**L100.0** `Compound Sentence` (0.887) → `decomposed`
- original: This is given as an injection into a vein by a healthcare provider and should only be used to treat myxedema coma.
- pronoun resolved: Levothyroxine is given as an injection into a vein by a healthcare provider and should only be used to treat myxedema coma.
  - edits: “This” → “Levothyroxine”
  - S1: Levothyroxine is given as an injection into a vein by a healthcare provider.
  - S2: It should only be used to treat myxedema coma.

**L101.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Blood tests, biotin, and monitoring:

**L102.0** `Compound Sentence` (0.869) → `decomposed`
- original: Your doctor will use blood tests to check that your dose is right, usually 6 to 8 weeks after any dose change, and then every 6 to 12 months once your dose is stable.
  - S1: Your doctor will use blood tests to check that your dose is right.
  - S2: This is usually done 6 to 8 weeks after any dose change.
  - S3: Then, blood tests are performed every 6 to 12 months once your dose is stable.

**L102.1** `Compound Sentence` (0.68) → `decomposed`
- original: Children are tested more often, including 2 and 4 weeks after starting treatment and 2 weeks after any dose change.
  - S1: Children are tested more often.
  - S2: They are tested 2 and 4 weeks after starting treatment.
  - S3: They are also tested 2 weeks after any dose change.

**L103.0** `Incomplete Sentence` (0.331) → `excluded_incomplete`
- original: Tell your doctor or pharmacist if you take biotin, or a multivitamin, hair, skin, or nail supplement that contains biotin (sometimes listed as vitamin B7).

**L103.1** `Complex Sentence` (0.875) → `decomposed`
- original: Biotin can interfere with thyroid blood tests and give a falsely high or falsely low result, which could lead to the wrong dose change.
  - S1: Biotin can interfere with thyroid blood tests.
  - S2: This interference can give a falsely high or falsely low result.
  - S3: This could lead to the wrong dose change.

**L103.2** `Incomplete Sentence` (0.97) → `excluded_incomplete`
- original: Stop biotin and any biotin-containing supplements at least 2 days before a thyroid blood test.

**L104.0** `Complex Sentence` (0.623) → `decomposed`
- original: If your symptoms and blood tests still suggest an underactive thyroid even though you are on a dose that should be enough, it may be because the medicine is not being absorbed properly, doses are being missed, or another medicine is interfering.
- pronoun resolved: If your symptoms and blood tests still suggest an underactive thyroid even though you are on a dose that should be enough, an underactive thyroid may be because the medicine is not being absorbed properly, doses are being missed, or another medicine is interfering.
  - edits: “it” → “an underactive thyroid”
  - S1: If your symptoms and blood tests still suggest an underactive thyroid even though you are on a dose that should be enough, an underactive thyroid may be because the medicine is not being absorbed properly.
  - S2: An underactive thyroid may be because doses are being missed.
  - S3: An underactive thyroid may be because another medicine is interfering.

**L104.1** `Incomplete Sentence` (0.881) → `excluded_incomplete`
- original: Talk to your doctor before your dose is increased.

## What happens if I miss a dose?

**L107.0** `Simple Sentence` (0.975) → `passthrough`
- original: In a medical setting, you are not likely to miss a dose of levothyroxine injection.

**L108.0** `Compound Sentence` (0.67) → `decomposed`
- original: Take the missed oral levothyroxine dose as soon as you remember, and then go back to your regular schedule.
  - S1: Take the missed oral levothyroxine dose as soon as you remember.
  - S2: Then go back to your regular schedule.

**L108.1** `Incomplete Sentence` (0.946) → `excluded_incomplete`
- original: Do not use two doses at one time.

## What happens if I overdose?

**L111.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L111.1** `Simple Sentence` (0.984) → `passthrough`
- original: An overdose can be fatal.

**L112.0** `Compound Sentence` (0.459) → `decomposed`
- original: Overdose symptoms may include headache, leg cramps, tremors, feeling nervous or irritable, confusion, chest pain, shortness of breath, fast or pounding heartbeats, stroke, seizures, shock, and coma.
  - S1: Overdose symptoms may include headache.
  - S2: Overdose symptoms may include leg cramps.
  - S3: Overdose symptoms may include tremors.
  - S4: Overdose symptoms may include feeling nervous or irritable.
  - S5: Overdose symptoms may include confusion.
  - S6: Overdose symptoms may include chest pain.
  - S7: Overdose symptoms may include shortness of breath.
  - S8: Overdose symptoms may include fast or pounding heartbeats.
  - S9: Overdose symptoms may include stroke.
  - S10: Overdose symptoms may include seizures.
  - S11: Overdose symptoms may include shock.
  - S12: Overdose symptoms may include coma.

**L112.1** `Compound Sentence` (0.52) → `decomposed`
- original: Symptoms may not appear straight away and can take several days to develop, so get medical advice even if the person seems well.
  - S1: Symptoms may not appear straight away and can take several days to develop.
  - S2: Get medical advice even if the person seems well.

## What should I avoid while using levothyroxine?

**L115.0** `Compound Sentence` (0.409) → `decomposed`
- original: Avoid the following food products within 1 hour of taking oral levothyroxine or the medication will not be as effective: grapefruit juice, infant soy formula, soybean flour, cottonseed meal, walnuts, and high-fiber foods.
- pronoun resolved: Avoid the following food products within 1 hour of taking oral levothyroxine or levothyroxine will not be as effective: grapefruit juice, infant soy formula, soybean flour, cottonseed meal, walnuts, and high-fiber foods.
  - edits: “the medication” → “levothyroxine”
  - S1: Avoid the following food products within 1 hour of taking oral levothyroxine.
  - S2: If you do not avoid these products, levothyroxine will not be as effective.
  - S3: The food products to avoid are grapefruit juice, infant soy formula, soybean flour, cottonseed meal, walnuts, and high-fiber foods.

**L115.1** `Simple Sentence` (0.39) → `passthrough`
- original: Grapefruit juice can both delay absorption and reduce the amount of levothyroxine that gets into your body.

**L116.0** `Complex Sentence` (0.481) → `decomposed`
- original: If you eat or drink any of these regularly, tell your doctor, as your dose may need adjusting.
  - S1: If you eat or drink any of these regularly, tell your doctor.
  - S2: Your dose may need adjusting.

## What other drugs will affect levothyroxine?

**L119.0** `Simple Sentence` (0.978) → `passthrough`
- original: Sometimes it is not safe to use certain medicines at the same time.

**L119.1** `Compound Sentence` (0.567) → `decomposed`
- original: Some drugs can affect your thyroid hormone levels and also make levothyroxine less effective.
  - S1: Some drugs can affect your thyroid hormone levels.
  - S2: Some drugs can also make levothyroxine less effective.

**L120.0** `Simple Sentence` (0.616) → `passthrough`
- original: If you use any of the following drugs, avoid taking them within 4 hours before or 4 hours after you use levothyroxine:

**L121.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: calcium carbonate (Alka-Mints, Caltrate, Os-Cal, Oyster Shell Calcium, Rolaids Soft Chew, Tums, and others);

**L122.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: sevelamer, lanthanum;

**L123.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: cholestyramine, colesevelam, colestipol;

**L124.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: iron supplements, including ferrous sulfate;

**L125.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: sucralfate;

**L126.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: sodium polystyrene sulfonate (Kalexate, Kayexalate, Kionex);

**L127.0** `Compound-Complex Sentence` (0.382) → `decomposed`
- original: stomach acid reducers - esomeprazole, lansoprazole, omeprazole, rabeprazole, Nexium, Prilosec, Prevacid, Protonix, Zegerid, and others (this applies to most brands of levothyroxine except for Tirosint-SOL); or
  - S1: Stomach acid reducers include esomeprazole.
  - S2: Stomach acid reducers include lansoprazole.
  - S3: Stomach acid reducers include omeprazole.
  - S4: Stomach acid reducers include rabeprazole.
  - S5: Stomach acid reducers include Nexium.
  - S6: Stomach acid reducers include Prilosec.
  - S7: Stomach acid reducers include Prevacid.
  - S8: Stomach acid reducers include Protonix.
  - S9: Stomach acid reducers include Zegerid.
  - S10: Stomach acid reducers include other brands.
  - S11: This applies to most brands of levothyroxine.
  - S12: This does not apply to Tirosint-SOL.

**L128.0** `Incomplete Sentence` (0.897) → `excluded_incomplete`
- original: antacids that contain aluminum or magnesium - Gaviscon, Maalox, Milk of Magnesia, Mintox, Mylanta, Pepcid Complete, and others.

**L129.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Tell your doctor about all your other medicines, especially:

**L130.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: orlistat;

**L131.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: phenobarbital, rifampin;

**L132.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: ketamine, steroid medicines such as dexamethasone;

**L133.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: antidepressants such as amitriptyline, maprotiline, or sertraline;

**L134.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: heart or blood pressure medication, including amiodarone, digoxin, propranolol, and other beta blockers;

**L135.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: furosemide given by injection;

**L136.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: seizure medicines such as carbamazepine or phenytoin;

**L137.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: high-dose aspirin, or anti-inflammatory painkillers;

**L138.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: estrogen, birth control pills, or tamoxifen;

**L139.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: testosterone or anabolic steroids;

**L140.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: diabetes medications, including insulin;

**L141.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: cancer medicine such as imatinib;

**L142.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: biotin or supplements that contain biotin; or

**L143.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: a blood thinner - warfarin, Coumadin, Jantoven.

**L144.0** `Compound Sentence` (0.962) → `decomposed`
- original: If you have diabetes, levothyroxine can raise your blood sugar, and you may need more of your diabetes medicine or insulin.
  - S1: If you have diabetes, levothyroxine can raise your blood sugar.
  - S2: You may need more of your diabetes medicine or insulin.

**L144.1** `Compound Sentence` (0.787) → `decomposed`
- original: Check your blood sugar more often when you start, change, or stop levothyroxine, and tell your doctor about any changes.
  - S1: Check your blood sugar more often when you start, change, or stop levothyroxine.
  - S2: Tell your doctor about any changes.

**L145.0** `Simple Sentence` (0.513) → `passthrough`
- original: If you take a blood thinner such as warfarin, levothyroxine can increase its effect.
- pronoun resolved: If you take a blood thinner such as warfarin, levothyroxine can increase levothyroxine's effect.
  - edits: “its” → “levothyroxine's”

**L145.1** `Simple Sentence` (0.895) → `passthrough`
- original: You may need more frequent blood clotting tests and a lower blood thinner dose.

**L146.0** `Compound Sentence` (0.893) → `decomposed`
- original: This list is not complete, and many other drugs may interact with levothyroxine.
  - S1: This list is not complete.
  - S2: Many other drugs may interact with levothyroxine.

**L146.1** `Incomplete Sentence` (0.491) → `excluded_incomplete`
- original: This includes prescription and over-the-counter medicines, vitamins, and herbal products.
- pronoun resolved: List includes prescription and over-the-counter medicines, vitamins, and herbal products.
  - edits: “This” → “List”

**L146.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.

## Popular FAQ

**L149.0** `Incomplete Sentence` (0.96) → `excluded_incomplete`
- original: Q: Does levothyroxine cause weight gain or loss?

**L149.1** `Simple Sentence` (0.935) → `passthrough`
- original: A: In most cases, levothyroxine causes some weight loss.

**L149.2** `Complex Sentence` (0.825) → `decomposed`
- original: According to the American Thyroid Association, when this medication is started, you may lose up to 10% of your weight.
- pronoun resolved: According to the American Thyroid Association, when levothyroxine is started, you may lose up to 10% of your weight.
  - edits: “this medication” → “levothyroxine”
  - S1: According to the American Thyroid Association, when levothyroxine is started, you may lose up to 10% of your weight.

**L149.3** `Simple Sentence` (0.525) → `passthrough`
- original: This weight is mainly water weight, since being hypothyroid makes you retain water.

**L150.0** `Simple Sentence` (0.743) → `passthrough`
- original: Q: What can I eat for breakfast after taking levothyroxine?

**L150.1** `Complex Sentence` (0.501) → `decomposed`
- original: A: Most foods are considered fine to eat for breakfast as long as they are eaten 30 to 60 minutes after taking levothyroxine.
- pronoun resolved: A: Most foods are considered fine to eat for breakfast as long as foods are eaten 30 to 60 minutes after taking levothyroxine.
  - edits: “they” → “foods”
  - S1: Most foods are considered fine to eat for breakfast.
  - S2: This is true as long as foods are eaten 30 to 60 minutes after taking levothyroxine.

**L150.2** `Simple Sentence` (0.989) → `passthrough`
- original: Levothyroxine should be taken once a day on an empty stomach in the morning.

**L151.0** `Simple Sentence` (0.825) → `passthrough`
- original: Q: Can I take other medications with levothyroxine?

**L151.1** `Compound Sentence` (0.947) → `decomposed`
- original: A: Levothyroxine is known to interact with many other medications (called a drug-drug interaction), but there are different kinds of drug-drug interactions.
  - S1: Levothyroxine is known to interact with many other medications.
  - S2: These interactions are called drug-drug interactions.
  - S3: There are different kinds of drug-drug interactions.

**L151.2** `Compound Sentence` (0.757) → `decomposed`
- original: Some interactions require that drugs not be taken at the same time, while other interactions require more frequent laboratory testing or monitoring of your disease symptoms.
  - S1: Some interactions require that drugs not be taken at the same time.
  - S2: Other interactions require more frequent laboratory testing or monitoring of your disease symptoms.

**L152.0** `Simple Sentence` (0.798) → `passthrough`
- original: Q: How soon after taking levothyroxine can I take omeprazole?

**L152.1** `Compound Sentence` (0.702) → `decomposed`
- original: A: There is a known drug interaction between levothyroxine and omeprazole, but the timing of when you take the two medicines is not relevant.
  - S1: There is a known drug interaction between levothyroxine and omeprazole.
  - S2: The timing of when you take the two medicines is not relevant.

**L152.2** `Simple Sentence` (0.986) → `passthrough`
- original: Omeprazole decreases the absorption of your thyroid medication.

**L152.3** `Complex Sentence` (0.944) → `decomposed`
- original: If you need to be on a course of omeprazole while taking levothyroxine, your doctor may order more frequent laboratory testing to confirm you are absorbing enough levothyroxine.
  - S1: If you need to be on a course of omeprazole while taking levothyroxine.
  - S2: Your doctor may order more frequent laboratory testing.
  - S3: The testing is to confirm you are absorbing enough levothyroxine.

**L153.0** `Incomplete Sentence` (0.938) → `excluded_incomplete`
- original: Q: Does levothyroxine cause hair loss?

**L153.1** `Complex Sentence` (0.947) → `decomposed`
- original: A: Yes, levothyroxine, the main treatment for a sluggish thyroid gland, may cause hair loss in addition to other side effects.
  - S1: Levothyroxine may cause hair loss.
  - S2: Levothyroxine is the main treatment for a sluggish thyroid gland.
  - S3: Levothyroxine may cause other side effects in addition to hair loss.

**L153.2** `Compound Sentence` (0.688) → `decomposed`
- original: You may experience partial hair loss in the first few months of treatment, but this often resolves and goes back to normal in a short time.
- pronoun resolved: You may experience partial hair loss in the first few months of treatment, but partial hair loss often resolves and goes back to normal in a short time.
  - edits: “this” → “partial hair loss”
  - S1: You may experience partial hair loss in the first few months of treatment.
  - S2: Partial hair loss often resolves and goes back to normal in a short time.

**L154.0** `Simple Sentence` (0.634) → `passthrough`
- original: Q: How long after taking levothyroxine can you drink milk?

**L154.1** `Simple Sentence` (0.945) → `passthrough`
- original: A: You should avoid drinking milk until at least 4 hours after taking levothyroxine.

**L154.2** `Complex Sentence` (0.893) → `decomposed`
- original: Dairy products—including milk, cheese and yogurt—contain high calcium levels, which affect how levothyroxine is absorbed into your body.
  - S1: Dairy products contain high calcium levels.
  - S2: Dairy products include milk, cheese, and yogurt.
  - S3: High calcium levels affect how levothyroxine is absorbed into your body.

**L155.0** `Simple Sentence` (0.538) → `passthrough`
- original: Q: How long does levothyroxine stay in your system?

**L155.1** `Simple Sentence` (0.987) → `passthrough`
- original: A: Levothyroxine will stay in your system for around 4 to 6 weeks.

**L155.2** `Complex Sentence` (0.566) → `decomposed`
- original: It takes longer for people with hypothyroidism to eliminate levothyroxine (closer to 6 weeks) than those with normal thyroid function.
- pronoun resolved: Levothyroxine takes longer for people with hypothyroidism to eliminate levothyroxine (closer to 6 weeks) than those with normal thyroid function.
  - edits: “It” → “Levothyroxine”
  - S1: Levothyroxine takes longer for people with hypothyroidism to eliminate than for those with normal thyroid function.
  - S2: People with hypothyroidism take closer to 6 weeks to eliminate levothyroxine.
  - S3: People with normal thyroid function eliminate levothyroxine faster.

**L156.0** `Simple Sentence` (0.529) → `passthrough`
- original: Q: What is the difference between Levoxyl and Synthroid?

**L156.1** `Simple Sentence` (0.964) → `passthrough`
- original: A: Levoxyl and Synthroid are brand names for the drug levothyroxine.

**L156.2** `Compound Sentence` (0.961) → `decomposed`
- original: Both medications contain the same active ingredient, levothyroxine, but they contain different inactive ingredients.
- pronoun resolved: Both medications contain the same active ingredient, levothyroxine, but Levoxyl and Synthroid contain different inactive ingredients.
  - edits: “they” → “Levoxyl and Synthroid”
  - S1: Both medications contain the same active ingredient, levothyroxine.
  - S2: Levoxyl and Synthroid contain different inactive ingredients.

**L157.0** `Simple Sentence` (0.846) → `passthrough`
- original: Q: Can you take thyroid supplements with levothyroxine?

**L157.1** `Simple Sentence` (0.548) → `passthrough`
- original: A: Taking any other medication or supplement with levothyroxine may cause you to need a higher or lower dose of levothyroxine.

**L157.2** `Simple Sentence` (0.986) → `passthrough`
- original: Even supplements like calcium or iron can affect absorption of levothyroxine.
