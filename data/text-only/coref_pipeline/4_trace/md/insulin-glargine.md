# Insulin glargine — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/insulin-glargine.txt` · 175 sentences · 10 changed by pronoun resolution · 230 sentences sent to EDC

## What is insulin glargine?

**L5.0** `Complex Sentence` (0.883) → `decomposed`
- original: Insulin glargine is a long-acting insulin used to treat type 1 and type 2 diabetes in certain patients to improve and maintain blood glucose levels.
  - S1: Insulin glargine is a long-acting insulin.
  - S2: It is used to treat type 1 and type 2 diabetes in certain patients.
  - S3: The treatment aims to improve and maintain blood glucose levels.

**L5.1** `Complex Sentence` (0.858) → `decomposed`
- original: Insulin glargine is a man-made form of human insulin that is used once daily to provide a base level of insulin that keeps working for 24 hours or longer.
  - S1: Insulin glargine is a man-made form of human insulin.
  - S2: It is used once daily.
  - S3: It provides a base level of insulin.
  - S4: This insulin keeps working for 24 hours or longer.

**L6.0** `Simple Sentence` (0.905) → `passthrough`
- original: Insulin glargine is available under the brand names Lantus, Basaglar, Toujeo, Semglee, and Rezvoglar.

**L6.1** `Simple Sentence` (0.817) → `passthrough`
- original: Langlara is an interchangeable biosimilar to Lantus that was FDA-approved on May 4, 2026.

**L7.0** `Complex Sentence` (0.57) → `decomposed`
- original: Rezvoglar, Lantus, Langlara, Semglee, and Toujeo are FDA-approved to be used for use in adult and pediatric patients with type 1 and type 2 diabetes.
  - S1: Rezvoglar, Lantus, Langlara, Semglee, and Toujeo are FDA-approved.
  - S2: They are approved for use in adult and pediatric patients.
  - S3: These patients have type 1 and type 2 diabetes.

**L7.1** `Compound Sentence` (0.557) → `decomposed`
- original: Basasglar is FDA-approved to be used by adults for type 2 diabetes and also for adults and pediatric patients with type 1 diabetes.
  - S1: Basasglar is FDA-approved to be used by adults for type 2 diabetes.
  - S2: It is also approved for adults and pediatric patients with type 1 diabetes.

**L7.2** `Simple Sentence` (0.953) → `passthrough`
- original: In patients with type 1 diabetes, insulin glargine must be used together with a short-acting insulin.

## Insulin glargine side effects

**L10.0** `Complex Sentence` (0.895) → `decomposed`
- original: Common insulin glargine side effects may include low blood sugar, swelling, weight gain, allergic reaction, itching, rash, or thickening or hollowing of the skin where you injected the medicine (lipodystrophy).
- pronoun resolved: Common insulin glargine side effects may include low blood sugar, swelling, weight gain, allergic reaction, itching, rash, or thickening or hollowing of the skin where you injected Insulin glargine (lipodystrophy).
  - edits: “the medicine” → “Insulin glargine”
  - S1: Common insulin glargine side effects may include low blood sugar.
  - S2: Common insulin glargine side effects may include swelling.
  - S3: Common insulin glargine side effects may include weight gain.
  - S4: Common insulin glargine side effects may include allergic reaction.
  - S5: Common insulin glargine side effects may include itching.
  - S6: Common insulin glargine side effects may include rash.
  - S7: Common insulin glargine side effects may include thickening or hollowing of the skin where you injected Insulin glargine (lipodystrophy).

**L11.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious insulin glargine side effects

**L12.0** `Compound Sentence` (0.552) → `decomposed`
- original: Get emergency medical help if you have signs of insulin allergy: redness or swelling where an injection was given, itchy skin rash over the entire body, trouble breathing, fast heartbeats, feeling like you might pass out, or swelling in your tongue or throat.
  - S1: Get emergency medical help if you have signs of insulin allergy.
  - S2: Signs of insulin allergy include redness or swelling where an injection was given.
  - S3: Signs of insulin allergy include an itchy skin rash over the entire body.
  - S4: Signs of insulin allergy include trouble breathing.
  - S5: Signs of insulin allergy include fast heartbeats.
  - S6: Signs of insulin allergy include feeling like you might pass out.
  - S7: Signs of insulin allergy include swelling in your tongue or throat.

