# Sertraline — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/sertraline.txt` · 355 sentences · 40 changed by pronoun resolution · 705 sentences sent to EDC

## What is sertraline?

**L5.0** `Complex Sentence` (0.762) → `decomposed`
- original: Sertraline is a prescription medicine used to treat depression, obsessive-compulsive disorder (OCD), panic disorders, posttraumatic stress disorder (PTSD), social anxiety disorder, and premenstrual dysphoric disorder (PMDD).
  - S1: Sertraline is a prescription medicine.
  - S2: Sertraline is used to treat depression.
  - S3: Sertraline is used to treat obsessive-compulsive disorder (OCD).
  - S4: Sertraline is used to treat panic disorders.
  - S5: Sertraline is used to treat posttraumatic stress disorder (PTSD).
  - S6: Sertraline is used to treat social anxiety disorder.
  - S7: Sertraline is used to treat premenstrual dysphoric disorder (PMDD).

**L5.1** `Compound Sentence` (0.952) → `decomposed`
- original: It is sold under the brand name Zoloft, and generic sertraline is widely available.
- pronoun resolved: Sertraline is sold under the brand name Zoloft, and generic sertraline is widely available.
  - edits: “It” → “Sertraline”
  - S1: Sertraline is sold under the brand name Zoloft.
  - S2: Generic sertraline is widely available.

**L6.0** `Simple Sentence` (0.98) → `passthrough`
- original: Sertraline belongs to a group of medicines called selective serotonin reuptake inhibitors, or SSRIs.

**L6.1** `Complex Sentence` (0.588) → `decomposed`
- original: It increases serotonin activity in the brain by blocking the reuptake of serotonin (a chemical messenger that nerve cells use to communicate) back into nerve cells, so more of it stays available.
- pronoun resolved: Sertraline increases serotonin activity in the brain by blocking the reuptake of serotonin (a chemical messenger that nerve cells use to communicate) back into nerve cells, so more of serotonin stays available.
  - edits: “It” → “Sertraline”; “it” → “serotonin”
  - S1: Sertraline increases serotonin activity in the brain.
  - S2: It does this by blocking the reuptake of serotonin back into nerve cells.
  - S3: Serotonin is a chemical messenger that nerve cells use to communicate.
  - S4: Consequently, more serotonin stays available.

**L6.2** `Compound Sentence` (0.967) → `decomposed`
- original: Sertraline has only very weak effects on the reuptake of norepinephrine and dopamine, and it does not block monoamine oxidase.
- pronoun resolved: Sertraline has only very weak effects on the reuptake of norepinephrine and dopamine, and Sertraline does not block monoamine oxidase.
  - edits: “it” → “Sertraline”
  - S1: Sertraline has only very weak effects on the reuptake of norepinephrine and dopamine.
  - S2: Sertraline does not block monoamine oxidase.

**L7.0** `Compound Sentence` (0.603) → `decomposed`
- original: Sertraline is available as tablets (25 mg, 50 mg, and 100 mg), oral solution (20 mg/mL), and capsules (150 mg and 200 mg).
  - S1: Sertraline is available as tablets (25 mg, 50 mg, and 100 mg).
  - S2: It is available as an oral solution (20 mg/mL).
  - S3: It is available as capsules (150 mg and 200 mg).

**L8.0** `Simple Sentence` (0.986) → `passthrough`
- original: Sertraline is not a controlled substance.

## What is sertraline used for?

**L11.0** `Simple Sentence` (0.989) → `passthrough`
- original: Sertraline is FDA-approved to treat six conditions in adults:

**L12.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Major depressive disorder (MDD), the clinical term for depression.

**L13.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Obsessive-compulsive disorder (OCD), where unwanted thoughts drive repeated behaviors.

**L14.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Panic disorder, which causes sudden attacks of intense fear along with physical symptoms.

**L15.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Posttraumatic stress disorder (PTSD), which can follow a frightening or traumatic event.

**L16.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Social anxiety disorder (SAD), also called social phobia.

**L17.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: Premenstrual dysphoric disorder (PMDD), a severe form of premenstrual symptoms.

**L18.0** `Simple Sentence` (0.969) → `passthrough`
- original: In children and teenagers, sertraline is approved only for OCD, from age 6 upward.

**L18.1** `Compound Sentence` (0.668) → `decomposed`
- original: Its safety and effectiveness have not been established in children under 6 years of age, or in children and teenagers for any condition other than OCD.
- pronoun resolved: Sertraline's safety and effectiveness have not been established in children under 6 years of age, or in children and teenagers for any condition other than OCD.
  - edits: “Its” → “Sertraline's”
  - S1: Sertraline's safety and effectiveness have not been established in children under 6 years of age.
  - S2: Sertraline's safety and effectiveness have not been established in children and teenagers for any condition other than OCD.

**L19.0** `Simple Sentence` (0.984) → `passthrough`
- original: Not every sertraline product is approved for all six conditions:

**L20.0** `Simple Sentence` (0.988) → `passthrough`
- original: Sertraline tablets and oral solution are approved for all of them.

**L21.0** `Simple Sentence` (0.603) → `passthrough`
- original: Sertraline 150 mg and 200 mg capsules are approved only for depression in adults and for OCD in adults and children aged 6 and over.

## Boxed warning: suicidal thoughts and behaviors

**L24.0** `Simple Sentence` (0.966) → `passthrough`
- original: Sertraline carries a boxed warning, the FDA's most serious type of warning.

**L24.1** `Simple Sentence` (0.909) → `passthrough`
- original: Antidepressants increased the risk of suicidal thoughts and behavior in children, teenagers, and young adults in short-term studies.

**L25.0** `Complex Sentence` (0.95) → `decomposed`
- original: In pooled analyses of placebo-controlled antidepressant trials covering about 77,000 adults and more than 4,500 children and teenagers, the risk of suicidal thoughts and behaviors in people aged 24 and under was higher with an antidepressant than with placebo.
  - S1: Pooled analyses of placebo-controlled antidepressant trials were conducted.
  - S2: The trials covered about 77,000 adults and more than 4,500 children and teenagers.
  - S3: The risk of suicidal thoughts and behaviors in people aged 24 and under was higher with an antidepressant than with placebo.

**L25.1** `Compound-Complex Sentence` (0.644) → `decomposed`
- original: The risk varied considerably between different antidepressants, and it also varied by condition, with the highest rate in people being treated for depression.
- pronoun resolved: The risk varied considerably between different antidepressants, and risk also varied by condition, with the highest rate in people being treated for depression.
  - edits: “it” → “risk”
  - S1: The risk varied considerably between different antidepressants.
  - S2: The risk also varied by condition.
  - S3: The highest rate of risk was in people being treated for depression.

**L25.2** `Simple Sentence` (0.659) → `passthrough`
- original: The difference between antidepressant and placebo, per 1,000 patients treated, was:

**L26.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Age (years) | Difference compared with placebo

**L27.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Under 18 | 14 more patients with suicidal thoughts or behaviors

**L28.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: 18 to 24 | 5 more patients

**L29.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: 25 to 64 | 1 fewer patient

**L30.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: 65 and over | 6 fewer patients

**L31.0** `Simple Sentence` (0.965) → `passthrough`
- original: It is not known whether this risk continues beyond about four months of treatment.

**L31.1** `Compound Sentence` (0.858) → `decomposed`
- original: There is good evidence that antidepressants delay depression coming back in adults, and depression itself raises the risk of suicidal thoughts and behaviors.
  - S1: There is good evidence that antidepressants delay depression coming back in adults.
  - S2: Depression itself raises the risk of suicidal thoughts and behaviors.

**L32.0** `Complex Sentence` (0.93) → `decomposed`
- original: Anyone taking sertraline should be watched closely for worsening symptoms and for new or sudden changes in mood, behavior, thoughts, or feelings, especially in the first few months of treatment and whenever the dose is changed.
  - S1: Anyone taking sertraline should be watched closely.
  - S2: They should be watched for worsening symptoms.
  - S3: They should be watched for new or sudden changes in mood, behavior, thoughts, or feelings.
  - S4: This monitoring is especially important in the first few months of treatment.
  - S5: This monitoring is also important whenever the dose is changed.

**L32.1** `Incomplete Sentence` (0.491) → `excluded_incomplete`
- original: Call your healthcare provider right away, or call 911 in an emergency, if you notice:

**L33.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: thoughts about suicide or dying, or attempts to harm yourself

**L34.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: new or worse depression, anxiety, or panic attacks

**L35.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: feeling agitated, restless, angry, or irritable

**L36.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: acting aggressive or violent, or acting on dangerous impulses

**L37.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: trouble sleeping

**L38.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: a big increase in activity or talking more than is normal for you

**L39.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: any other unusual change in behavior or mood

**L40.0** `Compound Sentence` (0.367) → `decomposed`
- original: Tell family members or caregivers which symptoms to watch for, so they can call your provider if you are not able to.
- pronoun resolved: Tell family members or caregivers which symptoms to watch for, so family members or caregivers can call your provider if you are not able to.
  - edits: “they” → “family members or caregivers”
  - S1: Tell family members or caregivers which symptoms to watch for.
  - S2: Family members or caregivers can call your provider if you are not able to.

## Sertraline side effects

**L43.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Common sertraline side effects:

**L44.0** `Compound Sentence` (0.445) → `decomposed`
- original: The most common sertraline side effects are nausea, diarrhea or loose stools, trouble sleeping, dry mouth, tiredness, dizziness, sleepiness, tremor, indigestion, agitation, reduced appetite, increased sweating, and sexual problems.
  - S1: The most common sertraline side effects are nausea, diarrhea or loose stools.
  - S2: They include trouble sleeping, dry mouth, tiredness, dizziness, and sleepiness.
  - S3: Other common side effects are tremor, indigestion, agitation, reduced appetite, increased sweating, and sexual problems.

**L45.0** `Complex Sentence` (0.88) → `decomposed`
- original: The table below shows how often each side effect was reported in pooled placebo-controlled trials in 3,066 adults, compared with 2,293 people taking placebo.
  - S1: The table below shows how often each side effect was reported.
  - S2: The data comes from pooled placebo-controlled trials.
  - S3: The trials included 3,066 adults.
  - S4: The trials included 2,293 people taking placebo.

**L46.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Side effect | Sertraline | Placebo

**L47.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Nausea | 26% | 12%

**L48.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Diarrhea or loose stools | 20% | 10%

**L49.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Insomnia (trouble sleeping) | 20% | 13%

**L50.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Dry mouth | 14% | 9%

**L51.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Fatigue (tiredness) | 12% | 8%

