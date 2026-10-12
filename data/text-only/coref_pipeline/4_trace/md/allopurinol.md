# Allopurinol — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/allopurinol.txt` · 117 sentences · 11 changed by pronoun resolution · 142 sentences sent to EDC

## What is allopurinol?

**L5.0** `Simple Sentence` (0.99) → `passthrough`
- original: Allopurinol belongs to a class of medications called xanthine oxidase inhibitors.

**L5.1** `Simple Sentence` (0.984) → `passthrough`
- original: It works by reducing the production of uric acid in the body.
- pronoun resolved: Allopurinol works by reducing the production of uric acid in the body.
  - edits: “It” → “Allopurinol”

**L5.2** `Simple Sentence` (0.988) → `passthrough`
- original: High levels of uric acid may cause gout attacks or kidney stones.

**L6.0** `Complex Sentence` (0.727) → `decomposed`
- original: Allopurinol is used to treat gout (a type of arthritis in which uric acid, a naturally occurring substance in the body, builds up in the joints and causes sudden attacks of redness, swelling, pain, and heat in one or more joints).
  - S1: Allopurinol is used to treat gout.
  - S2: Gout is a type of arthritis.
  - S3: In gout, uric acid builds up in the joints.
  - S4: Uric acid is a naturally occurring substance in the body.
  - S5: The buildup of uric acid causes sudden attacks of redness, swelling, pain, and heat.
  - S6: These attacks occur in one or more joints.

**L6.1** `Compound Sentence` (0.67) → `decomposed`
- original: Allopurinol is used to prevent gout attacks, not to treat them once they occur.
- pronoun resolved: Allopurinol is used to prevent gout attacks, not to treat gout attacks once gout attacks occur.
  - edits: “them” → “gout attacks”; “they” → “gout attacks”
  - S1: Allopurinol is used to prevent gout attacks.
  - S2: It is not used to treat gout attacks once they occur.

**L6.2** `Simple Sentence` (0.985) → `passthrough`
- original: Allopurinol does not need to be stopped during an acute flare.

**L7.0** `Complex Sentence` (0.924) → `decomposed`
- original: Allopurinol is also used to treat high levels of uric acid that builds up in the blood as tumors break down in people with certain types of cancer who are being treated with chemotherapy medications.
  - S1: Allopurinol is also used to treat high levels of uric acid.
  - S2: The high levels of uric acid build up in the blood.
  - S3: This buildup occurs as tumors break down.
  - S4: This happens in people with certain types of cancer.
  - S5: These people are being treated with chemotherapy medications.

**L7.1** `Complex Sentence` (0.35) → `decomposed`
- original: It is also used to treat kidney stones that have come back in people who have high levels of uric acid in their urine.
- pronoun resolved: Allopurinol is also used to treat kidney stones that have come back in people who have high levels of uric acid in their urine.
  - edits: “It” → “Allopurinol”
  - S1: Allopurinol is used to treat kidney stones.
  - S2: The kidney stones have come back.
  - S3: This treatment is for people with high levels of uric acid in their urine.

## Warnings

**L10.0** `Simple Sentence` (0.979) → `passthrough`
- original: You should not use this medicine if you have ever had an allergic reaction to allopurinol.
- pronoun resolved: You should not use Allopurinol if you have ever had an allergic reaction to allopurinol.
  - edits: “this medicine” → “Allopurinol”

**L11.0** `Simple Sentence` (0.989) → `passthrough`
- original: Allopurinol can lower blood cells that help your body fight infections.

**L11.1** `Simple Sentence` (0.936) → `passthrough`
- original: This can make it easier for you to bleed from an injury or get sick from being around others who are ill.

**L11.2** `Simple Sentence` (0.964) → `passthrough`
- original: Your blood may need to be tested often.

**L11.3** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Visit your doctor regularly.

**L12.0** `Simple Sentence` (0.98) → `passthrough`
- original: In rare cases, allopurinol may cause a severe allergic reaction.

**L12.1** `Compound Sentence` (0.467) → `decomposed`
- original: Stop taking this medicine and call your doctor right away if you have painful urination, blood in your urine, burning in your eyes, swelling in your face or throat, skin redness or a rash that spreads and causes blistering and peeling.
- pronoun resolved: Stop taking Allopurinol and call your doctor right away if you have painful urination, blood in your urine, burning in your eyes, swelling in your face or throat, skin redness or a rash that spreads and causes blistering and peeling.
  - edits: “this medicine” → “Allopurinol”
  - S1: Stop taking Allopurinol and call your doctor right away if you have painful urination.
  - S2: Stop taking Allopurinol and call your doctor right away if you have blood in your urine.
  - S3: Stop taking Allopurinol and call your doctor right away if you have burning in your eyes.
  - S4: Stop taking Allopurinol and call your doctor right away if you have swelling in your face or throat.
  - S5: Stop taking Allopurinol and call your doctor right away if you have skin redness.
  - S6: Stop taking Allopurinol and call your doctor right away if you have a rash that spreads and causes blistering and peeling.

