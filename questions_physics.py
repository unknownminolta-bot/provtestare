"""Fysikfrågor för tentamen FYXF04 och Fysik 1+2 (Mat-Fys-stil)."""

FYXF04_QUESTIONS = [
    {
        "id": "fyxf04_grating_1",
        "exam": "fyxf04",
        "topic": "diffraction_grating",
        "topic_display": "Diffraktionsgitter",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "En laser med våglängd λ = 633 nm träffar ett diffraktionsgitter "
            "med 500 spalter per mm. Bestäm diffraktionsvinkeln θ för andra ordningens "
            "(m = 2) maximum."
        ),
        "answer_type": "numeric",
        "correct_answer": 39.3,
        "tolerance": 0.02,
        "unit": "°",
        "solution": (
            "Spaltavstånd d = 1 / (500 mm⁻¹) = 2.00 × 10⁻⁶ m.\n"
            "Gitterekvationen: d sin θ = mλ ⇒ sin θ = mλ / d = (2)(633×10⁻⁹) / (2.00×10⁻⁶) = 0.633.\n"
            "Alltså θ = arcsin(0.633) ≈ 39.3°."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_grating_2",
        "exam": "fyxf04",
        "topic": "diffraction_grating",
        "topic_display": "Diffraktionsgitter",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Ljus träffar ett gitter med spaltavstånd d = 2.50 μm. "
            "Första ordningens (m = 1) maximum uppträder vid θ = 15.0°. Bestäm våglängden λ."
        ),
        "answer_type": "numeric",
        "correct_answer": 647.0,
        "tolerance": 0.02,
        "unit": "nm",
        "solution": (
            "d sin θ = mλ med m = 1 ger λ = d sin θ.\n"
            "λ = (2.50×10⁻⁶ m) sin(15.0°) ≈ 6.47×10⁻⁷ m ≈ 647 nm."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_grating_3",
        "exam": "fyxf04",
        "topic": "diffraction_grating",
        "topic_display": "Diffraktionsgitter",
        "points": 3,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Ett gitter har 400 spalter/mm. För λ = 550 nm, vad är den högsta heltalsordningen m "
            "för vilken diffraktionsmaxima existerar (på vardera sida om centralmaximum)?"
        ),
        "answer_type": "numeric",
        "correct_answer": 4.0,
        "tolerance": 0.0,
        "unit": "",
        "solution": (
            "d = 1/(400 mm⁻¹) = 2.50×10⁻⁶ m = 2500 nm.\n"
            "Ordningar kräver |sin θ| ≤ 1 ⇒ m ≤ d/λ = 2500/550 ≈ 4.54, så den högsta heltalsordningen är m = 4."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_nuclear_1",
        "exam": "fyxf04",
        "topic": "nuclear_decay",
        "topic_display": "Kärnfysik – sönderfall",
        "points": 1,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Thorium-228 (²²⁸Th) genomgår alfa (α)-sönderfall. Skriv symbolen för dotterkärnan "
            "(t.ex. ²²⁶Ra eller Ra-226)."
        ),
        "answer_type": "text",
        "correct_answer": "Ra-224",
        "tolerance": None,
        "unit": None,
        "solution": (
            "α-sönderfall minskar Z med 2 och A med 4: ²²⁸Th → ²²⁴Ra + ⁴He.\n"
            "Dotterkärnan är radium-224 (²²⁴Ra), ofta skrivet Ra-224."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_nuclear_2",
        "exam": "fyxf04",
        "topic": "nuclear_decay",
        "topic_display": "Kärnfysik – sönderfall",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "I α-sönderfallet Po-210 (massa 209.9829 u) → Pb-206 (205.9745 u) + He-4 (4.0026 u), "
            "bestäm den frigjorda energin Q i MeV. Använd 1 u ≈ 931.5 MeV/c²."
        ),
        "answer_type": "numeric",
        "correct_answer": 5.40,
        "tolerance": 0.02,
        "unit": "MeV",
        "solution": (
            "Δm = m(Po) − m(Pb) − m(He) = 209.9829 − 205.9745 − 4.0026 = 0.0058 u.\n"
            "Q = Δm c² ≈ 0.0058 × 931.5 MeV ≈ 5.40 MeV."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_nuclear_3",
        "exam": "fyxf04",
        "topic": "nuclear_decay",
        "topic_display": "Kärnfysik – sönderfall",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Kol-14 genomgår β⁻-sönderfall till kväve-14. Givet m(¹⁴C) = 14.003242 u och "
            "m(¹⁴N) = 14.003074 u, bestäm den frigjorda energin i MeV (1 u ≈ 931.5 MeV/c²)."
        ),
        "answer_type": "numeric",
        "correct_answer": 0.156,
        "tolerance": 0.03,
        "unit": "MeV",
        "solution": (
            "Δm = 14.003242 − 14.003074 = 0.000168 u.\n"
            "Q ≈ 0.000168 × 931.5 MeV ≈ 0.156 MeV."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_radioactive_1",
        "exam": "fyxf04",
        "topic": "radioactive_decay",
        "topic_display": "Radioaktivt sönderfall",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Ett prov har initial aktivitet A₀ = 60 kBq. Efter t = 11 h är aktiviteten A = 17 kBq. "
            "Anta exponentiellt sönderfall A = A₀ e^(−λt) och bestäm halveringstiden t₁/₂."
        ),
        "answer_type": "numeric",
        "correct_answer": 6.04,
        "tolerance": 0.03,
        "unit": "h",
        "solution": (
            "A/A₀ = e^(−λt) ⇒ λ = (1/t) ln(A₀/A) = (1/11 h) ln(60/17) ≈ 0.1148 h⁻¹.\n"
            "t₁/₂ = ln 2 / λ ≈ 0.693/0.1148 h ≈ 6.04 h."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_radioactive_2",
        "exam": "fyxf04",
        "topic": "radioactive_decay",
        "topic_display": "Radioaktivt sönderfall",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Jod-131 har halveringstid t₁/₂ = 8.02 dagar. Hur lång tid tar det innan aktiviteten sjunkit till "
            "25 % av sitt ursprungliga värde?"
        ),
        "answer_type": "numeric",
        "correct_answer": 16.04,
        "tolerance": 0.02,
        "unit": "dagar",
        "solution": (
            "25 % = 1/4 = (1/2)², alltså två halveringstider: t = 2 t₁/₂ = 2(8.02 dagar) = 16.04 dagar."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_radioactive_3",
        "exam": "fyxf04",
        "topic": "radioactive_decay",
        "topic_display": "Radioaktivt sönderfall",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "En radioaktiv källas aktivitet minskar till 37 % av sitt ursprungsvärde på 60 dagar. "
            "Bestäm halveringstiden (anta exponentiellt sönderfall)."
        ),
        "answer_type": "numeric",
        "correct_answer": 41.8,
        "tolerance": 0.03,
        "unit": "dagar",
        "solution": (
            "0.37 = e^(−λ·60 d) ⇒ λ = ln(1/0.37)/60 d ≈ 0.01657 d⁻¹.\n"
            "t₁/₂ = ln 2/λ ≈ 0.693/0.01657 d ≈ 41.8 dagar."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_blackbody_1",
        "exam": "fyxf04",
        "topic": "blackbody_radiation",
        "topic_display": "Svartkroppsstrålning",
        "points": 2,
        "exam_frequency": 0.875,
        "no_calculator": False,
        "question": (
            "Ett glödande kol har temperaturen T = 750 °C. Använd Wiens förskjutningslag "
            "λ_max T = b med b = 2.898×10⁻³ m·K och bestäm toppvåglängden λ_max."
        ),
        "answer_type": "numeric",
        "correct_answer": 2.83,
        "tolerance": 0.02,
        "unit": "μm",
        "solution": (
            "T(K) = 750 + 273.15 ≈ 1023 K.\n"
            "λ_max = b/T ≈ 2.898×10⁻³ / 1023 m ≈ 2.83×10⁻⁶ m ≈ 2.83 μm."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_blackbody_2",
        "exam": "fyxf04",
        "topic": "blackbody_radiation",
        "topic_display": "Svartkroppsstrålning",
        "points": 2,
        "exam_frequency": 0.875,
        "no_calculator": False,
        "question": (
            "En metallsfär utstrålar totaleffekten P = 32 W från ytan A = 0.020 m². "
            "Använd Stefan–Boltzmanns lag P = σAT⁴ med σ = 5.67×10⁻⁸ W/(m²·K⁴) och bestäm T."
        ),
        "answer_type": "numeric",
        "correct_answer": 410.0,
        "tolerance": 0.03,
        "unit": "K",
        "solution": (
            "T⁴ = P/(σA) = 32 / (5.67×10⁻⁸ × 0.020) ≈ 2.82×10¹⁰ K⁴.\n"
            "T ≈ (2.82×10¹⁰)^(1/4) K ≈ 410 K."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_blackbody_3",
        "exam": "fyxf04",
        "topic": "blackbody_radiation",
        "topic_display": "Svartkroppsstrålning",
        "points": 3,
        "exam_frequency": 0.875,
        "no_calculator": False,
        "question": (
            "En 40 W halogenlampa har en glödtråd vid T = 3000 K med emissivitet ε = 1.0. "
            "Bestäm glödtrådens yta A med hjälp av P = εσAT⁴ (σ = 5.67×10⁻⁸ W/(m²·K⁴))."
        ),
        "answer_type": "numeric",
        "correct_answer": 8.71e-3,
        "tolerance": 0.03,
        "unit": "m²",
        "solution": (
            "A = P/(σT⁴) = 40 / (5.67×10⁻⁸ × 3000⁴) ≈ 40/4593 m² ≈ 8.71×10⁻³ m² "
            "(≈ 87 cm²)."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_photoelectric_1",
        "exam": "fyxf04",
        "topic": "photoelectric_effect",
        "topic_display": "Fotoelektriska effekten",
        "points": 2,
        "exam_frequency": 0.75,
        "no_calculator": False,
        "question": (
            "Koppars utträdesarbete är W = 4.7 eV. Vad är gränsfrekvensen f₀ "
            "(Plancks konstant h = 6.626×10⁻³⁴ J·s, e = 1.60×10⁻¹⁹ C)?"
        ),
        "answer_type": "numeric",
        "correct_answer": 1.14e15,
        "tolerance": 0.03,
        "unit": "Hz",
        "solution": (
            "W = h f₀ med W i joule: W = 4.7 e × 1 J/e.\n"
            "f₀ = W/h ≈ 1.14×10¹⁵ Hz."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_photoelectric_2",
        "exam": "fyxf04",
        "topic": "photoelectric_effect",
        "topic_display": "Fotoelektriska effekten",
        "points": 3,
        "exam_frequency": 0.75,
        "no_calculator": False,
        "question": (
            "Ljus med λ = 434 nm träffar en metall. De emitterade elektronernas maximala hastighet är "
            "v = 4.2×10⁵ m/s. Bestäm utträdesarbetet W i eV (m_e = 9.11×10⁻³¹ kg, "
            "h = 6.626×10⁻³⁴ J·s, c = 3.00×10⁸ m/s)."
        ),
        "answer_type": "numeric",
        "correct_answer": 2.36,
        "tolerance": 0.03,
        "unit": "eV",
        "solution": (
            "E_k,max = ½ m_e v² ≈ 8.04×10⁻²⁰ J.\n"
            "E_photon = hc/λ ≈ 4.58×10⁻¹⁹ J.\n"
            "W = E_photon − E_k,max ≈ 3.77×10⁻¹⁹ J ≈ 2.36 eV."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_debroglie_1",
        "exam": "fyxf04",
        "topic": "de_broglie",
        "topic_display": "de Broglie-våglängd",
        "points": 2,
        "exam_frequency": 0.875,
        "no_calculator": False,
        "question": (
            "En elektron har rörelsemängd p = 3.0×10⁻²³ kg·m/s. Bestäm dess de Broglie-våglängd λ = h/p "
            "(h = 6.626×10⁻³⁴ J·s)."
        ),
        "answer_type": "numeric",
        "correct_answer": 2.21e-11,
        "tolerance": 0.03,
        "unit": "m",
        "solution": (
            "λ = h/p = 6.626×10⁻³⁴ / 3.0×10⁻²³ m ≈ 2.21×10⁻¹¹ m (≈ 22.1 pm)."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_debroglie_2",
        "exam": "fyxf04",
        "topic": "de_broglie",
        "topic_display": "de Broglie-våglängd",
        "points": 3,
        "exam_frequency": 0.875,
        "no_calculator": False,
        "question": (
            "En elektron accelereras genom spänningen U = 120 V. Bestäm dess de Broglie-våglängd "
            "(icke-relativistiskt; e = 1.60×10⁻¹⁹ C, m_e = 9.11×10⁻³¹ kg, h = 6.626×10⁻³⁴ J·s)."
        ),
        "answer_type": "numeric",
        "correct_answer": 1.12e-10,
        "tolerance": 0.03,
        "unit": "m",
        "solution": (
            "E_k = eU = 1.92×10⁻¹⁷ J, p = √(2 m_e E_k) ≈ 5.91×10⁻²⁴ kg·m/s.\n"
            "λ = h/p ≈ 1.12×10⁻¹⁰ m (≈ 112 pm)."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_atomic_1",
        "exam": "fyxf04",
        "topic": "atomic_energy_levels",
        "topic_display": "Atomära energinivåer",
        "points": 2,
        "exam_frequency": 0.625,
        "no_calculator": False,
        "question": (
            "En väteatom övergår från n = 6 till n = 2. Bestäm den utsända fotonens våglängd. "
            "Använd E_n = −13.6 eV / n² och λ(nm) ≈ 1240 / ΔE(eV) där så är lämpligt."
        ),
        "answer_type": "numeric",
        "correct_answer": 410.0,
        "tolerance": 0.02,
        "unit": "nm",
        "solution": (
            "ΔE = E_6 − E_2 = −13.6/36 − (−13.6/4) ≈ 3.022 eV.\n"
            "λ ≈ 1240/3.022 nm ≈ 410 nm."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_atomic_2",
        "exam": "fyxf04",
        "topic": "atomic_energy_levels",
        "topic_display": "Atomära energinivåer",
        "points": 2,
        "exam_frequency": 0.625,
        "no_calculator": False,
        "question": (
            "Natrium emitterar λ = 589 nm vid övergång till grundtillståndet med E₀ = −5.13 eV. "
            "Bestäm den exciterade nivåns energi E (använd E_photon ≈ 1240/λ med λ i nm)."
        ),
        "answer_type": "numeric",
        "correct_answer": -3.025,
        "tolerance": 0.02,
        "unit": "eV",
        "solution": (
            "E_photon ≈ 1240/589 eV ≈ 2.105 eV.\n"
            "E − E₀ = E_photon ⇒ E = −5.13 + 2.105 eV ≈ −3.025 eV."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_refraction_1",
        "exam": "fyxf04",
        "topic": "refraction",
        "topic_display": "Brytning / Snells lag",
        "points": 1,
        "exam_frequency": 0.75,
        "no_calculator": False,
        "question": (
            "Ljus går från glas (n₁ = 1.6) till vatten (n₂ = 1.3) med infallsvinkel "
            "θ₁ = 18°. Bestäm brytningsvinkeln θ₂ i vattnet."
        ),
        "answer_type": "numeric",
        "correct_answer": 22.4,
        "tolerance": 0.02,
        "unit": "°",
        "solution": (
            "Snells lag: n₁ sin θ₁ = n₂ sin θ₂ ⇒ sin θ₂ = (1.6/1.3) sin 18° ≈ 0.380.\n"
            "Alltså θ₂ ≈ 22.4°."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_xray_1",
        "exam": "fyxf04",
        "topic": "xray_tube",
        "topic_display": "Röntgenrör",
        "points": 2,
        "exam_frequency": 0.625,
        "no_calculator": False,
        "question": (
            "Ett röntgenrör drivs vid spänningen U = 96 kV. Bestäm den kortaste våglängden λ_min "
            "(Duane–Hunt: λ_min = hc/(eU); h = 6.626×10⁻³⁴ J·s, c = 3.00×10⁸ m/s, e = 1.60×10⁻¹⁹ C)."
        ),
        "answer_type": "numeric",
        "correct_answer": 12.9,
        "tolerance": 0.03,
        "unit": "pm",
        "solution": (
            "λ_min = hc/(eU) ≈ 1.29×10⁻¹¹ m ≈ 12.9 pm."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_astro_1",
        "exam": "fyxf04",
        "topic": "astrophysics_redshift",
        "topic_display": "Astrofysik / Hubbles lag",
        "points": 2,
        "exam_frequency": 0.75,
        "no_calculator": False,
        "question": (
            "Galaxen M51 har en recessionshastighet v = 463 km/s. Använd H₀ = 70 km/s/Mpc och uppskatta dess avstånd d."
        ),
        "answer_type": "numeric",
        "correct_answer": 6.61,
        "tolerance": 0.02,
        "unit": "Mpc",
        "solution": (
            "Hubbles lag v = H₀ d ⇒ d = v/H₀ = 463/70 Mpc ≈ 6.61 Mpc."
        ),
        "choices": None,
    },
]

FYSIK12_QUESTIONS = [
    {
        "id": "fysik12_mech_mc_1",
        "exam": "fysik12",
        "topic": "mechanics",
        "topic_display": "Mekanik",
        "points": 1,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": (
            "En låda med massan 2 kg ligger på ett friktionsfritt horisontellt underlag och skjuts "
            "med en horisontell kraft på 10 N. Vad blir accelerationen?"
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "Newtons andra lag: F = ma ⇒ a = F/m = 10 N / 2 kg = 5 m/s². Alternativ B."
        ),
        "choices": [
            "A) 2 m/s²",
            "B) 5 m/s²",
            "C) 10 m/s²",
            "D) 20 m/s²",
        ],
    },
    {
        "id": "fysik12_mech_mc_2",
        "exam": "fysik12",
        "topic": "mechanics",
        "topic_display": "Mekanik",
        "points": 1,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": (
            "En boll kastas rakt uppåt med begynnelsehastigheten 20 m/s. Hur högt når den? "
            "Använd g = 10 m/s²."
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "I toppen är v = 0. v² = v₀² − 2gh ⇒ h = v₀²/(2g) = (20²)/(2·10) = 400/20 = 20 m. Alternativ B."
        ),
        "choices": [
            "A) 10 m",
            "B) 20 m",
            "C) 40 m",
            "D) 200 m",
        ],
    },
    {
        "id": "fysik12_mech_collision_1",
        "exam": "fysik12",
        "topic": "mechanics",
        "topic_display": "Mekanik",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": (
            "En kula med massan 3 kg rör sig med 4 m/s och kolliderar rakt med en stillastående kula "
            "på 1 kg på ett friktionsfritt underlag. Efter kollisionen rör sig 3 kg-kulan med 2 m/s "
            "i samma riktning som före. Vad är 1 kg-kulans hastighet (positiv = 3 kg-kulans ursprungliga riktning)?"
        ),
        "answer_type": "numeric",
        "correct_answer": 6.0,
        "tolerance": 0.0,
        "unit": "m/s",
        "solution": (
            "Rörelsemängdens bevarande: m₁v₁,i = m₁v₁,f + m₂v₂,f.\n"
            "3·4 = 3·2 + 1·v ⇒ 12 = 6 + v ⇒ v = 6 m/s."
        ),
        "choices": None,
    },
    {
        "id": "fysik12_mech_mc_3",
        "exam": "fysik12",
        "topic": "mechanics",
        "topic_display": "Mekanik",
        "points": 1,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": (
            "En fjäder med fjäderkonstant k = 200 N/m trycks ihop x = 0.1 m från jämviktsläget. "
            "Hur stor elastisk potentiell energi lagras i fjädern?"
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "U = ½ k x² = ½ (200)(0.1)² = 100 · 0.01 = 1 J. Alternativ B."
        ),
        "choices": [
            "A) 0.5 J",
            "B) 1 J",
            "C) 2 J",
            "D) 10 J",
        ],
    },
    {
        "id": "fysik12_mech_energy_1",
        "exam": "fysik12",
        "topic": "mechanics",
        "topic_display": "Mekanik",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": (
            "En person med massan 50 kg står på en sviktbräda 10 m ovanför vattenytan (använd g = 10 m/s²). "
            "Om den mekaniska energin bevaras, vad är personens hastighet precis innan denne träffar vattnet?"
        ),
        "answer_type": "numeric",
        "correct_answer": 14.142135623730951,
        "tolerance": 0.02,
        "unit": "m/s",
        "solution": (
            "½mv² = mgh ⇒ v = √(2gh) = √(2·10·10) = √200 = 10√2 m/s ≈ 14.1 m/s."
        ),
        "choices": None,
    },
    {
        "id": "fysik12_mech_mc_4",
        "exam": "fysik12",
        "topic": "mechanics",
        "topic_display": "Mekanik",
        "points": 1,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": (
            "Två krafter, 3 N och 4 N, verkar vinkelrätt mot varandra på ett föremål. "
            "Hur stor är den resulterande kraftens belopp?"
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "Vinkelräta vektorer: R = √(3² + 4²) = √(9+16) = √25 = 5 N (3-4-5-triangel). Alternativ B."
        ),
        "choices": [
            "A) 1 N",
            "B) 5 N",
            "C) 7 N",
            "D) 12 N",
        ],
    },
    {
        "id": "fysik12_mech_statics_1",
        "exam": "fysik12",
        "topic": "mechanics",
        "topic_display": "Mekanik",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": (
            "En homogen horisontell balk med längden 4 m och massan 20 kg vilar på stöd vid båda ändar. "
            "En punktmassa på 40 kg placeras på balken 1 m från det vänstra stödet. Använd g = 10 m/s². "
            "Bestäm reaktionskraften från det vänstra stödet."
        ),
        "answer_type": "numeric",
        "correct_answer": 400.0,
        "tolerance": 0.0,
        "unit": "N",
        "solution": (
            "Total tyngd = (20+40)·10 = 600 N.\n"
            "Momentjämvikt kring vänster stöd: R_höger·4 = (20·10)·2 + (40·10)·1 = 400 + 400 = 800 ⇒ "
            "R_höger = 200 N.\n"
            "Vertikal jämvikt: R_vänster = 600 − 200 = 400 N."
        ),
        "choices": None,
    },
    {
        "id": "fysik12_em_mc_1",
        "exam": "fysik12",
        "topic": "electromagnetism",
        "topic_display": "Elektromagnetism",
        "points": 1,
        "exam_frequency": 0.7,
        "no_calculator": True,
        "question": (
            "Två resistorer, 6 Ω och 3 Ω, är parallellkopplade. Vad är den ekvivalenta resistansen?"
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "Parallellkoppling: 1/R = 1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2 ⇒ R = 2 Ω. Alternativ B."
        ),
        "choices": [
            "A) 1 Ω",
            "B) 2 Ω",
            "C) 4.5 Ω",
            "D) 9 Ω",
        ],
    },
    {
        "id": "fysik12_em_wave_1",
        "exam": "fysik12",
        "topic": "electromagnetism",
        "topic_display": "Elektromagnetism",
        "points": 2,
        "exam_frequency": 0.7,
        "no_calculator": True,
        "question": (
            "En elektromagnetisk våg i vakuum har frekvensen f = 5×10¹⁴ Hz. Vad är dess våglängd? "
            "Använd c = 3×10⁸ m/s."
        ),
        "answer_type": "numeric",
        "correct_answer": 600.0,
        "tolerance": 0.0,
        "unit": "nm",
        "solution": (
            "λ = c/f = (3×10⁸)/(5×10¹⁴) m = (3/5)×10⁻⁶ m = 0.6×10⁻⁶ m = 6×10⁻⁷ m = 600 nm."
        ),
        "choices": None,
    },
    {
        "id": "fysik12_waves_mc_1",
        "exam": "fysik12",
        "topic": "waves",
        "topic_display": "Vågor",
        "points": 1,
        "exam_frequency": 0.7,
        "no_calculator": True,
        "question": (
            "En ljudvåg har frekvensen f = 340 Hz och hastigheten v = 340 m/s. Vad är våglängden?"
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "λ = v/f = 340/340 m = 1.0 m. Alternativ B."
        ),
        "choices": [
            "A) 0.5 m",
            "B) 1.0 m",
            "C) 2.0 m",
            "D) 340 m",
        ],
    },
    {
        "id": "fysik12_waves_interference_1",
        "exam": "fysik12",
        "topic": "waves",
        "topic_display": "Vågor",
        "points": 2,
        "exam_frequency": 0.7,
        "no_calculator": True,
        "question": (
            "Två högtalare med 2 m avstånd sänder ljud i fas vid f = 680 Hz. Ljudets hastighet är v = 340 m/s. "
            "Vad är våglängden? (För konstruktiv interferens vid en avlägsen punkt i den vanliga "
            "tvåkälleuppställningen gäller att gångskillnaden är nλ för heltal n — ange λ.)"
        ),
        "answer_type": "numeric",
        "correct_answer": 0.5,
        "tolerance": 0.0,
        "unit": "m",
        "solution": (
            "λ = v/f = 340/680 m = 0.5 m.\n"
            "Konstruktiv interferens: ΔL = nλ med n = 0, 1, 2, …"
        ),
        "choices": None,
    },
    {
        "id": "fysik12_thermo_mc_1",
        "exam": "fysik12",
        "topic": "thermodynamics",
        "topic_display": "Termodynamik",
        "points": 1,
        "exam_frequency": 0.5,
        "no_calculator": True,
        "question": (
            "m = 200 g vatten värms från 20 °C till 70 °C. Hur mycket värme krävs? "
            "Använd c = 4200 J/(kg·K)."
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "C",
        "tolerance": None,
        "unit": None,
        "solution": (
            "Q = m c ΔT = 0.200 kg · 4200 J/(kg·K) · (70−20) K = 0.2·4200·50 J = 42000 J. Alternativ C."
        ),
        "choices": [
            "A) 4200 J",
            "B) 8400 J",
            "C) 42000 J",
            "D) 84000 J",
        ],
    },
    {
        "id": "fysik12_quantum_mc_1",
        "exam": "fysik12",
        "topic": "quantum_relativity",
        "topic_display": "Kvant / Relativitet",
        "points": 1,
        "exam_frequency": 0.5,
        "no_calculator": True,
        "question": (
            "En foton har energin E = 2 eV. Vad är dess våglängd i nm? Använd genvägen E(eV) ≈ 1240/λ(nm)."
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "λ ≈ 1240/2 nm = 620 nm. Alternativ B."
        ),
        "choices": [
            "A) 310 nm",
            "B) 620 nm",
            "C) 1240 nm",
            "D) 2480 nm",
        ],
    },
    {
        "id": "fysik12_relativity_1",
        "exam": "fysik12",
        "topic": "quantum_relativity",
        "topic_display": "Kvant / Relativitet",
        "points": 2,
        "exam_frequency": 0.5,
        "no_calculator": True,
        "question": (
            "Ett rymdskepp rör sig med v = 0.8c relativt jorden. En klocka ombord mäter Δt₀ = 10 s "
            "mellan två tick. Vilket tidsintervall Δt mäter en jordobservatör för samma process?"
        ),
        "answer_type": "numeric",
        "correct_answer": 16.666666666666668,
        "tolerance": 0.001,
        "unit": "s",
        "solution": (
            "Tidsdilatation: Δt = γ Δt₀ med γ = 1/√(1 − v²/c²).\n"
            "v = 0.8c ⇒ v²/c² = 0.64 ⇒ √(1 − 0.64) = √0.36 = 0.6 ⇒ γ = 1/0.6 = 5/3.\n"
            "Δt = (5/3)·10 s = 50/3 s ≈ 16.7 s."
        ),
        "choices": None,
    },
]
