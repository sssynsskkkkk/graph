# Rosuvastatin — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/rosuvastatin.txt` · 126 sentences · 7 changed by pronoun resolution · 177 sentences sent to EDC

## What is rosuvastatin?

**L5.0** `Complex Sentence` (0.829) → `decomposed`
- original: Rosuvastatin (Crestor) is a prescription medicine used to treat high cholesterol and to reduce the risk of major cardiovascular events such as heart attack and stroke.
  - S1: Rosuvastatin (Crestor) is a prescription medicine.
  - S2: The medicine is used to treat high cholesterol.
  - S3: The medicine is used to reduce the risk of major cardiovascular events.
  - S4: Major cardiovascular events include heart attack and stroke.

**L6.0** `Simple Sentence` (0.989) → `passthrough`
- original: Rosuvastatin belongs to a class of medicines called statins.

**L6.1** `Complex Sentence` (0.451) → `decomposed`
- original: It works by blocking HMG-CoA reductase, the rate-limiting enzyme the liver uses to make cholesterol.
- pronoun resolved: Rosuvastatin works by blocking HMG-CoA reductase, the rate-limiting enzyme the liver uses to make cholesterol.
  - edits: “It” → “Rosuvastatin”
  - S1: Rosuvastatin works by blocking HMG-CoA reductase.
  - S2: HMG-CoA reductase is the rate-limiting enzyme the liver uses to make cholesterol.

**L6.2** `Complex Sentence` (0.867) → `decomposed`
- original: With cholesterol synthesis reduced, the liver increases its LDL receptors and clears more LDL, or "bad" cholesterol, from the blood.
- pronoun resolved: With cholesterol synthesis reduced, the liver increases liver's LDL receptors and clears more LDL, or "bad" cholesterol, from the blood.
  - edits: “its” → “liver's”
  - S1: With cholesterol synthesis reduced, the liver increases its LDL receptors.
  - S2: The liver clears more LDL from the blood.
  - S3: LDL is "bad" cholesterol.

**L6.3** `Compound Sentence` (0.814) → `decomposed`
- original: LDL and total cholesterol levels fall, with the maximum reduction usually reached by four weeks.
  - S1: LDL and total cholesterol levels fall.
  - S2: The maximum reduction is usually reached by four weeks.

**L7.0** `Simple Sentence` (0.987) → `passthrough`
- original: Rosuvastatin comes as a tablet.

**L7.1** `Simple Sentence` (0.743) → `passthrough`
- original: It was first approved by the US Food and Drug Administration (FDA) on August 12, 2003, under the brand name Crestor.
- pronoun resolved: Rosuvastatin was first approved by the US Food and Drug Administration (FDA) on August 12, 2003, under the brand name Crestor.
  - edits: “It” → “Rosuvastatin”

**L7.2** `Simple Sentence` (0.979) → `passthrough`
- original: Many generic versions of rosuvastatin tablets have since been approved.

## What is rosuvastatin used for?

**L10.0** `Simple Sentence` (0.582) → `passthrough`
- original: Rosuvastatin is used:

**L11.0** `Complex Sentence` (0.684) → `decomposed`
- original: to reduce the risk of major adverse cardiovascular (CV) events, such as death from cardiovascular disease, heart attack, stroke, or the need for procedures to improve blood flow to the heart called arterial revascularization, in adults at increased risk for these events.
  - S1: The goal is to reduce the risk of major adverse cardiovascular events.
  - S2: These events include death from cardiovascular disease.
  - S3: These events include heart attack.
  - S4: These events include stroke.
  - S5: These events include the need for procedures to improve blood flow to the heart.
  - S6: These procedures are called arterial revascularization.
  - S7: The target population is adults at increased risk for these events.

**L12.0** `Incomplete Sentence` (0.969) → `excluded_incomplete`
- original: along with diet and exercise to lower the level of low-density lipoprotein (LDL-C) cholesterol or "bad" cholesterol: in adults with primary hypercholesterolemia.

**L12.1** `Incomplete Sentence` (0.901) → `excluded_incomplete`
- original: and slow the buildup of fatty deposits (plaque) in the walls of blood vessels in adults.

