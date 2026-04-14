"""Matematikfrågor för MAXF02 (Mat–Fys provet-förberedelse). Alla uppgifter löses utan miniräknare."""

MAXF02_QUESTIONS = [
    {
        "id": "maxf02_trig_values_1",
        "exam": "maxf02",
        "topic": "exact_trig",
        "topic_display": "Exakta trigonometriska värden",
        "points": 1,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Bestäm det exakta värdet av $\\sin(840°)$.",
        "answer_type": "numeric",
        "correct_answer": 0.866,
        "tolerance": 0.01,
        "unit": "",
        "solution": (
            "Reducera vinkeln: $840° - 720° = 120°$. "
            "$\\sin(120°) = \\sin(180° - 60°) = \\sin(60°) = \\frac{\\sqrt{3}}{2}$."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_trig_values_2",
        "exam": "maxf02",
        "topic": "exact_trig",
        "topic_display": "Exakta trigonometriska värden",
        "points": 1,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Bestäm det exakta värdet av $\\cos(4\\pi/3)$.",
        "answer_type": "numeric",
        "correct_answer": -0.5,
        "tolerance": 0.01,
        "unit": "",
        "solution": (
            "$4\\pi/3$ ligger i tredje kvadranten (referensvinkel $\\pi/3$). "
            "$\\cos(4\\pi/3) = -\\cos(\\pi/3) = -\\frac{1}{2}$."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_trig_values_3",
        "exam": "maxf02",
        "topic": "exact_trig",
        "topic_display": "Exakta trigonometriska värden",
        "points": 1,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Bestäm det exakta värdet av $\\tan(-120°)$.",
        "answer_type": "numeric",
        "correct_answer": 1.732,
        "tolerance": 0.01,
        "unit": "",
        "solution": (
            "$\\tan$ är udda: $\\tan(-120°) = -\\tan(120°)$. "
            "$\\tan(120°) = \\tan(180° - 60°) = -\\tan(60°) = -\\sqrt{3}$, "
            "alltså $\\tan(-120°) = \\sqrt{3}$."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_trig_eq_1",
        "exam": "maxf02",
        "topic": "trig_equations",
        "topic_display": "Trigonometriska ekvationer",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Lös $\\sin(x) = \\frac{1}{2}$ för $0 \\leq x \\leq 2\\pi$. Ange alla lösningar (radianer).",
        "answer_type": "text",
        "correct_answer": "π/6 och 5π/6",
        "tolerance": None,
        "unit": "",
        "solution": (
            "$\\sin(x) = \\frac{1}{2}$ för $x = \\frac{\\pi}{6}$ (första kvadranten) och $x = \\pi - \\frac{\\pi}{6} = \\frac{5\\pi}{6}$ "
            "(andra kvadranten)."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_trig_eq_2",
        "exam": "maxf02",
        "topic": "trig_equations",
        "topic_display": "Trigonometriska ekvationer",
        "points": 3,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Lös $\\cos(2x) = \\frac{1}{2}$ för $0 \\leq x \\leq 2\\pi$. Ange alla lösningar (radianer).",
        "answer_type": "text",
        "correct_answer": "π/6, 5π/6, 7π/6, 11π/6",
        "tolerance": None,
        "unit": "",
        "solution": (
            "Låt $\\theta = 2x$, så $\\theta \\in [0, 4\\pi]$. $\\cos(\\theta) = \\frac{1}{2}$ för $\\theta = \\frac{\\pi}{3}, \\frac{5\\pi}{3}, \\frac{7\\pi}{3}, \\frac{11\\pi}{3}$. "
            "Dividera med $2$: $x = \\frac{\\pi}{6}, \\frac{5\\pi}{6}, \\frac{7\\pi}{6}, \\frac{11\\pi}{6}$."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_trig_eq_3",
        "exam": "maxf02",
        "topic": "trig_equations",
        "topic_display": "Trigonometriska ekvationer",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Lös $2\\sin(x) - 1 = 0$ för $0° \\leq x \\leq 360°$. Ange alla lösningar.",
        "answer_type": "text",
        "correct_answer": "30° och 150°",
        "tolerance": None,
        "unit": "",
        "solution": (
            "$2\\sin(x) = 1 \\Rightarrow \\sin(x) = \\frac{1}{2}$. I $[0°, 360°]$ ger det $x = 30°$ och $x = 180° - 30° = 150°$."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_deriv_1",
        "exam": "maxf02",
        "topic": "derivatives",
        "topic_display": "Derivata",
        "points": 1,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Bestäm derivatan av $f(x) = x^3 + \\ln(x)$.",
        "answer_type": "text",
        "correct_answer": "3x² + 1/x",
        "tolerance": None,
        "unit": "",
        "solution": (
            "$\\frac{d}{dx}(x^3) = 3x^2$; $\\frac{d}{dx}(\\ln x) = \\frac{1}{x}$. Summan: $f'(x) = 3x^2 + \\frac{1}{x}$."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_deriv_2",
        "exam": "maxf02",
        "topic": "derivatives",
        "topic_display": "Derivata",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Bestäm $f'(x)$ för $f(x) = (2x + 1) \\cdot e^{3x}$.",
        "answer_type": "text",
        "correct_answer": "(6x+5)e^(3x)",
        "tolerance": None,
        "unit": "",
        "solution": (
            "Produktregeln: $u = 2x+1$, $v = e^{3x}$; $u' = 2$, $v' = 3e^{3x}$. "
            "$f' = 2e^{3x} + (2x+1) \\cdot 3e^{3x} = e^{3x}(2 + 6x + 3) = (6x+5)e^{3x}$."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_deriv_3",
        "exam": "maxf02",
        "topic": "derivatives",
        "topic_display": "Derivata",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Bestäm $f'(x)$ för $f(x) = \\frac{x^2}{x + 2}$.",
        "answer_type": "text",
        "correct_answer": "x(x+4)/(x+2)²",
        "tolerance": None,
        "unit": "",
        "solution": (
            "Kvotregeln: $\\frac{(2x)(x+2) - x^2 \\cdot 1}{(x+2)^2} = \\frac{2x^2+4x-x^2}{(x+2)^2}$ "
            "$= \\frac{x^2+4x}{(x+2)^2} = \\frac{x(x+4)}{(x+2)^2}$."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_deriv_4",
        "exam": "maxf02",
        "topic": "derivatives",
        "topic_display": "Derivata",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Bestäm $f'(x)$ för $f(x) = \\cos(3x) \\cdot e^{4x}$.",
        "answer_type": "text",
        "correct_answer": "e^(4x)(4cos(3x) - 3sin(3x))",
        "tolerance": None,
        "unit": "",
        "solution": (
            "Produktregeln: derivatan av $\\cos(3x)$ är $-3\\sin(3x)$; av $e^{4x}$ är $4e^{4x}$. "
            "$f' = -3\\sin(3x)e^{4x} + \\cos(3x) \\cdot 4e^{4x} = e^{4x}(4\\cos(3x) - 3\\sin(3x))$."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_tangent_1",
        "exam": "maxf02",
        "topic": "tangent_lines",
        "topic_display": "Tangentlinjer",
        "points": 2,
        "exam_frequency": 0.9,
        "no_calculator": True,
        "question": "Bestäm ekvationen för tangentlinjen till $y = x^2 - 2x + 1$ i punkten $x = 3$.",
        "answer_type": "text",
        "correct_answer": "y = 4x - 8",
        "tolerance": None,
        "unit": "",
        "solution": (
            "$y' = 2x - 2$, så $y'(3) = 4$. $y(3) = 9 - 6 + 1 = 4$. "
            "Tangent: $y - 4 = 4(x - 3) \\Rightarrow y = 4x - 8$."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_tangent_2",
        "exam": "maxf02",
        "topic": "tangent_lines",
        "topic_display": "Tangentlinjer",
        "points": 3,
        "exam_frequency": 0.9,
        "no_calculator": True,
        "question": "Bestäm ekvationen för tangentlinjen till $y = \\ln(x)$ i punkten $x = 1$.",
        "answer_type": "text",
        "correct_answer": "y = x - 1",
        "tolerance": None,
        "unit": "",
        "solution": (
            "$y' = \\frac{1}{x}$, så $y'(1) = 1$. $y(1) = \\ln(1) = 0$. "
            "Tangent: $y - 0 = 1 \\cdot (x - 1) \\Rightarrow y = x - 1$."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_related_rates_1",
        "exam": "maxf02",
        "topic": "related_rates",
        "topic_display": "Ändringstakt",
        "points": 3,
        "exam_frequency": 0.9,
        "no_calculator": True,
        "question": (
            "Ett cirkulärt oljeutsläpp expanderar så att radien ökar med $2\\;\\text{m/min}$. "
            "Hur snabbt ökar arean när radien är $5\\;\\text{m}$?"
        ),
        "answer_type": "numeric",
        "correct_answer": 62.83,
        "tolerance": 0.02,
        "unit": "m²/min",
        "solution": (
            "$A = \\pi r^2$, så $\\frac{dA}{dt} = 2\\pi r \\cdot \\frac{dr}{dt}$. Med $r = 5$ och $\\frac{dr}{dt} = 2$: "
            "$\\frac{dA}{dt} = 2\\pi \\cdot 5 \\cdot 2 = 20\\pi\\;\\text{m}^2/\\text{min}$."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_related_rates_2",
        "exam": "maxf02",
        "topic": "related_rates",
        "topic_display": "Ändringstakt",
        "points": 3,
        "exam_frequency": 0.9,
        "no_calculator": True,
        "question": (
            "En sfärisk ballong blåses upp med $100\\;\\text{cm}^3/\\text{s}$. "
            "Hur snabbt ökar radien när $r = 10\\;\\text{cm}$?"
        ),
        "answer_type": "numeric",
        "correct_answer": 0.0796,
        "tolerance": 0.03,
        "unit": "cm/s",
        "solution": (
            "$V = \\frac{4}{3}\\pi r^3$, så $\\frac{dV}{dt} = 4\\pi r^2 \\cdot \\frac{dr}{dt}$. "
            "$\\frac{dr}{dt} = \\frac{\\frac{dV}{dt}}{4\\pi r^2} = \\frac{100}{4\\pi \\cdot 100} = \\frac{1}{4\\pi}\\;\\text{cm/s}$."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_curve_analysis_1",
        "exam": "maxf02",
        "topic": "curve_analysis",
        "topic_display": "Kurvanalys",
        "points": 3,
        "exam_frequency": 0.8,
        "no_calculator": True,
        "question": "Bestäm alla lokala extrempunkter för $f(x) = x^3 - 3x + 1$.",
        "answer_type": "text",
        "correct_answer": "Lokalt max vid (-1, 3), lokalt min vid (1, -1)",
        "tolerance": None,
        "unit": "",
        "solution": (
            "$f'(x) = 3x^2 - 3 = 3(x-1)(x+1)$, kritiska punkter $x = \\pm 1$. "
            "$f''(x) = 6x$: $f''(-1) = -6 < 0 \\Rightarrow$ lokalt max; $f(-1) = 3$. "
            "$f''(1) = 6 > 0 \\Rightarrow$ lokalt min; $f(1) = -1$."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_curve_analysis_2",
        "exam": "maxf02",
        "topic": "curve_analysis",
        "topic_display": "Kurvanalys",
        "points": 2,
        "exam_frequency": 0.8,
        "no_calculator": True,
        "question": "Bestäm $x$-koordinaten för maximum till $f(x) = x \\cdot e^{-x}$.",
        "answer_type": "numeric",
        "correct_answer": 1.0,
        "tolerance": 0.01,
        "unit": "",
        "solution": (
            "$f'(x) = e^{-x} - x \\cdot e^{-x} = e^{-x}(1 - x)$. "
            "$f'(x) = 0 \\Rightarrow x = 1$. $f''(1) = -e^{-1} < 0 \\Rightarrow$ maximum vid $x = 1$."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_circle_1",
        "exam": "maxf02",
        "topic": "circle_equations",
        "topic_display": "Cirkelns ekvation",
        "points": 3,
        "exam_frequency": 0.8,
        "no_calculator": True,
        "question": (
            "Bestäm medelpunkt och radie för cirkeln $x^2 + y^2 - 6x + 4y = 3$."
        ),
        "answer_type": "text",
        "correct_answer": "Medelpunkt (3, -2), radie 4",
        "tolerance": None,
        "unit": "",
        "solution": (
            "Kvadratkomplettering: $x^2 - 6x = (x-3)^2 - 9$; $y^2 + 4y = (y+2)^2 - 4$. "
            "Ekvationen blir $(x-3)^2 + (y+2)^2 = 3 + 9 + 4 = 16$. "
            "Medelpunkt $(3, -2)$, radie $\\sqrt{16} = 4$."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_optimization_1",
        "exam": "maxf02",
        "topic": "optimization",
        "topic_display": "Optimering",
        "points": 3,
        "exam_frequency": 0.6,
        "no_calculator": True,
        "question": (
            "Bestäm den maximala arean av en rektangel inskriven under $y = 9 - x^2$ "
            "(ovanför $x$-axeln), symmetrisk kring $y$-axeln."
        ),
        "answer_type": "numeric",
        "correct_answer": 20.78,
        "tolerance": 0.02,
        "unit": "",
        "solution": (
            "Hörn i $(\\pm x, 0)$ och $(\\pm x, 9-x^2)$ med $x > 0$: "
            "$A(x) = 2x(9-x^2) = 18x - 2x^3$. "
            "$A'(x) = 18 - 6x^2 = 0 \\Rightarrow x^2 = 3$, $x = \\sqrt{3}$. "
            "$A = 2\\sqrt{3} \\cdot (9-3) = 12\\sqrt{3}$."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_optimization_2",
        "exam": "maxf02",
        "topic": "optimization",
        "topic_display": "Optimering",
        "points": 3,
        "exam_frequency": 0.6,
        "no_calculator": True,
        "question": (
            "Summan av två positiva tal är $10$. Bestäm det största möjliga värdet "
            "av deras produkt."
        ),
        "answer_type": "numeric",
        "correct_answer": 25,
        "tolerance": 0.01,
        "unit": "",
        "solution": (
            "Låt talen vara $x$ och $10-x$ med $0 < x < 10$. "
            "$P(x) = x(10-x) = 10x - x^2$. $P'(x) = 10 - 2x = 0 \\Rightarrow x = 5$. "
            "$P(5) = 25$ (parabeln öppnar nedåt, alltså maximum)."
        ),
        "choices": None,
    },
    {
        "id": "maxf02_limit_def_mc_1",
        "exam": "maxf02",
        "topic": "definitions",
        "topic_display": "Definitioner och grunder",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": True,
        "question": "Vilken är den korrekta gränsvärdes­definitionen av $f'(x)$?",
        "answer_type": "multiple_choice",
        "correct_answer": "A",
        "tolerance": None,
        "unit": "",
        "solution": (
            "Derivatan definieras som $f'(x) = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}$ (differenskvoten)."
        ),
        "choices": [
            "A) $\\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}$",
            "B) $\\lim_{h \\to 0} \\frac{f(x) - f(h)}{x}$",
            "C) $\\lim_{x \\to 0} \\frac{f(x)}{x}$",
            "D) $\\lim_{h \\to \\infty} \\frac{f(x+h) - f(x)}{h}$",
        ],
    },
]
