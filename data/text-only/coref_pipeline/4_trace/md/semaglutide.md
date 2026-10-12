# Semaglutide — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/semaglutide.txt` · 337 sentences · 19 changed by pronoun resolution · 481 sentences sent to EDC

## What is semaglutide?

**L5.0** `Complex Sentence` (0.862) → `decomposed`
- original: Semaglutide (Ozempic, Wegovy, Rybelsus) is a prescription GLP-1 medication used for weight loss and weight management, type 2 diabetes treatment, or to reduce the risk of chronic kidney disease and major cardiovascular events in certain patients with type 2 diabetes.
  - S1: Semaglutide is a prescription GLP-1 medication.
  - S2: Semaglutide is used for weight loss and weight management.
  - S3: Semaglutide is used for type 2 diabetes treatment.
  - S4: Semaglutide is used to reduce the risk of chronic kidney disease and major cardiovascular events.
  - S5: This risk reduction applies to certain patients with type 2 diabetes.

**L5.1** `Complex Sentence` (0.659) → `decomposed`
- original: Semaglutide (Wegovy) is also used to treat metabolic dysfunction-associated steatohepatitis (MASH), without cirrhosis of the liver.
  - S1: Semaglutide (Wegovy) is used to treat metabolic dysfunction-associated steatohepatitis (MASH).
  - S2: This treatment is for cases without cirrhosis of the liver.

**L6.0** `Compound Sentence` (0.949) → `decomposed`
- original: Semaglutide injections are self-administered once weekly as an injection under the skin, and semaglutide pills are taken once daily.
  - S1: Semaglutide injections are self-administered once weekly as an injection under the skin.
  - S2: Semaglutide pills are taken once daily.

**L7.0** `Compound Sentence` (0.67) → `decomposed`
- original: Semaglutide works by reducing appetite, delaying gastric emptying, increasing insulin release, and lowering the amount of glucagon released.
  - S1: Semaglutide works by reducing appetite.
  - S2: It works by delaying gastric emptying.
  - S3: It works by increasing insulin release.
  - S4: It works by lowering the amount of glucagon released.

**L7.1** `Complex Sentence` (0.896) → `decomposed`
- original: Semaglutide is a GLP-1 receptor agonist that mimics the behavior of the GLP-1 hormone, which is naturally released after eating.
  - S1: Semaglutide is a GLP-1 receptor agonist.
  - S2: Semaglutide mimics the behavior of the GLP-1 hormone.
  - S3: The GLP-1 hormone is naturally released after eating.

**L8.0** `Simple Sentence` (0.752) → `passthrough`
- original: Semaglutide brand names are Ozempic, Rybelsus, and Wegovy, all made by Novo Nordisk.

**L8.1** `Simple Sentence` (0.985) → `passthrough`
- original: There is no generic semaglutide available.

**L8.2** `Simple Sentence` (0.65) → `passthrough`
- original: Semaglutide FDA approval was first granted on December 5, 2017, for the brand Ozempic.

**L9.0** `Simple Sentence` (0.97) → `passthrough`
- original: Each semaglutide brand or formulation is FDA-approved for specific conditions and patient populations.

## What is semaglutide used for?

**L12.0** `Complex Sentence` (0.522) → `decomposed`
- original: Semaglutide FDA-approved uses for each brand are Ozempic (type 2 diabetes, reducing cardiovascular event risks, reducing risk of kidney function decline), Wegovy (weight management, reducing cardiovascular event risks, non-cirrhotic MASH), and Rybelsus (type 2 diabetes, reducing cardiovascular event risks).
  - S1: Semaglutide has FDA-approved uses for each brand.
  - S2: Ozempic is approved for type 2 diabetes, reducing cardiovascular event risks, and reducing risk of kidney function decline.
  - S3: Wegovy is approved for weight management, reducing cardiovascular event risks, and non-cirrhotic MASH.
  - S4: Rybelsus is approved for type 2 diabetes and reducing cardiovascular event risks.

**L13.0** `Simple Sentence` (0.95) → `passthrough`
- original: Semaglutide should be used in addition to a reduced-calorie diet and increased physical activity.

**L14.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: What is Ozempic used for?

**L14.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L15.0** `Simple Sentence` (0.981) → `passthrough`
- original: Ozempic tablets and injections are FDA-approved in adults for:

**L16.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: type 2 diabetes to improve blood sugar control

**L17.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: reducing the risk of a major cardiovascular event (such as heart attack, stroke, or death) in type 2 diabetic patients who are at high risk for these events

**L18.0** `Simple Sentence` (0.98) → `passthrough`
- original: Ozempic injection is also FDA-approved in adults for:

**L19.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: reducing the risk of kidney function decline, kidney failure, and cardiovascular death in patients with type 2 diabetes and chronic kidney disease (CKD)

**L20.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: What is Wegovy used for?

**L20.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L21.0** `Simple Sentence` (0.984) → `passthrough`
- original: Wegovy tablets and injections are FDA-approved in adults for:

**L22.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: weight loss and weight management in adults with obesity or adults who are overweight and have a weight-related medical problem (e.g., blood pressure, type 2 diabetes, or high cholesterol)

**L23.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: reducing major cardiovascular event risks (such as heart attack, stroke, or death) in adults with established CV disease and either obesity or overweight

**L24.0** `Simple Sentence` (0.938) → `passthrough`
- original: Wegovy injection is also FDA-approved for:

**L25.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: weight loss and weight management patients with obesity who are 12 years and older

**L26.0** `Complex Sentence` (0.863) → `decomposed`
- original: non-cirrhotic metabolic dysfunction-associated steatohepatitis (MASH) in adults with moderate to advanced liver fibrosis (consistent with stages F2 to F3 fibrosis), this is an accelerated approval.
  - S1: This is an accelerated approval.
  - S2: The approval is for non-cirrhotic metabolic dysfunction-associated steatohepatitis (MASH) in adults.
  - S3: The adults have moderate to advanced liver fibrosis.
  - S4: The fibrosis is consistent with stages F2 to F3.

**L27.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: What is Rybelsus used for?

**L27.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L28.0** `Simple Sentence` (0.984) → `passthrough`
- original: Rybelsus oral tablets are FDA-approved in adults for:

**L29.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: type 2 diabetes in adults to help control blood sugar levels.

**L30.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: reducing the risk of major cardiovascular events (such as heart attack, stroke, or death) in type 2 diabetic patients with known heart disease.

**L31.0** `Incomplete Sentence` (0.852) → `excluded_incomplete`
- original: Also, see Wegovy vs Ozempic: Which is right for you?

## Ozempic vs Wegovy vs Rybelsus: Key Differences (Form, Dose, Strength & Uses)

**L34.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Ozempic | Wegovy | Rybelsus

**L35.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Form | subcutaneous injection, tablet | subcutaneous injection, tablet | tablet

**L36.0** `Incomplete Sentence` (0.898) → `excluded_incomplete`
- original: Strength | Injections: 0.25 mg or 0.5 mg dose pen, 1 mg dose pen, 2mg dose pen.

**L36.1** `Compound-Complex Sentence` (0.581) → `decomposed`
- original: Tablet: 1.5 mg, 4 mg tablet, 9 mg | Injections: 0.25 mg dose pen, 0.5 mg dose pen, 1 mg dose pen, 1.7 mg dose pen, 2.4 mg dose pen,7.2 mg dose pen Tablet: 1.5 mg, 4 mg, 9 mg, 25 mg | R1 formulation: 3 mg tablet, 7 mg tablet, and 14 mg tablet R2 formulation: 1.5 mg, 4 mg, and 9 mg tablets (Rebranded as Ozempic tablets)
  - S1: There is a 1.5 mg tablet.
  - S2: There is a 4 mg tablet.
  - S3: There is a 9 mg tablet.
  - S4: There is a 0.25 mg dose pen.
  - S5: There is a 0.5 mg dose pen.
  - S6: There is a 1 mg dose pen.
  - S7: There is a 1.7 mg dose pen.
  - S8: There is a 2.4 mg dose pen.
  - S9: There is a 7.2 mg dose pen.
  - S10: There is a 25 mg tablet.
  - S11: The R1 formulation includes a 3 mg tablet.
  - S12: The R1 formulation includes a 7 mg tablet.
  - S13: The R1 formulation includes a 14 mg tablet.
  - S14: The R2 formulation includes 1.5 mg tablets.
  - S15: The R2 formulation includes 4 mg tablets.
  - S16: The R2 formulation includes 9 mg tablets.
  - S17: The R2 formulation is rebranded as Ozempic tablets.