**L52.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Dizziness | 12% | 8%

**L53.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Somnolence (sleepiness) | 11% | 6%

**L54.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Tremor (shaking) | 9% | 2%

**L55.0** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Dyspepsia (indigestion) | 8% | 4%

**L56.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Agitation | 8% | 5%

**L57.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Decreased appetite | 7% | 2%

**L58.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Hyperhidrosis (heavy sweating) | 7% | 3%

**L59.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Constipation | 6% | 4%

**L60.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Decreased libido (lower sex drive) | 6% | 2%

**L61.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Palpitations | 4% | 2%

**L62.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Visual impairment | 4% | 2%

**L63.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Vomiting | 4% | 1%

**L64.0** `Simple Sentence` (0.981) → `passthrough`
- original: Some side effects were more common with particular conditions.

**L64.1** `Compound Sentence` (0.879) → `decomposed`
- original: Sleepiness was more common in depression trials, insomnia and agitation in OCD trials, constipation and agitation in panic disorder trials, tiredness in PTSD trials, and insomnia, dizziness, tiredness, dry mouth, and a general feeling of being unwell in social anxiety disorder trials.
  - S1: Sleepiness was more common in depression trials.
  - S2: Insomnia and agitation were more common in OCD trials.
  - S3: Constipation and agitation were more common in panic disorder trials.
  - S4: Tiredness was more common in PTSD trials.
  - S5: Insomnia, dizziness, tiredness, dry mouth, and a general feeling of being unwell were more common in social anxiety disorder trials.

**L64.2** `Simple Sentence` (0.832) → `passthrough`
- original: In PMDD trials, sleepiness, dry mouth, dizziness, tiredness, and stomach pain were more common.

**L65.0** `Complex Sentence` (0.675) → `decomposed`
- original: In these trials, 12% of people taking sertraline stopped treatment because of a side effect, compared with 4% of people taking placebo.
  - S1: In these trials, 12% of people taking sertraline stopped treatment.
  - S2: They stopped treatment because of a side effect.
  - S3: This was compared with 4% of people taking placebo.

**L65.1** `Compound Sentence` (0.709) → `decomposed`
- original: The most common reasons for stopping were nausea (3%), diarrhea (2%), agitation (2%), and insomnia (2%).
  - S1: The most common reason for stopping was nausea (3%).
  - S2: Diarrhea (2%) was another common reason for stopping.
  - S3: Agitation (2%) was also a common reason for stopping.
  - S4: Insomnia (2%) was a common reason for stopping.

**L66.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Sexual side effects of sertraline:

**L67.0** `Simple Sentence` (0.991) → `passthrough`
- original: SSRIs including sertraline can cause sexual problems.

**L67.1** `Complex Sentence` (0.65) → `decomposed`
- original: In men, this can mean delayed ejaculation or being unable to ejaculate, lower sex drive, and difficulty getting or keeping an erection.
- pronoun resolved: In men, sexual problems can mean delayed ejaculation or being unable to ejaculate, lower sex drive, and difficulty getting or keeping an erection.
  - edits: “this” → “sexual problems”
  - S1: In men, sexual problems can mean delayed ejaculation or being unable to ejaculate.
  - S2: Sexual problems can also mean lower sex drive.
  - S3: Sexual problems can also mean difficulty getting or keeping an erection.

**L67.2** `Complex Sentence` (0.57) → `decomposed`
- original: In women, it can mean lower sex drive and delayed orgasm or being unable to have an orgasm.
- pronoun resolved: In women, sexual problems can mean lower sex drive and delayed orgasm or being unable to have an orgasm.
  - edits: “it” → “sexual problems”
  - S1: In women, sexual problems can mean lower sex drive.
  - S2: Sexual problems can mean delayed orgasm.
  - S3: Sexual problems can mean being unable to have an orgasm.

**L68.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Sexual side effect | Sertraline | Placebo

**L69.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Ejaculation failure (men) | 8% | 1%

**L70.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Decreased libido (men) | 7% | 2%

**L71.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Erectile dysfunction (men) | 4% | 1%

**L72.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Ejaculation disorder (men) | 3% | 0%

**L73.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Male sexual dysfunction | 2% | 0%

**L74.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Decreased libido (women) | 4% | 2%

**L75.0** `Compound Sentence` (0.719) → `decomposed`
- original: Changes in sex drive and sexual function can also be part of depression and anxiety themselves, so the timing of when symptoms started matters.
  - S1: Changes in sex drive and sexual function can also be part of depression and anxiety themselves.
  - S2: The timing of when symptoms started matters.

**L75.1** `Complex Sentence` (0.896) → `decomposed`
- original: These numbers may underestimate how often sexual side effects happen, because people and their providers do not always raise the subject.
  - S1: These numbers may underestimate how often sexual side effects happen.
  - S2: People and their providers do not always raise the subject.
  - S3: The underestimation occurs because people and their providers do not always raise the subject.

**L75.2** `Incomplete Sentence` (0.972) → `excluded_incomplete`
- original: Tell your provider about any change in sexual function, since there may be ways to manage it.

**L76.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious sertraline side effects:

**L77.0** `Compound Sentence` (0.513) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to sertraline: rash, hives, swelling of the face, lips, tongue, or throat, or difficulty breathing.
  - S1: Get emergency medical help if you have signs of an allergic reaction to sertraline.
  - S2: These signs include a rash, hives, swelling of the face, lips, tongue, or throat, or difficulty breathing.

**L78.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L79.0** `Incomplete Sentence` (0.247) → `excluded_incomplete`
- original: signs of serotonin syndrome, which can be life threatening: agitation, hallucinations, confusion, coma or other changes in mental state, a racing heartbeat, high or low blood pressure, dizziness, heavy sweating, fever, muscle stiffness, twitching or overactive reflexes, loss of coordination, seizures, nausea, vomiting, or diarrhea;

**L80.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: unusual bleeding or bruising, including nosebleeds, bleeding gums, blood in vomit or stools, or black tarry stools;

**L81.0** `Incomplete Sentence` (0.917) → `excluded_incomplete`
- original: signs of a manic episode: greatly increased energy, severe trouble sleeping, racing thoughts, reckless behavior, unusually grand ideas, excessive happiness or irritability, or talking more or faster than usual;

**L82.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: seizures or convulsions;

**L83.0** `Incomplete Sentence` (0.332) → `excluded_incomplete`
- original: eye pain, changes in vision, or swelling or redness in or around the eye, which can be signs of angle-closure glaucoma (a sudden rise in pressure inside the eye);

**L84.0** `Complex Sentence` (0.452) → `decomposed`
- original: signs of low sodium in the blood (hyponatremia): headache, trouble concentrating or thinking, memory problems, confusion, weakness, or feeling unsteady, which can lead to falls.
  - S1: Signs of low sodium in the blood (hyponatremia) include headache, trouble concentrating or thinking, memory problems, confusion, weakness, or feeling unsteady.
  - S2: These symptoms can lead to falls.

**L84.1** `Simple Sentence` (0.923) → `passthrough`
- original: Severe cases have caused hallucinations, fainting, seizures, coma, and death;

**L85.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: fainting, chest discomfort, or an irregular heartbeat, which can be signs of a heart rhythm problem called QTc prolongation.

**L86.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Sertraline side effects in children and teenagers:

**L87.0** `Simple Sentence` (0.737) → `passthrough`
- original: The overall pattern of side effects in 281 children and teenagers treated with sertraline was generally similar to that seen in adults.

**L87.1** `Compound-Complex Sentence` (0.765) → `decomposed`
- original: Side effects reported in at least 2% of children and teenagers, and at least twice as often as with placebo, that were not common in adults were fever, hyperkinesia (abnormally increased movement), urinary incontinence, aggression, nosebleeds, purpura (purple spots under the skin), joint pain, weight loss, muscle twitching, and anxiety.
  - S1: Side effects were reported in at least 2% of children and teenagers.
  - S2: These side effects occurred at least twice as often as with placebo.
  - S3: These side effects were not common in adults.
  - S4: The reported side effects included fever.
  - S5: The reported side effects included hyperkinesia.
  - S6: Hyperkinesia is abnormally increased movement.
  - S7: The reported side effects included urinary incontinence.
  - S8: The reported side effects included aggression.
  - S9: The reported side effects included nosebleeds.
  - S10: The reported side effects included purpura.
  - S11: Purpura are purple spots under the skin.
  - S12: The reported side effects included joint pain.
  - S13: The reported side effects included weight loss.
  - S14: The reported side effects included muscle twitching.
  - S15: The reported side effects included anxiety.

**L88.0** `Compound Sentence` (0.944) → `decomposed`
- original: Reduced appetite and weight loss have been seen with SSRIs, so height and weight should be monitored during treatment.
  - S1: Reduced appetite and weight loss have been seen with SSRIs.
  - S2: Therefore, height and weight should be monitored during treatment.

**L89.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Other reported side effects:

**L90.0** `Compound-Complex Sentence` (0.442) → `decomposed` · repaired
- original: Less common side effects reported during studies include tachycardia (fast heartbeat), tinnitus (ringing in the ears), underactive thyroid, enlarged pupils, blurred vision, blood in the stools, swelling, unsteady walking, irritability, fever, raised liver enzymes, anaphylaxis, diabetes, high cholesterol, low blood sugar, increased appetite, joint pain, muscle spasms, poor coordination, coma, convulsions, reduced alertness, numbness, lethargy, restlessness, fainting, aggression, teeth grinding, confusion, euphoric mood, hallucination, blood in the urine, milk production from the breasts, priapism (a long-lasting erection), vaginal bleeding, wheezing, yawning, hair loss, cold sweats, skin inflammation, blistering, itching, rash, hives, bleeding, high blood pressure, and flushing.
  - S1: Less common side effects were reported during studies.
  - S2: Tachycardia was reported.
  - S3: Tachycardia is a fast heartbeat.
  - S4: Tinnitus was reported.
  - S5: Tinnitus is ringing in the ears.
  - S6: Underactive thyroid was reported.
  - S7: Enlarged pupils were reported.
  - S8: Blurred vision was reported.
  - S9: Blood in the stools was reported.
  - S10: Swelling was reported.
  - S11: Unsteady walking was reported.
  - S12: Irritability was reported.
  - S13: Fever was reported.
  - S14: Raised liver enzymes were reported.
  - S15: Anaphylaxis was reported.
  - S16: Diabetes was reported.
  - S17: High cholesterol was reported.
  - S18: Low blood sugar was reported.
  - S19: Increased appetite was reported.
  - S20: Joint pain was reported.
  - S21: Muscle spasms were reported.
  - S22: Poor coordination was reported.
  - S23: Coma was reported.
  - S24: Convulsions were reported.
  - S25: Reduced alertness was reported.
  - S26: Numbness was reported.
  - S27: Lethargy was reported.
  - S28: Restlessness was reported.
  - S29: Fainting was reported.
  - S30: Aggression was reported.
  - S31: Teeth grinding was reported.
  - S32: Confusion was reported.
  - S33: Euphoric mood was reported.
  - S34: Hallucination was reported.
  - S35: Blood in the urine was reported.
  - S36: Milk production from the breasts was reported.
  - S37: Priapism was reported.
  - S38: Priapism is a long-lasting erection.
  - S39: Vaginal bleeding was reported.
  - S40: Wheezing was reported.
  - S41: Yawning was reported.
  - S42: Hair loss was reported.
  - S43: Cold sweats were reported.
  - S44: Skin inflammation was reported.
  - S45: Blistering was reported.
  - S46: Itching was reported.
  - S47: Rash was reported.
  - S48: Hives were reported.
  - S49: Bleeding was reported.
  - S50: High blood pressure was reported.
  - S51: Flushing was reported.

