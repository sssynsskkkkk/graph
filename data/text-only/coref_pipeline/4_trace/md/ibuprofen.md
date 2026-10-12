# Ibuprofen — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/ibuprofen.txt` · 113 sentences · 13 changed by pronoun resolution · 168 sentences sent to EDC

## What is ibuprofen?

**L5.0** `Simple Sentence` (0.989) → `passthrough`
- original: Ibuprofen is a nonsteroidal anti-inflammatory drug (NSAID).

**L5.1** `Simple Sentence` (0.968) → `passthrough`
- original: It works by reducing hormones that cause inflammation and pain in the body.
- pronoun resolved: Ibuprofen works by reducing hormones that cause inflammation and pain in the body.
  - edits: “It” → “Ibuprofen”

**L6.0** `Complex Sentence` (0.736) → `decomposed`
- original: Ibuprofen is used to reduce fever and treat pain or inflammation caused by many conditions such as headache, toothache, back pain, arthritis, menstrual cramps, or minor injury.
  - S1: Ibuprofen is used to reduce fever.
  - S2: Ibuprofen is used to treat pain or inflammation.
  - S3: The pain or inflammation is caused by many conditions.
  - S4: These conditions include headache, toothache, back pain, arthritis, menstrual cramps, or minor injury.

**L7.0** `Simple Sentence` (0.99) → `passthrough`
- original: Ibuprofen is used in adults and children.

**L7.1** `Simple Sentence` (0.972) → `passthrough`
- original: Some formulations are also used in premature babies to close a certain heart defect.

## Warnings

**L10.0** `Simple Sentence` (0.971) → `passthrough`
- original: Ibuprofen can increase your risk of fatal heart attack, heart failure, or stroke.

**L10.1** `Simple Sentence` (0.639) → `passthrough`
- original: Do not use this medicine just before or after heart bypass surgery (coronary artery bypass graft, or CABG).
- pronoun resolved: Do not use Ibuprofen just before or after heart bypass surgery (coronary artery bypass graft, or CABG).
  - edits: “this medicine” → “Ibuprofen”

**L10.2** `Incomplete Sentence` (0.974) → `excluded_incomplete`
- original: Avoid taking ibuprofen after a recent heart attack, unless your doctor tells you to.

**L11.0** `Compound Sentence` (0.674) → `decomposed`
- original: Ibuprofen may also cause stomach or intestinal bleeding, which can be fatal.
  - S1: Ibuprofen may also cause stomach or intestinal bleeding.
  - S2: This bleeding can be fatal.

**L11.1** `Simple Sentence` (0.792) → `passthrough`
- original: These conditions can occur without warning while you are using this medicine, especially in older adults.
- pronoun resolved: These conditions can occur without warning while you are using Ibuprofen, especially in older adults.
  - edits: “this medicine,” → “Ibuprofen,”

**L12.0** `Incomplete Sentence` (0.893) → `excluded_incomplete`
- original: Do not take more than your recommended dose.

**L12.1** `Simple Sentence` (0.99) → `passthrough`
- original: An ibuprofen overdose can damage your stomach or intestines.

**L12.2** `Incomplete Sentence` (0.921) → `excluded_incomplete`
- original: Use only the smallest amount of medication needed to get relief from your pain, swelling, or fever.

## Before taking this medicine

**L15.0** `Compound Sentence` (0.887) → `decomposed`
- original: You should not use ibuprofen if you are allergic to it, or if you have ever had an asthma attack or severe allergic reaction after taking aspirin or an NSAID.
- pronoun resolved: You should not use ibuprofen if you are allergic to ibuprofen, or if you have ever had an asthma attack or severe allergic reaction after taking aspirin or an NSAID.
  - edits: “it,” → “ibuprofen,”
  - S1: You should not use ibuprofen if you are allergic to ibuprofen.
  - S2: You should not use ibuprofen if you have ever had an asthma attack or severe allergic reaction after taking aspirin or an NSAID.

**L16.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Ask a doctor or pharmacist if this medicine is safe to use if you have ever had:

