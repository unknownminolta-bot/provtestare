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
            "a) $\\text{Ba(NO}_3\\text{)}_2$\n"
            "b) $\\text{PbS}$\n"
            "c) $\\text{Mg(OH)}_2$\n"
            "d) $\\text{Sn(ClO}_4\\text{)}_2$"
        ),
        "answer_type": "text",
        "correct_answer": "a) Bariumnitrat b) Blysulfid c) Magnesiumhydroxid d) Tenn(II)perklorat",
        "tolerance": None,
        "unit": None,
        "solution": (
            "a) $\\text{Ba}^{2+} + \\text{NO}_3^- \\to$ Bariumnitrat\n"
            "b) $\\text{Pb}^{2+} + \\text{S}^{2-} \\to$ Blysulfid (bly(II)sulfid)\n"
            "c) $\\text{Mg}^{2+} + \\text{OH}^- \\to$ Magnesiumhydroxid\n"
            "d) $\\text{Sn}^{2+} + \\text{ClO}_4^- \\to$ Tenn(II)perklorat"
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
            "a) $\\text{Ni}^{2+}$ och $\\text{ClO}_2^-$ $\\to$ $\\text{Ni(ClO}_2\\text{)}_2$\n"
            "b) $\\text{Cs}^+$ och $\\text{HPO}_4^{2-}$ $\\to$ $\\text{Cs}_2\\text{HPO}_4$\n"
            "c) $\\text{Sn}^{4+}$ och $\\text{MnO}_4^-$ $\\to$ $\\text{Sn(MnO}_4\\text{)}_4$\n"
            "d) $\\text{NH}_4^+$ och $\\text{CrO}_4^{2-}$ $\\to$ $\\text{(NH}_4\\text{)}_2\\text{CrO}_4$"
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
            "a) $\\text{Zn}^{2+}$ och $\\text{PO}_4^{3-}$ $\\to$ $\\text{Zn}_3\\text{(PO}_4\\text{)}_2$\n"
            "b) $\\text{Ca}^{2+}$ och $\\text{SO}_4^{2-}$ $\\to$ $\\text{CaSO}_4$\n"
            "c) $\\text{Cr}^{3+}$ och $\\text{F}^-$ $\\to$ $\\text{CrF}_3$\n"
            "d) $\\text{K}^+$ och $\\text{Cr}_2\\text{O}_7^{2-}$ $\\to$ $\\text{K}_2\\text{Cr}_2\\text{O}_7$\n"
            "e) $\\text{Mg}^{2+}$ och $\\text{NO}_2^-$ $\\to$ $\\text{Mg(NO}_2\\text{)}_2$"
        ),
        "choices": None,
    },

    # ── Balansering av reaktionsformler (4/4 tentor) ─────────────────
    {
        "id": "kexf01_balans_1",
        "exam": "kexf01",
        "topic": "balansering",
        "topic_display": "Balansering av reaktionsformler",
        "points": 6,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Skriv och balansera reaktionsformlerna för följande reaktioner:\n"
            "a) Metan förbränns fullständigt i syrgas\n"
            "b) Kiseloxid reagerar med aluminium och bildar kisel och aluminiumoxid\n"
            "c) Saltsyra reagerar med syrgas och bildar klorgas och vatten\n"
            "d) Kalciumfosfid reagerar med vatten och bildar fosfin och kalciumhydroxid"
        ),
        "answer_type": "text",
        "correct_answer": "a) 1,2,1,2 b) 3,4,3,2 c) 4,1,2,2 d) 1,6,2,3",
        "tolerance": None,
        "unit": None,
        "solution": (
            "a) $\\text{CH}_4 + 2\\text{O}_2 \\to \\text{CO}_2 + 2\\text{H}_2\\text{O}$\n"
            "b) $3\\text{SiO}_2 + 4\\text{Al} \\to 3\\text{Si} + 2\\text{Al}_2\\text{O}_3$\n"
            "c) $4\\text{HCl} + \\text{O}_2 \\to 2\\text{Cl}_2 + 2\\text{H}_2\\text{O}$\n"
            "d) $\\text{Ca}_3\\text{P}_2 + 6\\text{H}_2\\text{O} \\to 2\\text{PH}_3 + 3\\text{Ca(OH)}_2$"
        ),
        "choices": None,
    },
    {
        "id": "kexf01_balans_2",
        "exam": "kexf01",
        "topic": "balansering",
        "topic_display": "Balansering av reaktionsformler",
        "points": 3,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": "Skriv och balansera reaktionsformeln för fullständig förbränning av $\\text{C}_7\\text{H}_{12}$ i syrgas.",
        "answer_type": "text",
        "correct_answer": "C7H12 + 10O2 -> 7CO2 + 6H2O",
        "tolerance": None,
        "unit": None,
        "solution": (
            "$\\text{C}_7\\text{H}_{12} + 10\\text{O}_2 \\to 7\\text{CO}_2 + 6\\text{H}_2\\text{O}$\n"
            "Kontroll: C: $7=7$, H: $12=12$, O: $20=14+6=20$ ✓"
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
            "a) $\\text{CrO}_2$\n"
            "b) $\\text{Cr}_2\\text{O}_3$\n"
            "c) $\\text{CrO}_4^{2-}$"
        ),
        "answer_type": "text",
        "correct_answer": "a) +4 b) +3 c) +6",
        "tolerance": None,
        "unit": None,
        "solution": (
            "a) $\\text{CrO}_2$: $\\text{Cr} + 2(-2) = 0 \\to \\text{Cr} = +4$\n"
            "b) $\\text{Cr}_2\\text{O}_3$: $2\\text{Cr} + 3(-2) = 0 \\to \\text{Cr} = +3$\n"
            "c) $\\text{CrO}_4^{2-}$: $\\text{Cr} + 4(-2) = -2 \\to \\text{Cr} = +6$"
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
            "a) $\\text{VO}$\n"
            "b) $\\text{VO}_2$\n"
            "c) $\\text{V}_2\\text{O}_5$\n"
            "d) $\\text{VO}_3^-$"
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "D",
        "tolerance": None,
        "unit": None,
        "solution": (
            "a) $\\text{VO}$: $\\text{V} = +2$\n"
            "b) $\\text{VO}_2$: $\\text{V} = +4$\n"
            "c) $\\text{V}_2\\text{O}_5$: $\\text{V} = +5$\n"
            "d) $\\text{VO}_3^-$: $\\text{V} + 3(-2) = -1 \\to \\text{V} = +5$. "
            "Men $\\text{VO}_3^-$ kräver $\\text{V} = +5$, samma som c). "
            "Dock tolkas tentans facit som D."
        ),
        "choices": [
            "A) $\\text{VO}$",
            "B) $\\text{VO}_2$",
            "C) $\\text{V}_2\\text{O}_5$",
            "D) $\\text{VO}_3^-$",
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
        "question": "Beräkna pH i en lösning av $0{,}000012\\;\\text{mol/dm}^3$ $\\text{NaOH}$.",
        "answer_type": "numeric",
        "correct_answer": 9.08,
        "tolerance": 0.02,
        "unit": "",
        "solution": (
            "$[\\text{OH}^-] = 1{,}2 \\times 10^{-5}\\;\\text{mol/dm}^3$\n"
            "$\\text{pOH} = -\\log(1{,}2 \\times 10^{-5}) \\approx 4{,}92$\n"
            "$\\text{pH} = 14 - \\text{pOH} \\approx 9{,}08$"
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
        "question": "Ange pH i saltsyra som har koncentrationen $0{,}0025\\;\\text{mol/dm}^3$.",
        "answer_type": "numeric",
        "correct_answer": 2.60,
        "tolerance": 0.02,
        "unit": "",
        "solution": (
            "$\\text{HCl}$ är en stark syra: $[\\text{H}^+] = 0{,}0025\\;\\text{mol/dm}^3$\n"
            "$\\text{pH} = -\\log(0{,}0025) \\approx 2{,}60$"
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
            "Vad är pH i en blandning av $0{,}645\\;\\text{dm}^3$ $0{,}0035\\;\\text{mol/dm}^3$ $\\text{HNO}_3$ "
            "och $1200\\;\\text{ml}$ $0{,}0015\\;\\text{mol/dm}^3$ $\\text{NaOH}$?"
        ),
        "answer_type": "numeric",
        "correct_answer": 3.61,
        "tolerance": 0.03,
        "unit": "",
        "solution": (
            "$n(\\text{H}^+) = 0{,}645 \\times 0{,}0035 = 2{,}2575 \\times 10^{-3}\\;\\text{mol}$\n"
            "$n(\\text{OH}^-) = 1{,}200 \\times 0{,}0015 = 1{,}800 \\times 10^{-3}\\;\\text{mol}$\n"
            "Överskott $\\text{H}^+$: $2{,}2575 \\times 10^{-3} - 1{,}800 \\times 10^{-3} = 4{,}575 \\times 10^{-4}\\;\\text{mol}$\n"
            "$V_{\\text{tot}} = 0{,}645 + 1{,}200 = 1{,}845\\;\\text{dm}^3$\n"
            "$[\\text{H}^+] = 4{,}575 \\times 10^{-4} / 1{,}845 \\approx 2{,}48 \\times 10^{-4}\\;\\text{mol/dm}^3$\n"
            "$\\text{pH} = -\\log(2{,}48 \\times 10^{-4}) \\approx 3{,}61$"
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
            "Du har $500\\;\\text{ml}$ $1{,}6\\;\\text{mol/dm}^3$ saltsyra i en hink. "
            "Du häller i $9$ liter rent vatten. Vilket pH blir det?"
        ),
        "answer_type": "numeric",
        "correct_answer": 1.07,
        "tolerance": 0.03,
        "unit": "",
        "solution": (
            "$n(\\text{HCl}) = 0{,}500 \\times 1{,}6 = 0{,}800\\;\\text{mol}$\n"
            "$V_{\\text{tot}} = 0{,}500 + 9{,}000 = 9{,}500\\;\\text{dm}^3$\n"
            "$[\\text{H}^+] = 0{,}800 / 9{,}500 \\approx 0{,}0842\\;\\text{mol/dm}^3$\n"
            "$\\text{pH} = -\\log(0{,}0842) \\approx 1{,}07$"
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
            "$220\\;\\text{g}$ glukos ($\\text{C}_6\\text{H}_{12}\\text{O}_6$) förbränns fullständigt. "
            "Ställ upp den balanserade reaktionsformeln och beräkna massan koldioxid som bildas."
        ),
        "answer_type": "numeric",
        "correct_answer": 322.7,
        "tolerance": 0.02,
        "unit": "g",
        "solution": (
            "$\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O}$\n"
            "$M(\\text{C}_6\\text{H}_{12}\\text{O}_6) = 180\\;\\text{g/mol}$\n"
            "$n(\\text{glukos}) = 220/180 \\approx 1{,}222\\;\\text{mol}$\n"
            "$n(\\text{CO}_2) = 6 \\times 1{,}222 = 7{,}333\\;\\text{mol}$\n"
            "$m(\\text{CO}_2) = 7{,}333 \\times 44 \\approx 322{,}7\\;\\text{g}$"
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
            "$37\\;\\text{g}$ butan ($\\text{C}_4\\text{H}_{10}$) förbränns fullständigt i syrgas.\n"
            "a) Ställ upp den balanserade reaktionsformeln med minsta möjliga heltalskoefficienter.\n"
            "b) Beräkna massan syre som förbrukas."
        ),
        "answer_type": "numeric",
        "correct_answer": 132.7,
        "tolerance": 0.03,
        "unit": "g",
        "solution": (
            "$2\\text{C}_4\\text{H}_{10} + 13\\text{O}_2 \\to 8\\text{CO}_2 + 10\\text{H}_2\\text{O}$\n"
            "$M(\\text{C}_4\\text{H}_{10}) = 58\\;\\text{g/mol}$\n"
            "$n(\\text{butan}) = 37/58 \\approx 0{,}6379\\;\\text{mol}$\n"
            "$n(\\text{O}_2) = (13/2) \\times 0{,}6379 = 4{,}146\\;\\text{mol}$\n"
            "$m(\\text{O}_2) = 4{,}146 \\times 32 \\approx 132{,}7\\;\\text{g}$"
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
        "question": "Hur stor massa har $9{,}0\\;\\text{mol}$ glukos (druvsocker), $\\text{C}_6\\text{H}_{12}\\text{O}_6$?",
        "answer_type": "numeric",
        "correct_answer": 1620.0,
        "tolerance": 0.01,
        "unit": "g",
        "solution": (
            "$M(\\text{C}_6\\text{H}_{12}\\text{O}_6) = 6(12) + 12(1) + 6(16) = 180\\;\\text{g/mol}$\n"
            "$m = n \\times M = 9{,}0 \\times 180 = 1620\\;\\text{g}$"
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
            "Man blandar $4{,}0\\;\\text{dm}^3$ $5{,}00\\;\\text{M}$ saltsyra med $3{,}0\\;\\text{dm}^3$ $0{,}50\\;\\text{M}$ saltsyra. "
            "Vilken koncentration får saltsyralösningen?"
        ),
        "answer_type": "numeric",
        "correct_answer": 3.07,
        "tolerance": 0.02,
        "unit": "mol/dm³",
        "solution": (
            "$n_1 = 4{,}0 \\times 5{,}00 = 20{,}0\\;\\text{mol}$\n"
            "$n_2 = 3{,}0 \\times 0{,}50 = 1{,}5\\;\\text{mol}$\n"
            "$n_{\\text{tot}} = 21{,}5\\;\\text{mol}$, $V_{\\text{tot}} = 7{,}0\\;\\text{dm}^3$\n"
            "$c = 21{,}5 / 7{,}0 \\approx 3{,}07\\;\\text{mol/dm}^3$"
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
            "Man har $25{,}0\\;\\text{cm}^3$ natriumkloridlösning med koncentrationen "
            "$0{,}35\\;\\text{mol/dm}^3$. Vilken volym vatten ska tillsättas för att "
            "lösningens koncentration ska bli $0{,}15\\;\\text{mol/dm}^3$?"
        ),
        "answer_type": "numeric",
        "correct_answer": 33.3,
        "tolerance": 0.03,
        "unit": "cm³",
        "solution": (
            "$n(\\text{NaCl}) = 0{,}0250 \\times 0{,}35 = 8{,}75 \\times 10^{-3}\\;\\text{mol}$\n"
            "$V_{\\text{ny}} = n/c = 8{,}75 \\times 10^{-3} / 0{,}15 = 0{,}05833\\;\\text{dm}^3 = 58{,}33\\;\\text{cm}^3$\n"
            "Vatten att tillsätta $= 58{,}33 - 25{,}0 = 33{,}3\\;\\text{cm}^3$"
        ),
        "choices": None,
    },

    # ── Redoxbalansering med oxidationstal (4/4 tentor) ──────────────
    {
        "id": "kexf01_redox_1",
        "exam": "kexf01",
        "topic": "redox_balansering",
        "topic_display": "Redoxbalansering",
        "points": 5,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Koppar löses i utspädd salpetersyra under sur miljö. Koppar oxideras till koppar(II)-joner "
            "och nitratjoner reduceras till dikväveoxid ($\\text{N}_2\\text{O}$). "
            "Ställ upp och balansera den fullständiga redoxreaktionen med hjälp av oxidationstal. "
            "Minsta möjliga heltalskoefficienter ska användas."
        ),
        "answer_type": "text",
        "correct_answer": "4Cu + 2NO3- + 10H+ -> 4Cu2+ + N2O + 5H2O",
        "tolerance": None,
        "unit": None,
        "solution": (
            "$\\text{Cu} \\to \\text{Cu}^{2+}$ (oxidation, ökning $+2$)\n"
            "$\\text{N}^{+5} \\to \\text{N}^{+1}$ i $\\text{N}_2\\text{O}$ (reduktion, minskning $4$ per N, totalt $8$ för $2$ N)\n"
            "$4$ Cu balanserar $8$ elektroner: $4\\text{Cu} + 2\\text{NO}_3^- + 10\\text{H}^+ \\to 4\\text{Cu}^{2+} + \\text{N}_2\\text{O} + 5\\text{H}_2\\text{O}$"
        ),
        "choices": None,
    },
    {
        "id": "kexf01_redox_2",
        "exam": "kexf01",
        "topic": "redox_balansering",
        "topic_display": "Redoxbalansering",
        "points": 4,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "I sur lösning reagerar permanganatjoner med järn(II)-joner. Permanganat reduceras till "
            "mangan(II)-joner och järn(II) oxideras till järn(III). "
            "Ställ upp och balansera den fullständiga redoxreaktionen med hjälp av oxidationstal."
        ),
        "answer_type": "text",
        "correct_answer": "MnO4- + 8H+ + 5Fe2+ -> Mn2+ + 4H2O + 5Fe3+",
        "tolerance": None,
        "unit": None,
        "solution": (
            "$\\text{Mn}^{+7} \\to \\text{Mn}^{2+}$ (minskning $5$)\n"
            "$\\text{Fe}^{2+} \\to \\text{Fe}^{3+}$ (ökning $1$)\n"
            "$5$ $\\text{Fe}^{2+}$ behövs per $\\text{MnO}_4^-$:\n"
            "$\\text{MnO}_4^- + 8\\text{H}^+ + 5\\text{Fe}^{2+} \\to \\text{Mn}^{2+} + 4\\text{H}_2\\text{O} + 5\\text{Fe}^{3+}$"
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
            "En galvanisk cell består av redoxparen $\\text{Cu}^{2+}\\text{(aq)}/\\text{Cu(s)}$ och $\\text{Al}^{3+}\\text{(aq)}/\\text{Al(s)}$.\n"
            "a) Skriv cellschemat.\n"
            "b) Skriv elektrodreaktionerna.\n"
            "c) Skriv formeln för cellreaktionen."
        ),
        "answer_type": "text",
        "correct_answer": "Al(s)|Al3+(aq)||Cu2+(aq)|Cu(s)",
        "tolerance": None,
        "unit": None,
        "solution": (
            "a) $\\text{Al(s)}|\\text{Al}^{3+}\\text{(aq)}\\|\\text{Cu}^{2+}\\text{(aq)}|\\text{Cu(s)}$\n"
            "b) Anod: $\\text{Al} \\to \\text{Al}^{3+} + 3e^-$ (oxidation)\n"
            "   Katod: $\\text{Cu}^{2+} + 2e^- \\to \\text{Cu}$ (reduktion)\n"
            "c) $2\\text{Al} + 3\\text{Cu}^{2+} \\to 2\\text{Al}^{3+} + 3\\text{Cu}$"
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
            "a) $\\text{Cu}$ ligger över $\\text{Zn}$ i spänningsserien $\\to$ $\\text{Cu}$ kan inte reducera $\\text{Zn}^{2+}$. Ingen reaktion.\n"
            "b) $\\text{Mg}$ ligger under $\\text{Au}$ $\\to$ $\\text{Mg}$ oxideras: $\\text{Mg} \\to \\text{Mg}^{2+} + 2e^-$\n"
            "   $\\text{Au}^{3+}$ reduceras: $\\text{Au}^{3+} + 3e^- \\to \\text{Au}$\n"
            "   Total: $3\\text{Mg} + 2\\text{Au}^{3+} \\to 3\\text{Mg}^{2+} + 2\\text{Au}$\n"
            "c) $\\text{Ag}$ ligger över $\\text{Cu}$ $\\to$ $\\text{Ag}$ kan inte reducera $\\text{Cu}^{2+}$. Ingen reaktion."
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
            "$\\text{HF(l)}$   $\\text{N}_2\\text{(l)}$   $\\text{NH}_3\\text{(l)}$   $\\text{H}_2\\text{O(l)}$   $\\text{CH}_4\\text{(l)}$   $\\text{H}_2\\text{S(l)}$\n\n"
            "Vilken eller vilka av molekylerna ovan är dipoler?"
        ),
        "answer_type": "text",
        "correct_answer": "HF: vätebindning, dipol. N2: London. NH3: vätebindning, dipol. H2O: vätebindning, dipol. CH4: London. H2S: dipol-dipol, dipol.",
        "tolerance": None,
        "unit": None,
        "solution": (
            "$\\text{HF}$: vätebindning + dipol-dipol (dipol)\n"
            "$\\text{N}_2$: London-krafter (opolär)\n"
            "$\\text{NH}_3$: vätebindning + dipol-dipol (dipol)\n"
            "$\\text{H}_2\\text{O}$: vätebindning + dipol-dipol (dipol)\n"
            "$\\text{CH}_4$: London-krafter (opolär, tetraedrisk symmetri)\n"
            "$\\text{H}_2\\text{S}$: dipol-dipol (dipol, vinklad molekyl)\n"
            "Dipoler: $\\text{HF}$, $\\text{NH}_3$, $\\text{H}_2\\text{O}$, $\\text{H}_2\\text{S}$"
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
            "En okänd gas är i en behållare med volymen $5{,}4\\;\\text{liter}$ "
            "och trycket $101{,}3\\;\\text{kPa}$. Temperaturen är $125\\;°\\text{C}$ och gasen "
            "väger $32\\;\\text{g}$. Bestäm gasens molmassa."
        ),
        "answer_type": "numeric",
        "correct_answer": 193.5,
        "tolerance": 0.05,
        "unit": "g/mol",
        "solution": (
            "$pV = nRT \\to n = \\frac{pV}{RT}$\n"
            "$T = 125 + 273{,}15 = 398{,}15\\;\\text{K}$\n"
            "$n = \\frac{101{,}3 \\times 10^3 \\times 5{,}4 \\times 10^{-3}}{8{,}314 \\times 398{,}15}$\n"
            "$n \\approx 0{,}1653\\;\\text{mol}$\n"
            "$M = m/n = 32/0{,}1653 \\approx 193{,}6\\;\\text{g/mol}$"
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
            "$8{,}3\\;\\text{g}$ magnesium löses upp i utspädd saltsyra. "
            "Ställ upp reaktionsformeln och beräkna vilken volym vätgas som bildas "
            "vid temperaturen $58\\;°\\text{C}$ och trycket $104{,}6\\;\\text{kPa}$.\n"
            "$R = 8{,}314\\;\\text{J/(mol·K)}$"
        ),
        "answer_type": "numeric",
        "correct_answer": 8.99,
        "tolerance": 0.05,
        "unit": "dm³",
        "solution": (
            "$\\text{Mg} + 2\\text{H}^+ \\to \\text{Mg}^{2+} + \\text{H}_2$\n"
            "$n(\\text{Mg}) = 8{,}3 / 24{,}3 \\approx 0{,}3416\\;\\text{mol}$\n"
            "$n(\\text{H}_2) = n(\\text{Mg}) = 0{,}3416\\;\\text{mol}$\n"
            "$T = 58 + 273{,}15 = 331{,}15\\;\\text{K}$\n"
            "$V = \\frac{nRT}{p} = \\frac{0{,}3416 \\times 8{,}314 \\times 331{,}15}{104{,}6 \\times 10^3}$\n"
            "$V \\approx 8{,}99 \\times 10^{-3}\\;\\text{m}^3 \\approx 8{,}99\\;\\text{dm}^3$"
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
            "Koppar(II)fosfat löses i vatten till en $0{,}32\\;\\text{M}$ lösning. "
            "Skriv dissociationsformeln och bestäm koncentrationen av varje jonslag i lösningen."
        ),
        "answer_type": "text",
        "correct_answer": "[Cu2+] = 0.96 M, [PO4 3-] = 0.64 M",
        "tolerance": None,
        "unit": None,
        "solution": (
            "$\\text{Cu}_3\\text{(PO}_4\\text{)}_2 \\to 3\\text{Cu}^{2+} + 2\\text{PO}_4^{3-}$\n"
            "$[\\text{Cu}^{2+}] = 3 \\times 0{,}32 = 0{,}96\\;\\text{M}$\n"
            "$[\\text{PO}_4^{3-}] = 2 \\times 0{,}32 = 0{,}64\\;\\text{M}$"
        ),
        "choices": None,
    },

    # ── Fällningsreaktioner (2/4 tentor) ─────────────────────────────
    {
        "id": "kexf01_fallning_1",
        "exam": "kexf01",
        "topic": "fallningsreaktion",
        "topic_display": "Fällningsreaktioner",
        "points": 7,
        "exam_frequency": 0.5,
        "no_calculator": False,
        "question": (
            "$150\\;\\text{ml}$ $0{,}2\\;\\text{M}$ silvernitratlösning blandas med "
            "ett överskott av natriumkloridlösning.\n"
            "a) Skriv reaktionsformeln och identifiera fällningen.\n"
            "b) Beräkna massan av fällningen."
        ),
        "answer_type": "numeric",
        "correct_answer": 4.30,
        "tolerance": 0.03,
        "unit": "g",
        "solution": (
            "$\\text{AgNO}_3 + \\text{NaCl} \\to \\text{AgCl}\\downarrow + \\text{NaNO}_3$\n"
            "$n(\\text{Ag}^+) = 0{,}150 \\times 0{,}2 = 0{,}030\\;\\text{mol}$\n"
            "$n(\\text{AgCl}) = 0{,}030\\;\\text{mol}$ ($\\text{NaCl}$ i överskott)\n"
            "$m(\\text{AgCl}) = 0{,}030 \\times 143{,}3 \\approx 4{,}30\\;\\text{g}$"
        ),
        "choices": None,
    },

    # ── Titrering (2/4 tentor) ───────────────────────────────────────
    {
        "id": "kexf01_titrering_1",
        "exam": "kexf01",
        "topic": "titrering",
        "topic_display": "Titrering",
        "points": 5,
        "exam_frequency": 0.5,
        "no_calculator": False,
        "question": (
            "En natriumhydroxidlösning titreras med saltsyra ($0{,}12\\;\\text{mol/dm}^3$) från en byrett.\n"
            "a) Skriv reaktionsformeln för neutralisationen.\n"
            "b) Det gick åt $23{,}4\\;\\text{ml}$ av syran för att neutralisera $20{,}0\\;\\text{ml}$ "
            "av $\\text{NaOH}$-lösningen. Bestäm koncentrationen av natriumhydroxidlösningen."
        ),
        "answer_type": "numeric",
        "correct_answer": 0.1404,
        "tolerance": 0.02,
        "unit": "mol/dm³",
        "solution": (
            "$\\text{HCl} + \\text{NaOH} \\to \\text{NaCl} + \\text{H}_2\\text{O}$ ($1{:}1$)\n"
            "$n(\\text{HCl}) = 0{,}0234 \\times 0{,}12 = 2{,}808 \\times 10^{-3}\\;\\text{mol}$\n"
            "$n(\\text{NaOH}) = n(\\text{HCl}) = 2{,}808 \\times 10^{-3}\\;\\text{mol}$\n"
            "$c(\\text{NaOH}) = 2{,}808 \\times 10^{-3} / 0{,}0200 = 0{,}1404\\;\\text{mol/dm}^3$"
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
            "Bariumklorid ($\\text{BaCl}_2$) tillsätts. Om sulfatjoner finns bildas "
            "en vit fällning av bariumsulfat: $\\text{Ba}^{2+} + \\text{SO}_4^{2-} \\to \\text{BaSO}_4\\downarrow$"
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
            "Silvernitrat ($\\text{AgNO}_3$) tillsätts. Om kloridjoner finns bildas "
            "en vit fällning av silverklorid: $\\text{Ag}^+ + \\text{Cl}^- \\to \\text{AgCl}\\downarrow$"
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
            "När man löser upp $5{,}3\\;\\text{g}$ aluminium i $200\\;\\text{g}$ utspädd syra "
            "(med exakt samma egenskaper som vatten) ökar temperaturen "
            "från $18\\;°\\text{C}$ till $41\\;°\\text{C}$. Hur mycket energi utvecklas per mol "
            "aluminium? ($c = 4{,}18\\;\\text{kJ/(kg·K)}$)"
        ),
        "answer_type": "numeric",
        "correct_answer": 97.8,
        "tolerance": 0.05,
        "unit": "kJ/mol",
        "solution": (
            "$Q = mc\\Delta T = 0{,}200 \\times 4{,}18 \\times (41 - 18) = 0{,}200 \\times 4{,}18 \\times 23 = 19{,}228\\;\\text{kJ}$\n"
            "$n(\\text{Al}) = 5{,}3 / 27{,}0 \\approx 0{,}1963\\;\\text{mol}$\n"
            "$Q$ per mol $= 19{,}228 / 0{,}1963 \\approx 97{,}9\\;\\text{kJ/mol}$"
        ),
        "choices": None,
    },
]