**L91.0** `Compound-Complex Sentence` (0.729) → `decomposed` · repaired
- original: Side effects reported after sertraline came onto the market include increased clotting times, AV block, slow heartbeat, atrial arrhythmias, QTc prolongation, ventricular tachycardia including Torsade de Pointes, breast enlargement in men, raised prolactin, irregular periods, SIADH, blindness, optic neuritis, cataract, severe liver problems including hepatitis, jaundice, and liver failure with some fatal outcomes, pancreatitis, several blood disorders, angioedema, low sodium, high blood sugar, rhabdomyolysis (muscle breakdown), lockjaw, serotonin syndrome, movement disorders including akathisia and dystonia, psychosis, bedwetting, nightmares, sudden kidney failure, pulmonary hypertension, eosinophilic pneumonia, loss of smell, photosensitivity, severe skin reactions such as Stevens-Johnson syndrome and toxic epidermal necrolysis, spasm of blood vessels in the brain, and vasculitis.
  - S1: Sertraline came onto the market.
  - S2: Side effects were reported after sertraline came onto the market.
  - S3: Increased clotting times were reported as a side effect.
  - S4: AV block was reported as a side effect.
  - S5: Slow heartbeat was reported as a side effect.
  - S6: Atrial arrhythmias were reported as a side effect.
  - S7: QTc prolongation was reported as a side effect.
  - S8: Ventricular tachycardia was reported as a side effect.
  - S9: Torsade de Pointes was reported as a side effect.
  - S10: Breast enlargement in men was reported as a side effect.
  - S11: Raised prolactin was reported as a side effect.
  - S12: Irregular periods were reported as a side effect.
  - S13: SIADH was reported as a side effect.
  - S14: Blindness was reported as a side effect.
  - S15: Optic neuritis was reported as a side effect.
  - S16: Cataract was reported as a side effect.
  - S17: Severe liver problems were reported as a side effect.
  - S18: Hepatitis was reported as a side effect.
  - S19: Jaundice was reported as a side effect.
  - S20: Liver failure was reported as a side effect.
  - S21: Some liver failure outcomes were fatal.
  - S22: Pancreatitis was reported as a side effect.
  - S23: Several blood disorders were reported as side effects.
  - S24: Angioedema was reported as a side effect.
  - S25: Low sodium was reported as a side effect.
  - S26: High blood sugar was reported as a side effect.
  - S27: Rhabdomyolysis was reported as a side effect.
  - S28: Muscle breakdown was reported as a side effect.
  - S29: Lockjaw was reported as a side effect.
  - S30: Serotonin syndrome was reported as a side effect.
  - S31: Movement disorders were reported as a side effect.
  - S32: Akathisia was reported as a side effect.
  - S33: Dystonia was reported as a side effect.
  - S34: Psychosis was reported as a side effect.
  - S35: Bedwetting was reported as a side effect.
  - S36: Nightmares were reported as a side effect.
  - S37: Sudden kidney failure was reported as a side effect.
  - S38: Pulmonary hypertension was reported as a side effect.
  - S39: Eosinophilic pneumonia was reported as a side effect.
  - S40: Loss of smell was reported as a side effect.
  - S41: Photosensitivity was reported as a side effect.
  - S42: Severe skin reactions were reported as a side effect.
  - S43: Stevens-Johnson syndrome was reported as a side effect.
  - S44: Toxic epidermal necrolysis was reported as a side effect.
  - S45: Spasm of blood vessels in the brain was reported as a side effect.
  - S46: Vasculitis was reported as a side effect.

**L92.0** `Compound Sentence` (0.545) → `decomposed`
- original: This is not a complete list of side effects, and others may occur.
  - S1: This is not a complete list of side effects.
  - S2: Others may occur.

**L92.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L92.2** `Simple Sentence` (0.97) → `passthrough`
- original: You may report side effects to the FDA at 1-800-FDA-1088.

## Warnings

**L95.0** `Compound Sentence` (0.517) → `decomposed`
- original: Do not take sertraline with a monoamine oxidase inhibitor (MAOI), or within 14 days of stopping one, because of the risk of serotonin syndrome.
  - S1: Do not take sertraline with a monoamine oxidase inhibitor (MAOI).
  - S2: Do not take sertraline within 14 days of stopping one.
  - S3: This is because of the risk of serotonin syndrome.

**L95.1** `Simple Sentence` (0.976) → `passthrough`
- original: This includes the antibiotic linezolid and intravenous methylene blue.

**L95.2** `Simple Sentence` (0.829) → `passthrough`
- original: You also need to wait at least 14 days after stopping sertraline before starting an MAOI.

**L96.0** `Simple Sentence` (0.647) → `passthrough`
- original: Do not take sertraline with pimozide, an antipsychotic medicine.

**L96.1** `Simple Sentence` (0.631) → `passthrough`
- original: Do not take sertraline oral solution if you take disulfiram (Antabuse), because the solution contains alcohol.

**L97.0** `Complex Sentence` (0.892) → `decomposed`
- original: Sertraline can raise the risk of bleeding, particularly if you also take aspirin, NSAIDs such as ibuprofen or naproxen, other antiplatelet medicines, warfarin, or other anticoagulants.
  - S1: Sertraline can raise the risk of bleeding.
  - S2: This risk is particularly high if you also take aspirin.
  - S3: It is also high if you take NSAIDs such as ibuprofen or naproxen.
  - S4: The risk increases if you take other antiplatelet medicines.
  - S5: The risk increases if you take warfarin.
  - S6: The risk increases if you take other anticoagulants.

**L98.0** `Compound-Complex Sentence` (0.711) → `decomposed`
- original: Screening for a personal or family history of bipolar disorder, mania, or hypomania is recommended before starting sertraline, since treating a depressive episode with an antidepressant can trigger a manic episode in someone with bipolar disorder.
  - S1: Screening for a personal or family history of bipolar disorder, mania, or hypomania is recommended before starting sertraline.
  - S2: Treating a depressive episode with an antidepressant can trigger a manic episode.
  - S3: This risk applies to someone with bipolar disorder.

**L99.0** `Incomplete Sentence` (0.901) → `excluded_incomplete`
- original: Do not stop taking sertraline suddenly.

**L99.1** `Compound-Complex Sentence` (0.856) → `decomposed`
- original: Adverse reactions can occur when it is stopped, especially when it is stopped abruptly, so the dose should be lowered gradually where possible.
- pronoun resolved: Adverse reactions can occur when sertraline is stopped, especially when sertraline is stopped abruptly, so the dose should be lowered gradually where possible.
  - edits: “it” → “sertraline”; “it” → “sertraline”
  - S1: Adverse reactions can occur when sertraline is stopped.
  - S2: Adverse reactions are especially likely when sertraline is stopped abruptly.
  - S3: The dose should be lowered gradually where possible.

## Before taking sertraline

**L102.0** `Compound Sentence` (0.876) → `decomposed`
- original: You should not take sertraline if you are allergic to sertraline or any of the ingredients in it, if you take an MAOI or have taken one in the past 14 days, or if you take pimozide.
- pronoun resolved: You should not take sertraline if you are allergic to sertraline or any of the ingredients in sertraline, if you take an MAOI or have taken one in the past 14 days, or if you take pimozide.
  - edits: “it,” → “sertraline,”
  - S1: You should not take sertraline if you are allergic to sertraline or any of the ingredients in sertraline.
  - S2: You should not take sertraline if you take an MAOI or have taken one in the past 14 days.
  - S3: You should not take sertraline if you take pimozide.

**L102.1** `Simple Sentence` (0.764) → `passthrough`
- original: Do not take the oral solution if you take disulfiram.

**L103.0** `Simple Sentence` (0.59) → `passthrough`
- original: To make sure sertraline is safe for you, tell your doctor if you have or have ever had:

**L104.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: liver problems

**L105.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: kidney problems

**L106.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: heart problems, or risk factors for a heart rhythm problem called QTc prolongation

**L107.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: bipolar disorder or mania

**L108.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: seizures or convulsions

**L109.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: low sodium levels in your blood

**L110.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: bleeding problems, or you take a medicine that thins the blood

**L111.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: narrow angles in the eye or glaucoma

**L112.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: a stroke or high blood pressure

**L113.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Pregnancy:

**L114.0** `Incomplete Sentence` (0.583) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant, plan to become pregnant, or become pregnant while taking sertraline.

**L114.1** `Complex Sentence` (0.922) → `decomposed`
- original: Studies of women exposed to sertraline in the first trimester suggest no overall difference in the risk of major birth defects compared with the background rate.
  - S1: Studies of women exposed to sertraline in the first trimester suggest no overall difference in the risk of major birth defects.
  - S2: This difference is compared with the background rate.

**L114.2** `Compound Sentence` (0.94) → `decomposed`
- original: Some studies have reported increases in specific defects, but those results are inconclusive.
  - S1: Some studies have reported increases in specific defects.
  - S2: Those results are inconclusive.

**L115.0** `Compound Sentence` (0.664) → `decomposed`
- original: Taking sertraline late in pregnancy may raise the risk of newborn problems that need longer hospital stays, breathing support, and tube feeding, and of persistent pulmonary hypertension of the newborn (PPHN), a serious lung problem.
  - S1: Taking sertraline late in pregnancy may raise the risk of newborn problems that need longer hospital stays, breathing support, and tube feeding.
  - S2: It may also raise the risk of persistent pulmonary hypertension of the newborn (PPHN), a serious lung problem.

