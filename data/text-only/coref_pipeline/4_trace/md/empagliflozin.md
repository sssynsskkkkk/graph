# Empagliflozin — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/empagliflozin.txt` · 74 sentences · 3 changed by pronoun resolution · 100 sentences sent to EDC

## What is empagliflozin?

**L5.0** `Simple Sentence` (0.858) → `passthrough`
- original: Empagliflozin is used together with diet and exercise to lower blood sugar levels in adults and children at least 10 years old with type 2 diabetes.

**L6.0** `Complex Sentence` (0.862) → `decomposed`
- original: Empagliflozin is also used to lower the risk of death from heart attack, stroke, or heart failure in adults with type 2 diabetes who also have heart disease.
  - S1: Empagliflozin is used to lower the risk of death.
  - S2: The risk of death is from heart attack, stroke, or heart failure.
  - S3: This applies to adults with type 2 diabetes.
  - S4: The adults also have heart disease.

**L7.0** `Complex Sentence` (0.734) → `decomposed`
- original: Empagliflozin is also used in adults to lower the risk of dying or needing to be in a hospital for heart failure when the heart cannot pump blood properly.
  - S1: Empagliflozin is used in adults.
  - S2: It is used to lower the risk of dying or needing hospitalization for heart failure.
  - S3: This applies when the heart cannot pump blood properly.

**L8.0** `Simple Sentence` (0.99) → `passthrough`
- original: Empagliflozin is not for treating type 1 diabetes.

**L9.0** `Simple Sentence` (0.979) → `passthrough`
- original: Empagliflozin may also be used for purposes not listed in this medication guide.

## Empagliflozin side effects

**L12.0** `Simple Sentence` (0.363) → `passthrough`
- original: Get emergency medical help if you have signs of an allergic reaction: hives, difficult breathing, swelling of your face, lips, tongue, or throat.

**L13.0** `Complex Sentence` (0.451) → `decomposed`
- original: Seek medical attention right away if you have signs of a serious genital infection (penis or vagina): burning, itching, odor, discharge, pain, tenderness, redness or swelling of the genital or rectal area, fever, not feeling well.
  - S1: Seek medical attention right away if you have signs of a serious genital infection.
  - S2: The infection may affect the penis or vagina.
  - S3: Signs include burning, itching, odor, discharge, pain, tenderness, redness, or swelling of the genital or rectal area.
  - S4: Other signs include fever and not feeling well.

**L13.1** `Simple Sentence` (0.986) → `passthrough`
- original: These symptoms may get worse quickly.

**L14.0** `Simple Sentence` (0.989) → `passthrough`
- original: Empagliflozin may cause serious side effects.

**L14.1** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L15.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a light-headed feeling, like you might pass out;

**L16.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: low blood sugar -- headache, hunger, weakness, sweating, confusion, irritability, dizziness, fast heart rate, or feeling jittery;

**L17.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: dehydration --dizziness, confusion, feeling very thirsty, less urination;

**L18.0** `Incomplete Sentence` (0.953) → `excluded_incomplete`
- original: ketoacidosis (too much acid in the blood) --nausea, vomiting, stomach pain, confusion, unusual drowsiness, or trouble breathing; or

**L19.0** `Incomplete Sentence` (0.778) → `excluded_incomplete`
- original: signs of a bladder infection --pain or burning when you urinate, blood in your urine, pain in pelvis or back.

**L20.0** `Simple Sentence` (0.96) → `passthrough`
- original: Common side effects of empagliflozin may include:

**L21.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: a bladder infection; or

**L22.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: yeast infection in women (vaginal itching or discharge).

**L23.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L23.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L23.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## Warnings

**L26.0** `Incomplete Sentence` (0.49) → `excluded_incomplete`
- original: Call your doctor at once if you have signs of a serious side effect, such as stomach pain, vomiting, tiredness, or trouble breathing.

**L27.0** `Incomplete Sentence` (0.427) → `excluded_incomplete`
- original: Tell your doctor if you are sick with vomiting or diarrhea, or if you eat or drink less than usual.

**L28.0** `Simple Sentence` (0.991) → `passthrough`
- original: Empagliflozin can cause serious infections around the penis or vagina.