**L13.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Avoid drinking alcohol.

**L13.1** `Simple Sentence` (0.99) → `passthrough`
- original: It can make your condition worse.
- pronoun resolved: Allopurinol can make your condition worse.
  - edits: “It” → “Allopurinol”

**L13.2** `Simple Sentence` (0.99) → `passthrough`
- original: Allopurinol may impair your thinking or reactions.

**L13.3** `Incomplete Sentence` (0.688) → `excluded_incomplete`
- original: Be careful if you drive or do anything that requires you to be alert.

## Before taking this medicine

**L16.0** `Simple Sentence` (0.988) → `passthrough`
- original: You should not use allopurinol if you are allergic to it.
- pronoun resolved: You should not use allopurinol if you are allergic to allopurinol.
  - edits: “it.” → “allopurinol.”

**L17.0** `Simple Sentence` (0.59) → `passthrough`
- original: To make sure this medicine is safe for you, tell your doctor if you have ever had:

**L18.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: diabetes;

**L19.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: congestive heart failure;

**L20.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: high blood pressure;

**L21.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: if you are receiving chemotherapy;

**L22.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: if you have a gene variation called HLA-B*58:01 allele (your doctor can test you for this);

**L23.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: liver disease; or

**L24.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: kidney disease.

**L25.0** `Simple Sentence` (0.992) → `passthrough`
- original: Allopurinol may harm an unborn baby.

**L25.1** `Incomplete Sentence` (0.915) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or plan to become pregnant.

**L26.0** `Incomplete Sentence` (0.609) → `excluded_incomplete`
- original: Do not breastfeed while using this medicine, and for at least 1 week after your last dose.

## How should I use allopurinol?

**L29.0** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Take allopurinol exactly as prescribed by your doctor.

**L29.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L29.2** `Simple Sentence` (0.984) → `passthrough`
- original: Your doctor may occasionally change your dose.

**L30.0** `Incomplete Sentence` (0.979) → `excluded_incomplete`
- original: Take the tablets with a full glass of water.

**L30.1** `Complex Sentence` (0.584) → `decomposed`
- original: To reduce your risk of kidney stones, drink 8 to 10 full glasses of fluid every day, unless your doctor tells you otherwise.
  - S1: To reduce your risk of kidney stones, drink 8 to 10 full glasses of fluid every day.
  - S2: Do this unless your doctor tells you otherwise.

**L31.0** `Incomplete Sentence` (0.904) → `excluded_incomplete`
- original: Take allopurinol tablets after meals to help prevent stomach upset.

**L32.0** `Simple Sentence` (0.966) → `passthrough`
- original: Allopurinol injection is injected into a vein by a healthcare provider.

**L32.1** `Simple Sentence` (0.98) → `passthrough`
- original: The injection is usually only used if you are unable to take medicine by mouth.

**L33.0** `Compound Sentence` (0.622) → `decomposed`
- original: You may need frequent medical tests while using this medicine, even if you have no symptoms.
- pronoun resolved: You may need frequent medical tests while using Allopurinol, even if you have no symptoms.
  - edits: “this medicine,” → “Allopurinol,”
  - S1: You may need frequent medical tests while using Allopurinol.
  - S2: You may need these tests even if you have no symptoms.

**L34.0** `Simple Sentence` (0.963) → `passthrough`
- original: Your kidney and liver function may also need to be tested.

**L34.1** `Simple Sentence` (0.985) → `passthrough`
- original: Your doctor may change your dose if your kidney function changes.

**L35.0** `Simple Sentence` (0.989) → `passthrough`
- original: You may have gout attacks when you first start taking allopurinol tablets.

**L35.1** `Simple Sentence` (0.98) → `passthrough`
- original: Your doctor may recommend another gout medication to take with allopurinol.

**L35.2** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Keep taking the medicine as directed.
- pronoun resolved: Keep taking Allopurinol as directed.
  - edits: “the medicine” → “Allopurinol”

**L36.0** `Simple Sentence` (0.984) → `passthrough`
- original: Your symptoms may not improve for up to 2 to 6 weeks.

**L36.1** `Incomplete Sentence` (0.824) → `excluded_incomplete`
- original: Call your doctor if your symptoms do not improve after 6 weeks.

**L37.0** `Simple Sentence` (0.96) → `passthrough`
- original: You may need to follow a special diet to help prevent kidney stones.

**L37.1** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Follow all instructions of your doctor or dietitian.

**L37.2** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Learn about the foods you should eat or avoid.

**L38.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Store at room temperature away from moisture and heat.

## What happens if I miss a dose?

**L41.0** `Compound Sentence` (0.564) → `decomposed`
- original: Take allopurinol as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - S1: Take allopurinol as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L41.1** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

**L42.0** `Incomplete Sentence` (0.915) → `excluded_incomplete`
- original: Call your doctor for instructions if you miss an appointment for your allopurinol injection.

