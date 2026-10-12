# Meloxicam — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/meloxicam.txt` · 142 sentences · 17 changed by pronoun resolution · 192 sentences sent to EDC

## What is meloxicam?

**L5.0** `Simple Sentence` (0.987) → `passthrough`
- original: Meloxicam is a nonsteroidal anti-inflammatory drug (NSAID).

**L5.1** `Simple Sentence` (0.909) → `passthrough`
- original: It works by reducing hormones that cause pain, fever, and inflammation in the body.
- pronoun resolved: Meloxicam works by reducing hormones that cause pain, fever, and inflammation in the body.
  - edits: “It” → “Meloxicam”

**L6.0** `Complex Sentence` (0.454) → `decomposed`
- original: Meloxicam is used to relieve pain, tenderness, swelling, and stiffness caused by osteoarthritis (arthritis caused by a breakdown of the lining of the joints) and rheumatoid arthritis (arthritis caused by swelling of the lining of the joints).
  - S1: Meloxicam is used to relieve pain, tenderness, swelling, and stiffness.
  - S2: These symptoms are caused by osteoarthritis and rheumatoid arthritis.
  - S3: Osteoarthritis is arthritis caused by a breakdown of the lining of the joints.
  - S4: Rheumatoid arthritis is arthritis caused by swelling of the lining of the joints.

**L7.0** `Complex Sentence` (0.911) → `decomposed`
- original: Meloxicam is also used to relieve the pain, tenderness, swelling, and stiffness caused by juvenile rheumatoid arthritis (a type of arthritis that affects children) in children 2 years of age and older.
  - S1: Meloxicam is used to relieve pain, tenderness, swelling, and stiffness.
  - S2: These symptoms are caused by juvenile rheumatoid arthritis.
  - S3: Juvenile rheumatoid arthritis is a type of arthritis that affects children.
  - S4: Meloxicam is used in children 2 years of age and older.

**L8.0** `Simple Sentence` (0.558) → `passthrough`
- original: IV meloxicam (brands Anjeso [discontinued], Qamzova, Xifyrm) is used for moderate to severe pain in adults, alone or in combination with non-NSAID analgesics.

**L9.0** `Simple Sentence` (0.99) → `passthrough`
- original: Vivlodex capsules [discontinued] are only for use in adults.

**L9.1** `Simple Sentence` (0.759) → `passthrough`
- original: Qmiiz ODT (orally disintegrating tablet) [discontinued] is for adults and children weighing at least 132 pounds (60 kilograms).

**L10.0** `Simple Sentence` (0.975) → `passthrough`
- original: Generic meloxicam is available.

## Warnings

**L13.0** `Complex Sentence` (0.617) → `decomposed`
- original: Meloxicam can increase your risk of a fatal heart attack or stroke, especially if you use it long term or take high doses, or if you have heart disease.
- pronoun resolved: Meloxicam can increase your risk of a fatal heart attack or stroke, especially if you use Meloxicam long term or take high doses, or if you have heart disease.
  - edits: “it” → “Meloxicam”
  - S1: Meloxicam can increase your risk of a fatal heart attack or stroke.
  - S2: This risk is especially high if you use Meloxicam long term.
  - S3: The risk is also higher if you take high doses.
  - S4: The risk is further increased if you have heart disease.

**L13.1** `Simple Sentence` (0.928) → `passthrough`
- original: Even people without heart disease or risk factors could have a stroke or heart attack while taking this medicine.
- pronoun resolved: Even people without heart disease or risk factors could have a stroke or heart attack while taking Meloxicam.
  - edits: “this medicine.” → “Meloxicam.”

**L14.0** `Simple Sentence` (0.704) → `passthrough`
- original: Do not use this medicine just before or after heart bypass surgery (coronary artery bypass graft, or CABG).
- pronoun resolved: Do not use Meloxicam just before or after heart bypass surgery (coronary artery bypass graft, or CABG).
  - edits: “this medicine” → “Meloxicam”