**L37.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Dose | weekly (injection), daily (tablet) | weekly (injection), daily (tablet) | daily

**L38.0** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Uses | Type 2 diabetic adults to help control blood sugar levels (injection, tablets).

**L38.1** `Compound-Complex Sentence` (0.444) → `decomposed`
- original: Reduce the risk of major cardiac events in patients with type 2 diabetes and cardiovascular disease (injection, tablets) Reduce the risk of kidney function decline, kidney failure, and death due to cardiovascular disease in adults with chronic kidney disease (CKD) and type 2 diabetes (injection) | Weight loss and weight management for patients with obesity aged 12 years and older (injection) or adults (tablets).
  - S1: Reduce the risk of major cardiac events in patients with type 2 diabetes and cardiovascular disease.
  - S2: Reduce the risk of major cardiac events in patients with type 2 diabetes and cardiovascular disease using injections or tablets.
  - S3: Reduce the risk of kidney function decline in adults with chronic kidney disease and type 2 diabetes.
  - S4: Reduce the risk of kidney failure in adults with chronic kidney disease and type 2 diabetes.
  - S5: Reduce the risk of death due to cardiovascular disease in adults with chronic kidney disease and type 2 diabetes.
  - S6: Reduce the risk of kidney function decline, kidney failure, and death due to cardiovascular disease in adults with chronic kidney disease and type 2 diabetes using injections.
  - S7: Achieve weight loss and weight management for patients with obesity aged 12 years and older.
  - S8: Achieve weight loss and weight management for patients with obesity aged 12 years and older using injections.
  - S9: Achieve weight loss and weight management for adults with obesity using tablets.
  - S10: Achieve weight loss and weight management for patients with obesity aged 12 years and older or adults using injections or tablets.

**L38.2** `Incomplete Sentence` (0.956) → `excluded_incomplete`
- original: Reduce major cardiovascular event risks in adults with type 2 diabetes with known heart disease (injection, tablets).

**L38.3** `Incomplete Sentence` (0.966) → `excluded_incomplete`
- original: Non-cirrhotic metabolic dysfunction-associated steatohepatitis (MASH) in patients with moderate to advanced liver fibrosis (consistent with stages F2 to F3 fibrosis) in adults (injection only).

**L38.4** `Complex Sentence` (0.433) → `decomposed`
- original: | Type 2 diabetic adults to help control blood sugar levels Reduce major cardiovascular event risks in adults with type 2 diabetes with known heart disease.
  - S1: Type 2 diabetic adults should help control blood sugar levels.
  - S2: The goal is to reduce major cardiovascular event risks.
  - S3: This applies to adults with type 2 diabetes and known heart disease.

## How does semaglutide work?

**L41.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Semaglutide works by:

**L42.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Stimulates insulin production in the pancreas

**L43.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Reduces sugar production in the liver

**L44.0** `Incomplete Sentence` (0.951) → `excluded_incomplete`
- original: Slows down digestion, so food stays in the stomach longer

**L45.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Decreases appetite and food intake

**L46.0** `Compound Sentence` (0.555) → `decomposed`
- original: These combined actions help you feel full longer, eat less, and maintain better control over blood sugar levels.
  - S1: These combined actions help you feel full longer.
  - S2: They help you eat less.
  - S3: They help you maintain better control over blood sugar levels.

**L46.1** `Compound Sentence` (0.859) → `decomposed`
- original: As a result, semaglutide supports weight loss, improves blood sugar management, and helps reduce the risk of cardiovascular events.
  - S1: As a result, semaglutide supports weight loss.
  - S2: It improves blood sugar management.
  - S3: It helps reduce the risk of cardiovascular events.

**L47.0** `Complex Sentence` (0.928) → `decomposed`
- original: Semaglutide's mechanism of action mimics a natural hormone in the body called GLP-1 (glucagon-like peptide-1), which is released after eating to help regulate appetite and blood sugar levels.
  - S1: Semaglutide's mechanism of action mimics a natural hormone in the body called GLP-1.
  - S2: GLP-1 is released after eating.
  - S3: GLP-1 helps regulate appetite and blood sugar levels.

**L48.0** `Simple Sentence` (0.911) → `passthrough`
- original: The way semaglutide works for kidney-related risk reduction is not fully understood.

**L49.0** `Simple Sentence` (0.989) → `passthrough`
- original: Semaglutide belongs to the drug class called GLP-1 receptor agonists.

## What is the cost of semaglutide?

**L52.0** `Simple Sentence` (0.921) → `passthrough`
- original: The cost of semaglutide varies depending on your insurance plan and which pharmacy you use.

**L53.0** `Simple Sentence` (0.663) → `passthrough`
- original: Refer to our Ozempic price guide page for more information about the Ozempic cost.

**L53.1** `Simple Sentence` (0.962) → `passthrough`
- original: You may also be eligible for an Ozempic coupon or savings card.

**L54.0** `Simple Sentence` (0.693) → `passthrough`
- original: Refer to our Wegovy price guide page for more information about the Wegovy cost.

**L54.1** `Simple Sentence` (0.956) → `passthrough`
- original: You may also be eligible for a Wegovy coupon or savings card.

**L55.0** `Simple Sentence` (0.607) → `passthrough`
- original: Refer to our Rybelsus price guide page for more information about the Rybelsus cost.

**L55.1** `Simple Sentence` (0.963) → `passthrough`
- original: You may also be eligible for a Rybelsus coupon or savings card.

## Semaglutide side effects

**L58.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Common semaglutide side effects:

**L59.0** `Complex Sentence` (0.684) → `decomposed` · repaired
- original: Common semaglutide side effects may include upset stomach, heartburn, burping, gas, bloating, nausea, vomiting, stomach pain, loss of appetite, diarrhea, constipation, stomach flu symptoms, low blood sugar (in people with type 2 diabetes), headache, dizziness, tiredness, hair loss, and changes in skin sensations.
  - S1: Common semaglutide side effects may include upset stomach, heartburn, burping, gas, bloating, nausea, vomiting, stomach pain, loss of appetite, diarrhea, constipation, stomach flu symptoms, headache, dizziness, tiredness, hair loss, and changes in skin sensations.

**L60.0** `Compound-Complex Sentence` (0.802) → `decomposed`
- original: Stomach or gastrointestinal side effects are common, but they tend to be mild and clear up in a few weeks and usually will not interfere with long-term treatment.
- pronoun resolved: Stomach or gastrointestinal side effects are common, but Stomach or gastrointestinal side effects tend to be mild and clear up in a few weeks and usually will not interfere with long-term treatment.
  - edits: “they” → “Stomach or gastrointestinal side effects”
  - S1: Stomach or gastrointestinal side effects are common.
  - S2: Stomach or gastrointestinal side effects tend to be mild.
  - S3: Stomach or gastrointestinal side effects clear up in a few weeks.
  - S4: Stomach or gastrointestinal side effects usually will not interfere with long-term treatment.

**L60.1** `Simple Sentence` (0.988) → `passthrough`
- original: Stomach side effects can be more common with higher doses.

**L61.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Tips for managing stomach side effects:

**L62.0** `Simple Sentence` (0.987) → `passthrough`
- original: Following these tips may help you manage stomach semaglutide side effects:

**L63.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Eat more slowly

**L64.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Eat smaller meals

**L65.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Choose more bland, low-fat foods (like crackers, toast, and rice)

**L66.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Avoid eating greasy, fried foods or sugar treats

**L67.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Eat foods that contain water (like soup or gelatin)

**L68.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: Do not lie down right after eating

**L69.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Drink clear or ice-cold liquids

**L70.0** `Incomplete Sentence` (0.936) → `excluded_incomplete`
- original: If possible, go outside for fresh air if you feel sick to your stomach

**L71.0** `Simple Sentence` (0.991) → `passthrough`
- original: Ryebelsus is not recommended in patients with severe gastroparesis.

**L72.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Tips for managing low blood sugar levels (hypoglycemia) side effects:

