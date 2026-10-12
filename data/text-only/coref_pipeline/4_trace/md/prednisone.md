# Prednisone — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/prednisone.txt` · 274 sentences · 39 changed by pronoun resolution · 426 sentences sent to EDC

## What is prednisone?

**L5.0** `Complex Sentence` (0.671) → `decomposed`
- original: Prednisone is a prescription corticosteroid (steroid) used to reduce inflammation, suppress an overactive immune system, and treat endocrine and metabolic disorders.
  - S1: Prednisone is a prescription corticosteroid.
  - S2: Prednisone is used to reduce inflammation.
  - S3: Prednisone is used to suppress an overactive immune system.
  - S4: Prednisone is used to treat endocrine and metabolic disorders.

**L5.1** `Complex Sentence` (0.849) → `decomposed`
- original: Prednisone is used for a wide range of conditions, including severe allergies, asthma and COPD flare-ups, rheumatoid arthritis and other forms of arthritis, lupus, psoriasis and other skin conditions, ulcerative colitis, Crohn's disease, eye inflammation, some blood disorders, and low adrenal hormone levels.
  - S1: Prednisone is used for a wide range of conditions.
  - S2: These conditions include severe allergies.
  - S3: These conditions include asthma and COPD flare-ups.
  - S4: These conditions include rheumatoid arthritis and other forms of arthritis.
  - S5: These conditions include lupus.
  - S6: These conditions include psoriasis and other skin conditions.
  - S7: These conditions include ulcerative colitis.
  - S8: These conditions include Crohn's disease.
  - S9: These conditions include eye inflammation.
  - S10: These conditions include some blood disorders.
  - S11: These conditions include low adrenal hormone levels.

**L6.0** `Simple Sentence` (0.986) → `passthrough`
- original: Prednisone works by mimicking the effects of glucocorticoid hormones secreted naturally by our adrenal glands.

**L6.1** `Simple Sentence` (0.99) → `passthrough`
- original: Prednisone is a man-made (synthetic) version of these hormones.

**L6.2** `Simple Sentence` (0.988) → `passthrough`
- original: Prednisone is different from steroids taken to build muscle (anabolic steroids).

**L7.0** `Simple Sentence` (0.975) → `passthrough`
- original: Prednisone belongs to the drug class called glucocorticoids, which are a type of corticosteroid.

**L8.0** `Simple Sentence` (0.912) → `passthrough`
- original: Prednisone tablets come in 1 mg, 2.5 mg, 5 mg, 10 mg, 20 mg, and 50 mg strengths.

**L8.1** `Simple Sentence` (0.945) → `passthrough`
- original: Prednisone 20 mg and prednisone 10 mg tablets are the strengths most often used for short courses in adults.

**L8.2** `Compound Sentence` (0.793) → `decomposed`
- original: Prednisone also comes as a delayed-release tablet (Rayos), as an oral liquid, and as a concentrated oral solution (Prednisone Intensol) that is measured with a special dropper.
  - S1: Prednisone also comes as a delayed-release tablet (Rayos).
  - S2: It also comes as an oral liquid.
  - S3: It also comes as a concentrated oral solution (Prednisone Intensol) that is measured with a special dropper.

**L9.0** `Compound Sentence` (0.82) → `decomposed`
- original: Many of the original brands are discontinued; however, generic prednisone is available.
  - S1: Many of the original brands are discontinued.
  - S2: Generic prednisone is available.

## Prednisone side effects

**L12.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Common prednisone side effects:

**L13.0** `Complex Sentence` (0.469) → `decomposed`
- original: The most common prednisone side effects are trouble sleeping, mood changes, increased appetite and weight gain, fluid retention and swelling, increased sweating, acne, thinning skin that bruises easily, slow wound healing, higher blood sugar, indigestion and stomach upset.
  - S1: The most common prednisone side effects are trouble sleeping.
  - S2: The most common prednisone side effects are mood changes.
  - S3: The most common prednisone side effects are increased appetite and weight gain.
  - S4: The most common prednisone side effects are fluid retention and swelling.
  - S5: The most common prednisone side effects are increased sweating.
  - S6: The most common prednisone side effects are acne.
  - S7: The most common prednisone side effects are thinning skin that bruises easily.
  - S8: The most common prednisone side effects are slow wound healing.
  - S9: The most common prednisone side effects are higher blood sugar.
  - S10: The most common prednisone side effects are indigestion and stomach upset.

**L14.0** `Simple Sentence` (0.989) → `passthrough`
- original: Many of these effects are dose related.

**L14.1** `Compound Sentence` (0.962) → `decomposed`
- original: They are more likely on higher doses and on longer courses, and most settle after the medicine is stopped.
- pronoun resolved: These effects are more likely on higher doses and on longer courses, and most settle after Prednisone is stopped.
  - edits: “They” → “These effects”; “the medicine” → “Prednisone”
  - S1: These effects are more likely on higher doses and on longer courses.
  - S2: Most of them settle after Prednisone is stopped.

**L15.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious prednisone side effects:

**L16.0** `Compound Sentence` (0.39) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to prednisone: hives, difficult breathing, or swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to prednisone.
  - S2: Signs of an allergic reaction to prednisone include hives.
  - S3: Signs of an allergic reaction to prednisone include difficult breathing.
  - S4: Signs of an allergic reaction to prednisone include swelling of your face, lips, tongue, or throat.

**L17.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L18.0** `Incomplete Sentence` (0.755) → `excluded_incomplete`
- original: signs of infection, such as fever, chills, sore throat, cough or a wound that is not healing, since prednisone can hide the usual warning signs;

**L19.0** `Incomplete Sentence` (0.949) → `excluded_incomplete`
- original: blurred vision, eye pain or seeing halos around lights, which can be signs of glaucoma (raised pressure in the eye) or cataracts;

**L20.0** `Compound-Complex Sentence` (0.528) → `decomposed`
- original: severe pain in your upper stomach that spreads to your back, with nausea and vomiting, which can be a sign of pancreatitis (inflamed pancreas);
  - S1: You have severe pain in your upper stomach.
  - S2: The pain spreads to your back.
  - S3: You experience nausea.
  - S4: You experience vomiting.
  - S5: These symptoms can be a sign of pancreatitis.
  - S6: Pancreatitis is an inflamed pancreas.

**L21.0** `Incomplete Sentence` (0.917) → `excluded_incomplete`
- original: bloody or black, tarry stools, or vomit that looks like coffee grounds, which can be signs of a bleeding stomach ulcer;

**L22.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: severe depression, unusual excitement, confusion, changes in personality or behavior, or a seizure;

**L23.0** `Incomplete Sentence` (0.979) → `excluded_incomplete`
- original: swelling, rapid weight gain or shortness of breath, which can be signs of fluid retention or heart failure;

**L24.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: signs of low potassium, such as confusion, an uneven heartbeat, extreme thirst, passing more urine than usual, leg discomfort, or muscle weakness;

**L25.0** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: a very high blood pressure reading with severe headache, blurred vision, ringing in your ears, chest pain or shortness of breath;

**L26.0** `Incomplete Sentence` (0.881) → `excluded_incomplete`
- original: sudden pain, swelling or bruising in a tendon, especially at the back of the ankle, since prednisone can weaken tendons and cause the Achilles tendon to rupture;