**L28.1** `Compound Sentence` (0.491) → `decomposed`
- original: Get medical help right away if you have burning, itching, odor, discharge, pain, tenderness, redness or swelling of the genital or rectal area, fever, or if you don't feel well.
  - S1: Get medical help right away if you have burning, itching, odor, discharge, pain, tenderness, redness, or swelling of the genital or rectal area.
  - S2: Get medical help right away if you have a fever.
  - S3: Get medical help right away if you don't feel well.

## Before taking this medicine

**L31.0** `Simple Sentence` (0.933) → `passthrough`
- original: You should not use empagliflozin if you are allergic to it, or if you have:
- pronoun resolved: You should not use empagliflozin if you are allergic to empagliflozin, or if you have:
  - edits: “it,” → “empagliflozin,”

**L32.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: severe kidney disease (or if you are on dialysis).

**L33.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Tell your doctor if you have or have ever had:

**L34.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a bladder infection or urination problems;

**L35.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a genital infection (penis or vagina);

**L36.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: problems with your pancreas, including surgery;

**L37.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: alcoholism, or if you currently drink large amounts of alcohol;

**L38.0** `Incomplete Sentence` (0.674) → `excluded_incomplete`
- original: if you are on a low salt diet, you are eating less, or there is a change in your diet;

**L39.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: if you are 65 or older; or

**L40.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: liver or kidney disease.

**L41.0** `Incomplete Sentence` (0.889) → `excluded_incomplete`
- original: Follow your doctor's instructions about using empagliflozin if you are pregnant or you become pregnant.

**L41.1** `Simple Sentence` (0.992) → `passthrough`
- original: Controlling diabetes is very important during pregnancy.

**L42.0** `Simple Sentence` (0.981) → `passthrough`
- original: You should not use empagliflozin during the second or third trimester of pregnancy.

**L43.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Do not breastfeed.

## How should I take empagliflozin?

**L46.0** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L46.1** `Simple Sentence` (0.984) → `passthrough`
- original: Your doctor may occasionally change your dose.

**L46.2** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Use the medicine exactly as directed.

**L47.0** `Incomplete Sentence` (0.918) → `excluded_incomplete`
- original: Take empagliflozin once a day in the morning, with or without food.

**L48.0** `Compound Sentence` (0.953) → `decomposed`
- original: Your blood sugar will need to be checked often, and you may also need to test the level of ketones in your urine.
  - S1: Your blood sugar will need to be checked often.
  - S2: You may also need to test the level of ketones in your urine.

**L48.1** `Simple Sentence` (0.985) → `passthrough`
- original: Empagliflozin can cause life-threatening ketoacidosis (too much acid in the blood).

**L48.2** `Complex Sentence` (0.533) → `decomposed`
- original: Even if your blood sugar is normal, contact your doctor if a urine test shows that you have high ketones in the urine.
  - S1: Contact your doctor if a urine test shows that you have high ketones in the urine.
  - S2: Even if your blood sugar is normal.

**L49.0** `Simple Sentence` (0.866) → `passthrough`
- original: Blood sugar can be affected by stress, illness, surgery, exercise, alcohol use, or skipping meals.

**L50.0** `Simple Sentence` (0.874) → `passthrough`
- original: Low blood sugar (hypoglycemia) can make you feel very hungry, dizzy, irritable, or shaky.

**L50.1** `Simple Sentence` (0.942) → `passthrough`
- original: To quickly treat hypoglycemia, eat or drink hard candy, crackers, raisins, fruit juice, or non-diet soda.

**L50.2** `Simple Sentence` (0.981) → `passthrough`
- original: Your doctor may prescribe glucagon injection in case of severe hypoglycemia.

**L51.0** `Simple Sentence` (0.986) → `passthrough`
- original: You may get dehydrated during prolonged illness.

**L51.1** `Incomplete Sentence` (0.896) → `excluded_incomplete`
- original: Call your doctor if you are sick with vomiting or diarrhea.

**L52.0** `Simple Sentence` (0.991) → `passthrough`
- original: This medicine can affect the results of certain medical tests.
- pronoun resolved: Empagliflozin can affect the results of certain medical tests.
  - edits: “This medicine” → “Empagliflozin”