**L13.0** `Simple Sentence` (0.99) → `passthrough`
- original: Insulin glargine may cause other serious side effects.

**L13.1** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L14.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: rapid weight gain, swelling in your feet or ankles;

**L15.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: shortness of breath; or

**L16.0** `Incomplete Sentence` (0.618) → `excluded_incomplete`
- original: low blood potassium--leg cramps, constipation, irregular heartbeats, fluttering in your chest, increased thirst or urination, numbness or tingling, muscle weakness or limp feeling.

**L17.0** `Compound Sentence` (0.545) → `decomposed`
- original: This is not a complete list of side effects, and others may occur.
  - S1: This is not a complete list of side effects.
  - S2: Others may occur.

**L17.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L17.2** `Simple Sentence` (0.97) → `passthrough`
- original: You may report side effects to the FDA at 1-800-FDA-1088.

## Warnings

**L20.0** `Incomplete Sentence` (0.964) → `excluded_incomplete`
- original: Never share an injection pen, even if you changed the needle.

## Before taking this medicine

**L23.0** `Complex Sentence` (0.446) → `decomposed`
- original: You should not use insulin glargine if you are allergic to insulin, or if you are having an episode of hypoglycemia (low blood sugar) or diabetic ketoacidosis (call your doctor for treatment).
  - S1: You should not use insulin glargine if you are allergic to insulin.
  - S2: You should not use insulin glargine if you are having an episode of hypoglycemia.
  - S3: You should not use insulin glargine if you are having an episode of diabetic ketoacidosis.
  - S4: Call your doctor for treatment.

**L24.0** `Simple Sentence` (0.981) → `passthrough`
- original: Different brands of insulin glargine are specifically approved for different age groups and different diabetes types.

**L24.1** `Compound Sentence` (0.437) → `decomposed`
- original: The safety and effectiveness of insulin glargine in pediatric patients younger than 6 years of age with type 1 diabetes and pediatric patients with type 2 diabetes has not been established.
  - S1: The safety and effectiveness of insulin glargine in pediatric patients younger than 6 years of age with type 1 diabetes has not been established.
  - S2: The safety and effectiveness of insulin glargine in pediatric patients with type 2 diabetes has not been established.

**L25.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Tell your doctor if you have ever had:

**L26.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: liver or kidney disease; or

**L27.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: heart failure or other heart problems.

**L28.0** `Incomplete Sentence` (0.46) → `excluded_incomplete`
- original: Tell your doctor if you also take pioglitazone or rosiglitazone (sometimes contained in combinations with glimepiride or metformin).

**L28.1** `Simple Sentence` (0.979) → `passthrough`
- original: Taking certain oral diabetes medicines while you are using insulin may increase your risk of serious heart problems.

**L29.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Pregnancy:

**L30.0** `Incomplete Sentence` (0.328) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or plan to become pregnant, as it is not known if insulin glargine will harm your unborn baby.

**L30.1** `Incomplete Sentence` (0.922) → `excluded_incomplete`
- original: Follow your doctor's instructions about using this medicine if you are pregnant or you become pregnant.
- pronoun resolved: Follow your doctor's instructions about using Insulin glargine if you are pregnant or you become pregnant.
  - edits: “this medicine” → “Insulin glargine”

**L30.2** `Simple Sentence` (0.992) → `passthrough`
- original: Controlling diabetes is very important during pregnancy.

**L31.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Breastfeeding:

**L32.0** `Compound Sentence` (0.336) → `decomposed`
- original: Tell your healthcare provider if you are breastfeeding or are planning to breastfeed, as it is not known if insulin glargine may harm your breastfeeding baby.
  - S1: Tell your healthcare provider if you are breastfeeding or are planning to breastfeed.
  - S2: It is not known if insulin glargine may harm your breastfeeding baby.

## How should I use insulin glargine?

**L35.0** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L35.1** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Use the medicine exactly as directed.

**L35.2** `Incomplete Sentence` (0.854) → `excluded_incomplete`
- original: Ask your doctor or pharmacist if you don't understand how to use an injection.

**L36.0** `Incomplete Sentence` (0.956) → `excluded_incomplete`
- original: Prepare an injection only when you are ready to give it.

