# Simvastatin — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/simvastatin.txt` · 110 sentences · 18 changed by pronoun resolution · 163 sentences sent to EDC

## What is simvastatin?

**L5.0** `Simple Sentence` (0.984) → `passthrough`
- original: Simvastatin belongs to a group of drugs called HMG CoA reductase inhibitors, or "statins."

**L6.0** `Compound Sentence` (0.853) → `decomposed`
- original: Simvastatin is used to lower blood levels of "bad" cholesterol (low-density lipoprotein, or LDL), to increase levels of "good" cholesterol (high-density lipoprotein, or HDL), and to lower triglycerides (a type of fat in the blood).
  - S1: Simvastatin is used to lower blood levels of "bad" cholesterol (low-density lipoprotein, or LDL).
  - S2: It is used to increase levels of "good" cholesterol (high-density lipoprotein, or HDL).
  - S3: It is used to lower triglycerides (a type of fat in the blood).

**L7.0** `Complex Sentence` (0.804) → `decomposed`
- original: Simvastatin is also used to lower the risk of stroke, heart attack, and other heart complications in people with diabetes, coronary heart disease, or other risk factors.
  - S1: Simvastatin is used to lower the risk of stroke, heart attack, and other heart complications.
  - S2: This is done in people with diabetes, coronary heart disease, or other risk factors.

**L8.0** `Simple Sentence` (0.987) → `passthrough`
- original: Simvastatin is used in adults and children who are at least 10 years old.

## Warnings

**L11.0** `Complex Sentence` (0.95) → `decomposed`
- original: In rare cases, simvastatin can cause a condition that results in the breakdown of skeletal muscle tissue, potentially leading to kidney failure.
  - S1: In rare cases, simvastatin can cause a condition.
  - S2: The condition results in the breakdown of skeletal muscle tissue.
  - S3: The condition potentially leads to kidney failure.

**L11.1** `Compound-Complex Sentence` (0.251) → `decomposed`
- original: Call your doctor right away if you have unexplained muscle pain, tenderness, or weakness especially if you also have fever, unusual tiredness, and dark colored urine.
  - S1: Call your doctor right away if you have unexplained muscle pain.
  - S2: Call your doctor right away if you have tenderness.
  - S3: Call your doctor right away if you have weakness.
  - S4: Call your doctor right away if you have a fever.
  - S5: Call your doctor right away if you have unusual tiredness.
  - S6: Call your doctor right away if you have dark colored urine.

**L12.0** `Incomplete Sentence` (0.858) → `excluded_incomplete`
- original: Never take simvastatin in larger amounts, or for longer than recommended by your doctor.

**L12.1** `Incomplete Sentence` (0.925) → `excluded_incomplete`
- original: Follow your doctor's dosing instructions very carefully.

**L12.2** `Simple Sentence` (0.982) → `passthrough`
- original: Taking too much of this medication may cause serious or life-threatening side effects.

**L13.0** `Complex Sentence` (0.748) → `decomposed`
- original: Before taking this medicine, tell your doctor if you have ever had liver or kidney disease, diabetes, a thyroid disorder, a muscle weakness condition (such as myasthenia gravis or ocular myasthenia), if you are of Chinese descent, or if you drink more than 2 alcoholic beverages daily.
  - S1: Before taking this medicine, tell your doctor if you have ever had liver or kidney disease.
  - S2: Tell your doctor if you have diabetes.
  - S3: Tell your doctor if you have a thyroid disorder.
  - S4: Tell your doctor if you have a muscle weakness condition.
  - S5: A muscle weakness condition includes myasthenia gravis or ocular myasthenia.
  - S6: Tell your doctor if you are of Chinese descent.
  - S7: Tell your doctor if you drink more than 2 alcoholic beverages daily.

**L14.0** `Simple Sentence` (0.984) → `passthrough`
- original: Simvastatin can harm an unborn baby or cause birth defects.

**L14.1** `Incomplete Sentence` (0.87) → `excluded_incomplete`
- original: Do not use if you are pregnant or planning to become pregnant.

**L15.0** `Simple Sentence` (0.98) → `passthrough`
- original: Grapefruit and grapefruit juice may interact with simvastatin and lead to potentially dangerous effects.

**L15.1** `Incomplete Sentence` (0.673) → `excluded_incomplete`
- original: Do not consume grapefruit products while taking this medication.

**L16.0** `Simple Sentence` (0.989) → `passthrough`
- original: Some medicines can cause unwanted or dangerous effects when used with simvastatin.

