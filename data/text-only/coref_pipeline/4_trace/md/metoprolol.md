# Metoprolol — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/metoprolol.txt` · 259 sentences · 28 changed by pronoun resolution · 361 sentences sent to EDC

## What is metoprolol?

**L5.0** `Complex Sentence` (0.684) → `decomposed`
- original: Metoprolol is a beta-blocker medication used to treat high blood pressure, chest pain (angina), and heart failure, and to improve survival after a heart attack.
  - S1: Metoprolol is a beta-blocker medication.
  - S2: Metoprolol is used to treat high blood pressure.
  - S3: Metoprolol is used to treat chest pain (angina).
  - S4: Metoprolol is used to treat heart failure.
  - S5: Metoprolol is used to improve survival after a heart attack.

**L5.1** `Compound Sentence` (0.871) → `decomposed`
- original: It works mainly on the heart, so it is called a cardioselective beta-blocker.
- pronoun resolved: Metoprolol works mainly on the heart, so Metoprolol is called a cardioselective beta-blocker.
  - edits: “It” → “Metoprolol”; “it” → “Metoprolol”
  - S1: Metoprolol works mainly on the heart.
  - S2: Metoprolol is called a cardioselective beta-blocker.

**L6.0** `Simple Sentence` (0.915) → `passthrough`
- original: Metoprolol works by blocking the effect of adrenaline and noradrenaline on beta-1 receptors in your heart.

**L6.1** `Compound Sentence` (0.902) → `decomposed`
- original: This slows your heart rate, reduces how hard your heart squeezes, and lowers your blood pressure.
  - S1: This slows your heart rate.
  - S2: It reduces how hard your heart squeezes.
  - S3: It lowers your blood pressure.

**L6.2** `Complex Sentence` (0.911) → `decomposed`
- original: Because the heart is doing less work, it needs less oxygen, which is why metoprolol also helps with angina.
- pronoun resolved: Because the heart is doing less work, Metoprolol needs less oxygen, which is why metoprolol also helps with angina.
  - edits: “it” → “Metoprolol”
  - S1: Because the heart is doing less work, Metoprolol needs less oxygen.
  - S2: This is why metoprolol also helps with angina.

**L6.3** `Complex Sentence` (0.514) → `decomposed`
- original: Exactly how metoprolol works for high blood pressure, heart failure, and after a heart attack is not fully understood.
  - S1: Exactly how metoprolol works is not fully understood.
  - S2: It works for high blood pressure.
  - S3: It works for heart failure.
  - S4: It works after a heart attack.

**L7.0** `Complex Sentence` (0.775) → `decomposed`
- original: At higher blood levels, metoprolol also blocks beta-2 receptors in the airways and blood vessels, which is why it still needs care in people with breathing problems.
- pronoun resolved: At higher blood levels, metoprolol also blocks beta-2 receptors in the airways and blood vessels, which is why Metoprolol still needs care in people with breathing problems.
  - edits: “it” → “Metoprolol”
  - S1: At higher blood levels, metoprolol also blocks beta-2 receptors in the airways and blood vessels.
  - S2: Metoprolol still needs care in people with breathing problems.
  - S3: This is because metoprolol blocks beta-2 receptors in the airways and blood vessels at higher blood levels.

**L8.0** `Simple Sentence` (0.981) → `passthrough`
- original: Metoprolol comes as two different salts, metoprolol tartrate and metoprolol succinate.

**L8.1** `Simple Sentence` (0.985) → `passthrough`
- original: They are not interchangeable dose for dose:
- pronoun resolved: Metoprolol tartrate and metoprolol succinate are not interchangeable dose for dose:
  - edits: “They” → “Metoprolol tartrate and metoprolol succinate”

**L9.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Metoprolol tartrate, an immediate-release tablet usually taken once or twice a day (brand name Lopressor)

**L10.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Metoprolol succinate, an extended-release tablet or capsule taken once a day (brand names Toprol-XL and Kapspargo Sprinkle)

**L11.0** `Simple Sentence` (0.969) → `passthrough`
- original: Metoprolol tartrate is also given as an injection into a vein in a hospital during a heart attack.

## What is metoprolol used for?

**L14.0** `Compound Sentence` (0.956) → `decomposed`
- original: Metoprolol is FDA-approved to treat high blood pressure, angina, heart failure, and heart attack, but the two forms are not approved for the same conditions.
  - S1: Metoprolol is FDA-approved to treat high blood pressure, angina, heart failure, and heart attack.
  - S2: The two forms are not approved for the same conditions.

**L15.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Condition | Metoprolol tartrate (immediate release) | Metoprolol succinate (extended release)

**L16.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: High blood pressure (hypertension) in adults | Yes | Yes

**L17.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: High blood pressure in children 6 years and older | No | Yes

**L18.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Angina (chest pain) | Yes | Yes

**L19.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Heart failure | No | Yes

**L20.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Heart attack (myocardial infarction) | Yes | No

**L21.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: High blood pressure (hypertension).

**L21.1** `Complex Sentence` (0.4) → `decomposed`
- original: Lowering blood pressure reduces the risk of fatal and non-fatal heart and blood vessel events, mainly strokes and heart attacks.
  - S1: Lowering blood pressure reduces the risk of fatal and non-fatal heart and blood vessel events.
  - S2: These events mainly include strokes and heart attacks.

**L21.2** `Simple Sentence` (0.988) → `passthrough`
- original: Metoprolol can be used on its own or with other blood pressure medicines.

**L21.3** `Simple Sentence` (0.987) → `passthrough`
- original: Many people need more than one medicine to reach their blood pressure goal.

**L22.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Angina.

**L22.1** `Compound Sentence` (0.5) → `decomposed`
- original: Metoprolol is used for long-term treatment of angina, to reduce how often attacks happen and to help you do more before chest pain starts.
  - S1: Metoprolol is used for long-term treatment of angina.
  - S2: It is used to reduce how often attacks happen.
  - S3: It is used to help you do more before chest pain starts.

**L22.2** `Simple Sentence` (0.985) → `passthrough`
- original: It is not used to stop an attack that has already begun.
- pronoun resolved: Metoprolol is not used to stop an attack that has already begun.
  - edits: “It” → “Metoprolol”

**L23.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Heart failure.

**L23.1** `Simple Sentence` (0.981) → `passthrough`
- original: Only the extended-release form is approved for heart failure.

