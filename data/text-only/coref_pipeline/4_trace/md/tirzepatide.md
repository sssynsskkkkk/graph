# Tirzepatide — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/tirzepatide.txt` · 259 sentences · 30 changed by pronoun resolution · 412 sentences sent to EDC

## What is Tirzepatide?

**L5.0** `Complex Sentence` (0.922) → `decomposed`
- original: Tirzepatide is a once-weekly injection available as two brands: Zepbound (for weight loss, weight management, and obstructive sleep apnea) and Mounjaro (for type 2 diabetes and to lower the risk of major adverse cardiovascular events in those with type 2 diabetes at high risk).
  - S1: Tirzepatide is a once-weekly injection.
  - S2: It is available as two brands.
  - S3: One brand is Zepbound.
  - S4: Zepbound is for weight loss, weight management, and obstructive sleep apnea.
  - S5: The other brand is Mounjaro.
  - S6: Mounjaro is for type 2 diabetes.
  - S7: Mounjaro is also to lower the risk of major adverse cardiovascular events.
  - S8: This risk reduction applies to those with type 2 diabetes at high risk.

**L6.0** `Complex Sentence` (0.586) → `decomposed`
- original: Zepbound (tirzepatide) is FDA-approved for weight loss and weight management in adults with obesity, or in overweight adults with at least one weight-related medical condition.
  - S1: Zepbound (tirzepatide) is FDA-approved for weight loss and weight management in adults with obesity.
  - S2: It is also approved for overweight adults with at least one weight-related medical condition.

**L6.1** `Simple Sentence` (0.397) → `passthrough`
- original: Zepbound is also approved to treat moderate-to-severe obstructive sleep apnea (OSA) in adults with obesity.

**L7.0** `Complex Sentence` (0.935) → `decomposed`
- original: Mounjaro (tirzepatide) is FDA-approved for type 2 diabetes in adults and children aged 10 years and older to help improve blood sugar (glucose) levels, used alongside diet and exercise.
  - S1: Mounjaro (tirzepatide) is FDA-approved for type 2 diabetes in adults and children aged 10 years and older.
  - S2: It is used to help improve blood sugar (glucose) levels.
  - S3: It is used alongside diet and exercise.

**L7.1** `Complex Sentence` (0.928) → `decomposed`
- original: It is also approved to lower the risk of major adverse cardiovascular events (cardiovascular death, non-fatal heart attack, or non-fatal stroke) in adults with type 2 diabetes who are at high risk for these events.
- pronoun resolved: Mounjaro is also approved to lower the risk of major adverse cardiovascular events (cardiovascular death, non-fatal heart attack, or non-fatal stroke) in adults with type 2 diabetes who are at high risk for these events.
  - edits: “It” → “Mounjaro”
  - S1: Mounjaro is approved to lower the risk of major adverse cardiovascular events.
  - S2: These events include cardiovascular death, non-fatal heart attack, or non-fatal stroke.
  - S3: This approval applies to adults with type 2 diabetes.
  - S4: It applies to those who are at high risk for these events.

**L8.0** `Complex Sentence` (0.909) → `decomposed`
- original: Tirzepatide is a dual GIP/ GLP-1 receptor agonist, meaning it activates two gut hormone receptors that help regulate appetite, digestion, and blood sugar.
- pronoun resolved: Tirzepatide is a dual GIP/ GLP-1 receptor agonist, meaning Tirzepatide activates two gut hormone receptors that help regulate appetite, digestion, and blood sugar.
  - edits: “it” → “Tirzepatide”
  - S1: Tirzepatide is a dual GIP/GLP-1 receptor agonist.
  - S2: Tirzepatide activates two gut hormone receptors.
  - S3: These receptors help regulate appetite, digestion, and blood sugar.

**L8.1** `Compound Sentence` (0.81) → `decomposed`
- original: It works by reducing appetite, increasing feelings of fullness, slowing gastric emptying, boosting insulin release when blood sugar is high, and reducing glucagon secretion.
- pronoun resolved: Tirzepatide works by reducing appetite, increasing feelings of fullness, slowing gastric emptying, boosting insulin release when blood sugar is high, and reducing glucagon secretion.
  - edits: “It” → “Tirzepatide”
  - S1: Tirzepatide works by reducing appetite.
  - S2: It increases feelings of fullness.
  - S3: It slows gastric emptying.
  - S4: It boosts insulin release when blood sugar is high.
  - S5: It reduces glucagon secretion.

**L9.0** `Compound Sentence` (0.958) → `decomposed`
- original: Tirzepatide is self-administered as a subcutaneous (under the skin) injection using a single-dose pen, KwikPen, or vial with syringe, and should always be used together with diet and exercise.
  - S1: Tirzepatide is self-administered as a subcutaneous (under the skin) injection using a single-dose pen, KwikPen, or vial with syringe.
  - S2: It should always be used together with diet and exercise.

**L10.0** `Simple Sentence` (0.992) → `passthrough`
- original: Tirzepatide should not be used in people with type 1 diabetes.

**L10.1** `Simple Sentence` (0.725) → `passthrough`
- original: It is not known if tirzepatide is safe in people who have had pancreatitis.

## How Much Weight Can You Lose on Tirzepatide?

**L13.0** `Complex Sentence` (0.87) → `decomposed`
- original: Patients on Tirzepatide 15 mg weekly lost an average of 20.9% or 48.6 lb of their body weight after 72 weeks in the Zepbound Study 1 (NCT04184622) compared to placebo patients who lost an average of 3.1% or 7.2 lb.
- pronoun resolved: Patients on Tirzepatide 15 mg weekly lost an average of 20.9% or 48.6 lb of Patients's body weight after 72 weeks in the Zepbound Study 1 (NCT04184622) compared to placebo patients who lost an average of 3.1% or 7.2 lb.
  - edits: “their” → “Patients's”
  - S1: Patients on Tirzepatide 15 mg weekly lost an average of 20.9% or 48.6 lb of body weight.
  - S2: This occurred after 72 weeks in the Zepbound Study 1 (NCT04184622).
  - S3: Placebo patients lost an average of 3.1% or 7.2 lb of body weight.

**L14.0** `Complex Sentence` (0.884) → `decomposed`
- original: Study 1 was a 72-week trial comparing Zepbound weight loss with placebo in adults with obesity or overweight with at least one weight-related condition, excluding patients with type 2 diabetes.
  - S1: Study 1 was a 72-week trial.
  - S2: The trial compared Zepbound weight loss with placebo.
  - S3: The trial included adults with obesity or overweight with at least one weight-related condition.
  - S4: The trial excluded patients with type 2 diabetes.

**L15.0** `Simple Sentence` (0.99) → `passthrough`
- original: Zepbound Weight Loss Results at 72 Weeks by Dose:

**L16.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Treatment dose | Average % weight loss | Average weight lost | Average starting weight

**L17.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Zepbound 5 mg | 15.0% | 34.0 lb | 226.9 lb

**L18.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Zepbound 10 mg | 19.5% | 45.5 lb | 233.2 lb

**L19.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Zepbound 15 mg | 20.9% | 48.6 lb | 232.8 lb

**L20.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Placebo | 3.1% | 7.2 lb | 231.0 lb

## Mounjaro HbA1c Results for Type 2 Diabetes