**L12.2** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: in adults and children 8 years of age and older with high blood cholesterol due to heterozygous familial hypercholesterolemia (HeFH) (an inherited condition that causes high levels of LDL-C).

**L12.3** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: in adults and children 7 years of age and older with homozygous familial hypercholesterolemia (HoFH) (an inherited condition that causes high levels of LDL-C).

**L13.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: along with diet for the treatment of adults with: primary dysbetalipoproteinemia (an inherited condition that causes high levels of cholesterol and fat).

**L13.1** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: hypertriglyceridemia.

**L14.0** `Complex Sentence` (0.718) → `decomposed`
- original: It is not known if rosuvastatin is safe and effective in children younger than 8 years of age with HeFH, children younger than 7 years of age with HoFH, or in children with other types of hypercholesterolemia (other than HeFH or HoFH).
  - S1: It is not known if rosuvastatin is safe and effective in children younger than 8 years of age with HeFH.
  - S2: It is not known if rosuvastatin is safe and effective in children younger than 7 years of age with HoFH.
  - S3: It is not known if rosuvastatin is safe and effective in children with other types of hypercholesterolemia.
  - S4: These other types of hypercholesterolemia are other than HeFH or HoFH.

## What are the side effects of rosuvastatin?

**L17.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Common side effects:

**L18.0** `Simple Sentence` (0.705) → `passthrough`
- original: The most common side effects may include headache, nausea, muscle aches and pains, weakness, and constipation.

**L19.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious side effects:

**L20.0** `Simple Sentence` (0.975) → `passthrough`
- original: Rosuvastatin may cause serious side effects, including:

**L21.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Muscle pain, tenderness and weakness (myopathy).

**L21.1** `Compound Sentence` (0.916) → `decomposed`
- original: Muscle problems, including muscle breakdown, can be serious in some people and rarely cause kidney damage that can lead to death.
  - S1: Muscle problems, including muscle breakdown, can be serious in some people.
  - S2: They rarely cause kidney damage that can lead to death.

**L21.2** `Complex Sentence` (0.291) → `decomposed`
- original: Tell your doctor right away if: you have unexplained muscle pain, tenderness, or weakness, especially if you have a fever or feel more tired than usual, while you take this medicine.
  - S1: Tell your doctor right away if you have unexplained muscle pain, tenderness, or weakness.
  - S2: Tell your doctor right away if you have a fever.
  - S3: Tell your doctor right away if you feel more tired than usual.
  - S4: These symptoms may occur while you take this medicine.

**L21.3** `Simple Sentence` (0.862) → `passthrough`
- original: you have muscle problems that do not go away even after your doctor has told you to stop taking this medicine.

**L21.4** `Simple Sentence` (0.964) → `passthrough`
- original: Your doctor may do further tests to diagnose the cause of your muscle problems.

**L21.5** `Complex Sentence` (0.716) → `decomposed`
- original: Your chances of getting muscle problems are higher if you: are taking certain other medicines while you take rosuvastatin are 65 years of age or older are of Asian descent have thyroid problems (hypothyroidism) that are not controlled have kidney problems are taking higher doses of this medicine
- pronoun resolved: Your chances of getting muscle problems are higher if you: are taking certain other medicines while you take rosuvastatin are 65 years of age or older are of Asian descent have thyroid problems (hypothyroidism) that are not controlled have kidney problems are taking higher doses of rosuvastatin
  - edits: “this medicine” → “rosuvastatin”
  - S1: Your chances of getting muscle problems are higher if you are taking certain other medicines while you take rosuvastatin.
  - S2: Your chances of getting muscle problems are higher if you are 65 years of age or older.
  - S3: Your chances of getting muscle problems are higher if you are of Asian descent.
  - S4: Your chances of getting muscle problems are higher if you have thyroid problems (hypothyroidism) that are not controlled.
  - S5: Your chances of getting muscle problems are higher if you have kidney problems.
  - S6: Your chances of getting muscle problems are higher if you are taking higher doses of rosuvastatin.

**L22.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Liver problems.