**L27.0** `Incomplete Sentence` (0.952) → `excluded_incomplete`
- original: new bone pain, especially in a hip, shoulder or knee, which can be a sign of aseptic necrosis (bone tissue that has lost its blood supply); or

**L28.0** `Incomplete Sentence` (0.913) → `excluded_incomplete`
- original: flat, painless spots that are red or purple on light skin, or bluish, brown or black on dark skin, which can be a sign of Kaposi's sarcoma.

**L29.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Prednisone side effects in women:

**L30.0** `Complex Sentence` (0.818) → `decomposed`
- original: Women taking prednisone may notice irregular or missed periods, unwanted facial hair growth, acne and changes in body fat, such as a rounder face and more fat around the neck and waist.
  - S1: Women taking prednisone may notice irregular or missed periods.
  - S2: Women taking prednisone may notice unwanted facial hair growth.
  - S3: Women taking prednisone may notice acne.
  - S4: Women taking prednisone may notice changes in body fat.
  - S5: These changes include a rounder face.
  - S6: These changes include more fat around the neck and waist.

**L30.1** `Compound Sentence` (0.962) → `decomposed`
- original: Long courses of prednisone also raise the risk of osteoporosis (thinning of the bones), and postmenopausal women are already at higher risk.
  - S1: Long courses of prednisone also raise the risk of osteoporosis (thinning of the bones).
  - S2: Postmenopausal women are already at higher risk.

**L30.2** `Incomplete Sentence` (0.96) → `excluded_incomplete`
- original: Ask your doctor whether you need a bone density scan or a calcium and vitamin D supplement.

**L31.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Long-term prednisone side effects:

**L32.0** `Compound-Complex Sentence` (0.738) → `decomposed` · repaired
- original: Taking prednisone for months or years raises the risk of osteoporosis and broken bones, muscle weakness and muscle loss, cataracts and glaucoma, diabetes, high blood pressure, Cushing's syndrome (a set of changes caused by too much steroid, including a rounded face and fat around the trunk), and adrenal suppression, where your body stops making enough of its own steroid hormones.
  - S1: Taking prednisone for months or years raises the risk of osteoporosis.
  - S2: Taking prednisone for months or years raises the risk of broken bones.
  - S3: Taking prednisone for months or years raises the risk of muscle weakness.
  - S4: Taking prednisone for months or years raises the risk of muscle loss.
  - S5: Taking prednisone for months or years raises the risk of cataracts.
  - S6: Taking prednisone for months or years raises the risk of glaucoma.
  - S7: Taking prednisone for months or years raises the risk of diabetes.
  - S8: Taking prednisone for months or years raises the risk of high blood pressure.
  - S9: Taking prednisone for months or years raises the risk of Cushing's syndrome.
  - S10: Cushing's syndrome is a set of changes caused by too much steroid.
  - S11: Cushing's syndrome includes a rounded face.
  - S12: Cushing's syndrome includes fat around the trunk.
  - S13: Taking prednisone for months or years raises the risk of adrenal suppression.
  - S14: Adrenal suppression is where your body stops making enough of its own steroid hormones.

**L33.0** `Simple Sentence` (0.987) → `passthrough`
- original: Children who take prednisone for a long time may grow more slowly.

**L33.1** `Simple Sentence` (0.976) → `passthrough`
- original: Your child's doctor should check their growth at regular visits.
- pronoun resolved: Your child's doctor should check Children's growth at regular visits.
  - edits: “their” → “Children's”

**L34.0** `Compound Sentence` (0.545) → `decomposed`
- original: This is not a complete list of side effects, and others may occur.
  - S1: This is not a complete list of side effects.
  - S2: Others may occur.

**L34.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L34.2** `Simple Sentence` (0.97) → `passthrough`
- original: You may report side effects to the FDA at 1-800-FDA-1088.

## Warnings

**L37.0** `Simple Sentence` (0.622) → `passthrough`
- original: Do not take prednisone if you have a systemic fungal infection, which is a fungal infection that has spread through your body.

**L38.0** `Simple Sentence` (0.99) → `passthrough`
- original: Prednisone weakens your immune system.

**L38.1** `Compound Sentence` (0.811) → `decomposed`
- original: This makes it easier to get an infection; an existing infection may become worse and can reactivate an old infection, such as tuberculosis or hepatitis B.
  - S1: This makes it easier to get an infection.
  - S2: An existing infection may become worse.
  - S3: An existing infection can reactivate an old infection, such as tuberculosis or hepatitis B.

**L38.2** `Compound Sentence` (0.886) → `decomposed`
- original: It can also hide the usual signs of infection, so an infection may be advanced before you notice it.
- pronoun resolved: It can also hide the usual signs of infection, so an infection may be advanced before you notice infection.
  - edits: “it.” → “infection.”
  - S1: It can also hide the usual signs of infection.
  - S2: An infection may be advanced before you notice it.

**L38.3** `Incomplete Sentence` (0.908) → `excluded_incomplete`
- original: Tell your doctor about any illness or infection you have had in the past few weeks.

**L39.0** `Incomplete Sentence` (0.922) → `excluded_incomplete`
- original: Stay away from people who are sick.

**L39.1** `Simple Sentence` (0.988) → `passthrough`
- original: Chickenpox and measles can be serious or even fatal in someone taking a steroid.

**L39.2** `Incomplete Sentence` (0.756) → `excluded_incomplete`
- original: Call your doctor straight away if you are exposed to either one.

**L40.0** `Incomplete Sentence` (0.737) → `excluded_incomplete`
- original: Do not have a live vaccine while you are taking prednisone unless your doctor says it is safe.

**L41.0** `Simple Sentence` (0.522) → `passthrough`
- original: Do not stop taking prednisone suddenly after more than a few days of treatment.

**L41.1** `Simple Sentence` (0.972) → `passthrough`
- original: Your body needs time to start making its own steroid hormones again.

**L41.2** `Simple Sentence` (0.972) → `passthrough`
- original: Your doctor will lower your dose in steps.

**L42.0** `Compound Sentence` (0.319) → `decomposed`
- original: Call your doctor at once if you have shortness of breath, severe pain in your upper stomach, bloody or black stools, severe depression, changes in personality or behavior, vision problems, or eye pain.
  - S1: Call your doctor at once if you have shortness of breath.
  - S2: Call your doctor at once if you have severe pain in your upper stomach.
  - S3: Call your doctor at once if you have bloody or black stools.
  - S4: Call your doctor at once if you have severe depression.
  - S5: Call your doctor at once if you have changes in personality or behavior.
  - S6: Call your doctor at once if you have vision problems.
  - S7: Call your doctor at once if you have eye pain.

## Before taking this medicine

**L45.0** `Compound Sentence` (0.564) → `decomposed`
- original: You should not use prednisone if you are allergic to it, or if you have a systemic fungal infection.
- pronoun resolved: You should not use prednisone if you are allergic to prednisone, or if you have a systemic fungal infection.
  - edits: “it,” → “prednisone,”
  - S1: You should not use prednisone if you are allergic to prednisone.
  - S2: You should not use prednisone if you have a systemic fungal infection.

**L46.0** `Simple Sentence` (0.785) → `passthrough`
- original: To make sure prednisone is safe for you, tell your doctor if you have or have ever had:

**L47.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: an infection of any kind, including tuberculosis, hepatitis B, herpes infection of the eye, or a fungal infection;