**L16.1** `Complex Sentence` (0.895) → `decomposed`
- original: Your doctor may need to change your treatment plan if you use certain antibiotics or antifungal medicines, heart medication, antiviral medications such as hepatitis C medications, HIV/AIDS medications, or Paxlovid for COVID-19.
  - S1: Your doctor may need to change your treatment plan.
  - S2: This may happen if you use certain antibiotics or antifungal medicines.
  - S3: It may also happen if you use heart medication.
  - S4: It may also happen if you use antiviral medications.
  - S5: Examples of antiviral medications include hepatitis C medications.
  - S6: Examples of antiviral medications include HIV/AIDS medications.
  - S7: Examples of antiviral medications include Paxlovid for COVID-19.

**L17.0** `Simple Sentence` (0.497) → `passthrough`
- original: Stop taking this medication and tell your doctor right away if you become pregnant.

## Before taking this medicine

**L20.0** `Incomplete Sentence` (0.896) → `excluded_incomplete`
- original: You should not take this medicine if you are allergic to simvastatin, or if:
- pronoun resolved: You should not take Simvastatin if you are allergic to simvastatin, or if:
  - edits: “this medicine” → “Simvastatin”

**L21.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: you have active liver disease; or

**L22.0** `Incomplete Sentence` (0.844) → `excluded_incomplete`
- original: you are pregnant or breastfeeding.

**L23.0** `Simple Sentence` (0.928) → `passthrough`
- original: The following drugs can increase your risk of serious muscle problems if you take them together with simvastatin.

**L23.1** `Simple Sentence` (0.987) → `passthrough`
- original: These drugs should not be used while you are taking this medicine:
- pronoun resolved: These drugs should not be used while you are taking Simvastatin:
  - edits: “this medicine:” → “Simvastatin:”

**L24.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: cyclosporine;

**L25.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: danazol;

**L26.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: gemfibrozil;

**L27.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: nefazodone;

**L28.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: an antibiotic - clarithromycin, erythromycin, telithromycin;

**L29.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: antifungal medication - itraconazole, ketoconazole, posaconazole, voriconazole;

**L30.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: hepatitis C medications - boceprevir, telaprevir; or

**L31.0** `Incomplete Sentence` (0.644) → `excluded_incomplete`
- original: HIV/AIDS medication - atazanavir, cobicistat (Stribild, Tybost), darunavir, fosamprenavir, indinavir, nelfinavir, ritonavir, saquinavir, tipranavir.

**L32.0** `Simple Sentence` (0.748) → `passthrough`
- original: Before you start taking simvastatin, tell your doctor if you are already using any of these other medicines:

**L33.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: lomitapide; or

**L34.0** `Incomplete Sentence` (0.976) → `excluded_incomplete`
- original: heart medication - amiodarone, amlodipine, diltiazem, dronedarone, ranolazine, verapamil.

**L35.0** `Simple Sentence` (0.703) → `passthrough`
- original: To make sure simvastatin is safe for you, tell your doctor if you have:

**L36.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: history of liver disease;

**L37.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: history of kidney disease;

**L38.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: diabetes;

**L39.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a thyroid disorder; or

**L40.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: if you drink more than 2 alcoholic beverages daily

**L41.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a muscle weakness condition (such as myasthenia gravis or ocular myasthenia).

**L42.0** `Complex Sentence` (0.793) → `decomposed`
- original: Simvastatin can cause a condition that results in the breakdown of skeletal muscle tissue, potentially leading to kidney failure.
  - S1: Simvastatin can cause a condition.
  - S2: The condition results in the breakdown of skeletal muscle tissue.
  - S3: The condition potentially leads to kidney failure.

**L42.1** `Complex Sentence` (0.615) → `decomposed`
- original: This condition may be more likely to occur in older adults and in people who have kidney disease or poorly controlled hypothyroidism (underactive thyroid).
  - S1: This condition may be more likely to occur in older adults.
  - S2: This condition may be more likely to occur in people who have kidney disease.
  - S3: This condition may be more likely to occur in people who have poorly controlled hypothyroidism.

**L43.0** `Simple Sentence` (0.984) → `passthrough`
- original: This medicine can harm an unborn baby or cause birth defects.
- pronoun resolved: Simvastatin can harm an unborn baby or cause birth defects.
  - edits: “This medicine” → “Simvastatin”

**L43.1** `Simple Sentence` (0.727) → `passthrough`
- original: Do not take simvastatin if you are pregnant.