**L52.1** `Incomplete Sentence` (0.893) → `excluded_incomplete`
- original: Tell any doctor who treats you that you are using empagliflozin.

**L53.0** `Simple Sentence` (0.808) → `passthrough`
- original: Your treatment may also include diet, exercise, weight control, and special medical care.

**L54.0** `Incomplete Sentence` (0.955) → `excluded_incomplete`
- original: Tell your doctor if you have a planned surgery.

**L55.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Store at room temperature away from moisture and heat.

## What happens if I miss a dose?

**L58.0** `Compound Sentence` (0.555) → `decomposed`
- original: Take the medicine as soon as you can, but skip the missed dose if it is almost time for your next dose.
  - S1: Take the medicine as soon as you can.
  - S2: Skip the missed dose if it is almost time for your next dose.

**L58.1** `Incomplete Sentence` (0.84) → `excluded_incomplete`
- original: Do not take two doses at one time.

## What happens if I overdose?

**L61.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

## What should I avoid while taking empagliflozin?

**L64.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Avoid drinking alcohol.

**L65.0** `Incomplete Sentence` (0.599) → `excluded_incomplete`
- original: Avoid getting up too fast from a sitting or lying position, or you may feel dizzy.

## What other drugs will affect empagliflozin?

**L68.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Tell your doctor about all your other medicines, especially:

**L69.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: insulin, or other oral diabetes medicine; or

**L70.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a diuretic or "water pill."

**L71.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L71.1** `Complex Sentence` (0.605) → `decomposed`
- original: Other drugs may affect empagliflozin, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may affect empagliflozin.
  - S2: These other drugs include prescription and over-the-counter medicines.
  - S3: These other drugs also include vitamins and herbal products.

**L71.2** `Simple Sentence` (0.98) → `passthrough`
- original: Not all possible drug interactions are listed here.

## Popular FAQ

**L74.0** `Incomplete Sentence` (0.944) → `excluded_incomplete`
- original: Q: How long does it take for Jardiance to work?

**L74.1** `Compound-Complex Sentence` (0.918) → `decomposed`
- original: A: The beneficial effect of oral Jardiance on your blood sugar levels may begin quickly, within the first 1 to 2 weeks, but Jardiance is used over the long-term to treat type 2 diabetes and can offer ongoing benefits for heart health, kidney function and weight loss.
  - S1: The beneficial effect of oral Jardiance on your blood sugar levels may begin quickly.
  - S2: The beneficial effect of oral Jardiance on your blood sugar levels may begin within the first 1 to 2 weeks.
  - S3: Jardiance is used over the long-term to treat type 2 diabetes.
  - S4: Jardiance can offer ongoing benefits for heart health.
  - S5: Jardiance can offer ongoing benefits for kidney function.
  - S6: Jardiance can offer ongoing benefits for weight loss.

**L75.0** `Incomplete Sentence` (0.969) → `excluded_incomplete`
- original: Q: How does Jardiance help with heart failure?

**L75.1** `Complex Sentence` (0.789) → `decomposed`
- original: A: Jardiance (empagliflozin) helps with heart failure by making your kidneys remove extra sugar, salt, and water through your urine.
  - S1: Jardiance (empagliflozin) helps with heart failure.
  - S2: It does this by making your kidneys remove extra sugar, salt, and water.
  - S3: The kidneys remove these substances through your urine.

**L75.2** `Compound Sentence` (0.648) → `decomposed`
- original: This eases fluid buildup and lowers the pressure your heart pumps against, so the heart does not have to work as hard.
  - S1: This eases fluid buildup.
  - S2: It lowers the pressure your heart pumps against.
  - S3: Therefore, the heart does not have to work as hard.

**L75.3** `Complex Sentence` (0.839) → `decomposed`
- original: Researchers think it may also help the heart use energy better, calm inflammation, and slow harmful changes in the heart's shape.
- pronoun resolved: Researchers think Empagliflozin may also help the heart use energy better, calm inflammation, and slow harmful changes in the heart's shape.
  - edits: “it” → “Empagliflozin”
  - S1: Researchers think Empagliflozin may help the heart use energy better.
  - S2: Researchers think Empagliflozin may calm inflammation.
  - S3: Researchers think Empagliflozin may slow harmful changes in the heart's shape.
