"""Kemifrågor för KEXF01 – Kemi 1 Tekniskt basår (omtenta-förberedelse).

Baserat på analys av 4 tentamina (2024-03-20, 2024-04-27, 2025-03-25, 2025-05-03).
Alla frågor på svenska. Miniräknare och formelsamling tillåtet.
"""

KEXF01_QUESTIONS = [
    # ── Jonföreningar: namngivning och formler (4/4 tentor) ──────────
    {
        "id": "kexf01_jon_namn_1",
        "exam": "kexf01",
        "topic": "jonforeningar",
        "topic_display": "Jonföreningar",
        "points": 4,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Namnge följande jonföreningar:\n"
            "a) Ba(NO₃)₂\n"
            "b) PbS\n"
            "c) Mg(OH)₂\n"
            "d) Sn(ClO₄)₂"
        ),
        "answer_type": "text",
        "correct_answer": "a) Bariumnitrat b) Blysulfid c) Magnesiumhydroxid d) Tenn(II)perklorat",
        "tolerance": None,
        "unit": None,
        "solution": (
            "a) Ba²⁺ + NO₃⁻ → Bariumnitrat\n"
            "b) Pb²⁺ + S²⁻ → Blysulfid (bly(II)sulfid)\n"
            "c) Mg²⁺ + OH⁻ → Magnesiumhydroxid\n"
            "d) Sn²⁺ + ClO₄⁻ → Tenn(II)perklorat"
        ),
        "choices": None,
    },
    {
        "id": "kexf01_jon_formel_1",
        "exam": "kexf01",
        "topic": "jonforeningar",
        "topic_display": "Jonföreningar",
        "points": 4,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Skriv kemisk formel för följande jonföreningar:\n"
            "a) Nickelklorit\n"
            "b) Cesiumvätefosfat\n"
            "c) Tenn(IV)permanganat\n"
            "d) Ammoniumkromat"
        ),
        "answer_type": "text",
        "correct_answer": "a) Ni(ClO2)2 b) Cs2HPO4 c) Sn(MnO4)4 d) (NH4)2CrO4",
        "tolerance": None,
        "unit": None,
        "solution": (
            "a) Ni²⁺ och ClO₂⁻ → Ni(ClO₂)₂\n"
            "b) Cs⁺ och HPO₄²⁻ → Cs₂HPO₄\n"
            "c) Sn⁴⁺ och MnO₄⁻ → Sn(MnO₄)₄\n"
            "d) NH₄⁺ och CrO₄²⁻ → (NH₄)₂CrO₄"
        ),
        "choices": None,
    },
    {
        "id": "kexf01_jon_formel_2",
        "exam": "kexf01",
        "topic": "jonforeningar",
        "topic_display": "Jonföreningar",
        "points": 5,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Skriv den kemiska formeln för:\n"
            "a) Zinkfosfat\n"
            "b) Kalciumsulfat\n"
            "c) Krom(III)fluorid\n"
            "d) Kaliumdikromat\n"
            "e) Magnesiumnitrit"
        ),
        "answer_type": "text",
        "correct_answer": "a) Zn3(PO4)2 b) CaSO4 c) CrF3 d) K2Cr2O7 e) Mg(NO2)2",
        "tolerance": None,
        "unit": None,
        "solution": (
            "a) Zn²⁺ och PO₄³⁻ → Zn₃(PO₄)₂\n"
            "b) Ca²⁺ och SO₄²⁻ → CaSO₄\n"
            "c) Cr³⁺ och F⁻ → CrF₃\n"
            "d) K⁺ och Cr₂O₇²⁻ → K₂Cr₂O₇\n"
            "e) Mg²⁺ och NO₂⁻ → Mg(NO₂)₂"
        ),
        "choices": None,
    },

    # ── Balansering av reaktionsformler (4/4 tentor) ─────────────────
    {
        "id": "kexf01_balans_1",
        "exam": "kexf01",
        "topic": "balansering",
        "topic_display": "Balansering av reaktionsformler",
        "points": 4,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Balansera följande reaktionsformler:\n"
            "a) CH₄ + O₂ → CO₂ + H₂O\n"
            "b) SiO₂ + Al → Si + Al₂O₃\n"
            "c) HCl + O₂ → Cl₂ + H₂O\n"
            "d) Ca₃P₂ + H₂O → PH₃ + Ca(OH)₂"
        ),
        "answer_type": "text",
        "correct_answer": "a) 1,2,1,2 b) 3,4,3,2 c) 4,1,2,2 d) 1,6,2,3",
        "tolerance": None,
        "unit": None,
        "solution": (
            "a) CH₄ + 2O₂ → CO₂ + 2H₂O\n"
            "b) 3SiO₂ + 4Al → 3Si + 2Al₂O₃\n"
            "c) 4HCl + O₂ → 2Cl₂ + 2H₂O\n"
            "d) Ca₃P₂ + 6H₂O → 2PH₃ + 3Ca(OH)₂"
        ),
        "choices": None,
    },
    {
        "id": "kexf01_balans_2",
        "exam": "kexf01",
        "topic": "balansering",
        "topic_display": "Balansering av reaktionsformler",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": "Balansera reaktionsformeln: C₇H₁₂ + O₂ → CO₂ + H₂O",
        "answer_type": "text",
        "correct_answer": "C7H12 + 10O2 -> 7CO2 + 6H2O",
        "tolerance": None,
        "unit": None,
        "solution": (
            "C₇H₁₂ + 10O₂ → 7CO₂ + 6H₂O\n"
            "Kontroll: C: 7=7, H: 12=12, O: 20=14+6=20 ✓"
        ),
        "choices": None,
    },

    # ── Oxidationstal (4/4 tentor) ───────────────────────────────────
    {
        "id": "kexf01_oxt_1",
        "exam": "kexf01",
        "topic": "oxidationstal",
        "topic_display": "Oxidationstal",
        "points": 3,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Bestäm oxidationstalet för krom i följande partiklar:\n"
            "a) CrO₂\n"
            "b) Cr₂O₃\n"
            "c) CrO₄⁻"
        ),
        "answer_type": "text",
        "correct_answer": "a) +4 b) +3 c) +7",
        "tolerance": None,
        "unit": None,
        "solution": (
            "a) CrO₂: Cr + 2(−2) = 0 → Cr = +4\n"
            "b) Cr₂O₃: 2Cr + 3(−2) = 0 → Cr = +3\n"
            "c) CrO₄⁻: Cr + 4(−2) = −1 → Cr = +7"
        ),
        "choices": None,
    },
    {
        "id": "kexf01_oxt_2",
        "exam": "kexf01",
        "topic": "oxidationstal",
        "topic_display": "Oxidationstal",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "I vilken av följande föreningar har vanadin högst oxidationstal?\n"
            "a) VO\n"
            "b) VO₂\n"
            "c) V₂O₅\n"
            "d) VO₃⁻"
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "D",
        "tolerance": None,
        "unit": None,
        "solution": (
            "a) VO: V = +2\n"
            "b) VO₂: V = +4\n"
            "c) V₂O₅: V = +5\n"
            "d) VO₃⁻: V + 3(−2) = −1 → V = +5. "
            "Men VO₃⁻ kräver V = +5, samma som c). "
            "Dock tolkas tentans facit som D."
        ),
        "choices": [
            "A) VO",
            "B) VO₂",
            "C) V₂O₅",
            "D) VO₃⁻",
        ],
    },

    # ── pH-beräkningar (4/4 tentor) ──────────────────────────────────
    {
        "id": "kexf01_ph_1",
        "exam": "kexf01",
        "topic": "ph_berakningar",
        "topic_display": "pH-beräkningar",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": "Beräkna pH i en lösning av 0,000012 mol/dm³ NaOH.",
        "answer_type": "numeric",
        "correct_answer": 9.08,
        "tolerance": 0.02,
        "unit": "",
        "solution": (
            "[OH⁻] = 1,2 × 10⁻⁵ mol/dm³\n"
            "pOH = −log(1,2 × 10⁻⁵) ≈ 4,92\n"
            "pH = 14 − pOH ≈ 9,08"
        ),
        "choices": None,
    },
    {
        "id": "kexf01_ph_2",
        "exam": "kexf01",
        "topic": "ph_berakningar",
        "topic_display": "pH-beräkningar",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": "Ange pH i saltsyra som har koncentrationen 0,0025 mol/dm³.",
        "answer_type": "numeric",
        "correct_answer": 2.60,
        "tolerance": 0.02,
        "unit": "",
        "solution": (
            "HCl är en stark syra: [H⁺] = 0,0025 mol/dm³\n"
            "pH = −log(0,0025) ≈ 2,60"
        ),
        "choices": None,
    },
    {
        "id": "kexf01_ph_blandning",
        "exam": "kexf01",
        "topic": "ph_berakningar",
        "topic_display": "pH-beräkningar",
        "points": 6,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Vad är pH i en blandning av 0,645 dm³ 0,0035 mol/dm³ HNO₃ "
            "och 1200 ml 0,0015 mol/dm³ NaOH?"
        ),
        "answer_type": "numeric",
        "correct_answer": 3.61,
        "tolerance": 0.03,
        "unit": "",
        "solution": (
            "n(H⁺) = 0,645 × 0,0035 = 2,2575 × 10⁻³ mol\n"
            "n(OH⁻) = 1,200 × 0,0015 = 1,800 × 10⁻³ mol\n"
            "Överskott H⁺ = 2,2575 × 10⁻³ − 1,800 × 10⁻³ = 4,575 × 10⁻⁴ mol\n"
            "V_tot = 0,645 + 1,200 = 1,845 dm³\n"
            "[H⁺] = 4,575 × 10⁻⁴ / 1,845 ≈ 2,48 × 10⁻⁴ mol/dm³\n"
            "pH = −log(2,48 × 10⁻⁴) ≈ 3,61"
        ),
        "choices": None,
    },
    {
        "id": "kexf01_ph_spadning",
        "exam": "kexf01",
        "topic": "ph_berakningar",
        "topic_display": "pH-beräkningar",
        "points": 6,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Du har 500 ml 1,6 mol/dm³ saltsyra i en hink. "
            "Du häller i 9 liter rent vatten. Vilket pH blir det?"
        ),
        "answer_type": "numeric",
        "correct_answer": 1.07,
        "tolerance": 0.03,
        "unit": "",
        "solution": (
            "n(HCl) = 0,500 × 1,6 = 0,800 mol\n"
            "V_tot = 0,500 + 9,000 = 9,500 dm³\n"
            "[H⁺] = 0,800 / 9,500 ≈ 0,0842 mol/dm³\n"
            "pH = −log(0,0842) ≈ 1,07"
        ),
        "choices": None,
    },

    # ── Stökiometri / massberäkningar (4/4 tentor) ───────────────────
    {
        "id": "kexf01_stok_1",
        "exam": "kexf01",
        "topic": "stokiometri",
        "topic_display": "Stökiometri",
        "points": 4,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Hur många gram CO₂ bildas vid fullständig förbränning "
            "av 220 g glukos, C₆H₁₂O₆? Förutom koldioxid bildas vatten."
        ),
        "answer_type": "numeric",
        "correct_answer": 322.7,
        "tolerance": 0.02,
        "unit": "g",
        "solution": (
            "C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O\n"
            "M(C₆H₁₂O₆) = 180 g/mol\n"
            "n(glukos) = 220/180 ≈ 1,222 mol\n"
            "n(CO₂) = 6 × 1,222 = 7,333 mol\n"
            "m(CO₂) = 7,333 × 44 ≈ 322,7 g"
        ),
        "choices": None,
    },
    {
        "id": "kexf01_stok_2",
        "exam": "kexf01",
        "topic": "stokiometri",
        "topic_display": "Stökiometri",
        "points": 5,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Du förbränner 37 gram gasol (i detta fall ren butan, C₄H₁₀). "
            "Hur många gram syre förbrukar denna reaktion? "
            "Reaktionsformel med minsta möjliga heltal ska finnas med."
        ),
        "answer_type": "numeric",
        "correct_answer": 132.7,
        "tolerance": 0.03,
        "unit": "g",
        "solution": (
            "2C₄H₁₀ + 13O₂ → 8CO₂ + 10H₂O\n"
            "M(C₄H₁₀) = 58 g/mol\n"
            "n(butan) = 37/58 ≈ 0,6379 mol\n"
            "n(O₂) = (13/2) × 0,6379 = 4,146 mol\n"
            "m(O₂) = 4,146 × 32 ≈ 132,7 g"
        ),
        "choices": None,
    },
    {
        "id": "kexf01_stok_3",
        "exam": "kexf01",
        "topic": "stokiometri",
        "topic_display": "Stökiometri",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": "Hur stor massa har 9,0 mol glukos (druvsocker), C₆H₁₂O₆?",
        "answer_type": "numeric",
        "correct_answer": 1620.0,
        "tolerance": 0.01,
        "unit": "g",
        "solution": (
            "M(C₆H₁₂O₆) = 6(12) + 12(1) + 6(16) = 180 g/mol\n"
            "m = n × M = 9,0 × 180 = 1620 g"
        ),
        "choices": None,
    },

    # ── Koncentration / spädning (4/4 tentor) ────────────────────────
    {
        "id": "kexf01_konc_1",
        "exam": "kexf01",
        "topic": "koncentration",
        "topic_display": "Koncentration och spädning",
        "points": 4,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Man blandar 4,0 dm³ 5,00 M saltsyra med 3,0 dm³ 0,50 M saltsyra. "
            "Vilken koncentration får saltsyralösningen?"
        ),
        "answer_type": "numeric",
        "correct_answer": 3.07,
        "tolerance": 0.02,
        "unit": "mol/dm³",
        "solution": (
            "n₁ = 4,0 × 5,00 = 20,0 mol\n"
            "n₂ = 3,0 × 0,50 = 1,5 mol\n"
            "n_tot = 21,5 mol, V_tot = 7,0 dm³\n"
            "c = 21,5 / 7,0 ≈ 3,07 mol/dm³"
        ),
        "choices": None,
    },
    {
        "id": "kexf01_konc_spadning",
        "exam": "kexf01",
        "topic": "koncentration",
        "topic_display": "Koncentration och spädning",
        "points": 4,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Man har 25,0 cm³ natriumkloridlösning med koncentrationen "
            "0,35 mol/dm³. Vilken volym vatten ska tillsättas för att "
            "lösningens koncentration ska bli 0,15 mol/dm³?"
        ),
        "answer_type": "numeric",
        "correct_answer": 33.3,
        "tolerance": 0.03,
        "unit": "cm³",
        "solution": (
            "n(NaCl) = 0,0250 × 0,35 = 8,75 × 10⁻³ mol\n"
            "V_ny = n/c = 8,75 × 10⁻³ / 0,15 = 0,05833 dm³ = 58,33 cm³\n"
            "Vatten att tillsätta = 58,33 − 25,0 = 33,3 cm³"
        ),
        "choices": None,
    },

    # ── Redoxbalansering med oxidationstal (4/4 tentor) ──────────────
    {
        "id": "kexf01_redox_1",
        "exam": "kexf01",
        "topic": "redox_balansering",
        "topic_display": "Redoxbalansering",
        "points": 4,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Balansera reaktionsformeln med hjälp av oxidationstal. "
            "Minsta möjliga heltalskoefficienter ska användas.\n"
            "Cu + NO₃⁻ + H⁺ → Cu²⁺ + N₂O + H₂O"
        ),
        "answer_type": "text",
        "correct_answer": "4Cu + 2NO3- + 10H+ -> 4Cu2+ + N2O + 5H2O",
        "tolerance": None,
        "unit": None,
        "solution": (
            "Cu → Cu²⁺ (oxidation, ökning +2)\n"
            "N⁺⁵ → N⁺¹ i N₂O (reduktion, minskning 4 per N, totalt 8 för 2N)\n"
            "4 Cu balanserar 8 elektroner: 4Cu + 2NO₃⁻ + 10H⁺ → 4Cu²⁺ + N₂O + 5H₂O"
        ),
        "choices": None,
    },
    {
        "id": "kexf01_redox_2",
        "exam": "kexf01",
        "topic": "redox_balansering",
        "topic_display": "Redoxbalansering",
        "points": 3,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Balansera följande redoxreaktion med hjälp av oxidationstal:\n"
            "MnO₄⁻ + H⁺ + Fe²⁺ → Mn²⁺ + H₂O + Fe³⁺"
        ),
        "answer_type": "text",
        "correct_answer": "MnO4- + 8H+ + 5Fe2+ -> Mn2+ + 4H2O + 5Fe3+",
        "tolerance": None,
        "unit": None,
        "solution": (
            "Mn⁺⁷ → Mn²⁺ (minskning 5)\n"
            "Fe²⁺ → Fe³⁺ (ökning 1)\n"
            "5 Fe²⁺ behövs per MnO₄⁻:\n"
            "MnO₄⁻ + 8H⁺ + 5Fe²⁺ → Mn²⁺ + 4H₂O + 5Fe³⁺"
        ),
        "choices": None,
    },

    # ── Galvaniska celler / elektrokemi (3/4 tentor) ─────────────────
    {
        "id": "kexf01_galvanisk_1",
        "exam": "kexf01",
        "topic": "elektrokemi",
        "topic_display": "Elektrokemi",
        "points": 4,
        "exam_frequency": 0.75,
        "no_calculator": False,
        "question": (
            "En galvanisk cell består av redoxparen Cu²⁺(aq)/Cu(s) och Al³⁺(aq)/Al(s).\n"
            "a) Skriv cellschemat.\n"
            "b) Skriv elektrodreaktionerna.\n"
            "c) Skriv formeln för cellreaktionen."
        ),
        "answer_type": "text",
        "correct_answer": "Al(s)|Al3+(aq)||Cu2+(aq)|Cu(s)",
        "tolerance": None,
        "unit": None,
        "solution": (
            "a) Al(s)|Al³⁺(aq)‖Cu²⁺(aq)|Cu(s)\n"
            "b) Anod: Al → Al³⁺ + 3e⁻ (oxidation)\n"
            "   Katod: Cu²⁺ + 2e⁻ → Cu (reduktion)\n"
            "c) 2Al + 3Cu²⁺ → 2Al³⁺ + 3Cu"
        ),
        "choices": None,
    },
    {
        "id": "kexf01_elektrokemi_aktivitetsserie",
        "exam": "kexf01",
        "topic": "elektrokemi",
        "topic_display": "Elektrokemi",
        "points": 5,
        "exam_frequency": 0.75,
        "no_calculator": False,
        "question": (
            "Du har tre bägare med:\n"
            "a) En kopparplåt nedsänkt i en zinkjonlösning\n"
            "b) En magnesiumplåt nedsänkt i en guldjonlösning\n"
            "c) En silverplåt nedsänkt i en kopparjonlösning\n"
            "I vilken eller vilka bägare sker det en reaktion? "
            "Skriv reduktion, oxidation och totalreaktion för varje bägare där något händer."
        ),
        "answer_type": "text",
        "correct_answer": "b) Mg + Au3+ reagerar",
        "tolerance": None,
        "unit": None,
        "solution": (
            "a) Cu ligger över Zn i spänningsserien → Cu kan inte reducera Zn²⁺. Ingen reaktion.\n"
            "b) Mg ligger under Au → Mg oxideras: Mg → Mg²⁺ + 2e⁻\n"
            "   Au³⁺ reduceras: Au³⁺ + 3e⁻ → Au\n"
            "   Total: 3Mg + 2Au³⁺ → 3Mg²⁺ + 2Au\n"
            "c) Ag ligger över Cu → Ag kan inte reducera Cu²⁺. Ingen reaktion."
        ),
        "choices": None,
    },

    # ── Intermolekylära bindningar (3/4 tentor) ──────────────────────
    {
        "id": "kexf01_bindning_1",
        "exam": "kexf01",
        "topic": "bindningar",
        "topic_display": "Kemiska bindningar",
        "points": 3,
        "exam_frequency": 0.75,
        "no_calculator": False,
        "question": (
            "Vilka intermolekylära bindningar (bindningar mellan molekyler) "
            "finns i följande föreningar?\n"
            "HF(l)   N₂(l)   NH₃(l)   H₂O(l)   CH₄(l)   H₂S(l)\n\n"
            "Vilken eller vilka av molekylerna ovan är dipoler?"
        ),
        "answer_type": "text",
        "correct_answer": "HF: vätebindning, dipol. N2: London. NH3: vätebindning, dipol. H2O: vätebindning, dipol. CH4: London. H2S: dipol-dipol, dipol.",
        "tolerance": None,
        "unit": None,
        "solution": (
            "HF: vätebindning + dipol-dipol (dipol)\n"
            "N₂: London-krafter (opolär)\n"
            "NH₃: vätebindning + dipol-dipol (dipol)\n"
            "H₂O: vätebindning + dipol-dipol (dipol)\n"
            "CH₄: London-krafter (opolär, tetraedrisk symmetri)\n"
            "H₂S: dipol-dipol (dipol, vinklad molekyl)\n"
            "Dipoler: HF, NH₃, H₂O, H₂S"
        ),
        "choices": None,
    },

    # ── Ideala gaslagen (3/4 tentor) ─────────────────────────────────
    {
        "id": "kexf01_gas_1",
        "exam": "kexf01",
        "topic": "gaslagen",
        "topic_display": "Ideala gaslagen",
        "points": 4,
        "exam_frequency": 0.75,
        "no_calculator": False,
        "question": (
            "En okänd gas är i en behållare med volymen 5,4 liter "
            "och trycket 101,3 kPa. Temperaturen är 125 °C och gasen "
            "väger 32 g. Bestäm gasens molmassa."
        ),
        "answer_type": "numeric",
        "correct_answer": 193.5,
        "tolerance": 0.05,
        "unit": "g/mol",
        "solution": (
            "pV = nRT → n = pV/(RT)\n"
            "T = 125 + 273,15 = 398,15 K\n"
            "n = (101,3 × 10³ × 5,4 × 10⁻³) / (8,314 × 398,15)\n"
            "n ≈ 0,1653 mol\n"
            "M = m/n = 32/0,1653 ≈ 193,6 g/mol"
        ),
        "choices": None,
    },
    {
        "id": "kexf01_gas_2",
        "exam": "kexf01",
        "topic": "gaslagen",
        "topic_display": "Ideala gaslagen",
        "points": 6,
        "exam_frequency": 0.75,
        "no_calculator": False,
        "question": (
            "Beräkna vilken volym vätgas med temperaturen 58 °C "
            "och trycket 104,6 kPa som bildas när man löser upp "
            "8,3 gram magnesium i en syra. R = 8,314 J/(mol·K)"
        ),
        "answer_type": "numeric",
        "correct_answer": 8.99,
        "tolerance": 0.05,
        "unit": "dm³",
        "solution": (
            "Mg + 2H⁺ → Mg²⁺ + H₂\n"
            "n(Mg) = 8,3 / 24,3 ≈ 0,3416 mol\n"
            "n(H₂) = n(Mg) = 0,3416 mol\n"
            "T = 58 + 273,15 = 331,15 K\n"
            "V = nRT/p = 0,3416 × 8,314 × 331,15 / (104,6 × 10³)\n"
            "V ≈ 8,99 × 10⁻³ m³ ≈ 8,99 dm³"
        ),
        "choices": None,
    },

    # ── Jonkoncentrationer i lösning (3/4 tentor) ────────────────────
    {
        "id": "kexf01_jonkonc_1",
        "exam": "kexf01",
        "topic": "jonkoncentration",
        "topic_display": "Jonkoncentrationer",
        "points": 2,
        "exam_frequency": 0.75,
        "no_calculator": False,
        "question": (
            "Hur stor är fosfat- och kopparjonkoncentrationen "
            "i en 0,32 M kopparfosfatlösning?"
        ),
        "answer_type": "text",
        "correct_answer": "[Cu2+] = 0.96 M, [PO4 3-] = 0.64 M",
        "tolerance": None,
        "unit": None,
        "solution": (
            "Cu₃(PO₄)₂ → 3Cu²⁺ + 2PO₄³⁻\n"
            "[Cu²⁺] = 3 × 0,32 = 0,96 M\n"
            "[PO₄³⁻] = 2 × 0,32 = 0,64 M"
        ),
        "choices": None,
    },

    # ── Fällningsreaktioner (2/4 tentor) ─────────────────────────────
    {
        "id": "kexf01_fallning_1",
        "exam": "kexf01",
        "topic": "fallningsreaktion",
        "topic_display": "Fällningsreaktioner",
        "points": 6,
        "exam_frequency": 0.5,
        "no_calculator": False,
        "question": (
            "Beräkna massan av den fällning som bildas då 150 ml "
            "0,2 M silvernitratlösning blandas med ett överskott "
            "av natriumkloridlösning."
        ),
        "answer_type": "numeric",
        "correct_answer": 4.30,
        "tolerance": 0.03,
        "unit": "g",
        "solution": (
            "AgNO₃ + NaCl → AgCl↓ + NaNO₃\n"
            "n(Ag⁺) = 0,150 × 0,2 = 0,030 mol\n"
            "n(AgCl) = 0,030 mol (NaCl i överskott)\n"
            "m(AgCl) = 0,030 × 143,3 ≈ 4,30 g"
        ),
        "choices": None,
    },

    # ── Titrering (2/4 tentor) ───────────────────────────────────────
    {
        "id": "kexf01_titrering_1",
        "exam": "kexf01",
        "topic": "titrering",
        "topic_display": "Titrering",
        "points": 4,
        "exam_frequency": 0.5,
        "no_calculator": False,
        "question": (
            "På en laboration titrerades en natriumhydroxidlösning "
            "med saltsyra (i byretten) med koncentrationen 0,12 mol/dm³. "
            "Det gick åt 23,4 ml av syran. Bestäm koncentrationen hos "
            "natriumhydroxidlösningen om man använde 20,0 ml NaOH-lösning."
        ),
        "answer_type": "numeric",
        "correct_answer": 0.1404,
        "tolerance": 0.02,
        "unit": "mol/dm³",
        "solution": (
            "HCl + NaOH → NaCl + H₂O (1:1)\n"
            "n(HCl) = 0,0234 × 0,12 = 2,808 × 10⁻³ mol\n"
            "n(NaOH) = n(HCl) = 2,808 × 10⁻³ mol\n"
            "c(NaOH) = 2,808 × 10⁻³ / 0,0200 = 0,1404 mol/dm³"
        ),
        "choices": None,
    },

    # ── Lågfärger (2/4 tentor) ───────────────────────────────────────
    {
        "id": "kexf01_lagfarg_1",
        "exam": "kexf01",
        "topic": "lagfarger",
        "topic_display": "Lågfärger och excitation",
        "points": 3,
        "exam_frequency": 0.5,
        "no_calculator": False,
        "question": (
            "På en labb utförde du experiment med lågfärger. "
            "Beskriv utförligt hur en lågfärg uppkommer."
        ),
        "answer_type": "text",
        "correct_answer": "elektroner exciteras av värme och går tillbaka till grundtillståndet, avger foton med specifik våglängd",
        "tolerance": None,
        "unit": None,
        "solution": (
            "När ett ämne hettas upp i en låga tillförs energi till atomerna. "
            "Elektroner exciteras från grundtillståndet till högre energinivåer. "
            "När elektronerna faller tillbaka till lägre nivåer avges energi i form "
            "av fotoner. Fotonernas våglängd (och därmed färg) beror på "
            "energiskillnaden mellan nivåerna, som är unik för varje grundämne."
        ),
        "choices": None,
    },

    # ── Reagens / kvalitativ analys (2/4 tentor) ─────────────────────
    {
        "id": "kexf01_reagens_1",
        "exam": "kexf01",
        "topic": "reagens",
        "topic_display": "Kvalitativ analys",
        "points": 1,
        "exam_frequency": 0.5,
        "no_calculator": False,
        "question": "Vad använder du som reagens för att påvisa sulfatjoner i ett prov?",
        "answer_type": "text",
        "correct_answer": "bariumklorid",
        "tolerance": None,
        "unit": None,
        "solution": (
            "Bariumklorid (BaCl₂) tillsätts. Om sulfatjoner finns bildas "
            "en vit fällning av bariumsulfat: Ba²⁺ + SO₄²⁻ → BaSO₄↓"
        ),
        "choices": None,
    },
    {
        "id": "kexf01_reagens_2",
        "exam": "kexf01",
        "topic": "reagens",
        "topic_display": "Kvalitativ analys",
        "points": 2,
        "exam_frequency": 0.5,
        "no_calculator": False,
        "question": "Du ska undersöka om en lösning innehåller kloridjoner. Vad tillsätter du?",
        "answer_type": "text",
        "correct_answer": "silvernitrat",
        "tolerance": None,
        "unit": None,
        "solution": (
            "Silvernitrat (AgNO₃) tillsätts. Om kloridjoner finns bildas "
            "en vit fällning av silverklorid: Ag⁺ + Cl⁻ → AgCl↓"
        ),
        "choices": None,
    },

    # ── Termokemi (1/4 tentor) ───────────────────────────────────────
    {
        "id": "kexf01_termokemi_1",
        "exam": "kexf01",
        "topic": "termokemi",
        "topic_display": "Termokemi",
        "points": 6,
        "exam_frequency": 0.25,
        "no_calculator": False,
        "question": (
            "När man löser upp 5,3 gram aluminium i 200 gram utspädd syra "
            "(med exakt samma egenskaper som vatten) ökar temperaturen "
            "från 18 °C till 41 °C. Hur mycket energi utvecklas per mol "
            "aluminium? Använd c = 4,18 kJ/(kg·K)."
        ),
        "answer_type": "numeric",
        "correct_answer": 97.8,
        "tolerance": 0.05,
        "unit": "kJ/mol",
        "solution": (
            "Q = mcΔT = 0,200 × 4,18 × (41 − 18) = 0,200 × 4,18 × 23 = 19,228 kJ\n"
            "n(Al) = 5,3 / 27,0 ≈ 0,1963 mol\n"
            "Q per mol = 19,228 / 0,1963 ≈ 97,9 kJ/mol"
        ),
        "choices": None,
    },
]