**L22.1** `Compound Sentence` (0.558) → `decomposed`
- original: Your doctor may do blood tests to check your liver before you start taking this medicine and if you have symptoms of liver problems while you are taking it.
- pronoun resolved: Your doctor may do blood tests to check your liver before you start taking rosuvastatin and if you have symptoms of liver problems while you are taking rosuvastatin.
  - edits: “this medicine” → “rosuvastatin”; “it.” → “rosuvastatin.”
  - S1: Your doctor may do blood tests to check your liver before you start taking rosuvastatin.
  - S2: Your doctor may do blood tests to check your liver if you have symptoms of liver problems while you are taking rosuvastatin.

**L22.2** `Complex Sentence` (0.266) → `decomposed`
- original: Call your doctor right away if you have any of the following symptoms of liver problems: feel unusually tired or weak loss of appetite upper belly pain dark urine yellowing of your skin or the whites of your eyes
  - S1: Call your doctor right away if you have any of the following symptoms of liver problems.
  - S2: The symptoms include feeling unusually tired or weak.
  - S3: The symptoms include loss of appetite.
  - S4: The symptoms include upper belly pain.
  - S5: The symptoms include dark urine.
  - S6: The symptoms include yellowing of your skin or the whites of your eyes.

**L23.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Protein and blood in the urine.

**L23.1** `Simple Sentence` (0.991) → `passthrough`
- original: Rosuvastatin may cause you to have protein and blood in your urine.

**L23.2** `Simple Sentence` (0.559) → `passthrough`
- original: If you develop protein or blood in your urine, your doctor may decrease your dose.

**L24.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Increase in blood sugar (glucose) levels.

**L24.1** `Simple Sentence` (0.991) → `passthrough`
- original: Rosuvastatin may cause an increase in your blood sugar levels.

**L25.0** `Complex Sentence` (0.37) → `decomposed`
- original: Additional side effects that have been reported with rosuvastatin include abdominal pain, dizziness, memory loss and confusion.
  - S1: Additional side effects have been reported with rosuvastatin.
  - S2: The reported side effects include abdominal pain, dizziness, memory loss, and confusion.

**L26.0** `Incomplete Sentence` (0.817) → `excluded_incomplete`
- original: Tell your doctor if you have any side effect that bothers you or that does not go away.

**L27.0** `Simple Sentence` (0.941) → `passthrough`
- original: These are not all the possible side effects.

**L27.1** `Incomplete Sentence` (0.669) → `excluded_incomplete`
- original: For more information, ask your doctor or pharmacist.

**L28.0** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L28.1** `Simple Sentence` (0.97) → `passthrough`
- original: You may report side effects to the FDA at 1-800-FDA-1088.

## Who should not take rosuvastatin?

**L31.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Do not take rosuvastatin if you:

**L32.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: are allergic to rosuvastatin or any of the ingredients in your rosuvastatin tablets.

**L32.1** `Simple Sentence` (0.575) → `passthrough`
- original: See below for a complete list of ingredients.

**L33.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: have liver problems.

**L34.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Rosuvastatin pregnancy and breastfeeding warnings (more detail)

## What should I tell my doctor before taking rosuvastatin?

**L37.0** `Incomplete Sentence` (0.841) → `excluded_incomplete`
- original: Before taking rosuvastatin, tell your healthcare provider about all of your medical conditions, including if you:

**L38.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: have unexplained muscle aches or weakness

**L39.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: have or have had kidney problems

**L40.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: have or have had liver problems

**L41.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: drink more than 2 glasses of alcohol daily

**L42.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: have thyroid problems

**L43.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: are of Asian descent

**L44.0** `Incomplete Sentence` (0.934) → `excluded_incomplete`
- original: Also tell your healthcare provider if you are 65 years of age or older.

## How should I take rosuvastatin?

**L47.0** `Incomplete Sentence` (0.943) → `excluded_incomplete`
- original: Take rosuvastatin exactly as your doctor tells you to.

**L48.0** `Incomplete Sentence` (0.905) → `excluded_incomplete`
- original: Take rosuvastatin by mouth once daily.

**L48.1** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Swallow the tablet whole.

**L49.0** `Simple Sentence` (0.986) → `passthrough`
- original: Rosuvastatin can be taken at any time of day, with or without food.

