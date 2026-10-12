# Tamsulosin — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/tamsulosin.txt` · 129 sentences · 7 changed by pronoun resolution · 161 sentences sent to EDC

## What is tamsulosin?

**L5.0** `Simple Sentence` (0.424) → `passthrough`
- original: Tamsulosin is used to treat the symptoms of an enlarged prostate, also called benign prostatic hyperplasia or BPH.

**L5.1** `Compound Sentence` (0.686) → `decomposed`
- original: These symptoms include a weak urine stream, trouble starting to urinate, dribbling, a feeling of not emptying the bladder completely, needing to urinate often or urgently, and getting up at night to urinate.
  - S1: These symptoms include a weak urine stream.
  - S2: They include trouble starting to urinate.
  - S3: They include dribbling.
  - S4: They include a feeling of not emptying the bladder completely.
  - S5: They include needing to urinate often or urgently.
  - S6: They include getting up at night to urinate.

**L6.0** `Simple Sentence` (0.989) → `passthrough`
- original: Tamsulosin belongs to a group of medicines called alpha blockers.

**L6.1** `Simple Sentence` (0.987) → `passthrough`
- original: It works by blocking alpha-1 receptors in the prostate and bladder neck.
- pronoun resolved: Tamsulosin works by blocking alpha-1 receptors in the prostate and bladder neck.
  - edits: “It” → “Tamsulosin”

**L6.2** `Compound Sentence` (0.673) → `decomposed`
- original: Blocking these receptors relaxes the muscle there, which improves urine flow and eases BPH symptoms.
  - S1: Blocking these receptors relaxes the muscle there.
  - S2: This improves urine flow and eases BPH symptoms.

**L7.0** `Simple Sentence` (0.966) → `passthrough`
- original: Tamsulosin is taken once daily, about half an hour after the same meal each day.

**L7.1** `Simple Sentence` (0.891) → `passthrough`
- original: Capsules should be swallowed whole and not crushed, chewed, or opened.

**L8.0** `Compound Sentence` (0.955) → `decomposed`
- original: The tamsulosin brand name was Flomax, which has now been discontinued in the U.S., but generic tamsulosin is available.
  - S1: The tamsulosin brand name was Flomax.
  - S2: Flomax has now been discontinued in the U.S.
  - S3: Generic tamsulosin is available.

**L9.0** `Compound Sentence` (0.959) → `decomposed`
- original: Tamsulosin is not approved to treat high blood pressure, and it is not approved for use in women or children.
- pronoun resolved: Tamsulosin is not approved to treat high blood pressure, and Tamsulosin is not approved for use in women or children.
  - edits: “it” → “Tamsulosin”
  - S1: Tamsulosin is not approved to treat high blood pressure.
  - S2: Tamsulosin is not approved for use in women or children.

## Warnings and precautions

**L12.0** `Simple Sentence` (0.743) → `passthrough`
- original: Do not take tamsulosin if you are allergic to tamsulosin or to any of the ingredients in the capsule.

**L13.0** `Compound Sentence` (0.515) → `decomposed`
- original: Do not take tamsulosin with other alpha blockers such as alfuzosin (Uroxatral), doxazosin (Cardura), prazosin (Minipress), silodosin (Rapaflo), or terazosin (Hytrin).
  - S1: Do not take tamsulosin with other alpha blockers.
  - S2: Examples of other alpha blockers include alfuzosin (Uroxatral), doxazosin (Cardura), prazosin (Minipress), silodosin (Rapaflo), and terazosin (Hytrin).

**L14.0** `Simple Sentence` (0.605) → `passthrough`
- original: Do not take tamsulosin 0.4 mg with a strong CYP3A4 inhibitor such as ketoconazole.

**L14.1** `Simple Sentence` (0.991) → `passthrough`
- original: These medicines raise tamsulosin levels in your blood.

**L15.0** `Compound Sentence` (0.666) → `decomposed`
- original: Tamsulosin can lower your blood pressure when you stand up, which may make you feel dizzy or faint.
  - S1: Tamsulosin can lower your blood pressure when you stand up.
  - S2: This may make you feel dizzy or faint.

**L15.1** `Compound Sentence` (0.619) → `decomposed`
- original: This is most likely when you first start taking it, when your dose changes, or when you start it again after a break.
- pronoun resolved: This is most likely when you first start taking it, when your dose changes, or when you start Tamsulosin again after a break.
  - edits: “it” → “Tamsulosin”
  - S1: This is most likely when you first start taking it.
  - S2: This is most likely when your dose changes.
  - S3: This is most likely when you start Tamsulosin again after a break.

**L15.2** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Get up slowly from sitting or lying down.