**L48.0** `Compound-Complex Sentence` (0.341) → `decomposed`
- original: diarrhea that has no clear cause, or time spent in the tropics, since prednisone can wake up a parasite infection such as amebiasis or threadworm;
  - S1: Diarrhea has no clear cause.
  - S2: Time is spent in the tropics.
  - S3: Prednisone can wake up a parasite infection.
  - S4: The parasite infection is amebiasis.
  - S5: The parasite infection is threadworm.

**L49.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: malaria, especially cerebral malaria (malaria affecting the brain);

**L50.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: liver disease, such as cirrhosis;

**L51.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: kidney disease;

**L52.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: heart disease, heart failure, high blood pressure or low potassium levels;

**L53.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: an underactive thyroid;

**L54.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: diabetes;

**L55.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: osteoporosis;

**L56.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: glaucoma or cataracts;

**L57.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: stomach ulcers, ulcerative colitis, diverticulitis, or a history of bleeding in the stomach or bowel;

**L58.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: myasthenia gravis (a condition that causes muscle weakness); or

**L59.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: depression, mood swings or another mental health condition.

**L60.0** `Simple Sentence` (0.991) → `passthrough`
- original: Long-term steroid use can cause bone loss.

**L60.1** `Compound Sentence` (0.897) → `decomposed`
- original: Your risk is higher if you smoke, if you do not exercise, if you do not get enough calcium or vitamin D, or if osteoporosis runs in your family.
  - S1: Your risk is higher if you smoke.
  - S2: Your risk is higher if you do not exercise.
  - S3: Your risk is higher if you do not get enough calcium or vitamin D.
  - S4: Your risk is higher if osteoporosis runs in your family.

**L60.2** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: Talk with your doctor about protecting your bones.

**L61.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Pregnancy:

**L62.0** `Simple Sentence` (0.99) → `passthrough`
- original: Prednisone crosses the placenta.

**L62.1** `Compound Sentence` (0.864) → `decomposed`
- original: Taking it in the first trimester may raise the risk of birth defects, and taking higher doses later in pregnancy may affect the baby's growth and their adrenal glands.
- pronoun resolved: Taking Prednisone in the first trimester may raise the risk of birth defects, and taking higher doses later in pregnancy may affect the baby's growth and baby's adrenal glands.
  - edits: “it” → “Prednisone”; “their” → “baby's”
  - S1: Taking Prednisone in the first trimester may raise the risk of birth defects.
  - S2: Taking higher doses later in pregnancy may affect the baby's growth and baby's adrenal glands.

**L62.2** `Incomplete Sentence` (0.915) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or plan to become pregnant.

**L62.3** `Compound Sentence` (0.924) → `decomposed`
- original: Some conditions still need steroid treatment during pregnancy, so this is a decision to make with your doctor rather than stopping on your own.
  - S1: Some conditions still need steroid treatment during pregnancy.
  - S2: This is a decision to make with your doctor rather than stopping on your own.

**L63.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Breastfeeding:

**L64.0** `Simple Sentence` (0.989) → `passthrough`
- original: Prednisone passes into breast milk in small amounts.

**L64.1** `Incomplete Sentence` (0.407) → `excluded_incomplete`
- original: Tell your doctor if you are breastfeeding so you can talk through the dose and the timing of feeds.

**L65.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Children:

**L66.0** `Compound Sentence` (0.953) → `decomposed`
- original: Prednisone is used in children, but long courses can slow growth and affect bone development.
  - S1: Prednisone is used in children.
  - S2: Long courses can slow growth and affect bone development.

**L66.1** `Compound Sentence` (0.947) → `decomposed`
- original: The dose should not be higher than prescribed, and your child should be monitored during treatment.
  - S1: The dose should not be higher than prescribed.
  - S2: Your child should be monitored during treatment.

**L67.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Older adults:

**L68.0** `Compound Sentence` (0.913) → `decomposed`
- original: Older adults are more likely to have liver, kidney, or heart problems that affect how prednisone is handled, and are more likely to already have osteoporosis, diabetes, or high blood pressure.
  - S1: Older adults are more likely to have liver, kidney, or heart problems that affect how prednisone is handled.
  - S2: Older adults are more likely to already have osteoporosis, diabetes, or high blood pressure.

**L68.1** `Simple Sentence` (0.972) → `passthrough`
- original: A lower dose may be needed.

## How should I take prednisone?

**L71.0** `Incomplete Sentence` (0.902) → `excluded_incomplete`
- original: Take prednisone exactly as prescribed, with food or milk to protect your stomach.

**L71.1** `Simple Sentence` (0.96) → `passthrough`
- original: Your doctor will often start you on a higher dose and then lower it.

**L71.2** `Simple Sentence` (0.679) → `passthrough`
- original: Do not change your dose or stop the medicine without advice.
- pronoun resolved: Do not change your dose or stop prednisone without advice.
  - edits: “the medicine” → “prednisone”

**L72.0** `Incomplete Sentence` (0.904) → `excluded_incomplete`
- original: Take your dose in the morning if your doctor tells you to.

**L72.1** `Compound Sentence` (0.947) → `decomposed`
- original: Your adrenal glands are most active between 2 am and 8 am, and taking a steroid at that time interferes with them the least.
- pronoun resolved: Your adrenal glands are most active between 2 am and 8 am, and taking a steroid at that time interferes with adrenal glands the least.
  - edits: “them” → “adrenal glands”
  - S1: Your adrenal glands are most active between 2 am and 8 am.
  - S2: Taking a steroid at that time interferes with adrenal glands the least.

**L72.2** `Compound Sentence` (0.898) → `decomposed`
- original: A morning dose may also help you sleep better, though that is a separate benefit.
  - S1: A morning dose may also help you sleep better.
  - S2: That is a separate benefit.

**L73.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Swallow delayed-release tablets whole.

**L73.1** `Incomplete Sentence` (0.962) → `excluded_incomplete`
- original: Do not crush, break, or chew them.

**L74.0** `Incomplete Sentence` (0.959) → `excluded_incomplete`
- original: Measure liquid prednisone with a marked oral syringe, dosing spoon or medicine cup, not a kitchen spoon.

**L74.1** `Incomplete Sentence` (0.973) → `excluded_incomplete`
- original: Use the dropper that comes with the concentrated solution.

**L75.0** `Simple Sentence` (0.926) → `passthrough`
- original: You may mix the concentrated solution with juice or a soft food such as applesauce.

**L76.0** `Incomplete Sentence` (0.6) → `excluded_incomplete`
- original: Tell your doctor if you have a serious illness, a fever, an infection, surgery, or a medical emergency.

**L76.1** `Simple Sentence` (0.948) → `passthrough`
- original: You may need a higher dose for a short time.

**L77.0** `Simple Sentence` (0.815) → `passthrough`
- original: You may need regular blood tests, blood pressure checks and eye checks during long-term treatment.

**L78.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Wear a medical alert tag or carry a card saying you take a steroid.

**L79.0** `Incomplete Sentence` (0.966) → `excluded_incomplete`
- original: Store prednisone at room temperature, away from moisture and heat.

**L79.1** `Incomplete Sentence` (0.945) → `excluded_incomplete`
- original: Throw away any unused concentrated solution 90 days after you first open the bottle.