**L73.0** `Incomplete Sentence` (0.83) → `excluded_incomplete`
- original: Test blood sugar levels regularly if you are also taking diabetic medicines, including insulin or sulphonylureas (e.g., glibenclamide/glyburide, glipizide, and gliclazide) and when you increase your semaglutide dose.

**L74.0** `Simple Sentence` (0.431) → `passthrough`
- original: Your prescriber might reduce your dose of insulin or sulphonylureas if needed to reduce the risk of hypoglycemia

**L75.0** `Simple Sentence` (0.964) → `passthrough`
- original: Symptoms of low blood sugar levels include:

**L76.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Treatment for hypoglycemia

**L77.0** `Simple Sentence` (0.988) → `passthrough`
- original: Severe hypoglycemia may require a glucagon injection.

**L78.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious semaglutide side effects:

**L79.0** `Compound Sentence` (0.498) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction: hives, itching, dizziness, fast heartbeats, difficulty breathing, swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction.
  - S2: Signs of an allergic reaction include hives, itching, dizziness, fast heartbeats, difficulty breathing, and swelling of your face, lips, tongue, or throat.

**L80.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L81.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: vision changes;

**L82.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: unusual mood changes, thoughts about hurting yourself;

**L83.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: pounding heartbeats or fluttering in your chest;

**L84.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a light-headed feeling, like you might pass out;

**L85.0** `Incomplete Sentence` (0.92) → `excluded_incomplete`
- original: signs of a thyroid tumor - swelling or a lump in your neck, trouble swallowing, a hoarse voice, feeling short of breath;

**L86.0** `Simple Sentence` (0.794) → `passthrough`
- original: symptoms of pancreatitis - severe pain in your upper stomach spreading to your back, nausea with or without vomiting, fast heart rate;

**L87.0** `Incomplete Sentence` (0.953) → `excluded_incomplete`
- original: gallbladder problems - upper stomach pain, fever, clay-colored stools, jaundice (yellowing of the skin or eyes);

**L88.0** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: low blood sugar - headache, hunger, weakness, sweating, confusion, irritability, dizziness, fast heart rate, or feeling jittery;

**L89.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: kidney problems - swelling, urinating less, feeling tired or short of breath; or

**L90.0** `Compound Sentence` (0.778) → `decomposed`
- original: stomach flu symptoms - stomach cramps, vomiting, loss of appetite, diarrhea (may be watery or bloody); or severe stomach problems like severe constipation, fecal impaction, or intestinal obstruction.
  - S1: Stomach flu symptoms include stomach cramps, vomiting, loss of appetite, and diarrhea.
  - S2: The diarrhea may be watery or bloody.
  - S3: Severe stomach problems include severe constipation, fecal impaction, or intestinal obstruction.

**L91.0** `Compound Sentence` (0.545) → `decomposed`
- original: This is not a complete list of side effects, and others may occur.
  - S1: This is not a complete list of side effects.
  - S2: Others may occur.

**L91.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L91.2** `Simple Sentence` (0.97) → `passthrough`
- original: You may report side effects to the FDA at 1-800-FDA-1088.

## Warnings

**L94.0** `Simple Sentence` (0.972) → `passthrough`
- original: Semaglutide has a boxed warning for the risk of thyroid C-cell tumors.

**L94.1** `Simple Sentence` (0.978) → `passthrough`
- original: A boxed warning is the strongest safety-related warning issued by the FDA.

**L94.2** `Simple Sentence` (0.865) → `passthrough`
- original: Semaglutide may cause serious side effects, including possible thyroid tumors and thyroid cancer.

**L95.0** `Compound Sentence` (0.304) → `decomposed`
- original: Call your doctor at once if you have signs of a thyroid tumor, such as swelling or a lump in your neck, trouble swallowing, a hoarse voice, or shortness of breath.
  - S1: Call your doctor at once if you have signs of a thyroid tumor.
  - S2: These signs include swelling or a lump in your neck.
  - S3: They also include trouble swallowing.
  - S4: A hoarse voice is another sign.
  - S5: Shortness of breath is also a sign.

**L96.0** `Complex Sentence` (0.593) → `decomposed`
- original: You should not use semaglutide if you have multiple endocrine neoplasia type 2 (tumors in your glands) or a personal or family history of medullary thyroid cancer.
  - S1: You should not use semaglutide if you have multiple endocrine neoplasia type 2.
  - S2: Multiple endocrine neoplasia type 2 involves tumors in your glands.
  - S3: You should not use semaglutide if you have a personal or family history of medullary thyroid cancer.

**L97.0** `Compound Sentence` (0.45) → `decomposed`
- original: Semaglutide also has warnings for pancreatitis, diabetic retinopathy complications, hypoglycemia that can be severe, acute kidney injury, acute gallbladder disease, hypersensitivity reactions, and pulmonary aspiration during general anesthesia or deep sedation.
  - S1: Semaglutide also has warnings for pancreatitis.
  - S2: It has warnings for diabetic retinopathy complications.
  - S3: It has warnings for hypoglycemia that can be severe.
  - S4: It has warnings for acute kidney injury.
  - S5: It has warnings for acute gallbladder disease.
  - S6: It has warnings for hypersensitivity reactions.
  - S7: It has warnings for pulmonary aspiration during general anesthesia or deep sedation.

**L97.1** `Simple Sentence` (0.52) → `passthrough`
- original: For Wegovy, there are also warnings for a heart rate increase and suicidal behaviour or ideation.

**L97.2** `Simple Sentence` (0.833) → `passthrough`
- original: For Rybelsus, there is also a warning for severe gastrointestinal side effects.

## Before taking this medicine

**L100.0** `Simple Sentence` (0.964) → `passthrough`
- original: You should not use semaglutide if you are allergic to it, or if you have:
- pronoun resolved: You should not use semaglutide if you are allergic to semaglutide, or if you have:
  - edits: “it,” → “semaglutide,”

**L101.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: multiple endocrine neoplasia type 2 (tumors in your glands);

**L102.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: a personal or family history of medullary thyroid carcinoma (a type of thyroid cancer); or

**L103.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: diabetic ketoacidosis (call your doctor for treatment).

**L104.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Tell your doctor if you have ever had:

**L105.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a stomach or intestinal disorder;

**L106.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: pancreatitis;

**L107.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: are planning surgery or other procedure that uses anesthesia or deep sedation;

**L108.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: kidney disease; or

**L109.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: eye problems caused by diabetes (retinopathy).

**L110.0** `Simple Sentence` (0.989) → `passthrough`
- original: In animal studies, semaglutide caused thyroid tumors or thyroid cancer.

**L110.1** `Simple Sentence` (0.974) → `passthrough`
- original: It is not known whether these effects would occur in people.

**L110.2** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Ask your doctor about your risk.

**L111.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Pregnancy:

**L112.0** `Simple Sentence` (0.785) → `passthrough`
- original: Men and women should stop using semaglutide at least 2 months before they plan to get pregnant.
- pronoun resolved: Men and women should stop using semaglutide at least 2 months before Men and women plan to get pregnant.
  - edits: “they” → “Men and women”

**L112.1** `Incomplete Sentence` (0.937) → `excluded_incomplete`
- original: Ask your doctor for a safer medicine to use during this time.

**L112.2** `Compound Sentence` (0.685) → `decomposed`
- original: Controlling diabetes is very important during pregnancy, as is gaining the right amount of weight.
  - S1: Controlling diabetes is very important during pregnancy.
  - S2: Gaining the right amount of weight is also very important during pregnancy.

**L112.3** `Simple Sentence` (0.587) → `passthrough`
- original: Even if you are overweight, losing weight during pregnancy could harm the unborn baby.

**L113.0** `Simple Sentence` (0.979) → `passthrough`
- original: There is a pregnancy exposure registry for women who use Wegovy during pregnancy.

**L113.1** `Simple Sentence` (0.974) → `passthrough`
- original: The purpose of this registry is to collect information about the health of you and your baby.

**L113.2** `Compound Sentence` (0.633) → `decomposed`
- original: Talk to your healthcare provider about how you can take part in this registry or contact Novo Nordisk at 1-877-390-2760 or www.wegovypregnancyregistry.com.
  - S1: Talk to your healthcare provider about how you can take part in this registry.
  - S2: Contact Novo Nordisk at 1-877-390-2760 or www.wegovypregnancyregistry.com.