**L23.2** `Compound Sentence` (0.695) → `decomposed`
- original: It is used to reduce the risk of dying from heart and blood vessel causes and to reduce hospital admissions for heart failure.
- pronoun resolved: Metoprolol is used to reduce the risk of dying from heart and blood vessel causes and to reduce hospital admissions for heart failure.
  - edits: “It” → “Metoprolol”
  - S1: Metoprolol is used to reduce the risk of dying from heart and blood vessel causes.
  - S2: It is used to reduce hospital admissions for heart failure.

**L24.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Heart attack (myocardial infarction).

**L24.1** `Complex Sentence` (0.938) → `decomposed`
- original: Metoprolol tartrate is used in people whose blood pressure and circulation are stable after a definite or suspected heart attack, to reduce the risk of dying from heart and blood vessel causes.
  - S1: Metoprolol tartrate is used in people whose blood pressure and circulation are stable after a definite or suspected heart attack.
  - S2: It is used to reduce the risk of dying from heart and blood vessel causes.

**L24.2** `Simple Sentence` (0.756) → `passthrough`
- original: In hospital, it may be started as an injection into a vein and then continued as tablets.
- pronoun resolved: In hospital, Metoprolol may be started as an injection into a vein and then continued as tablets.
  - edits: “it” → “Metoprolol”

## What is the difference between metoprolol succinate and metoprolol tartrate?

**L27.0** `Compound Sentence` (0.935) → `decomposed`
- original: The two forms release the same medicine at different speeds, and they are approved for different conditions.
- pronoun resolved: The two forms release the same medicine at different speeds, and the two forms are approved for different conditions.
  - edits: “they” → “the two forms”
  - S1: The two forms release the same medicine at different speeds.
  - S2: The two forms are approved for different conditions.

**L27.1** `Compound Sentence` (0.848) → `decomposed`
- original: Metoprolol tartrate is released all at once, so it acts sooner and wears off sooner.
- pronoun resolved: Metoprolol tartrate is released all at once, so Metoprolol tartrate acts sooner and wears off sooner.
  - edits: “it” → “Metoprolol tartrate”
  - S1: Metoprolol tartrate is released all at once.
  - S2: Metoprolol tartrate acts sooner and wears off sooner.

**L27.2** `Compound Sentence` (0.868) → `decomposed`
- original: Metoprolol succinate is released slowly over the day, so one dose lasts about 24 hours.
  - S1: Metoprolol succinate is released slowly over the day.
  - S2: One dose lasts about 24 hours.

**L27.3** `Compound Sentence` (0.963) → `decomposed`
- original: Only the extended-release form is approved for heart failure and for children, and only the immediate-release form is approved for use after a heart attack.
  - S1: Only the extended-release form is approved for heart failure and for children.
  - S2: Only the immediate-release form is approved for use after a heart attack.

**L28.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Metoprolol tartrate | Metoprolol succinate

**L29.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Release | Immediate release | Extended release

**L30.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Usual dosing | Once or twice a day, or every 6 hours after a heart attack | Once a day

**L31.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Forms | Tablet, injection | Tablet, capsule

**L32.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Tablet strengths | 25 mg, 37.5 mg, 50 mg, 75 mg, 100 mg | 25 mg, 50 mg, 100 mg, 200 mg

**L33.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Brand names | Lopressor | Toprol-XL, Kapspargo Sprinkle

**L34.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Approved for heart failure | No | Yes

**L35.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Approved after a heart attack | Yes | No

**L36.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Approved for children 6 years and older | No | Yes

**L37.0** `Compound Sentence` (0.632) → `decomposed`
- original: If you switch from immediate-release metoprolol to the extended-release form, the total amount you take in a day stays the same.
  - S1: If you switch from immediate-release metoprolol to the extended-release form.
  - S2: The total amount you take in a day stays the same.

**L37.1** `Simple Sentence` (0.932) → `passthrough`
- original: Your prescriber makes this change, not you.

## Metoprolol side effects

**L40.0** `Compound Sentence` (0.474) → `decomposed`
- original: The most common side effects of metoprolol are tiredness, dizziness, low mood (depression), diarrhea, shortness of breath, a slow heartbeat (bradycardia), and itching or rash.
  - S1: The most common side effects of metoprolol are tiredness, dizziness, low mood (depression), diarrhea, shortness of breath, a slow heartbeat (bradycardia), and itching or rash.

**L40.1** `Simple Sentence` (0.951) → `passthrough`
- original: Most side effects reported in studies were mild and did not last.

**L41.0** `Compound Sentence` (0.436) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to metoprolol: hives, difficulty breathing, or swelling of your face, lips, tongue, or throat.
  - S1: Get emergency medical help if you have signs of an allergic reaction to metoprolol.
  - S2: These signs include hives, difficulty breathing, or swelling of your face, lips, tongue, or throat.

**L42.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Common side effects of metoprolol:

**L43.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: In studies of people taking metoprolol for high blood pressure or angina:

**L44.0** `Simple Sentence` (0.978) → `passthrough`
- original: Tiredness and dizziness occurred in about 10% of people

**L45.0** `Simple Sentence` (0.985) → `passthrough`
- original: Low mood or depression was reported in about 5 out of 100 people

**L46.0** `Simple Sentence` (0.989) → `passthrough`
- original: Diarrhea occurred in about 5% of people

**L47.0** `Simple Sentence` (0.988) → `passthrough`
- original: Itching or rash occurred in about 5% of people

**L48.0** `Simple Sentence` (0.981) → `passthrough`
- original: Shortness of breath and a slow heartbeat occurred in about 3% of people

**L49.0** `Simple Sentence` (0.762) → `passthrough`
- original: Cold hands and feet, palpitations, swelling of the ankles, and low blood pressure were each reported in about 1% of people

**L50.0** `Simple Sentence` (0.879) → `passthrough`
- original: Nausea, dry mouth, stomach pain, constipation, gas, and heartburn were each reported in about 1% of people

**L51.0** `Simple Sentence` (0.728) → `passthrough`
- original: Headache, nightmares, trouble sleeping, confusion, and short-term memory loss have also been reported.

**L52.0** `Compound Sentence` (0.835) → `decomposed`
- original: In the heart failure study of extended-release metoprolol, dizziness or vertigo was reported by 1.8% of people taking metoprolol compared with 1.0% taking placebo, and a slow heartbeat by 1.5% compared with 0.4%.
  - S1: In the heart failure study of extended-release metoprolol, dizziness or vertigo was reported by 1.8% of people taking metoprolol compared with 1.0% taking placebo.
  - S2: A slow heartbeat was reported by 1.5% of people taking metoprolol compared with 0.4% taking placebo.