**L115.1** `Complex Sentence` (0.614) → `decomposed`
- original: Use in the month before delivery has been linked with a less than two-fold increase in the risk of postpartum hemorrhage (heavy bleeding after birth).
  - S1: Use in the month before delivery has been linked with an increase in the risk of postpartum hemorrhage.
  - S2: Postpartum hemorrhage is heavy bleeding after birth.
  - S3: The increase in risk is less than two-fold.

**L116.0** `Simple Sentence` (0.963) → `passthrough`
- original: Stopping treatment is not automatically the safer choice.

**L116.1** `Complex Sentence` (0.932) → `decomposed`
- original: In one study of 201 pregnant women with a history of major depression, those who stopped their antidepressant during pregnancy were more likely to relapse than those who continued.
  - S1: In one study of 201 pregnant women with a history of major depression.
  - S2: Those who stopped their antidepressant during pregnancy were more likely to relapse.
  - S3: Those who continued were less likely to relapse.

**L116.2** `Simple Sentence` (0.917) → `passthrough`
- original: This is a decision to make with your doctor.

**L117.0** `Compound Sentence` (0.559) → `decomposed`
- original: Sertraline oral solution contains 12% alcohol and is not recommended during pregnancy, because there is no known safe level of alcohol exposure in pregnancy.
  - S1: Sertraline oral solution contains 12% alcohol.
  - S2: It is not recommended during pregnancy.
  - S3: This is because there is no known safe level of alcohol exposure in pregnancy.

**L118.0** `Simple Sentence` (0.982) → `passthrough`
- original: There is a pregnancy registry that collects information on antidepressant use in pregnancy.

**L118.1** `Simple Sentence` (0.908) → `passthrough`
- original: You can join by calling 1-866-961-2388.

**L119.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Breastfeeding:

**L120.0** `Simple Sentence` (0.99) → `passthrough`
- original: Low levels of sertraline and its breakdown products pass into breast milk.

**L120.1** `Complex Sentence` (0.948) → `decomposed`
- original: In a pooled analysis of 53 mother and infant pairs, exclusively breastfed infants had an average of 2% of the sertraline levels measured in their mothers' blood, ranging from 0% to 15%.
  - S1: A pooled analysis of 53 mother and infant pairs was conducted.
  - S2: Exclusively breastfed infants had an average of 2% of the sertraline levels measured in their mothers' blood.
  - S3: The levels ranged from 0% to 15%.

**L120.2** `Simple Sentence` (0.976) → `passthrough`
- original: No side effects were seen in those infants.

**L120.3** `Simple Sentence` (0.989) → `passthrough`
- original: There is no information on whether sertraline affects milk production.

**L120.4** `Incomplete Sentence` (0.969) → `excluded_incomplete`
- original: Talk with your doctor about the benefits of breastfeeding alongside your need for treatment.

**L121.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Children:

**L122.0** `Simple Sentence` (0.992) → `passthrough`
- original: Sertraline is approved for OCD in children aged 6 to 17 years.

**L122.1** `Compound Sentence` (0.559) → `decomposed`
- original: It is not known to be safe and effective in children under 6, or for any other condition in this age group.
  - S1: It is not known to be safe and effective in children under 6.
  - S2: It is not known to be safe and effective for any other condition in this age group.

**L122.2** `Compound Sentence` (0.702) → `decomposed`
- original: Children and teenagers taking sertraline should be monitored for worsening symptoms and suicidal thoughts, especially early in treatment and when the dose changes, and their weight and growth should be checked.
- pronoun resolved: Children and teenagers taking sertraline should be monitored for worsening symptoms and suicidal thoughts, especially early in treatment and when the dose changes, and Children's weight and growth should be checked.
  - edits: “their” → “Children's”
  - S1: Children and teenagers taking sertraline should be monitored for worsening symptoms and suicidal thoughts.
  - S2: This monitoring is especially important early in treatment and when the dose changes.
  - S3: Children's weight and growth should be checked.

**L123.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Older adults:

**L124.0** `Simple Sentence` (0.99) → `passthrough`
- original: Older adults clear sertraline more slowly.

**L124.1** `Compound Sentence` (0.833) → `decomposed`
- original: In one study, plasma clearance in people aged 65 and over was about 40% lower than in adults aged 25 to 32, so it took 2 to 3 weeks to reach steady levels rather than about 1 week.
  - S1: In one study, plasma clearance in people aged 65 and over was about 40% lower than in adults aged 25 to 32.
  - S2: It took 2 to 3 weeks to reach steady levels rather than about 1 week.

**L124.2** `Simple Sentence` (0.982) → `passthrough`
- original: Doctors usually start older adults at the low end of the dose range.

**L124.3** `Complex Sentence` (0.866) → `decomposed`
- original: Older adults are also at greater risk of low sodium levels in the blood, particularly if they take diuretics (water pills) or are dehydrated.
- pronoun resolved: Older adults are also at greater risk of low sodium levels in the blood, particularly if older adults take diuretics (water pills) or are dehydrated.
  - edits: “they” → “older adults”
  - S1: Older adults are at greater risk of low sodium levels in the blood.
  - S2: This risk is particularly high if older adults take diuretics.
  - S3: This risk is also particularly high if older adults are dehydrated.

## How should I take sertraline?

**L127.0** `Incomplete Sentence` (0.943) → `excluded_incomplete`
- original: Take sertraline exactly as prescribed, once a day, in either the morning or the evening.

**L127.1** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Take it at around the same time each day.
- pronoun resolved: Take sertraline at around the same time each day.
  - edits: “it” → “sertraline”

**L128.0** `Simple Sentence` (0.986) → `passthrough`
- original: Tablets and capsules can be taken with or without food.

**L128.1** `Simple Sentence` (0.964) → `passthrough`
- original: Taking sertraline with food causes only a small increase in the amount absorbed.

**L129.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Swallow capsules whole.

**L129.1** `Incomplete Sentence` (0.963) → `excluded_incomplete`
- original: Do not open, crush, or chew them.

**L130.0** `Compound Sentence` (0.68) → `decomposed`
- original: Your doctor may start you on a low dose and raise it gradually, usually no more often than once a week.
- pronoun resolved: Your doctor may start you on a low dose and raise dose gradually, usually no more often than once a week.
  - edits: “it” → “dose”
  - S1: Your doctor may start you on a low dose.
  - S2: Your doctor may raise the dose gradually.
  - S3: This is usually done no more often than once a week.

**L131.0** `Compound Sentence` (0.366) → `decomposed`
- original: Keep taking sertraline even if you feel well, and do not stop without talking to your doctor first.
  - S1: Keep taking sertraline even if you feel well.
  - S2: Do not stop without talking to your doctor first.

**L132.0** `Incomplete Sentence` (0.77) → `excluded_incomplete`
- original: Tell any doctor or lab that you take sertraline before you have tests.

**L132.1** `Compound Sentence` (0.962) → `decomposed`
- original: Sertraline can cause a false-positive result on urine screening tests for benzodiazepines, and this can continue for several days after you stop taking it.
  - S1: Sertraline can cause a false-positive result on urine screening tests for benzodiazepines.
  - S2: This can continue for several days after you stop taking it.

**L132.2** `Simple Sentence` (0.977) → `passthrough`
- original: A confirmatory test will tell the difference.

**L133.0** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Store sertraline at room temperature, 68°F to 77°F (20°C to 25°C).

**L134.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: How to take sertraline oral solution:

**L135.0** `Simple Sentence` (0.987) → `passthrough`
- original: Sertraline oral solution must be diluted before you take it.

**L135.1** `Incomplete Sentence` (0.955) → `excluded_incomplete`
- original: Do not mix it in advance.
- pronoun resolved: Do not mix sertraline in advance.
  - edits: “it” → “sertraline”

**L136.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Use the dropper supplied with the bottle.

**L136.1** `Simple Sentence` (0.978) → `passthrough`
- original: The dropper has graduation marks for 25 mg and 50 mg only.

**L137.0** `Incomplete Sentence` (0.685) → `excluded_incomplete`
- original: Mix your dose with 4 ounces (half a cup) of water, ginger ale, lemon or lime soda, lemonade, or orange juice only.

**L137.1** `Incomplete Sentence` (0.796) → `excluded_incomplete`
- original: Do not mix it with any other liquid.
- pronoun resolved: Do not mix sertraline with any other liquid.
  - edits: “it” → “sertraline”

**L138.0** `Incomplete Sentence` (0.993) → `excluded_incomplete`
- original: Drink it straight away.
- pronoun resolved: Drink sertraline straight away.
  - edits: “it” → “sertraline”

**L138.1** `Compound Sentence` (0.8) → `decomposed`
- original: A slight haze may appear after mixing, and this is normal.
  - S1: A slight haze may appear after mixing.
  - S2: This is normal.

**L139.0** `Simple Sentence` (0.975) → `passthrough`
- original: The dropper dispenser contains dry natural rubber, a form of latex.

**L139.1** `Incomplete Sentence` (0.882) → `excluded_incomplete`
- original: Tell your doctor or pharmacist if you have a latex allergy.

## What is the usual sertraline dosage?

**L142.0** `Compound Sentence` (0.959) → `decomposed`
- original: The usual starting dose of sertraline is 25 mg or 50 mg once a day, depending on the condition being treated, and the usual treatment range is 50 mg to 200 mg a day.
  - S1: The usual starting dose of sertraline is 25 mg or 50 mg once a day.
  - S2: This depends on the condition being treated.
  - S3: The usual treatment range is 50 mg to 200 mg a day.

**L142.1** `Simple Sentence` (0.987) → `passthrough`
- original: The maximum dose for most conditions is 200 mg a day.

**L143.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Condition | Starting dose | Usual range or maximum

**L144.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Depression (MDD), adults | 50 mg a day | 50 mg to 200 mg a day

**L145.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: OCD, adults | 50 mg a day | 50 mg to 200 mg a day

**L146.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: OCD, ages 6 to 12 | 25 mg a day | 50 mg to 200 mg a day

**L147.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: OCD, ages 13 to 17 | 50 mg a day | 50 mg to 200 mg a day

**L148.0** `Incomplete Sentence` (0.99) → `excluded_incomplete`
- original: Panic disorder, PTSD, social anxiety disorder | 25 mg a day | 50 mg to 200 mg a day

**L149.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: PMDD, taken every day | 50 mg a day | Up to 150 mg a day

**L150.0** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: PMDD, taken in the luteal phase only | 50 mg a day | Up to 100 mg a day