**L15.3** `Simple Sentence` (0.478) → `passthrough`
- original: Be careful driving or doing anything that needs you to be alert until you know how tamsulosin affects you.

**L16.0** `Complex Sentence` (0.91) → `decomposed`
- original: In rare cases (probably fewer than 1 in 50,000 patients), tamsulosin can cause priapism, a painful erection that lasts a long time and is not related to sexual activity.
  - S1: In rare cases, tamsulosin can cause priapism.
  - S2: These cases probably occur in fewer than 1 in 50,000 patients.
  - S3: Priapism is a painful erection that lasts a long time.
  - S4: Priapism is not related to sexual activity.

**L16.1** `Incomplete Sentence` (0.521) → `excluded_incomplete`
- original: Get medical help straight away if this happens, because without prompt treatment it can lead to permanent erectile dysfunction.
- pronoun resolved: Get medical help straight away if this happens, because without prompt treatment priapism can lead to permanent erectile dysfunction.
  - edits: “it” → “priapism”

**L17.0** `Simple Sentence` (0.991) → `passthrough`
- original: An enlarged prostate and prostate cancer can occur together.

**L17.1** `Incomplete Sentence` (0.71) → `excluded_incomplete`
- original: Ask your doctor about prostate cancer screening before you start tamsulosin and at regular intervals while you are taking it.

**L18.0** `Simple Sentence` (0.872) → `passthrough`
- original: Tamsulosin can cause a problem called intraoperative floppy iris syndrome (IFIS) during cataract or glaucoma surgery.

**L18.1** `Incomplete Sentence` (0.776) → `excluded_incomplete`
- original: Tell your eye surgeon that you take tamsulosin or have taken it in the past, even if you stopped months ago.
- pronoun resolved: Tell your eye surgeon that you take tamsulosin or have taken tamsulosin in the past, even if you stopped months ago.
  - edits: “it” → “tamsulosin”

**L18.2** `Simple Sentence` (0.77) → `passthrough`
- original: Do not stop taking tamsulosin before surgery unless your surgeon tells you to.

**L18.3** `Complex Sentence` (0.543) → `decomposed`
- original: If you are already booked in for cataract or glaucoma surgery, starting tamsulosin is not recommended.
  - S1: Starting tamsulosin is not recommended.
  - S2: This applies if you are already booked in for cataract or glaucoma surgery.

**L19.0** `Simple Sentence` (0.5) → `passthrough`
- original: If you stop taking tamsulosin for several days, talk to your doctor before starting again.

**L19.1** `Simple Sentence` (0.975) → `passthrough`
- original: You will need to restart at the 0.4 mg dose.

**L20.0** `Simple Sentence` (0.991) → `passthrough`
- original: Many other medicines can interact with tamsulosin.

**L20.1** `Incomplete Sentence` (0.893) → `excluded_incomplete`
- original: Tell your doctor about everything you take, including prescription medicines, over-the-counter medicines, vitamins, and herbal products.

## Before taking this medicine

**L23.0** `Incomplete Sentence` (0.505) → `excluded_incomplete`
- original: To make sure tamsulosin is safe for you, tell your doctor if you have ever had:

**L24.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: an allergy to tamsulosin or any of its ingredients
- pronoun resolved: an allergy to tamsulosin or any of tamsulosin's ingredients
  - edits: “its” → “tamsulosin's”

**L25.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: an allergy to sulfa drugs

**L26.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: kidney problems

**L27.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: liver problems

**L28.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: low blood pressure (hypotension)

**L29.0** `Incomplete Sentence` (0.841) → `excluded_incomplete`
- original: Also tell your doctor if you are planning to have cataract or glaucoma surgery.

**L30.0** `Incomplete Sentence` (0.843) → `excluded_incomplete`
- original: Ask your doctor about prostate cancer screening before starting tamsulosin and at regular intervals afterwards.

**L31.0** `Simple Sentence` (0.987) → `passthrough`
- original: Tamsulosin is not approved for use in women or in children.

## How should I take tamsulosin?

**L34.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Take tamsulosin exactly as prescribed.

**L34.1** `Incomplete Sentence` (0.802) → `excluded_incomplete`
- original: Follow the directions on your prescription label and read any medication guides or instruction sheets.

**L35.0** `Incomplete Sentence` (0.959) → `excluded_incomplete`
- original: Take once a day, about 30 minutes after the same meal each day.

**L35.1** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: For example, 30 minutes after dinner.

**L36.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Swallow the capsule whole.

**L36.1** `Incomplete Sentence` (0.899) → `excluded_incomplete`
- original: Do not crush, chew, break, or open it.

