# Amoxicillin — pronoun resolution → sentence classification → decomposition

Source: `/home/heesun/graph/data/text-only/text-only/amoxicillin.txt` · 115 sentences · 24 changed by pronoun resolution · 162 sentences sent to EDC

## What is amoxicillin?

**L5.0** `Complex Sentence` (0.675) → `decomposed`
- original: Amoxicillin is a penicillin antibiotic used to treat bacterial infections such as tonsillitis, bronchitis, sinusitis, pneumonia, and infections of the ear, nose, throat, skin, or urinary tract.
  - S1: Amoxicillin is a penicillin antibiotic.
  - S2: Amoxicillin is used to treat bacterial infections.
  - S3: The infections include tonsillitis, bronchitis, sinusitis, pneumonia, and infections of the ear, nose, throat, skin, or urinary tract.

**L6.0** `Simple Sentence` (0.944) → `passthrough`
- original: Amoxicillin clavulanate is a combination of amoxicillin and clavulanate potassium.

**L6.1** `Compound Sentence` (0.97) → `decomposed`
- original: The amoxicillin fights bacteria, and the clavulanate potassium helps prevent certain bacteria from becoming resistant to amoxicillin.
  - S1: The amoxicillin fights bacteria.
  - S2: The clavulanate potassium helps prevent certain bacteria from becoming resistant to amoxicillin.

**L7.0** `Complex Sentence` (0.483) → `decomposed`
- original: Amoxicillin is also sometimes used together with another antibiotic called clarithromycin (Biaxin) to treat stomach ulcers caused by Helicobacter pylori infection.
  - S1: Amoxicillin is sometimes used together with another antibiotic called clarithromycin (Biaxin).
  - S2: This combination is used to treat stomach ulcers.
  - S3: The ulcers are caused by Helicobacter pylori infection.

**L7.1** `Simple Sentence` (0.89) → `passthrough`
- original: This combination is sometimes used with a stomach acid reducer called lansoprazole (Prevacid).

**L8.0** `Simple Sentence` (0.972) → `passthrough`
- original: Amoxicillin 500mg and 250mg are available as tablets or capsules and as an oral suspension.

**L8.1** `Compound Sentence` (0.922) → `decomposed`
- original: Many brands and forms of amoxicillin are available, and not all brands are listed on this leaflet.
  - S1: Many brands and forms of amoxicillin are available.
  - S2: Not all brands are listed on this leaflet.

## Amoxicillin side effects

**L11.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Common amoxicillin side effects:

**L12.0** `Simple Sentence` (0.943) → `passthrough`
- original: Common amoxicillin side effects may include nausea, vomiting, diarrhea, or rash.

**L12.1** `Simple Sentence` (0.989) → `passthrough`
- original: These side effects affected more than 1% of patients in clinical trials.

**L13.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: Serious amoxicillin side effects:

**L14.0** `Compound Sentence` (0.392) → `decomposed`
- original: Get emergency medical help if you have signs of an allergic reaction to amoxicillin (hives, difficult breathing, swelling in your face or throat) or a severe skin reaction (fever, sore throat, burning eyes, skin pain, red or purple skin rash with blistering and peeling).
  - S1: Get emergency medical help if you have signs of an allergic reaction to amoxicillin.
  - S2: Signs of an allergic reaction to amoxicillin include hives, difficult breathing, and swelling in your face or throat.
  - S3: Get emergency medical help if you have a severe skin reaction.
  - S4: Signs of a severe skin reaction include fever, sore throat, burning eyes, skin pain, and a red or purple skin rash with blistering and peeling.

**L15.0** `Incomplete Sentence` (0.977) → `excluded_incomplete`
- original: Call your doctor at once if you have:

**L16.0** `Incomplete Sentence` (0.988) → `excluded_incomplete`
- original: severe stomach pain or vomiting (which may be signs of a serious intestinal condition); or

**L17.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: diarrhea that is watery or bloody (even if it occurs months after your last dose).
- pronoun resolved: diarrhea that is watery or bloody (even if diarrhea occurs months after your last dose).
  - edits: “it” → “diarrhea”