**L17.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: heart disease, high blood pressure, high cholesterol, diabetes, or if you smoke;

**L18.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a heart attack, stroke, or blood clot;

**L19.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: stomach ulcers or bleeding;

**L20.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: liver or kidney disease;

**L21.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: asthma; or

**L22.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: if you take aspirin to prevent heart attack or stroke.

**L23.0** `Incomplete Sentence` (0.49) → `excluded_incomplete`
- original: Ask a doctor before using this medicine if you are pregnant or breastfeeding.

**L24.0** `Simple Sentence` (0.847) → `passthrough`
- original: If you are pregnant, you should not take ibuprofen unless your doctor tells you to.

**L24.1** `Simple Sentence` (0.753) → `passthrough`
- original: Taking an NSAID at 20 weeks or later in pregnancy can cause serious heart or kidney problems in the unborn baby and possible complications with your pregnancy.

**L24.2** `Incomplete Sentence` (0.635) → `excluded_incomplete`
- original: Do not take ibuprofen after 30 weeks of pregnancy.

**L25.0** `Complex Sentence` (0.842) → `decomposed`
- original: Ibuprofen may cause a temporary delay in ovulation, which can make it harder to get pregnant.
  - S1: Ibuprofen may cause a temporary delay in ovulation.
  - S2: This delay can make it harder to get pregnant.

**L25.1** `Incomplete Sentence` (0.914) → `excluded_incomplete`
- original: Tell your doctor if you are having trouble getting pregnant.

**L26.0** `Incomplete Sentence` (0.697) → `excluded_incomplete`
- original: Do not give ibuprofen to a child younger than 6 months old without the advice of a doctor.

## How should I take ibuprofen?

**L29.0** `Incomplete Sentence` (0.945) → `excluded_incomplete`
- original: Use ibuprofen exactly as directed on the label, or as prescribed by your doctor.

**L29.1** `Incomplete Sentence` (0.948) → `excluded_incomplete`
- original: Use the lowest dose that is effective in treating your condition.

**L30.0** `Simple Sentence` (0.99) → `passthrough`
- original: An ibuprofen overdose can damage your stomach or intestines.

**L30.1** `Simple Sentence` (0.838) → `passthrough`
- original: The maximum amount of ibuprofen for adults is 800 milligrams per dose or 3200 mg per day (4 maximum doses).

**L31.0** `Simple Sentence` (0.956) → `passthrough`
- original: A child's dose is based on the age and weight of the child.

**L31.1** `Incomplete Sentence` (0.801) → `excluded_incomplete`
- original: Carefully follow the dosing instructions provided with children's ibuprofen for the age and weight of your child.

**L31.2** `Incomplete Sentence` (0.921) → `excluded_incomplete`
- original: Ask a doctor or pharmacist if you have questions.

**L32.0** `Incomplete Sentence` (0.9) → `excluded_incomplete`
- original: Take ibuprofen with food or milk to lessen stomach upset.

**L33.0** `Incomplete Sentence` (0.968) → `excluded_incomplete`
- original: Shake the oral suspension (liquid) before you measure a dose.

**L33.1** `Incomplete Sentence` (0.955) → `excluded_incomplete`
- original: Use the dosing syringe provided, or use a medicine dose-measuring device (not a kitchen spoon).

**L34.0** `Simple Sentence` (0.983) → `passthrough`
- original: You must chew the chewable tablet before you swallow it.
- pronoun resolved: You must chew the chewable tablet before you swallow chewable tablet.
  - edits: “it.” → “chewable tablet.”

**L35.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Store at room temperature away from moisture and heat.

**L35.1** `Incomplete Sentence` (0.94) → `excluded_incomplete`
- original: Do not allow the liquid medicine to freeze.

## What happens if I miss a dose?

**L38.0** `Complex Sentence` (0.489) → `decomposed`
- original: Since ibuprofen is used when needed, you may not be on a dosing schedule.
  - S1: Ibuprofen is used when needed.
  - S2: You may not be on a dosing schedule.