**L15.0** `Incomplete Sentence` (0.965) → `excluded_incomplete`
- original: Avoid taking meloxicam after a recent heart attack, unless your doctor tells you to.

**L15.1** `Simple Sentence` (0.883) → `passthrough`
- original: You may have an increased risk of another heart attack if you take this medicine after a recent heart attack.
- pronoun resolved: You may have an increased risk of another heart attack if you take Meloxicam after a recent heart attack.
  - edits: “this medicine” → “Meloxicam”

**L16.0** `Incomplete Sentence` (0.703) → `excluded_incomplete`
- original: Get emergency medical help if you have chest pain, weakness, shortness of breath, slurred speech, or problems with vision or balance.

**L17.0** `Compound Sentence` (0.622) → `decomposed`
- original: Meloxicam may also cause stomach or intestinal bleeding, which can be fatal.
  - S1: Meloxicam may also cause stomach or intestinal bleeding.
  - S2: This bleeding can be fatal.

**L17.1** `Simple Sentence` (0.952) → `passthrough`
- original: These conditions can occur without warning while you are using this medicine, especially in older adults.
- pronoun resolved: These conditions can occur without warning while you are using Meloxicam, especially in older adults.
  - edits: “this medicine,” → “Meloxicam,”

**L18.0** `Compound Sentence` (0.294) → `decomposed`
- original: Call your doctor at once if you have symptoms of stomach bleeding, such as black, bloody, or tarry stools, or coughing up blood or vomit that looks like coffee grounds.
  - S1: Call your doctor at once if you have symptoms of stomach bleeding.
  - S2: Such symptoms include black, bloody, or tarry stools.
  - S3: Such symptoms also include coughing up blood or vomit that looks like coffee grounds.

**L19.0** `Incomplete Sentence` (0.824) → `excluded_incomplete`
- original: Avoid smoking and drinking alcohol, as they also increase your risk of stomach bleeding.
- pronoun resolved: Avoid smoking and drinking alcohol, as smoking and drinking alcohol also increase your risk of stomach bleeding.
  - edits: “they” → “smoking and drinking alcohol”

## Before taking this medicine

**L22.0** `Simple Sentence` (0.987) → `passthrough`
- original: Meloxicam can increase your risk of a fatal heart attack or stroke.

**L22.1** `Simple Sentence` (0.704) → `passthrough`
- original: Do not use this medicine just before or after heart bypass surgery (coronary artery bypass graft, or CABG).
- pronoun resolved: Do not use Meloxicam just before or after heart bypass surgery (coronary artery bypass graft, or CABG).
  - edits: “this medicine” → “Meloxicam”

**L22.2** `Compound Sentence` (0.622) → `decomposed`
- original: Meloxicam may also cause stomach or intestinal bleeding, which can be fatal.
  - S1: Meloxicam may also cause stomach or intestinal bleeding.
  - S2: This bleeding can be fatal.

**L23.0** `Compound Sentence` (0.622) → `decomposed`
- original: Meloxicam may also cause stomach or intestinal bleeding, which can be fatal.
  - S1: Meloxicam may also cause stomach or intestinal bleeding.
  - S2: This bleeding can be fatal.

**L23.1** `Simple Sentence` (0.952) → `passthrough`
- original: These conditions can occur without warning while you are using this medicine, especially in older adults.
- pronoun resolved: These conditions can occur without warning while you are using Meloxicam, especially in older adults.
  - edits: “this medicine,” → “Meloxicam,”

**L24.0** `Compound Sentence` (0.874) → `decomposed`
- original: You should not use meloxicam if you are allergic to it, or if you have ever had an asthma attack or severe allergic reaction after taking aspirin or an NSAID.
  - S1: You should not use meloxicam if you are allergic to it.
  - S2: You should not use meloxicam if you have ever had an asthma attack or severe allergic reaction after taking aspirin or an NSAID.

**L25.0** `Simple Sentence` (0.838) → `passthrough`
- original: To make sure meloxicam is safe for you, tell your doctor if you have ever had:

**L26.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: heart disease, high blood pressure, high cholesterol, diabetes, or if you smoke;