**L18.0** `Compound Sentence` (0.545) → `decomposed`
- original: This is not a complete list of side effects, and others may occur.
  - S1: This is not a complete list of side effects.
  - S2: Others may occur.

**L18.1** `Incomplete Sentence` (0.923) → `excluded_incomplete`
- original: Call your doctor for medical advice about side effects.

**L18.2** `Simple Sentence` (0.938) → `passthrough`
- original: You may also report side effects to the FDA at 1-800-FDA-1088.

## Warnings

**L21.0** `Complex Sentence` (0.705) → `decomposed`
- original: Do not use this medication if you are allergic to amoxicillin or to any other penicillin antibiotic, such as ampicillin (Omnipen, Principen), dicloxacillin (Dycill, Dynapen), oxacillin (Bactocill), penicillin (Beepen-VK, Ledercillin VK, Pen-V, Pen-Vee K, Pfizerpen, V-Cillin K, Veetids), and others.
- pronoun resolved: Do not use Amoxicillin if you are allergic to amoxicillin or to any other penicillin antibiotic, such as ampicillin (Omnipen, Principen), dicloxacillin (Dycill, Dynapen), oxacillin (Bactocill), penicillin (Beepen-VK, Ledercillin VK, Pen-V, Pen-Vee K, Pfizerpen, V-Cillin K, Veetids), and others.
  - edits: “this medication” → “Amoxicillin”
  - S1: Do not use Amoxicillin if you are allergic to amoxicillin.
  - S2: Do not use Amoxicillin if you are allergic to any other penicillin antibiotic.
  - S3: Examples of other penicillin antibiotics include ampicillin, dicloxacillin, oxacillin, and penicillin.
  - S4: Other penicillin antibiotics include brands such as Omnipen, Principen, Dycill, Dynapen, Bactocill, Beepen-VK, Ledercillin VK, Pen-V, Pen-Vee K, Pfizerpen, V-Cillin K, and Veetids.

**L22.0** `Complex Sentence` (0.631) → `decomposed`
- original: Before using amoxicillin, tell your doctor if you are allergic to cephalosporins such as Omnicef, Cefzil, Ceftin, Keflex, and others.
  - S1: Before using amoxicillin, tell your doctor if you are allergic to cephalosporins.
  - S2: Examples of cephalosporins include Omnicef, Cefzil, Ceftin, and Keflex.
  - S3: There are other cephalosporins as well.

**L22.1** `Compound Sentence` (0.626) → `decomposed`
- original: Also, tell your doctor if you have asthma, liver or kidney disease, a bleeding or blood-clotting disorder, mononucleosis (also called "mono"), or any type of allergy.
  - S1: Also, tell your doctor if you have asthma.
  - S2: Tell your doctor if you have liver disease.
  - S3: Tell your doctor if you have kidney disease.
  - S4: Tell your doctor if you have a bleeding or blood-clotting disorder.
  - S5: Tell your doctor if you have mononucleosis (also called "mono").
  - S6: Tell your doctor if you have any type of allergy.

**L23.0** `Simple Sentence` (0.99) → `passthrough`
- original: Amoxicillin can make birth control pills less effective.

**L23.1** `Incomplete Sentence` (0.8) → `excluded_incomplete`
- original: Ask your doctor about using a non-hormone method of birth control (such as a condom, diaphragm, or spermicide) to prevent pregnancy while taking this medicine.
- pronoun resolved: Ask your doctor about using a non-hormone method of birth control (such as a condom, diaphragm, or spermicide) to prevent pregnancy while taking Amoxicillin.
  - edits: “this medicine.” → “Amoxicillin.”

**L23.2** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Take this medication for the full prescribed length of time.
- pronoun resolved: Take Amoxicillin for the full prescribed length of time.
  - edits: “this medication” → “Amoxicillin”

**L23.3** `Simple Sentence` (0.962) → `passthrough`
- original: Your symptoms may improve before the infection is completely cleared.

**L23.4** `Simple Sentence` (0.971) → `passthrough`
- original: Amoxicillin will not treat a viral infection such as the common cold or flu.