**L151.0** `Complex Sentence` (0.551) → `decomposed`
- original: If the starting dose is not enough, the dose can be raised in steps of 25 mg to 50 mg a day.
  - S1: If the starting dose is not enough, the dose can be raised.
  - S2: The dose can be raised in steps of 25 mg to 50 mg a day.

**L151.1** `Complex Sentence` (0.85) → `decomposed`
- original: Because sertraline stays in the body for about 24 hours, doses are usually changed no more often than once a week.
  - S1: Sertraline stays in the body for about 24 hours.
  - S2: Doses are usually changed no more often than once a week.

**L152.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Dosing for PMDD.

**L152.1** `Complex Sentence` (0.534) → `decomposed`
- original: Sertraline can be taken every day of the menstrual cycle, or only during the luteal phase, meaning you start 14 days before your period is due and continue until it starts, then repeat with each cycle.
- pronoun resolved: Sertraline can be taken every day of the menstrual cycle, or only during the luteal phase, meaning you start 14 days before your period is due and continue until period starts, then repeat with each cycle.
  - edits: “it” → “period”
  - S1: Sertraline can be taken every day of the menstrual cycle.
  - S2: Sertraline can be taken only during the luteal phase.
  - S3: The luteal phase starts 14 days before the period is due.
  - S4: The luteal phase continues until the period starts.
  - S5: This process is repeated with each cycle.

**L152.2** `Compound Sentence` (0.477) → `decomposed`
- original: On daily dosing, the dose can go up by 50 mg per cycle to a maximum of 150 mg a day.
  - S1: On daily dosing, the dose can go up by 50 mg per cycle.
  - S2: The maximum dose is 150 mg a day.

**L152.3** `Complex Sentence` (0.555) → `decomposed`
- original: On luteal phase dosing, the maximum is 100 mg a day, taken as 50 mg for the first 3 days of the dosing cycle and 100 mg for the rest of it.
- pronoun resolved: On luteal phase dosing, the maximum is 100 mg a day, taken as 50 mg for the first 3 days of the dosing cycle and 100 mg for the rest of cycle.
  - edits: “it.” → “cycle.”
  - S1: On luteal phase dosing, the maximum is 100 mg a day.
  - S2: The dose is taken as 50 mg for the first 3 days of the dosing cycle.
  - S3: The dose is 100 mg for the rest of the cycle.

**L153.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Sertraline 150 mg and 200 mg capsules.

**L153.1** `Compound Sentence` (0.553) → `decomposed`
- original: These are not used to start treatment or to titrate a dose, because there are no lower capsule strengths.
  - S1: These are not used to start treatment.
  - S2: They are not used to titrate a dose.
  - S3: This is because there are no lower capsule strengths.

**L153.2** `Simple Sentence` (0.959) → `passthrough`
- original: They can be started in someone who has been taking 100 mg or 125 mg of another sertraline product for at least a week.

**L153.3** `Compound Sentence` (0.937) → `decomposed`
- original: The recommended capsule dose is 150 mg or 200 mg once a day, and the maximum is 200 mg a day.
  - S1: The recommended capsule dose is 150 mg or 200 mg once a day.
  - S2: The maximum dose is 200 mg a day.

**L153.4** `Complex Sentence` (0.957) → `decomposed`
- original: Because the dose cannot be lowered in steps using capsules alone, coming off treatment requires switching back to another sertraline product.
  - S1: Coming off treatment requires switching back to another sertraline product.
  - S2: This is because the dose cannot be lowered in steps using capsules alone.

**L154.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Liver problems.

**L154.1** `Compound-Complex Sentence` (0.675) → `decomposed`
- original: With sertraline tablets and oral solution, mild liver impairment (Child-Pugh score 5 or 6) means both the starting dose and the usual range are halved, and use is not recommended in moderate or severe liver impairment (Child-Pugh score 7 to 15).
  - S1: Sertraline is available in tablet and oral solution forms.
  - S2: Mild liver impairment is defined as a Child-Pugh score of 5 or 6.
  - S3: In patients with mild liver impairment, the starting dose of sertraline is halved.
  - S4: In patients with mild liver impairment, the usual dose range of sertraline is halved.
  - S5: Use of sertraline is not recommended in moderate liver impairment.
  - S6: Use of sertraline is not recommended in severe liver impairment.
  - S7: Moderate liver impairment is defined as a Child-Pugh score of 7 to 15.
  - S8: Severe liver impairment is defined as a Child-Pugh score of 7 to 15.

**L154.2** `Complex Sentence` (0.79) → `decomposed`
- original: Sertraline capsules are not recommended in mild, moderate, or severe liver impairment, because the dose cannot be adjusted with the strengths available.
  - S1: Sertraline capsules are not recommended in mild, moderate, or severe liver impairment.
  - S2: The dose cannot be adjusted with the strengths available.
  - S3: This is the reason for the recommendation.

**L155.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Kidney problems.

**L155.1** `Compound Sentence` (0.576) → `decomposed`
- original: No dose change is needed for mild, moderate, or severe kidney impairment, including in people on dialysis.
  - S1: No dose change is needed for mild kidney impairment.
  - S2: No dose change is needed for moderate kidney impairment.
  - S3: No dose change is needed for severe kidney impairment.
  - S4: No dose change is needed for people on dialysis.

## Sertraline formulations and strengths

**L158.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Sertraline 25 mg tablets

**L159.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Sertraline 50 mg tablets

**L160.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Sertraline 100 mg tablets

**L161.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Sertraline oral solution, 20 mg per mL

**L162.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Sertraline 150 mg capsules

**L163.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Sertraline 200 mg capsules

**L164.0** `Simple Sentence` (0.987) → `passthrough`
- original: Capsule strengths are based on sertraline itself.

**L164.1** `Compound Sentence` (0.835) → `decomposed`
- original: A 150 mg capsule contains 168 mg of sertraline hydrochloride, and a 200 mg capsule contains 224 mg.
  - S1: A 150 mg capsule contains 168 mg of sertraline hydrochloride.
  - S2: A 200 mg capsule contains 224 mg.

**L164.2** `Simple Sentence` (0.982) → `passthrough`
- original: Capsule appearance and imprints differ between manufacturers.

## What happens if I miss a dose?

**L167.0** `Incomplete Sentence` (0.926) → `excluded_incomplete`
- original: Take the missed dose as soon as you remember.

**L167.1** `Compound Sentence` (0.636) → `decomposed`
- original: If it is almost time for your next dose, skip the one you missed and take the next dose at the usual time.
  - S1: If it is almost time for your next dose, skip the one you missed.
  - S2: Take the next dose at the usual time.

**L167.2** `Incomplete Sentence` (0.871) → `excluded_incomplete`
- original: Do not take two doses at once.

## What happens if I overdose?

**L170.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

**L171.0** `Compound Sentence` (0.755) → `decomposed`
- original: Effects reported after a sertraline tablet overdose include seizures, which may be delayed, and changes in mental state including coma.
  - S1: Effects reported after a sertraline tablet overdose include seizures.
  - S2: These seizures may be delayed.
  - S3: Effects reported after a sertraline tablet overdose also include changes in mental state.
  - S4: These changes include coma.

**L171.1** `Compound Sentence` (0.474) → `decomposed`
- original: Heart effects can also be delayed and include changes in the electrical activity of the heart (QRS and QTc prolongation).
  - S1: Heart effects can also be delayed.
  - S2: They include changes in the electrical activity of the heart.
  - S3: These changes involve QRS and QTc prolongation.

**L171.2** `Compound-Complex Sentence` (0.674) → `decomposed`
- original: High blood pressure is seen most often, and low blood pressure is rare, though it can happen when other substances including alcohol have also been taken.
- pronoun resolved: High blood pressure is seen most often, and low blood pressure is rare, though low blood pressure can happen when other substances including alcohol have also been taken.
  - edits: “it” → “low blood pressure”
  - S1: High blood pressure is seen most often.
  - S2: Low blood pressure is rare.
  - S3: Low blood pressure can happen when other substances are taken.
  - S4: Alcohol is one of the substances that can cause low blood pressure.

**L171.3** `Compound Sentence` (0.969) → `decomposed`
- original: Serotonin syndrome can occur, and the risk is higher when several drugs that raise serotonin have been taken together.
  - S1: Serotonin syndrome can occur.
  - S2: The risk is higher when several drugs that raise serotonin have been taken together.

## What should I avoid while taking sertraline?

**L174.0** `Incomplete Sentence` (0.526) → `excluded_incomplete`
- original: Do not drink alcohol while you take sertraline.

**L174.1** `Compound Sentence` (0.86) → `decomposed`
- original: In healthy volunteers, sertraline did not add to the immediate effects of alcohol on thinking and coordination, but drinking is still not recommended during treatment.
  - S1: In healthy volunteers, sertraline did not add to the immediate effects of alcohol on thinking and coordination.
  - S2: Drinking is still not recommended during treatment.

**L175.0** `Incomplete Sentence` (0.731) → `excluded_incomplete`
- original: Do not drive or operate machinery until you know how sertraline affects you.

**L175.1** `Compound Sentence` (0.83) → `decomposed`
- original: It can cause sleepiness and can affect your ability to think clearly, make decisions, or react quickly.
- pronoun resolved: Sertraline can cause sleepiness and can affect your ability to think clearly, make decisions, or react quickly.
  - edits: “It” → “Sertraline”
  - S1: Sertraline can cause sleepiness.
  - S2: It can affect your ability to think clearly, make decisions, or react quickly.

**L176.0** `Simple Sentence` (0.531) → `passthrough`
- original: Do not start or stop any other medicine without checking first, including over-the-counter products, vitamins, and herbal supplements.

## What other drugs will affect sertraline?

**L179.0** `Simple Sentence` (0.991) → `passthrough`
- original: Several medicines interact with sertraline.

**L179.1** `Incomplete Sentence` (0.969) → `excluded_incomplete`
- original: Give a full list of everything you take to any provider who treats you.

**L179.2** `Incomplete Sentence` (0.902) → `excluded_incomplete`
- original: The most important interactions are:

**L180.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: MAOIs.

**L180.1** `Compound Sentence` (0.968) → `decomposed`
- original: Taking sertraline with an MAOI raises the risk of serotonin syndrome, and the combination is contraindicated.
  - S1: Taking sertraline with an MAOI raises the risk of serotonin syndrome.
  - S2: The combination is contraindicated.

**L180.2** `Simple Sentence` (0.939) → `passthrough`
- original: Examples include selegiline, tranylcypromine, isocarboxazid, phenelzine, linezolid, and methylene blue.

**L181.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Pimozide.