**L50.0** `Compound Sentence` (0.645) → `decomposed`
- original: Do not change your dose or stop this medicine without talking to your doctor, even if you are feeling well.
- pronoun resolved: Do not change your dose or stop rosuvastatin without talking to your doctor, even if you are feeling well.
  - edits: “this medicine” → “rosuvastatin”
  - S1: Do not change your dose or stop rosuvastatin without talking to your doctor.
  - S2: You should do this even if you are feeling well.

**L51.0** `Simple Sentence` (0.758) → `passthrough`
- original: Your doctor may do blood tests to check your cholesterol levels before and during your treatment with rosuvastatin.

**L51.1** `Simple Sentence` (0.971) → `passthrough`
- original: Your doctor may change your dose if needed.

**L52.0** `Simple Sentence` (0.935) → `passthrough`
- original: Your doctor may start you on a cholesterol-lowering diet before giving you rosuvastatin.

**L52.1** `Incomplete Sentence` (0.946) → `excluded_incomplete`
- original: Stay on this diet when you take this medicine.
- pronoun resolved: Stay on this diet when you take rosuvastatin.
  - edits: “this medicine.” → “rosuvastatin.”

**L53.0** `Complex Sentence` (0.628) → `decomposed`
- original: If you take an antacid that contains a combination of aluminum and magnesium hydroxide, take rosuvastatin at least 2 hours before you take the antacid.
  - S1: If you take an antacid that contains a combination of aluminum and magnesium hydroxide.
  - S2: Take rosuvastatin at least 2 hours before you take the antacid.

## What happens if I miss a dose?

**L56.0** `Simple Sentence` (0.626) → `passthrough`
- original: If you miss a dose of rosuvastatin, take your next dose at your normal scheduled time.

**L56.1** `Incomplete Sentence` (0.972) → `excluded_incomplete`
- original: Do not take an extra dose.

## What happens if I overdose?

**L59.0** `Complex Sentence` (0.42) → `decomposed`
- original: In case of an overdose, get medical help or contact a live Poison Center expert right away at 1-800-222-1222.
  - S1: In case of an overdose, get medical help.
  - S2: In case of an overdose, contact a live Poison Center expert right away.
  - S3: The Poison Center expert can be reached at 1-800-222-1222.

**L59.1** `Simple Sentence` (0.899) → `passthrough`
- original: Advice is also available online at poisonhelp.org.

## Dosing information

**L62.0** `Incomplete Sentence` (0.778) → `excluded_incomplete`
- original: Dose range: 5 mg to 40 mg once daily.

**L62.1** `Compound Sentence` (0.709) → `decomposed`
- original: The dose depends on the reason you are taking it, your LDL cholesterol level, and your individual risk of cardiovascular events.
  - S1: The dose depends on the reason you are taking it.
  - S2: The dose depends on your LDL cholesterol level.
  - S3: The dose depends on your individual risk of cardiovascular events.

**L63.0** `Simple Sentence` (0.966) → `passthrough`
- original: People of Asian descent: the recommended starting dose is 5 mg once daily.

**L64.0** `Compound Sentence` (0.899) → `decomposed`
- original: Severe kidney impairment (not on hemodialysis): the recommended starting dose is 5 mg once daily, and the dose should not exceed 10 mg once daily.
  - S1: The recommended starting dose for severe kidney impairment (not on hemodialysis) is 5 mg once daily.
  - S2: The dose should not exceed 10 mg once daily.

**L65.0** `Simple Sentence` (0.615) → `passthrough`
- original: Children with homozygous familial hypercholesterolemia: 20 mg once daily for those 7 years of age and older.

**L66.0** `Compound Sentence` (0.633) → `decomposed`
- original: Children with heterozygous familial hypercholesterolemia: 5 mg to 10 mg once daily for those 8 years to less than 10 years of age, and 5 mg to 20 mg once daily for those 10 years of age and older.
  - S1: Children with heterozygous familial hypercholesterolemia should receive 5 mg to 10 mg once daily for those 8 years to less than 10 years of age.
  - S2: They should receive 5 mg to 20 mg once daily for those 10 years of age and older.