**L37.0** `Simple Sentence` (0.688) → `passthrough`
- original: If you stop taking tamsulosin for several days, do not start again without talking to your doctor.

**L38.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Store at room temperature, away from moisture and heat.

**L39.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Dosing information:

**L40.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Usual adult dose for benign prostatic hyperplasia:

**L41.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: 0.4 mg by mouth once a day, taken about half an hour after the same meal each day.

**L42.0** `Complex Sentence` (0.712) → `decomposed`
- original: If symptoms have not improved after 2 to 4 weeks at 0.4 mg, the dose may be increased to 0.8 mg once a day.
  - S1: If symptoms have not improved after 2 to 4 weeks at 0.4 mg.
  - S2: The dose may be increased to 0.8 mg once a day.

**L43.0** `Simple Sentence` (0.981) → `passthrough`
- original: Tamsulosin 0.4 mg should not be taken with a strong CYP3A4 inhibitor such as ketoconazole.

**L44.0** `Complex Sentence` (0.565) → `decomposed`
- original: If tamsulosin is stopped or interrupted for several days, treatment should start again at 0.4 mg once a day.
  - S1: If tamsulosin is stopped or interrupted for several days.
  - S2: Treatment should start again.
  - S3: The treatment should start at 0.4 mg once a day.

## What happens if I miss a dose?

**L47.0** `Incomplete Sentence` (0.926) → `excluded_incomplete`
- original: Take the missed dose as soon as you remember.

**L47.1** `Compound Sentence` (0.69) → `decomposed`
- original: If you have missed the dose for the whole day, skip it and take your next dose at the usual time.
- pronoun resolved: If you have missed the dose for the whole day, skip the dose and take your next dose at the usual time.
  - edits: “it” → “the dose”
  - S1: If you have missed the dose for the whole day, skip the dose.
  - S2: Take your next dose at the usual time.

**L47.2** `Incomplete Sentence` (0.871) → `excluded_incomplete`
- original: Do not take two doses at once.

**L48.0** `Simple Sentence` (0.459) → `passthrough`
- original: If you stop taking tamsulosin for several days in a row, talk to your doctor before starting again.

## What happens if I overdose?

**L51.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L51.1** `Simple Sentence` (0.988) → `passthrough`
- original: An overdose can cause a serious drop in blood pressure.

**L51.2** `Simple Sentence` (0.976) → `passthrough`
- original: Lying down flat can help until medical help arrives.

## What should I avoid while taking tamsulosin?

**L54.0** `Incomplete Sentence` (0.963) → `excluded_incomplete`
- original: Avoid driving or other activities that could be dangerous until you know how tamsulosin affects you.

**L54.1** `Simple Sentence` (0.945) → `passthrough`
- original: It can make you feel dizzy or lightheaded.

**L55.0** `Incomplete Sentence` (0.565) → `excluded_incomplete`
- original: Avoid getting up too quickly from sitting or lying down, or you may feel dizzy.

## Tamsulosin side effects

**L58.0** `Incomplete Sentence` (0.243) → `excluded_incomplete`
- original: Get emergency medical help if you have signs of an allergic reaction, such as hives, itching, rash, swelling of your face, tongue, or throat, or trouble breathing.

**L58.1** `Simple Sentence` (0.552) → `passthrough`
- original: Rarely, tamsulosin has been linked to severe skin reactions with blistering and peeling of the skin.

**L59.0** `Incomplete Sentence` (0.956) → `excluded_incomplete`
- original: Stop taking tamsulosin and call your doctor at once if you have:

**L60.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a lightheaded feeling, like you might pass out

**L61.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a painful erection that will not go away and is not related to sexual activity

**L62.0** `Incomplete Sentence` (0.973) → `excluded_incomplete`
- original: What are the common side effects of tamsulosin?

**L62.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L63.0** `Simple Sentence` (0.899) → `passthrough`
- original: Common tamsulosin side effects may include:

**L64.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: headache

**L65.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: dizziness

**L66.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: runny or stuffy nose, sore throat, cough, sinus congestion

**L67.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: flu-like symptoms or infection

**L68.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: weakness or lack of energy

**L69.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: back pain, chest pain

**L70.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: diarrhea, nausea

**L71.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: drowsiness or trouble sleeping

**L72.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: tooth problems

**L73.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: abnormal ejaculation, including a smaller amount of semen or no semen at all

**L74.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: reduced interest in sex

**L75.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: blurred vision

**L76.0** `Simple Sentence` (0.839) → `passthrough`
- original: Some side effects are more likely at the higher 0.8 mg dose than at the usual 0.4 mg starting dose.