**L181.1** `Complex Sentence` (0.522) → `decomposed`
- original: Sertraline raises pimozide levels, which can lead to QTc prolongation and irregular heartbeats.
  - S1: Sertraline raises pimozide levels.
  - S2: This can lead to QTc prolongation.
  - S3: This can lead to irregular heartbeats.

**L181.2** `Simple Sentence` (0.983) → `passthrough`
- original: The combination is contraindicated.

**L182.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Other medicines that raise serotonin.

**L182.1** `Simple Sentence` (0.987) → `passthrough`
- original: These add to the risk of serotonin syndrome.

**L182.2** `Compound Sentence` (0.729) → `decomposed`
- original: Examples include other SSRIs and SNRIs, triptans for migraine, tricyclic antidepressants, opioids, lithium, tryptophan, buspirone, amphetamines, and St. John's wort.
  - S1: Examples include other SSRIs and SNRIs.
  - S2: Examples include triptans for migraine.
  - S3: Examples include tricyclic antidepressants.
  - S4: Examples include opioids.
  - S5: Examples include lithium.
  - S6: Examples include tryptophan.
  - S7: Examples include buspirone.
  - S8: Examples include amphetamines.
  - S9: Examples include St. John's wort.

**L183.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Blood thinners and antiplatelet medicines.

**L183.1** `Simple Sentence` (0.913) → `passthrough`
- original: Aspirin, clopidogrel, heparin, and warfarin can add to the bleeding risk.

**L183.2** `Simple Sentence` (0.974) → `passthrough`
- original: If you take warfarin, your INR should be monitored carefully.

**L184.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Medicines broken down by CYP2D6.

**L184.1** `Compound Sentence` (0.819) → `decomposed`
- original: Sertraline blocks this liver enzyme, so levels of these drugs can rise and doses may need to be lowered.
  - S1: Sertraline blocks this liver enzyme.
  - S2: Levels of these drugs can rise.
  - S3: Doses may need to be lowered.

**L184.2** `Simple Sentence` (0.518) → `passthrough`
- original: Examples include propafenone, flecainide, atomoxetine, desipramine, dextromethorphan, metoprolol, nebivolol, perphenazine, thioridazine, tolterodine, and venlafaxine.

**L185.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Phenytoin and fosphenytoin.

**L185.1** `Compound Sentence` (0.672) → `decomposed`
- original: Sertraline can raise phenytoin levels, so levels should be checked when sertraline is started or the dose is changed.
  - S1: Sertraline can raise phenytoin levels.
  - S2: Levels should be checked when sertraline is started or the dose is changed.

**L186.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: Medicines that prolong the QTc interval.

**L186.1** `Simple Sentence` (0.97) → `passthrough`
- original: These should generally be avoided.

**L186.2** `Compound-Complex Sentence` (0.466) → `decomposed` · repaired
- original: Examples include certain antipsychotics (ziprasidone, iloperidone, chlorpromazine, mesoridazine, droperidol), certain antibiotics (erythromycin, gatifloxacin, moxifloxacin, sparfloxacin), Class 1A antiarrhythmics (quinidine, procainamide), Class III antiarrhythmics (amiodarone, sotalol), and others including pentamidine, methadone, halofantrine, mefloquine, dolasetron, probucol, and tacrolimus.
  - S1: Examples include certain antipsychotics.
  - S2: Examples include ziprasidone.
  - S3: Examples include iloperidone.
  - S4: Examples include chlorpromazine.
  - S5: Examples include mesoridazine.
  - S6: Examples include droperidol.
  - S7: Examples include certain antibiotics.
  - S8: Examples include erythromycin.
  - S9: Examples include gatifloxacin.
  - S10: Examples include moxifloxacin.
  - S11: Examples include sparfloxacin.
  - S12: Examples include Class 1A antiarrhythmics.
  - S13: Examples include quinidine.
  - S14: Examples include procainamide.
  - S15: Examples include Class III antiarrhythmics.
  - S16: Examples include amiodarone.
  - S17: Examples include sotalol.
  - S18: Examples include others.
  - S19: Examples include pentamidine.
  - S20: Examples include methadone.
  - S21: Examples include halofantrine.
  - S22: Examples include mefloquine.
  - S23: Examples include dolasetron.
  - S24: Examples include probucol.
  - S25: Examples include tacrolimus.

**L187.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: Disulfiram, with the oral solution only, because of its alcohol content.

**L188.0** `Compound Sentence` (0.584) → `decomposed`
- original: No dose adjustment is needed when sertraline is taken with cimetidine, diazepam, lithium, atenolol, tolbutamide, digoxin, or medicines broken down by CYP3A4.
  - S1: No dose adjustment is needed when sertraline is taken with cimetidine, diazepam, lithium, atenolol, tolbutamide, or digoxin.
  - S2: No dose adjustment is needed when sertraline is taken with medicines broken down by CYP3A4.

**L189.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L189.1** `Simple Sentence` (0.865) → `passthrough`
- original: Many other prescription medicines, over-the-counter products, vitamins, and herbal products can interact with sertraline.

## Sertraline FAQs

**L192.0** `Incomplete Sentence` (0.979) → `excluded_incomplete`
- original: Is sertraline the same as Zoloft?

**L192.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L193.0** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Yes.

**L193.1** `Compound Sentence` (0.953) → `decomposed`
- original: Sertraline is the active ingredient, and Zoloft is the brand name it is sold under in the United States.
- pronoun resolved: Sertraline is the active ingredient, and Zoloft is the brand name Sertraline is sold under in the United States.
  - edits: “it” → “Sertraline”
  - S1: Sertraline is the active ingredient.
  - S2: Zoloft is the brand name Sertraline is sold under in the United States.

**L193.2** `Compound Sentence` (0.947) → `decomposed`
- original: Sertraline is the generic version of Zoloft, and the two contain the same medicine, sertraline hydrochloride.
  - S1: Sertraline is the generic version of Zoloft.
  - S2: The two contain the same medicine, sertraline hydrochloride.

**L193.3** `Simple Sentence` (0.983) → `passthrough`
- original: You may also see it written as sertraline HCl.
- pronoun resolved: You may also see sertraline written as sertraline HCl.
  - edits: “it” → “sertraline”

**L194.0** `Incomplete Sentence` (0.841) → `excluded_incomplete`
- original: Is sertraline an SSRI, and how does it work?
- pronoun resolved: Is sertraline an SSRI, and how does sertraline work?
  - edits: “it” → “sertraline”

**L194.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L195.0** `Simple Sentence` (0.889) → `passthrough`
- original: Yes, sertraline is an SSRI, which stands for selective serotonin reuptake inhibitor.

**L195.1** `Compound Sentence` (0.591) → `decomposed`
- original: Nerve cells in the brain release serotonin to send signals, then reabsorb it.
- pronoun resolved: Nerve cells in the brain release serotonin to send signals, then reabsorb serotonin.
  - edits: “it.” → “serotonin.”
  - S1: Nerve cells in the brain release serotonin to send signals.
  - S2: Then, they reabsorb serotonin.

**L195.2** `Compound Sentence` (0.829) → `decomposed`
- original: Sertraline blocks that reabsorption, so more serotonin stays available between nerve cells.
  - S1: Sertraline blocks that reabsorption.
  - S2: More serotonin stays available between nerve cells.

**L195.3** `Compound-Complex Sentence` (0.914) → `decomposed`
- original: Sertraline has very little effect on norepinephrine and dopamine, and it has no meaningful effect on adrenergic, cholinergic, GABA, dopamine, histamine, or benzodiazepine receptors, which is part of why it is described as selective.
- pronoun resolved: Sertraline has very little effect on norepinephrine and dopamine, and Sertraline has no meaningful effect on adrenergic, cholinergic, GABA, dopamine, histamine, or benzodiazepine receptors, which is part of why Sertraline is described as selective.
  - edits: “it” → “Sertraline”; “it” → “Sertraline”
  - S1: Sertraline has very little effect on norepinephrine.
  - S2: Sertraline has very little effect on dopamine.
  - S3: Sertraline has no meaningful effect on adrenergic receptors.
  - S4: Sertraline has no meaningful effect on cholinergic receptors.
  - S5: Sertraline has no meaningful effect on GABA receptors.
  - S6: Sertraline has no meaningful effect on histamine receptors.
  - S7: Sertraline has no meaningful effect on benzodiazepine receptors.
  - S8: This lack of effect on other receptors is part of why Sertraline is described as selective.

**L196.0** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: How long does sertraline take to work?

**L196.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L197.0** `Compound Sentence` (0.965) → `decomposed`
- original: Sertraline levels in the blood become steady after about a week of once daily dosing, but the effect on symptoms takes longer.
  - S1: Sertraline levels in the blood become steady after about a week of once daily dosing.
  - S2: The effect on symptoms takes longer.

**L197.1** `Compound-Complex Sentence` (0.839) → `decomposed`
- original: The trials that established sertraline ran for 6 to 12 weeks for depression, OCD, panic disorder, PTSD, and social anxiety disorder, and over three menstrual cycles for PMDD, which gives a sense of the time frame over which the benefit was measured.
  - S1: The trials that established sertraline ran for 6 to 12 weeks.
  - S2: These trials were for depression.
  - S3: These trials were for OCD.
  - S4: These trials were for panic disorder.
  - S5: These trials were for PTSD.
  - S6: These trials were for social anxiety disorder.
  - S7: The trials ran for over three menstrual cycles.
  - S8: These trials were for PMDD.
  - S9: This duration gives a sense of the time frame over which the benefit was measured.

**L197.2** `Compound Sentence` (0.923) → `decomposed`
- original: Because it takes time, doses are usually raised no more often than once a week, and you should keep taking sertraline even if you do not feel a change yet.
  - S1: It takes time.
  - S2: Doses are usually raised no more often than once a week.
  - S3: You should keep taking sertraline even if you do not feel a change yet.

**L198.0** `Incomplete Sentence` (0.965) → `excluded_incomplete`
- original: How long does sertraline stay in your system?

**L198.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L199.0** `Compound Sentence` (0.635) → `decomposed`
- original: Sertraline has a half-life of about 26 hours, meaning half of what is in your blood is cleared in roughly a day.
  - S1: Sertraline has a half-life of about 26 hours.
  - S2: This means half of what is in your blood is cleared in roughly a day.

**L199.1** `Simple Sentence` (0.903) → `passthrough`
- original: At that rate, most of a dose has left your bloodstream within about 5 to 6 days.

