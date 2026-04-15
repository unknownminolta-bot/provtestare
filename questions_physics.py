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
            "En laser med våglängd $\\lambda = 633\\;\\text{nm}$ träffar ett diffraktionsgitter "
            "med $500$ spalter per mm. Bestäm diffraktionsvinkeln $\\theta$ för andra ordningens "
            "($m = 2$) maximum."
        ),
        "answer_type": "numeric",
        "correct_answer": 39.3,
        "tolerance": 0.02,
        "unit": "°",
        "solution": (
            "Spaltavstånd $d = 1/(500\\;\\text{mm}^{-1}) = 2{,}00 \\times 10^{-6}\\;\\text{m}$.\n"
            "Gitterekvationen: $d \\sin \\theta = m\\lambda$ $\\Rightarrow$ $\\sin \\theta = m\\lambda / d = (2)(633 \\times 10^{-9}) / (2{,}00 \\times 10^{-6}) = 0{,}633$.\n"
            "Alltså $\\theta = \\arcsin(0{,}633) \\approx 39{,}3°$."
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
            "Ljus träffar ett gitter med spaltavstånd $d = 2{,}50\\;\\mu\\text{m}$. "
            "Första ordningens ($m = 1$) maximum uppträder vid $\\theta = 15{,}0°$. Bestäm våglängden $\\lambda$."
        ),
        "answer_type": "numeric",
        "correct_answer": 647.0,
        "tolerance": 0.05,
        "unit": "nm",
        "solution": (
            "$d \\sin \\theta = m\\lambda$ med $m = 1$ ger $\\lambda = d \\sin \\theta$.\n"
            "$\\lambda = (2{,}50 \\times 10^{-6}\\;\\text{m}) \\sin(15{,}0°) \\approx 6{,}47 \\times 10^{-7}\\;\\text{m} \\approx 647\\;\\text{nm}$."
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
            "Ett gitter har $400$ spalter/mm. För $\\lambda = 550\\;\\text{nm}$, vad är den högsta heltalsordningen $m$ "
            "för vilken diffraktionsmaxima existerar (på vardera sida om centralmaximum)?"
        ),
        "answer_type": "numeric",
        "correct_answer": 4.0,
        "tolerance": 0.0,
        "unit": "",
        "solution": (
            "$d = 1/(400\\;\\text{mm}^{-1}) = 2{,}50 \\times 10^{-6}\\;\\text{m} = 2500\\;\\text{nm}$.\n"
            "Ordningar kräver $|\\sin \\theta| \\leq 1$ $\\Rightarrow$ $m \\leq d/\\lambda = 2500/550 \\approx 4{,}54$, så den högsta heltalsordningen är $m = 4$."
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
            "Thorium-228 genomgår alfasönderfall. "
            "Skriv den fullständiga sönderfallsreaktionen och identifiera dotterkärnan."
        ),
        "answer_type": "text",
        "correct_answer": "Ra-224",
        "tolerance": None,
        "unit": None,
        "solution": (
            "$\\alpha$-sönderfall minskar $Z$ med $2$ och $A$ med $4$: ${}^{228}_{\\;90}\\text{Th} \\to {}^{224}_{\\;88}\\text{Ra} + {}^{4}_{2}\\text{He}$.\n"
            "Dotterkärnan är radium-224 (${}^{224}_{\\;88}\\text{Ra}$), ofta skrivet Ra-224."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_nuclear_2",
        "exam": "fyxf04",
        "topic": "nuclear_decay",
        "topic_display": "Kärnfysik – sönderfall",
        "points": 3,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Polonium-210 genomgår alfasönderfall. "
            "Skriv sönderfallsreaktionen och bestäm den frigjorda energin $Q$ i MeV.\n"
            "Atommassor: Po-210: $209{,}9829\\;\\text{u}$, Pb-206: $205{,}9745\\;\\text{u}$, He-4: $4{,}0026\\;\\text{u}$.\n"
            "($1\\;\\text{u} \\approx 931{,}5\\;\\text{MeV}/c^2$)"
        ),
        "answer_type": "numeric",
        "correct_answer": 5.40,
        "tolerance": 0.02,
        "unit": "MeV",
        "solution": (
            "$\\Delta m = m(\\text{Po}) - m(\\text{Pb}) - m(\\text{He}) = 209{,}9829 - 205{,}9745 - 4{,}0026 = 0{,}0058\\;\\text{u}$.\n"
            "$Q = \\Delta m \\, c^2 \\approx 0{,}0058 \\times 931{,}5\\;\\text{MeV} \\approx 5{,}40\\;\\text{MeV}$."
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
            "Kol-14 genomgår $\\beta^-$-sönderfall.\n"
            "a) Identifiera dotterkärnan.\n"
            "b) Bestäm den frigjorda energin $Q$ i MeV.\n"
            "Atommassor: C-14: $14{,}003242\\;\\text{u}$, N-14: $14{,}003074\\;\\text{u}$.\n"
            "($1\\;\\text{u} \\approx 931{,}5\\;\\text{MeV}/c^2$)"
        ),
        "answer_type": "numeric",
        "correct_answer": 0.156,
        "tolerance": 0.03,
        "unit": "MeV",
        "solution": (
            "$\\Delta m = 14{,}003242 - 14{,}003074 = 0{,}000168\\;\\text{u}$.\n"
            "$Q \\approx 0{,}000168 \\times 931{,}5\\;\\text{MeV} \\approx 0{,}156\\;\\text{MeV}$."
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
            "Ett prov har initial aktivitet $A_0 = 60\\;\\text{kBq}$. Efter $t = 11\\;\\text{h}$ är aktiviteten $A = 17\\;\\text{kBq}$. "
            "Bestäm halveringstiden."
        ),
        "answer_type": "numeric",
        "correct_answer": 6.04,
        "tolerance": 0.03,
        "unit": "h",
        "solution": (
            "$A/A_0 = e^{-\\lambda t}$ $\\Rightarrow$ $\\lambda = (1/t) \\ln(A_0/A) = (1/11\\;\\text{h}) \\ln(60/17) \\approx 0{,}1148\\;\\text{h}^{-1}$.\n"
            "$t_{1/2} = \\ln 2 / \\lambda \\approx 0{,}693/0{,}1148\\;\\text{h} \\approx 6{,}04\\;\\text{h}$."
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
            "Jod-131 har halveringstid $t_{1/2} = 8{,}02$ dagar. Hur lång tid tar det innan aktiviteten sjunkit till "
            "$25\\;\\%$ av sitt ursprungliga värde?"
        ),
        "answer_type": "numeric",
        "correct_answer": 16.04,
        "tolerance": 0.02,
        "unit": "dagar",
        "solution": (
            "$25\\;\\% = 1/4 = (1/2)^2$, alltså två halveringstider: $t = 2 \\, t_{1/2} = 2(8{,}02\\;\\text{dagar}) = 16{,}04$ dagar."
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
            "En radioaktiv källas aktivitet minskar till $37\\;\\%$ av sitt ursprungsvärde på $60$ dagar. "
            "Bestäm halveringstiden."
        ),
        "answer_type": "numeric",
        "correct_answer": 41.8,
        "tolerance": 0.03,
        "unit": "dagar",
        "solution": (
            "$0{,}37 = e^{-\\lambda \\cdot 60\\;\\text{d}}$ $\\Rightarrow$ $\\lambda = \\ln(1/0{,}37)/60\\;\\text{d} \\approx 0{,}01657\\;\\text{d}^{-1}$.\n"
            "$t_{1/2} = \\ln 2/\\lambda \\approx 0{,}693/0{,}01657\\;\\text{d} \\approx 41{,}8$ dagar."
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
            "Ett glödande kol har temperaturen $T = 750\\;°\\text{C}$. Bestäm toppvåglängden $\\lambda_{\\text{max}}$. "
            "($b = 2{,}898 \\times 10^{-3}\\;\\text{m}\\cdot\\text{K}$)"
        ),
        "answer_type": "numeric",
        "correct_answer": 2.83,
        "tolerance": 0.02,
        "unit": "μm",
        "solution": (
            "$T(\\text{K}) = 750 + 273{,}15 \\approx 1023\\;\\text{K}$.\n"
            "$\\lambda_{\\text{max}} = b/T \\approx 2{,}898 \\times 10^{-3} / 1023\\;\\text{m} \\approx 2{,}83 \\times 10^{-6}\\;\\text{m} \\approx 2{,}83\\;\\mu\\text{m}$."
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
            "En metallsfär utstrålar totaleffekten $P = 32\\;\\text{W}$ från ytan $A = 0{,}020\\;\\text{m}^2$. "
            "Bestäm yttemperaturen $T$. ($\\sigma = 5{,}67 \\times 10^{-8}\\;\\text{W}/(\\text{m}^2 \\cdot \\text{K}^4)$)"
        ),
        "answer_type": "numeric",
        "correct_answer": 410.0,
        "tolerance": 0.05,
        "unit": "K",
        "solution": (
            "$T^4 = P/(\\sigma A) = 32 / (5{,}67 \\times 10^{-8} \\times 0{,}020) \\approx 2{,}82 \\times 10^{10}\\;\\text{K}^4$.\n"
            "$T \\approx (2{,}82 \\times 10^{10})^{1/4}\\;\\text{K} \\approx 410\\;\\text{K}$."
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
            "En $40\\;\\text{W}$ halogenlampa har en glödtråd vid $T = 3000\\;\\text{K}$ med emissivitet $\\varepsilon = 1{,}0$. "
            "Bestäm glödtrådens yta $A$. ($\\sigma = 5{,}67 \\times 10^{-8}\\;\\text{W}/(\\text{m}^2 \\cdot \\text{K}^4)$)"
        ),
        "answer_type": "numeric",
        "correct_answer": 8.71e-6,
        "tolerance": 0.03,
        "unit": "m²",
        "solution": (
            "$A = \\frac{P}{\\sigma T^4} = \\frac{40}{5{,}67 \\times 10^{-8} \\times 3000^4} \\approx \\frac{40}{4{,}59 \\times 10^{6}}\\;\\text{m}^2 \\approx 8{,}71 \\times 10^{-6}\\;\\text{m}^2$ "
            "($\\approx 0{,}087\\;\\text{cm}^2$)."
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
            "Koppars utträdesarbete är $W = 4{,}7\\;\\text{eV}$. Vad är gränsfrekvensen $f_0$ "
            "(Plancks konstant $h = 6{,}626 \\times 10^{-34}\\;\\text{J}\\cdot\\text{s}$, $e = 1{,}60 \\times 10^{-19}\\;\\text{C}$)?"
        ),
        "answer_type": "numeric",
        "correct_answer": 1.14e15,
        "tolerance": 0.03,
        "unit": "Hz",
        "solution": (
            "$W = h f_0$ med $W$ i joule: $W = 4{,}7\\;\\text{eV} \\times 1{,}60 \\times 10^{-19}\\;\\text{J/eV}$.\n"
            "$f_0 = W/h \\approx 1{,}14 \\times 10^{15}\\;\\text{Hz}$."
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
            "Ljus med $\\lambda = 434\\;\\text{nm}$ träffar en metall. De emitterade elektronernas maximala hastighet är "
            "$v = 4{,}2 \\times 10^{5}\\;\\text{m/s}$. Bestäm utträdesarbetet $W$ i eV ($m_e = 9{,}11 \\times 10^{-31}\\;\\text{kg}$, "
            "$h = 6{,}626 \\times 10^{-34}\\;\\text{J}\\cdot\\text{s}$, $c = 3{,}00 \\times 10^{8}\\;\\text{m/s}$)."
        ),
        "answer_type": "numeric",
        "correct_answer": 2.36,
        "tolerance": 0.03,
        "unit": "eV",
        "solution": (
            "$E_{k,\\text{max}} = \\frac{1}{2} m_e v^2 \\approx 8{,}04 \\times 10^{-20}\\;\\text{J}$.\n"
            "$E_{\\text{photon}} = hc/\\lambda \\approx 4{,}58 \\times 10^{-19}\\;\\text{J}$.\n"
            "$W = E_{\\text{photon}} - E_{k,\\text{max}} \\approx 3{,}77 \\times 10^{-19}\\;\\text{J} \\approx 2{,}36\\;\\text{eV}$."
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
            "En elektron har rörelsemängd $p = 3{,}0 \\times 10^{-23}\\;\\text{kg}\\cdot\\text{m/s}$. "
            "Bestäm dess de Broglie-våglängd. ($h = 6{,}626 \\times 10^{-34}\\;\\text{J}\\cdot\\text{s}$)"
        ),
        "answer_type": "numeric",
        "correct_answer": 2.21e-11,
        "tolerance": 0.03,
        "unit": "m",
        "solution": (
            "$\\lambda = h/p = 6{,}626 \\times 10^{-34} / 3{,}0 \\times 10^{-23}\\;\\text{m} \\approx 2{,}21 \\times 10^{-11}\\;\\text{m}$ ($\\approx 22{,}1\\;\\text{pm}$)."
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
            "En elektron accelereras genom spänningen $U = 120\\;\\text{V}$. Bestäm dess de Broglie-våglängd "
            "(icke-relativistiskt; $e = 1{,}60 \\times 10^{-19}\\;\\text{C}$, $m_e = 9{,}11 \\times 10^{-31}\\;\\text{kg}$, $h = 6{,}626 \\times 10^{-34}\\;\\text{J}\\cdot\\text{s}$)"
        ),
        "answer_type": "numeric",
        "correct_answer": 1.12e-10,
        "tolerance": 0.03,
        "unit": "m",
        "solution": (
            "$E_k = eU = 1{,}92 \\times 10^{-17}\\;\\text{J}$, $p = \\sqrt{2 m_e E_k} \\approx 5{,}91 \\times 10^{-24}\\;\\text{kg}\\cdot\\text{m/s}$.\n"
            "$\\lambda = h/p \\approx 1{,}12 \\times 10^{-10}\\;\\text{m}$ ($\\approx 112\\;\\text{pm}$)."
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
            "En väteatom övergår från $n = 6$ till $n = 2$. Bestäm den utsända fotonens våglängd."
        ),
        "answer_type": "numeric",
        "correct_answer": 410.0,
        "tolerance": 0.05,
        "unit": "nm",
        "solution": (
            "$\\Delta E = E_6 - E_2 = -13{,}6/36 - (-13{,}6/4) \\approx 3{,}022\\;\\text{eV}$.\n"
            "$\\lambda \\approx 1240/3{,}022\\;\\text{nm} \\approx 410\\;\\text{nm}$."
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
            "Natrium emitterar $\\lambda = 589\\;\\text{nm}$ vid övergång till grundtillståndet med $E_0 = -5{,}13\\;\\text{eV}$. "
            "Bestäm den exciterade nivåns energi $E$."
        ),
        "answer_type": "numeric",
        "correct_answer": -3.025,
        "tolerance": 0.02,
        "unit": "eV",
        "solution": (
            "$E_{\\text{photon}} \\approx 1240/589\\;\\text{eV} \\approx 2{,}105\\;\\text{eV}$.\n"
            "$E - E_0 = E_{\\text{photon}}$ $\\Rightarrow$ $E = -5{,}13 + 2{,}105\\;\\text{eV} \\approx -3{,}025\\;\\text{eV}$."
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
            "Ljus går från glas ($n_1 = 1{,}6$) till vatten ($n_2 = 1{,}3$) med infallsvinkel "
            "$\\theta_1 = 18°$. Bestäm brytningsvinkeln $\\theta_2$ i vattnet."
        ),
        "answer_type": "numeric",
        "correct_answer": 22.4,
        "tolerance": 0.05,
        "unit": "°",
        "solution": (
            "Snells lag: $n_1 \\sin \\theta_1 = n_2 \\sin \\theta_2$ $\\Rightarrow$ $\\sin \\theta_2 = (1{,}6/1{,}3) \\sin 18° \\approx 0{,}380$.\n"
            "Alltså $\\theta_2 \\approx 22{,}4°$."
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
            "Ett röntgenrör drivs vid spänningen $U = 96\\;\\text{kV}$. Bestäm den kortaste våglängden $\\lambda_{\\text{min}}$ i röntgenspektrumet. "
            "($h = 6{,}626 \\times 10^{-34}\\;\\text{J}\\cdot\\text{s}$, $c = 3{,}00 \\times 10^{8}\\;\\text{m/s}$, $e = 1{,}60 \\times 10^{-19}\\;\\text{C}$)"
        ),
        "answer_type": "numeric",
        "correct_answer": 12.9,
        "tolerance": 0.03,
        "unit": "pm",
        "solution": (
            "$\\lambda_{\\text{min}} = hc/(eU) \\approx 1{,}29 \\times 10^{-11}\\;\\text{m} \\approx 12{,}9\\;\\text{pm}$."
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
            "Galaxen M51 har en recessionshastighet $v = 463\\;\\text{km/s}$. Uppskatta dess avstånd $d$. "
            "($H_0 = 70\\;\\text{km/s/Mpc}$)"
        ),
        "answer_type": "numeric",
        "correct_answer": 6.61,
        "tolerance": 0.02,
        "unit": "Mpc",
        "solution": (
            "Hubbles lag $v = H_0 d$ $\\Rightarrow$ $d = v/H_0 = 463/70\\;\\text{Mpc} \\approx 6{,}61\\;\\text{Mpc}$."
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
            "En låda med massan $2\\;\\text{kg}$ ligger på ett friktionsfritt horisontellt underlag och skjuts "
            "med en horisontell kraft på $10\\;\\text{N}$. Vad blir accelerationen?"
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "Newtons andra lag: $F = ma$ $\\Rightarrow$ $a = F/m = 10\\;\\text{N} / 2\\;\\text{kg} = 5\\;\\text{m/s}^2$. Alternativ B."
        ),
        "choices": [
            "A) $2\\;\\text{m/s}^2$",
            "B) $5\\;\\text{m/s}^2$",
            "C) $10\\;\\text{m/s}^2$",
            "D) $20\\;\\text{m/s}^2$",
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
            "En boll kastas rakt uppåt med begynnelsehastigheten $20\\;\\text{m/s}$. Hur högt når den? "
            "Använd $g = 10\\;\\text{m/s}^2$."
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "I toppen är $v = 0$. $v^2 = v_0^2 - 2gh$ $\\Rightarrow$ $h = v_0^2/(2g) = (20^2)/(2 \\cdot 10) = 400/20 = 20\\;\\text{m}$. Alternativ B."
        ),
        "choices": [
            "A) $10\\;\\text{m}$",
            "B) $20\\;\\text{m}$",
            "C) $40\\;\\text{m}$",
            "D) $200\\;\\text{m}$",
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
            "En kula med massan $3\\;\\text{kg}$ rör sig med $4\\;\\text{m/s}$ och kolliderar rakt med en stillastående kula "
            "på $1\\;\\text{kg}$ på ett friktionsfritt underlag. Efter kollisionen rör sig $3\\;\\text{kg}$-kulan med $2\\;\\text{m/s}$ "
            "i samma riktning som före. Vad är $1\\;\\text{kg}$-kulans hastighet (positiv = $3\\;\\text{kg}$-kulans ursprungliga riktning)?"
        ),
        "answer_type": "numeric",
        "correct_answer": 6.0,
        "tolerance": 0.0,
        "unit": "m/s",
        "solution": (
            "Rörelsemängdens bevarande: $m_1 v_{1,i} = m_1 v_{1,f} + m_2 v_{2,f}$.\n"
            "$3 \\cdot 4 = 3 \\cdot 2 + 1 \\cdot v$ $\\Rightarrow$ $12 = 6 + v$ $\\Rightarrow$ $v = 6\\;\\text{m/s}$."
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
            "En fjäder med fjäderkonstant $k = 200\\;\\text{N/m}$ trycks ihop $x = 0{,}1\\;\\text{m}$ från jämviktsläget. "
            "Hur stor elastisk potentiell energi lagras i fjädern?"
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "$U = \\frac{1}{2} k x^2 = \\frac{1}{2} (200)(0{,}1)^2 = 100 \\cdot 0{,}01 = 1\\;\\text{J}$. Alternativ B."
        ),
        "choices": [
            "A) $0{,}5\\;\\text{J}$",
            "B) $1\\;\\text{J}$",
            "C) $2\\;\\text{J}$",
            "D) $10\\;\\text{J}$",
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
            "En person med massan $50\\;\\text{kg}$ står på en sviktbräda $10\\;\\text{m}$ ovanför vattenytan (använd $g = 10\\;\\text{m/s}^2$). "
            "Om den mekaniska energin bevaras, vad är personens hastighet precis innan denne träffar vattnet?"
        ),
        "answer_type": "numeric",
        "correct_answer": 14.142135623730951,
        "tolerance": 0.02,
        "unit": "m/s",
        "solution": (
            "$\\frac{1}{2}mv^2 = mgh$ $\\Rightarrow$ $v = \\sqrt{2gh} = \\sqrt{2 \\cdot 10 \\cdot 10} = \\sqrt{200} = 10\\sqrt{2}\\;\\text{m/s} \\approx 14{,}1\\;\\text{m/s}$."
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
            "Två krafter, $3\\;\\text{N}$ och $4\\;\\text{N}$, verkar vinkelrätt mot varandra på ett föremål. "
            "Hur stor är den resulterande kraftens belopp?"
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "Vinkelräta vektorer: $R = \\sqrt{3^2 + 4^2} = \\sqrt{9+16} = \\sqrt{25} = 5\\;\\text{N}$ (3-4-5-triangel). Alternativ B."
        ),
        "choices": [
            "A) $1\\;\\text{N}$",
            "B) $5\\;\\text{N}$",
            "C) $7\\;\\text{N}$",
            "D) $12\\;\\text{N}$",
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
            "En homogen horisontell balk med längden $4\\;\\text{m}$ och massan $20\\;\\text{kg}$ vilar på stöd vid båda ändar. "
            "En punktmassa på $40\\;\\text{kg}$ placeras på balken $1\\;\\text{m}$ från det vänstra stödet. Använd $g = 10\\;\\text{m/s}^2$. "
            "Bestäm reaktionskraften från det vänstra stödet."
        ),
        "answer_type": "numeric",
        "correct_answer": 400.0,
        "tolerance": 0.0,
        "unit": "N",
        "solution": (
            "Total tyngd $= (20+40) \\cdot 10 = 600\\;\\text{N}$.\n"
            "Momentjämvikt kring vänster stöd: $R_{\\text{höger}} \\cdot 4 = (20 \\cdot 10) \\cdot 2 + (40 \\cdot 10) \\cdot 1 = 400 + 400 = 800$ $\\Rightarrow$ "
            "$R_{\\text{höger}} = 200\\;\\text{N}$.\n"
            "Vertikal jämvikt: $R_{\\text{vänster}} = 600 - 200 = 400\\;\\text{N}$."
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
            "Två resistorer, $6\\;\\Omega$ och $3\\;\\Omega$, är parallellkopplade. Vad är den ekvivalenta resistansen?"
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "Parallellkoppling: $1/R = 1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2$ $\\Rightarrow$ $R = 2\\;\\Omega$. Alternativ B."
        ),
        "choices": [
            "A) $1\\;\\Omega$",
            "B) $2\\;\\Omega$",
            "C) $4{,}5\\;\\Omega$",
            "D) $9\\;\\Omega$",
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
            "En elektromagnetisk våg i vakuum har frekvensen $f = 5 \\times 10^{14}\\;\\text{Hz}$. Vad är dess våglängd? "
            "Använd $c = 3 \\times 10^{8}\\;\\text{m/s}$."
        ),
        "answer_type": "numeric",
        "correct_answer": 600.0,
        "tolerance": 0.0,
        "unit": "nm",
        "solution": (
            "$\\lambda = c/f = (3 \\times 10^{8})/(5 \\times 10^{14})\\;\\text{m} = (3/5) \\times 10^{-6}\\;\\text{m} = 0{,}6 \\times 10^{-6}\\;\\text{m} = 6 \\times 10^{-7}\\;\\text{m} = 600\\;\\text{nm}$."
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
            "En ljudvåg har frekvensen $f = 340\\;\\text{Hz}$ och hastigheten $v = 340\\;\\text{m/s}$. Vad är våglängden?"
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "$\\lambda = v/f = 340/340\\;\\text{m} = 1{,}0\\;\\text{m}$. Alternativ B."
        ),
        "choices": [
            "A) $0{,}5\\;\\text{m}$",
            "B) $1{,}0\\;\\text{m}$",
            "C) $2{,}0\\;\\text{m}$",
            "D) $340\\;\\text{m}$",
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
            "En ljudvåg har frekvensen $f = 680\\;\\text{Hz}$ och utbreder sig med hastigheten $v = 340\\;\\text{m/s}$. "
            "Bestäm våglängden."
        ),
        "answer_type": "numeric",
        "correct_answer": 0.5,
        "tolerance": 0.0,
        "unit": "m",
        "solution": (
            "$\\lambda = v/f = 340/680\\;\\text{m} = 0{,}5\\;\\text{m}$.\n"
            "Konstruktiv interferens: $\\Delta L = n\\lambda$ med $n = 0, 1, 2, \\ldots$"
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
            "$m = 200\\;\\text{g}$ vatten värms från $20\\;°\\text{C}$ till $70\\;°\\text{C}$. Hur mycket värme krävs? "
            "Använd $c = 4200\\;\\text{J/(kg}\\cdot\\text{K)}$."
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "C",
        "tolerance": None,
        "unit": None,
        "solution": (
            "$Q = mc\\Delta T = 0{,}200\\;\\text{kg} \\cdot 4200\\;\\text{J/(kg}\\cdot\\text{K)} \\cdot (70-20)\\;\\text{K} = 0{,}2 \\cdot 4200 \\cdot 50\\;\\text{J} = 42000\\;\\text{J}$. Alternativ C."
        ),
        "choices": [
            "A) $4200\\;\\text{J}$",
            "B) $8400\\;\\text{J}$",
            "C) $42000\\;\\text{J}$",
            "D) $84000\\;\\text{J}$",
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
            "En foton har energin $E = 2\\;\\text{eV}$. Vad är dess våglängd i nm?"
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "$\\lambda \\approx 1240/2\\;\\text{nm} = 620\\;\\text{nm}$. Alternativ B."
        ),
        "choices": [
            "A) $310\\;\\text{nm}$",
            "B) $620\\;\\text{nm}$",
            "C) $1240\\;\\text{nm}$",
            "D) $2480\\;\\text{nm}$",
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
            "Ett rymdskepp rör sig med $v = 0{,}8c$ relativt jorden. En klocka ombord mäter $\\Delta t_0 = 10\\;\\text{s}$ "
            "mellan två tick. Vilket tidsintervall $\\Delta t$ mäter en jordobservatör för samma process?"
        ),
        "answer_type": "numeric",
        "correct_answer": 16.666666666666668,
        "tolerance": 0.001,
        "unit": "s",
        "solution": (
            "Tidsdilatation: $\\Delta t = \\gamma \\Delta t_0$ med $\\gamma = 1/\\sqrt{1 - v^2/c^2}$.\n"
            "$v = 0{,}8c$ $\\Rightarrow$ $v^2/c^2 = 0{,}64$ $\\Rightarrow$ $\\sqrt{1 - 0{,}64} = \\sqrt{0{,}36} = 0{,}6$ $\\Rightarrow$ $\\gamma = 1/0{,}6 = 5/3$.\n"
            "$\\Delta t = (5/3) \\cdot 10\\;\\text{s} = 50/3\\;\\text{s} \\approx 16{,}7\\;\\text{s}$."
        ),
        "choices": None,
    },
]