## What is the usual prednisone dosage?

**L82.0** `Complex Sentence` (0.499) → `decomposed`
- original: The usual starting dose of prednisone for adults is 5 mg to 60 mg per day, depending on the condition being treated and how severe it is.
- pronoun resolved: The usual starting dose of prednisone for adults is 5 mg to 60 mg per day, depending on the condition being treated and how severe condition is.
  - edits: “it” → “condition”
  - S1: The usual starting dose of prednisone for adults is 5 mg to 60 mg per day.
  - S2: The dose depends on the condition being treated.
  - S3: The dose also depends on how severe the condition is.

**L83.0** `Simple Sentence` (0.977) → `passthrough`
- original: There is no single standard dose.

**L83.1** `Compound Sentence` (0.755) → `decomposed`
- original: Your doctor will decide on a starting dose, then lower it in small steps to the smallest dose that still controls your condition.
- pronoun resolved: Your doctor will decide on a starting dose, then lower dose in small steps to the smallest dose that still controls your condition.
  - edits: “it” → “dose”
  - S1: Your doctor will decide on a starting dose.
  - S2: Then, the doctor will lower the dose in small steps.
  - S3: The goal is to reach the smallest dose that still controls your condition.

**L84.0** `Compound Sentence` (0.94) → `decomposed`
- original: Doses for children are based on the condition rather than strictly on age or weight, and must be set by a doctor.
  - S1: Doses for children are based on the condition rather than strictly on age or weight.
  - S2: They must be set by a doctor.

**L85.0** `Simple Sentence` (0.469) → `passthrough`
- original: Short courses of prednisone for problems such as an asthma flare, gout, or a bad allergic reaction are often given as a short fixed-dose course for a few days.

**L85.1** `Simple Sentence` (0.968) → `passthrough`
- original: A dose pack steps the dose down day by day over about six days.

**L85.2** `Incomplete Sentence` (0.867) → `excluded_incomplete`
- original: Follow the instructions on your pack exactly, since the number of tablets changes each day.

**L86.0** `Simple Sentence` (0.964) → `passthrough`
- original: Prednisone treatment takes one of two shapes.

**L86.1** `Complex Sentence` (0.743) → `decomposed`
- original: Some people take it for a few days or weeks for a problem that will settle, such as an asthma flare or a severe allergic reaction.
- pronoun resolved: Some people take Prednisone for a few days or weeks for a problem that will settle, such as an asthma flare or a severe allergic reaction.
  - edits: “it” → “Prednisone”
  - S1: Some people take Prednisone for a few days or weeks.
  - S2: They take it for a problem that will settle.
  - S3: Examples of such problems include an asthma flare or a severe allergic reaction.

**L86.2** `Simple Sentence` (0.661) → `passthrough`
- original: Others take it every day for months or years for an ongoing condition such as rheumatoid arthritis or ulcerative colitis.
- pronoun resolved: Others take Prednisone every day for months or years for an ongoing condition such as rheumatoid arthritis or ulcerative colitis.
  - edits: “it” → “Prednisone”

**L87.0** `Simple Sentence` (0.903) → `passthrough`
- original: If you take prednisone long term, your doctor will settle you on a maintenance dose.

**L87.1** `Compound Sentence` (0.956) → `decomposed`
- original: This is the lowest daily dose that still keeps your condition under control, and it is reached by lowering the dose in small steps rather than all at once.
- pronoun resolved: Maintenance dose is the lowest daily dose that still keeps your condition under control, and maintenance dose is reached by lowering the dose in small steps rather than all at once.
  - edits: “This” → “Maintenance dose”; “it” → “maintenance dose”
  - S1: Maintenance dose is the lowest daily dose that still keeps your condition under control.
  - S2: Maintenance dose is reached by lowering the dose in small steps rather than all at once.

**L87.2** `Simple Sentence` (0.977) → `passthrough`
- original: Your maintenance dose is not fixed.

**L87.3** `Compound Sentence` (0.568) → `decomposed`
- original: It may need to go up for a time if your condition flares, or if you have surgery, a fever, an infection, or another serious illness, and it may come down again afterwards.
- pronoun resolved: Maintenance dose may need to go up for a time if your condition flares, or if you have surgery, a fever, an infection, or another serious illness, and maintenance dose may come down again afterwards.
  - edits: “It” → “Maintenance dose”; “it” → “maintenance dose”
  - S1: Maintenance dose may need to go up for a time if your condition flares.
  - S2: It may need to go up for a time if you have surgery, a fever, an infection, or another serious illness.
  - S3: Maintenance dose may come down again afterwards.

**L87.4** `Incomplete Sentence` (0.926) → `excluded_incomplete`
- original: Do not adjust it yourself.
- pronoun resolved: Do not adjust dose yourself.
  - edits: “it” → “dose”

**L88.0** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: How do you stop taking prednisone safely?

**L88.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L89.0** `Simple Sentence` (0.568) → `passthrough`
- original: If you have taken prednisone for more than a few days, your doctor will taper the dose rather than stopping it all at once.
- pronoun resolved: If you have taken prednisone for more than a few days, your doctor will taper the dose rather than stopping dose all at once.
  - edits: “it” → “dose”

**L89.1** `Compound Sentence` (0.961) → `decomposed`
- original: While you are taking a steroid, your adrenal glands slow down their own hormone production, and they need time to start up again.
- pronoun resolved: While you are taking a steroid, your adrenal glands slow down their own hormone production, and adrenal glands need time to start up again.
  - edits: “they” → “adrenal glands”
  - S1: While you are taking a steroid, your adrenal glands slow down their own hormone production.
  - S2: Adrenal glands need time to start up again.

**L89.2** `Simple Sentence` (0.484) → `passthrough`
- original: Stopping suddenly can cause extreme tiredness, weakness, body aches, upset stomach, weight loss, a craving for salt, and changes in skin color.

**L89.3** `Incomplete Sentence` (0.897) → `excluded_incomplete`
- original: Call your doctor if you feel unwell while your dose is being lowered or after you finish.

**L90.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Prednisone formulations:

**L91.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Prednisone 1 mg tablets

**L92.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Prednisone 2.5 mg tablets

**L93.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Prednisone 5 mg tablets

**L94.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Prednisone 10 mg tablets

**L95.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Prednisone 20 mg tablets

**L96.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Prednisone 50 mg tablets

**L97.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Prednisone Oral Solution 5 mg per 5 mL

**L98.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Prednisone Intensol™ Oral Solution (Concentrate) 5 mg per mL

**L99.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Prednisone delayed-release tablets (Rayos) 1 mg, 2 mg, and 5 mg

## What happens if I miss a dose?

**L102.0** `Incomplete Sentence` (0.926) → `excluded_incomplete`
- original: Take the missed dose as soon as you remember.

**L102.1** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Skip it if it is almost time for your next dose.
- pronoun resolved: Skip dose if it is almost time for your next dose.
  - edits: “it” → “dose”

**L102.2** `Incomplete Sentence` (0.759) → `excluded_incomplete`
- original: Do not take extra medicine to make up a missed dose.

**L102.3** `Complex Sentence` (0.507) → `decomposed`
- original: If you take prednisone once every other day, or you are following a taper, call your doctor or pharmacist for advice rather than guessing.
  - S1: If you take prednisone once every other day, or you are following a taper, call your doctor or pharmacist for advice.
  - S2: Do not guess.