**L199.2** `Compound Sentence` (0.571) → `decomposed`
- original: Its main breakdown product, N-desmethylsertraline, lasts longer, with a half-life of 62 to 104 hours, though it is much less active than sertraline itself.
- pronoun resolved: Its main breakdown product, N-desmethylsertraline, lasts longer, with a half-life of 62 to 104 hours, though N-desmethylsertraline is much less active than sertraline itself.
  - edits: “it” → “N-desmethylsertraline”
  - S1: Its main breakdown product, N-desmethylsertraline, lasts longer.
  - S2: It has a half-life of 62 to 104 hours.
  - S3: N-desmethylsertraline is much less active than sertraline itself.

**L199.3** `Simple Sentence` (0.469) → `passthrough`
- original: Sertraline can also cause false-positive urine screening tests for benzodiazepines for several days after you stop taking it.

**L200.0** `Incomplete Sentence` (0.976) → `excluded_incomplete`
- original: Should I take sertraline in the morning or at night?

**L200.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L201.0** `Incomplete Sentence` (0.96) → `excluded_incomplete`
- original: Either is fine.

**L201.1** `Compound Sentence` (0.867) → `decomposed`
- original: Sertraline is taken once a day, in the morning or the evening, and the label does not favor one over the other.
  - S1: Sertraline is taken once a day.
  - S2: It is taken in the morning or the evening.
  - S3: The label does not favor one over the other.

**L201.2** `Simple Sentence` (0.961) → `passthrough`
- original: What matters more is taking it at around the same time each day.
- pronoun resolved: What matters more is taking Sertraline at around the same time each day.
  - edits: “it” → “Sertraline”

**L201.3** `Compound-Complex Sentence` (0.911) → `decomposed`
- original: Insomnia was reported by 20% of people taking sertraline in trials, compared with 13% on placebo, and sleepiness by 11% compared with 6%, so some people find one timing suits them better than the other.
  - S1: Insomnia was reported by 20% of people taking sertraline in trials.
  - S2: Insomnia was reported by 13% of people on placebo in trials.
  - S3: Sleepiness was reported by 11% of people taking sertraline in trials.
  - S4: Sleepiness was reported by 6% of people on placebo in trials.
  - S5: Some people find one timing suits them better than the other.

**L201.4** `Incomplete Sentence` (0.95) → `excluded_incomplete`
- original: Talk to your doctor before changing when you take it.

**L202.0** `Incomplete Sentence` (0.892) → `excluded_incomplete`
- original: Does sertraline cause weight gain or weight loss?

**L202.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L203.0** `Complex Sentence` (0.605) → `decomposed`
- original: Reduced appetite is a common sertraline side effect, reported by 7% of adults in trials compared with 2% on placebo.
  - S1: Reduced appetite is a common sertraline side effect.
  - S2: This side effect was reported by 7% of adults in trials.
  - S3: The report rate was 2% on placebo.

**L203.1** `Simple Sentence` (0.963) → `passthrough`
- original: Increased appetite was reported less often, in fewer than 2% of people.

**L203.2** `Complex Sentence` (0.946) → `decomposed`
- original: In children and teenagers taking sertraline for depression, there was a difference in weight change of roughly 1 kg compared with placebo over 10 weeks, representing slight weight loss on sertraline and slight gain on placebo.
  - S1: In children and teenagers taking sertraline for depression, there was a difference in weight change of roughly 1 kg compared with placebo over 10 weeks.
  - S2: This difference represented slight weight loss on sertraline.
  - S3: This difference represented slight weight gain on placebo.

**L203.3** `Simple Sentence` (0.588) → `passthrough`
- original: Around 7% of children lost more than 7% of their body weight, compared with none on placebo.

**L203.4** `Simple Sentence` (0.873) → `passthrough`
- original: In a longer 34 week extension study, weight gain was similar to what would be expected for their age.

**L203.5** `Simple Sentence` (0.986) → `passthrough`
- original: Height and weight should be monitored in younger patients.

**L203.6** `Incomplete Sentence` (0.96) → `excluded_incomplete`
- original: Tell your doctor about any weight change that concerns you.

**L204.0** `Incomplete Sentence` (0.931) → `excluded_incomplete`
- original: Does sertraline make you tired or sleepy?

**L204.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L205.0** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: It can.

**L205.1** `Compound Sentence` (0.968) → `decomposed`
- original: Sleepiness was reported by 11% of adults taking sertraline in trials, compared with 6% on placebo, and tiredness by 12% compared with 8%.
  - S1: Sleepiness was reported by 11% of adults taking sertraline in trials.
  - S2: This was compared with 6% on placebo.
  - S3: Tiredness was reported by 12%.
  - S4: This was compared with 8%.

**L205.2** `Compound Sentence` (0.643) → `decomposed`
- original: Sertraline can also affect how clearly you think and how quickly you react, so do not drive or use machinery until you know how it affects you.
- pronoun resolved: Sertraline can also affect how clearly you think and how quickly you react, so do not drive or use machinery until you know how Sertraline affects you.
  - edits: “it” → “Sertraline”
  - S1: Sertraline can also affect how clearly you think and how quickly you react.
  - S2: Do not drive or use machinery until you know how Sertraline affects you.

**L206.0** `Incomplete Sentence` (0.972) → `excluded_incomplete`
- original: Is sertraline a controlled substance?

**L206.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L207.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: No.

**L207.1** `Simple Sentence` (0.986) → `passthrough`
- original: Sertraline is not a controlled substance.

**L207.2** `Complex Sentence` (0.934) → `decomposed`
- original: In a study comparing sertraline with alprazolam and d-amphetamine, sertraline did not produce the effects associated with a potential for misuse, such as euphoria or drug liking, that were seen with the other two medicines.
  - S1: A study compared sertraline with alprazolam and d-amphetamine.
  - S2: Sertraline did not produce effects associated with a potential for misuse.
  - S3: The other two medicines produced effects such as euphoria or drug liking.

**L208.0** `Incomplete Sentence` (0.659) → `excluded_incomplete`
- original: Can sertraline cause diarrhea or nausea?

**L208.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L209.0** `Simple Sentence` (0.986) → `passthrough`
- original: Yes, these are the two most common sertraline side effects.
- pronoun resolved: Yes, Sertraline are the two most common sertraline side effects.
  - edits: “these” → “Sertraline”

**L209.1** `Compound Sentence` (0.971) → `decomposed`
- original: Nausea was reported by 26% of people taking sertraline in trials, compared with 12% on placebo, and diarrhea or loose stools by 20% compared with 10%.
  - S1: Nausea was reported by 26% of people taking sertraline in trials, compared with 12% on placebo.
  - S2: Diarrhea or loose stools were reported by 20% of people taking sertraline in trials, compared with 10% on placebo.

**L209.2** `Simple Sentence` (0.983) → `passthrough`
- original: Nausea was also the most common reason people stopped treatment.

**L209.3** `Incomplete Sentence` (0.961) → `excluded_incomplete`
- original: Tell your doctor if these do not settle.
- pronoun resolved: Tell your doctor if Sertraline do not settle.
  - edits: “these” → “Sertraline”

**L210.0** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: How do you stop taking sertraline safely?

**L210.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L211.0** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Lower the dose gradually rather than stopping all at once, and only under your doctor's guidance.

**L211.1** `Complex Sentence` (0.859) → `decomposed`
- original: Symptoms reported after stopping a serotonergic antidepressant, especially when it is stopped abruptly, include nausea, sweating, low or unstable mood, irritability, agitation, dizziness, unusual sensations such as electric shock feelings, tremor, anxiety, confusion, headache, lethargy, insomnia, hypomania, ringing in the ears, and seizures.
- pronoun resolved: Symptoms reported after stopping a serotonergic antidepressant, especially when a serotonergic antidepressant is stopped abruptly, include nausea, sweating, low or unstable mood, irritability, agitation, dizziness, unusual sensations such as electric shock feelings, tremor, anxiety, confusion, headache, lethargy, insomnia, hypomania, ringing in the ears, and seizures.
  - edits: “it” → “a serotonergic antidepressant”
  - S1: Symptoms reported after stopping a serotonergic antidepressant include nausea, sweating, low or unstable mood, irritability, agitation, dizziness, unusual sensations such as electric shock feelings, tremor, anxiety, confusion, headache, lethargy, insomnia, hypomania, ringing in the ears, and seizures.
  - S2: These symptoms are especially present when a serotonergic antidepressant is stopped abruptly.

**L212.0** `Incomplete Sentence` (0.948) → `excluded_incomplete`
- original: Can you drink alcohol while taking sertraline?

**L212.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L213.0** `Simple Sentence` (0.987) → `passthrough`
- original: Drinking alcohol is not recommended while you take sertraline.

**L213.1** `Compound-Complex Sentence` (0.609) → `decomposed`
- original: In healthy volunteers, sertraline did not increase the immediate effects of alcohol on thinking and coordination, but the advice for patients is still to avoid it.
  - S1: In healthy volunteers, sertraline did not increase the immediate effects of alcohol on thinking.
  - S2: In healthy volunteers, sertraline did not increase the immediate effects of alcohol on coordination.
  - S3: The advice for patients is still to avoid sertraline with alcohol.

**L213.2** `Compound Sentence` (0.365) → `decomposed`
- original: Separately, do not take sertraline oral solution with disulfiram, because the solution contains 12% alcohol.
  - S1: Separately, do not take sertraline oral solution with disulfiram.
  - S2: The solution contains 12% alcohol.

**L214.0** `Incomplete Sentence` (0.945) → `excluded_incomplete`
- original: Can you take sertraline while pregnant?

**L214.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L215.0** `Compound Sentence` (0.87) → `decomposed`
- original: That depends on your situation, and it is a decision to make with your doctor rather than on your own.
- pronoun resolved: That depends on your situation, and Sertraline is a decision to make with your doctor rather than on your own.
  - edits: “it” → “Sertraline”
  - S1: That depends on your situation.
  - S2: Sertraline is a decision to make with your doctor rather than on your own.

**L215.1** `Compound-Complex Sentence` (0.538) → `decomposed`
- original: Studies of first trimester use suggest no overall difference in the risk of major birth defects, but use late in pregnancy has been linked with newborn breathing problems and with persistent pulmonary hypertension of the newborn.
  - S1: Studies of first trimester use suggest no overall difference in the risk of major birth defects.
  - S2: Use late in pregnancy has been linked with newborn breathing problems.
  - S3: Use late in pregnancy has been linked with persistent pulmonary hypertension of the newborn.

**L215.2** `Compound Sentence` (0.545) → `decomposed`
- original: At the same time, stopping an antidepressant during pregnancy raises the risk of depression coming back.
  - S1: At the same time, stopping an antidepressant during pregnancy raises the risk of depression.
  - S2: Depression comes back.