**L67.0** `Compound Sentence` (0.968) → `decomposed`
- original: Some medicines require a lower rosuvastatin dose, and a few should not be taken with rosuvastatin at all.
  - S1: Some medicines require a lower rosuvastatin dose.
  - S2: A few should not be taken with rosuvastatin at all.

**L67.1** `Incomplete Sentence` (0.884) → `excluded_incomplete`
- original: See the detailed dosage information for the full list.

## What other drugs will affect rosuvastatin?

**L70.0** `Incomplete Sentence` (0.896) → `excluded_incomplete`
- original: Tell your doctor about all the medicines you take, including prescription and over-the-counter medicines, vitamins, and herbal supplements.

**L70.1** `Incomplete Sentence` (0.451) → `excluded_incomplete`
- original: Also tell the doctor who prescribes rosuvastatin if another doctor increases the dose of another medicine you are taking.

**L70.2** `Compound Sentence` (0.969) → `decomposed`
- original: Rosuvastatin may affect the way other medicines work, and other medicines may affect how rosuvastatin works.
  - S1: Rosuvastatin may affect the way other medicines work.
  - S2: Other medicines may affect how rosuvastatin works.

**L70.3** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Especially tell your doctor if you take:

**L71.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: coumarin anticoagulants (medicines that prevent blood clots, such as warfarin)

**L72.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: antacids (medicines you take for heartburn that contain aluminum and magnesium hydroxide)

**L73.0** `Simple Sentence` (0.988) → `passthrough`
- original: Taking rosuvastatin with certain medicines may increase the risk of muscle problems.

**L73.1** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Especially tell your doctor if you take:

**L74.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: cyclosporine (a medicine for your immune system)

**L75.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: teriflunomide (a medicine used to treat relapsing remitting multiple sclerosis)

**L76.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: enasidenib (a medicine used to treat acute myeloid leukemia)

**L77.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: capmatinib (a medicine for the treatment of non-small cell lung cancer)

**L78.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: fostamatinib (a medicine used to treat low platelet counts)

**L79.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: febuxostat (a medicine used to treat and prevent high blood levels of uric acid)

**L80.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: gemfibrozil (a fibric acid medicine for lowering cholesterol)

**L81.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: tafamidis [used to treat cardiomyopathy (enlarged and thickened heart muscle)]

**L82.0** `Incomplete Sentence` (0.937) → `excluded_incomplete`
- original: anti-viral medicines including certain HIV or hepatitis C virus drugs such as: lopinavir, ritonavir, fosamprenavir, tipranavir, atazanavir, simeprevir combination of sofosbuvir/velpatasvir/voxilaprevir dasabuvir/ombitasvir/paritaprevir/ritonavir elbasvir/grazoprevir sofosbuvir/velpatasvir glecaprevir/pibrentasvir and all other combinations with ledipasvir including ledipasvir/sofosbuvir

**L83.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: darolutamide (a medicine for the treatment of prostate cancer)

**L84.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: regorafenib (a medicine used to treat cancer of the colon and rectum)

**L85.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: fibric acid derivatives (such as fenofibrate)

**L86.0** `Incomplete Sentence` (0.945) → `excluded_incomplete`
- original: ticagrelor (helps reduce the chance of blood clot formation that can block a blood vessel)

**L87.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: niacin or nicotinic acid

**L88.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: colchicine (a medicine used to treat gout)

**L89.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: belumosudil (used to treat chronic graft-versus-host disease)

**L90.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: momelotinib (used to treat myelofibrosis, a rare form of blood cancer)

**L91.0** `Incomplete Sentence` (0.853) → `excluded_incomplete`
- original: Ask your doctor or pharmacist for a list of these medicines if you are not sure.

**L91.1** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Know all of the medicines you take.

**L91.2** `Incomplete Sentence` (0.632) → `excluded_incomplete`
- original: Keep a list of them to show your doctor and pharmacist when you get new medicine.

## Pregnancy and breastfeeding

**L94.0** `Incomplete Sentence` (0.771) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or think you may be pregnant, or are planning to become pregnant.

**L94.1** `Simple Sentence` (0.99) → `passthrough`
- original: Rosuvastatin may harm your unborn baby.