**L36.1** `Simple Sentence` (0.456) → `passthrough`
- original: Do not use it if the medicine looks cloudy, has changed colors, or has particles in it.

**L37.0** `Simple Sentence` (0.946) → `passthrough`
- original: Insulin glargine is injected under the skin, using a syringe or insulin pen, once per day at the same time of day.

**L38.0** `Simple Sentence` (0.976) → `passthrough`
- original: Insulin can be injected into your upper legs (thighs), upper arms, or stomach area (abdomen).

**L38.1** `Incomplete Sentence` (0.967) → `excluded_incomplete`
- original: Do not inject into the same place two times in a row.

**L38.2** `Incomplete Sentence` (0.748) → `excluded_incomplete`
- original: Avoid injecting into skin that is damaged, tender, bruised, pitted, thickened, scaly, or has a scar or hard lump.

**L39.0** `Simple Sentence` (0.92) → `passthrough`
- original: When treating type 1 diabetes, use your short-acting insulin before meals as directed by your doctor.

**L40.0** `Simple Sentence` (0.972) → `passthrough`
- original: Insulin glargine must not be given with an insulin pump or mixed with other insulins.

**L40.1** `Simple Sentence` (0.663) → `passthrough`
- original: Do not inject insulin glargine into a vein or a muscle.

**L41.0** `Simple Sentence` (0.746) → `passthrough`
- original: Your dose needs may change if you switch to a different brand, strength, or form of this medicine.

**L41.1** `Incomplete Sentence` (0.936) → `excluded_incomplete`
- original: Avoid medication errors by using only the medicine your doctor prescribes.

**L42.0** `Simple Sentence` (0.761) → `passthrough`
- original: If you use an injection pen, use only the injection pen that comes with insulin glargine.

**L42.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Attach a new needle before each use.

**L42.2** `Incomplete Sentence` (0.785) → `excluded_incomplete`
- original: Do not transfer the insulin from the pen into a syringe.

**L43.0** `Incomplete Sentence` (0.964) → `excluded_incomplete`
- original: Never share an injection pen, even if you changed the needle.

**L43.1** `Simple Sentence` (0.99) → `passthrough`
- original: Sharing these devices can pass infections from person to person.

**L44.0** `Simple Sentence` (0.866) → `passthrough`
- original: Blood sugar can be affected by stress, illness, surgery, exercise, alcohol use, or skipping meals.

**L45.0** `Simple Sentence` (0.874) → `passthrough`
- original: Low blood sugar (hypoglycemia) can make you feel very hungry, dizzy, irritable, or shaky.

**L45.1** `Simple Sentence` (0.942) → `passthrough`
- original: To quickly treat hypoglycemia, eat or drink hard candy, crackers, raisins, fruit juice, or non-diet soda.

**L45.2** `Simple Sentence` (0.98) → `passthrough`
- original: Your doctor may prescribe glucagon injections in case of severe hypoglycemia.

**L46.0** `Incomplete Sentence` (0.597) → `excluded_incomplete`
- original: Tell your doctor if you have frequent symptoms of high blood sugar (hyperglycemia), such as increased thirst or urination.

**L46.1** `Incomplete Sentence` (0.69) → `excluded_incomplete`
- original: Ask your doctor before changing your medication dosage.

**L47.0** `Incomplete Sentence` (0.955) → `excluded_incomplete`
- original: Wear a medical alert tag or carry an ID card to let others know you have diabetes.

**L48.0** `Simple Sentence` (0.798) → `passthrough`
- original: Insulin glargine is available as:

**L49.0** `Simple Sentence` (0.902) → `passthrough`
- original: Basaglar 100 units/mL is available as Basaglar KwikPen 3 mL, BasaglarTempo Pen

**L50.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: 3 mL

**L51.0** `Simple Sentence` (0.564) → `passthrough`
- original: Lantus 100 units/mL is available as a Lantus multiple-dose vial 10 mL, Lantus SoloStar prefilled pen 3 mL

**L52.0** `Simple Sentence` (0.986) → `passthrough`
- original: Langlara 100 units/mL is available as a single-patient-use prefilled pen 3 mL

**L53.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Rezvoglar 100 units/mL available as Rezvoglar KwikPen prefilled pen 3 mL

**L54.0** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: Semglee 100 units/mL available as Semglee multiple-dose vial 10 mL, Semglee prefilled pen 3 mL