**L27.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a heart attack, stroke, or blood clot;

**L28.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: ulcers or stomach bleeding;

**L29.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: asthma;

**L30.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: kidney disease (or if you are on dialysis);

**L31.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: liver disease; or

**L32.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: fluid retention

**L33.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: are pregnant or planning a pregnancy

**L34.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: are breastfeeding or intending to breastfeed.

**L35.0** `Simple Sentence` (0.989) → `passthrough`
- original: Meloxicam is not approved for use by anyone younger than 2 years old.

**L36.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Pregnancy:

**L37.0** `Simple Sentence` (0.915) → `passthrough`
- original: If you are pregnant, you should not take meloxicam unless your doctor tells you to.

**L37.1** `Simple Sentence` (0.988) → `passthrough`
- original: Taking an NSAID at about 20 weeks of pregnancy or later may harm your unborn baby.

**L37.2** `Complex Sentence` (0.941) → `decomposed`
- original: If you need to take this medicine for more than 2 days when you are between 20 and 30 weeks of pregnancy, your doctor may need to monitor the amount of fluid around your baby.
- pronoun resolved: If you need to take Meloxicam for more than 2 days when you are between 20 and 30 weeks of pregnancy, your doctor may need to monitor the amount of fluid around your baby.
  - edits: “this medicine” → “Meloxicam”
  - S1: If you need to take Meloxicam for more than 2 days when you are between 20 and 30 weeks of pregnancy.
  - S2: Your doctor may need to monitor the amount of fluid around your baby.

**L37.3** `Simple Sentence` (0.989) → `passthrough`
- original: You should not take meloxicam after about 30 weeks of pregnancy.

**L38.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Planning a pregnancy:

**L39.0** `Simple Sentence` (0.789) → `passthrough`
- original: Meloxicam may cause a delay in ovulation (the release of an egg from an ovary).

**L39.1** `Simple Sentence` (0.916) → `passthrough`
- original: You should not take this medicine if you are undergoing fertility treatment or are otherwise trying to get pregnant.
- pronoun resolved: You should not take Meloxicam if you are undergoing fertility treatment or are otherwise trying to get pregnant.
  - edits: “this medicine” → “Meloxicam”

**L40.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Breastfeeding:

**L41.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Ask a doctor if it is safe to breastfeed while using this medicine.
- pronoun resolved: Ask a doctor if it is safe to breastfeed while using Meloxicam.
  - edits: “this medicine.” → “Meloxicam.”

## How is meloxicam given?

**L44.0** `Incomplete Sentence` (0.974) → `excluded_incomplete`
- original: Take Meloxicam exactly as prescribed by your doctor.

**L44.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L44.2** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: Use the lowest effective dose for your condition.

**L45.0** `Simple Sentence` (0.989) → `passthrough`
- original: Meloxicam oral is taken by mouth.

**L46.0** `Simple Sentence` (0.982) → `passthrough`
- original: Meloxicam injection (Qamzova, Xifyrm) is given as an intravenous bolus injection over 15 seconds.

**L46.1** `Simple Sentence` (0.981) → `passthrough`
- original: A healthcare provider will give you this injection.

**L47.0** `Simple Sentence` (0.542) → `passthrough`
- original: Your dose needs may change if you switch to a different brand, strength, or form of meloxicam.

**L47.1** `Incomplete Sentence` (0.936) → `excluded_incomplete`
- original: Avoid medication errors by using only the medicine your doctor prescribes.

**L48.0** `Simple Sentence` (0.985) → `passthrough`
- original: Meloxicam doses are based on weight (especially in children and teenagers).

**L48.1** `Simple Sentence` (0.983) → `passthrough`
- original: Your dose needs may change if you gain or lose weight.

**L49.0** `Simple Sentence` (0.876) → `passthrough`
- original: If you use this medicine long-term, you may need frequent medical tests.

**L50.0** `Incomplete Sentence` (0.912) → `excluded_incomplete`
- original: Store oral suspension, tablets, or capsules at room temperature, away from moisture and heat.