**L23.0** `Complex Sentence` (0.913) → `decomposed`
- original: In the Mounjaro prescribing information, SURPASS-1 (NCT03954834) was a 40-week trial in adults with type 2 diabetes whose blood sugar was not adequately controlled with diet and exercise alone.
  - S1: In the Mounjaro prescribing information, SURPASS-1 (NCT03954834) was a 40-week trial.
  - S2: The trial was in adults with type 2 diabetes.
  - S3: The adults had blood sugar that was not adequately controlled with diet and exercise alone.

**L23.1** `Simple Sentence` (0.964) → `passthrough`
- original: Patients received once-weekly Mounjaro 5 mg, 10 mg, or 15 mg, or placebo.

**L24.0** `Compound Sentence` (0.436) → `decomposed`
- original: After 40 weeks, 78% to 85% of adults taking Mounjaro achieved an HbA1c below 7%, compared with 23% of adults taking a placebo.
  - S1: After 40 weeks, 78% to 85% of adults taking Mounjaro achieved an HbA1c below 7%.
  - S2: This is compared with 23% of adults taking a placebo.

**L25.0** `Compound Sentence` (0.942) → `decomposed`
- original: The average HbA1c change was -1.8% with Mounjaro 5 mg, -1.7% with Mounjaro 10 mg, and -1.7% with Mounjaro 15 mg, compared with -0.1% with placebo.
  - S1: The average HbA1c change was -1.8% with Mounjaro 5 mg.
  - S2: The average HbA1c change was -1.7% with Mounjaro 10 mg.
  - S3: The average HbA1c change was -1.7% with Mounjaro 15 mg.
  - S4: The average HbA1c change was -0.1% with placebo.

## Mounjaro Results for Reducing Cardiovascular Risk

**L28.0** `Complex Sentence` (0.948) → `decomposed`
- original: SURPASS-CVOT randomized 13,299 adults with type 2 diabetes and established cardiovascular disease to Mounjaro (tirzepatide, up to 15 mg once weekly) or dulaglutide 1.5 mg once weekly, a GLP-1 medicine already approved to reduce cardiovascular risk, with a median follow-up of about 4 years.
  - S1: SURPASS-CVOT randomized 13,299 adults with type 2 diabetes and established cardiovascular disease.
  - S2: The adults were randomized to Mounjaro (tirzepatide, up to 15 mg once weekly) or dulaglutide 1.5 mg once weekly.
  - S3: Dulaglutide is a GLP-1 medicine already approved to reduce cardiovascular risk.
  - S4: The study had a median follow-up of about 4 years.

**L29.0** `Complex Sentence` (0.908) → `decomposed`
- original: Cardiovascular death, non-fatal heart attack, or non-fatal stroke occurred in 12.1% of those taking Mounjaro compared with 13.0% of those taking dulaglutide (HR 0.92, 95.3% CI 0.83–1.01), meeting the trial's goal of non-inferiority but not demonstrating superiority.
  - S1: Cardiovascular death, non-fatal heart attack, or non-fatal stroke occurred in 12.1% of those taking Mounjaro.
  - S2: These events occurred in 13.0% of those taking dulaglutide.
  - S3: The hazard ratio was 0.92 with a 95% CI of 0.83–1.01.
  - S4: The results met the trial's goal of non-inferiority.
  - S5: The results did not demonstrate superiority.

**L30.0** `Compound-Complex Sentence` (0.911) → `decomposed`
- original: Death from any cause occurred in 8.5% of the Mounjaro group versus 10.1% of the dulaglutide group (HR 0.84, 95% CI 0.75–0.94), though this was not a primary endpoint and was not adjusted for multiple comparisons, so it should be read as exploratory.
- pronoun resolved: Death from any cause occurred in 8.5% of the Mounjaro group versus 10.1% of the dulaglutide group (HR 0.84, 95% CI 0.75–0.94), though this was not a primary endpoint and was not adjusted for multiple comparisons, so Mounjaro should be read as exploratory.
  - edits: “it” → “Mounjaro”
  - S1: Death from any cause occurred in 8.5% of the Mounjaro group.
  - S2: Death from any cause occurred in 10.1% of the dulaglutide group.
  - S3: The hazard ratio was 0.84.
  - S4: The 95% confidence interval was 0.75–0.94.
  - S5: This outcome was not a primary endpoint.
  - S6: This outcome was not adjusted for multiple comparisons.
  - S7: Therefore, Mounjaro results should be read as exploratory.

**L31.0** `Complex Sentence` (0.927) → `decomposed`
- original: Because the comparator was an active medicine rather than placebo, these results describe how Mounjaro performs against another GLP-1, not how much it lowers risk compared with no treatment.
- pronoun resolved: Because the comparator was an active medicine rather than placebo, these results describe how Mounjaro performs against another GLP-1, not how much Mounjaro lowers risk compared with no treatment.
  - edits: “it” → “Mounjaro”
  - S1: The comparator was an active medicine rather than placebo.
  - S2: These results describe how Mounjaro performs against another GLP-1.
  - S3: These results do not describe how much Mounjaro lowers risk compared with no treatment.

## Tirzepatide side effects

**L34.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Common Side Effects:

**L35.0** `Simple Sentence` (0.964) → `passthrough`
- original: The most common tirzepatide side effects are:

**L36.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Diarrhea

**L37.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Vomiting

**L38.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Constipation

**L39.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Nausea (mild to moderate)

**L40.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Decreased appetite

**L41.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Abdominal pain.

**L42.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious side effects:

**L43.0** `Simple Sentence` (0.989) → `passthrough`
- original: Tirzepatide can cause serious side effects.

**L43.1** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Call your doctor right away if you have any of the following:

**L44.0** `Complex Sentence` (0.601) → `decomposed`
- original: Severe stomach pain (pancreatitis): Stop taking tirzepatide and call your healthcare provider immediately if you have severe pain in your stomach area that will not go away, with or without vomiting, or pain that spreads to your back.
  - S1: Stop taking tirzepatide and call your healthcare provider immediately if you have severe pain in your stomach area that will not go away.
  - S2: This applies if the pain occurs with or without vomiting.
  - S3: This also applies if the pain spreads to your back.
  - S4: Severe stomach pain is a sign of pancreatitis.

**L45.0** `Complex Sentence` (0.659) → `decomposed`
- original: Kidney problems: Diarrhea, nausea, and vomiting can cause dehydration, which may lead to kidney problems.
  - S1: Diarrhea, nausea, and vomiting can cause dehydration.
  - S2: Dehydration may lead to kidney problems.

**L45.1** `Compound Sentence` (0.525) → `decomposed`
- original: Drink plenty of fluids to reduce this risk and tell your doctor if you are unable to keep fluids down.
  - S1: Drink plenty of fluids to reduce this risk.
  - S2: Tell your doctor if you are unable to keep fluids down.

**L46.0** `Compound Sentence` (0.505) → `decomposed`
- original: Gallbladder problems: Symptoms include severe upper stomach pain, fever, nausea, vomiting, yellowing of the skin or eyes (jaundice), or clay-colored stools.
  - S1: Gallbladder problems include severe upper stomach pain.
  - S2: They include fever.
  - S3: They include nausea.
  - S4: They include vomiting.
  - S5: They include yellowing of the skin or eyes (jaundice).
  - S6: They include clay-colored stools.

**L47.0** `Complex Sentence` (0.75) → `decomposed`
- original: Serious allergic reactions: Seek emergency medical attention if you experience hives, difficulty breathing, feeling light-headed, or swelling of your face, lips, tongue, or throat (anaphylaxis or angioedema).
  - S1: Serious allergic reactions require seeking emergency medical attention.
  - S2: Seek emergency medical attention if you experience hives.
  - S3: Seek emergency medical attention if you experience difficulty breathing.
  - S4: Seek emergency medical attention if you feel light-headed.
  - S5: Seek emergency medical attention if you experience swelling of your face, lips, tongue, or throat.
  - S6: These symptoms include anaphylaxis or angioedema.