**L53.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Other reported side effects:

**L54.0** `Simple Sentence` (0.984) → `passthrough`
- original: These have been reported since metoprolol came on the market.
- pronoun resolved: Side effects have been reported since metoprolol came on the market.
  - edits: “These” → “Side effects”

**L54.1** `Simple Sentence` (0.969) → `passthrough`
- original: Their frequency is not known:
- pronoun resolved: Side effects's frequency is not known:
  - edits: “Their” → “Side effects's”

**L55.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Hair thinning or hair loss, which reversed after stopping

**L56.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Reduced sex drive and difficulty getting an erection

**L57.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Dry eyes, blurred vision, and ringing in the ears

**L58.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Sweating, sensitivity to sunlight, and worsening of psoriasis

**L59.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: Change in taste, joint and muscle pain, and fainting

**L60.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Liver inflammation (hepatitis)

**L61.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: A severe drop in white blood cells (agranulocytosis), which can show up as fever, chills, or a sore throat

**L62.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious side effects of metoprolol:

**L63.0** `Compound Sentence` (0.41) → `decomposed`
- original: Some of these, such as shortness of breath and a slow heartbeat, are also listed as common side effects above.
- pronoun resolved: Some of side effects, such as shortness of breath and a slow heartbeat, are also listed as common side effects above.
  - edits: “these,” → “side effects,”
  - S1: Some of the side effects are also listed as common side effects above.
  - S2: These side effects include shortness of breath and a slow heartbeat.

**L63.1** `Simple Sentence` (0.657) → `passthrough`
- original: They need urgent attention when they are severe, new, or getting worse.
- pronoun resolved: Side effects need urgent attention when side effects are severe, new, or getting worse.
  - edits: “They” → “Side effects”; “they” → “side effects”

**L64.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L65.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: A very slow heartbeat, pauses in your heartbeat, or a feeling that you might faint.

**L65.1** `Simple Sentence` (0.974) → `passthrough`
- original: Sinus pause, heart block, and cardiac arrest have all been reported.

**L66.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Signs that heart failure is getting worse, such as weight gain over a few days, more shortness of breath, or swelling of your feet or lower legs

**L67.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Wheezing or trouble breathing

**L68.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Chest pain that is worse or more frequent than usual, especially if you have recently stopped or missed doses

**L69.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Cold, pale, or blue fingers and toes, or pain in your legs when you walk

**L70.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Confusion, hallucinations, or memory problems

**L71.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Yellowing of your skin or eyes, which can be a sign of liver inflammation

**L72.0** `Simple Sentence` (0.838) → `passthrough`
- original: This is not a complete list of side effects and others may occur.

**L72.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L72.2** `Simple Sentence` (0.97) → `passthrough`
- original: You may report side effects to the FDA at 1-800-FDA-1088.

## Metoprolol warnings

**L75.0** `Simple Sentence` (0.986) → `passthrough`
- original: The most important warning with metoprolol is not to stop it suddenly.
- pronoun resolved: The most important warning with metoprolol is not to stop Metoprolol suddenly.
  - edits: “it” → “Metoprolol”

**L75.1** `Compound Sentence` (0.516) → `decomposed`
- original: Stopping a beta blocker abruptly can bring on worse chest pain and, in some cases, a heart attack.
  - S1: Stopping a beta blocker abruptly can bring on worse chest pain.
  - S2: In some cases, it can bring on a heart attack.

**L75.2** `Complex Sentence` (0.7) → `decomposed`
- original: If your treatment needs to stop, your prescriber will lower the dose gradually over 1 to 2 weeks and watch how you respond.
  - S1: If your treatment needs to stop, your prescriber will lower the dose gradually over 1 to 2 weeks.
  - S2: Your prescriber will watch how you respond.

**L75.3** `Complex Sentence` (0.713) → `decomposed`
- original: This applies even if you only take metoprolol for blood pressure, because heart disease is common and is not always known about.
  - S1: This applies even if you only take metoprolol for blood pressure.
  - S2: Heart disease is common.
  - S3: Heart disease is not always known about.

**L76.0** `Incomplete Sentence` (0.929) → `excluded_incomplete`
- original: Talk to your care team before starting metoprolol if any of these apply to you.

**L77.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Asthma or other breathing problems.

**L77.1** `Simple Sentence` (0.989) → `passthrough`
- original: Beta blockers can tighten the airways.

**L77.2** `Complex Sentence` (0.687) → `decomposed`
- original: Metoprolol is used in people with these conditions only when other treatments are not suitable, at the lowest possible dose, with a reliever inhaler on hand.
  - S1: Metoprolol is used in people with these conditions only when other treatments are not suitable.
  - S2: It is used at the lowest possible dose.
  - S3: A reliever inhaler is kept on hand.

**L78.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Heart failure.

**L78.1** `Simple Sentence` (0.979) → `passthrough`
- original: Heart failure can get worse while the dose is being increased.

**L78.2** `Incomplete Sentence` (0.954) → `excluded_incomplete`
- original: Tell your doctor about weight gain or increasing breathlessness.

**L79.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: A slow heart rate or a conduction problem in the heart.

**L79.1** `Simple Sentence` (0.813) → `passthrough`
- original: This includes first-degree heart block, sinus node problems, and Wolff-Parkinson-White syndrome.

**L79.2** `Simple Sentence` (0.961) → `passthrough`
- original: Your heart rate should be monitored.

**L80.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Diabetes or long gaps without food.

**L80.1** `Compound Sentence` (0.964) → `decomposed`
- original: Metoprolol can hide the early warning signs of low blood sugar, such as a fast heartbeat, and can make low blood sugar more severe or last longer.
  - S1: Metoprolol can hide the early warning signs of low blood sugar, such as a fast heartbeat.
  - S2: Metoprolol can make low blood sugar more severe or last longer.

**L80.2** `Simple Sentence` (0.889) → `passthrough`
- original: The risk is higher if you are fasting, not eating regularly, or vomiting.

**L81.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: An overactive thyroid.

**L81.1** `Simple Sentence` (0.992) → `passthrough`
- original: Metoprolol can mask signs of an overactive thyroid.

**L81.2** `Simple Sentence` (0.989) → `passthrough`
- original: Stopping it suddenly can trigger a thyroid crisis.

**L82.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Circulation problems in your arms or legs.