**L55.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: Toujeo 300 units/mL available as Toujeo SoloStar prefilled pen 1.5 ml, Toujeo Max SoloStar 3 mL prefilled pen

## What happens if I miss a dose?

**L58.0** `Incomplete Sentence` (0.893) → `excluded_incomplete`
- original: Call your doctor for instructions if you miss a dose.

**L58.1** `Incomplete Sentence` (0.76) → `excluded_incomplete`
- original: Do not use more than one dose in a 24-hour period unless your doctor tells you to.

**L59.0** `Incomplete Sentence` (0.913) → `excluded_incomplete`
- original: Get your prescription refilled before you run out of medicine completely.

## What happens if I overdose?

**L62.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L62.1** `Simple Sentence` (0.991) → `passthrough`
- original: Insulin overdose can cause severe hypoglycemia.

**L62.2** `Simple Sentence` (0.596) → `passthrough`
- original: Symptoms include drowsiness, confusion, blurred vision, numbness or tingling in your mouth, trouble speaking, muscle weakness, clumsy or jerky movements, seizure (convulsions), or loss of consciousness.

## What should I avoid while using insulin glargine?

**L65.0** `Incomplete Sentence` (0.966) → `excluded_incomplete`
- original: Avoid driving or hazardous activity until you know how insulin glargine will affect you.

**L65.1** `Simple Sentence` (0.878) → `passthrough`
- original: Your reactions could be impaired.

**L66.0** `Incomplete Sentence` (0.93) → `excluded_incomplete`
- original: Avoid medication errors by always checking the medicine label before injecting your insulin.

**L67.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Avoid drinking alcohol or using medicines that contain alcohol.

**L67.1** `Simple Sentence` (0.981) → `passthrough`
- original: It may interfere with your diabetes treatment.

## What other drugs will affect insulin glargine?

**L70.0** `Compound Sentence` (0.709) → `decomposed`
- original: Many drugs can affect your blood sugar and may also affect insulin glargine.
  - S1: Many drugs can affect your blood sugar.
  - S2: Many drugs may also affect insulin glargine.

**L70.1** `Simple Sentence` (0.849) → `passthrough`
- original: This includes prescription and over-the-counter medicines, vitamins, and herbal products.

**L70.2** `Incomplete Sentence` (0.967) → `excluded_incomplete`
- original: Tell your doctor about all other medicines you use.

**L70.3** `Simple Sentence` (0.949) → `passthrough`
- original: Not all possible interactions are listed here.

**L71.0** `Incomplete Sentence` (0.46) → `excluded_incomplete`
- original: Tell your doctor if you also take pioglitazone or rosiglitazone (sometimes contained in combinations with glimepiride or metformin).

**L71.1** `Simple Sentence` (0.979) → `passthrough`
- original: Taking certain oral diabetes medicines while you are using insulin may increase your risk of serious heart problems.

## Storage

**L74.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Storing unopened (not in use) insulin glargine:

**L75.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Refrigerate at 36°F–46°F (2°C–8°C)

**L76.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Do NOT use after the expiration date.

**L77.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Storing opened (in use) insulin glargine:

**L78.0** `Simple Sentence` (0.988) → `passthrough`
- original: Storage once in use varies for different brands of insulin glargine.

**L78.1** `Complex Sentence` (0.454) → `decomposed`
- original: For storage information for the different brands of insulin glargine while in use, check the prescribing information.
  - S1: Check the prescribing information.
  - S2: The prescribing information contains storage information for the different brands of insulin glargine while in use.

**L79.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: General storage information

**L80.0** `Incomplete Sentence` (0.961) → `excluded_incomplete`
- original: Keep this medicine in its original container protected from heat and light.

**L81.0** `Incomplete Sentence` (0.891) → `excluded_incomplete`
- original: Do not store an injection pen with the needle attached.

**L81.1** `Incomplete Sentence` (0.89) → `excluded_incomplete`
- original: Do not reuse a needle or syringe.

**L81.2** `Incomplete Sentence` (0.822) → `excluded_incomplete`
- original: Place them in a puncture-proof "sharps" container and dispose of it following state or local laws.
- pronoun resolved: Place them in a puncture-proof "sharps" container and dispose of needle following state or local laws.
  - edits: “it” → “needle”