**L38.1** `Incomplete Sentence` (0.868) → `excluded_incomplete`
- original: Skip any missed dose if it's almost time for your next dose.

**L38.2** `Incomplete Sentence` (0.946) → `excluded_incomplete`
- original: Do not use two doses at one time.

## What happens if I overdose?

**L41.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L41.1** `Compound Sentence` (0.577) → `decomposed`
- original: Overdose symptoms may include nausea, vomiting, stomach pain, drowsiness, black or bloody stools, coughing up blood, shallow breathing, fainting, or coma.
  - S1: Overdose symptoms may include nausea, vomiting, stomach pain, drowsiness, black or bloody stools, coughing up blood, shallow breathing, fainting, or coma.

## What to avoid

**L44.0** `Incomplete Sentence` (0.775) → `excluded_incomplete`
- original: Ask a doctor or pharmacist before using other medicines for pain, fever, swelling, or cold/flu symptoms.

**L44.1** `Compound Sentence` (0.472) → `decomposed`
- original: They may contain ingredients similar to ibuprofen (such as aspirin, ketoprofen, or naproxen).
- pronoun resolved: Other medicines may contain ingredients similar to ibuprofen (such as aspirin, ketoprofen, or naproxen).
  - edits: “They” → “Other medicines”
  - S1: Other medicines may contain ingredients similar to ibuprofen.
  - S2: These ingredients include aspirin, ketoprofen, or naproxen.

**L45.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Avoid taking aspirin unless your doctor tells you to.

**L46.0** `Complex Sentence` (0.956) → `decomposed`
- original: If you also take aspirin to prevent stroke or heart attack, taking ibuprofen can make aspirin less effective in protecting your heart and blood vessels.
  - S1: If you also take aspirin to prevent stroke or heart attack.
  - S2: Taking ibuprofen can make aspirin less effective.
  - S3: Aspirin protects your heart and blood vessels.

**L46.1** `Complex Sentence` (0.473) → `decomposed`
- original: If you take both medicines, take ibuprofen at least 8 hours before or 30 minutes after you take aspirin (non-enteric coated form).
  - S1: If you take both medicines, take ibuprofen at least 8 hours before or 30 minutes after you take aspirin.
  - S2: The aspirin is the non-enteric coated form.

**L47.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Avoid drinking alcohol.

**L47.1** `Simple Sentence` (0.989) → `passthrough`
- original: It may increase your risk of stomach bleeding.
- pronoun resolved: Alcohol may increase your risk of stomach bleeding.
  - edits: “It” → “Alcohol”

## Ibuprofen side effects

**L50.0** `Compound Sentence` (0.38) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to ibuprofen (hives, difficult breathing, swelling in your face or throat) or a severe skin reaction (fever, sore throat, burning eyes, skin pain, red or purple skin rash with blistering and peeling).
  - S1: Get emergency medical help if you have signs of an allergic reaction to ibuprofen.
  - S2: Signs of an allergic reaction to ibuprofen include hives, difficult breathing, and swelling in your face or throat.
  - S3: Get emergency medical help if you have a severe skin reaction.
  - S4: Signs of a severe skin reaction include fever, sore throat, burning eyes, skin pain, and a red or purple skin rash with blistering and peeling.

**L51.0** `Compound Sentence` (0.521) → `decomposed`
- original: Get emergency medical help if you have signs of a heart attack or stroke: chest pain spreading to your jaw or shoulder, sudden numbness or weakness on one side of the body, slurred speech, leg swelling, feeling short of breath.
  - S1: Get emergency medical help if you have signs of a heart attack or stroke.
  - S2: These signs include chest pain spreading to your jaw or shoulder.
  - S3: These signs include sudden numbness or weakness on one side of the body.
  - S4: These signs include slurred speech.
  - S5: These signs include leg swelling.
  - S6: These signs include feeling short of breath.

**L52.0** `Incomplete Sentence` (0.954) → `excluded_incomplete`
- original: Stop using this medicine and call your doctor at once if you have:
- pronoun resolved: Stop using Ibuprofen and call your doctor at once if you have:
  - edits: “this medicine” → “Ibuprofen”