**L82.1** `Simple Sentence` (0.99) → `passthrough`
- original: Beta blockers can make symptoms of poor circulation worse.

**L83.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: A history of severe allergic reactions.

**L83.1** `Complex Sentence` (0.845) → `decomposed`
- original: If you have anaphylaxis while taking a beta blocker, the usual dose of injectable epinephrine may not work as well.
  - S1: If you have anaphylaxis while taking a beta blocker.
  - S2: The usual dose of injectable epinephrine may not work as well.

**L84.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Pheochromocytoma (a tumor of the adrenal gland).

**L84.1** `Compound Sentence` (0.929) → `decomposed`
- original: Metoprolol must only be started after an alpha blocker has been started, or blood pressure can rise sharply.
  - S1: Metoprolol must only be started after an alpha blocker has been started.
  - S2: Otherwise, blood pressure can rise sharply.

**L85.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Liver disease.

**L85.1** `Simple Sentence` (0.646) → `passthrough`
- original: Metoprolol is broken down by the liver, so levels can build up.

**L85.2** `Simple Sentence` (0.985) → `passthrough`
- original: Treatment is usually started at a lower dose.

**L86.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Surgery.

**L86.1** `Incomplete Sentence` (0.89) → `excluded_incomplete`
- original: Tell your surgeon and dentist that you take metoprolol.

**L86.2** `Simple Sentence` (0.989) → `passthrough`
- original: Long-term beta blocker treatment is not usually stopped before surgery.

**L86.3** `Complex Sentence` (0.594) → `decomposed`
- original: Starting a high dose of extended-release metoprolol shortly before non-cardiac surgery is avoided, because in one large trial this was linked to more slow heartbeats, low blood pressure, strokes, and deaths.
  - S1: Starting a high dose of extended-release metoprolol shortly before non-cardiac surgery is avoided.
  - S2: This practice is avoided because in one large trial it was linked to adverse outcomes.
  - S3: The adverse outcomes included more slow heartbeats, low blood pressure, strokes, and deaths.

## Who should not take metoprolol?

**L89.0** `Complex Sentence` (0.506) → `decomposed`
- original: You should not take metoprolol if you have a very slow heart rate, heart block beyond the first degree, sick sinus syndrome without a pacemaker, cardiogenic shock, or heart failure that is not under control.
  - S1: You should not take metoprolol if you have a very slow heart rate.
  - S2: You should not take metoprolol if you have heart block beyond the first degree.
  - S3: You should not take metoprolol if you have sick sinus syndrome without a pacemaker.
  - S4: You should not take metoprolol if you have cardiogenic shock.
  - S5: You should not take metoprolol if you have heart failure that is not under control.

**L90.0** `Simple Sentence` (0.929) → `passthrough`
- original: Metoprolol is not for you if you have:

**L91.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Severe bradycardia (a very slow heart rate)

**L92.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Second-degree or third-degree heart block, which is a fault in the heart's electrical signal

**L93.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Sick sinus syndrome, unless you have a permanent pacemaker

**L94.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Cardiogenic shock, when the heart cannot pump enough blood

**L95.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Decompensated heart failure, meaning heart failure that is not stable

**L96.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: An allergy to metoprolol or to any of the other ingredients in your product

**L97.0** `Compound Sentence` (0.457) → `decomposed`
- original: Immediate-release metoprolol tartrate tablets should also not be used if your top blood pressure reading is below 100 mmHg.
  - S1: Immediate-release metoprolol tartrate tablets should not be used.
  - S2: This applies if your top blood pressure reading is below 100 mmHg.

## Before taking metoprolol

**L100.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Tell your doctor or pharmacist if you:

**L101.0** `Incomplete Sentence` (0.791) → `excluded_incomplete`
- original: Take any other medicine for your heart or blood pressure, especially digoxin, clonidine, diltiazem, or verapamil

**L102.0** `Incomplete Sentence` (0.735) → `excluded_incomplete`
- original: Take fluoxetine, paroxetine, quinidine, or propafenone, which raise metoprolol levels in your blood

**L103.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Are pregnant, planning a pregnancy, or breastfeeding

**L104.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Have liver problems

**L105.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Have ever had a severe allergic reaction to anything, including foods and insect stings

**L106.0** `Simple Sentence` (0.989) → `passthrough`
- original: Kidney problems do not usually change your dose.

**L106.1** `Complex Sentence` (0.404) → `decomposed`
- original: The amount of metoprolol in your body and how long it lasts are not meaningfully different in people with kidney failure.
- pronoun resolved: The amount of metoprolol in your body and how long metoprolol lasts are not meaningfully different in people with kidney failure.
  - edits: “it” → “metoprolol”
  - S1: The amount of metoprolol in your body is not meaningfully different in people with kidney failure.
  - S2: How long metoprolol lasts is not meaningfully different in people with kidney failure.

## How should I take metoprolol?

**L109.0** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: Take metoprolol at the same time each day, exactly as prescribed.

**L109.1** `Simple Sentence` (0.779) → `passthrough`
- original: Do not change your dose or stop taking it without talking to your prescriber first.
- pronoun resolved: Do not change your dose or stop taking metoprolol without talking to your prescriber first.
  - edits: “it” → “metoprolol”

**L110.0** `Simple Sentence` (0.983) → `passthrough`
- original: Immediate-release metoprolol tartrate tablets should be taken with a meal or immediately after a meal.

**L110.1** `Compound-Complex Sentence` (0.69) → `decomposed`
- original: For extended-release tablets and capsules, taking your dose with or just after a meal is preferred, but food does not have a significant effect on how much metoprolol your body absorbs.
  - S1: Extended-release tablets and capsules are preferred to be taken with or just after a meal.
  - S2: Food does not have a significant effect on how much metoprolol your body absorbs.

**L111.0** `Incomplete Sentence` (0.94) → `excluded_incomplete`
- original: Keep taking metoprolol even if you feel well.

**L111.1** `Simple Sentence` (0.99) → `passthrough`
- original: High blood pressure often causes no symptoms.

**L112.0** `Simple Sentence` (0.776) → `passthrough`
- original: Extended-release tablets are scored and can be split in half if your prescriber tells you to.

**L112.1** `Incomplete Sentence` (0.972) → `excluded_incomplete`
- original: Swallow the whole or half tablet without crushing or chewing it.

**L113.0** `Simple Sentence` (0.986) → `passthrough`
- original: Extended-release capsules (Kapspargo Sprinkle) should be swallowed whole.