**L48.0** `Compound Sentence` (0.495) → `decomposed`
- original: Low blood sugar (hypoglycemia): Symptoms may include headache, hunger, weakness, sweating, confusion, irritability, dizziness, fast heart rate, or feeling jittery.
  - S1: Low blood sugar is hypoglycemia.
  - S2: Symptoms may include headache, hunger, weakness, sweating, confusion, irritability, dizziness, fast heart rate, or feeling jittery.

**L49.0** `Simple Sentence` (0.837) → `passthrough`
- original: Vision changes: Tell your doctor about any blurred vision or other vision changes, particularly if you have type 2 diabetes.

**L50.0** `Simple Sentence` (0.625) → `passthrough`
- original: Thyroid tumor: Symptoms may include a lump or swelling in your neck, trouble swallowing, hoarseness, or shortness of breath.

**L51.0** `Simple Sentence` (0.595) → `passthrough`
- original: Mental health changes: Tell your healthcare provider right away about any new or worsening depression, mood changes, or thoughts of suicide or self-harm.

**L52.0** `Complex Sentence` (0.937) → `decomposed`
- original: Aspiration during surgery: Tirzepatide slows stomach emptying, which may increase the risk of food or liquid entering the lungs during procedures using anesthesia or sedation.
  - S1: Aspiration during surgery may increase the risk of food or liquid entering the lungs.
  - S2: Tirzepatide slows stomach emptying.
  - S3: This risk may occur during procedures using anesthesia or sedation.

**L52.1** `Incomplete Sentence` (0.803) → `excluded_incomplete`
- original: Tell all your healthcare providers you are taking tirzepatide before any planned surgery or procedure.

**L53.0** `Simple Sentence` (0.937) → `passthrough`
- original: This is not a complete list of side effects.

**L53.1** `Compound Sentence` (0.397) → `decomposed`
- original: Call your doctor for medical advice about side effects, or report them to the FDA at 1-800-FDA-1088.
- pronoun resolved: Call your doctor for medical advice about side effects, or report side effects to the FDA at 1-800-FDA-1088.
  - edits: “them” → “side effects”
  - S1: Call your doctor for medical advice about side effects.
  - S2: Report side effects to the FDA at 1-800-FDA-1088.

## Important Safety Information

**L56.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Who should not use tirzepatide:

**L57.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Type 1 diabetes patients (tirzepatide is not approved for type 1 diabetes)

**L58.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Personal or family history of medullary thyroid carcinoma (MTC)

**L59.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Multiple Endocrine Neoplasia syndrome type 2 (MEN 2).

**L60.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Use with Caution:

**L61.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: History of pancreatitis (safety not established in patients with prior pancreatitis)

**L62.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Severe gastrointestinal disease

**L63.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Diabetic retinopathy complications.

## Warnings

**L66.0** `Simple Sentence` (0.987) → `passthrough`
- original: Tirzepatide carries a Boxed Warning for the risk of possible thyroid tumors.

**L67.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Possible Thyroid Tumors (Including Cancer):

**L68.0** `Incomplete Sentence` (0.401) → `excluded_incomplete`
- original: Tell your healthcare provider if you get a lump or swelling in your neck, hoarseness, trouble swallowing, or shortness of breath.

**L68.1** `Simple Sentence` (0.987) → `passthrough`
- original: These may be symptoms of thyroid cancer.

**L68.2** `Complex Sentence` (0.895) → `decomposed`
- original: In studies with rats, tirzepatide and medicines that work like tirzepatide have caused thyroid tumors, including thyroid cancer.
  - S1: In studies with rats, tirzepatide and medicines that work like tirzepatide have caused thyroid tumors.
  - S2: These tumors include thyroid cancer.

**L68.3** `Complex Sentence` (0.613) → `decomposed`
- original: It is not known if tirzepatide will cause thyroid tumors, or a type of thyroid cancer called medullary thyroid carcinoma (MTC) in people.
  - S1: It is not known if tirzepatide will cause thyroid tumors.
  - S2: It is not known if tirzepatide will cause medullary thyroid carcinoma.
  - S3: Medullary thyroid carcinoma is a type of thyroid cancer.
  - S4: This applies to people.

**L69.0** `Compound Sentence` (0.619) → `decomposed`
- original: Do not use tirzepatide if you or any of your family have ever had a type of thyroid cancer called medullary thyroid carcinoma (MTC), or if you have an endocrine system condition called Multiple Endocrine Neoplasia syndrome type 2 (MEN 2).
  - S1: Do not use tirzepatide if you or any of your family have ever had a type of thyroid cancer called medullary thyroid carcinoma (MTC).
  - S2: Do not use tirzepatide if you have an endocrine system condition called Multiple Endocrine Neoplasia syndrome type 2 (MEN 2).

## Before using tirzepatide

**L72.0** `Incomplete Sentence` (0.318) → `excluded_incomplete`
- original: Tell your doctor and pharmacist if you are allergic to tirzepatide, any other medications, or any of the ingredients in this medicine.
- pronoun resolved: Tell your doctor and pharmacist if you are allergic to tirzepatide, any other medications, or any of the ingredients in tirzepatide.
  - edits: “this medicine.” → “tirzepatide.”

**L72.1** `Simple Sentence` (0.972) → `passthrough`
- original: There is a list of ingredients in this medicine, at the bottom of this page.
- pronoun resolved: There is a list of ingredients in tirzepatide, at the bottom of this page.
  - edits: “this medicine,” → “tirzepatide,”

**L73.0** `Incomplete Sentence` (0.835) → `excluded_incomplete`
- original: Tell your healthcare team if you are planning surgery or other procedure that uses anesthesia or deep sedation.

**L74.0** `Incomplete Sentence` (0.321) → `excluded_incomplete`
- original: Tell your doctor if you have or have ever had kidney or pancreas disease, a history of diabetic retinopathy or any stomach problems such as difficulty digesting food.

**L75.0** `Incomplete Sentence` (0.674) → `excluded_incomplete`
- original: Tell your doctor if you plan to become pregnant, are pregnant, or are breastfeeding.

**L75.1** `Simple Sentence` (0.925) → `passthrough`
- original: If you become pregnant while taking this medicine, you should tell your doctor.
- pronoun resolved: If you become pregnant while taking tirzepatide, you should tell your doctor.
  - edits: “this medicine,” → “tirzepatide,”

**L75.2** `Simple Sentence` (0.982) → `passthrough`
- original: There is a pregnancy exposure registry for women who take Zepbound during pregnancy.

**L75.3** `Compound Sentence` (0.772) → `decomposed`
- original: Talk to your healthcare provider about how you can take part, call 1-844-524-0039, or visit https://pregnancyregistry.lilly.com/zepbound.
  - S1: Talk to your healthcare provider about how you can take part.
  - S2: Call 1-844-524-0039.
  - S3: Visit https://pregnancyregistry.lilly.com/zepbound.

## What is the cost of tirzepatide?

**L78.0** `Simple Sentence` (0.683) → `passthrough`
- original: The cost of tirzepatide depends on your insurance plan, pharmacy, and the brand you use.

**L79.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Zepbound cost