**L215.3** `Simple Sentence` (0.972) → `passthrough`
- original: The oral solution specifically is not recommended in pregnancy because it contains alcohol.
- pronoun resolved: The oral solution specifically is not recommended in pregnancy because oral solution contains alcohol.
  - edits: “it” → “oral solution”

**L216.0** `Incomplete Sentence` (0.981) → `excluded_incomplete`
- original: What are sertraline 150 mg and 200 mg capsules for?

**L216.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L217.0** `Compound Sentence` (0.966) → `decomposed`
- original: Sertraline capsules come in 150 mg and 200 mg only, and they are not used to start treatment.
- pronoun resolved: Sertraline capsules come in 150 mg and 200 mg only, and Sertraline capsules are not used to start treatment.
  - edits: “they” → “Sertraline capsules”
  - S1: Sertraline capsules come in 150 mg and 200 mg only.
  - S2: Sertraline capsules are not used to start treatment.

**L217.1** `Complex Sentence` (0.384) → `decomposed`
- original: They are for people who have already been taking 100 mg or 125 mg of another sertraline product for at least a week and need a higher dose.
- pronoun resolved: Sertraline capsules are for people who have already been taking 100 mg or 125 mg of another sertraline product for at least a week and need a higher dose.
  - edits: “They” → “Sertraline capsules”
  - S1: Sertraline capsules are for people who need a higher dose.
  - S2: These people have already been taking 100 mg or 125 mg of another sertraline product.
  - S3: They have been taking this product for at least a week.

**L217.2** `Simple Sentence` (0.917) → `passthrough`
- original: The maximum is 200 mg a day, the same as for tablets.

**L217.3** `Simple Sentence` (0.93) → `passthrough`
- original: Capsules should be swallowed whole and not opened, crushed, or chewed.

**L217.4** `Complex Sentence` (0.882) → `decomposed`
- original: If you need to come off sertraline, the dose has to be lowered gradually using another sertraline product, because there is no capsule strength below 150 mg.
  - S1: If you need to come off sertraline, the dose has to be lowered gradually.
  - S2: This must be done using another sertraline product.
  - S3: There is no capsule strength below 150 mg.

**L217.5** `Compound Sentence` (0.84) → `decomposed`
- original: Capsules are approved for depression in adults and OCD from age 6, not for panic disorder, PTSD, social anxiety disorder, or PMDD.
  - S1: Capsules are approved for depression in adults.
  - S2: Capsules are approved for OCD from age 6.
  - S3: Capsules are not approved for panic disorder.
  - S4: Capsules are not approved for PTSD.
  - S5: Capsules are not approved for social anxiety disorder.
  - S6: Capsules are not approved for PMDD.

**L218.0** `Incomplete Sentence` (0.947) → `excluded_incomplete`
- original: Does sertraline interact with warfarin?

**L218.1** `Incomplete Sentence` (0.994) → `excluded_incomplete`
- original: :

**L219.0** `Incomplete Sentence` (0.929) → `excluded_incomplete`
- original: Yes, in two ways.

**L219.1** `Compound-Complex Sentence` (0.808) → `decomposed`
- original: Sertraline can add to warfarin's effect on bleeding risk, and both medicines bind tightly to proteins in the blood, so taking them together can raise the free level of one or both.
  - S1: Sertraline can add to warfarin's effect on bleeding risk.
  - S2: Both medicines bind tightly to proteins in the blood.
  - S3: Taking them together can raise the free level of one or both.

**L219.2** `Simple Sentence` (0.949) → `passthrough`
- original: If you take warfarin with sertraline, your INR should be monitored carefully.

## Popular FAQ

**L222.0** `Incomplete Sentence` (0.939) → `excluded_incomplete`
- original: Q: How long does Zoloft (sertraline) withdrawal last?

**L222.1** `Compound Sentence` (0.842) → `decomposed`
- original: A: Sertraline (Zoloft) withdrawal symptoms typically last up to 1 to 2 weeks, but may last even longer in some people.
  - S1: Sertraline (Zoloft) withdrawal symptoms typically last up to 1 to 2 weeks.
  - S2: They may last even longer in some people.

**L222.2** `Simple Sentence` (0.959) → `passthrough`
- original: You should avoid abruptly stopping sertraline treatment unless otherwise directed by your healthcare provider.

**L222.3** `Compound Sentence` (0.953) → `decomposed`
- original: Gradually reducing the dose over 2 to 4 weeks can help to prevent severe withdrawal symptoms in most people, and should be directed by your doctor.
  - S1: Gradually reducing the dose over 2 to 4 weeks can help to prevent severe withdrawal symptoms in most people.
  - S2: This process should be directed by your doctor.

**L223.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: Q: How long does Zoloft (sertraline) take to work?

**L223.1** `Complex Sentence` (0.935) → `decomposed`
- original: A: Zoloft (sertraline), a common SSRI antidepressant, can take about 4 to 6 weeks of regular dosing to reach its full therapeutic effect for depression.
- pronoun resolved: A: Zoloft (sertraline), a common SSRI antidepressant, can take about 4 to 6 weeks of regular dosing to reach Zoloft's full therapeutic effect for depression.
  - edits: “its” → “Zoloft's”
  - S1: Zoloft (sertraline) is a common SSRI antidepressant.
  - S2: It can take about 4 to 6 weeks of regular dosing to reach Zoloft's full therapeutic effect for depression.

**L223.2** `Complex Sentence` (0.625) → `decomposed`
- original: For other uses, such as obsessive compulsive disorder (OCD) or posttraumatic stress disorder (PTSD), a full effect may take up to 12 weeks of treatment.
  - S1: For other uses, a full effect may take up to 12 weeks of treatment.
  - S2: Other uses include obsessive compulsive disorder (OCD).
  - S3: Other uses include posttraumatic stress disorder (PTSD).

**L223.3** `Complex Sentence` (0.96) → `decomposed`
- original: When prescribed for premenstrual dysphoric disorder (PMDD), benefits may seen in the first menstrual cycle after starting treatment.
  - S1: Benefits may be seen in the first menstrual cycle after starting treatment.
  - S2: This occurs when the treatment is prescribed for premenstrual dysphoric disorder (PMDD).

**L224.0** `Incomplete Sentence` (0.951) → `excluded_incomplete`
- original: Q: Why does does sertraline make you sleepy?

**L224.1** `Complex Sentence` (0.912) → `decomposed`
- original: A: Sertraline can make some people feel sleepy due to its effects on chemicals in the brain, especially in the first days to weeks of treatment.
- pronoun resolved: A: Sertraline can make some people feel sleepy due to Sertraline's effects on chemicals in the brain, especially in the first days to weeks of treatment.
  - edits: “its” → “Sertraline's”
  - S1: Sertraline can make some people feel sleepy.
  - S2: This is due to Sertraline's effects on chemicals in the brain.
  - S3: This effect is especially common in the first days to weeks of treatment.

**L224.2** `Simple Sentence` (0.968) → `passthrough`
- original: Others experience the opposite problem and develop insomnia instead.

**L224.3** `Compound-Complex Sentence` (0.89) → `decomposed`
- original: Clinical trials suggest that drowsiness, fatigue, and other sleep-related side effects are common, but they are usually mild and often improve as the body adapts to the medication over time.
- pronoun resolved: Clinical trials suggest that drowsiness, fatigue, and other sleep-related side effects are common, but drowsiness are usually mild and often improve as the body adapts to the medication over time.
  - edits: “they” → “drowsiness”
  - S1: Clinical trials suggest that drowsiness, fatigue, and other sleep-related side effects are common.
  - S2: Drowsiness is usually mild.
  - S3: Drowsiness often improves as the body adapts to the medication over time.

**L225.0** `Incomplete Sentence` (0.933) → `excluded_incomplete`
- original: Q: Does Zoloft (sertraline) cause weight gain?

**L225.1** `Compound Sentence` (0.942) → `decomposed`
- original: A: Yes, Zoloft (sertraline) can cause weight gain, but for most people the amount is small.
  - S1: Yes, Zoloft (sertraline) can cause weight gain.
  - S2: For most people, the amount is small.

**L225.2** `Complex Sentence` (0.527) → `decomposed`
- original: In a large 2024 U.S. study, adults who started sertraline gained about half a pound on average after 6 months and about 3 pounds after 2 years.
  - S1: A large 2024 U.S. study was conducted.
  - S2: Adults who started sertraline gained about half a pound on average after 6 months.
  - S3: These adults gained about 3 pounds after 2 years.

**L225.3** `Compound Sentence` (0.942) → `decomposed`
- original: Many people gain no weight at all, and some people, especially children, lose weight.
  - S1: Many people gain no weight at all.
  - S2: Some people, especially children, lose weight.

**L226.0** `Complex Sentence` (0.512) → `decomposed`
- original: Q: Prozac vs Zoloft: Understanding the Differences Between Two Popular Antidepressants A: Prozac and Zoloft represent two of the most widely prescribed antidepressant medications in the United States.
  - S1: Prozac and Zoloft represent two of the most widely prescribed antidepressant medications.
  - S2: These medications are in the United States.

**L226.1** `Complex Sentence` (0.92) → `decomposed`
- original: Both medications belong to a class of drugs known as selective serotonin reuptake inhibitors (SSRIs), which have revolutionized depression treatment since their introduction in the late 1980s and early 1990s.
  - S1: Both medications belong to a class of drugs known as selective serotonin reuptake inhibitors (SSRIs).
  - S2: SSRIs have revolutionized depression treatment since their introduction in the late 1980s and early 1990s.

**L227.0** `Incomplete Sentence` (0.968) → `excluded_incomplete`
- original: Q: Is Zoloft (sertraline) a controlled substance?

**L227.1** `Simple Sentence` (0.93) → `passthrough`
- original: A: No, Zoloft (sertraline) is not a controlled substance.

**L227.2** `Simple Sentence` (0.981) → `passthrough`
- original: It is in an antidepressant drug class known as selective serotonin reuptake inhibitors (SSRIs).
- pronoun resolved: Zoloft is in an antidepressant drug class known as selective serotonin reuptake inhibitors (SSRIs).
  - edits: “It” → “Zoloft”

**L227.3** `Simple Sentence` (0.974) → `passthrough`
- original: Zoloft is commonly used to treat depression, anxiety, panic attacks and other mood disorders.

**L227.4** `Simple Sentence` (0.968) → `passthrough`
- original: Doses should be stopped slowly to help prevent withdrawal symptoms.

**L227.5** `Simple Sentence` (0.989) → `passthrough`
- original: Zoloft can be used for long-term treatment if needed.