**L94.2** `Compound Sentence` (0.353) → `decomposed`
- original: If you become pregnant while taking rosuvastatin, call your doctor right away to discuss your treatment.
  - S1: If you become pregnant while taking rosuvastatin, call your doctor right away.
  - S2: You should discuss your treatment.

**L95.0** `Incomplete Sentence` (0.911) → `excluded_incomplete`
- original: Tell your doctor if you are breastfeeding or plan to breastfeed.

**L95.1** `Simple Sentence` (0.963) → `passthrough`
- original: Medicines like rosuvastatin can pass into your breast milk and may harm your baby.

**L95.2** `Incomplete Sentence` (0.946) → `excluded_incomplete`
- original: Talk to your doctor about the best way to feed your baby if you take this medicine.

**L95.3** `Incomplete Sentence` (0.5) → `excluded_incomplete`
- original: Do not breastfeed while taking rosuvastatin.

## Storage

**L98.0** `Incomplete Sentence` (0.931) → `excluded_incomplete`
- original: Store rosuvastatin at room temperature, between 68°F and 77°F (20°C and 25°C).

**L99.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Store in a dry place.

**L100.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Safely throw away medicine that is out of date or no longer needed.

**L101.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Keep this and all medicines out of the reach of children.

## What are the ingredients in rosuvastatin?

**L104.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Active ingredient: rosuvastatin calcium

**L105.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Inactive ingredients:

**L106.0** `Simple Sentence` (0.583) → `passthrough`
- original: Crestor tablets: microcrystalline cellulose NF, lactose monohydrate NF, tribasic calcium phosphate NF, crospovidone NF, magnesium stearate NF, hypromellose NF, triacetin NF, titanium dioxide USP, yellow ferric oxide, and red ferric oxide NF.

**L107.0** `Simple Sentence` (0.988) → `passthrough`
- original: Generic versions of rosuvastatin tablets may contain different inactive ingredients from those listed above.

**L107.1** `Incomplete Sentence` (0.898) → `excluded_incomplete`
- original: Check the product label for your particular formulation for a complete list of ingredients.

## Company

**L110.0** `Complex Sentence` (0.775) → `decomposed`
- original: The Crestor brand of rosuvastatin tablets is distributed by AstraZeneca Pharmaceuticals LP, Wilmington, DE 19850, under license from Shionogi & Co., LTD., Osaka, Japan.
  - S1: The Crestor brand of rosuvastatin tablets is distributed by AstraZeneca Pharmaceuticals LP.
  - S2: AstraZeneca Pharmaceuticals LP is located in Wilmington, DE 19850.
  - S3: The distribution is under license from Shionogi & Co., LTD.
  - S4: Shionogi & Co., LTD. is located in Osaka, Japan.

**L111.0** `Simple Sentence` (0.957) → `passthrough`
- original: Generic versions are also manufactured by several other companies.

**L112.0** `Simple Sentence` (0.948) → `passthrough`
- original: Ezallor Sprinkle (rosuvastatin) has been discontinued and is no longer available.

## Popular FAQ

**L115.0** `Incomplete Sentence` (0.716) → `excluded_incomplete`
- original: Q: Rosuvastatin or Atorvastatin: What’s the better choice for you?

**L115.1** `Complex Sentence` (0.95) → `decomposed`
- original: A: Rosuvastatin (Crestor) and atorvastatin (Lipitor) are both statins that lower “bad” LDL cholesterol and reduce the risk of heart attack and stroke in people at increased cardiovascular risk.
  - S1: Rosuvastatin (Crestor) and atorvastatin (Lipitor) are both statins.
  - S2: These statins lower "bad" LDL cholesterol.
  - S3: They reduce the risk of heart attack and stroke.
  - S4: This applies to people at increased cardiovascular risk.

**L115.2** `Compound Sentence` (0.659) → `decomposed`
- original: The better choice for you depends on factors such as how much LDL reduction you need, your medical history, and cost and insurance coverage.
  - S1: The better choice for you depends on factors such as how much LDL reduction you need.
  - S2: It depends on your medical history.
  - S3: It depends on cost and insurance coverage.