**L81.3** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Keep out of the reach of children and pets.

## Company

**L84.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Basaglar manufactured by: Eli Lilly and Company, Indianapolis, IN 46285 USA.

**L85.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Lantus manufactured by: sanofi-aventis U.S. LLC, Bridgewater, NJ 08807, A SANOFI COMPANY.

**L86.0** `Incomplete Sentence` (0.831) → `excluded_incomplete`
- original: Langlara manufactured by: Sunshine Lake Pharma, China; its U.S. distributor is Lanexa Biologics/Lannett.
- pronoun resolved: Langlara manufactured by: Sunshine Lake Pharma, China; sanofi-aventis U.S. LLC's U.S. distributor is Lanexa Biologics/Lannett.
  - edits: “its” → “sanofi-aventis U.S. LLC's”

**L87.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Rezvoglar manufactured by: Eli Lilly and Company, Indianapolis, IN 46285, USA.

**L88.0** `Simple Sentence` (0.551) → `passthrough`
- original: Semglee manufactured by: Biocon Biologics Inc. 245 Main St, 2nd Floor, Cambridge, MA 02142 USA.

**L89.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Toujeo manufactured by: sanofi-aventis U.S. LLC, Bridgewater, NJ 08807, A SANOFI COMPANY.

## Insulin glargine Biosimilars

**L92.0** `Simple Sentence` (0.75) → `passthrough`
- original: Biosimilar and interchangeable products are biological products that are highly similar to and have no clinically meaningful differences from the reference product.

**L93.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Reference products:

**L94.0** `Simple Sentence` (0.829) → `passthrough`
- original: These are biological products that have already been approved by the FDA, against which biosimilar products are compared.

**L94.1** `Simple Sentence` (0.987) → `passthrough`
- original: There are 4 for insulin glargine.

**L95.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Basaglar (insulin glargine) - Eli Lilly and Company:

**L96.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Formulation type | Strength

**L97.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Autoinjector | 300 units/3 mL (100 units/mL)

**L98.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: View Basaglar information in detail.

**L99.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Lantus (insulin glargine) - Sanofi-Aventis U.S. LLC:

**L100.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Formulation type | Strength

**L101.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Autoinjector | 300 units/3 mL (100 units/mL)

**L102.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Multi-Dose Cartridge | 300 units/3 mL (100 units/mL) Discontinued

**L103.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Multi-Dose Vial | 1,000 units/10 mL (100 units/mL)

**L104.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Multi-Dose Vial | 500 units/5 mL (100 units/mL) Discontinued

**L105.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: View Lantus information in detail.

**L106.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Semglee (insulin glargine) - Mylan Pharmaceuticals Inc.:

**L107.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Formulation type | Strength

**L108.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Autoinjector | 300 units/3 mL (100 units/mL) Discontinued, Voluntarily Revoked

**L109.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Multi-Dose Vial | 1,000 units/10 mL (100 units/mL) Discontinued, Voluntarily Revoked

**L110.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: View Semglee information in detail.

**L111.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Toujeo (insulin glargine) - Sanofi-Aventis U.S. LLC:

**L112.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Formulation type | Strength

**L113.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Autoinjector | 450 units/1.5 mL (300 units/mL)

**L114.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Autoinjector | 900 units/3 mL (300 units/mL)

**L115.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: View Toujeo information in detail.

**L116.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Lantus interchangeable products:

**L117.0** `Simple Sentence` (0.759) → `passthrough`
- original: Interchangeable biosimilar products can be dispensed by a pharmacist without the intervention of the prescriber of the reference product.

**L118.0** `Simple Sentence` (0.982) → `passthrough`
- original: Pharmacy laws for biosimilar prescribing may vary by state.

**L119.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Langlara (insulin glargine-aldy) - Sunshine Lake Pharma Co., Ltd.:

**L120.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Formulation type | Strength

**L121.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Autoinjector | 300 units/3 mL (100 units/mL)

**L122.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: View Langlara information in detail.

**L123.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: Rezvoglar (insulin glargine-aglr) - Eli Lilly and Company:

**L124.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Formulation type | Strength

**L125.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Autoinjector | 300 units/3 mL (100 units/mL)

**L126.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: View Rezvoglar information in detail.