**L43.2** `Simple Sentence` (0.608) → `passthrough`
- original: Stop taking this medication and tell your doctor right away if you become pregnant.
- pronoun resolved: Stop taking Simvastatin and tell your doctor right away if you become pregnant.
  - edits: “this medication” → “Simvastatin”

**L43.3** `Incomplete Sentence` (0.819) → `excluded_incomplete`
- original: Use effective birth control to avoid pregnancy while you are taking this medicine.
- pronoun resolved: Use effective birth control to avoid pregnancy while you are taking Simvastatin.
  - edits: “this medicine.” → “Simvastatin.”

**L44.0** `Simple Sentence` (0.883) → `passthrough`
- original: Simvastatin may pass into breast milk and could harm a nursing baby.

**L44.1** `Simple Sentence` (0.488) → `passthrough`
- original: Do not breast-feed while you are taking this medicine.
- pronoun resolved: Do not breast-feed while you are taking Simvastatin.
  - edits: “this medicine.” → “Simvastatin.”

## How should I take simvastatin?

**L47.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Take simvastatin exactly as prescribed.

**L47.1** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Follow all directions on your prescription label.

**L47.2** `Incomplete Sentence` (0.968) → `excluded_incomplete`
- original: Never take this medicine in larger amounts, or for longer than prescribed.
- pronoun resolved: Never take simvastatin in larger amounts, or for longer than prescribed.
  - edits: “this medicine” → “simvastatin”

**L47.3** `Simple Sentence` (0.985) → `passthrough`
- original: Taking too much of this medication may cause serious or life-threatening side effects.
- pronoun resolved: Taking too much of simvastatin may cause serious or life-threatening side effects.
  - edits: “this medication” → “simvastatin”

**L48.0** `Simple Sentence` (0.989) → `passthrough`
- original: Simvastatin is usually taken once a day in the evening.

**L48.1** `Simple Sentence` (0.884) → `passthrough`
- original: If you are taking the oral suspension, take it on an empty stomach.
- pronoun resolved: If you are taking the oral suspension, take oral suspension on an empty stomach.
  - edits: “it” → “oral suspension”

**L48.2** `Simple Sentence` (0.957) → `passthrough`
- original: Your doctor may occasionally change your dose to make sure you get the best results.

**L49.0** `Simple Sentence` (0.814) → `passthrough`
- original: If you are taking the oral suspension, shake the bottle well for at least 20 seconds before each use.

**L49.1** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: Measure the medicine with an accurate measuring device, not a regular household spoon.

**L50.0** `Simple Sentence` (0.758) → `passthrough`
- original: While using simvastatin, you may need frequent blood tests at your doctor's office.

**L51.0** `Simple Sentence` (0.907) → `passthrough`
- original: You may need to take simvastatin on a long-term basis for the treatment of high cholesterol.

**L51.1** `Simple Sentence` (0.685) → `passthrough`
- original: You may need to stop using this medicine for a short time if you have surgery or a medical emergency.
- pronoun resolved: You may need to stop using simvastatin for a short time if you have surgery or a medical emergency.
  - edits: “this medicine” → “simvastatin”

**L51.2** `Simple Sentence` (0.513) → `passthrough`
- original: Do not stop taking this medicine unless your doctor tells you to.
- pronoun resolved: Do not stop taking simvastatin unless your doctor tells you to.
  - edits: “this medicine” → “simvastatin”

**L52.0** `Simple Sentence` (0.901) → `passthrough`
- original: Simvastatin is only part of a complete program of treatment that also includes diet, exercise, and weight control.

**L52.1** `Incomplete Sentence` (0.934) → `excluded_incomplete`
- original: Follow your diet, medication, and exercise routines very closely.

**L53.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Store at room temperature away from moisture, heat, and light.

## What happens if I miss a dose?

**L56.0** `Incomplete Sentence` (0.926) → `excluded_incomplete`
- original: Take the missed dose as soon as you remember.

**L56.1** `Incomplete Sentence` (0.89) → `excluded_incomplete`
- original: Skip the missed dose if it is almost time for your next scheduled dose.

**L56.2** `Incomplete Sentence` (0.748) → `excluded_incomplete`
- original: Do not take extra medicine to make up the missed dose.

## What happens if I overdose?

**L59.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

## What to avoid

**L62.0** `Simple Sentence` (0.984) → `passthrough`
- original: Grapefruit and grapefruit juice may interact with simvastatin and lead to unwanted side effects.