**L113.1** `Complex Sentence` (0.583) → `decomposed`
- original: If you cannot swallow the capsule, you can open it and sprinkle the contents over a teaspoon of soft food such as applesauce, pudding, or yogurt.
  - S1: If you cannot swallow the capsule, you can open it.
  - S2: You can sprinkle the contents over a teaspoon of soft food.
  - S3: Examples of soft food include applesauce, pudding, or yogurt.

**L113.2** `Incomplete Sentence` (0.612) → `excluded_incomplete`
- original: Swallow the mixture within 60 minutes and do not save any for later.

**L114.0** `Incomplete Sentence` (0.47) → `excluded_incomplete`
- original: Tell your doctor if you are fasting or vomiting, because this raises your risk of low blood sugar.

**L115.0** `Simple Sentence` (0.975) → `passthrough`
- original: Your blood pressure and heart rate will need checking regularly.

**L116.0** `Incomplete Sentence` (0.915) → `excluded_incomplete`
- original: Store metoprolol at room temperature, between 68°F and 77°F (20°C to 25°C), away from moisture and heat.

**L117.0** `Complex Sentence` (0.882) → `decomposed`
- original: Metoprolol injection is given into a vein by a healthcare professional in a coronary care unit or similar setting, where your blood pressure, heart rate, and heart tracing can be watched.
  - S1: Metoprolol injection is given into a vein by a healthcare professional.
  - S2: This is done in a coronary care unit or similar setting.
  - S3: In this setting, your blood pressure, heart rate, and heart tracing can be watched.

**L117.1** `Simple Sentence` (0.982) → `passthrough`
- original: You are then switched to metoprolol tablets.

## Metoprolol dosage

**L120.0** `Compound Sentence` (0.9) → `decomposed`
- original: The usual starting dose is 25 mg to 100 mg once a day for extended-release metoprolol, and 100 mg a day for immediate-release metoprolol.
  - S1: The usual starting dose is 25 mg to 100 mg once a day for extended-release metoprolol.
  - S2: The usual starting dose is 100 mg a day for immediate-release metoprolol.

**L120.1** `Compound Sentence` (0.593) → `decomposed`
- original: Your dose is then adjusted at intervals of a week or longer until your blood pressure or symptoms are controlled.
  - S1: Your dose is then adjusted at intervals of a week or longer.
  - S2: This continues until your blood pressure or symptoms are controlled.

**L121.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Metoprolol tartrate (immediate-release tablets) dosage for adults:

**L122.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Condition | Starting dose | Usual range

**L123.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: High blood pressure | 100 mg a day, as one dose or split into two | 100 mg to 450 mg a day.

**L123.1** `Simple Sentence` (0.985) → `passthrough`
- original: Doses above 450 mg a day have not been studied.

**L124.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Angina | 100 mg a day, split into two doses | 100 mg to 400 mg a day.

**L124.1** `Simple Sentence` (0.985) → `passthrough`
- original: Doses above 400 mg a day have not been studied.

**L125.0** `Incomplete Sentence` (0.782) → `excluded_incomplete`
- original: After a heart attack | 50 mg every 6 hours for 48 hours, starting 15 minutes after the last dose given into a vein.

**L125.1** `Compound Sentence` (0.456) → `decomposed`
- original: If the full intravenous dose was not tolerated, 25 mg is used.
  - S1: If the full intravenous dose was not tolerated.
  - S2: 25 mg is used.

**L125.2** `Simple Sentence` (0.97) → `passthrough`
- original: | Maintenance is 100 mg twice a day, continued for at least 3 months.

**L126.0** `Compound-Complex Sentence` (0.426) → `decomposed`
- original: With immediate-release tablets, a once-daily dose may not keep blood pressure controlled for the full 24 hours, especially at 100 mg. Splitting the dose or taking a larger daily dose may be needed.
  - S1: Immediate-release tablets are used.
  - S2: A once-daily dose may not keep blood pressure controlled for the full 24 hours.
  - S3: This lack of control is especially true at a 100 mg dose.
  - S4: Splitting the dose may be needed.
  - S5: Taking a larger daily dose may be needed.

**L127.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Metoprolol succinate (extended-release tablets and capsules) dosage for adults:

**L128.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Condition | Starting dose | Usual range

**L129.0** `Simple Sentence` (0.944) → `passthrough`
- original: High blood pressure | 25 mg to 100 mg once a day | Adjust weekly or less often.

**L129.1** `Simple Sentence` (0.985) → `passthrough`
- original: Doses above 400 mg a day have not been studied.

**L130.0** `Simple Sentence` (0.97) → `passthrough`
- original: Angina | 100 mg once a day | Increase weekly until symptoms are controlled or your heart rate slows noticeably.

**L130.1** `Simple Sentence` (0.985) → `passthrough`
- original: Doses above 400 mg a day have not been studied.

**L131.0** `Compound Sentence` (0.714) → `decomposed`
- original: Heart failure | 25 mg once a day for two weeks, or 12.5 mg once a day in more severe heart failure | Double the dose every two weeks to the highest dose you tolerate, up to 200 mg once a day.
  - S1: Heart failure is treated with 25 mg once a day for two weeks, or 12.5 mg once a day in more severe heart failure.
  - S2: The dose should be doubled every two weeks to the highest dose you tolerate, up to 200 mg once a day.

**L132.0** `Simple Sentence` (0.42) → `passthrough`
- original: Kapspargo Sprinkle capsules are not suitable to start heart failure treatment if a dose below 25 mg is needed.

**L133.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Metoprolol dosage for children:

**L134.0** `Compound Sentence` (0.865) → `decomposed`
- original: Extended-release metoprolol is the only form approved for children, and only for high blood pressure in children aged 6 years and older.
  - S1: Extended-release metoprolol is the only form approved for children.
  - S2: It is approved only for high blood pressure in children aged 6 years and older.

**L134.1** `Compound Sentence` (0.888) → `decomposed`
- original: The starting dose is 1 mg for each kilogram of body weight once a day, up to a maximum first dose of 50 mg. Doses above 2 mg/kg, or above 200 mg a day, have not been studied.
  - S1: The starting dose is 1 mg for each kilogram of body weight once a day.
  - S2: This is up to a maximum first dose of 50 mg.
  - S3: Doses above 2 mg/kg have not been studied.
  - S4: Doses above 200 mg a day have not been studied.

**L134.2** `Simple Sentence` (0.989) → `passthrough`
- original: Extended-release metoprolol has not been studied in children under 6 years.

