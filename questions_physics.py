"""Physics exam questions for FYXF04 and Fysik 1+2 (Mat-Fys style)."""

FYXF04_QUESTIONS = [
    {
        "id": "fyxf04_grating_1",
        "exam": "fyxf04",
        "topic": "diffraction_grating",
        "topic_display": "Diffraction Grating",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "A laser with wavelength λ = 633 nm is incident on a diffraction grating "
            "with 500 slits per mm. Find the diffraction angle θ for the second-order "
            "(m = 2) maximum."
        ),
        "answer_type": "numeric",
        "correct_answer": 39.3,
        "tolerance": 0.02,
        "unit": "°",
        "solution": (
            "Slit separation d = 1 / (500 mm⁻¹) = 2.00 × 10⁻⁶ m.\n"
            "Grating equation: d sin θ = mλ ⇒ sin θ = mλ / d = (2)(633×10⁻⁹) / (2.00×10⁻⁶) = 0.633.\n"
            "Thus θ = arcsin(0.633) ≈ 39.3°."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_grating_2",
        "exam": "fyxf04",
        "topic": "diffraction_grating",
        "topic_display": "Diffraction Grating",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Light is incident on a grating with slit separation d = 2.50 μm. "
            "The first-order (m = 1) maximum appears at θ = 15.0°. Find the wavelength λ."
        ),
        "answer_type": "numeric",
        "correct_answer": 647.0,
        "tolerance": 0.02,
        "unit": "nm",
        "solution": (
            "d sin θ = mλ with m = 1 gives λ = d sin θ.\n"
            "λ = (2.50×10⁻⁶ m) sin(15.0°) ≈ 6.47×10⁻⁷ m ≈ 647 nm."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_grating_3",
        "exam": "fyxf04",
        "topic": "diffraction_grating",
        "topic_display": "Diffraction Grating",
        "points": 3,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "A grating has 400 slits/mm. For λ = 550 nm, what is the maximum integer order m "
            "for which diffraction maxima exist (on either side of the central maximum)?"
        ),
        "answer_type": "numeric",
        "correct_answer": 4.0,
        "tolerance": 0.0,
        "unit": "",
        "solution": (
            "d = 1/(400 mm⁻¹) = 2.50×10⁻⁶ m = 2500 nm.\n"
            "Orders require |sin θ| ≤ 1 ⇒ m ≤ d/λ = 2500/550 ≈ 4.54, so the largest integer order is m = 4."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_nuclear_1",
        "exam": "fyxf04",
        "topic": "nuclear_decay",
        "topic_display": "Nuclear Decay",
        "points": 1,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Thorium-228 (²²⁸Th) undergoes alpha (α) decay. Write the symbol of the daughter nucleus "
            "(e.g. ²²⁶Ra or Ra-226)."
        ),
        "answer_type": "text",
        "correct_answer": "Ra-224",
        "tolerance": None,
        "unit": None,
        "solution": (
            "α decay reduces Z by 2 and A by 4: ²²⁸Th → ²²⁴Ra + ⁴He.\n"
            "The daughter is radium-224 (²²⁴Ra), often written Ra-224."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_nuclear_2",
        "exam": "fyxf04",
        "topic": "nuclear_decay",
        "topic_display": "Nuclear Decay",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "In the α decay Po-210 (mass 209.9829 u) → Pb-206 (205.9745 u) + He-4 (4.0026 u), "
            "find the energy released Q in MeV. Use 1 u ≈ 931.5 MeV/c²."
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
        "topic_display": "Nuclear Decay",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Carbon-14 undergoes β⁻ decay to nitrogen-14. Given m(¹⁴C) = 14.003242 u and "
            "m(¹⁴N) = 14.003074 u, find the released energy in MeV (1 u ≈ 931.5 MeV/c²)."
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
        "topic_display": "Radioactive Decay",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "A sample has initial activity A₀ = 60 kBq. After t = 11 h the activity is A = 17 kBq. "
            "Assuming exponential decay A = A₀ e^(−λt), find the half-life t₁/₂."
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
        "topic_display": "Radioactive Decay",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "Iodine-131 has half-life t₁/₂ = 8.02 days. How long until the activity falls to "
            "25% of its initial value?"
        ),
        "answer_type": "numeric",
        "correct_answer": 16.04,
        "tolerance": 0.02,
        "unit": "days",
        "solution": (
            "25% = 1/4 = (1/2)², so two half-lives: t = 2 t₁/₂ = 2(8.02 days) = 16.04 days."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_radioactive_3",
        "exam": "fyxf04",
        "topic": "radioactive_decay",
        "topic_display": "Radioactive Decay",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
        "question": (
            "A radioactive source’s activity decreases to 37% of its initial value in 60 days. "
            "Find the half-life (assume exponential decay)."
        ),
        "answer_type": "numeric",
        "correct_answer": 41.8,
        "tolerance": 0.03,
        "unit": "days",
        "solution": (
            "0.37 = e^(−λ·60 d) ⇒ λ = ln(1/0.37)/60 d ≈ 0.01657 d⁻¹.\n"
            "t₁/₂ = ln 2/λ ≈ 0.693/0.01657 d ≈ 41.8 days."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_blackbody_1",
        "exam": "fyxf04",
        "topic": "blackbody_radiation",
        "topic_display": "Blackbody Radiation",
        "points": 2,
        "exam_frequency": 0.875,
        "no_calculator": False,
        "question": (
            "A glowing coal has temperature T = 750 °C. Using Wien’s displacement law "
            "λ_max T = b with b = 2.898×10⁻³ m·K, find the peak wavelength λ_max."
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
        "topic_display": "Blackbody Radiation",
        "points": 2,
        "exam_frequency": 0.875,
        "no_calculator": False,
        "question": (
            "A metal sphere radiates total power P = 32 W from surface area A = 0.020 m². "
            "Using the Stefan–Boltzmann law P = σAT⁴ with σ = 5.67×10⁻⁸ W/(m²·K⁴), find T."
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
        "topic_display": "Blackbody Radiation",
        "points": 3,
        "exam_frequency": 0.875,
        "no_calculator": False,
        "question": (
            "A 40 W halogen lamp filament at T = 3000 K has emissivity ε = 1.0. "
            "Find the filament surface area A using P = εσAT⁴ (σ = 5.67×10⁻⁸ W/(m²·K⁴))."
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
        "topic_display": "Photoelectric Effect",
        "points": 2,
        "exam_frequency": 0.75,
        "no_calculator": False,
        "question": (
            "The work function of copper is W = 4.7 eV. What is the threshold frequency f₀ "
            "(Planck constant h = 6.626×10⁻³⁴ J·s, e = 1.60×10⁻¹⁹ C)?"
        ),
        "answer_type": "numeric",
        "correct_answer": 1.14e15,
        "tolerance": 0.03,
        "unit": "Hz",
        "solution": (
            "W = h f₀ with W in joules: W = 4.7 e × 1 J/e.\n"
            "f₀ = W/h ≈ 1.14×10¹⁵ Hz."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_photoelectric_2",
        "exam": "fyxf04",
        "topic": "photoelectric_effect",
        "topic_display": "Photoelectric Effect",
        "points": 3,
        "exam_frequency": 0.75,
        "no_calculator": False,
        "question": (
            "Light with λ = 434 nm strikes a metal. The maximum emitted electron speed is "
            "v = 4.2×10⁵ m/s. Find the work function W in eV (m_e = 9.11×10⁻³¹ kg, "
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
        "topic_display": "de Broglie Wavelength",
        "points": 2,
        "exam_frequency": 0.875,
        "no_calculator": False,
        "question": (
            "An electron has momentum p = 3.0×10⁻²³ kg·m/s. Find its de Broglie wavelength λ = h/p "
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
        "topic_display": "de Broglie Wavelength",
        "points": 3,
        "exam_frequency": 0.875,
        "no_calculator": False,
        "question": (
            "An electron is accelerated through U = 120 V. Find its de Broglie wavelength "
            "(non-relativistic; e = 1.60×10⁻¹⁹ C, m_e = 9.11×10⁻³¹ kg, h = 6.626×10⁻³⁴ J·s)."
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
        "topic_display": "Atomic Energy Levels",
        "points": 2,
        "exam_frequency": 0.625,
        "no_calculator": False,
        "question": (
            "A hydrogen atom transitions from n = 6 to n = 2. Find the emitted photon wavelength. "
            "Use E_n = −13.6 eV / n² and λ(nm) ≈ 1240 / ΔE(eV) where convenient."
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
        "topic_display": "Atomic Energy Levels",
        "points": 2,
        "exam_frequency": 0.625,
        "no_calculator": False,
        "question": (
            "Sodium emits λ = 589 nm when decaying to the ground state at E₀ = −5.13 eV. "
            "Find the excited level energy E (use E_photon ≈ 1240/λ with λ in nm)."
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
        "topic_display": "Refraction / Snell's Law",
        "points": 1,
        "exam_frequency": 0.75,
        "no_calculator": False,
        "question": (
            "Light travels from glass (n₁ = 1.6) to water (n₂ = 1.3) with incidence angle "
            "θ₁ = 18°. Find the refraction angle θ₂ in the water."
        ),
        "answer_type": "numeric",
        "correct_answer": 22.4,
        "tolerance": 0.02,
        "unit": "°",
        "solution": (
            "Snell: n₁ sin θ₁ = n₂ sin θ₂ ⇒ sin θ₂ = (1.6/1.3) sin 18° ≈ 0.380.\n"
            "Thus θ₂ ≈ 22.4°."
        ),
        "choices": None,
    },
    {
        "id": "fyxf04_xray_1",
        "exam": "fyxf04",
        "topic": "xray_tube",
        "topic_display": "X-ray Tube",
        "points": 2,
        "exam_frequency": 0.625,
        "no_calculator": False,
        "question": (
            "An X-ray tube operates at U = 96 kV. Find the minimum wavelength λ_min "
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
        "topic_display": "Astrophysics / Hubble's Law",
        "points": 2,
        "exam_frequency": 0.75,
        "no_calculator": False,
        "question": (
            "Galaxy M51 has recession speed v = 463 km/s. Using H₀ = 70 km/s/Mpc, estimate its distance d."
        ),
        "answer_type": "numeric",
        "correct_answer": 6.61,
        "tolerance": 0.02,
        "unit": "Mpc",
        "solution": (
            "Hubble law v = H₀ d ⇒ d = v/H₀ = 463/70 Mpc ≈ 6.61 Mpc."
        ),
        "choices": None,
    },
]

FYSIK12_QUESTIONS = [
    {
        "id": "fysik12_mech_mc_1",
        "exam": "fysik12",
        "topic": "mechanics",
        "topic_display": "Mechanics",
        "points": 1,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": (
            "A 2 kg box on a frictionless horizontal surface is pushed with a horizontal force of 10 N. "
            "What is the acceleration?"
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "Newton’s second law: F = ma ⇒ a = F/m = 10 N / 2 kg = 5 m/s². Choice B."
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
        "topic_display": "Mechanics",
        "points": 1,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": (
            "A ball is thrown vertically upward with initial speed 20 m/s. How high does it go? "
            "Use g = 10 m/s²."
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "At the top, v = 0. v² = v₀² − 2gh ⇒ h = v₀²/(2g) = (20²)/(2·10) = 400/20 = 20 m. Choice B."
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
        "topic_display": "Mechanics",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": (
            "A 3 kg ball moving at 4 m/s collides head-on with a stationary 1 kg ball on a frictionless line. "
            "After the collision, the 3 kg ball moves at 2 m/s in the same direction as before. "
            "What is the velocity of the 1 kg ball (positive = original direction of the 3 kg ball)?"
        ),
        "answer_type": "numeric",
        "correct_answer": 6.0,
        "tolerance": 0.0,
        "unit": "m/s",
        "solution": (
            "Momentum conservation: m₁v₁,i = m₁v₁,f + m₂v₂,f.\n"
            "3·4 = 3·2 + 1·v ⇒ 12 = 6 + v ⇒ v = 6 m/s."
        ),
        "choices": None,
    },
    {
        "id": "fysik12_mech_mc_3",
        "exam": "fysik12",
        "topic": "mechanics",
        "topic_display": "Mechanics",
        "points": 1,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": (
            "A spring with spring constant k = 200 N/m is compressed x = 0.1 m from equilibrium. "
            "How much elastic potential energy is stored?"
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "U = ½ k x² = ½ (200)(0.1)² = 100 · 0.01 = 1 J. Choice B."
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
        "topic_display": "Mechanics",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": (
            "A 50 kg person stands on a diving board 10 m above the water surface (use g = 10 m/s²). "
            "If mechanical energy is conserved, what is their speed just before hitting the water?"
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
        "topic_display": "Mechanics",
        "points": 1,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": (
            "Two forces, 3 N and 4 N, act perpendicularly on an object. What is the magnitude of the "
            "resultant force?"
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "Perpendicular vectors: R = √(3² + 4²) = √(9+16) = √25 = 5 N (3-4-5 triangle). Choice B."
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
        "topic_display": "Mechanics",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": (
            "A uniform horizontal beam of length 4 m and mass 20 kg rests on supports at both ends. "
            "A point mass of 40 kg sits on the beam 1 m from the left support. Take g = 10 m/s². "
            "Find the reaction force from the left support."
        ),
        "answer_type": "numeric",
        "correct_answer": 400.0,
        "tolerance": 0.0,
        "unit": "N",
        "solution": (
            "Total weight = (20+40)·10 = 600 N.\n"
            "Torque about the left support: R_right·4 = (20·10)·2 + (40·10)·1 = 400 + 400 = 800 ⇒ "
            "R_right = 200 N.\n"
            "Vertical equilibrium: R_left = 600 − 200 = 400 N."
        ),
        "choices": None,
    },
    {
        "id": "fysik12_em_mc_1",
        "exam": "fysik12",
        "topic": "electromagnetism",
        "topic_display": "Electromagnetism",
        "points": 1,
        "exam_frequency": 0.7,
        "no_calculator": True,
        "question": (
            "Two resistors, 6 Ω and 3 Ω, are connected in parallel. What is the equivalent resistance?"
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "Parallel: 1/R = 1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2 ⇒ R = 2 Ω. Choice B."
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
        "topic_display": "Electromagnetism",
        "points": 2,
        "exam_frequency": 0.7,
        "no_calculator": True,
        "question": (
            "An electromagnetic wave in vacuum has frequency f = 5×10¹⁴ Hz. What is its wavelength? "
            "Use c = 3×10⁸ m/s."
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
        "topic_display": "Waves",
        "points": 1,
        "exam_frequency": 0.7,
        "no_calculator": True,
        "question": (
            "A sound wave has frequency f = 340 Hz and speed v = 340 m/s. What is the wavelength?"
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "λ = v/f = 340/340 m = 1.0 m. Choice B."
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
        "topic_display": "Waves",
        "points": 2,
        "exam_frequency": 0.7,
        "no_calculator": True,
        "question": (
            "Two speakers 2 m apart emit sound in phase at f = 680 Hz. The sound speed is v = 340 m/s. "
            "What is the wavelength? (For constructive interference at a distant point in the "
            "usual two-source setup, path difference equals nλ for integer n — report λ.)"
        ),
        "answer_type": "numeric",
        "correct_answer": 0.5,
        "tolerance": 0.0,
        "unit": "m",
        "solution": (
            "λ = v/f = 340/680 m = 0.5 m.\n"
            "Constructive interference: ΔL = nλ with n = 0, 1, 2, …"
        ),
        "choices": None,
    },
    {
        "id": "fysik12_thermo_mc_1",
        "exam": "fysik12",
        "topic": "thermodynamics",
        "topic_display": "Thermodynamics",
        "points": 1,
        "exam_frequency": 0.5,
        "no_calculator": True,
        "question": (
            "m = 200 g of water is heated from 20 °C to 70 °C. How much heat is required? "
            "Use c = 4200 J/(kg·K)."
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "C",
        "tolerance": None,
        "unit": None,
        "solution": (
            "Q = m c ΔT = 0.200 kg · 4200 J/(kg·K) · (70−20) K = 0.2·4200·50 J = 42000 J. Choice C."
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
        "topic_display": "Quantum / Relativity",
        "points": 1,
        "exam_frequency": 0.5,
        "no_calculator": True,
        "question": (
            "A photon has energy E = 2 eV. What is its wavelength in nm? Use the shortcut E(eV) ≈ 1240/λ(nm)."
        ),
        "answer_type": "multiple_choice",
        "correct_answer": "B",
        "tolerance": None,
        "unit": None,
        "solution": (
            "λ ≈ 1240/2 nm = 620 nm. Choice B."
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
        "topic_display": "Quantum / Relativity",
        "points": 2,
        "exam_frequency": 0.5,
        "no_calculator": True,
        "question": (
            "A spaceship moves at v = 0.8c relative to Earth. A clock on the ship measures Δt₀ = 10 s "
            "between two ticks. What time interval Δt does an Earth observer measure for the same process?"
        ),
        "answer_type": "numeric",
        "correct_answer": 16.666666666666668,
        "tolerance": 0.001,
        "unit": "s",
        "solution": (
            "Time dilation: Δt = γ Δt₀ with γ = 1/√(1 − v²/c²).\n"
            "v = 0.8c ⇒ v²/c² = 0.64 ⇒ √(1 − 0.64) = √0.36 = 0.6 ⇒ γ = 1/0.6 = 5/3.\n"
            "Δt = (5/3)·10 s = 50/3 s ≈ 16.7 s."
        ),
        "choices": None,
    },
]