**L114.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Breastfeeding:

**L115.0** `Incomplete Sentence` (0.976) → `excluded_incomplete`
- original: Ask a doctor if it is safe to breastfeed while using Ozempic or Wegovy injections.

**L115.1** `Simple Sentence` (0.988) → `passthrough`
- original: Breastfeeding is not recommended during treatment with Wegovy tablets.

**L116.0** `Simple Sentence` (0.979) → `passthrough`
- original: You should not breastfeed while using Rybelsus.

## How should I use or take semaglutide?

**L119.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Semaglutide injection directions:

**L120.0** `Simple Sentence` (0.769) → `passthrough`
- original: Semaglutide injections (Ozempic and Wegovy) are injected under the skin, usually once per week at any time of the day, with or without food.

**L120.1** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Use an injection on the same day each week.

**L121.0** `Incomplete Sentence` (0.975) → `excluded_incomplete`
- original: Read and follow all instructions you have been given.

**L121.1** `Incomplete Sentence` (0.887) → `excluded_incomplete`
- original: Ask your doctor or pharmacist if you need help.

**L122.0** `Incomplete Sentence` (0.956) → `excluded_incomplete`
- original: Prepare an injection only when you are ready to give it.

**L122.1** `Incomplete Sentence` (0.652) → `excluded_incomplete`
- original: Call your pharmacist if the medicine looks cloudy, has changed colors, or has particles in it.

**L123.0** `Simple Sentence` (0.982) → `passthrough`
- original: Your healthcare provider will show you where to inject semaglutide.

**L123.1** `Incomplete Sentence` (0.962) → `excluded_incomplete`
- original: Do not inject into the same place twice in a row.

**L123.2** `Simple Sentence` (0.593) → `passthrough`
- original: If you are visually impaired, the Wegovy FlexTouch pen is not recommended for self-injection.

**L124.0** `Compound Sentence` (0.439) → `decomposed`
- original: If you choose a different weekly injection day, start your new schedule after at least 2 days have passed since the last injection you gave.
  - S1: If you choose a different weekly injection day, start your new schedule after at least 2 days have passed since the last injection you gave.

**L125.0** `Incomplete Sentence` (0.968) → `excluded_incomplete`
- original: Do not use different brands of semaglutide at the same time.

**L126.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Semaglutide tablets directions:

**L127.0** `Complex Sentence` (0.738) → `decomposed`
- original: Semaglutide oral tablets (Ozempic, Wegovy, Rybelsus) are taken once a day at least 30 minutes before the first food, beverage, or other oral medications of the day with no more than 4 ounces of plain water only.
  - S1: Semaglutide oral tablets (Ozempic, Wegovy, Rybelsus) are taken once a day.
  - S2: They are taken at least 30 minutes before the first food, beverage, or other oral medications of the day.
  - S3: They are taken with no more than 4 ounces of plain water only.

**L127.1** `Simple Sentence` (0.64) → `passthrough`
- original: After 30 minutes of taking the tablet, you may eat, drink, or take other oral medicines.

**L127.2** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Swallow tablets whole.

**L127.3** `Incomplete Sentence` (0.935) → `excluded_incomplete`
- original: Do not split, crush, or chew tablets.

**L128.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: General semaglutide use:

**L129.0** `Simple Sentence` (0.866) → `passthrough`
- original: Blood sugar can be affected by stress, illness, surgery, exercise, alcohol use, or skipping meals.

**L130.0** `Simple Sentence` (0.874) → `passthrough`
- original: Low blood sugar (hypoglycemia) can make you feel very hungry, dizzy, irritable, or shaky.

**L130.1** `Simple Sentence` (0.942) → `passthrough`
- original: To quickly treat hypoglycemia, eat or drink hard candy, crackers, raisins, fruit juice, or non-diet soda.

**L130.2** `Simple Sentence` (0.98) → `passthrough`
- original: Your doctor may prescribe glucagon injections in case of severe hypoglycemia.

**L131.0** `Incomplete Sentence` (0.597) → `excluded_incomplete`
- original: Tell your doctor if you have frequent symptoms of high blood sugar (hyperglycemia), such as increased thirst or urination.

**L131.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Ask your doctor before changing your dose or medication schedule.

**L132.0** `Simple Sentence` (0.524) → `passthrough`
- original: Your treatment may also include diet, exercise, weight control, medical tests, and special medical care.

**L133.0** `Simple Sentence` (0.986) → `passthrough`
- original: You may get dehydrated during prolonged illness.

**L133.1** `Incomplete Sentence` (0.483) → `excluded_incomplete`
- original: Call your doctor if you are sick with vomiting or diarrhea, or if you eat or drink less than usual.

**L134.0** `Incomplete Sentence` (0.964) → `excluded_incomplete`
- original: Never share an injection pen, even if you changed the needle.

**L134.1** `Simple Sentence` (0.99) → `passthrough`
- original: Sharing an injection can pass infection or disease from person to person.

**L135.0** `Simple Sentence` (0.981) → `passthrough`
- original: The Ozempic injection pen contains more than one dose.

**L135.1** `Simple Sentence` (0.572) → `passthrough`
- original: After your first use, store the pen with the needle removed in a refrigerator or at room temperature.

**L135.2** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Protect from heat and light.

**L135.3** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Keep the cap on when not in use.

**L135.4** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Throw the pen away 56 days after the first use or if less than 0.25 mg is shown on the dose counter.

**L136.0** `Incomplete Sentence` (0.97) → `excluded_incomplete`
- original: Do not reuse a needle.

**L136.1** `Incomplete Sentence` (0.967) → `excluded_incomplete`
- original: Place it in a puncture-proof "sharps" container and dispose of it following state or local laws.
- pronoun resolved: Place needle in a puncture-proof "sharps" container and dispose of it following state or local laws.
  - edits: “it” → “needle”

**L136.2** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Keep out of the reach of children and pets.

## Semaglutide dosing information

**L139.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Ozempic Dosing Information:

**L140.0** `Simple Sentence` (0.95) → `passthrough`
- original: Ozempic Injection Recommended Dosage:

**L141.0** `Incomplete Sentence` (0.892) → `excluded_incomplete`
- original: Start Ozempic with a 0.25 mg subcutaneous injection (injection under the skin) once weekly for 4 weeks.

**L141.1** `Compound Sentence` (0.794) → `decomposed`
- original: The 0.25 mg dosage is intended for treatment initiation and is not effective for glycemic control.
  - S1: The 0.25 mg dosage is intended for treatment initiation.
  - S2: It is not effective for glycemic control.

**L142.0** `Incomplete Sentence` (0.871) → `excluded_incomplete`
- original: After 4 weeks on the 0.25 mg dosage, increase the dosage to 0.5 mg once weekly.

**L143.0** `Complex Sentence` (0.894) → `decomposed`
- original: If additional glycemic control is needed after at least 4 weeks on the 0.5 mg dosage, the dosage may be increased to 1 mg once weekly.
  - S1: If additional glycemic control is needed after at least 4 weeks on the 0.5 mg dosage.
  - S2: The dosage may be increased to 1 mg once weekly.

**L144.0** `Complex Sentence` (0.896) → `decomposed`
- original: If additional glycemic control is needed after at least 4 weeks on the 1 mg dosage, the dosage may be increased to 2 mg once weekly.
  - S1: If additional glycemic control is needed after at least 4 weeks on the 1 mg dosage.
  - S2: The dosage may be increased to 2 mg once weekly.

**L144.1** `Simple Sentence` (0.983) → `passthrough`
- original: The maximum recommended dosage is 2 mg once weekly.

**L145.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Administer Ozempic once weekly, on the same day each week, at any time of the day, with or without meals.

**L146.0** `Compound Sentence` (0.744) → `decomposed`
- original: The day of weekly administration can be changed if necessary, as long as the time between two doses is at least 2 days (>48 hours).
  - S1: The day of weekly administration can be changed if necessary.
  - S2: The time between two doses must be at least 2 days (>48 hours).

**L147.0** `Simple Sentence` (0.536) → `passthrough`
- original: If a dose is missed, administer Ozempic as soon as possible within 5 days after the missed dose.