**L50.1** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Keep the bottle tightly closed when not in use.

## Dosing Information

**L53.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose of Meloxicam for Osteoarthritis:

**L54.0** `Compound-Complex Sentence` (0.622) → `decomposed`
- original: Oral Tablets and Oral Disintegrating Tablets: -Initial dose: 7.5 mg orally once a day -Maintenance dose: 15 mg orally once a day in patients requiring additional analgesia -Maximum dose: 15 mg orally once a day Oral Capsules: -Initial dose: 5 mg orally once a day -Maintenance dose: 10 mg orally once a day in patients requiring additional analgesia -Maximum dose: 10 mg orally once a day.
  - S1: Oral tablets are available.
  - S2: Oral disintegrating tablets are available.
  - S3: The initial dose of oral tablets is 7.5 mg orally once a day.
  - S4: The maintenance dose of oral tablets is 15 mg orally once a day in patients requiring additional analgesia.
  - S5: The maximum dose of oral tablets is 15 mg orally once a day.
  - S6: The initial dose of oral capsules is 5 mg orally once a day.
  - S7: The maintenance dose of oral capsules is 10 mg orally once a day in patients requiring additional analgesia.
  - S8: The maximum dose of oral capsules is 10 mg orally once a day.

**L55.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Use: For the relief of signs and symptoms of osteoarthritis pain

**L56.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose of Meloxicam for Rheumatoid Arthritis:

**L57.0** `Compound Sentence` (0.622) → `decomposed`
- original: Oral Tablets and Oral Disintegrating Tablets: -Initial dose: 7.5 mg orally once a day -Maintenance dose: 15 mg orally once a day in patients requiring additional analgesia -Maximum dose: 15 mg orally once a day.
  - S1: Oral Tablets and Oral Disintegrating Tablets have an initial dose of 7.5 mg orally once a day.
  - S2: The maintenance dose is 15 mg orally once a day in patients requiring additional analgesia.
  - S3: The maximum dose is 15 mg orally once a day.

**L58.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Use: For the relief of signs and symptoms of rheumatoid arthritis

**L59.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Adult Dose of Meloxicam IV for Pain:

**L60.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: 30 mg IV bolus (over 15 seconds) once a day.

**L61.0** `Simple Sentence` (0.975) → `passthrough`
- original: The median time to meaningful pain relief was 2 to 3 hours in clinical trials.

**L62.0** `Simple Sentence` (0.968) → `passthrough`
- original: A non-NSAID with a rapid onset may be used in combination with IV meloxicam.

**L63.0** `Simple Sentence` (0.98) → `passthrough`
- original: Some patients may not experience adequate analgesia for the first 24 hours.

**L64.0** `Simple Sentence` (0.933) → `passthrough`
- original: The lowest effective dose for the shortest duration possible consistent with individual treatment goals should be used.

**L65.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Usual Pediatric Dose of Meloxicam for Juvenile Rheumatoid Arthritis:

**L66.0** `Incomplete Sentence` (0.718) → `excluded_incomplete`
- original: Oral disintegrating tablets in children 60 kg or greater: 7.5 mg orally once a day.

**L67.0** `Incomplete Sentence` (0.494) → `excluded_incomplete`
- original: Oral suspension in children 2 years and older: 0.125 mg/kg orally once a day (to a maximum dose of 7.5 mg/day).

**L68.0** `Simple Sentence` (0.833) → `passthrough`
- original: No additional benefit has been demonstrated with doses above 7.5 mg/day.

**L68.1** `Compound Sentence` (0.815) → `decomposed`
- original: Oral formulations have not shown equivalent systemic exposure and are not considered interchangeable.
  - S1: Oral formulations have not shown equivalent systemic exposure.
  - S2: They are not considered interchangeable.

**L69.0** `Simple Sentence` (0.976) → `passthrough`
- original: The oral disintegrating tablets should not be used in children who weigh less than 60 kg.

## What happens if I miss a dose?