**L23.5** `Incomplete Sentence` (0.565) → `excluded_incomplete`
- original: Do not share this medication with another person, even if they have the same symptoms you have.
- pronoun resolved: Do not share Amoxicillin with another person, even if another person have the same symptoms you have.
  - edits: “this medication” → “Amoxicillin”; “they” → “another person”

**L24.0** `Simple Sentence` (0.992) → `passthrough`
- original: Antibiotic medicines can cause diarrhea.

**L24.1** `Compound Sentence` (0.645) → `decomposed`
- original: This may happen while you are taking amoxicillin, or within a few months after you stop taking it.
- pronoun resolved: Antibiotic medicines may happen while you are taking amoxicillin, or within a few months after you stop taking amoxicillin.
  - edits: “This” → “Antibiotic medicines”; “it.” → “amoxicillin.”
  - S1: Antibiotic medicines may happen while you are taking amoxicillin.
  - S2: Antibiotic medicines may happen within a few months after you stop taking amoxicillin.

**L24.2** `Simple Sentence` (0.99) → `passthrough`
- original: This may be a sign of a new infection.
- pronoun resolved: Diarrhea may be a sign of a new infection.
  - edits: “This” → “Diarrhea”

**L24.3** `Simple Sentence` (0.492) → `passthrough`
- original: If you have diarrhea that is watery or bloody, stop taking this medicine and call your doctor.
- pronoun resolved: If you have diarrhea that is watery or bloody, stop taking Amoxicillin and call your doctor.
  - edits: “this medicine” → “Amoxicillin”

**L24.4** `Incomplete Sentence` (0.678) → `excluded_incomplete`
- original: Do not use anti-diarrhea medicine unless your doctor tells you to.

## Before taking this medicine

**L27.0** `Complex Sentence` (0.813) → `decomposed`
- original: You should not use amoxicillin if you are allergic to any penicillin antibiotic, such as ampicillin, dicloxacillin, oxacillin, penicillin, or ticarcillin.
  - S1: You should not use amoxicillin if you are allergic to any penicillin antibiotic.
  - S2: Examples of penicillin antibiotics include ampicillin, dicloxacillin, oxacillin, penicillin, and ticarcillin.

**L28.0** `Simple Sentence` (0.784) → `passthrough`
- original: To make sure this medicine is safe for you, tell your doctor if you have:
- pronoun resolved: To make sure Amoxicillin is safe for you, tell your doctor if you have:
  - edits: “this medicine” → “Amoxicillin”

**L29.0** `Incomplete Sentence` (0.863) → `excluded_incomplete`
- original: Tell your doctor if you have phenylketonuria (PKU).

**L29.1** `Simple Sentence` (0.986) → `passthrough`
- original: The chewable tablets may contain phenylalanine.

**L30.0** `Simple Sentence` (0.976) → `passthrough`
- original: It is not known whether this medicine will harm an unborn baby.
- pronoun resolved: It is not known whether Amoxicillin will harm an unborn baby.
  - edits: “this medicine” → “Amoxicillin”

**L30.1** `Incomplete Sentence` (0.915) → `excluded_incomplete`
- original: Tell your doctor if you are pregnant or plan to become pregnant.

**L31.0** `Simple Sentence` (0.99) → `passthrough`
- original: Amoxicillin can make birth control pills less effective.

**L31.1** `Incomplete Sentence` (0.903) → `excluded_incomplete`
- original: Ask your doctor about using a non-hormonal birth control (condom, diaphragm, cervical cap, or contraceptive sponge) to prevent pregnancy.

**L32.0** `Simple Sentence` (0.986) → `passthrough`
- original: It may not be safe to breastfeed while using this medicine.
- pronoun resolved: It may not be safe to breastfeed while using Amoxicillin.
  - edits: “this medicine.” → “Amoxicillin.”

**L32.1** `Incomplete Sentence` (0.985) → `excluded_incomplete`
- original: Ask your doctor about any risk.

## How should I take amoxicillin?

