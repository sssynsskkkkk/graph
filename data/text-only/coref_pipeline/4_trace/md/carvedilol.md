# Carvedilol — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/carvedilol.txt` · 119 sentences · 9 changed by pronoun resolution · 141 sentences sent to EDC

## What is carvedilol?

**L5.0** `Simple Sentence` (0.99) → `passthrough`
- original: Carvedilol is a beta-blocker.

**L5.1** `Simple Sentence` (0.986) → `passthrough`
- original: Beta-blockers affect the heart and circulation (blood flow through arteries and veins).

**L6.0** `Simple Sentence` (0.978) → `passthrough`
- original: Carvedilol is used to treat heart failure and hypertension (high blood pressure).

**L6.1** `Simple Sentence` (0.938) → `passthrough`
- original: It is also used after a heart attack that has caused your heart not to pump as well.
- pronoun resolved: Carvedilol is also used after a heart attack that has caused your heart not to pump as well.
  - edits: “It” → “Carvedilol”

**L7.0** `Simple Sentence` (0.983) → `passthrough`
- original: Carvedilol may also be used for purposes not listed in this medication guide.

**L8.0** `Simple Sentence` (0.983) → `passthrough`
- original: Carvedilol is not approved for use by anyone younger than 18 years of age.

## Warnings

**L11.0** `Complex Sentence` (0.732) → `decomposed`
- original: You should not take carvedilol if you have asthma, bronchitis, emphysema, severe liver disease, severe heart failure requiring certain IV medications, or a serious heart condition such as heart block, "sick sinus syndrome," or slow heart rate (unless you have a pacemaker).
  - S1: You should not take carvedilol if you have asthma, bronchitis, or emphysema.
  - S2: You should not take carvedilol if you have severe liver disease.
  - S3: You should not take carvedilol if you have severe heart failure requiring certain IV medications.
  - S4: You should not take carvedilol if you have a serious heart condition such as heart block, "sick sinus syndrome," or slow heart rate.
  - S5: You may take carvedilol if you have a serious heart condition such as heart block, "sick sinus syndrome," or slow heart rate and have a pacemaker.

**L12.0** `Incomplete Sentence` (0.965) → `excluded_incomplete`
- original: Avoid drinking alcohol within 2 hours before or after taking extended-release carvedilol (Coreg CR).

**L12.1** `Incomplete Sentence` (0.989) → `excluded_incomplete`
- original: Also avoid taking medicines or other products that might contain alcohol.

**L12.2** `Simple Sentence` (0.969) → `passthrough`
- original: Alcohol may cause the carvedilol in Coreg CR to be released too quickly into the body.

**L13.0** `Simple Sentence` (0.581) → `passthrough`
- original: If you are being treated for high blood pressure, keep using carvedilol even if you feel well.

**L13.1** `Simple Sentence` (0.988) → `passthrough`
- original: High blood pressure often has no symptoms.

**L13.2** `Simple Sentence` (0.976) → `passthrough`
- original: You may need to use blood pressure medication for the rest of your life.

## Before taking this medicine

**L16.0** `Simple Sentence` (0.948) → `passthrough`
- original: You should not take carvedilol if you are allergic to it, or if you have:
- pronoun resolved: You should not take carvedilol if you are allergic to Carvedilol, or if you have:
  - edits: “it,” → “Carvedilol,”

**L17.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: asthma, bronchitis, emphysema;

**L18.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: severe liver disease; or

**L19.0** `Compound Sentence` (0.441) → `decomposed`
- original: a serious heart condition such as heart block, "sick sinus syndrome," or slow heart rate (unless you have a pacemaker); or severe heart failure requiring certain IV medications.
  - S1: A serious heart condition such as heart block, "sick sinus syndrome," or slow heart rate (unless you have a pacemaker) exists.
  - S2: Severe heart failure requiring certain IV medications exists.

**L20.0** `Incomplete Sentence` (0.583) → `excluded_incomplete`
- original: To make sure carvedilol is safe for you, tell your doctor if you have:

**L21.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: diabetes (taking carvedilol can make it harder for you to tell when you have low blood sugar);

**L22.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: angina (chest pain);

**L23.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: liver or kidney disease;

**L24.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a thyroid disorder;

**L25.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: pheochromocytoma (tumor of the adrenal gland);

**L26.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: circulation problems (such as Raynaud's syndrome); or

**L27.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a history of allergies.

**L28.0** `Simple Sentence` (0.497) → `passthrough`
- original: FDA pregnancy category C. It is not known whether carvedilol will harm an unborn baby.

**L28.1** `Incomplete Sentence` (0.917) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or plan to become pregnant while using this medication.
- pronoun resolved: Tell your doctor if you are pregnant or plan to become pregnant while using Carvedilol.
  - edits: “this medication.” → “Carvedilol.”

**L29.0** `Compound Sentence` (0.453) → `decomposed`
- original: It is not known whether carvedilol passes into breast milk or if it could harm a nursing baby.
- pronoun resolved: It is not known whether carvedilol passes into breast milk or if Carvedilol could harm a nursing baby.
  - edits: “it” → “Carvedilol”
  - S1: It is not known whether carvedilol passes into breast milk.
  - S2: It is not known if Carvedilol could harm a nursing baby.

**L29.1** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Talk with your doctor about the best way to feed your baby if you are taking carvedilol.

## How should I take carvedilol?

**L32.0** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Take carvedilol exactly as prescribed by your doctor.

**L32.1** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Follow all directions on your prescription label.

**L32.2** `Simple Sentence` (0.957) → `passthrough`
- original: Your doctor may occasionally change your dose to make sure you get the best results.

**L32.3** `Incomplete Sentence` (0.903) → `excluded_incomplete`
- original: Do not take this medicine in larger or smaller amounts or for longer than recommended.

**L33.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Take carvedilol with food.

**L34.0** `Incomplete Sentence` (0.621) → `excluded_incomplete`
- original: Swallow the extended-release capsule whole and do not crush or chew it.

**L34.1** `Complex Sentence` (0.804) → `decomposed`
- original: If you have trouble swallowing, you may open the carvedilol capsule and sprinkle the medicine into a spoonful of applesauce to make swallowing easier.
- pronoun resolved: If you have trouble swallowing, you may open the carvedilol capsule and sprinkle carvedilol into a spoonful of applesauce to make swallowing easier.
  - edits: “the medicine” → “carvedilol”
  - S1: If you have trouble swallowing, you may open the carvedilol capsule.
  - S2: You may sprinkle carvedilol into a spoonful of applesauce.
  - S3: This makes swallowing easier.

**L34.2** `Simple Sentence` (0.935) → `passthrough`
- original: The applesauce should not be warm.

**L34.3** `Incomplete Sentence` (0.913) → `excluded_incomplete`
- original: Do not sprinkle contents on foods other than applesauce.

**L34.4** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Swallow right away without chewing.

**L34.5** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Do not save the mixture for later use.

**L34.6** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Discard the empty capsule.

**L35.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Take carvedilol at the same time every day.

**L35.1** `Incomplete Sentence` (0.601) → `excluded_incomplete`
- original: Do not skip doses or stop taking carvedilol without first talking to your doctor.

**L35.2** `Simple Sentence` (0.985) → `passthrough`
- original: Stopping suddenly may cause chest pain or a heart attack.

**L36.0** `Complex Sentence` (0.952) → `decomposed`
- original: If you are switched from carvedilol tablets to carvedilol extended-release capsules (Coreg CR), your daily total dose of this medicine may be higher or lower than before.
- pronoun resolved: If you are switched from carvedilol tablets to carvedilol extended-release capsules (Coreg CR), your daily total dose of carvedilol may be higher or lower than before.
  - edits: “this medicine” → “carvedilol”
  - S1: If you are switched from carvedilol tablets to carvedilol extended-release capsules (Coreg CR).
  - S2: Your daily total dose of carvedilol may be higher or lower than before.

**L36.1** `Complex Sentence` (0.604) → `decomposed`
- original: Older adults may be more likely to become dizzy or feel faint when switching from tablets to extended-release capsules.
  - S1: Older adults may be more likely to become dizzy or feel faint.
  - S2: This may happen when switching from tablets to extended-release capsules.

**L36.2** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Follow your doctor's instructions.

**L37.0** `Simple Sentence` (0.978) → `passthrough`
- original: Your blood pressure will need to be checked often.

**L38.0** `Simple Sentence` (0.581) → `passthrough`
- original: If you are being treated for high blood pressure, keep using this medication even if you feel well.
- pronoun resolved: If you are being treated for high blood pressure, keep using carvedilol even if you feel well.
  - edits: “this medication” → “carvedilol”

**L38.1** `Simple Sentence` (0.988) → `passthrough`
- original: High blood pressure often has no symptoms.

**L38.2** `Simple Sentence` (0.976) → `passthrough`
- original: You may need to use blood pressure medication for the rest of your life.

**L39.0** `Simple Sentence` (0.667) → `passthrough`
- original: If you need surgery, tell the surgeon ahead of time that you are using carvedilol.

**L39.1** `Simple Sentence` (0.963) → `passthrough`
- original: You may need to stop using the medicine for a short time.
- pronoun resolved: You may need to stop using carvedilol for a short time.
  - edits: “the medicine” → “carvedilol”

**L40.0** `Simple Sentence` (0.95) → `passthrough`
- original: You should not stop using carvedilol suddenly.

**L40.1** `Simple Sentence` (0.985) → `passthrough`
- original: Stopping suddenly may cause chest pain or a heart attack.

**L41.0** `Simple Sentence` (0.992) → `passthrough`
- original: Carvedilol can affect your pupils during cataract surgery.

**L41.1** `Incomplete Sentence` (0.892) → `excluded_incomplete`
- original: Tell your eye surgeon ahead of time that you are using this medication.
- pronoun resolved: Tell your eye surgeon ahead of time that you are using carvedilol.
  - edits: “this medication.” → “carvedilol.”

**L41.2** `Simple Sentence` (0.729) → `passthrough`
- original: Do not stop using carvedilol before surgery unless your surgeon tells you to.

**L42.0** `Complex Sentence` (0.649) → `decomposed`
- original: Carvedilol is only part of a complete program of treatment for hypertension that may also include diet, exercise, and weight control.
  - S1: Carvedilol is only part of a complete program of treatment for hypertension.
  - S2: The program may also include diet, exercise, and weight control.

**L42.1** `Incomplete Sentence` (0.698) → `excluded_incomplete`
- original: Follow your diet, medication, and exercise routines very closely if you are being treated for hypertension.

**L43.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Store at room temperature away from moisture and heat.

## What happens if I miss a dose?

**L46.0** `Incomplete Sentence` (0.926) → `excluded_incomplete`
- original: Take the missed dose as soon as you remember.

**L46.1** `Incomplete Sentence` (0.89) → `excluded_incomplete`
- original: Skip the missed dose if it is almost time for your next scheduled dose.

**L46.2** `Incomplete Sentence` (0.748) → `excluded_incomplete`
- original: Do not take extra medicine to make up the missed dose.

## What happens if I overdose?

**L49.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L50.0** `Compound Sentence` (0.485) → `decomposed`
- original: Overdose symptoms may include uneven heartbeats, shortness of breath, bluish-colored fingernails, dizziness, weakness, fainting, and seizure (convulsions).
  - S1: Overdose symptoms may include uneven heartbeats.
  - S2: Overdose symptoms may include shortness of breath.
  - S3: Overdose symptoms may include bluish-colored fingernails.
  - S4: Overdose symptoms may include dizziness.
  - S5: Overdose symptoms may include weakness.
  - S6: Overdose symptoms may include fainting.
  - S7: Overdose symptoms may include seizure (convulsions).

## What to avoid

**L53.0** `Simple Sentence` (0.987) → `passthrough`
- original: Carvedilol may impair your thinking or reactions.

**L53.1** `Incomplete Sentence` (0.688) → `excluded_incomplete`
- original: Be careful if you drive or do anything that requires you to be alert.

**L54.0** `Compound Sentence` (0.688) → `decomposed`
- original: Drinking alcohol can further lower your blood pressure and may increase certain side effects of carvedilol.
  - S1: Drinking alcohol can further lower your blood pressure.
  - S2: Drinking alcohol may increase certain side effects of carvedilol.

**L54.1** `Simple Sentence` (0.692) → `passthrough`
- original: You should especially avoid drinking alcohol within 2 hours before or after taking extended-release carvedilol (Coreg CR).

**L55.0** `Incomplete Sentence` (0.599) → `excluded_incomplete`
- original: Avoid getting up too fast from a sitting or lying position, or you may feel dizzy.

**L55.1** `Incomplete Sentence` (0.49) → `excluded_incomplete`
- original: Get up slowly and steady yourself to prevent a fall.

## Carvedilol side effects

**L58.0** `Compound Sentence` (0.446) → `decomposed`
- original: Get emergency medical help if you have any of these signs of an allergic reaction to carvedilol: hives; difficulty breathing; swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have hives.
  - S2: Get emergency medical help if you have difficulty breathing.
  - S3: Get emergency medical help if you have swelling of your face, lips, tongue, or throat.

**L59.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Call your doctor at once if you have a serious side effect such as:

**L60.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a light-headed feeling, like you might pass out;

**L61.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: slow or uneven heartbeats;

**L62.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: swelling, rapid weight gain, feeling short of breath (even with mild exertion);

**L63.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: cold feeling or numbness in your fingers or toes;

**L64.0** `Incomplete Sentence` (0.986) → `excluded_incomplete`
- original: chest pain, dry cough, wheezing, chest tightness, trouble breathing; or

**L65.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: high blood sugar (increased thirst, increased urination, hunger, dry mouth, fruity breath odor, drowsiness, dry skin, blurred vision, weight loss).

**L66.0** `Simple Sentence` (0.946) → `passthrough`
- original: Common carvedilol side effects may include:

**L67.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: weakness, dizziness;

**L68.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: diarrhea;

**L69.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: dry eyes;

**L70.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: tired feeling; or

**L71.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: weight gain.

**L72.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L72.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L72.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## What other drugs will affect carvedilol?

**L75.0** `Complex Sentence` (0.507) → `decomposed`
- original: Other drugs may interact with carvedilol, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may interact with carvedilol.
  - S2: These drugs include prescription and over-the-counter medicines.
  - S3: These drugs also include vitamins and herbal products.

**L75.1** `Incomplete Sentence` (0.762) → `excluded_incomplete`
- original: Tell each of your health care providers about all medicines you use now and any medicine you start or stop using.

**L76.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Check interactions

**L77.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Compare alternatives

**L78.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Pricing & coupons

**L79.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Reviews (217)

**L80.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Drug images

**L81.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Side effects

**L82.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Dosage information

**L83.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Patient tips

**L84.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: During pregnancy

**L85.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Support group

**L86.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Drug class: non-cardioselective beta blockers

**L87.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Breastfeeding

**L88.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: En español

**L89.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Patient resources:

**L90.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Other brands:

**L91.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Coreg

**L92.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Professional resources:

**L93.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Carvedilol monograph

**L94.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Carvedilol (FDA)

**L95.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Carvedilol Capsule (FDA)

**L96.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Other brands:

**L97.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Coreg, Coreg CR

**L98.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Related treatment guides:

**L99.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Atrial Fibrillation

**L100.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: High Blood Pressure

**L101.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Left Ventricular Dysfunction

**L102.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Heart Failure

**L103.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Angina