**L72.0** `Compound Sentence` (0.562) → `decomposed`
- original: Use the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - S1: Use the medicine as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L72.1** `Incomplete Sentence` (0.946) → `excluded_incomplete`
- original: Do not use two doses at one time.

## What happens if I overdose?

**L75.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

## What should I avoid while receiving meloxicam?

**L78.0** `Simple Sentence` (0.99) → `passthrough`
- original: Drinking alcohol may increase your risk of stomach bleeding.

**L79.0** `Incomplete Sentence` (0.936) → `excluded_incomplete`
- original: Avoid taking aspirin while you are taking meloxicam, unless your doctor tells you to.

**L80.0** `Incomplete Sentence` (0.775) → `excluded_incomplete`
- original: Ask a doctor or pharmacist before using other medicines for pain, fever, swelling, or cold/flu symptoms.

**L80.1** `Compound Sentence` (0.476) → `decomposed`
- original: They may contain ingredients similar to meloxicam (such as aspirin, ibuprofen, ketoprofen, or naproxen).
- pronoun resolved: Other medicines may contain ingredients similar to meloxicam (such as aspirin, ibuprofen, ketoprofen, or naproxen).
  - edits: “They” → “Other medicines”
  - S1: Other medicines may contain ingredients similar to meloxicam.
  - S2: These ingredients include aspirin, ibuprofen, ketoprofen, or naproxen.

## Meloxicam side effects

**L83.0** `Compound Sentence` (0.396) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to meloxicam (hives, difficult breathing, swelling in your face or throat) or a severe skin reaction (fever, sore throat, burning eyes, skin pain, red or purple skin rash with blistering and peeling).
  - S1: Get emergency medical help if you have signs of an allergic reaction to meloxicam.
  - S2: Signs of an allergic reaction to meloxicam include hives, difficult breathing, and swelling in your face or throat.
  - S3: Get emergency medical help if you have a severe skin reaction.
  - S4: Signs of a severe skin reaction include fever, sore throat, burning eyes, skin pain, and a red or purple skin rash with blistering and peeling.

**L84.0** `Compound Sentence` (0.471) → `decomposed`
- original: Get emergency medical help if you have signs of a heart attack or stroke: chest pain spreading to your jaw or shoulder, sudden numbness or weakness on one side of the body, slurred speech, leg swelling, or feeling short of breath.
  - S1: Get emergency medical help if you have signs of a heart attack or stroke.
  - S2: These signs include chest pain spreading to your jaw or shoulder.
  - S3: These signs include sudden numbness or weakness on one side of the body.
  - S4: These signs include slurred speech.
  - S5: These signs include leg swelling.
  - S6: These signs include feeling short of breath.

**L85.0** `Simple Sentence` (0.99) → `passthrough`
- original: Meloxicam may cause serious side effects.

**L85.1** `Incomplete Sentence` (0.928) → `excluded_incomplete`
- original: Stop using this medicine and call your doctor at once if you have:
- pronoun resolved: Stop using Meloxicam and call your doctor at once if you have:
  - edits: “this medicine” → “Meloxicam”

**L86.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: the first sign of any skin rash, no matter how mild;

**L87.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: shortness of breath (even with mild exertion);

**L88.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: swelling or rapid weight gain;

**L89.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: signs of stomach bleeding - bloody or tarry stools, coughing up blood or vomit that looks like coffee grounds;

**L90.0** `Incomplete Sentence` (0.909) → `excluded_incomplete`
- original: liver problems - nausea, upper stomach pain, itching, tired feeling, flu-like symptoms, loss of appetite, dark urine, clay-colored stools, jaundice (yellowing of the skin or eyes);

**L91.0** `Incomplete Sentence` (0.975) → `excluded_incomplete`
- original: low red blood cells (anemia) - pale skin, unusual tiredness, feeling light-headed, cold hands and feet; or

**L92.0** `Incomplete Sentence` (0.873) → `excluded_incomplete`
- original: kidney problems - little or no urination, swelling in your feet or ankles, feeling tired or short of breath.