**L53.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: changes in your vision;

**L54.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: shortness of breath (even with mild exertion);

**L55.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: swelling or rapid weight gain;

**L56.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a skin rash, no matter how mild;

**L57.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: signs of stomach bleeding - bloody or tarry stools, coughing up blood or vomit that looks like coffee grounds;

**L58.0** `Incomplete Sentence` (0.909) → `excluded_incomplete`
- original: liver problems - nausea, upper stomach pain, itching, tired feeling, flu-like symptoms, loss of appetite, dark urine, clay-colored stools, jaundice (yellowing of the skin or eyes);

**L59.0** `Incomplete Sentence` (0.957) → `excluded_incomplete`
- original: low red blood cells (anemia) - pale skin, feeling light-headed or short of breath, rapid heart rate, trouble concentrating; or

**L60.0** `Incomplete Sentence` (0.461) → `excluded_incomplete`
- original: kidney problems - little or no urinating, painful or difficult urination, swelling in your feet or ankles, feeling tired or short of breath.

**L61.0** `Simple Sentence` (0.94) → `passthrough`
- original: Common ibuprofen side effects may include:

**L62.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: nausea, vomiting, gas;

**L63.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: bleeding; or

**L64.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: dizziness, headache.

**L65.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L65.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L65.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## What other drugs will affect ibuprofen?

**L68.0** `Incomplete Sentence` (0.832) → `excluded_incomplete`
- original: Ask your doctor before using ibuprofen if you take an antidepressant.

**L68.1** `Simple Sentence` (0.976) → `passthrough`
- original: Taking certain antidepressants with an NSAID may cause you to bruise or bleed easily.

**L69.0** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: Ask a doctor or pharmacist before using ibuprofen with any other medications, especially:

**L70.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: cyclosporine;

**L71.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: lithium;

**L72.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: methotrexate;

**L73.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: a blood thinner (warfarin, Coumadin, Jantoven);

**L74.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: heart or blood pressure medication, including a diuretic or "water pill"; or

**L75.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: steroid medicine (such as prednisone)

**L76.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: digoxin.

**L77.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L77.1** `Complex Sentence` (0.574) → `decomposed`
- original: Other drugs may interact with ibuprofen, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may interact with ibuprofen.
  - S2: These drugs include prescription and over-the-counter medicines.
  - S3: These drugs also include vitamins and herbal products.

**L77.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.

## Popular FAQ

**L80.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: Q: Meloxicam vs Ibuprofen: What's the difference?

**L80.1** `Compound Sentence` (0.626) → `decomposed`
- original: A: Meloxicam is stronger, prescription-only, longer-acting, and used mainly for arthritis; ibuprofen is milder, OTC, shorter-acting, and treats various pains.
  - S1: Meloxicam is stronger, prescription-only, longer-acting, and used mainly for arthritis.
  - S2: Ibuprofen is milder, OTC, shorter-acting, and treats various pains.

**L81.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: Q: Naproxen vs ibuprofen: What's the difference?

**L81.1** `Compound Sentence` (0.951) → `decomposed`
- original: A: Ibuprofen is short acting, while naproxen is long acting and more likely to cause an upset stomach.
  - S1: Ibuprofen is short acting.
  - S2: Naproxen is long acting.
  - S3: Naproxen is more likely to cause an upset stomach.

**L81.2** `Compound Sentence` (0.955) → `decomposed`
- original: Naproxen also increases the risk of uncontrolled bleeding in people taking blood thinners by 4-fold, and ibuprofen increases the risk 2-fold.
  - S1: Naproxen also increases the risk of uncontrolled bleeding in people taking blood thinners by 4-fold.
  - S2: Ibuprofen increases the risk 2-fold.