**L35.0** `Incomplete Sentence` (0.978) → `excluded_incomplete`
- original: Take amoxicillin exactly as prescribed by your doctor.

**L35.1** `Incomplete Sentence` (0.833) → `excluded_incomplete`
- original: Follow all directions on your prescription label and read all medication guides or instruction sheets.

**L36.0** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Take amoxicillin at the same time each day.

**L37.0** `Simple Sentence` (0.99) → `passthrough`
- original: Some forms of amoxicillin may be taken with or without food.

**L37.1** `Incomplete Sentence` (0.926) → `excluded_incomplete`
- original: Check your medicine label to see if you should take your medicine with food or not.

**L38.0** `Incomplete Sentence` (0.968) → `excluded_incomplete`
- original: Shake the oral suspension (liquid) before you measure a dose.

**L39.0** `Incomplete Sentence` (0.479) → `excluded_incomplete`
- original: Measure liquid medicine with the dosing syringe provided, or use a medicine dose-measuring device (not a kitchen spoon).

**L39.1** `Simple Sentence` (0.885) → `passthrough`
- original: You may mix the liquid with water, milk, baby formula, fruit juice, or ginger ale.

**L39.2** `Incomplete Sentence` (0.968) → `excluded_incomplete`
- original: Drink all of the mixture right away.

**L39.3** `Incomplete Sentence` (0.995) → `excluded_incomplete`
- original: Do not save for later use.

**L40.0** `Simple Sentence` (0.983) → `passthrough`
- original: You must chew the chewable tablet before you swallow it.
- pronoun resolved: You must chew the chewable tablet before you swallow chewable tablet.
  - edits: “it.” → “chewable tablet.”

**L41.0** `Incomplete Sentence` (0.599) → `excluded_incomplete`
- original: Swallow the regular tablet whole and do not crush, chew, or break it.
- pronoun resolved: Swallow the regular tablet whole and do not crush, chew, or break regular tablet.
  - edits: “it.” → “regular tablet.”

**L42.0** `Complex Sentence` (0.547) → `decomposed`
- original: If you are taking amoxicillin with clarithromycin and/or lansoprazole to treat stomach ulcer, use all of your medications as directed.
  - S1: If you are taking amoxicillin with clarithromycin and/or lansoprazole to treat stomach ulcer.
  - S2: Use all of your medications as directed.

**L42.1** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Read the medication guide or patient instructions provided with each medication.

**L42.2** `Simple Sentence` (0.54) → `passthrough`
- original: Do not change your doses or medication schedule without your doctor's advice.

**L43.0** `Incomplete Sentence` (0.801) → `excluded_incomplete`
- original: Use this medicine for the full prescribed length of time, even if your symptoms quickly improve.

**L43.1** `Simple Sentence` (0.96) → `passthrough`
- original: Skipping doses can increase your risk of infection, that is resistant to medication.

**L43.2** `Simple Sentence` (0.958) → `passthrough`
- original: Amoxicillin will not treat a viral infection such as the flu or a common cold.

**L44.0** `Simple Sentence` (0.497) → `passthrough`
- original: Do not share this medicine with another person, even if they have the same symptoms you have.
- pronoun resolved: Do not share this medicine with another person, even if another person have the same symptoms you have.
  - edits: “they” → “another person”

**L45.0** `Simple Sentence` (0.99) → `passthrough`
- original: This medicine can affect the results of certain medical tests.

**L45.1** `Incomplete Sentence` (0.911) → `excluded_incomplete`
- original: Tell any doctor who treats you that you are using this medicine.

**L46.0** `Incomplete Sentence` (0.938) → `excluded_incomplete`
- original: Store tablets and capsules at room temperature, away from moisture, heat, and light.

**L47.0** `Simple Sentence` (0.428) → `passthrough`
- original: Liquid amoxicillin may need to be stored in a refrigerator or at room temperature, depending on the brand.

**L47.1** `Incomplete Sentence` (0.982) → `excluded_incomplete`
- original: Check your label for storage instructions.