**L80.0** `Compound Sentence` (0.457) → `decomposed`
- original: Zepbound may cost $25 for a 1-month or 3-month pen prescription if you have commercial insurance and are eligible for the Savings Card.
  - S1: Zepbound may cost $25 for a 1-month or 3-month pen prescription.
  - S2: This pricing applies if you have commercial insurance and are eligible for the Savings Card.

**L80.1** `Simple Sentence` (0.639) → `passthrough`
- original: Note that patients with government insurance (Medicare, Medicaid) are not eligible for the savings card.

**L80.2** `Complex Sentence` (0.77) → `decomposed`
- original: Through the Zepbound self-pay program, tirzepatide is available directly to patients as a 4-count single-dose vial or single-patient-use KwikPen.
  - S1: Through the Zepbound self-pay program, tirzepatide is available directly to patients.
  - S2: Tirzepatide is available as a 4-count single-dose vial.
  - S3: Tirzepatide is available as a single-patient-use KwikPen.

**L80.3** `Compound Sentence` (0.828) → `decomposed`
- original: All six doses are available: 2.5 mg ($299), 5 mg ($399), 7.5 mg ($499), 10 mg ($699), 12.5 mg ($699), and 15 mg ($699) per month.
  - S1: All six doses are available.
  - S2: The 2.5 mg dose costs $299 per month.
  - S3: The 5 mg dose costs $399 per month.
  - S4: The 7.5 mg dose costs $499 per month.
  - S5: The 10 mg dose costs $699 per month.
  - S6: The 12.5 mg dose costs $699 per month.
  - S7: The 15 mg dose costs $699 per month.

**L80.4** `Compound Sentence` (0.717) → `decomposed`
- original: The list price of Zepbound is $499–$1,086.37 per fill, but this is not what most people pay.
  - S1: The list price of Zepbound is $499–$1,086.37 per fill.
  - S2: This is not what most people pay.

**L81.0** `Incomplete Sentence` (0.945) → `excluded_incomplete`
- original: Refer to our Zepbound price guide for more information, or see " How much is Zepbound with or without insurance? "

**L81.1** `Incomplete Sentence` (0.97) → `excluded_incomplete`
- original: and " What is the Zepbound Coupon or Savings Card? "

**L82.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Mounjaro cost

**L83.0** `Compound Sentence` (0.543) → `decomposed`
- original: Mounjaro may cost $25 for up to a 3-month prescription if you have commercial insurance and are eligible for the Savings Card.
  - S1: Mounjaro may cost $25 for up to a 3-month prescription.
  - S2: This applies if you have commercial insurance and are eligible for the Savings Card.

**L83.1** `Simple Sentence` (0.639) → `passthrough`
- original: Note that patients with government insurance (Medicare, Medicaid) are not eligible for the savings card.

**L83.2** `Complex Sentence` (0.801) → `decomposed`
- original: Without insurance, Mounjaro can cost $499 for a 1-month prescription of single-dose pens (all strengths) through the LillyDirect Mounjaro Self Pay Journey Program.
  - S1: Without insurance, Mounjaro can cost $499 for a 1-month prescription.
  - S2: The prescription consists of single-dose pens of all strengths.
  - S3: This pricing is available through the LillyDirect Mounjaro Self Pay Journey Program.

**L83.3** `Compound Sentence` (0.832) → `decomposed`
- original: The list price of Mounjaro is $1,112.16 per fill, but this is not what most people pay.
  - S1: The list price of Mounjaro is $1,112.16 per fill.
  - S2: This is not what most people pay.

**L84.0** `Incomplete Sentence` (0.927) → `excluded_incomplete`
- original: Refer to our Mounjaro price guide for more information, or see " Can you afford Mounjaro without insurance? "

**L84.1** `Incomplete Sentence` (0.972) → `excluded_incomplete`
- original: and " What is the Mounjaro Coupon or Savings Card? "

## How should I use tirzepatide?

**L87.0** `Compound Sentence` (0.536) → `decomposed`
- original: You should follow the directions on your prescription label carefully and ask your pharmacist or doctor to explain any part you do not understand.
  - S1: You should follow the directions on your prescription label carefully.
  - S2: You should ask your pharmacist or doctor to explain any part you do not understand.

**L87.1** `Simple Sentence` (0.968) → `passthrough`
- original: It is important to use this medicine exactly as directed.

**L87.2** `Incomplete Sentence` (0.924) → `excluded_incomplete`
- original: Do not take more or less of it or take it more often than prescribed by your doctor.

**L88.0** `Compound Sentence` (0.798) → `decomposed`
- original: Tirzepatide is injected under the skin (subcutaneously) using a pre-filled single-dose pen, a multi-dose KwikPen (for single patient use), and a single-dose vial with a syringe.
  - S1: Tirzepatide is injected under the skin (subcutaneously) using a pre-filled single-dose pen.
  - S2: It is also injected using a multi-dose KwikPen (for single patient use).
  - S3: Additionally, it is injected using a single-dose vial with a syringe.

**L88.1** `Compound Sentence` (0.665) → `decomposed`
- original: Caregivers or patients should be trained on proper injection techniques and should read the instructions for use.
  - S1: Caregivers or patients should be trained on proper injection techniques.
  - S2: They should read the instructions for use.

**L88.2** `Compound Sentence` (0.832) → `decomposed`
- original: Children should not inject themselves with the KwikPen; an adult caregiver should give a child their injections.
- pronoun resolved: Children should not inject Children with the KwikPen; an adult caregiver should give a child a child's injections.
  - edits: “themselves” → “Children”; “their” → “a child's”
  - S1: Children should not inject children with the KwikPen.
  - S2: An adult caregiver should give a child a child's injections.

**L89.0** `Simple Sentence` (0.974) → `passthrough`
- original: Tirzepatide is usually given:

**L90.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: once a week.

**L91.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: can be given with or without meals at any time of the day.

**L92.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: may be injected into the thigh, abdomen, or have another person inject it into the back of your upper arm
- pronoun resolved: may be injected into the thigh, abdomen, or have another person inject Tirzepatide into the back of your upper arm
  - edits: “it” → “Tirzepatide”

**L93.0** `Simple Sentence` (0.986) → `passthrough`
- original: You should rotate injection sites with each dose.

**L94.0** `Incomplete Sentence` (0.599) → `excluded_incomplete`
- original: Do not inject into a muscle (intramuscularly) or vein (intravenously).

**L95.0** `Simple Sentence` (0.532) → `passthrough`
- original: Do not mix insulin and tirzepatide together in the same injection.

**L95.1** `Simple Sentence` (0.54) → `passthrough`
- original: You may give an injection of tirzepatide and insulin in the same body area, but not right next to each other.

**L96.0** `Compound Sentence` (0.792) → `decomposed`
- original: Your doctor will probably start you on a low dose, which may be gradually increased, but not more than once every 4 weeks.
  - S1: Your doctor will probably start you on a low dose.
  - S2: This dose may be gradually increased.
  - S3: However, it will not be increased more than once every 4 weeks.

**L97.0** `Simple Sentence` (0.728) → `passthrough`
- original: You may change the day of the week you use tirzepatide as long as there are at least three days between doses.

**L98.0** `Simple Sentence` (0.777) → `passthrough`
- original: Do not stop taking this medicine without talking to your doctor.
- pronoun resolved: Do not stop taking Tirzepatide without talking to your doctor.
  - edits: “this medicine” → “Tirzepatide”

**L99.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Tirzepatide KwikPen:

**L100.0** `Compound Sentence` (0.945) → `decomposed`
- original: The KwikPen contains 4 fixed doses, and one dose is injected weekly (subcutaneously).
  - S1: The KwikPen contains 4 fixed doses.
  - S2: One dose is injected weekly (subcutaneously).

**L101.0** `Complex Sentence` (0.589) → `decomposed`
- original: For your weekly dose, you need to turn the dose knob all the way until it stops AND the 1 icon is in the dose window.
- pronoun resolved: For your weekly dose, you need to turn the dose knob all the way until KwikPen stops AND the 1 icon is in the dose window.
  - edits: “it” → “KwikPen”
  - S1: For your weekly dose, you need to turn the dose knob all the way until KwikPen stops.
  - S2: You also need to turn the dose knob until the 1 icon is in the dose window.

**L102.0** `Incomplete Sentence` (0.599) → `excluded_incomplete`
- original: After 4 doses, throw away (discard) the Pen, including the unused medicine.

**L102.1** `Simple Sentence` (0.947) → `passthrough`
- original: The Pen will prevent you from dialing a full dose after you have given yourself 4 weekly doses.

**L102.2** `Incomplete Sentence` (0.942) → `excluded_incomplete`
- original: Do not inject the leftover medicine.

**L102.3** `Simple Sentence` (0.534) → `passthrough`
- original: Do not transfer the leftover medicine from your Pen into a syringe.

**L103.0** `Incomplete Sentence` (0.622) → `excluded_incomplete`
- original: Do not share your tirzepatide Pen with other people, even if the pen needle has been changed.

**L103.1** `Simple Sentence` (0.974) → `passthrough`
- original: You may give other people a serious infection or get a serious infection from them.
- pronoun resolved: You may give other people a serious infection or get a serious infection from other people.
  - edits: “them.” → “other people.”

**L104.0** `Complex Sentence` (0.462) → `decomposed`
- original: People who are blind or have vision problems should not use the Pen without help from a person who has been trained to use the pen.
  - S1: People who are blind or have vision problems should not use the Pen.
  - S2: They should not use the Pen without help.
  - S3: The help must come from a person who has been trained to use the pen.

## Dosing Information

**L107.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual Zepbound Dose for Weight Loss and OSA (Adult):

**L108.0** `Incomplete Sentence` (0.769) → `excluded_incomplete`
- original: Initial dose: 2.5 mg under the skin (subcutaneously) once a week.

**L109.0** `Simple Sentence` (0.873) → `passthrough`
- original: After 4 weeks: The dosage should be increased to 5 mg subcutaneously once a week.

**L110.0** `Complex Sentence` (0.758) → `decomposed`
- original: Further dose increases: After at least 4 weeks on the current dose, the dosage may be increased in 2.5 mg increments.
  - S1: Further dose increases may occur after at least 4 weeks on the current dose.
  - S2: The dosage may be increased in 2.5 mg increments.

**L111.0** `Simple Sentence` (0.849) → `passthrough`
- original: Recommended maintenance dose for weight loss: 5 mg, 10 mg, or 15 mg injected subcutaneously once weekly.

**L112.0** `Simple Sentence` (0.829) → `passthrough`
- original: Recommended maintenance dose for OSA: 10 mg or 15 mg injected subcutaneously once weekly.

**L113.0** `Incomplete Sentence` (0.917) → `excluded_incomplete`
- original: Maximum dose: 15 mg subcutaneously once a week.

**L114.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Dose of Mounjaro for Type 2 Diabetes (Adults and Children 10 Years and Older):

**L115.0** `Incomplete Sentence` (0.913) → `excluded_incomplete`
- original: Initial dose: 2.5 mg subcutaneously once a week.

**L116.0** `Compound Sentence` (0.474) → `decomposed`
- original: If additional glycemic control is needed: Increase the dose in 2.5 mg increments after at least 4 weeks on the current dose.
  - S1: Additional glycemic control is needed.
  - S2: Increase the dose in 2.5 mg increments after at least 4 weeks on the current dose.

**L117.0** `Incomplete Sentence` (0.513) → `excluded_incomplete`
- original: Maximum dose (adults): 15 mg subcutaneously once a week.

**L118.0** `Simple Sentence` (0.68) → `passthrough`
- original: Maximum dose (children 10 years and older): 10 mg subcutaneously once a week.

**L119.0** `Simple Sentence` (0.53) → `passthrough`
- original: Comments: The starting dose and escalation schedule are designed to reduce the risk of gastrointestinal side effects.

**L120.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Dose of Mounjaro to Reduce Cardiovascular Risk (Adults With Type 2 Diabetes at High Risk):

**L121.0** `Simple Sentence` (0.972) → `passthrough`
- original: The same dosing and escalation schedule applies.

**L122.0** `Compound Sentence` (0.602) → `decomposed`
- original: Start at 2.5 mg subcutaneously once a week and increase in 2.5 mg increments after at least 4 weeks on the current dose, up to a maximum of 15 mg once a week.
  - S1: Start at 2.5 mg subcutaneously once a week.
  - S2: Increase in 2.5 mg increments after at least 4 weeks on the current dose.
  - S3: Continue up to a maximum of 15 mg once a week.

**L123.0** `Compound Sentence` (0.475) → `decomposed`
- original: In the SURPASS-CVOT trial, participants were titrated to 15 mg once weekly or their maximum tolerated dose.
- pronoun resolved: In the SURPASS-CVOT trial, participants were titrated to 15 mg once weekly or participants's maximum tolerated dose.
  - edits: “their” → “participants's”
  - S1: In the SURPASS-CVOT trial, participants were titrated to 15 mg once weekly.
  - S2: Participants were titrated to their maximum tolerated dose.

**L124.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: How to Use Mounjaro:

**L125.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Give once weekly at any time of day, with or without meals.

**L126.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Inject subcutaneously into the abdomen or thigh.

**L126.1** `Simple Sentence` (0.98) → `passthrough`
- original: Another person may inject into the back of the upper arm.

**L126.2** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Rotate injection sites with each dose.

**L127.0** `Incomplete Sentence` (0.809) → `excluded_incomplete`
- original: Missed dose: Give as soon as possible within 4 days (96 hours).

**L127.1** `Compound Sentence` (0.679) → `decomposed`
- original: If more than 4 days have passed, skip the missed dose and give the next dose on the regularly scheduled day.
  - S1: If more than 4 days have passed, skip the missed dose.
  - S2: Give the next dose on the regularly scheduled day.

**L128.0** `Compound Sentence` (0.687) → `decomposed`
- original: The day of weekly administration can be changed, if necessary, as long as the time between the 2 doses is at least 3 days (72 hours).
  - S1: The day of weekly administration can be changed, if necessary.
  - S2: The time between the 2 doses must be at least 3 days (72 hours).

## What should I do if I miss a dose?

**L131.0** `Complex Sentence` (0.527) → `decomposed`
- original: If you miss a dose of tirzepatide, take the missed dose as soon as you remember it, if within 4 days after the missed dose.
- pronoun resolved: If you miss a dose of tirzepatide, take the missed dose as soon as you remember dose, if within 4 days after the missed dose.
  - edits: “it,” → “dose,”
  - S1: If you miss a dose of tirzepatide, take the missed dose as soon as you remember.
  - S2: Take the missed dose if it is within 4 days after the missed dose.