**L62.1** `Incomplete Sentence` (0.975) → `excluded_incomplete`
- original: Avoid the use of grapefruit products while taking this medicine.
- pronoun resolved: Avoid the use of grapefruit products while taking Simvastatin.
  - edits: “this medicine.” → “Simvastatin.”

**L63.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Avoid eating foods that are high in fat or cholesterol.

**L63.1** `Simple Sentence` (0.36) → `passthrough`
- original: Simvastatin will not be as effective in lowering your cholesterol if you do not follow a cholesterol-lowering diet plan.

**L64.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Avoid drinking alcohol.

**L64.1** `Simple Sentence` (0.564) → `passthrough`
- original: It can raise triglyceride levels and may increase your risk of liver damage.
- pronoun resolved: Alcohol can raise triglyceride levels and may increase your risk of liver damage.
  - edits: “It” → “Alcohol”

## Simvastatin side effects

**L67.0** `Compound Sentence` (0.397) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to simvastatin (hives, difficult breathing, swelling in your face or throat) or a severe skin reaction (fever, sore throat, burning eyes, skin pain, red or purple skin rash with blistering and peeling).
  - S1: Get emergency medical help if you have signs of an allergic reaction to simvastatin.
  - S2: Signs of an allergic reaction to simvastatin include hives, difficult breathing, and swelling in your face or throat.
  - S3: Get emergency medical help if you have a severe skin reaction.
  - S4: Signs of a severe skin reaction include fever, sore throat, burning eyes, skin pain, and a red or purple skin rash with blistering and peeling.

**L68.0** `Complex Sentence` (0.533) → `decomposed`
- original: Simvastatin can cause the breakdown of muscle tissue, which can lead to kidney failure.
  - S1: Simvastatin can cause the breakdown of muscle tissue.
  - S2: The breakdown of muscle tissue can lead to kidney failure.

**L68.1** `Compound-Complex Sentence` (0.254) → `decomposed`
- original: Call your doctor right away if you have unexplained muscle pain, tenderness, or weakness especially if you also have fever, unusual tiredness, or dark urine.
  - S1: Call your doctor right away if you have unexplained muscle pain.
  - S2: Call your doctor right away if you have tenderness.
  - S3: Call your doctor right away if you have weakness.
  - S4: Call your doctor right away if you have a fever.
  - S5: Call your doctor right away if you have unusual tiredness.
  - S6: Call your doctor right away if you have dark urine.

**L69.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Also call your doctor at once if you have:

**L70.0** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: signs of a kidney problem - little or no urinating; painful or difficult urination; swelling in your feet or ankles; feeling tired or short of breath; or

**L71.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: muscle weakness in your hips, shoulders, neck, and back;

**L72.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: trouble lifting your arms, trouble climbing or standing; or

**L73.0** `Simple Sentence` (0.458) → `passthrough`
- original: liver problems - nausea, upper stomach pain, itching, tired feeling, loss of appetite, dark urine, clay-colored stools, jaundice (yellowing of the skin or eyes).

**L74.0** `Simple Sentence` (0.934) → `passthrough`
- original: Common simvastatin side effects may include:

**L75.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: headache;

**L76.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: constipation, nausea, stomach pain; or

**L77.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: cold symptoms such as stuffy nose, sneezing, sore throat.

**L78.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L78.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L78.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## What other drugs will affect simvastatin?

**L81.0** `Simple Sentence` (0.991) → `passthrough`
- original: Many drugs can interact with simvastatin.

**L81.1** `Simple Sentence` (0.949) → `passthrough`
- original: Not all possible interactions are listed here.

**L81.2** `Incomplete Sentence` (0.97) → `excluded_incomplete`
- original: Tell your doctor about all your medications and any you start or stop using during treatment, especially:

**L82.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: delavirdine;

**L83.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: fenofibrate; or

**L84.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: fluconazole.

**L85.0** `Complex Sentence` (0.895) → `decomposed`
- original: Your doctor may need to change your treatment plan if you use certain antibiotics or antifungal medicines, heart medication, antiviral medications such as hepatitis C medications, HIV/AIDS medications, or Paxlovid for COVID-19.
  - S1: Your doctor may need to change your treatment plan.
  - S2: This may happen if you use certain antibiotics or antifungal medicines.
  - S3: It may also happen if you use heart medication.
  - S4: It may also happen if you use antiviral medications.
  - S5: Examples of antiviral medications include hepatitis C medications.
  - S6: Examples of antiviral medications include HIV/AIDS medications.
  - S7: Examples of antiviral medications include Paxlovid for COVID-19.