**L135.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Dose adjustments:

**L136.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Liver problems.

**L136.1** `Incomplete Sentence` (0.98) → `excluded_incomplete`
- original: Start at a lower dose than usual and increase slowly.

**L137.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Kidney problems.

**L137.1** `Simple Sentence` (0.958) → `passthrough`
- original: No dose reduction is needed.

**L138.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Older adults.

**L138.1** `Compound Sentence` (0.478) → `decomposed`
- original: A low starting dose is generally used, because liver, kidney, and heart function are more often reduced and other medicines are more often involved.
  - S1: A low starting dose is generally used.
  - S2: This is because liver, kidney, and heart function are more often reduced.
  - S3: Other medicines are more often involved.

**L139.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Switching between forms.

**L139.1** `Simple Sentence` (0.636) → `passthrough`
- original: When changing from immediate-release to extended-release metoprolol, the same total daily dose is used.

## What happens if I miss a dose of metoprolol?

**L142.0** `Simple Sentence` (0.453) → `passthrough`
- original: Skip the missed dose and take your next dose at the usual time.

**L142.1** `Simple Sentence` (0.494) → `passthrough`
- original: Do not take two doses at once and do not double up to catch up.

## What happens if I take too much metoprolol?

**L145.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L146.0** `Simple Sentence` (0.908) → `passthrough`
- original: Too much metoprolol can cause a dangerously slow heartbeat, very low blood pressure, and cardiogenic shock.

**L146.1** `Compound Sentence` (0.647) → `decomposed`
- original: It can also cause heart block, heart failure, wheezing, low oxygen levels, drowsiness or loss of consciousness, nausea, and vomiting.
- pronoun resolved: Metoprolol can also cause heart block, heart failure, wheezing, low oxygen levels, drowsiness or loss of consciousness, nausea, and vomiting.
  - edits: “It” → “Metoprolol”
  - S1: Metoprolol can also cause heart block.
  - S2: It can cause heart failure.
  - S3: It can cause wheezing.
  - S4: It can cause low oxygen levels.
  - S5: It can cause drowsiness or loss of consciousness.
  - S6: It can cause nausea.
  - S7: It can cause vomiting.

**L146.2** `Simple Sentence` (0.989) → `passthrough`
- original: Overdose is treated in an intensive care setting.

**L146.3** `Simple Sentence` (0.991) → `passthrough`
- original: Dialysis does not remove metoprolol effectively.

## What should I avoid while taking metoprolol?

**L149.0** `Incomplete Sentence` (0.974) → `excluded_incomplete`
- original: Avoid driving and other tasks that need alertness until you know how metoprolol affects you.

**L149.1** `Simple Sentence` (0.965) → `passthrough`
- original: It can make you feel tired or less alert.

**L150.0** `Incomplete Sentence` (0.878) → `excluded_incomplete`
- original: Get up slowly from sitting or lying down, because metoprolol can make you feel dizzy or lightheaded.

**L151.0** `Incomplete Sentence` (0.967) → `excluded_incomplete`
- original: Avoid alcohol if you take Kapspargo Sprinkle capsules.

**L151.1** `Complex Sentence` (0.718) → `decomposed`
- original: Alcohol makes the capsule release its metoprolol much faster, which raises the risk of side effects.
- pronoun resolved: Alcohol makes the capsule release metoprolol's metoprolol much faster, which raises the risk of side effects.
  - edits: “its” → “metoprolol's”
  - S1: Alcohol makes the capsule release metoprolol much faster.
  - S2: This raises the risk of side effects.

**L152.0** `Simple Sentence` (0.493) → `passthrough`
- original: Do not stop taking metoprolol on your own, even if you feel fine.

## What other drugs affect metoprolol?

**L155.0** `Compound Sentence` (0.581) → `decomposed`
- original: The interactions that matter most are medicines that also slow the heart and medicines that block the liver enzyme CYP2D6, which raises metoprolol levels in your blood.
  - S1: The interactions that matter most are medicines that also slow the heart.
  - S2: The interactions that matter most are medicines that block the liver enzyme CYP2D6.
  - S3: This enzyme raises metoprolol levels in your blood.

**L156.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Digoxin, clonidine, diltiazem, and verapamil.

**L156.1** `Simple Sentence` (0.985) → `passthrough`
- original: These all slow the heart's electrical signal and heart rate.

**L156.2** `Simple Sentence` (0.851) → `passthrough`
- original: Taking them with metoprolol raises the risk of a very slow heartbeat.
- pronoun resolved: Taking Digoxin, clonidine, diltiazem, and verapamil with metoprolol raises the risk of a very slow heartbeat.
  - edits: “them” → “Digoxin, clonidine, diltiazem, and verapamil”

**L157.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Clonidine, when stopping either medicine.

**L157.1** `Compound-Complex Sentence` (0.664) → `decomposed`
- original: If you take both, the metoprolol is stopped several days before clonidine is slowly withdrawn, because beta blockers can worsen the blood pressure rebound that follows clonidine withdrawal.
  - S1: You take both medications.
  - S2: Metoprolol is stopped several days before clonidine is slowly withdrawn.
  - S3: Beta blockers can worsen the blood pressure rebound that follows clonidine withdrawal.
  - S4: Clonidine withdrawal causes a blood pressure rebound.

**L158.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Quinidine, fluoxetine, paroxetine, and propafenone.

**L158.1** `Simple Sentence` (0.992) → `passthrough`
- original: These strong CYP2D6 blockers double the amount of metoprolol in your blood.

**L158.2** `Simple Sentence` (0.823) → `passthrough`
- original: Quinidine tripled levels of one form of metoprolol and doubled how long it lasted.
- pronoun resolved: Quinidine tripled levels of one form of metoprolol and doubled how long metoprolol lasted.
  - edits: “it” → “metoprolol”

**L158.3** `Simple Sentence` (0.988) → `passthrough`
- original: Weaker CYP2D6 blockers are likely to raise levels too.

**L159.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Reserpine and MAO inhibitors.

**L159.1** `Complex Sentence` (0.611) → `decomposed`
- original: These deplete adrenaline-type chemicals and can add to metoprolol's effect, causing low blood pressure or a marked slowing of the heart.
  - S1: These deplete adrenaline-type chemicals.
  - S2: These can add to metoprolol's effect.
  - S3: This can cause low blood pressure or a marked slowing of the heart.

**L160.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Epinephrine.