**L93.0** `Simple Sentence` (0.954) → `passthrough`
- original: Common meloxicam side effects may include:

**L94.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: stomach pain, nausea, vomiting, heartburn

**L95.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: diarrhea, constipation, gas;

**L96.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: dizziness; or

**L97.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: cold symptoms, flu symptoms.

**L98.0** `Compound Sentence` (0.545) → `decomposed`
- original: This is not a complete list of side effects, and others may occur.
  - S1: This is not a complete list of side effects.
  - S2: Others may occur.

**L98.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L98.2** `Simple Sentence` (0.977) → `passthrough`
- original: You may report side effects tothe FDA at 1-800-FDA-1088.

## What other drugs will affect meloxicam?

**L101.0** `Incomplete Sentence` (0.749) → `excluded_incomplete`
- original: Ask your doctor before using meloxicam if you take an antidepressant.

**L101.1** `Simple Sentence` (0.976) → `passthrough`
- original: Taking certain antidepressants with an NSAID may cause you to bruise or bleed easily.

**L102.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Tell your doctor about all your other medicines, especially:

**L103.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: cyclosporine;

**L104.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: lithium;

**L105.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: methotrexate;

**L106.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: pemetrexed;

**L107.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: sodium polystyrene sulfonate (Kayexalate);

**L108.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: a blood thinner (warfarin, Coumadin, Jantoven);

**L109.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: heart or blood pressure medication, including a diuretic or "water pill"; or

**L110.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: steroid medicine (such as prednisone).

**L111.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L111.1** `Complex Sentence` (0.559) → `decomposed`
- original: Other drugs may interact with meloxicam, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may interact with meloxicam.
  - S2: These drugs include prescription and over-the-counter medicines.
  - S3: These drugs also include vitamins and herbal products.

**L111.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.

## Popular FAQ

**L114.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: Q: Meloxicam vs Ibuprofen: What's the difference?

**L114.1** `Compound Sentence` (0.626) → `decomposed`
- original: A: Meloxicam is stronger, prescription-only, longer-acting, and used mainly for arthritis; ibuprofen is milder, OTC, shorter-acting, and treats various pains.
  - S1: Meloxicam is stronger, prescription-only, longer-acting, and used mainly for arthritis.
  - S2: Ibuprofen is milder, OTC, shorter-acting, and treats various pains.

**L115.0** `Incomplete Sentence` (0.967) → `excluded_incomplete`
- original: Q: Should I take meloxicam tablets at night or in the morning?

**L115.1** `Simple Sentence` (0.985) → `passthrough`
- original: A: Meloxicam can be taken in the morning or at night.

**L115.2** `Simple Sentence` (0.985) → `passthrough`
- original: Oral meloxicam is usually taken once daily, at about the same time each day.

**L115.3** `Compound Sentence` (0.916) → `decomposed`
- original: You can take it with or without food, but food may help with stomach upset.
- pronoun resolved: You can take meloxicam with or without food, but food may help with stomach upset.
  - edits: “it” → “meloxicam”
  - S1: You can take meloxicam with or without food.
  - S2: Food may help with stomach upset.

**L115.4** `Incomplete Sentence` (0.655) → `excluded_incomplete`
- original: Follow your prescribed dose and do not take more than recommended.

**L116.0** `Incomplete Sentence` (0.931) → `excluded_incomplete`
- original: Q: How long does it take for meloxicam to work?

**L116.1** `Compound Sentence` (0.832) → `decomposed`
- original: A: Meloxicam usually starts to ease pain within the first day, but the full benefit for chronic conditions like osteoarthritis can take several days to a couple of weeks.
  - S1: Meloxicam usually starts to ease pain within the first day.
  - S2: The full benefit for chronic conditions like osteoarthritis can take several days to a couple of weeks.

**L116.2** `Compound Sentence` (0.636) → `decomposed`
- original: How quickly you feel relief depends on the dose, the formulation (oral tablet vs intravenous), and whether you are treating short‑term postoperative pain or long‑term arthritis.
  - S1: How quickly you feel relief depends on the dose.
  - S2: It depends on the formulation (oral tablet vs intravenous).
  - S3: It depends on whether you are treating short‑term postoperative pain or long‑term arthritis.