**L147.1** `Compound Sentence` (0.645) → `decomposed`
- original: If more than 5 days have passed, skip the missed dose and administer the next dose on the regularly scheduled day.
  - S1: If more than 5 days have passed, skip the missed dose.
  - S2: Administer the next dose on the regularly scheduled day.

**L147.2** `Compound Sentence` (0.412) → `decomposed`
- original: In each case, patients can then resume their regular once-weekly dosing schedule.
  - S1: In each case, patients can resume their regular dosing schedule.
  - S2: The dosing schedule is once-weekly.

**L148.0** `Compound Sentence` (0.954) → `decomposed`
- original: Ozempic is available as single-patient-use injections, and there are multiple strength options:
  - S1: Ozempic is available as single-patient-use injections.
  - S2: There are multiple strength options.

**L149.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: 0.25 mg or 0.5 mg dose pen (4 doses of 0.25 mg and 2 doses of 0.5 mg, or 4 doses of 0.5 mg)

**L150.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: 1 mg dose pen (4 doses per pen)

**L151.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: 2 mg dose pen (4 doses per pen)

**L152.0** `Compound Sentence` (0.779) → `decomposed`
- original: Each Ozempic pen carton contains 4 NovoFine Plus needles with 1mg and 2mg pens and 6 NovoFine Plus needles with the 0.25/0.5mg dose pen.
  - S1: Each Ozempic pen carton contains 4 NovoFine Plus needles with 1mg and 2mg pens.
  - S2: It also contains 6 NovoFine Plus needles with the 0.25/0.5mg dose pen.

**L152.1** `Simple Sentence` (0.951) → `passthrough`
- original: Each injection is pre-filled and intended for use by one patient only.

**L153.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Ozempic Pill Dosing Information:

**L154.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Starting Ozempic Dosage (Initiation phase):

**L155.0** `Incomplete Sentence` (0.775) → `excluded_incomplete`
- original: Days 1 through 30: 1.5 mg orally once daily (this dose is not effective for glycemic control).

**L156.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Escalation and Maintenance Ozempic Dosage:

**L157.0** `Incomplete Sentence` (0.656) → `excluded_incomplete`
- original: Days 31 to 60: 4 mg orally once daily.

**L158.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Day 61 or thereafter if:

**L159.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Wegovy Dosing Information:

**L160.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Wegovy injection dosing information:

**L161.0** `Compound Sentence` (0.851) → `decomposed`
- original: Initiate Wegovy injection with a dose of 0.25 mg injected subcutaneously once weekly and follow the dose escalation schedule below to minimize gastrointestinal adverse reactions.
  - S1: Initiate Wegovy injection with a dose of 0.25 mg injected subcutaneously once weekly.
  - S2: Follow the dose escalation schedule below to minimize gastrointestinal adverse reactions.

**L162.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Initial Wegovy Injection Dose Escalation Schedule (all indications):

**L163.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Week 1 to week 4: 0.25mg once a week

**L164.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: Week 5 to week 8: 0.5mg once a week

**L165.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Week 9 to week 12: 1mg once a week

**L166.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Week 13 to week 16: 1.7mg once a week

**L167.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Maintenance injection dose guidance:

**L168.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Adult weight reduction maintenance dose:

**L169.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: 1.7 mg or 2.4 mg (recommended) injected subcutaneously once weekly.

**L170.0** `Compound Sentence` (0.887) → `decomposed`
- original: Dose may be increased to 7.2 mg subcutaneously once weekly on patients who tolerate the 2.4 mg dosage for at least 4 weeks and additional weight reduction is clinically indicated.
  - S1: Dose may be increased to 7.2 mg subcutaneously once weekly.
  - S2: This increase applies to patients who tolerate the 2.4 mg dosage for at least 4 weeks.
  - S3: The increase is also required when additional weight reduction is clinically indicated.

**L171.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Maximum dose 7.2 mg once weekly

**L172.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Consider treatment response and tolerability when selecting the maintenance dosage

**L173.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Pediatric patients' weight reduction maintenance dose (patients aged 12 years and older):

**L174.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Either 2.4 mg (recommended) or 1.7 mg once weekly.

**L175.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Consider treatment response and tolerability when selecting the maintenance dosage

**L176.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Cardiovascular risk reduction maintenance dose:

**L177.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Either 2.4 mg (recommended) or 1.7 mg once weekly, based on patient response and tolerance.

**L178.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Non-cirrhotic metabolic dysfunction–associated steatohepatitis (MASH) with moderate to advanced liver fibrosis maintenance dose:

**L179.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: 2.4 mg injected once weekly.

**L180.0** `Complex Sentence` (0.792) → `decomposed`
- original: If a patient does not tolerate the 2.4 mg once-weekly maintenance dose, the dose may be reduced to 1.7 mg once weekly.
  - S1: If a patient does not tolerate the 2.4 mg once-weekly maintenance dose, the dose may be reduced.
  - S2: The dose may be reduced to 1.7 mg once weekly.

**L181.0** `Compound Sentence` (0.456) → `decomposed`
- original: Re-escalation to 2.4 mg once weekly may be considered if the lower dose is tolerated.
  - S1: Re-escalation to 2.4 mg once weekly may be considered.
  - S2: This is if the lower dose is tolerated.

**L182.0** `Simple Sentence` (0.92) → `passthrough`
- original: In patients with type 2 diabetes, monitor blood glucose prior to starting Wegovy and during Wegovy treatment.

**L183.0** `Simple Sentence` (0.904) → `passthrough`
- original: Wegovy Injections Strengths available:

**L184.0** `Simple Sentence` (0.982) → `passthrough`
- original: Wegovy 0.25 mg pen delivers one 0.25 mg dose (0.25 mg/0.5 mL)

**L185.0** `Simple Sentence` (0.984) → `passthrough`
- original: Wegovy 0.5 mg pen delivers one 0.5 mg dose (0.5 mg / 0.5 mL)

**L186.0** `Simple Sentence` (0.986) → `passthrough`
- original: Wegovy 1 mg pen delivers one 1 mg dose (1 mg / 0.5 mL)

**L187.0** `Simple Sentence` (0.981) → `passthrough`
- original: Wegovy 1.7 mg pen delivers one 1.7 mg dose (1.7 mg / 0.75 mL)

**L188.0** `Simple Sentence` (0.98) → `passthrough`
- original: Wegovy 2.4 mg pen delivers one 2.4 mg dose (2.4 mg / 0.75 mL)

**L189.0** `Simple Sentence` (0.982) → `passthrough`
- original: Wegovy 7.2 mg pen delivers one 7.2 mg dose (7.2 mg/0.75 mL)

**L190.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Wegovy Tablets Dosing Information:

**L191.0** `Incomplete Sentence` (0.898) → `excluded_incomplete`
- original: Initial dose: 1.5 mg once daily for 30 days.

**L192.0** `Simple Sentence` (0.89) → `passthrough`
- original: Titration: Follow the dosage escalation schedule, titrating every 30 days to achieve the maintenance dosage.

**L193.0** `Simple Sentence` (0.663) → `passthrough`
- original: Maintenance dose: 25 mg orally once daily for cardiovascular risk reduction and weight reduction in adults.

**L194.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Rybelsus Dosing Information:

**L195.0** `Incomplete Sentence` (0.928) → `excluded_incomplete`
- original: Take Rybelsus at least 30 minutes before the first food, beverage, or other oral medications of the day with no more than 4 ounces of plain water only.

**L195.1** `Simple Sentence` (0.769) → `passthrough`
- original: After 30 minutes of taking the tablet, you may eat, drink, or take other oral medicines.
- pronoun resolved: After 30 minutes of taking Semaglutide, you may eat, drink, or take other oral medicines.
  - edits: “the tablet,” → “Semaglutide,”

**L195.2** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Swallow tablets whole.

**L195.3** `Incomplete Sentence` (0.935) → `excluded_incomplete`
- original: Do not split, crush, or chew tablets.

**L196.0** `Simple Sentence` (0.989) → `passthrough`
- original: Rybelsus Recommended Dosage R1 formulation

**L197.0** `Incomplete Sentence` (0.975) → `excluded_incomplete`
- original: Start Rybelsus with 3 mg once daily for 30 days.