## What happens if I overdose?

**L105.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L106.0** `Simple Sentence` (0.977) → `passthrough`
- original: A single large dose of prednisone is not likely to cause life-threatening symptoms.

**L106.1** `Complex Sentence` (0.76) → `decomposed`
- original: The bigger risk comes from taking high doses over a long time, which can cause thinning skin, easy bruising, changes in the shape or location of body fat, acne, extra facial hair, irregular periods, and loss of interest in sex.
  - S1: The bigger risk comes from taking high doses over a long time.
  - S2: This can cause thinning skin.
  - S3: This can cause easy bruising.
  - S4: This can cause changes in the shape or location of body fat.
  - S5: This can cause acne.
  - S6: This can cause extra facial hair.
  - S7: This can cause irregular periods.
  - S8: This can cause loss of interest in sex.

## What should I avoid while taking prednisone?

**L109.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Avoid being near people who are sick or have an infection.

**L109.1** `Incomplete Sentence` (0.869) → `excluded_incomplete`
- original: Call your doctor if you are exposed to chickenpox or measles.

**L110.0** `Simple Sentence` (0.34) → `passthrough`
- original: Do not have a live vaccine, such as MMR, chickenpox, rotavirus, yellow fever, oral typhoid, or the nasal flu vaccine, without your doctor's approval.

**L110.1** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Avoid close contact with someone who has just had an oral or nasal live vaccine.

**L111.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Limit alcohol.

**L111.1** `Compound Sentence` (0.91) → `decomposed`
- original: Both alcohol and prednisone irritate the stomach lining, so together they raise the risk of stomach bleeding.
  - S1: Both alcohol and prednisone irritate the stomach lining.
  - S2: Together, they raise the risk of stomach bleeding.

**L112.0** `Complex Sentence` (0.298) → `decomposed`
- original: Be careful with NSAIDs such as ibuprofen, naproxen, and aspirin, since taking them with prednisone raises the risk of stomach bleeding.
- pronoun resolved: Be careful with NSAIDs such as ibuprofen, naproxen, and aspirin, since taking NSAIDs with prednisone raises the risk of stomach bleeding.
  - edits: “them” → “NSAIDs”
  - S1: Be careful with NSAIDs such as ibuprofen, naproxen, and aspirin.
  - S2: Taking NSAIDs with prednisone raises the risk of stomach bleeding.

**L113.0** `Compound Sentence` (0.46) → `decomposed`
- original: Your doctor may ask you to cut back on salt, since prednisone makes your body hold onto fluid.
  - S1: Your doctor may ask you to cut back on salt.
  - S2: Prednisone makes your body hold onto fluid.

## What other drugs will affect prednisone?

**L116.0** `Simple Sentence` (0.991) → `passthrough`
- original: Many medicines interact with prednisone.

**L116.1** `Compound Sentence` (0.957) → `decomposed`
- original: Some change how much prednisone is in your body, and others add to its side effects.
- pronoun resolved: Some change how much prednisone is in your body, and others add to prednisone's side effects.
  - edits: “its” → “prednisone's”
  - S1: Some change how much prednisone is in your body.
  - S2: Others add to prednisone's side effects.

**L116.2** `Incomplete Sentence` (0.877) → `excluded_incomplete`
- original: Tell your doctor about every medicine you take, including anything you start or stop during treatment.

**L116.3** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Be especially careful with:

**L117.0** `Incomplete Sentence` (0.964) → `excluded_incomplete`
- original: medicines that raise prednisone levels, such as ketoconazole, itraconazole, posaconazole, voriconazole, clarithromycin, and some HIV and hepatitis C medicines;

**L118.0** `Incomplete Sentence` (0.943) → `excluded_incomplete`
- original: medicines that lower prednisone levels and can make it work less well, such as rifampin, rifabutin, rifapentine, carbamazepine, phenytoin, phenobarbital, primidone and St. John's wort;
- pronoun resolved: medicines that lower prednisone levels and can make prednisone work less well, such as rifampin, rifabutin, rifapentine, carbamazepine, phenytoin, phenobarbital, primidone and St. John's wort;
  - edits: “it” → “prednisone”

**L119.0** `Incomplete Sentence` (0.966) → `excluded_incomplete`
- original: NSAIDs and aspirin, which raise the risk of stomach ulcers and bleeding;

**L120.0** `Incomplete Sentence` (0.763) → `excluded_incomplete`
- original: blood thinners such as warfarin, since prednisone can change how your blood clots and you may need extra monitoring;

**L121.0** `Incomplete Sentence` (0.96) → `excluded_incomplete`
- original: insulin and diabetes tablets, since prednisone raises blood sugar and your doses may need to go up;

**L122.0** `Incomplete Sentence` (0.953) → `excluded_incomplete`
- original: diuretics (water pills) and amphotericin B, which can lower potassium further;

**L123.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: digoxin, which is more likely to cause problems if your potassium is low;

**L124.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: live vaccines, which should usually be avoided;

**L125.0** `Incomplete Sentence` (0.933) → `excluded_incomplete`
- original: cyclosporine, which interacts in both directions and raises the risk of seizures; and

**L126.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: birth control pills and hormone therapy.

**L127.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L127.1** `Simple Sentence` (0.955) → `passthrough`
- original: Many other prescription medicines, over-the-counter products, vitamins and herbal products can interact with prednisone.

**L127.2** `Incomplete Sentence` (0.956) → `excluded_incomplete`
- original: Give a list of all your medicines to any healthcare provider who treats you.

## Prednisone FAQs

**L130.0** `Incomplete Sentence` (0.972) → `excluded_incomplete`
- original: Is prednisone a steroid?

**L130.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L131.0** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Yes.

**L131.1** `Simple Sentence` (0.984) → `passthrough`
- original: Prednisone is a corticosteroid, also called a glucocorticoid.

**L131.2** `Compound Sentence` (0.971) → `decomposed`
- original: Corticosteroids are copies of hormones your adrenal glands make naturally, and they work by lowering inflammation and immune activity.
  - S1: Corticosteroids are copies of hormones your adrenal glands make naturally.
  - S2: They work by lowering inflammation and immune activity.

**L131.3** `Simple Sentence` (0.965) → `passthrough`
- original: They are not the same as the anabolic steroids some athletes misuse to build muscle.

**L132.0** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: How long does it take for prednisone to work?

**L132.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L133.0** `Compound Sentence` (0.95) → `decomposed`
- original: Prednisone starts to be absorbed within about an hour, and many people notice a difference in symptoms such as swelling, pain, or wheezing within a few hours to a day.
  - S1: Prednisone starts to be absorbed within about an hour.
  - S2: Many people notice a difference in symptoms such as swelling, pain, or wheezing within a few hours to a day.

**L133.1** `Simple Sentence` (0.983) → `passthrough`
- original: Some conditions take several days or longer to respond.

**L133.2** `Compound Sentence` (0.87) → `decomposed`
- original: Delayed-release tablets are designed to release the medicine about four hours after you take them, so the timing of your dose matters.
  - S1: Delayed-release tablets are designed to release the medicine about four hours after you take them.
  - S2: Therefore, the timing of your dose matters.

**L134.0** `Incomplete Sentence` (0.972) → `excluded_incomplete`
- original: How long does prednisone stay in your system?