**L47.2** `Simple Sentence` (0.838) → `passthrough`
- original: If stored in the refrigerator, do not allow it to freeze.
- pronoun resolved: If stored in the refrigerator, do not allow Liquid amoxicillin to freeze.
  - edits: “it” → “Liquid amoxicillin”

**L47.3** `Incomplete Sentence` (0.984) → `excluded_incomplete`
- original: Throw away any liquid medicine that is not used within 14 days after it was mixed at the pharmacy.
- pronoun resolved: Throw away any liquid medicine that is not used within 14 days after liquid medicine was mixed at the pharmacy.
  - edits: “it” → “liquid medicine”

## What happens if I miss a dose?

**L50.0** `Incomplete Sentence` (0.469) → `excluded_incomplete`
- original: Skip the missed dose and use your next dose at the regular time.

**L50.1** `Incomplete Sentence` (0.946) → `excluded_incomplete`
- original: Do not use two doses at one time.

## What happens if I overdose?

**L53.0** `Incomplete Sentence` (0.992) → `excluded_incomplete`
- original: Seek emergency medical attention or call the Poison Help line at 1-800-222-1222.

## What to avoid

**L56.0** `Simple Sentence` (0.661) → `passthrough`
- original: Antibiotic medicines can cause diarrhea, which may be a sign of a new infection.

**L56.1** `Simple Sentence` (0.351) → `passthrough`
- original: If you have diarrhea that is watery or bloody, call your doctor before using anti-diarrhea medicine.

## What other drugs will affect amoxicillin?

**L59.0** `Incomplete Sentence` (0.991) → `excluded_incomplete`
- original: Tell your doctor about all your other medicines, especially:

**L60.0** `Incomplete Sentence` (0.997) → `excluded_incomplete`
- original: any other antibiotics;

**L61.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: allopurinol;

**L62.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: probenecid; or

**L63.0** `Incomplete Sentence` (0.996) → `excluded_incomplete`
- original: a blood thinner - warfarin, Coumadin, Jantoven;

**L64.0** `Incomplete Sentence` (0.998) → `excluded_incomplete`
- original: birth control pills.

**L65.0** `Incomplete Sentence` (0.704) → `excluded_incomplete`
- original: This list is not complete.

**L65.1** `Complex Sentence` (0.622) → `decomposed`
- original: Other drugs may interact with amoxicillin, including prescription and over-the-counter medicines, vitamins, and herbal products.
  - S1: Other drugs may interact with amoxicillin.
  - S2: These drugs include prescription and over-the-counter medicines.
  - S3: These drugs also include vitamins and herbal products.

**L65.2** `Compound Sentence` (0.657) → `decomposed`
- original: Not all possible drug interactions are listed here; to check for interactions, click on the link below.
  - S1: Not all possible drug interactions are listed here.
  - S2: To check for interactions, click on the link below.

## Popular FAQ

**L68.0** `Incomplete Sentence` (0.663) → `excluded_incomplete`
- original: Q: What are the best antibiotics for a tooth infection?

**L68.1** `Simple Sentence` (0.853) → `passthrough`
- original: A: There are several antibiotics that kill the common mouth bacteria that cause tooth infections.

**L68.2** `Simple Sentence` (0.823) → `passthrough`
- original: The best (first-line) antibiotics for tooth infection include: Amoxicillin, Penicillin, Cephalexin, Clindamycin, Azithromycin.

**L68.3** `Complex Sentence` (0.833) → `decomposed`
- original: Amoxicillin is often the first choice because it is widely effective and has the fewest gastrointestinal side effects.
- pronoun resolved: Amoxicillin is often the first choice because Amoxicillin is widely effective and has the fewest gastrointestinal side effects.
  - edits: “it” → “Amoxicillin”
  - S1: Amoxicillin is often the first choice.
  - S2: Amoxicillin is widely effective.
  - S3: Amoxicillin has the fewest gastrointestinal side effects.

**L69.0** `Incomplete Sentence` (0.783) → `excluded_incomplete`
- original: Q: Can you drink alcohol with amoxicillin?