**L197.1** `Compound Sentence` (0.819) → `decomposed`
- original: The 3 mg dose is intended for treatment initiation and is not effective for glycemic control.
  - S1: The 3 mg dose is intended for treatment initiation.
  - S2: It is not effective for glycemic control.

**L198.0** `Incomplete Sentence` (0.721) → `excluded_incomplete`
- original: After 30 days on the 3 mg dose, increase the dose to 7 mg once daily.

**L199.0** `Complex Sentence` (0.54) → `decomposed`
- original: Dose may be increased to 14 mg once daily if additional glycemic control is needed after at least 30 days on the 7 mg dose.
  - S1: Dose may be increased to 14 mg once daily.
  - S2: This increase is needed if additional glycemic control is required.
  - S3: This requirement applies after at least 30 days on the 7 mg dose.

**L200.0** `Simple Sentence` (0.978) → `passthrough`
- original: Taking two 7 mg Rybelsus tablets to achieve a 14 mg dose is not recommended.

**L201.0** `Compound Sentence` (0.937) → `decomposed`
- original: If a dose is missed, the missed dose should be skipped, and the next dose should be taken the following day.
  - S1: If a dose is missed, the missed dose should be skipped.
  - S2: The next dose should be taken the following day.

**L202.0** `Simple Sentence` (0.985) → `passthrough`
- original: Rybelsus tablets strengths are available in 3mg, 7mg, and 14mg

**L203.0** `Simple Sentence` (0.99) → `passthrough`
- original: Rybelsus Recommended Dosage R2 formulation

**L204.0** `Incomplete Sentence` (0.976) → `excluded_incomplete`
- original: Start Rybelsus with 1.5 mg once daily for 30 days.

**L204.1** `Compound Sentence` (0.794) → `decomposed`
- original: The 1.5 mg dose is intended for treatment initiation and is not effective for glycemic control.
  - S1: The 1.5 mg dose is intended for treatment initiation.
  - S2: It is not effective for glycemic control.

**L205.0** `Incomplete Sentence` (0.748) → `excluded_incomplete`
- original: After 30 days on the 1.5 mg dose, increase the dose to 4 mg once daily.

**L206.0** `Complex Sentence` (0.548) → `decomposed`
- original: Dose may be increased to 9 mg once daily if additional glycemic control is needed after at least 30 days on the 4 mg dose.
  - S1: Dose may be increased to 9 mg once daily.
  - S2: This increase is needed if additional glycemic control is required.
  - S3: The increase occurs after at least 30 days on the 4 mg dose.

**L207.0** `Compound Sentence` (0.937) → `decomposed`
- original: If a dose is missed, the missed dose should be skipped, and the next dose should be taken the following day.
  - S1: If a dose is missed, the missed dose should be skipped.
  - S2: The next dose should be taken the following day.

**L208.0** `Simple Sentence` (0.984) → `passthrough`
- original: Rybelsus tablets strengths are available in 1.5 mg, 4 mg, and 9 mg

**L209.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Switching Patients between Ozempic and Rybelsus

**L210.0** `Simple Sentence` (0.941) → `passthrough`
- original: Patients treated with Rybelsus 14 mg daily can be transitioned to Ozempic subcutaneous injection 0.5 mg once weekly.

**L210.1** `Simple Sentence` (0.988) → `passthrough`
- original: Patients can start Ozempic the day after their last dose of Rybelsus.

**L211.0** `Simple Sentence` (0.969) → `passthrough`
- original: Patients treated with once-weekly Ozempic 0.5 mg subcutaneous injection can be transitioned to Rybelsus 7 mg or 14 mg.

**L211.1** `Simple Sentence` (0.988) → `passthrough`
- original: Patients can start Rybelsus up to 7 days after their last injection of Ozempic.

**L211.2** `Simple Sentence` (0.99) → `passthrough`
- original: There is no equivalent dose of Rybelsus for Ozempic 1 mg.

## What happens if I miss a dose?

**L214.0** `Simple Sentence` (0.572) → `passthrough`
- original: For Rybelsus: Skip the missed dose and use your next dose at the regular time.

**L215.0** `Incomplete Sentence` (0.611) → `excluded_incomplete`
- original: For Ozempic injection: Use the medicine as soon as you can and then go back to your regular schedule.
- pronoun resolved: For Ozempic injection: Use Ozempic as soon as you can and then go back to your regular schedule.
  - edits: “the medicine” → “Ozempic”

**L215.1** `Compound Sentence` (0.517) → `decomposed`
- original: If you are more than 5 days late for the injection, skip the missed dose and return to your regular schedule.
- pronoun resolved: If you are more than 5 days late for Ozempic, skip the missed dose and return to your regular schedule.
  - edits: “the injection,” → “Ozempic,”
  - S1: If you are more than 5 days late for Ozempic, skip the missed dose.
  - S2: Return to your regular schedule.

**L216.0** `Incomplete Sentence` (0.558) → `excluded_incomplete`
- original: For Wegovy injection: Use the medicine as soon as you can and then go back to your regular schedule.
- pronoun resolved: For Wegovy injection: Use Wegovy as soon as you can and then go back to your regular schedule.
  - edits: “the medicine” → “Wegovy”

**L216.1** `Compound Sentence` (0.464) → `decomposed`
- original: If your next dose is due in less than 2 days (48 hours), skip the missed dose and return to your regular schedule.
  - S1: If your next dose is due in less than 2 days (48 hours), skip the missed dose.
  - S2: Return to your regular schedule.

**L216.2** `Incomplete Sentence` (0.867) → `excluded_incomplete`
- original: Call your doctor if you miss more than 2 doses in a row of Wegovy injection.

**L216.3** `Simple Sentence` (0.976) → `passthrough`
- original: You may need to restart the medicine at a lower dose to avoid stomach problems.
- pronoun resolved: You may need to restart Wegovy at a lower dose to avoid stomach problems.
  - edits: “the medicine” → “Wegovy”

**L217.0** `Complex Sentence` (0.416) → `decomposed`
- original: For Wegovy tablets: If you miss a dose of Wegovy tablets, skip the missed dose and go back to your regular schedule for the next dose.
  - S1: This instruction applies to Wegovy tablets.
  - S2: If you miss a dose of Wegovy tablets, skip the missed dose.
  - S3: Then go back to your regular schedule for the next dose.

**L218.0** `Incomplete Sentence` (0.624) → `excluded_incomplete`
- original: Do not use two doses of semaglutide at one time.

## What happens if I overdose?

**L221.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L222.0** `Simple Sentence` (0.954) → `passthrough`
- original: Overdose may cause severe nausea, vomiting, or low blood sugar.

## What other drugs will affect semaglutide?

**L225.0** `Compound Sentence` (0.963) → `decomposed`
- original: Semaglutide can slow your digestion, and it may take longer for your body to absorb any medicines you take by mouth.
- pronoun resolved: Semaglutide can slow your digestion, and semaglutide may take longer for your body to absorb any medicines you take by mouth.
  - edits: “it” → “semaglutide”
  - S1: Semaglutide can slow your digestion.
  - S2: Semaglutide may take longer for your body to absorb any medicines you take by mouth.

**L226.0** `Incomplete Sentence` (0.609) → `excluded_incomplete`
- original: Tell your doctor about all your other medicines, especially insulin or other diabetes medicines, such as dulaglutide, exenatide, liraglutide, Byetta, Trulicity, Victoza, and others.

**L227.0** `Complex Sentence` (0.65) → `decomposed`
- original: Other drugs may affect semaglutide, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may affect semaglutide.
  - S2: These other drugs include prescription medicines.
  - S3: These other drugs include over-the-counter medicines.
  - S4: These other drugs include vitamins.
  - S5: These other drugs include herbal products.

**L227.1** `Incomplete Sentence` (0.967) → `excluded_incomplete`
- original: Tell your doctor about all other medicines you use.

## Storage

**L230.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Ozempic

**L231.0** `Simple Sentence` (0.714) → `passthrough`
- original: Prior to first use, Ozempic should be stored in a refrigerator between 36ºF to 46ºF (2ºC to 8ºC).

**L231.1** `Incomplete Sentence` (0.976) → `excluded_incomplete`
- original: Do not store in the freezer or directly adjacent to the refrigerator cooling element.