**L134.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L135.0** `Complex Sentence` (0.54) → `decomposed`
- original: Prednisone and prednisolone have a half-life of about 2 to 3 hours, which means half of a dose leaves your blood in that time.
  - S1: Prednisone and prednisolone have a half-life of about 2 to 3 hours.
  - S2: This means half of a dose leaves your blood in that time.

**L135.1** `Simple Sentence` (0.977) → `passthrough`
- original: Most of a single dose is out of your bloodstream within about a day.

**L136.0** `Simple Sentence` (0.958) → `passthrough`
- original: The effect lasts longer than the drug itself.

**L136.1** `Complex Sentence` (0.757) → `decomposed`
- original: A single dose of prednisone quiets your own adrenal glands for about one and a quarter to one and a half days, which is why prednisone is described as short-acting compared with steroids such as dexamethasone.
  - S1: A single dose of prednisone quiets your own adrenal glands.
  - S2: This effect lasts for about one and a quarter to one and a half days.
  - S3: This is why prednisone is described as short-acting.
  - S4: It is short-acting compared with steroids such as dexamethasone.

**L136.2** `Complex Sentence` (0.79) → `decomposed`
- original: This is also why a course of prednisone can affect your blood sugar, your sleep, and your energy for longer than the drug is measurable in your blood.
  - S1: A course of prednisone can affect your blood sugar, your sleep, and your energy.
  - S2: This effect can last longer than the drug is measurable in your blood.

**L137.0** `Incomplete Sentence` (0.96) → `excluded_incomplete`
- original: Why has my doctor prescribed prednisone every other day?

**L137.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L138.0** `Simple Sentence` (0.977) → `passthrough`
- original: Alternate day dosing means taking twice your usual daily dose every other morning instead of a dose every day.

**L138.1** `Simple Sentence` (0.99) → `passthrough`
- original: It is used for people who need steroid treatment for a long time.
- pronoun resolved: Prednisone is used for people who need steroid treatment for a long time.
  - edits: “It” → “Prednisone”

**L138.2** `Complex Sentence` (0.898) → `decomposed`
- original: Giving your body a day off from the steroid lets your adrenal glands recover between doses, which reduces the risk of adrenal suppression, Cushing's syndrome, withdrawal symptoms, and slowed growth in children.
  - S1: Giving your body a day off from the steroid lets your adrenal glands recover between doses.
  - S2: This recovery reduces the risk of adrenal suppression, Cushing's syndrome, withdrawal symptoms, and slowed growth in children.

**L139.0** `Compound Sentence` (0.558) → `decomposed`
- original: The trade-off is that your symptoms may flare a little late in the day you do not take it.
  - S1: The trade-off is that your symptoms may flare a little late in the day.
  - S2: This happens if you do not take it.

**L139.1** `Compound Sentence` (0.364) → `decomposed`
- original: Tell your doctor if this happens, since other treatment can often be added for that gap.
  - S1: Tell your doctor if this happens.
  - S2: Other treatment can often be added for that gap.

**L139.2** `Compound Sentence` (0.758) → `decomposed`
- original: Do not switch yourself to an every other day schedule, and do not double up on a day you were not meant to take a dose.
  - S1: Do not switch yourself to an every other day schedule.
  - S2: Do not double up on a day you were not meant to take a dose.

**L140.0** `Incomplete Sentence` (0.955) → `excluded_incomplete`
- original: What is the difference between prednisone and prednisolone?

**L140.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L141.0** `Compound Sentence` (0.938) → `decomposed`
- original: Prednisone has to be converted by your liver into prednisolone before it can work, while prednisolone is already in the active form.
- pronoun resolved: Prednisone has to be converted by your liver into prednisolone before Prednisone can work, while prednisolone is already in the active form.
  - edits: “it” → “Prednisone”
  - S1: Prednisone has to be converted by your liver into prednisolone before it can work.
  - S2: Prednisolone is already in the active form.

**L141.1** `Simple Sentence` (0.985) → `passthrough`
- original: For most people the two work in a very similar way at equivalent doses.

**L141.2** `Compound Sentence` (0.661) → `decomposed`
- original: Prednisolone is often chosen for people with significant liver disease, and for children, because it comes in liquid forms that are easier to dose.
- pronoun resolved: Prednisolone is often chosen for people with significant liver disease, and for children, because Prednisolone comes in liquid forms that are easier to dose.
  - edits: “it” → “Prednisolone”
  - S1: Prednisolone is often chosen for people with significant liver disease.
  - S2: It is also chosen for children because Prednisolone comes in liquid forms that are easier to dose.

**L142.0** `Incomplete Sentence` (0.947) → `excluded_incomplete`
- original: Does prednisone cause weight gain?

**L142.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L143.0** `Simple Sentence` (0.991) → `passthrough`
- original: Weight gain is a common side effect of prednisone.

**L143.1** `Simple Sentence` (0.947) → `passthrough`
- original: It happens for two reasons.
- pronoun resolved: Weight gain happens for two reasons.
  - edits: “It” → “Weight gain”

**L143.2** `Compound-Complex Sentence` (0.635) → `decomposed`
- original: Prednisone makes your body hold onto salt and water, which adds weight quickly in the first days or weeks, and it increases appetite, which adds body fat over longer courses.
- pronoun resolved: Prednisone makes your body hold onto salt and water, which adds weight quickly in the first days or weeks, and prednisone increases appetite, which adds body fat over longer courses.
  - edits: “it” → “prednisone”
  - S1: Prednisone makes your body hold onto salt and water.
  - S2: Holding onto salt and water adds weight quickly in the first days or weeks.
  - S3: Prednisone increases appetite.
  - S4: Increased appetite adds body fat over longer courses.

**L143.3** `Simple Sentence` (0.985) → `passthrough`
- original: It also moves fat toward the face, neck, upper back and waist.
- pronoun resolved: Prednisone also moves fat toward the face, neck, upper back and waist.
  - edits: “It” → “Prednisone”

**L143.4** `Compound Sentence` (0.932) → `decomposed`
- original: Weight from fluid usually goes once you stop, but weight from extra eating takes longer to shift.
  - S1: Weight from fluid usually goes once you stop.
  - S2: Weight from extra eating takes longer to shift.

**L144.0** `Incomplete Sentence` (0.972) → `excluded_incomplete`
- original: Can you drink alcohol while taking prednisone?

**L144.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L145.0** `Compound Sentence` (0.945) → `decomposed`
- original: There is no direct interaction between alcohol and prednisone, but drinking is best kept to a minimum.
  - S1: There is no direct interaction between alcohol and prednisone.
  - S2: Drinking is best kept to a minimum.

**L145.1** `Compound Sentence` (0.939) → `decomposed`
- original: Both irritate the stomach lining, so together they raise the risk of stomach ulcers and bleeding.
- pronoun resolved: Both irritate the stomach lining, so together Alcohol and prednisone raise the risk of stomach ulcers and bleeding.
  - edits: “they” → “Alcohol and prednisone”
  - S1: Alcohol and prednisone both irritate the stomach lining.
  - S2: Together, they raise the risk of stomach ulcers and bleeding.

**L145.2** `Compound Sentence` (0.96) → `decomposed`
- original: Alcohol also raises blood sugar and weakens bones, and prednisone does both of these too.
  - S1: Alcohol also raises blood sugar and weakens bones.
  - S2: Prednisone does both of these too.