**L69.1** `Simple Sentence` (0.94) → `passthrough`
- original: A: Yes, you can drink alcohol while taking the antibiotic amoxicillin.

**L69.2** `Simple Sentence` (0.988) → `passthrough`
- original: The alcohol will not stop amoxicillin from working.

**L69.3** `Complex Sentence` (0.88) → `decomposed`
- original: However, many health professionals will recommend you avoid alcohol to give your body the best chance possible to fight the infection.
  - S1: However, many health professionals will recommend you avoid alcohol.
  - S2: This is to give your body the best chance possible.
  - S3: The goal is to fight the infection.

**L69.4** `Simple Sentence` (0.972) → `passthrough`
- original: Moderation is key.

**L70.0** `Incomplete Sentence` (0.987) → `excluded_incomplete`
- original: Q: Does amoxicillin expire?

**L70.1** `Incomplete Sentence` (0.964) → `excluded_incomplete`
- original: Is it safe to take after expiration?
- pronoun resolved: Is amoxicillin safe to take after expiration?
  - edits: “it” → “amoxicillin”

**L70.2** `Compound-Complex Sentence` (0.892) → `decomposed`
- original: A: Amoxicillin capsules and tablets have an expiry of around 2 years and, provided they are stored as recommended and in the original packaging, there will be a small lee way of safety if used beyond expiry.
- pronoun resolved: A: Amoxicillin capsules and tablets have an expiry of around 2 years and, provided Amoxicillin capsules and tablets are stored as recommended and in the original packaging, there will be a small lee way of safety if used beyond expiry.
  - edits: “they” → “Amoxicillin capsules and tablets”
  - S1: Amoxicillin capsules and tablets have an expiry of around 2 years.
  - S2: Amoxicillin capsules and tablets should be stored as recommended.
  - S3: Amoxicillin capsules and tablets should be kept in the original packaging.
  - S4: If stored as recommended and in the original packaging, there will be a small margin of safety if used beyond expiry.

**L70.3** `Compound Sentence` (0.674) → `decomposed`
- original: Amoxicillin suspension is different and has a very short shelf life of about 7-10 days once it is prepared.
- pronoun resolved: Amoxicillin suspension is different and has a very short shelf life of about 7-10 days once Amoxicillin suspension is prepared.
  - edits: “it” → “Amoxicillin suspension”
  - S1: Amoxicillin suspension is different.
  - S2: It has a very short shelf life of about 7-10 days once prepared.

**L71.0** `Incomplete Sentence` (0.811) → `excluded_incomplete`
- original: Q: What are the best antibiotics for pneumonia?

**L71.1** `Simple Sentence` (0.776) → `passthrough`
- original: A: The best antibiotic depends on your infection type, health, and local resistance patterns.

**L71.2** `Simple Sentence` (0.987) → `passthrough`
- original: Common first choices include azithromycin, clarithromycin, or doxycycline.

**L71.3** `Simple Sentence` (0.981) → `passthrough`
- original: More serious infections may require levofloxacin or amoxicillin/clavulanate.

**L72.0** `Incomplete Sentence` (0.975) → `excluded_incomplete`
- original: Q: Is amoxicillin safe for dogs?

**L72.1** `Compound Sentence` (0.828) → `decomposed`
- original: A: Amoxicillin is a prescription antibiotic that veterinarians commonly use to treat bacterial infections in dogs, and it is generally considered safe when given at the correct dose under veterinary supervision.
- pronoun resolved: A: Amoxicillin is a prescription antibiotic that veterinarians commonly use to treat bacterial infections in dogs, and Amoxicillin is generally considered safe when given at the correct dose under veterinary supervision.
  - edits: “it” → “Amoxicillin”
  - S1: Amoxicillin is a prescription antibiotic that veterinarians commonly use to treat bacterial infections in dogs.
  - S2: Amoxicillin is generally considered safe when given at the correct dose under veterinary supervision.