**L231.2** `Incomplete Sentence` (0.878) → `excluded_incomplete`
- original: Do not freeze Ozempic and do not use Ozempic if it has been frozen.
- pronoun resolved: Do not freeze Ozempic and do not use Ozempic if Ozempic has been frozen.
  - edits: “it” → “Ozempic”

**L232.0** `Complex Sentence` (0.501) → `decomposed`
- original: After the first use of the Ozempic pen, the pen can be stored for 56 days at controlled room temperature (59°F to 86°F; 15°C to 30°C) or in a refrigerator (36°F to 46°F; 2°C to 8°C).
  - S1: After the first use of the Ozempic pen, the pen can be stored for 56 days.
  - S2: The pen can be stored at controlled room temperature.
  - S3: The pen can be stored in a refrigerator.
  - S4: The controlled room temperature is 59°F to 86°F (15°C to 30°C).
  - S5: The refrigerator temperature is 36°F to 46°F (2°C to 8°C).

**L232.1** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Do not freeze.

**L233.0** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: Keep the pen cap on when not in use.

**L233.1** `Simple Sentence` (0.984) → `passthrough`
- original: Ozempic should be protected from excessive heat and sunlight.

**L234.0** `Incomplete Sentence` (0.756) → `excluded_incomplete`
- original: Always remove and safely discard the needle after each injection and store the Ozempic pen without an injection needle attached.

**L234.1** `Incomplete Sentence` (0.967) → `excluded_incomplete`
- original: Always use a new needle for each injection.

**L235.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Wegovy Injection

**L236.0** `Incomplete Sentence` (0.897) → `excluded_incomplete`
- original: Store the single-dose pen or syringe in the refrigerator from 2°C to 8°C (36°F to 46°F).

**L236.1** `Incomplete Sentence` (0.814) → `excluded_incomplete`
- original: Do not store Wegovy in the freezer or directly beside the refrigerator cooling element.

**L236.2** `Incomplete Sentence` (0.635) → `excluded_incomplete`
- original: Do not freeze Wegovy and do not use it if it has been frozen.

**L236.3** `Complex Sentence` (0.749) → `decomposed`
- original: If needed, prior to cap removal, the single-dose pen or syringe can be kept from 8°C to 30°C (46°F to 86°F) for up to 28 days.
  - S1: The single-dose pen or syringe can be kept from 8°C to 30°C (46°F to 86°F) for up to 28 days.
  - S2: This storage is allowed prior to cap removal.
  - S3: This storage is allowed if needed.

**L236.4** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Protect Wegovy from light.

**L236.5** `Simple Sentence` (0.981) → `passthrough`
- original: Wegovy must be kept in the original carton until time of administration.

**L236.6** `Incomplete Sentence` (0.975) → `excluded_incomplete`
- original: Discard the Wegovy single-dose pen or syringe after use.

**L236.7** `Simple Sentence` (0.489) → `passthrough`
- original: For the Wegovy FlexTouch single-patient-use pen, store in the refrigerator until first use.

**L236.8** `Incomplete Sentence` (0.912) → `excluded_incomplete`
- original: After first use, store between 59°F to 86°F (15°C to 30°C) or in the refrigerator for up to 56 days.

**L236.9** `Incomplete Sentence` (0.707) → `excluded_incomplete`
- original: Keep the pen cap on when not in use and remove the needle after each injection.

**L237.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Wegovy, Ozempic, Rybelsus Tablets

**L238.0** `Incomplete Sentence` (0.895) → `excluded_incomplete`
- original: Store Wegovy tablets at room temperature between 68°F and 77°F (20°C to 25°C) in their original closed bottle until you are ready to take one.

**L238.1** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Do not store in any other container.

**L239.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Store in a dry place away from moisture.

## What are the Ingredients of semaglutide?

**L242.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Active ingredient: semaglutide Inactive ingredients:

**L243.0** `Incomplete Sentence` (0.542) → `excluded_incomplete`
- original: Ozempic injection: disodium phosphate dihydrate, propylene glycol, phenol, and water for injections.

**L243.1** `Simple Sentence` (0.978) → `passthrough`
- original: Ozempic has a pH of approximately 7.4.

**L243.2** `Simple Sentence` (0.979) → `passthrough`
- original: Hydrochloric acid or sodium hydroxide may be added to adjust pH.

**L244.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Ozempic tablet: magnesium stearate and salcaprozate sodium

**L245.0** `Incomplete Sentence` (0.735) → `excluded_incomplete`
- original: Wegovy injection: disodium phosphate dihydrate, sodium chloride, and water for injection.

**L245.1** `Simple Sentence` (0.924) → `passthrough`
- original: Phenol and propylene glycol are also inactive ingredients in the single-patient-use Wegovy FlexTouch.

**L245.2** `Simple Sentence` (0.979) → `passthrough`
- original: Hydrochloric acid or sodium hydroxide may be added to adjust pH.

**L246.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Wegovy tablets: salcaprozate sodium (SNAC) and magnesium stearate

**L247.0** `Simple Sentence` (0.909) → `passthrough`
- original: Rybelsus R1 formulation: magnesium stearate, microcrystalline cellulose, povidone, and salcaprozate sodium (SNAC).

**L248.0** `Simple Sentence` (0.492) → `passthrough`
- original: Rybelsus R2 formulation: magnesium stearate and salcaprozate sodium (SNAC).

## Company

**L251.0** `Simple Sentence` (0.748) → `passthrough`
- original: Ozempic, Wegovy, and Rybelsus are Manufactured by Novo Nordisk A/S, DK-2880 Bagsvaerd, Denmark.

## Popular FAQ

**L254.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Q: Which GLP-1 drug is best for weight loss?

**L254.1** `Complex Sentence` (0.897) → `decomposed`
- original: A: The most effective GLP-1 drug for weight loss currently (as of early 2026) is tirzepatide, marketed under the names Zepbound (for weight loss) and Mounjaro (for diabetes).
  - S1: The most effective GLP-1 drug for weight loss currently is tirzepatide.
  - S2: Tirzepatide is marketed under the name Zepbound for weight loss.
  - S3: Tirzepatide is marketed under the name Mounjaro for diabetes.

**L254.2** `Complex Sentence` (0.928) → `decomposed`
- original: Clinical trials and recent meta-analyses consistently show tirzepatide delivers the most substantial weight reduction among GLP-1 medications, with average losses of up to 22.5% of body weight.
  - S1: Clinical trials and recent meta-analyses consistently show tirzepatide delivers the most substantial weight reduction among GLP-1 medications.
  - S2: The average weight loss is up to 22.5% of body weight.

**L255.0** `Incomplete Sentence` (0.972) → `excluded_incomplete`
- original: Q: Wegovy vs Ozempic: Which is Right for You?

**L255.1** `Compound-Complex Sentence` (0.922) → `decomposed`
- original: A: Both Wegovy and Ozempic contain the GLP-1 agonist semaglutide, but Wegovy is prescribed for long-term weight management and certain forms of liver disease, while Ozempic is used to control blood sugar in type 2 diabetes and help protect the heart and kidneys.
  - S1: Both Wegovy and Ozempic contain the GLP-1 agonist semaglutide.
  - S2: Wegovy is prescribed for long-term weight management.
  - S3: Wegovy is prescribed for certain forms of liver disease.
  - S4: Ozempic is used to control blood sugar in type 2 diabetes.
  - S5: Ozempic is used to help protect the heart.
  - S6: Ozempic is used to help protect the kidneys.

**L255.2** `Compound Sentence` (0.945) → `decomposed`
- original: They both lower the risk for heart-related complications, but differ in other approved uses and populations, side effects, dosage forms and costs.
- pronoun resolved: Wegovy and Ozempic both lower the risk for heart-related complications, but differ in other approved uses and populations, side effects, dosage forms and costs.
  - edits: “They” → “Wegovy and Ozempic”
  - S1: Wegovy and Ozempic both lower the risk for heart-related complications.
  - S2: They differ in other approved uses and populations.
  - S3: They differ in side effects.
  - S4: They differ in dosage forms.
  - S5: They differ in costs.

**L256.0** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: Q: How long does it take for Ozempic to work?