**L145.3** `Incomplete Sentence` (0.906) → `excluded_incomplete`
- original: Ask your doctor what is reasonable for you, especially if you are on a long course.

**L146.0** `Incomplete Sentence` (0.849) → `excluded_incomplete`
- original: Can you take ibuprofen with prednisone?

**L146.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L147.0** `Simple Sentence` (0.961) → `passthrough`
- original: It is usually best to avoid ibuprofen while you are taking prednisone.

**L147.1** `Compound Sentence` (0.958) → `decomposed`
- original: Ibuprofen is an NSAID, and taking an NSAID with a steroid raises the risk of stomach ulcers and bleeding.
  - S1: Ibuprofen is an NSAID.
  - S2: Taking an NSAID with a steroid raises the risk of stomach ulcers and bleeding.

**L147.2** `Simple Sentence` (0.641) → `passthrough`
- original: The same applies to naproxen, diclofenac, and regular doses of aspirin.

**L147.3** `Simple Sentence` (0.796) → `passthrough`
- original: If you need a painkiller, ask your doctor or pharmacist first.

**L148.0** `Incomplete Sentence` (0.853) → `excluded_incomplete`
- original: Can you take Tylenol with prednisone?

**L148.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L149.0** `Compound-Complex Sentence` (0.624) → `decomposed`
- original: Acetaminophen (Tylenol) does not interact with prednisone and does not irritate the stomach, so it is generally the preferred choice for pain or fever while you are taking prednisone.
- pronoun resolved: Acetaminophen (Tylenol) does not interact with prednisone and does not irritate the stomach, so Acetaminophen is generally the preferred choice for pain or fever while you are taking prednisone.
  - edits: “it” → “Acetaminophen”
  - S1: Acetaminophen does not interact with prednisone.
  - S2: Acetaminophen does not irritate the stomach.
  - S3: Prednisone is a medication.
  - S4: Acetaminophen is generally the preferred choice for pain or fever while taking prednisone.

**L149.1** `Incomplete Sentence` (0.481) → `excluded_incomplete`
- original: Stay within the recommended daily limit on the packet and check whether any other product you take already contains acetaminophen.

**L150.0** `Incomplete Sentence` (0.976) → `excluded_incomplete`
- original: Why does prednisone keep me awake?

**L150.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L151.0** `Simple Sentence` (0.488) → `passthrough`
- original: Prednisone acts like your body's stress hormone, which naturally peaks in the morning to help you wake up.

**L151.1** `Simple Sentence` (0.931) → `passthrough`
- original: Taking it, especially later in the day, can leave you feeling wired, restless or unable to sleep.
- pronoun resolved: Taking prednisone, especially later in the day, can leave you feeling wired, restless or unable to sleep.
  - edits: “it,” → “prednisone,”

**L151.2** `Simple Sentence` (0.971) → `passthrough`
- original: Taking your dose in the morning often helps.

**L151.3** `Incomplete Sentence` (0.865) → `excluded_incomplete`
- original: Talk to your doctor before changing when you take it.
- pronoun resolved: Talk to your doctor before changing when you take prednisone.
  - edits: “it.” → “prednisone.”

**L152.0** `Incomplete Sentence` (0.859) → `excluded_incomplete`
- original: Does prednisone raise blood pressure?

**L152.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L153.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: It can.
- pronoun resolved: Prednisone can.
  - edits: “It” → “Prednisone”

**L153.1** `Complex Sentence` (0.892) → `decomposed`
- original: Prednisone makes your body hold onto salt and water, which raises blood pressure in some people, particularly at higher doses or on longer courses.
  - S1: Prednisone makes your body hold onto salt and water.
  - S2: This raises blood pressure in some people.
  - S3: This effect is particularly seen at higher doses or on longer courses.

**L153.2** `Compound Sentence` (0.96) → `decomposed`
- original: Your blood pressure should be checked during treatment, and your doctor may ask you to reduce salt in your diet.
  - S1: Your blood pressure should be checked during treatment.
  - S2: Your doctor may ask you to reduce salt in your diet.

**L154.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: What is considered a high dose of prednisone?

**L154.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L155.0** `Compound Sentence` (0.631) → `decomposed`
- original: There is no official cutoff, but doctors generally treat doses under 7.5 mg a day as low, 7.5 mg to 40 mg a day as moderate, and more than 40 mg a day as high.
  - S1: There is no official cutoff.
  - S2: Doctors generally treat doses under 7.5 mg a day as low.
  - S3: Doctors generally treat doses from 7.5 mg to 40 mg a day as moderate.
  - S4: Doctors generally treat doses over 40 mg a day as high.

**L155.1** `Simple Sentence` (0.982) → `passthrough`
- original: A dose of 20 mg a day sits in the moderate range.

**L155.2** `Complex Sentence` (0.512) → `decomposed`
- original: What matters as much as the number is how long you take it, because side effects build up over time.
- pronoun resolved: What matters as much as the number is how long you take prednisone, because side effects build up over time.
  - edits: “it,” → “prednisone,”
  - S1: What matters as much as the number is how long you take prednisone.
  - S2: Side effects build up over time.

**L156.0** `Incomplete Sentence` (0.888) → `excluded_incomplete`
- original: Can prednisone make you tired?

**L156.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L157.0** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Yes.

**L157.1** `Simple Sentence` (0.921) → `passthrough`
- original: Some people feel energized on prednisone while others feel drained.

**L157.2** `Simple Sentence` (0.983) → `passthrough`
- original: Poor sleep, mood changes and muscle weakness all contribute.

**L157.3** `Compound-Complex Sentence` (0.871) → `decomposed`
- original: Tiredness that starts as your dose is being lowered, or after you stop, can be a sign that your adrenal glands have not caught up yet, so tell your doctor if it is severe or comes with dizziness, nausea, or body aches.
- pronoun resolved: Tiredness that starts as your dose is being lowered, or after you stop, can be a sign that your adrenal glands have not caught up yet, so tell your doctor if Tiredness is severe or comes with dizziness, nausea, or body aches.
  - edits: “it” → “Tiredness”
  - S1: Tiredness can start as your dose is being lowered.
  - S2: Tiredness can start after you stop taking the medication.
  - S3: This tiredness can be a sign that your adrenal glands have not caught up yet.
  - S4: Tell your doctor if tiredness is severe.
  - S5: Tell your doctor if tiredness comes with dizziness.
  - S6: Tell your doctor if tiredness comes with nausea.
  - S7: Tell your doctor if tiredness comes with body aches.

## Popular FAQ

**L160.0** `Incomplete Sentence` (0.973) → `excluded_incomplete`
- original: Q: What is considered a high dose of prednisone?

**L160.1** `Simple Sentence` (0.901) → `passthrough`
- original: A: The starting dose of prednisone may be between 5 mg to 60 mg per day.

**L160.2** `Simple Sentence` (0.973) → `passthrough`
- original: A dose above 40 mg per day may be considered a high dose.

**L160.3** `Compound Sentence` (0.873) → `decomposed`
- original: However, everybody responds differently to prednisone, so what might be a high dose depends on the person and the condition.
  - S1: However, everybody responds differently to prednisone.
  - S2: So what might be a high dose depends on the person and the condition.