**L160.1** `Complex Sentence` (0.952) → `decomposed`
- original: If you need epinephrine for a severe allergic reaction, the usual dose may not work as well while you are on a beta blocker.
  - S1: If you need epinephrine for a severe allergic reaction, the usual dose may not work as well.
  - S2: This reduced effectiveness occurs while you are on a beta blocker.

**L161.0** `Complex Sentence` (0.403) → `decomposed`
- original: Other medicines that lower blood pressure or heart rate, including fingolimod, can add to metoprolol's effect.
  - S1: Other medicines that lower blood pressure or heart rate can add to metoprolol's effect.
  - S2: Fingolimod is one of these medicines.
  - S3: Fingolimod lowers blood pressure or heart rate.

**L162.0** `Incomplete Sentence` (0.831) → `excluded_incomplete`
- original: Tell each of your healthcare providers about all medicines you take, including prescription and over-the-counter medicines, vitamins, and herbal products.

**L162.1** `Simple Sentence` (0.949) → `passthrough`
- original: Not all possible interactions are listed here.

## Can you take metoprolol during pregnancy or while breastfeeding?

**L165.0** `Simple Sentence` (0.985) → `passthrough`
- original: Metoprolol crosses the placenta and passes into breast milk in small amounts.

**L165.1** `Incomplete Sentence` (0.82) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant, planning a pregnancy, or breastfeeding.

**L166.0** `Complex Sentence` (0.519) → `decomposed`
- original: Studies published to date have not shown a link between metoprolol taken in pregnancy and major birth defects or miscarriage.
  - S1: Studies published to date have not shown a link between metoprolol taken in pregnancy and major birth defects or miscarriage.

**L166.1** `Compound Sentence` (0.9) → `decomposed`
- original: Reports on growth restriction, early birth, and death around the time of birth have been inconsistent, and those studies have limitations that make them hard to interpret.
- pronoun resolved: Reports on growth restriction, early birth, and death around the time of birth have been inconsistent, and those studies have limitations that make studies hard to interpret.
  - edits: “them” → “studies”
  - S1: Reports on growth restriction, early birth, and death around the time of birth have been inconsistent.
  - S2: Those studies have limitations that make studies hard to interpret.

**L166.2** `Simple Sentence` (0.936) → `passthrough`
- original: Untreated high blood pressure and untreated heart failure in pregnancy carry their own serious risks for both mother and baby.

**L167.0** `Compound Sentence` (0.807) → `decomposed`
- original: Babies born to mothers taking metoprolol may have low blood pressure, low blood sugar, a slow heartbeat, or slow breathing, so they are watched after birth.
- pronoun resolved: Babies born to mothers taking metoprolol may have low blood pressure, low blood sugar, a slow heartbeat, or slow breathing, so Babies born to mothers taking metoprolol are watched after birth.
  - edits: “they” → “Babies born to mothers taking metoprolol”
  - S1: Babies born to mothers taking metoprolol may have low blood pressure, low blood sugar, a slow heartbeat, or slow breathing.
  - S2: Babies born to mothers taking metoprolol are watched after birth.

**L168.0** `Complex Sentence` (0.655) → `decomposed`
- original: The amount of metoprolol a breastfed baby receives is estimated at 0.05 mg to under 1 mg a day, which is about 0.5% to 2% of the mother's weight-adjusted dose.
  - S1: The amount of metoprolol a breastfed baby receives is estimated at 0.05 mg to under 1 mg a day.
  - S2: This amount is about 0.5% to 2% of the mother's weight-adjusted dose.

**L168.1** `Simple Sentence` (0.987) → `passthrough`
- original: No side effects in breastfed babies have been identified.

**L168.2** `Simple Sentence` (0.799) → `passthrough`
- original: Babies are still monitored for a slow heartbeat and for signs such as unusual sleepiness.

## Popular FAQ

**L171.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Q: Does metoprolol cause weight gain?

**L171.1** `Simple Sentence` (0.974) → `passthrough`
- original: A: Metoprolol is not likely to cause weight gain.

**L171.2** `Simple Sentence` (0.524) → `passthrough`
- original: However, weight gain can be a warning sign that heart failure is getting worse.

**L171.3** `Simple Sentence` (0.403) → `passthrough`
- original: If you are taking metoprolol for heart failure, tell your doctor right away if you gain weight suddenly.

**L171.4** `Complex Sentence` (0.429) → `decomposed`
- original: This weight gain is due to extra fluid in the body that may cause swelling in the feet, ankles, legs and belly.
  - S1: This weight gain is due to extra fluid in the body.
  - S2: The extra fluid may cause swelling in the feet, ankles, legs and belly.

**L171.5** `Simple Sentence` (0.968) → `passthrough`
- original: The fluid builds up because the heart isn’t working as well as it should.
- pronoun resolved: The fluid builds up because the heart isn’t working as well as heart should.
  - edits: “it” → “heart”

**L172.0** `Incomplete Sentence` (0.831) → `excluded_incomplete`
- original: Q: Does metoprolol lower blood pressure?

**L172.1** `Complex Sentence` (0.701) → `decomposed`
- original: A: Yes, metoprolol causes the blood vessels to relax, which helps to lower blood pressure.
  - S1: Metoprolol causes the blood vessels to relax.
  - S2: This helps to lower blood pressure.

**L172.2** `Complex Sentence` (0.939) → `decomposed`
- original: If you are prescribed metoprolol for high blood pressure, your doctor may ask you to check your blood pressure regularly at home with an automatic, cuff-style device that goes around your upper arm.
  - S1: If you are prescribed metoprolol for high blood pressure, your doctor may ask you to check your blood pressure regularly at home.
  - S2: You can use an automatic, cuff-style device to check your blood pressure.
  - S3: The device goes around your upper arm.

**L172.3** `Complex Sentence` (0.504) → `decomposed`
- original: Keeping track of your blood pressure at home is one way to help your doctor know if the prescribed dosage of metoprolol is working for you.
  - S1: Keeping track of your blood pressure at home is one way to help your doctor.
  - S2: This helps the doctor know if the prescribed dosage of metoprolol is working for you.
  - S3: The prescribed dosage of metoprolol is intended to work for you.

**L173.0** `Incomplete Sentence` (0.94) → `excluded_incomplete`
- original: Q: Should I take metoprolol in the morning or at night?

**L173.1** `Simple Sentence` (0.946) → `passthrough`
- original: A: When you take metoprolol depends on which salt form is prescribed.