**L256.1** `Complex Sentence` (0.615) → `decomposed`
- original: A: Your blood glucose (sugar) levels should start to decline within the first days to a week after you start using Ozempic (semaglutide).
  - S1: Your blood glucose (sugar) levels should start to decline.
  - S2: This decline should occur within the first days to a week.
  - S3: This happens after you start using Ozempic (semaglutide).

**L256.2** `Compound Sentence` (0.631) → `decomposed`
- original: You will start with lower doses for the first 4 weeks of treatment to help reduce initial stomach side effects, but this is not an effective dose to lower blood sugar over the long-term.
  - S1: You will start with lower doses for the first 4 weeks of treatment to help reduce initial stomach side effects.
  - S2: This is not an effective dose to lower blood sugar over the long-term.

**L256.3** `Simple Sentence` (0.775) → `passthrough`
- original: The full effect can take 12 weeks or longer, depending upon how well you tolerate the medicine.
- pronoun resolved: The full effect can take 12 weeks or longer, depending upon how well you tolerate Ozempic.
  - edits: “the medicine.” → “Ozempic.”

**L257.0** `Incomplete Sentence` (0.976) → `excluded_incomplete`
- original: Q: Tirzepatide vs semaglutide: How do they compare?
- pronoun resolved: Q: Tirzepatide vs semaglutide: How do Tirzepatide vs semaglutide compare?
  - edits: “they” → “Tirzepatide vs semaglutide”

**L257.1** `Simple Sentence` (0.863) → `passthrough`
- original: A: Semaglutide and tirzepatide are prescription medicines used for type 2 diabetes and long-term weight management.

**L257.2** `Compound Sentence` (0.942) → `decomposed`
- original: Semaglutide products include Ozempic, Rybelsus, Wegovy, and Wegovy HD, while tirzepatide products include Mounjaro and Zepbound.
  - S1: Semaglutide products include Ozempic, Rybelsus, Wegovy, and Wegovy HD.
  - S2: Tirzepatide products include Mounjaro and Zepbound.

**L257.3** `Compound Sentence` (0.816) → `decomposed`
- original: These medicines differ in dosing, approved uses, side effects, and cost, so discuss options with your healthcare provider.
- pronoun resolved: Semaglutide and tirzepatide differ in dosing, approved uses, side effects, and cost, so discuss options with your healthcare provider.
  - edits: “These medicines” → “Semaglutide and tirzepatide”
  - S1: Semaglutide and tirzepatide differ in dosing, approved uses, side effects, and cost.
  - S2: You should discuss options with your healthcare provider.

**L258.0** `Incomplete Sentence` (0.523) → `excluded_incomplete`
- original: Q: How long until I'll lose weight with Wegovy?

**L258.1** `Compound Sentence` (0.929) → `decomposed`
- original: A: Wegovy and Wegovy HD take time to work, but you may see some weight loss results in the first 4 weeks of treatment.
  - S1: Wegovy and Wegovy HD take time to work.
  - S2: You may see some weight loss results in the first 4 weeks of treatment.

**L258.2** `Complex Sentence` (0.679) → `decomposed`
- original: Weight loss for both the pill and injection may increase when you get closer to your full maintenance dose, usually after a few months.
  - S1: Weight loss for both the pill and injection may increase.
  - S2: This increase may happen when you get closer to your full maintenance dose.
  - S3: This usually happens after a few months.

**L258.3** `Compound Sentence` (0.85) → `decomposed`
- original: In studies, the average long-term weight loss with Wegovy was 35 to 39 lbs (16 to 17.7 kg) and about 21% of body weight with Wegovy HD.
  - S1: In studies, the average long-term weight loss with Wegovy was 35 to 39 lbs (16 to 17.7 kg).
  - S2: It was about 21% of body weight with Wegovy HD.

**L259.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Q: How does Ozempic work for weight loss?

**L259.1** `Complex Sentence` (0.849) → `decomposed`
- original: A: Ozempic (semaglutide) can help you lose weight by reducing hunger, increasing feelings of fullness, and helping you eat fewer calories.
  - S1: Ozempic (semaglutide) can help you lose weight.
  - S2: It can help you lose weight by reducing hunger.
  - S3: It can help you lose weight by increasing feelings of fullness.
  - S4: It can help you lose weight by helping you eat fewer calories.

**L259.2** `Simple Sentence` (0.983) → `passthrough`
- original: It works like the natural GLP-1 hormone to regulate appetite and food intake.
- pronoun resolved: Ozempic works like the natural GLP-1 hormone to regulate appetite and food intake.
  - edits: “It” → “Ozempic”

**L259.3** `Compound Sentence` (0.891) → `decomposed`
- original: Ozempic also slows stomach emptying, but this does not fully explain its effects on long-term weight loss.
- pronoun resolved: Ozempic also slows stomach emptying, but this does not fully explain Ozempic's effects on long-term weight loss.
  - edits: “its” → “Ozempic's”
  - S1: Ozempic also slows stomach emptying.
  - S2: This does not fully explain Ozempic's effects on long-term weight loss.

**L260.0** `Incomplete Sentence` (0.578) → `excluded_incomplete`
- original: Q: Can you get tirzepatide from a compounding pharmacy?

**L260.1** `Complex Sentence` (0.841) → `decomposed`
- original: A: Tirzepatide cannot be legally compounded in a U.S. pharmacy at this time because it was removed from the FDA drug shortage list as of October 2, 2024.
- pronoun resolved: A: Tirzepatide cannot be legally compounded in a U.S. pharmacy at this time because Tirzepatide was removed from the FDA drug shortage list as of October 2, 2024.
  - edits: “it” → “Tirzepatide”
  - S1: Tirzepatide cannot be legally compounded in a U.S. pharmacy at this time.
  - S2: This is because Tirzepatide was removed from the FDA drug shortage list.
  - S3: The removal occurred as of October 2, 2024.

**L260.2** `Complex Sentence` (0.92) → `decomposed`
- original: When drugs are in short supply, the FDA can allow temporary compounding of some medicines so that patients can access their treatments.
- pronoun resolved: When drugs are in short supply, the FDA can allow temporary compounding of some medicines so that patients can access patients's treatments.
  - edits: “their” → “patients's”
  - S1: When drugs are in short supply, the FDA can allow temporary compounding of some medicines.
  - S2: This allows patients to access their treatments.

**L260.3** `Complex Sentence` (0.854) → `decomposed`
- original: Tirzepatide is now widely available as a prescription medicine made by Eli Lilly under the brands names Mounjaro (for type 2 diabetes) and Zepbound (for weight loss and sleep apnea).
  - S1: Tirzepatide is now widely available as a prescription medicine.
  - S2: The medicine is made by Eli Lilly.
  - S3: It is sold under the brand name Mounjaro for type 2 diabetes.
  - S4: It is sold under the brand name Zepbound for weight loss and sleep apnea.

**L261.0** `Incomplete Sentence` (0.838) → `excluded_incomplete`
- original: Q: Why am I not losing weight on Ozempic?

**L261.1** `Complex Sentence` (0.941) → `decomposed`
- original: A: Although Ozempic is not FDA-approved for weight loss, over 86% of people lose at least 5% of their body weight in trials that have studied semaglutide, the active ingredient of Ozempic.
  - S1: Ozempic is not FDA-approved for weight loss.
  - S2: Over 86% of people lose at least 5% of their body weight in trials.
  - S3: The trials studied semaglutide.
  - S4: Semaglutide is the active ingredient of Ozempic.

**L261.2** `Compound Sentence` (0.891) → `decomposed`
- original: But the same clinical trials also show that just under 14% don’t lose weight, and some may even gain weight.
  - S1: But the same clinical trials also show that just under 14% don't lose weight.
  - S2: Some may even gain weight.

**L262.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Q: Where and how should Ozempic be injected?

**L262.1** `Simple Sentence` (0.771) → `passthrough`
- original: A: Ozempic (semaglutide) comes as a prefilled pen given by self-injection once a week, on the same day each week, with or without meals.

**L262.2** `Simple Sentence` (0.939) → `passthrough`
- original: Ozempic is injected under the skin (subcutaneously) in your stomach (abdomen), thigh, or upper arm area.

**L262.3** `Simple Sentence` (0.977) → `passthrough`
- original: Ozempic also comes as an oral tablet taken once daily if you prefer.