**L131.1** `Complex Sentence` (0.762) → `decomposed`
- original: However, if it has been more than 4 days since your last dose, then skip the missed dose and continue your regular dosing schedule.
- pronoun resolved: However, if dose has been more than 4 days since your last dose, then skip the missed dose and continue your regular dosing schedule.
  - edits: “it” → “dose”
  - S1: However, if more than 4 days have passed since your last dose.
  - S2: Then skip the missed dose.
  - S3: And continue your regular dosing schedule.

**L131.2** `Incomplete Sentence` (0.905) → `excluded_incomplete`
- original: Do not inject two doses within 3 days of each other.

## What happens if I overdose?

**L134.0** `Incomplete Sentence` (0.298) → `excluded_incomplete`
- original: In case of overdose, call the poison control helpline at 1-800-222-1222.

**L134.1** `Simple Sentence` (0.966) → `passthrough`
- original: Information is also available online at Poison Help.

**L134.2** `Complex Sentence` (0.529) → `decomposed`
- original: If the victim has collapsed, had a seizure, has trouble breathing, or can't be awakened, immediately call emergency services at 911.
  - S1: If the victim has collapsed, had a seizure, has trouble breathing, or can't be awakened.
  - S2: Immediately call emergency services at 911.

## Interactions

**L137.0** `Incomplete Sentence` (0.861) → `excluded_incomplete`
- original: Tell your doctor and pharmacist what prescription and over-the-counter medications, vitamins, nutritional supplements, and herbal products you are planning to take or are taking.

**L137.1** `Compound Sentence` (0.905) → `decomposed`
- original: They may interact with tirzepatide, and your doctor may need to change the doses of your medications or monitor you carefully for side effects.
  - S1: They may interact with tirzepatide.
  - S2: Your doctor may need to change the doses of your medications or monitor you carefully for side effects.

**L138.0** `Simple Sentence` (0.987) → `passthrough`
- original: Birth control pills may not work as well while receiving this medicine.
- pronoun resolved: Birth control pills may not work as well while receiving Tirzepatide.
  - edits: “this medicine.” → “Tirzepatide.”

**L138.1** `Compound Sentence` (0.437) → `decomposed`
- original: Your doctor may suggest you use another form of birth control for 4 weeks after starting tirzepatide and for 4 weeks after each dose change.
  - S1: Your doctor may suggest you use another form of birth control for 4 weeks after starting tirzepatide.
  - S2: Your doctor may suggest you use another form of birth control for 4 weeks after each dose change.

**L139.0** `Simple Sentence` (0.484) → `passthrough`
- original: Taking tirzepatide with other medicines to treat diabetes, such as sulfonylureas or insulin, may increase your risk of hypoglycemia.

**L139.1** `Incomplete Sentence` (0.941) → `excluded_incomplete`
- original: Talk to your doctor and pharmacist about low blood sugar and how to manage it.
- pronoun resolved: Talk to your doctor and pharmacist about low blood sugar and how to manage low blood sugar.
  - edits: “it.” → “low blood sugar.”

**L140.0** `Compound Sentence` (0.885) → `decomposed`
- original: This medicine delays gastric emptying and may alter the absorption of other orally administered medicines.
- pronoun resolved: Tirzepatide delays gastric emptying and may alter the absorption of other orally administered medicines.
  - edits: “This medicine” → “Tirzepatide”
  - S1: Tirzepatide delays gastric emptying.
  - S2: It may alter the absorption of other orally administered medicines.

**L141.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L141.1** `Complex Sentence` (0.579) → `decomposed`
- original: Many other drugs may interact with Mounjaro and Zepbound, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Many other drugs may interact with Mounjaro and Zepbound.
  - S2: These drugs include prescription and over-the-counter medicines.
  - S3: These drugs also include vitamins and herbal products.

**L141.2** `Simple Sentence` (0.952) → `passthrough`
- original: To check for interactions with this medicine, click the link below.
- pronoun resolved: To check for interactions with Tirzepatide, click the link below.
  - edits: “this medicine,” → “Tirzepatide,”

## How long does it take to lose weight on tirzepatide?

**L144.0** `Compound Sentence` (0.51) → `decomposed`
- original: Weight loss starts slowly in the first 4 weeks of treatment, with changes in appetite and a feeling of fullness with fewer cravings.
  - S1: Weight loss starts slowly in the first 4 weeks of treatment.
  - S2: Changes in appetite and a feeling of fullness with fewer cravings occur during this time.

**L144.1** `Compound Sentence` (0.838) → `decomposed`
- original: Then, more measurable weight loss occurs in the first 2 to 3 months, and increases over 6 to 12 months (SURMOUNT-1).
  - S1: Then, more measurable weight loss occurs in the first 2 to 3 months.
  - S2: Weight loss increases over 6 to 12 months (SURMOUNT-1).

**L144.2** `Simple Sentence` (0.875) → `passthrough`
- original: To learn more, see ” How long does it take for Zepbound to work?"

## Do you regain weight after stopping tirzepatide?

**L147.0** `Simple Sentence` (0.95) → `passthrough`
- original: Yes, when you stop tirzepatide, you may regain weight.

**L147.1** `Simple Sentence` (0.986) → `passthrough`
- original: Tirzepatide only works while you are using it.
- pronoun resolved: Tirzepatide only works while you are using Tirzepatide.
  - edits: “it.” → “Tirzepatide.”

**L147.2** `Compound-Complex Sentence` (0.897) → `decomposed`
- original: Patients who used Zepbound for 36 weeks lost an average of 21%, but then, when switched to a placebo, after 1 year, they had regained 14% of their weight back.
- pronoun resolved: Patients who used Zepbound for 36 weeks lost an average of 21%, but then, when switched to a placebo, after 1 year, Patients had regained 14% of Patients's weight back.
  - edits: “they” → “Patients”; “their” → “Patients's”
  - S1: Patients used Zepbound for 36 weeks.
  - S2: Patients who used Zepbound for 36 weeks lost an average of 21% of their weight.
  - S3: Patients were switched to a placebo after 1 year.
  - S4: Patients regained 14% of their weight back.

**L147.3** `Incomplete Sentence` (0.922) → `excluded_incomplete`
- original: (Phase 3 SURMOUNT-4 study) Learn more at: " What happens when you stop taking Zepbound ?

**L148.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Single-dose pens and vials (Zepbound and Mounjaro)

**L149.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Store in the refrigerator between 36°F and 46°F (2°C and 8°C).

**L150.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Do not freeze.

**L150.1** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Do not use if the medication has been frozen.

**L151.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Keep in the original carton until use to protect from light.

**L152.0** `Complex Sentence` (0.439) → `decomposed`
- original: If needed, single-dose pens and vials may be kept at room temperature up to 86°F (30°C) for up to 21 days.
  - S1: Single-dose pens and vials may be kept at room temperature.
  - S2: The pens and vials may be kept at room temperature if needed.
  - S3: They may be kept at room temperature up to 86°F (30°C).
  - S4: They may be kept at room temperature for up to 21 days.

**L152.1** `Simple Sentence` (0.693) → `passthrough`
- original: Once at room temperature, do not return to the refrigerator.

**L153.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Discard after 21 days at room temperature if unused.

**L154.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: KwikPen (Zepbound KwikPen and Mounjaro KwikPen)

**L155.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Before first use:

**L156.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Store in the refrigerator between 36°F and 46°F (2°C and 8°C).

**L157.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Keep until the expiration date printed on the label.

**L158.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Do not freeze.

**L158.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Discard the pen if it has been frozen.
- pronoun resolved: Discard the pen if pen has been frozen.
  - edits: “it” → “pen”

**L159.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: After first use:

**L160.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: Store in the refrigerator or at room temperature up to 86°F (30°C).

**L161.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Keep away from heat and light.

**L162.0** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: Discard the pen 30 days after first use, even if medicine remains.

**L163.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Discard after 4 weekly doses have been given.

**L164.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: General storage advice (all tirzepatide products)

**L165.0** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Keep all pens, vials, needles, and syringes out of reach of children.

**L166.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Dispose of used pens, needles, and syringes in an approved sharps container.

## Tirzepatide ingredients

**L169.0** `Simple Sentence` (0.586) → `passthrough`
- original: Zepbound and Mounjaro contain the same active ingredient, tirzepatide, and share the same inactive ingredients.

**L170.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Active ingredient: tirzepatide

**L171.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Inactive ingredients (single-dose pens and vials):

**L172.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Sodium chloride

**L173.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Sodium phosphate dibasic heptahydrate

**L174.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Water for injection

**L175.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Hydrochloric acid and/or sodium hydroxide (added to adjust pH)

**L176.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Additional inactive ingredients (KwikPen and multi-dose vial only):

**L177.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Benzyl alcohol

**L178.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Glycerin

**L179.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Phenol

## What strengths are Zepbound pens?

**L182.0** `Simple Sentence` (0.978) → `passthrough`
- original: Zepbound is available in the following strengths as single-dose pens or vials:

**L183.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: 2.5 mg/0.5 mL

**L184.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: 5 mg/0.5 mL

**L185.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: 7.5 mg/0.5 mL

**L186.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: 10 mg/0.5 mL

**L187.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: 12.5 mg/0.5 mL

**L188.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: 15 mg/0.5 mL

**L189.0** `Complex Sentence` (0.415) → `decomposed`
- original: Zepbound KwikPen (single-patient-use) or multi-dose vial, each containing 4 doses, are approved by the FDA in the following strengths:
  - S1: Zepbound KwikPen is available as a single-patient-use pen or a multi-dose vial.
  - S2: Each container contains 4 doses.
  - S3: These products are approved by the FDA in the following strengths.

**L190.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: 10 mg/2.4 mL (4.17 mg/mL) for four 2.5 mg /0.6 mL doses

**L191.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: 20 mg/2.4 mL (8.33 mg/mL) for four 5 mg /0.6 mL doses

**L192.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: 30 mg/2.4 mL (12.5 mg/mL) for four 7.5 mg /0.6 mL doses

**L193.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: 40 mg/2.4 mL (16.7 mg/mL) for four 10 mg /0.6 mL doses

**L194.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: 50 mg/2.4 mL (20.8 mg/mL) for four 12.5 mg /0.6 mL doses

**L195.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: 60 mg/2.4 mL (25 mg/mL) for four 15 mg /0.6 mL doses

## What strengths are Mounjaro pens?

**L198.0** `Simple Sentence` (0.972) → `passthrough`
- original: Mounjaro is available as a single-dose autoinjector pen or single-dose vial in the following strengths:

**L199.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: 2.5 mg/0.5 mL

**L200.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: 5 mg/0.5 mL

**L201.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: 7.5 mg/0.5 mL

**L202.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: 10 mg/0.5 mL

**L203.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: 12.5 mg/0.5 mL

**L204.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: 15 mg/0.5 mL.

**L205.0** `Simple Sentence` (0.547) → `passthrough`
- original: Mounjaro is also available as the

**L206.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Mounjaro KwikPen

**L207.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: , a multi-dose prefilled pen for subcutaneous use.

**L208.0** `Compound Sentence` (0.926) → `decomposed`
- original: Each pen contains 4 fixed doses, and one dose is injected weekly.
  - S1: Each pen contains 4 fixed doses.
  - S2: One dose is injected weekly.

**L209.0** `Simple Sentence` (0.973) → `passthrough`
- original: The single-patient use Mounjaro KwikPen and multi-dose vial are available in the following strengths:

**L210.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: 10 mg/2.4 mL (4.17 mg/mL) for 4 x 2.5 mg/0.6 mL doses

**L211.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: 20 mg/2.4 mL (8.33 mg/mL) for 4 x 5 mg/0.6 mL doses

**L212.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: 30 mg/2.4 mL (12.5 mg/mL) for 4 x 7.5 mg/0.6 mL doses

**L213.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: 40 mg/2.4 mL (16.7 mg/mL) for 4 x 10 mg/0.6 mL doses

**L214.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: 50 mg/2.4 mL (20.8 mg/mL) for 4 x 12.5 mg/0.6 mL doses

**L215.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: 60 mg/2.4 mL (25 mg/mL) for 4 x 15 mg/0.6 mL doses.

## Company

**L218.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Zepbound and Mounjaro

**L219.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Eli Lilly and Company.

**L220.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Marketed by: Lilly USA, LLC, Indianapolis, IN 46285, USA.

## Popular FAQ

**L223.0** `Compound Sentence` (0.588) → `decomposed`
- original: Q: Zepbound vs Mounjaro: Comparison Guide for Weight Loss and Diabetes Treatment A: Zepbound and Mounjaro contain tirzepatide and are made by Eli Lilly.
  - S1: Zepbound and Mounjaro contain tirzepatide.
  - S2: They are made by Eli Lilly.

**L223.1** `Compound Sentence` (0.95) → `decomposed`
- original: They are both administered as a once-weekly subcutaneous injection, but they have different FDA-approved indications and insurance coverage.
- pronoun resolved: Zepbound and Mounjaro are both administered as a once-weekly subcutaneous injection, but Zepbound and Mounjaro have different FDA-approved indications and insurance coverage.
  - edits: “They” → “Zepbound and Mounjaro”; “they” → “Zepbound and Mounjaro”
  - S1: Zepbound and Mounjaro are both administered as a once-weekly subcutaneous injection.
  - S2: Zepbound and Mounjaro have different FDA-approved indications and insurance coverage.

**L224.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Q: Which GLP-1 drug is best for weight loss?

**L224.1** `Complex Sentence` (0.897) → `decomposed`
- original: A: The most effective GLP-1 drug for weight loss currently (as of early 2026) is tirzepatide, marketed under the names Zepbound (for weight loss) and Mounjaro (for diabetes).
  - S1: The most effective GLP-1 drug for weight loss currently is tirzepatide.
  - S2: Tirzepatide is marketed under the name Zepbound for weight loss.
  - S3: Tirzepatide is marketed under the name Mounjaro for diabetes.

**L224.2** `Complex Sentence` (0.928) → `decomposed`
- original: Clinical trials and recent meta-analyses consistently show tirzepatide delivers the most substantial weight reduction among GLP-1 medications, with average losses of up to 22.5% of body weight.
  - S1: Clinical trials and recent meta-analyses consistently show tirzepatide delivers the most substantial weight reduction among GLP-1 medications.
  - S2: The average weight loss is up to 22.5% of body weight.

**L225.0** `Incomplete Sentence` (0.973) → `excluded_incomplete`
- original: Q: How long does it take for Mounjaro (tirzepatide) to start working?

**L225.1** `Compound Sentence` (0.954) → `decomposed`
- original: A: Mounjaro (generic name: tirzepatide) will start to lower your blood sugar levels right away but it can take 8 to 12 weeks to reach your target A1C goal.
- pronoun resolved: A: Mounjaro (generic name: tirzepatide) will start to lower your blood sugar levels right away but Mounjaro can take 8 to 12 weeks to reach your target A1C goal.
  - edits: “it” → “Mounjaro”
  - S1: Mounjaro (generic name: tirzepatide) will start to lower your blood sugar levels right away.
  - S2: Mounjaro can take 8 to 12 weeks to reach your target A1C goal.