**L81.3** `Compound-Complex Sentence` (0.718) → `decomposed`
- original: Naproxen and ibuprofen are both NSAIDs so they are similar in many ways, but there are important differences.
- pronoun resolved: Naproxen and ibuprofen are both NSAIDs so Naproxen and ibuprofen are similar in many ways, but there are important differences.
  - edits: “they” → “Naproxen and ibuprofen”
  - S1: Naproxen and ibuprofen are both NSAIDs.
  - S2: Naproxen and ibuprofen are similar in many ways.
  - S3: There are important differences between Naproxen and ibuprofen.

**L82.0** `Simple Sentence` (0.773) → `passthrough`
- original: Q: Can you take ibuprofen on an empty stomach?

**L82.1** `Compound-Complex Sentence` (0.912) → `decomposed`
- original: A: Despite the common belief that you must take ibuprofen with food, you can safely take low-dose ibuprofen (up to 1200 mg daily in divided doses for 1 to 7 days) on an empty stomach, and this provides faster pain relief than taking ibuprofen with food.
  - S1: There is a common belief that you must take ibuprofen with food.
  - S2: You can safely take low-dose ibuprofen on an empty stomach.
  - S3: The recommended dosage is up to 1200 mg daily in divided doses for 1 to 7 days.
  - S4: Taking low-dose ibuprofen on an empty stomach provides faster pain relief.
  - S5: Taking ibuprofen with food provides slower pain relief.

**L82.2** `Compound Sentence` (0.949) → `decomposed`
- original: Food slows ibuprofen absorption time, although it doesn't affect the total amount absorbed.
- pronoun resolved: Food slows ibuprofen absorption time, although Food doesn't affect the total amount absorbed.
  - edits: “it” → “Food”
  - S1: Food slows ibuprofen absorption time.
  - S2: Food doesn't affect the total amount absorbed.

**L82.3** `Simple Sentence` (0.81) → `passthrough`
- original: There is actually no scientific evidence that taking ibuprofen with food prevents stomach irritation.

**L82.4** `Simple Sentence` (0.903) → `passthrough`
- original: Over-the-counter ibuprofen doses have a low incidence of gastric problems anyway.

**L83.0** `Simple Sentence` (0.55) → `passthrough`
- original: Q: Can you take expired ibuprofen?

**L83.1** `Compound-Complex Sentence` (0.789) → `decomposed`
- original: A: Although taking expired ibuprofen is not recommended by the manufacturer, the actual shelf-life is likely to be longer than that indicated by the expiry date, with FDA testing showing many drugs are active for years beyond their expiry date, although specific data on ibuprofen is not available.
  - S1: Taking expired ibuprofen is not recommended by the manufacturer.
  - S2: The actual shelf-life of ibuprofen is likely to be longer than that indicated by the expiry date.
  - S3: FDA testing shows many drugs are active for years beyond their expiry date.
  - S4: Specific data on ibuprofen is not available.

**L83.2** `Complex Sentence` (0.846) → `decomposed`
- original: Within reason, an ibuprofen tablet that is a few months past its expiry date is probably safe to take.
- pronoun resolved: Within reason, an ibuprofen tablet that is a few months past ibuprofen tablet's expiry date is probably safe to take.
  - edits: “its” → “ibuprofen tablet's”
  - S1: An ibuprofen tablet that is a few months past its expiry date is probably safe to take.
  - S2: This is true within reason.

**L83.3** `Simple Sentence` (0.968) → `passthrough`
- original: Ibuprofen that is years past its expiry date should not be taken.
- pronoun resolved: Ibuprofen that is years past Ibuprofen's expiry date should not be taken.
  - edits: “its” → “Ibuprofen's”

**L84.0** `Simple Sentence` (0.907) → `passthrough`
- original: Q: Can You Take Tramadol with Acetaminophen, Ibuprofen, or Aspirin?

**L84.1** `Compound-Complex Sentence` (0.711) → `decomposed`
- original: A: Yes, for most people, tramadol can be safely combined with acetaminophen, ibuprofen, or aspirin, and doing so can provide better pain relief than either medicine alone.
  - S1: Tramadol can be safely combined with acetaminophen.
  - S2: Tramadol can be safely combined with ibuprofen.
  - S3: Tramadol can be safely combined with aspirin.
  - S4: Combining tramadol with these medicines provides better pain relief.
  - S5: This relief is better than using either medicine alone.