**L72.2** `Compound Sentence` (0.516) → `decomposed`
- original: However, amoxicillin can cause side effects, allergic reactions, and serious problems if the dose is wrong, the drug is not needed, or human products are used without a veterinarian’s guidance.
  - S1: However, amoxicillin can cause side effects.
  - S2: It can cause allergic reactions.
  - S3: It can cause serious problems if the dose is wrong.
  - S4: It can cause serious problems if the drug is not needed.
  - S5: It can cause serious problems if human products are used without a veterinarian's guidance.

**L73.0** `Incomplete Sentence` (0.892) → `excluded_incomplete`
- original: Q: Does amoxicillin help with tooth infection and pain?

**L73.1** `Simple Sentence` (0.984) → `passthrough`
- original: A: Yes, amoxicillin will help your tooth infection.

**L73.2** `Simple Sentence` (0.98) → `passthrough`
- original: Amoxicillin is one of the first antibiotics recommended for the treatment of a tooth infection.

**L73.3** `Compound Sentence` (0.585) → `decomposed`
- original: It has shown to be widely effective and have fewer gastrointestinal side effects compared to other options.
- pronoun resolved: Amoxicillin has shown to be widely effective and have fewer gastrointestinal side effects compared to other options.
  - edits: “It” → “Amoxicillin”
  - S1: Amoxicillin has shown to be widely effective.
  - S2: It has fewer gastrointestinal side effects compared to other options.

**L74.0** `Incomplete Sentence` (0.736) → `excluded_incomplete`
- original: Q: What is the Best Antibiotic for Strep Throat?

**L74.1** `Simple Sentence` (0.98) → `passthrough`
- original: A: Penicillin and amoxicillin are the first-choice antibiotics for strep throat.

**L74.2** `Complex Sentence` (0.942) → `decomposed`
- original: According to the CDC, Group A Streptococcus (the bacteria that cause Strep throat) has never shown resistance to penicillin, making it the gold standard treatment.
- pronoun resolved: According to the CDC, Group A Streptococcus (the bacteria that cause Strep throat) has never shown resistance to penicillin, making Penicillin the gold standard treatment.
  - edits: “it” → “Penicillin”
  - S1: According to the CDC, Group A Streptococcus has never shown resistance to penicillin.
  - S2: Group A Streptococcus is the bacteria that cause Strep throat.
  - S3: This lack of resistance makes Penicillin the gold standard treatment.

**L75.0** `Simple Sentence` (0.555) → `passthrough`
- original: Q: What's the difference between amoxicillin and penicillin?

**L75.1** `Complex Sentence` (0.916) → `decomposed`
- original: A: The main difference between amoxicillin and penicillin is that amoxicillin is effective against a wider spectrum of bacteria compared with penicillin.
  - S1: The main difference between amoxicillin and penicillin is that amoxicillin is effective against a wider spectrum of bacteria.
  - S2: This is compared with penicillin.

**L75.2** `Simple Sentence` (0.987) → `passthrough`
- original: Both amoxicillin and penicillin belong to the class of antibiotics called penicillins.

**L76.0** `Incomplete Sentence` (0.983) → `excluded_incomplete`
- original: Q: Amoxicillin rash: When should I be concerned?

**L76.1** `Complex Sentence` (0.894) → `decomposed`
- original: A: From 5% to 10% of children will develop a rash from amoxicillin after taking it, which in most cases, is considered a side effect of amoxicillin and not an allergic rash.
- pronoun resolved: A: From 5% to 10% of children will develop a rash from amoxicillin after taking Amoxicillin, which in most cases, is considered a side effect of amoxicillin and not an allergic rash.
  - edits: “it,” → “Amoxicillin,”
  - S1: From 5% to 10% of children will develop a rash from amoxicillin.
  - S2: This occurs after taking Amoxicillin.
  - S3: In most cases, this is considered a side effect of amoxicillin.
  - S4: It is not an allergic rash.

**L76.2** `Complex Sentence` (0.777) → `decomposed`
- original: But in a small number of cases, the rash will be a sign of an allergic reaction which means the amoxicillin will need to be stopped right away.
  - S1: In a small number of cases, the rash will be a sign of an allergic reaction.
  - S2: This means the amoxicillin will need to be stopped right away.