## What happens if I overdose?

**L45.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

## What should I avoid while using allopurinol?

**L48.0** `Incomplete Sentence` (0.974) → `excluded_incomplete`
- original: Avoid driving or hazardous activity until you know how allopurinol will affect you.

**L48.1** `Simple Sentence` (0.878) → `passthrough`
- original: Your reactions could be impaired.

**L49.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Avoid drinking alcohol.

## Allopurinol side effects

**L52.0** `Compound Sentence` (0.384) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to allopurinol (hives, difficult breathing, swelling in your face or throat) or a severe skin reaction (fever, sore throat, burning eyes, skin pain, red or purple skin rash with blistering and peeling).
  - S1: Get emergency medical help if you have signs of an allergic reaction to allopurinol.
  - S2: Signs of an allergic reaction to allopurinol include hives, difficult breathing, and swelling in your face or throat.
  - S3: Get emergency medical help if you have a severe skin reaction.
  - S4: Signs of a severe skin reaction include fever, sore throat, burning eyes, skin pain, and a red or purple skin rash with blistering and peeling.

**L53.0** `Incomplete Sentence` (0.953) → `excluded_incomplete`
- original: Seek medical treatment if you have a serious drug reaction that can affect many parts of your body.

**L53.1** `Simple Sentence` (0.476) → `passthrough`
- original: Symptoms may include skin rash, fever, swollen glands, muscle aches, severe weakness, unusual bruising, or yellowing of your skin or eyes.

**L54.0** `Simple Sentence` (0.99) → `passthrough`
- original: Allopurinol may cause serious side effects.

**L54.1** `Incomplete Sentence` (0.959) → `excluded_incomplete`
- original: Stop using this medicine and call your doctor at once if you have:
- pronoun resolved: Stop using Allopurinol and call your doctor at once if you have:
  - edits: “this medicine” → “Allopurinol”

**L55.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: any skin rash, no matter how mild;

**L56.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: painful urination, blood in the urine;

**L57.0** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: inflammation of your blood vessels - numbness or tingling, skin rash, fever, headache, body aches, night sweats, weight loss, feeling or weak or tired;

**L58.0** `Incomplete Sentence` (0.973) → `excluded_incomplete`
- original: signs of infection - fever, chills, sore throat, body aches, unusual tiredness, loss of appetite, bruising or bleeding; or

**L59.0** `Simple Sentence` (0.53) → `passthrough`
- original: liver problems - loss of appetite, weight loss, stomach pain (upper right side), itching, dark urine, clay-colored stools, jaundice (yellowing of the skin or eyes).

**L60.0** `Simple Sentence` (0.967) → `passthrough`
- original: Common allopurinol side effects may include:

**L61.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: an increase in gout attacks when you first start taking this medicine;
- pronoun resolved: an increase in gout attacks when you first start taking Allopurinol;
  - edits: “this medicine;” → “Allopurinol;”

**L62.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: rash;

**L63.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: drowsiness;

**L64.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: abnormal liver function tests;

**L65.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: nausea, vomiting, diarrhea; or

**L66.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: kidney problems - swelling, urinating less, feeling tired or short of breath.

**L67.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L67.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L67.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## What other drugs will affect allopurinol?

**L70.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Tell your doctor about all your other medicines, especially:

**L71.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: azathioprine or mercaptopurine;

**L72.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: chlorpropamide;

**L73.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: cyclosporine;

**L74.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: cancer medicine;

**L75.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: other gout medications;

**L76.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: an antibiotic such as ampicillin or amoxicillin;

**L77.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: a blood thinner such as warfarin, Coumadin, Jantoven; or

**L78.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a diuretic or "water pill".

**L79.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L79.1** `Complex Sentence` (0.558) → `decomposed`
- original: Other drugs may interact with allopurinol, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may interact with allopurinol.
  - S2: These include prescription and over-the-counter medicines.
  - S3: These also include vitamins and herbal products.

**L79.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.

**L80.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Check interactions

**L81.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Compare alternatives

**L82.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Pricing & coupons

**L83.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Reviews (92)

**L84.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Drug images

**L85.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Side effects

**L86.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Dosage information

**L87.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Patient tips

**L88.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: During pregnancy

**L89.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Support group

**L90.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Drug class: antigout agents

**L91.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Breastfeeding

**L92.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: En español

**L93.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Patient resources:

**L94.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Other brands:

**L95.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Zyloprim, Aloprim

**L96.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Professional resources:

**L97.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Allopurinol monograph

**L98.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Allopurinol (FDA)

**L99.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Allopurinol Injection (FDA)

**L100.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Other brands:

**L101.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Zyloprim, Aloprim

**L102.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Related treatment guides:

**L103.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Gout

**L104.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Calcium Oxalate Calculi with Hyperuricosuria

**L105.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Cardiothoracic Surgery

**L106.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: High Risk Percutaneous Transluminal Angioplasty