**L225.2** `Complex Sentence` (0.904) → `decomposed`
- original: When compared to some other diabetes treatments, studies have shown that it can take 8 weeks to reach an A1C target of ≤7% and 12 weeks to reach an A1C ≤6.5% with Mounjaro.
- pronoun resolved: When compared to some other diabetes treatments, studies have shown that Mounjaro can take 8 weeks to reach an A1C target of ≤7% and 12 weeks to reach an A1C ≤6.5% with Mounjaro.
  - edits: “it” → “Mounjaro”
  - S1: Studies have shown that Mounjaro can take 8 weeks to reach an A1C target of ≤7%.
  - S2: Studies have shown that Mounjaro can take 12 weeks to reach an A1C ≤6.5%.
  - S3: These findings are compared to some other diabetes treatments.

**L225.3** `Simple Sentence` (0.988) → `passthrough`
- original: Significant weight loss can occur as early as 28-weeks.

**L226.0** `Incomplete Sentence` (0.976) → `excluded_incomplete`
- original: Q: Tirzepatide vs semaglutide: How do they compare?
- pronoun resolved: Q: Tirzepatide vs semaglutide: How do Tirzepatide vs semaglutide compare?
  - edits: “they” → “Tirzepatide vs semaglutide”

**L226.1** `Simple Sentence` (0.863) → `passthrough`
- original: A: Semaglutide and tirzepatide are prescription medicines used for type 2 diabetes and long-term weight management.

**L226.2** `Compound Sentence` (0.942) → `decomposed`
- original: Semaglutide products include Ozempic, Rybelsus, Wegovy, and Wegovy HD, while tirzepatide products include Mounjaro and Zepbound.
  - S1: Semaglutide products include Ozempic, Rybelsus, Wegovy, and Wegovy HD.
  - S2: Tirzepatide products include Mounjaro and Zepbound.

**L226.3** `Compound Sentence` (0.592) → `decomposed`
- original: These medicines differ in dosing, approved uses, side effects, and cost, so discuss options with your healthcare provider.
  - S1: These medicines differ in dosing, approved uses, side effects, and cost.
  - S2: You should discuss options with your healthcare provider.

**L227.0** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: Q: How does retatrutide compare to tirzepatide?

**L227.1** `Compound-Complex Sentence` (0.875) → `decomposed`
- original: A: Retatrutide is an investigational triple hormone agonist (GLP-1, GIP, glucagon) showing promising early results for obesity and type 2 diabetes, while tirzepatide is an FDA-approved dual agonist (GLP-1, GIP) available for use today.
  - S1: Retatrutide is an investigational triple hormone agonist.
  - S2: Retatrutide targets GLP-1, GIP, and glucagon.
  - S3: Retatrutide is showing promising early results for obesity.
  - S4: Retatrutide is showing promising early results for type 2 diabetes.
  - S5: Tirzepatide is an FDA-approved dual agonist.
  - S6: Tirzepatide targets GLP-1 and GIP.
  - S7: Tirzepatide is available for use today.

**L228.0** `Incomplete Sentence` (0.926) → `excluded_incomplete`
- original: Q: How much is Zepbound with or without insurance?

**L228.1** `Compound-Complex Sentence` (0.906) → `decomposed`
- original: A: Zepbound may cost $25 for a 1-month or 3-month pen prescription if you have insurance and are eligible for the Savings Card, but without insurance, Zepbound costs start at $299 for a 2.5mg vial or 2.5mg KwikPen, $399 per month for a 5mg dose, and $449 for the higher doses per month.
  - S1: Zepbound may cost $25 for a 1-month or 3-month pen prescription.
  - S2: This low cost applies if you have insurance and are eligible for the Savings Card.
  - S3: Without insurance, Zepbound costs start at $299 for a 2.5mg vial or 2.5mg KwikPen.
  - S4: Without insurance, the cost is $399 per month for a 5mg dose.
  - S5: Without insurance, the cost is $449 per month for the higher doses.

**L229.0** `Incomplete Sentence` (0.578) → `excluded_incomplete`
- original: Q: Can you get tirzepatide from a compounding pharmacy?

**L229.1** `Complex Sentence` (0.841) → `decomposed`
- original: A: Tirzepatide cannot be legally compounded in a U.S. pharmacy at this time because it was removed from the FDA drug shortage list as of October 2, 2024.
- pronoun resolved: A: Tirzepatide cannot be legally compounded in a U.S. pharmacy at this time because Tirzepatide was removed from the FDA drug shortage list as of October 2, 2024.
  - edits: “it” → “Tirzepatide”
  - S1: Tirzepatide cannot be legally compounded in a U.S. pharmacy at this time.
  - S2: This is because Tirzepatide was removed from the FDA drug shortage list.
  - S3: The removal occurred as of October 2, 2024.

**L229.2** `Complex Sentence` (0.92) → `decomposed`
- original: When drugs are in short supply, the FDA can allow temporary compounding of some medicines so that patients can access their treatments.
  - S1: When drugs are in short supply, the FDA can allow temporary compounding of some medicines.
  - S2: This allows patients to access their treatments.

**L229.3** `Complex Sentence` (0.854) → `decomposed`
- original: Tirzepatide is now widely available as a prescription medicine made by Eli Lilly under the brands names Mounjaro (for type 2 diabetes) and Zepbound (for weight loss and sleep apnea).
  - S1: Tirzepatide is now widely available as a prescription medicine.
  - S2: The medicine is made by Eli Lilly.
  - S3: It is sold under the brand name Mounjaro for type 2 diabetes.
  - S4: It is sold under the brand name Zepbound for weight loss and sleep apnea.

**L230.0** `Incomplete Sentence` (0.619) → `excluded_incomplete`
- original: Q: How much weight can I lose on Zepbound?

**L230.1** `Compound-Complex Sentence` (0.888) → `decomposed`
- original: A: The specific amount of weight you might lose from Zepbound is uncertain, but significant weight loss ranging from 35.5 lb (16.1 kg) to 52.0 lb (23.6 kg) was observed in the 72-week SURMOUNT-1 clinical trial, which compared different Zepbound (tirzepatide) doses to a placebo (inactive treatment).
  - S1: The specific amount of weight you might lose from Zepbound is uncertain.
  - S2: Significant weight loss ranging from 35.5 lb (16.1 kg) to 52.0 lb (23.6 kg) was observed in the 72-week SURMOUNT-1 clinical trial.
  - S3: The SURMOUNT-1 clinical trial compared different Zepbound (tirzepatide) doses to a placebo (inactive treatment).

**L231.0** `Incomplete Sentence` (0.846) → `excluded_incomplete`
- original: Q: Is Zepbound covered by insurance?

**L231.1** `Compound Sentence` (0.87) → `decomposed`
- original: A: Most major insurance plans cover Zepbound, but your doctor may need to submit prior authorization before approval.
  - S1: Most major insurance plans cover Zepbound.
  - S2: Your doctor may need to submit prior authorization before approval.

**L231.2** `Incomplete Sentence` (0.951) → `excluded_incomplete`
- original: Check your plan for deductibles, copays, and coinsurance.

**L231.3** `Simple Sentence` (0.436) → `passthrough`
- original: Eligible Medicare Part D beneficiaries may receive Zepbound KwikPen through the temporary Medicare GLP-1 Bridge program for $50 per monthly supply.