**L173.2** `Compound Sentence` (0.936) → `decomposed`
- original: Metoprolol tartrate is usually taken twice daily, so it may be taken in the morning then at night.
- pronoun resolved: Metoprolol tartrate is usually taken twice daily, so Metoprolol tartrate may be taken in the morning then at night.
  - edits: “it” → “Metoprolol tartrate”
  - S1: Metoprolol tartrate is usually taken twice daily.
  - S2: Metoprolol tartrate may be taken in the morning then at night.

**L173.3** `Compound Sentence` (0.907) → `decomposed`
- original: Metoprolol succinate is taken once daily, so it may be taken either morning or night.
- pronoun resolved: Metoprolol succinate is taken once daily, so Metoprolol succinate may be taken either morning or night.
  - edits: “it” → “Metoprolol succinate”
  - S1: Metoprolol succinate is taken once daily.
  - S2: Metoprolol succinate may be taken either morning or night.

**L173.4** `Simple Sentence` (0.968) → `passthrough`
- original: Both forms are usually taken with or immediately after a meal.

**L173.5** `Incomplete Sentence` (0.965) → `excluded_incomplete`
- original: Follow your health care provider’s directions for when to take metoprolol.

**L174.0** `Simple Sentence` (0.808) → `passthrough`
- original: Q: What is the best time of day to take blood pressure medication?

**L174.1** `Complex Sentence` (0.932) → `decomposed`
- original: A: Research has suggested that taking your blood pressure medication at night instead of in the morning can provide better blood pressure control at night without compromising daytime blood pressure control and reduce your overall risk of dying because of cardiovascular disease by 45%.
  - S1: Research has suggested that taking your blood pressure medication at night instead of in the morning can provide better blood pressure control at night.
  - S2: This approach does not compromise daytime blood pressure control.
  - S3: It can reduce your overall risk of dying because of cardiovascular disease by 45%.

**L175.0** `Incomplete Sentence` (0.772) → `excluded_incomplete`
- original: Q: Does metoprolol lower resting heart rate?

**L175.1** `Simple Sentence` (0.984) → `passthrough`
- original: A: Yes, metoprolol can lower resting heart rate.

**L175.2** `Complex Sentence` (0.712) → `decomposed`
- original: It is a beta-blocking medication that is used to lower blood pressure, as well as relieve chest pain from angina pectoris.
- pronoun resolved: Metoprolol is a beta-blocking medication that is used to lower blood pressure, as well as relieve chest pain from angina pectoris.
  - edits: “It” → “Metoprolol”
  - S1: Metoprolol is a beta-blocking medication.
  - S2: Metoprolol is used to lower blood pressure.
  - S3: Metoprolol is used to relieve chest pain from angina pectoris.

**L176.0** `Incomplete Sentence` (0.939) → `excluded_incomplete`
- original: Q: Metoprolol Succinate vs Tartrate: What's the difference between them?

**L176.1** `Simple Sentence` (0.975) → `passthrough`
- original: A: Metoprolol is available as two different salts: metoprolol tartrate and metoprolol succinate.

**L176.2** `Compound-Complex Sentence` (0.851) → `decomposed`
- original: The main difference between metoprolol tartrate and metoprolol succinate is that metoprolol tartrate is only available as an immediate-release tablet which means it must be taken several times per day, whereas metoprolol succinate is an extended-release tablet that can be taken once a day.
  - S1: The main difference between metoprolol tartrate and metoprolol succinate is that metoprolol tartrate is only available as an immediate-release tablet.
  - S2: Metoprolol tartrate must be taken several times per day.
  - S3: Metoprolol succinate is an extended-release tablet.
  - S4: Metoprolol succinate can be taken once a day.

**L176.3** `Compound Sentence` (0.898) → `decomposed`
- original: As a result, there are differences in the dosages and indications for both metoprolol tartrate and metoprolol succinate and they are not considered interchangeable.
- pronoun resolved: As a result, there are differences in the dosages and indications for both metoprolol tartrate and metoprolol succinate and metoprolol tartrate and metoprolol succinate are not considered interchangeable.
  - edits: “they” → “metoprolol tartrate and metoprolol succinate”
  - S1: As a result, there are differences in the dosages and indications for both metoprolol tartrate and metoprolol succinate.
  - S2: Metoprolol tartrate and metoprolol succinate are not considered interchangeable.

**L177.0** `Incomplete Sentence` (0.964) → `excluded_incomplete`
- original: Q: What medications are known to cause hair loss?

**L177.1** `Simple Sentence` (0.594) → `passthrough`
- original: A: Medication-induced hair loss represents a significant concern for patients across multiple therapeutic categories.

**L177.2** `Complex Sentence` (0.956) → `decomposed`
- original: While chemotherapy drugs are most commonly associated with severe hair loss, many commonly prescribed medications-including antibiotics, psychiatric drugs, cardiovascular agents, and hormonal therapies-can also cause this distressing side effect.
  - S1: Chemotherapy drugs are most commonly associated with severe hair loss.
  - S2: Many commonly prescribed medications can also cause this distressing side effect.
  - S3: These medications include antibiotics, psychiatric drugs, cardiovascular agents, and hormonal therapies.

**L178.0** `Incomplete Sentence` (0.863) → `excluded_incomplete`
- original: Q: Does metoprolol make you sleepy?

**L178.1** `Simple Sentence` (0.977) → `passthrough`
- original: A: Yes, metoprolol can make you sleepy.

**L178.2** `Simple Sentence` (0.707) → `passthrough`
- original: One reason may be because beta blockers slow down your heart rate and lower your blood pressure.

**L179.0** `Incomplete Sentence` (0.953) → `excluded_incomplete`
- original: Q: How long does it take for metoprolol to work?

**L179.1** `Simple Sentence` (0.826) → `passthrough`
- original: A: How long it takes metoprolol to work depends on what form is given and what condition is being treated.
- pronoun resolved: A: How long metoprolol takes metoprolol to work depends on what form is given and what condition is being treated.
  - edits: “it” → “metoprolol”

**L179.2** `Compound Sentence` (0.805) → `decomposed`
- original: Effects on heart rate can be seen within one hour after taking metoprolol tartrate tablets and within 20 minutes after the intravenous form is given.
  - S1: Effects on heart rate can be seen within one hour after taking metoprolol tartrate tablets.
  - S2: Effects on heart rate can be seen within 20 minutes after the intravenous form is given.

**L179.3** `Simple Sentence` (0.987) → `passthrough`
- original: The onset of action of metoprolol succinate is similar to metoprolol tartrate.