**L127.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Semglee (insulin glargine-yfgn) - Biocon Biologics Inc.:

**L128.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Formulation type | Strength

**L129.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Autoinjector | 300 units/3 mL (100 units/mL)

**L130.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Multi-Dose Vial | 1,000 units/10 mL (100 units/mL)

**L131.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: View Semglee information in detail.

## Popular FAQ

**L134.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Q: How and where should I inject insulin?

**L134.1** `Compound Sentence` (0.93) → `decomposed`
- original: A: Injecting insulin is not difficult, but it does take a bit of practice.
- pronoun resolved: A: Injecting insulin is not difficult, but Injecting insulin does take a bit of practice.
  - edits: “it” → “Injecting insulin”
  - S1: Injecting insulin is not difficult.
  - S2: Injecting insulin does take a bit of practice.

**L134.2** `Compound-Complex Sentence` (0.874) → `decomposed`
- original: There are three main sites where insulin can be injected: the stomach area except for a 2-inch circle around your navel, and the soft part of your waist, but not anywhere near your spine; the top and outer part of your thighs, but not your inner thighs or anywhere close to your knee; the outer back of your upper arm where there is a pocket of fatty tissue.
  - S1: There are three main sites where insulin can be injected.
  - S2: One site is the stomach area.
  - S3: The stomach area excludes a 2-inch circle around your navel.
  - S4: Another site is the soft part of your waist.
  - S5: The waist site excludes areas near your spine.
  - S6: A third site is the top and outer part of your thighs.
  - S7: The thigh site excludes your inner thighs.
  - S8: The thigh site also excludes areas close to your knee.
  - S9: The final site is the outer back of your upper arm.
  - S10: This arm site must have a pocket of fatty tissue.

**L135.0** `Incomplete Sentence` (0.938) → `excluded_incomplete`
- original: Q: When is the best time to take Toujeo?

**L135.1** `Compound Sentence` (0.854) → `decomposed`
- original: A: Toujeo may be given at any time of the day; however, once you have chosen a time, it is best to inject Toujeo within three hours of that time every day.
  - S1: Toujeo may be given at any time of the day.
  - S2: Once you have chosen a time, it is best to inject Toujeo within three hours of that time every day.

**L135.2** `Compound Sentence` (0.521) → `decomposed`
- original: If needed, you can change the time you administer Toujeo, just talk to your doctor about this.
  - S1: If needed, you can change the time you administer Toujeo.
  - S2: You should talk to your doctor about this.

**L136.0** `Incomplete Sentence` (0.905) → `excluded_incomplete`
- original: Q: How long can Toujeo stay out of the refrigerator?

**L136.1** `Simple Sentence` (0.742) → `passthrough`
- original: A: Toujeo can stay out of the refrigerator for up to 56 days (8 weeks) according to the prescribing information written on 03/2023.

**L136.2** `Simple Sentence` (0.346) → `passthrough`
- original: If Toujeo if left out the refrigerator for more than 20 or 30 minutes, it should not be put back into the refrigerator.
- pronoun resolved: If Toujeo if left out the refrigerator for more than 20 or 30 minutes, Toujeo should not be put back into the refrigerator.
  - edits: “it” → “Toujeo”

**L137.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Q: What are the different types of insulin?

**L137.1** `Simple Sentence` (0.921) → `passthrough`
- original: A: Insulins are usually grouped as fast-acting, intermediate-acting, or long-acting.

**L137.2** `Simple Sentence` (0.429) → `passthrough`
- original: Within these groups, they can be further classified as human insulin and human insulin analogs.
- pronoun resolved: Within these groups, Insulins can be further classified as human insulin and human insulin analogs.
  - edits: “they” → “Insulins”

**L137.3** `Complex Sentence` (0.944) → `decomposed`
- original: An insulin analog is a human insulin that has one or two amino acids changed which affects how quickly it is absorbed after injection and how fast or slow it acts.
- pronoun resolved: An insulin analog is a human insulin that has one or two amino acids changed which affects how quickly insulin analog is absorbed after injection and how fast or slow insulin analog acts.
  - edits: “it” → “insulin analog”; “it” → “insulin analog”
  - S1: An insulin analog is a human insulin.
  - S2: The insulin analog has one or two amino acids changed.
  - S3: The change affects how quickly the insulin analog is absorbed after injection.
  - S4: The change affects how fast or slow the insulin analog acts.