**L161.0** `Simple Sentence` (0.57) → `passthrough`
- original: Q: Can you take prednisone with Keytruda?

**L161.1** `Incomplete Sentence` (0.658) → `excluded_incomplete`
- original: A: Use prednisone with Keytruda or Keytruda Qlex only if your healthcare provider prescribes it.
- pronoun resolved: A: Use prednisone with Keytruda or Keytruda Qlex only if your healthcare provider prescribes prednisone.
  - edits: “it.” → “prednisone.”

**L161.2** `Simple Sentence` (0.992) → `passthrough`
- original: Prednisone is a corticosteroid that lowers immune system activity.

**L161.3** `Simple Sentence` (0.975) → `passthrough`
- original: It may reduce how well Keytruda works or increase your risk of infection.
- pronoun resolved: Prednisone may reduce how well Keytruda works or increase your risk of infection.
  - edits: “It” → “Prednisone”

**L161.4** `Simple Sentence` (0.844) → `passthrough`
- original: However, your doctor may prescribe prednisone to treat certain immune-related side effects caused by Keytruda.

**L162.0** `Simple Sentence` (0.66) → `passthrough`
- original: Q: What's a good prednisone taper schedule?

**L162.1** `Complex Sentence` (0.506) → `decomposed`
- original: A: A prednisone taper depends on your dose, how long you have taken it, and the condition being treated.
- pronoun resolved: A: A prednisone taper depends on your dose, how long you have taken prednisone, and the condition being treated.
  - edits: “it,” → “prednisone,”
  - S1: A prednisone taper depends on your dose.
  - S2: A prednisone taper depends on how long you have taken prednisone.
  - S3: A prednisone taper depends on the condition being treated.

**L162.2** `Complex Sentence` (0.666) → `decomposed`
- original: If prednisone has been taken for less than 3 to 4 weeks, a taper is usually not needed, regardless of the dose.
  - S1: If prednisone has been taken for less than 3 to 4 weeks, a taper is usually not needed.
  - S2: This applies regardless of the dose.

**L162.3** `Simple Sentence` (0.93) → `passthrough`
- original: The risk of adrenal insufficiency increases with longer treatment and higher doses.

**L162.4** `Compound Sentence` (0.774) → `decomposed`
- original: Treatment for 3 to 4 weeks or longer at doses above about 4 to 6 mg of prednisone per day may suppress the body's normal cortisol production and may require a gradual taper.
  - S1: Treatment for 3 to 4 weeks or longer at doses above about 4 to 6 mg of prednisone per day may suppress the body's normal cortisol production.
  - S2: Such treatment may require a gradual taper.

**L163.0** `Incomplete Sentence` (0.718) → `excluded_incomplete`
- original: Q: Is it OK to drink alcohol with Prednisone?
- pronoun resolved: Q: Is Prednisone OK to drink alcohol with Prednisone?
  - edits: “it” → “Prednisone”

**L163.1** `Compound-Complex Sentence` (0.524) → `decomposed`
- original: A: Although there is no direct drug interaction between prednisone and alcohol, mixing them together is not a good idea because some of the effects of alcohol and the side effects of prednisone are similar, so taking both at the same time can increase the risk of these side effects occurring.
- pronoun resolved: A: Although there is no direct drug interaction between prednisone and alcohol, mixing prednisone together is not a good idea because some of the effects of alcohol and the side effects of prednisone are similar, so taking both at the same time can increase the risk of these side effects occurring.
  - edits: “them” → “prednisone”
  - S1: There is no direct drug interaction between prednisone and alcohol.
  - S2: Mixing prednisone together is not a good idea.
  - S3: Some of the effects of alcohol and the side effects of prednisone are similar.
  - S4: Taking both prednisone and alcohol at the same time can increase the risk of these side effects occurring.

**L164.0** `Incomplete Sentence` (0.939) → `excluded_incomplete`
- original: Q: How long can you take prednisone safely?

**L164.1** `Simple Sentence` (0.908) → `passthrough`
- original: A: There is no set limit on how long you can safely take prednisone.

**L164.2** `Simple Sentence` (0.774) → `passthrough`
- original: It depends on the dose of prednisone and the condition being treated.

**L164.3** `Simple Sentence` (0.975) → `passthrough`
- original: It may be prescribed short term or long term.

**L164.4** `Simple Sentence` (0.916) → `passthrough`
- original: The dosage will be adjusted or stopped based on your response or lack of response to the medication.

**L165.0** `Incomplete Sentence` (0.932) → `excluded_incomplete`
- original: Q: How long does it take for prednisone to work?

**L165.1** `Complex Sentence` (0.518) → `decomposed`
- original: A: Prednisone usually works very quickly, within a few hours to days of taking the first dose depending on the condition you are treating.
  - S1: Prednisone usually works very quickly.
  - S2: It works within a few hours to days of taking the first dose.
  - S3: The timing depends on the condition you are treating.

**L165.2** `Complex Sentence` (0.949) → `decomposed`
- original: If the prescribed dose of prednisone is effective at reducing your inflammation, then you may notice an effect within hours.
  - S1: You may notice an effect within hours.
  - S2: This effect occurs if the prescribed dose of prednisone is effective at reducing your inflammation.

**L166.0** `Incomplete Sentence` (0.976) → `excluded_incomplete`
- original: Q: Prednisone: What are 12 Things You Should Know?

**L166.1** `Compound Sentence` (0.572) → `decomposed`
- original: A: Prednisone has been on the market for more than 70 years but is still one of the most commonly prescribed anti-inflammatory or immunosuppressive medications.
  - S1: Prednisone has been on the market for more than 70 years.
  - S2: It is still one of the most commonly prescribed anti-inflammatory or immunosuppressive medications.

**L166.2** `Simple Sentence` (0.659) → `passthrough`
- original: Prednisone is used to treat dozens of different conditions such as skin disorders, breathing disorders, allergies, arthritis, and ulcerative colitis.

**L166.3** `Simple Sentence` (0.78) → `passthrough`
- original: But did you know it also has some pretty serious side effects as well?
- pronoun resolved: But did you know Prednisone also has some pretty serious side effects as well?
  - edits: “it” → “Prednisone”

**L167.0** `Incomplete Sentence` (0.518) → `excluded_incomplete`
- original: Q: Do I take all 6 prednisone pills at once on the first day?

**L167.1** `Simple Sentence` (0.956) → `passthrough`
- original: A: It's best to take prednisone as a single dose once a day straight after breakfast.

**L167.2** `Compound Sentence` (0.481) → `decomposed`
- original: For example if your dose is 30mg daily, it's usual to take 6 tablets (6 x 5mg) all at the same time after breakfast.
  - S1: For example, if your dose is 30mg daily, it is usual to take 6 tablets (6 x 5mg).
  - S2: You should take them all at the same time after breakfast.

**L168.0** `Incomplete Sentence` (0.649) → `excluded_incomplete`
- original: Q: How long does prednisone stay in your system?

**L168.1** `Simple Sentence` (0.377) → `passthrough`
- original: A: In general, you could expect a dose or prednisone to stay in your system for 16.5 to 22 hours based on a half life of 3 to 4 hours.

**L168.2** `Simple Sentence` (0.935) → `passthrough`
- original: It usually takes around 5.5 half lives for a drug to be completely eliminated from your system.
