"""Math questions for MAXF02 (Mat–Fys provet prep). All items are no-calculator."""

MAXF02_QUESTIONS = [
    {
        "id": "maxf02_trig_values_1",
        "exam": "maxf02",
        "topic": "exact_trig",
        "topic_display": "Exact trigonometric values",
        "points": 1,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Find the exact value of sin(840°).",
        "answer_type": "numeric",
        "correct_answer": 0.866,
        "tolerance": 0.01,
        "unit": "",
        "solution": (
            "Reduce the angle: 840° − 720° = 120°. "
            "sin(120°) = sin(180° − 60°) = sin(60°) = √3/2."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_trig_values_2",
        "exam": "maxf02",
        "topic": "exact_trig",
        "topic_display": "Exact trigonometric values",
        "points": 1,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Find the exact value of cos(4π/3).",
        "answer_type": "numeric",
        "correct_answer": -0.5,
        "tolerance": 0.01,
        "unit": "",
        "solution": (
            "4π/3 is in the third quadrant (reference angle π/3). "
            "cos(4π/3) = −cos(π/3) = −1/2."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_trig_values_3",
        "exam": "maxf02",
        "topic": "exact_trig",
        "topic_display": "Exact trigonometric values",
        "points": 1,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Find the exact value of tan(−120°).",
        "answer_type": "numeric",
        "correct_answer": 1.732,
        "tolerance": 0.01,
        "unit": "",
        "solution": (
            "tan is odd: tan(−120°) = −tan(120°). "
            "tan(120°) = tan(180° − 60°) = −tan(60°) = −√3, "
            "so tan(−120°) = √3."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_trig_eq_1",
        "exam": "maxf02",
        "topic": "trig_equations",
        "topic_display": "Trigonometric equations",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Solve sin(x) = 1/2 for 0 ≤ x ≤ 2π. Give all solutions (radians).",
        "answer_type": "text",
        "correct_answer": "π/6 and 5π/6",
        "tolerance": None,
        "unit": "",
        "solution": (
            "sin(x) = 1/2 at x = π/6 (first quadrant) and x = π − π/6 = 5π/6 "
            "(second quadrant)."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_trig_eq_2",
        "exam": "maxf02",
        "topic": "trig_equations",
        "topic_display": "Trigonometric equations",
        "points": 3,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Solve cos(2x) = 1/2 for 0 ≤ x ≤ 2π. Give all solutions (radians).",
        "answer_type": "text",
        "correct_answer": "π/6, 5π/6, 7π/6, 11π/6",
        "tolerance": None,
        "unit": "",
        "solution": (
            "Let θ = 2x, so θ ∈ [0, 4π]. cos(θ) = 1/2 at θ = π/3, 5π/3, 7π/3, 11π/3. "
            "Divide by 2: x = π/6, 5π/6, 7π/6, 11π/6."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_trig_eq_3",
        "exam": "maxf02",
        "topic": "trig_equations",
        "topic_display": "Trigonometric equations",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Solve 2sin(x) − 1 = 0 for 0° ≤ x ≤ 360°. Give all solutions.",
        "answer_type": "text",
        "correct_answer": "30° and 150°",
        "tolerance": None,
        "unit": "",
        "solution": (
            "2sin(x) = 1 ⇒ sin(x) = 1/2. In [0°, 360°], x = 30° and x = 180° − 30° = 150°."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_deriv_1",
        "exam": "maxf02",
        "topic": "derivatives",
        "topic_display": "Derivatives",
        "points": 1,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Find the derivative of f(x) = x³ + ln(x).",
        "answer_type": "text",
        "correct_answer": "3x² + 1/x",
        "tolerance": None,
        "unit": "",
        "solution": (
            "d/dx(x³) = 3x²; d/dx(ln x) = 1/x. Sum: f'(x) = 3x² + 1/x."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_deriv_2",
        "exam": "maxf02",
        "topic": "derivatives",
        "topic_display": "Derivatives",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Find f'(x) for f(x) = (2x + 1)·e^(3x).",
        "answer_type": "text",
        "correct_answer": "(6x+5)e^(3x)",
        "tolerance": None,
        "unit": "",
        "solution": (
            "Product rule: u = 2x+1, v = e^(3x); u' = 2, v' = 3e^(3x). "
            "f' = 2e^(3x) + (2x+1)·3e^(3x) = e^(3x)(2 + 6x + 3) = (6x+5)e^(3x)."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_deriv_3",
        "exam": "maxf02",
        "topic": "derivatives",
        "topic_display": "Derivatives",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Find f'(x) for f(x) = x²/(x + 2).",
        "answer_type": "text",
        "correct_answer": "x(x+4)/(x+2)²",
        "tolerance": None,
        "unit": "",
        "solution": (
            "Quotient rule: ((2x)(x+2) − x²·1)/(x+2)² = (2x²+4x−x²)/(x+2)² "
            "= (x²+4x)/(x+2)² = x(x+4)/(x+2)²."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_deriv_4",
        "exam": "maxf02",
        "topic": "derivatives",
        "topic_display": "Derivatives",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Find f'(x) for f(x) = cos(3x)·e^(4x).",
        "answer_type": "text",
        "correct_answer": "e^(4x)(4cos(3x) - 3sin(3x))",
        "tolerance": None,
        "unit": "",
        "solution": (
            "Product rule: derivative of cos(3x) is −3sin(3x); of e^(4x) is 4e^(4x). "
            "f' = −3sin(3x)e^(4x) + cos(3x)·4e^(4x) = e^(4x)(4cos(3x) − 3sin(3x))."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_tangent_1",
        "exam": "maxf02",
        "topic": "tangent_lines",
        "topic_display": "Tangent lines",
        "points": 2,
        "exam_frequency": 0.9,
        "no_calculator": True,
        "question": "Find the equation of the tangent line to y = x² − 2x + 1 at x = 3.",
        "answer_type": "text",
        "correct_answer": "y = 4x - 8",
        "tolerance": None,
        "unit": "",
        "solution": (
            "y' = 2x − 2, so y'(3) = 4. y(3) = 9 − 6 + 1 = 4. "
            "Tangent: y − 4 = 4(x − 3) ⇒ y = 4x − 8."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_tangent_2",
        "exam": "maxf02",
        "topic": "tangent_lines",
        "topic_display": "Tangent lines",
        "points": 3,
        "exam_frequency": 0.9,
        "no_calculator": True,
        "question": "Find the equation of the tangent line to y = ln(x) at x = 1.",
        "answer_type": "text",
        "correct_answer": "y = x - 1",
        "tolerance": None,
        "unit": "",
        "solution": (
            "y' = 1/x, so y'(1) = 1. y(1) = ln(1) = 0. "
            "Tangent: y − 0 = 1·(x − 1) ⇒ y = x − 1."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_related_rates_1",
        "exam": "maxf02",
        "topic": "related_rates",
        "topic_display": "Related rates",
        "points": 3,
        "exam_frequency": 0.9,
        "no_calculator": True,
        "question": (
            "A circular oil spill expands so its radius increases at 2 m/min. "
            "How fast is the area increasing when the radius is 5 m?"
        ),
        "answer_type": "numeric",
        "correct_answer": 62.83,
        "tolerance": 0.02,
        "unit": "m²/min",
        "solution": (
            "A = πr², so dA/dt = 2πr·dr/dt. With r = 5 and dr/dt = 2: "
            "dA/dt = 2π·5·2 = 20π m²/min."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_related_rates_2",
        "exam": "maxf02",
        "topic": "related_rates",
        "topic_display": "Related rates",
        "points": 3,
        "exam_frequency": 0.9,
        "no_calculator": True,
        "question": (
            "A spherical balloon is inflated at 100 cm³/s. "
            "How fast is the radius increasing when r = 10 cm?"
        ),
        "answer_type": "numeric",
        "correct_answer": 0.0796,
        "tolerance": 0.03,
        "unit": "cm/s",
        "solution": (
            "V = (4/3)πr³, so dV/dt = 4πr²·dr/dt. "
            "dr/dt = (dV/dt)/(4πr²) = 100/(4π·100) = 1/(4π) cm/s."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_curve_analysis_1",
        "exam": "maxf02",
        "topic": "curve_analysis",
        "topic_display": "Curve analysis",
        "points": 3,
        "exam_frequency": 0.8,
        "no_calculator": True,
        "question": "Find all local extrema of f(x) = x³ − 3x + 1.",
        "answer_type": "text",
        "correct_answer": "Local max at (-1, 3), local min at (1, -1)",
        "tolerance": None,
        "unit": "",
        "solution": (
            "f'(x) = 3x² − 3 = 3(x−1)(x+1), critical points x = ±1. "
            "f''(x) = 6x: f''(−1) = −6 < 0 ⇒ local max; f(−1) = 3. "
            "f''(1) = 6 > 0 ⇒ local min; f(1) = −1."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_curve_analysis_2",
        "exam": "maxf02",
        "topic": "curve_analysis",
        "topic_display": "Curve analysis",
        "points": 2,
        "exam_frequency": 0.8,
        "no_calculator": True,
        "question": "For f(x) = x·e^(−x), find the x-coordinate of the maximum.",
        "answer_type": "numeric",
        "correct_answer": 1.0,
        "tolerance": 0.01,
        "unit": "",
        "solution": (
            "f'(x) = e^(−x) − x·e^(−x) = e^(−x)(1 − x). "
            "f'(x) = 0 ⇒ x = 1. f''(1) = −e^(−1) < 0 ⇒ maximum at x = 1."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_circle_1",
        "exam": "maxf02",
        "topic": "circle_equations",
        "topic_display": "Circle equations",
        "points": 3,
        "exam_frequency": 0.8,
        "no_calculator": True,
        "question": (
            "Find the center and radius of the circle x² + y² − 6x + 4y = 3."
        ),
        "answer_type": "text",
        "correct_answer": "Center (3, -2), radius 4",
        "tolerance": None,
        "unit": "",
        "solution": (
            "Complete the square: x² − 6x = (x−3)² − 9; y² + 4y = (y+2)² − 4. "
            "Equation becomes (x−3)² + (y+2)² = 3 + 9 + 4 = 16. "
            "Center (3, −2), radius √16 = 4."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_optimization_1",
        "exam": "maxf02",
        "topic": "optimization",
        "topic_display": "Optimization",
        "points": 3,
        "exam_frequency": 0.6,
        "no_calculator": True,
        "question": (
            "Find the maximum area of a rectangle inscribed under y = 9 − x² "
            "(above the x-axis), symmetric about the y-axis."
        ),
        "answer_type": "numeric",
        "correct_answer": 20.78,
        "tolerance": 0.02,
        "unit": "",
        "solution": (
            "Vertices at (±x, 0) and (±x, 9−x²) with x > 0: "
            "A(x) = 2x(9−x²) = 18x − 2x³. "
            "A'(x) = 18 − 6x² = 0 ⇒ x² = 3, x = √3. "
            "A = 2√3·(9−3) = 12√3."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_optimization_2",
        "exam": "maxf02",
        "topic": "optimization",
        "topic_display": "Optimization",
        "points": 3,
        "exam_frequency": 0.6,
        "no_calculator": True,
        "question": (
            "The sum of two positive numbers is 10. Find the maximum possible value "
            "of their product."
        ),
        "answer_type": "numeric",
        "correct_answer": 25,
        "tolerance": 0.01,
        "unit": "",
        "solution": (
            "Let the numbers be x and 10−x with 0 < x < 10. "
            "P(x) = x(10−x) = 10x − x². P'(x) = 10 − 2x = 0 ⇒ x = 5. "
            "P(5) = 25 (parabola opens downward, so maximum)."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_limit_def_mc_1",
        "exam": "maxf02",
        "topic": "definitions",
        "topic_display": "Definitions and foundations",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Which is the correct limit definition of f'(x)?",
        "answer_type": "multiple_choice",
        "correct_answer": "A",
        "tolerance": None,
        "unit": "",
        "solution": (
            "The derivative is f'(x) = lim_{h→0} [f(x+h) − f(x)] / h (difference quotient)."
        ),
        "choices": [
            "A) lim h→0 [f(x+h) - f(x)] / h",
            "B) lim h→0 [f(x) - f(h)] / x",
            "C) lim x→0 f(x) / x",
            "D) lim h→∞ [f(x+h) - f(x)] / h",
        ],
    },
]