**L76.1** `Compound Sentence` (0.919) → `decomposed`
- original: In clinical studies, abnormal ejaculation was reported by about 8 in 100 men taking 0.4 mg and about 18 in 100 men taking 0.8 mg. Blurred vision was reported by about 2 in 100 men taking 0.8 mg, and was uncommon at 0.4 mg.
  - S1: In clinical studies, abnormal ejaculation was reported by about 8 in 100 men taking 0.4 mg.
  - S2: About 18 in 100 men taking 0.8 mg reported abnormal ejaculation.
  - S3: Blurred vision was reported by about 2 in 100 men taking 0.8 mg.
  - S4: Blurred vision was uncommon at 0.4 mg.

**L77.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L77.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L77.2** `Simple Sentence` (0.983) → `passthrough`
- original: You may report side effects to FDA at 1-800-FDA-1088.

## What other drugs will affect tamsulosin?

**L80.0** `Simple Sentence` (0.984) → `passthrough`
- original: Tamsulosin is broken down in the body mainly by two liver enzymes, CYP3A4 and CYP2D6.

**L80.1** `Complex Sentence` (0.425) → `decomposed`
- original: Medicines that block these enzymes can raise the amount of tamsulosin in your blood and increase the risk of side effects.
  - S1: Medicines that block these enzymes can raise the amount of tamsulosin in your blood.
  - S2: These medicines can increase the risk of side effects.
  - S3: These medicines block these enzymes.

**L81.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Do not take tamsulosin with:

**L82.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: strong CYP3A4 inhibitors, such as ketoconazole

**L83.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: other alpha blockers, such as alfuzosin, doxazosin, prazosin, silodosin, or terazosin

**L84.0** `Incomplete Sentence` (0.886) → `excluded_incomplete`
- original: Use with caution, and tell your doctor if you take:

**L85.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: moderate CYP3A4 inhibitors, such as erythromycin

**L86.0** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: strong CYP2D6 inhibitors, such as paroxetine, or moderate CYP2D6 inhibitors, such as terbinafine

**L87.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: cimetidine

**L88.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: warfarin

**L89.0** `Incomplete Sentence` (0.953) → `excluded_incomplete`
- original: medicines for erectile dysfunction or pulmonary arterial hypertension known as PDE5 inhibitors, including avanafil (Stendra), sildenafil (Viagra, Revatio), tadalafil (Adcirca, Cialis), and vardenafil (Levitra).

**L89.1** `Simple Sentence` (0.988) → `passthrough`
- original: Taking these with tamsulosin can lower blood pressure enough to cause symptoms.

**L90.0** `Simple Sentence` (0.967) → `passthrough`
- original: Some of these cautions matter more at the higher 0.8 mg dose than at 0.4 mg.

**L90.1** `Simple Sentence` (0.947) → `passthrough`
- original: Your doctor will decide what is right for you.

**L91.0** `Compound Sentence` (0.62) → `decomposed`
- original: No dose change is needed if you take tamsulosin with nifedipine, atenolol, enalapril, digoxin, theophylline, or furosemide.
  - S1: No dose change is needed if you take tamsulosin with nifedipine.
  - S2: No dose change is needed if you take tamsulosin with atenolol.
  - S3: No dose change is needed if you take tamsulosin with enalapril.
  - S4: No dose change is needed if you take tamsulosin with digoxin.
  - S5: No dose change is needed if you take tamsulosin with theophylline.
  - S6: No dose change is needed if you take tamsulosin with furosemide.

**L92.0** `Compound Sentence` (0.616) → `decomposed`
- original: This list is not complete, and many other medicines may interact with tamsulosin.
  - S1: This list is not complete.
  - S2: Many other medicines may interact with tamsulosin.

**L92.1** `Simple Sentence` (0.849) → `passthrough`
- original: This includes prescription and over-the-counter medicines, vitamins, and herbal products.

**L93.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Tamsulosin Prescribing Information

**L94.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Check interactions

**L95.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Compare alternatives

**L96.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Pricing & coupons

**L97.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Reviews (581)

**L98.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Drug images

**L99.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Side effects

**L100.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Dosage information

**L101.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Patient tips

**L102.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: During pregnancy

**L103.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Support group

**L104.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Drug class: alpha blockers

**L105.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Breastfeeding

**L106.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: En español

**L107.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Patient resources:

**L108.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Other brands:

**L109.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Flomax

**L110.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Professional resources:

**L111.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Tamsulosin monograph

**L112.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Tamsulosin (FDA)

**L113.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Other brands:

**L114.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Flomax

**L115.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Related treatment guides:

**L116.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Benign Prostatic Hyperplasia

**L117.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Urinary Tract Stones