**L137.4** `Simple Sentence` (0.986) → `passthrough`
- original: Insulin analogs are usually given within 15 minutes of a meal or at the same time as food.

**L138.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Q: Soliqua vs Lantus: What’s the difference between them?
- pronoun resolved: Q: Soliqua vs Lantus: What’s the difference between Soliqua?
  - edits: “them?” → “Soliqua?”

**L138.1** `Compound Sentence` (0.957) → `decomposed`
- original: A: Soliqua is a combination of insulin glargine plus lixisenatide, and Lantus only contains insulin glargine.
  - S1: Soliqua is a combination of insulin glargine plus lixisenatide.
  - S2: Lantus only contains insulin glargine.

**L138.2** `Compound-Complex Sentence` (0.897) → `decomposed`
- original: Both are once-daily injections that are given under the skin (subcutaneously), but Soliqua can only be used in adults with type 2 diabetes whereas Lantus may be used to treat both type 1 and type 2 diabetes in adults and children over the age of six years.
  - S1: Both are once-daily injections.
  - S2: Both are given under the skin.
  - S3: Both are given subcutaneously.
  - S4: Soliqua can only be used in adults with type 2 diabetes.
  - S5: Lantus may be used to treat type 1 diabetes in adults and children over the age of six years.
  - S6: Lantus may be used to treat type 2 diabetes in adults and children over the age of six years.

**L138.3** `Simple Sentence` (0.906) → `passthrough`
- original: Both are made by Sanofi-Aventis.

**L139.0** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: Q: Can Toujeo be given twice a day?

**L139.1** `Complex Sentence` (0.932) → `decomposed`
- original: A: Even though Toujeo is usually given once a day, some people may experience better blood sugar control if the dose is split and given twice a day (every 12 hours).
  - S1: Toujeo is usually given once a day.
  - S2: Some people may experience better blood sugar control if the dose is split.
  - S3: The split dose is given twice a day every 12 hours.

**L140.0** `Incomplete Sentence` (0.903) → `excluded_incomplete`
- original: Q: How many pens are in a box of Toujeo?

**L140.1** `Simple Sentence` (0.508) → `passthrough`
- original: A: There are three pens in a box of Toujeo Solostar.

**L140.2** `Simple Sentence` (0.967) → `passthrough`
- original: There are two pens in a box of Toujeo Max Solostar.

**L141.0** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Q: Is Toujeo a fast or long-acting insulin?

**L141.1** `Simple Sentence` (0.985) → `passthrough`
- original: A: Toujeo is a long-acting insulin that is usually given once a day.

**L141.2** `Simple Sentence` (0.978) → `passthrough`
- original: Toujeo lasts for up to 36 hours.

**L142.0** `Incomplete Sentence` (0.924) → `excluded_incomplete`
- original: Q: What is the difference between Soliqua and Xultophy?

**L142.1** `Simple Sentence` (0.909) → `passthrough`
- original: A: The main difference between Soliqua and Xultophy is what is inside each pen.

**L142.2** `Complex Sentence` (0.388) → `decomposed`
- original: Both are once-a-day shots for type 2 diabetes that combine a long-acting (basal) insulin with a GLP-1 medicine.
  - S1: Both are once-a-day shots for type 2 diabetes.
  - S2: The shots combine a long-acting (basal) insulin with a GLP-1 medicine.

**L142.3** `Simple Sentence` (0.991) → `passthrough`
- original: Soliqua 100/33 pairs insulin glargine (Lantus) with lixisenatide (Adlyxin).

**L142.4** `Simple Sentence` (0.973) → `passthrough`
- original: Xultophy 100/3.6 pairs insulin degludec (Tresiba) with liraglutide (Victoza).

**L142.5** `Compound Sentence` (0.502) → `decomposed`
- original: They also differ in how and when you inject them, their heart-health data, common side effects, and cost
- pronoun resolved: Soliqua and Xultophy also differ in how and when you inject them, their heart-health data, common side effects, and cost
  - edits: “They” → “Soliqua and Xultophy”
  - S1: Soliqua and Xultophy also differ in how and when you inject them.
  - S2: They differ in their heart-health data.
  - S3: They differ in their common side effects.
  - S4: They differ in their cost.