**L85.1** `Simple Sentence` (0.729) → `passthrough`
- original: This list is not complete and many other drugs can interact with simvastatin.

**L85.2** `Incomplete Sentence` (0.491) → `excluded_incomplete`
- original: This includes prescription and over-the-counter medicines, vitamins, and herbal products.
- pronoun resolved: List includes prescription and over-the-counter medicines, vitamins, and herbal products.
  - edits: “This” → “List”

**L85.3** `Incomplete Sentence` (0.956) → `excluded_incomplete`
- original: Give a list of all your medicines to any healthcare provider who treats you.

## Popular FAQ

**L88.0** `Incomplete Sentence` (0.706) → `excluded_incomplete`
- original: Q: Do statins cause rhabdomyolysis, and how is it treated?
- pronoun resolved: Q: Do statins cause rhabdomyolysis, and how is rhabdomyolysis treated?
  - edits: “it” → “rhabdomyolysis”

**L88.1** `Simple Sentence` (0.648) → `passthrough`
- original: A: Rhabdomyolysis is a rare but serious side effect of statins, a class of cholesterol-lowering medications.

**L88.2** `Complex Sentence` (0.917) → `decomposed`
- original: It involves the breakdown of muscle tissue, which releases substances into the bloodstream that can cause kidney damage.
- pronoun resolved: Rhabdomyolysis involves the breakdown of muscle tissue, which releases substances into the bloodstream that can cause kidney damage.
  - edits: “It” → “Rhabdomyolysis”
  - S1: Rhabdomyolysis involves the breakdown of muscle tissue.
  - S2: The breakdown releases substances into the bloodstream.
  - S3: These substances can cause kidney damage.

**L88.3** `Complex Sentence` (0.953) → `decomposed`
- original: While statins are generally safe, rhabdomyolysis from statins is uncommon and most likely to occur at high doses or when combined with certain other drugs.
  - S1: Statins are generally safe.
  - S2: Rhabdomyolysis from statins is uncommon.
  - S3: Rhabdomyolysis is most likely to occur at high doses.
  - S4: Rhabdomyolysis is most likely to occur when combined with certain other drugs.

**L89.0** `Incomplete Sentence` (0.7) → `excluded_incomplete`
- original: Q: When is the best time to take simvastatin?

**L89.1** `Simple Sentence` (0.967) → `passthrough`
- original: A: The best time to take simvastatin is in the evening.

**L89.2** `Simple Sentence` (0.927) → `passthrough`
- original: This is because your body makes most of its cholesterol at night when you are not eating.

**L89.3** `Complex Sentence` (0.91) → `decomposed`
- original: One study that measured people’s total cholesterol and low-density lipoproteins found that concentrations of these two lipids were significantly lower when simvastatin was taken in the evening, than when it was taken in the morning.
- pronoun resolved: One study that measured people’s total cholesterol and low-density lipoproteins found that concentrations of these two lipids were significantly lower when simvastatin was taken in the evening, than when simvastatin was taken in the morning.
  - edits: “it” → “simvastatin”
  - S1: One study measured people's total cholesterol and low-density lipoproteins.
  - S2: The study found that concentrations of these two lipids were significantly lower when simvastatin was taken in the evening.
  - S3: The concentrations were higher when simvastatin was taken in the morning.

**L90.0** `Incomplete Sentence` (0.637) → `excluded_incomplete`
- original: Q: Can I drink grapefruit juice with simvastatin?

**L90.1** `Complex Sentence` (0.823) → `decomposed`
- original: A: You should not drink grapefruit juice with simvastatin because it can significantly increase blood levels of simvastatin and increase the risk of side effects such as liver damage and a condition called rhabdomyolysis, which is the excessive breakdown of muscle tissue.
- pronoun resolved: A: You should not drink grapefruit juice with simvastatin because simvastatin can significantly increase blood levels of simvastatin and increase the risk of side effects such as liver damage and a condition called rhabdomyolysis, which is the excessive breakdown of muscle tissue.
  - edits: “it” → “simvastatin”
  - S1: You should not drink grapefruit juice with simvastatin.
  - S2: Simvastatin can significantly increase blood levels of simvastatin.
  - S3: This increases the risk of side effects.
  - S4: Side effects include liver damage.
  - S5: Side effects include a condition called rhabdomyolysis.
  - S6: Rhabdomyolysis is the excessive breakdown of muscle tissue.

**L90.2** `Simple Sentence` (0.98) → `passthrough`
- original: Occasionally, rhabdomyolysis can cause kidney damage and death.