**L117.0** `Incomplete Sentence` (0.959) → `excluded_incomplete`
- original: Q: How much meloxicam can I give my dog?

**L117.1** `Simple Sentence` (0.49) → `passthrough`
- original: A: The amount of meloxicam you can give your dog will depend on your dog’s weight and veterinarian’s instructions.

**L117.2** `Compound Sentence` (0.822) → `decomposed`
- original: The typical dose is 0.09 mg/lb (0.2 mg/kg) on day 1 given by mouth or mixed with food, then 0.045 mg/lb (0.1 mg/kg) once a day.
  - S1: The typical dose is 0.09 mg/lb (0.2 mg/kg) on day 1.
  - S2: It is given by mouth or mixed with food.
  - S3: Then the dose is 0.045 mg/lb (0.1 mg/kg) once a day.

**L118.0** `Simple Sentence` (0.803) → `passthrough`
- original: Q: How long do I wait after taking ibuprofen to take meloxicam?

**L118.1** `Complex Sentence` (0.765) → `decomposed`
- original: A: If you are switching from ibuprofen to meloxicam, wait until the ibuprofen has worn off before taking your first dose of meloxicam.
  - S1: Wait until the ibuprofen has worn off before taking your first dose of meloxicam.
  - S2: This applies if you are switching from ibuprofen to meloxicam.

**L118.2** `Simple Sentence` (0.869) → `passthrough`
- original: For most people, that’s about 6 hours after the last dose of ibuprofen.

**L119.0** `Incomplete Sentence` (0.888) → `excluded_incomplete`
- original: Q: Is meloxicam very similar to Celebrex?

**L119.1** `Compound Sentence` (0.963) → `decomposed`
- original: A: Both meloxicam and Celebrex are prescription NSAIDs that treat arthritis pain and swelling, and for most people they work about the same.
- pronoun resolved: A: Both meloxicam and Celebrex are prescription NSAIDs that treat arthritis pain and swelling, and for most people meloxicam work about the same.
  - edits: “they” → “meloxicam”
  - S1: Both meloxicam and Celebrex are prescription NSAIDs that treat arthritis pain and swelling.
  - S2: For most people, meloxicam works about the same.

**L119.2** `Compound Sentence` (0.944) → `decomposed`
- original: Celebrex is a more “stomach‑friendly” COX‑2 selective drug while meloxicam usually costs less and lasts longer in the body.
  - S1: Celebrex is a more "stomach‑friendly" COX‑2 selective drug.
  - S2: Meloxicam usually costs less and lasts longer in the body.

**L120.0** `Incomplete Sentence` (0.897) → `excluded_incomplete`
- original: Q: Can meloxicam cause drowsiness and headache?

**L120.1** `Simple Sentence` (0.957) → `passthrough`
- original: A: Drowsiness isn’t a known side effect of meloxicam.

**L120.2** `Simple Sentence` (0.95) → `passthrough`
- original: In fact, some people may have trouble sleeping instead.

**L120.3** `Compound Sentence` (0.965) → `decomposed`
- original: Dizziness can occur, and headache is a fairly common but usually mild side effect.
  - S1: Dizziness can occur.
  - S2: Headache is a fairly common but usually mild side effect.

**L121.0** `Incomplete Sentence` (0.975) → `excluded_incomplete`
- original: Q: Is meloxicam a narcotic?

**L121.1** `Simple Sentence` (0.74) → `passthrough`
- original: A: No, meloxicam is not a narcotic.

**L121.2** `Simple Sentence` (0.989) → `passthrough`
- original: It is in a group of drugs called nonsteroidal anti-inflammatory drugs (NSAIDs).
- pronoun resolved: Meloxicam is in a group of drugs called nonsteroidal anti-inflammatory drugs (NSAIDs).
  - edits: “It” → “Meloxicam”