**L84.2** `Simple Sentence` (0.934) → `passthrough`
- original: However, there are important age restrictions and clinical considerations to be aware of.

**L85.0** `Simple Sentence` (0.683) → `passthrough`
- original: Q: What's the difference between aspirin and ibuprofen?

**L85.1** `Complex Sentence` (0.835) → `decomposed`
- original: A: Both aspirin and ibuprofen are popular NSAIDs (nonsteroidal anti-inflammatory drugs) that work by blocking prostaglandin production to reduce pain and inflammation.
  - S1: Aspirin and ibuprofen are popular NSAIDs.
  - S2: NSAIDs are nonsteroidal anti-inflammatory drugs.
  - S3: Aspirin and ibuprofen work by blocking prostaglandin production.
  - S4: Blocking prostaglandin production reduces pain and inflammation.

**L85.2** `Complex Sentence` (0.586) → `decomposed`
- original: However, these over-the-counter pain relievers have important differences in safety, uses, and side effects.
  - S1: However, these over-the-counter pain relievers have important differences.
  - S2: The differences are in safety, uses, and side effects.

**L86.0** `Simple Sentence` (0.69) → `passthrough`
- original: Q: Can you overdose on ibuprofen?

**L86.1** `Compound-Complex Sentence` (0.806) → `decomposed`
- original: A: Despite ibuprofen having a wide safety margin, it is possible to overdose on it, but death from ibuprofen overdose is rare.
- pronoun resolved: A: Despite ibuprofen having a wide safety margin, it is possible to overdose on ibuprofen, but death from ibuprofen overdose is rare.
  - edits: “it,” → “ibuprofen,”
  - S1: Ibuprofen has a wide safety margin.
  - S2: It is possible to overdose on ibuprofen.
  - S3: Death from ibuprofen overdose is rare.

**L86.2** `Complex Sentence` (0.837) → `decomposed`
- original: Children are more susceptible to the effects of ibuprofen and likely to experience an overdosage of ibuprofen if dosages of more than 400mg/kg (in the range of 8000mg for a 20kg child [the equivalent of 40 x 200mg ibuprofen tablets]) are ingested.
  - S1: Children are more susceptible to the effects of ibuprofen.
  - S2: Children are likely to experience an overdosage of ibuprofen if high dosages are ingested.
  - S3: High dosages are defined as more than 400mg/kg.
  - S4: A dosage of 400mg/kg is equivalent to 8000mg for a 20kg child.
  - S5: This amount is equivalent to 40 x 200mg ibuprofen tablets.

**L86.3** `Simple Sentence` (0.86) → `passthrough`
- original: Studies have reported patients ingesting less than 99 mg/kg are unlikely to have symptoms.

**L87.0** `Incomplete Sentence` (0.928) → `excluded_incomplete`
- original: Q: How much ibuprofen can I take and how often?

**L87.1** `Complex Sentence` (0.48) → `decomposed`
- original: A: Adults can safely take ibuprofen 200 mg to 400 mg (one or two tablets) every 4-6 hours as needed for pain relief.
  - S1: Adults can take ibuprofen for pain relief.
  - S2: The dosage is 200 mg to 400 mg.
  - S3: This is equivalent to one or two tablets.
  - S4: The medication can be taken every 4-6 hours.
  - S5: It is safe for adults to take.

**L87.2** `Simple Sentence` (0.844) → `passthrough`
- original: The maximum dose in 24 hours for over-the-counter ibuprofen is 1200 mg (6 tablets of 200 mg each).

**L87.3** `Compound Sentence` (0.955) → `decomposed`
- original: Ibuprofen is also available on a prescription from a doctor and may be prescribed at a higher strength (600 mg or 800 mg every 6 hours) for severe pain.
  - S1: Ibuprofen is also available on a prescription from a doctor.
  - S2: It may be prescribed at a higher strength (600 mg or 800 mg every 6 hours) for severe pain.
