# Modular Question-Template System — Pre-plan

> **Status:** Draft · April 2026
> **Scope:** Replace 85 static question dicts with parameterized templates that generate
> infinite unique instances while preserving the existing scoring contract.

---

## Table of Contents

1. [Template Schema](#1-template-schema)
2. [Engine Design](#2-engine-design)
3. [Migration Strategy](#3-migration-strategy-5-phases)
4. [Risk Analysis](#4-risk-analysis)
5. [Example Templates](#5-example-templates)

---

## 1. Template Schema

Each template is a JSON object (stored as Python dicts in `*_TEMPLATES` lists,
mirroring the current `*_QUESTIONS` pattern). The schema below is authoritative.

```jsonc
{
  // ─── identity ───────────────────────────────────────────────
  "template_id": "fyxf04_grating",          // unique, snake_case
  "version":     1,                          // bump on any schema-breaking edit

  // ─── prompt ─────────────────────────────────────────────────
  "prompt_template": "En laser med våglängd $\\lambda = {{lambda_nm}}\\;\\text{nm}$ ...",
  //   • Placeholders use double-brace: {{var_name}}
  //   • May contain KaTeX / LaTeX markup
  //   • Multi-line via Python parenthesized string concatenation (same as today)

  // ─── variables ──────────────────────────────────────────────
  "variables": [
    {
      "name":  "lambda_nm",
      "kind":  "int",             // int | float | choice
      "min":   400,
      "max":   700,
      "step":  1                  // RNG picks from range(min, max+1, step)
      // "pool" and "labels" are unused for int/float kinds
    },
    {
      "name":  "slits_per_mm",
      "kind":  "choice",
      "pool":  [300, 500, 600, 800, 1000],   // RNG picks one
      "labels": null              // optional display overrides for MC
    },
    {
      "name":  "order_m",
      "kind":  "int",
      "min":   1,
      "max":   3,
      "step":  1
    }
  ],
  //   kind  | required fields         | optional
  //   ------+-------------------------+---------
  //   int   | min, max, step          |
  //   float | min, max, step, dp      | dp = decimal places for display rounding
  //   choice| pool                    | labels

  // ─── answer specification ───────────────────────────────────
  "answer_spec": {
    "type":               "numeric",   // numeric | text | mc
    "expr":               "degrees(asin(order_m * lambda_nm * 1e-9 / (1 / (slits_per_mm * 1e3))))",
    //   • Python expression evaluated inside a restricted math namespace
    //   • Variable names match "variables[].name" exactly
    //   • Result is the correct answer for this instance

    "tolerance_spec": {
      "mode":  "relative",             // relative | absolute
      "value": 0.02                    // same semantics as current tolerance field:
                                       //   relative → |user − correct| ≤ value × |correct|
                                       //   absolute → |user − correct| ≤ value
    },

    "correct_letter_rule": null,       // only for mc; see §1.1
    "unit":                "°"
  },

  // ─── solution template ──────────────────────────────────────
  "solution_template": (
      "Spaltavstånd $d = 1/({{slits_per_mm}}\\;\\text{mm}^{-1}) = {{d_m:.3e}}\\;\\text{m}$.\n"
      "Gitterekvationen: $d \\sin \\theta = m\\lambda$ ...\n"
      "$\\theta = \\arcsin({{sin_val:.3f}}) \\approx {{answer:.1f}}°$."
  ),
  //   • Same {{var}} placeholders, plus derived names injected by the engine
  //   • Format specs after colon: {{var:.2f}}, {{var:.3e}}
  //   • Engine adds "answer", "sin_val", "d_m" etc. via answer_spec.derived (see §1.2)

  // ─── rendering hints ────────────────────────────────────────
  "rendering_hints": {
    "decimal_comma":      true,        // post-process: replace '.' with ',' in rendered numbers
    "katex":              true,        // prompt contains KaTeX markup
    "significant_figures": null,       // if set (int), round displayed answer to N sig-figs
    "display_unit":       "°"          // unit shown next to answer input (mirrors answer_spec.unit)
  },

  // ─── metadata (unchanged from current static questions) ─────
  "metadata": {
    "exam":            "fyxf04",
    "topic":           "diffraction_grating",
    "topic_display":   "Diffraktionsgitter",
    "points":          2,
    "exam_frequency":  1.0,
    "no_calculator":   false
  }
}
```

### 1.1 Multiple-Choice Answer Spec

For MC templates, `answer_spec` differs:

```jsonc
{
  "type": "mc",
  "correct_letter_rule": "max_choice",   // see below
  "choices_template": [
    { "letter": "A", "expr": "F / (2 * m)",   "label_template": "${{val_A:.0f}}\\;\\text{m/s}^2$" },
    { "letter": "B", "expr": "F / m",          "label_template": "${{val_B:.0f}}\\;\\text{m/s}^2$" },
    { "letter": "C", "expr": "F",              "label_template": "${{val_C:.0f}}\\;\\text{m/s}^2$" },
    { "letter": "D", "expr": "F * m",          "label_template": "${{val_D:.0f}}\\;\\text{m/s}^2$" }
  ],
  "correct_letter_rule": "B",
  //   • Fixed letter: always "B" is correct (distractor expressions create wrong values)
  //   • OR computed: "max_choice" / "min_choice" — engine evaluates all exprs
  //     and picks the letter whose value is largest/smallest
  //   • OR "expr_match" — engine evaluates answer_spec.expr and picks the choice
  //     whose evaluated expr is closest

  "tolerance_spec": null,
  "unit": null
}
```

### 1.2 Derived Variables

Templates may declare `derived` in `answer_spec` — intermediate values computed
*after* variable binding but *before* answer evaluation. These are available in
`solution_template`:

```jsonc
"answer_spec": {
  "type": "numeric",
  "derived": {
    "d_m":     "1 / (slits_per_mm * 1e3)",
    "sin_val": "order_m * lambda_nm * 1e-9 / d_m"
  },
  "expr": "degrees(asin(sin_val))",
  "tolerance_spec": { "mode": "relative", "value": 0.02 },
  "unit": "°"
}
```

Evaluation order: **variables → derived (topologically sorted) → expr**.

### 1.3 Validation Constraints on Variables

The engine must reject a template at load time if:

- Any `kind: "int"` or `kind: "float"` has `min >= max` or `step <= 0`.
- Any `kind: "choice"` has an empty `pool`.
- `expr` references a name not in `variables` or `derived`.
- `prompt_template` or `solution_template` contain `{{x}}` where `x` is not in
  variables, derived, or the special name `answer`.

At instantiation time, the engine must reject (resample) if:

- A derived or answer expression produces `NaN`, `±Inf`, or raises `ZeroDivisionError`.
- For numeric answers: `|answer| > 1e12` or `|answer| < 1e-12` (configurable bounds).
- For MC: two choice expressions evaluate to the same display string after rounding.

---

## 2. Engine Design

### 2.1 Module: `question_engine.py`

New file at project root, alongside `scorer.py`.

```
question_engine.py
├── SAFE_NAMESPACE          (dict: restricted builtins for eval)
├── validate_template()     (load-time schema check)
├── instantiate()           (template + RNG → standard question dict)
├── _bind_variables()       (RNG → {name: value} mapping)
├── _eval_derived()         (topological eval of derived expressions)
├── _eval_expr()            (single expression in SAFE_NAMESPACE)
├── _render_template()      ({{var}} substitution with format specs)
├── _render_mc_choices()    (evaluate choice exprs, build choices list)
├── compute_answer()        (answer_spec + bindings → (value, metadata))
└── render_prompt()         (prompt_template + bindings → str)
```

### 2.2 `SAFE_NAMESPACE`

Restricted math namespace to prevent arbitrary code execution in `expr` strings:

```python
import math

SAFE_NAMESPACE: dict[str, Any] = {
    # trig (radians)
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "asin": math.asin, "acos": math.acos, "atan": math.atan, "atan2": math.atan2,
    # trig (degrees)
    "degrees": math.degrees, "radians": math.radians,
    # powers / roots
    "sqrt": math.sqrt, "pow": pow, "abs": abs,
    "exp": math.exp, "log": math.log, "log10": math.log10, "log2": math.log2,
    # constants
    "pi": math.pi, "e": math.e,
    # rounding
    "round": round, "floor": math.floor, "ceil": math.ceil,
    # min/max for choice rules
    "min": min, "max": max,
}
```

**No** `__builtins__`, `__import__`, `exec`, `eval`, `open`, `os`, or `sys`.
Expressions are evaluated via:

```python
def _eval_expr(expr: str, bindings: dict[str, float]) -> float:
    ns = {**SAFE_NAMESPACE, **bindings, "__builtins__": {}}
    return float(eval(expr, ns))  # noqa: S307
```

### 2.3 `instantiate(template, rng) → dict`

Central function. Returns a dict with the **exact same keys** as today's static
questions, so `scorer.py` and `app.py` require zero changes to consume it.

```python
def instantiate(
    template: dict,
    rng: random.Random | None = None,
) -> dict[str, Any]:
    """Materialize a template into a concrete question dict.

    The returned dict is wire-compatible with the static dicts in
    questions_*.py — same keys, same types. scorer.score_answers() and
    app.start_quiz() work unchanged.
    """
    if rng is None:
        rng = random.Random()

    bindings = _bind_variables(template["variables"], rng)
    derived  = _eval_derived(template["answer_spec"].get("derived", {}), bindings)
    bindings.update(derived)

    answer_val, answer_meta = compute_answer(template["answer_spec"], bindings)
    bindings["answer"] = answer_val

    prompt   = _render_template(template["prompt_template"], bindings, template["rendering_hints"])
    solution = _render_template(template["solution_template"], bindings, template["rendering_hints"])

    answer_type = template["answer_spec"]["type"]
    choices = None
    correct_answer = answer_val

    if answer_type == "mc":
        choices, correct_answer = _render_mc_choices(
            template["answer_spec"], bindings, template["rendering_hints"]
        )

    # Generate a unique instance id: template_id + hash of bindings
    instance_seed = "|".join(f"{k}={v}" for k, v in sorted(bindings.items()) if k != "answer")
    instance_hash = hashlib.md5(instance_seed.encode()).hexdigest()[:8]
    instance_id   = f"{template['template_id']}_{instance_hash}"

    meta = template["metadata"]
    return {
        "id":             instance_id,
        "template_id":    template["template_id"],
        "exam":           meta["exam"],
        "topic":          meta["topic"],
        "topic_display":  meta["topic_display"],
        "points":         meta["points"],
        "exam_frequency": meta["exam_frequency"],
        "no_calculator":  meta["no_calculator"],
        "question":       prompt,
        "answer_type":    {"numeric": "numeric", "text": "text", "mc": "multiple_choice"}[answer_type],
        "correct_answer": correct_answer,
        "tolerance":      answer_meta.get("tolerance"),
        "unit":           template["answer_spec"].get("unit", ""),
        "solution":       solution,
        "choices":        choices,
    }
```

**Key design choice:** the returned dict has an extra `"template_id"` key.
`scorer.py` ignores unknown keys, so this is backwards-compatible. It enables
tracing an instance back to its template for analytics.

### 2.4 `_bind_variables(variables, rng) → dict`

```python
def _bind_variables(variables: list[dict], rng: random.Random) -> dict[str, float]:
    bindings = {}
    for var in variables:
        name = var["name"]
        kind = var["kind"]
        if kind == "int":
            val = rng.randrange(var["min"], var["max"] + 1, var.get("step", 1))
        elif kind == "float":
            steps = round((var["max"] - var["min"]) / var["step"])
            val = var["min"] + rng.randint(0, steps) * var["step"]
            dp = var.get("dp")
            if dp is not None:
                val = round(val, dp)
        elif kind == "choice":
            val = rng.choice(var["pool"])
        else:
            raise ValueError(f"Unknown variable kind: {kind!r}")
        bindings[name] = val
    return bindings
```

### 2.5 `_render_template(template_str, bindings, hints) → str`

```python
import re as _re

_PLACEHOLDER_RE = _re.compile(r"\{\{(\w+)(?::([^}]+))?\}\}")

def _render_template(
    template_str: str,
    bindings: dict[str, Any],
    hints: dict,
) -> str:
    def _replace(m: _re.Match) -> str:
        name, fmt = m.group(1), m.group(2)
        val = bindings.get(name, m.group(0))  # leave unresolved if missing
        if fmt:
            rendered = format(val, fmt)
        else:
            rendered = str(val)
        if hints.get("decimal_comma"):
            rendered = rendered.replace(".", ",")
        return rendered

    return _PLACEHOLDER_RE.sub(_replace, template_str)
```

**Critical:** the regex deliberately avoids matching `{,}` (KaTeX thousands
separator) because placeholders require `{{name}}` with an alphanumeric name
after the opening braces. See §4.1 for full KaTeX collision analysis.

### 2.6 `compute_answer(answer_spec, bindings) → (value, metadata)`

```python
def compute_answer(
    answer_spec: dict,
    bindings: dict[str, float],
) -> tuple[Any, dict]:
    atype = answer_spec["type"]
    meta: dict[str, Any] = {}

    if atype == "numeric":
        val = _eval_expr(answer_spec["expr"], bindings)
        tol_spec = answer_spec.get("tolerance_spec", {})
        tol_mode = tol_spec.get("mode", "relative")
        tol_val  = tol_spec.get("value", 0.0)
        # Store the tolerance the same way scorer.py expects it:
        # relative → tolerance field is the fraction (scorer multiplies by |correct|)
        # absolute → we need |correct| to reverse-engineer the relative value,
        #            OR we change scorer.py (deferred to Phase 0)
        if tol_mode == "relative":
            meta["tolerance"] = tol_val
        else:
            # absolute: convert to relative for scorer compat
            ref = abs(val)
            meta["tolerance"] = tol_val / ref if ref > 1e-15 else tol_val
        return val, meta

    if atype == "text":
        # Text answers: expr evaluates to a string key in bindings
        val = answer_spec.get("expr")
        if val and "{{" not in val:
            try:
                val = _eval_expr(val, bindings)
            except Exception:
                pass
        meta["tolerance"] = None
        return val, meta

    if atype == "mc":
        meta["tolerance"] = None
        return None, meta  # letter determined by _render_mc_choices

    raise ValueError(f"Unknown answer type: {atype!r}")
```

### 2.7 Integration with `app.py`

#### `start_quiz` (lines 57–79 of current `app.py`)

Current flow:

```
questions = list(EXAM_SETS[mode])
random.shuffle(questions)
session["question_ids"] = [q["id"] for q in questions]
```

New flow:

```python
from question_engine import instantiate

quiz_rng = random.Random()  # seeded per quiz for reproducibility

materialized = []
for src in EXAM_SETS.get(exam_mode, ALL_SOURCES):
    if "template_id" in src:
        q = instantiate(src, quiz_rng)
    else:
        q = src  # legacy static dict, unchanged
    materialized.append(q)

random.shuffle(materialized)

# Store full materialized questions in session for submit_quiz lookup
session["materialized_questions"] = materialized
session["question_ids"] = [q["id"] for q in materialized]
```

#### `submit_quiz` (lines 82–111 of current `app.py`)

Current flow uses `ALL_QUESTIONS` for lookup by id. This breaks for templates
because instance ids are unique per quiz. Change:

```python
# Before (line 92):
q_lookup = {q["id"]: q for q in ALL_QUESTIONS}

# After:
materialized = session.get("materialized_questions", [])
q_lookup = {q["id"]: q for q in materialized}
# Fall back to static bank for legacy sessions
if not q_lookup:
    q_lookup = {q["id"]: q for q in ALL_QUESTIONS}
```

#### Session storage concern

Flask's default cookie-based session has a **4 KB limit**. 85 materialized
questions easily exceed this. Options (in order of preference):

1. **Flask-Session with filesystem backend** — `SESSION_TYPE = "filesystem"`,
   session dir on disk. Zero infrastructure, works on Render.
2. **Redis** — better for production, but adds a dependency.
3. **Store only seed + template list** — re-materialize on submit using the
   same RNG seed. Smallest session, but adds latency and complexity.

**Recommendation:** Option 1 for Phase 0–2, migrate to option 3 once stable.

---

## 3. Migration Strategy (5 Phases)

### Phase 0 — Infrastructure + Unit Tests

**Goal:** Ship `question_engine.py` with zero impact on the live app.

| Task | Detail |
|------|--------|
| Create `question_engine.py` | All functions from §2, plus `validate_template()` |
| Create `test_question_engine.py` | pytest suite: binding, expression eval, rendering, round-trip |
| Add `flask-session` to `requirements.txt` | For server-side session storage |
| Add `constraints` mechanism | Rejection-resample loop with max 100 attempts |
| Schema validator | Validate all templates at import time (`validate_template()`) |

**Test matrix:**

| Test | Asserts |
|------|---------|
| `test_bind_int_range` | Value ∈ [min, max], divisible by step |
| `test_bind_float_dp` | Decimal places match `dp` |
| `test_bind_choice` | Value ∈ pool |
| `test_eval_safe` | `sin(pi/2)` → 1.0 |
| `test_eval_rejects_builtins` | `__import__('os')` raises |
| `test_render_decimal_comma` | `{{x:.2f}}` with x=3.14, comma=true → "3,14" |
| `test_render_leaves_katex` | `{,}` and `\{` in template survive untouched |
| `test_instantiate_returns_compat_dict` | Output has all 14 keys from static schema |
| `test_tolerance_relative` | `_check_numeric(user, computed, tol)` agrees with `scorer._check_numeric` |
| `test_mc_letter_stability` | Same seed → same correct letter |
| `test_rejection_nan` | Template with `asin(2.0)` triggers resample, not crash |

**Exit criteria:** 100% of tests pass; `question_engine.py` importable without
side effects; no changes to `app.py`, `scorer.py`, or question files.

---

### Phase 1 — Shadow Mode

**Goal:** Validate that templates can reproduce the exact static questions
they replace, bit-for-bit.

| Task | Detail |
|------|--------|
| Write "frozen" templates | One template per static question, with `variables: []` and `expr` = literal value |
| `test_shadow.py` | For each static question, `instantiate(frozen_template)` must produce an identical dict (except `id` suffix and `template_id` key) |
| Shadow middleware in `app.py` | Behind `SHADOW_MODE=1` env flag: materialize templates alongside static questions, log any diff to stderr |

**Frozen template example** (for `fyxf04_grating_1`):

```python
{
    "template_id": "fyxf04_grating",
    "version": 1,
    "prompt_template": "En laser med våglängd $\\lambda = {{lambda_nm}}\\;\\text{nm}$ ...",
    "variables": [
        {"name": "lambda_nm", "kind": "int", "min": 633, "max": 633, "step": 1},
        {"name": "slits_per_mm", "kind": "choice", "pool": [500]},
        {"name": "order_m", "kind": "int", "min": 2, "max": 2, "step": 1}
    ],
    "answer_spec": { ... }
}
```

When min == max (or pool has one element), `_bind_variables` always picks the
same value — the original static value. This lets us validate rendering and
expression evaluation against known correct answers.

**Exit criteria:** 85/85 shadow tests pass. Zero diff in scored results between
static and shadow paths on a full quiz run.

---

### Phase 2 — Numeric Physics Subset (Pilot: Grating Family)

**Goal:** First real parameterized questions in production.

| Task | Detail |
|------|--------|
| Convert `fyxf04_grating_1` and `fyxf04_grating_2` to a single template `fyxf04_grating` | Open variable ranges (see §5.1) |
| Convert remaining `fyxf04_*` numeric questions | 21 questions → ~8–12 templates |
| Wire `app.py` to use templates for fyxf04 | `EXAM_SETS["fyxf04"]` reads from `templates_physics.py` |
| Keep static fallback | `FYXF04_QUESTIONS` still importable; feature flag `USE_TEMPLATES=1` |
| Tolerance regression test | For 1000 random instances of each template, verify `scorer._check_numeric` accepts `correct_answer ± tolerance` and rejects `correct_answer ± 2*tolerance` |

**Template file structure:**

```
templates_physics.py
├── FYXF04_TEMPLATES  (list[dict])
└── FYSIK12_TEMPLATES (list[dict])   ← Phase 3
```

**Exit criteria:** fyxf04 exam mode works entirely from templates. Manual
spot-check of 10 random instances confirms correct KaTeX rendering, correct
answer, and correct solution walkthrough.

---

### Phase 3 — Math Numeric + Simple MC

**Goal:** Convert MAXF02 (20 questions) and FYSIK12 (14 questions, mostly MC).

| Task | Detail |
|------|--------|
| `templates_math.py` with `MAXF02_TEMPLATES` | ~10–15 templates from 20 questions |
| `templates_physics.py` extended with `FYSIK12_TEMPLATES` | 14 MC questions → ~7–10 templates |
| MC choice shuffling (optional) | If enabled: shuffle choice order, remap correct letter. **Deferred** — see §4.4 |
| Decimal comma handling in math expressions | MAXF02 solutions use `{,}` extensively; validate rendering |

**Exit criteria:** All four exam modes (fyxf04, fysik12, maxf02, kexf01 partial)
work from templates. Shadow comparison still active for kexf01.

---

### Phase 4 — Chemistry Text Questions

**Goal:** Convert KEXF01 (30 questions) — the highest-risk set because it
includes `answer_type: "text"` (naming, formulas) alongside numeric.

| Task | Detail |
|------|--------|
| `templates_chemistry.py` with `KEXF01_TEMPLATES` | 30 questions → ~18–22 templates |
| Text-answer templates | `answer_spec.type = "text"`, `expr` returns a string from `variables.pool` |
| Compound-naming pool | Variable `kind: "choice"` with `pool: [{"formula": "NaCl", "name": "natriumklorid"}, ...]` |
| Remove static question files | Delete `questions_*.py`; `ALL_QUESTIONS` built from `instantiate()` calls |
| Remove shadow mode | Feature flag cleanup |

**Exit criteria:** `questions_*.py` files deleted. Full test suite passes.
`app.py` imports only from `templates_*.py` + `question_engine.py`.

---

## 4. Risk Analysis

### 4.1 KaTeX / LaTeX Brace Collision

**Problem:** KaTeX uses `{,}` as a thousands separator (e.g.,
`$2{,}00 \times 10^{-6}$`) and `\{`, `\}` for literal braces. The template
engine uses `{{var}}`. These could collide.

**Analysis of current question bank:**
- `{,}` appears in 50+ places across all question files (Swedish decimal comma).
- `\{` and `\}` appear in ~5 chemistry questions (set notation).
- `{{` never appears in current questions (no Jinja/Django).

**Mitigation:**
- The `_PLACEHOLDER_RE` regex `\{\{(\w+)(?::([^}]+))?\}\}` requires an
  alphanumeric character immediately after `{{`. The pattern `{,}` is `{` + `,`
  (non-word char), so it **cannot** match.
- `\{` is a single brace; the regex requires two consecutive `{`.
- **Conclusion: no collision.** But add an explicit test:
  `test_render_preserves_katex_braces()`.

### 4.2 Tolerance Fairness Under Rounding

**Problem:** When template variables are displayed rounded in the prompt
(e.g., `{{concentration:.4f}}`), the student works with the rounded value.
If `answer_spec.expr` uses the unrounded binding, the correct answer diverges
from what the student computes.

**Example:** Concentration = 0.000012345, displayed as `0{,}0000123`. Student
computes pH = 9.09. Engine computes pH from 0.000012345 = 9.0884. With
tolerance 0.02 (relative), the acceptance window is ±0.18, so both answers
pass — but only by luck.

**Mitigation:**
1. **Round-then-compute rule:** `_bind_variables` applies `dp` rounding to
   float variables *before* storing in bindings. All downstream computation
   uses the rounded value. This matches what the student sees.
2. **Display-precision metadata:** `rendering_hints.significant_figures` sets
   display rounding but does NOT affect computation. Only `variables[].dp`
   affects computation.
3. **Tolerance audit script:** `scripts/audit_tolerances.py` — for each
   template, sample 10,000 instances and report the min/max/mean
   `|answer_rounded - answer_exact|` / `|answer_exact|`. Flag any template
   where this ratio exceeds 50% of the tolerance.

### 4.3 Session Storage for Materialized Instances

**Problem:** Flask's cookie session is capped at 4 KB. A single materialized
question dict is ~400–800 bytes (JSON). 85 questions → 34–68 KB.

**Mitigation plan (phased):**

| Phase | Strategy | Session size |
|-------|----------|--------------|
| 0–2 | `flask-session` filesystem backend | N/A (server-side) |
| 3 | Evaluate: store `{template_id, seed}` per question + re-materialize on submit | ~2 KB for 85 questions |
| 4+ | Seed-based approach as default; filesystem as fallback for legacy | ~2 KB |

**Seed-based approach detail:**
```python
session["quiz_seed"] = 42
session["template_ids"] = ["fyxf04_grating", "kexf01_ph", ...]
# On submit:
rng = random.Random(session["quiz_seed"])
questions = [instantiate(TEMPLATE_LOOKUP[tid], rng) for tid in session["template_ids"]]
```
This requires that `instantiate` is **deterministic** given the same RNG state,
which it is by construction (no external I/O, no time-dependent logic).

### 4.4 MC Letter Stability After Choice Shuffling

**Problem:** If we shuffle MC choices for variety, the correct letter changes
per instance. The current scorer (`_check_multiple_choice`, `scorer.py:69`)
compares only the first character. If we shuffle, the correct letter stored in
`correct_answer` must match the shuffled order.

**Mitigation:**
1. **Phase 2–3: no shuffling.** Choices are always in the template-defined
   order. `correct_answer` is a fixed letter (e.g., `"B"`).
2. **Phase 4 (optional):** Implement `shuffle_choices(choices, correct_letter, rng)`:
   ```python
   def shuffle_choices(choices, correct_letter, rng):
       indexed = list(enumerate(choices))
       rng.shuffle(indexed)
       new_choices = [c for _, c in indexed]
       # Find where the originally-correct choice landed
       old_idx = ord(correct_letter.upper()) - ord("A")
       new_idx = next(i for i, (orig_i, _) in enumerate(indexed) if orig_i == old_idx)
       new_letter = chr(ord("A") + new_idx)
       # Re-label choices with new letters
       relabeled = [f"{chr(65+i)}) {c.split(')', 1)[1].strip()}" for i, c in enumerate(new_choices)]
       return relabeled, new_letter
   ```
3. **Scorer is already compatible:** it checks first character, so as long as
   `correct_answer` is updated to the new letter, scoring works.

### 4.5 Expression Security

**Problem:** `eval()` is inherently dangerous even with a restricted namespace.

**Mitigation:**
- `__builtins__` set to empty dict `{}` — blocks `__import__`, `exec`, `eval`,
  `open`, etc.
- Templates are authored by us (not user input) — attack surface is developer
  typos, not adversarial injection.
- Add an AST pre-check in `validate_template()`:
  ```python
  import ast
  tree = ast.parse(expr, mode="eval")
  for node in ast.walk(tree):
      if isinstance(node, (ast.Import, ast.ImportFrom, ast.Call)):
          if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
              if node.func.id not in SAFE_NAMESPACE:
                  raise ValueError(f"Disallowed function call: {node.func.id}")
  ```

### 4.6 Backward Compatibility During Migration

**Problem:** Existing sessions from before the migration will have
`question_ids` pointing to static question IDs. If we remove static questions,
those sessions break mid-quiz.

**Mitigation:**
- Keep `ALL_QUESTIONS` (static) importable through Phase 3.
- `submit_quiz` falls back to static lookup when `materialized_questions` is
  absent from session (see §2.7).
- On the cutover day (Phase 4), users with in-progress quizzes get a
  "quiz expired" message instead of a crash. Acceptable given quizzes take
  ~30 minutes.

---

## 5. Example Templates

### 5.1 `fyxf04_grating` — Numeric Physics (Diffraction Grating)

Merges current static questions `fyxf04_grating_1` (line 4, `questions_physics.py`)
and `fyxf04_grating_2` (line 28, `questions_physics.py`) into one template.

```python
FYXF04_GRATING_TEMPLATE = {
    "template_id": "fyxf04_grating",
    "version": 1,

    "prompt_template": (
        "En laser med våglängd $\\lambda = {{lambda_nm}}\\;\\text{nm}$ träffar ett "
        "diffraktionsgitter med ${{slits_per_mm}}$ spalter per mm. "
        "Bestäm diffraktionsvinkeln $\\theta$ för ordning $m = {{order_m}}$ maximum."
    ),

    "variables": [
        {
            "name": "lambda_nm",
            "kind": "int",
            "min": 400,
            "max": 700,
            "step": 1,
        },
        {
            "name": "slits_per_mm",
            "kind": "choice",
            "pool": [300, 500, 600, 800, 1000],
        },
        {
            "name": "order_m",
            "kind": "int",
            "min": 1,
            "max": 3,
            "step": 1,
        },
    ],

    "answer_spec": {
        "type": "numeric",
        "derived": {
            "d_m":     "1.0 / (slits_per_mm * 1e3)",
            "sin_val": "order_m * lambda_nm * 1e-9 / d_m",
        },
        "expr": "degrees(asin(sin_val))",
        "tolerance_spec": {
            "mode": "relative",
            "value": 0.02,
        },
        "unit": "°",
        # Constraint: sin_val must be in (-1, 1) for asin to be real.
        # The engine's rejection-resample loop handles this automatically
        # when asin raises ValueError or returns NaN.
    },

    "solution_template": (
        "Spaltavstånd $d = 1/({{slits_per_mm}}\\;\\text{mm}^{-1}) = {{d_m:.3e}}\\;\\text{m}$.\n"
        "Gitterekvationen: $d \\sin \\theta = m\\lambda$ "
        "$\\Rightarrow$ $\\sin \\theta = m\\lambda / d = {{sin_val:.4f}}$.\n"
        "Alltså $\\theta = \\arcsin({{sin_val:.3f}}) \\approx {{answer:.1f}}°$."
    ),

    "rendering_hints": {
        "decimal_comma": True,
        "katex": True,
        "significant_figures": None,
        "display_unit": "°",
    },

    "metadata": {
        "exam": "fyxf04",
        "topic": "diffraction_grating",
        "topic_display": "Diffraktionsgitter",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
    },
}
```

**Verification against original `fyxf04_grating_1`:**

| Field | Static (line 4) | Template with λ=633, slits=500, m=2 |
|-------|-----------------|--------------------------------------|
| `d_m` | — | `1/(500×1e3) = 2.0e-6` |
| `sin_val` | — | `2 × 633e-9 / 2e-6 = 0.633` |
| `answer` | 39.3 | `degrees(asin(0.633)) = 39.265...` ≈ 39.3 |
| `tolerance` | 0.02 (relative) | 0.02 (relative) |
| `unit` | `°` | `°` |

The acceptance window: `|user − 39.27| ≤ 0.02 × 39.27 = 0.785`. Original
correct_answer 39.3 falls within this window. ✓

**Constraint satisfaction:** Not all (λ, slits, m) combos are valid.
`sin_val > 1` ⇒ `asin` domain error. The resample loop catches this:
e.g., λ=700, slits=300, m=3 → sin_val = 3×700e-9/(1/300000) = 0.63 ✓,
but λ=700, slits=1000, m=2 → sin_val = 2×700e-9/(1/1e6) = 1.4 ✗ → resample.

---

### 5.2 `fysik12_mech_mc` — Multiple-Choice Mechanics (Newton's 2nd Law)

Converts `fysik12_mech_mc_1` (line 473, `questions_physics.py`).

```python
FYSIK12_MECH_MC_TEMPLATE = {
    "template_id": "fysik12_mech_mc_newton2",
    "version": 1,

    "prompt_template": (
        "En låda med massan ${{mass}}\\;\\text{kg}$ ligger på ett friktionsfritt "
        "horisontellt underlag och skjuts med en horisontell kraft på "
        "${{force}}\\;\\text{N}$. Vad blir accelerationen?"
    ),

    "variables": [
        {
            "name": "mass",
            "kind": "choice",
            "pool": [2, 3, 4, 5, 8, 10],
        },
        {
            "name": "force",
            "kind": "choice",
            "pool": [6, 10, 12, 15, 20, 24, 30, 40],
        },
    ],

    "answer_spec": {
        "type": "mc",
        "derived": {
            "a_correct": "force / mass",
        },
        "choices_template": [
            {
                "letter": "A",
                "expr":   "force / (2 * mass)",
                "label_template": "A) ${{val_A:.0f}}\\;\\text{m/s}^2$",
            },
            {
                "letter": "B",
                "expr":   "force / mass",
                "label_template": "B) ${{val_B:.0f}}\\;\\text{m/s}^2$",
            },
            {
                "letter": "C",
                "expr":   "force * 1",
                "label_template": "C) ${{val_C:.0f}}\\;\\text{m/s}^2$",
            },
            {
                "letter": "D",
                "expr":   "force * mass",
                "label_template": "D) ${{val_D:.0f}}\\;\\text{m/s}^2$",
            },
        ],
        "correct_letter_rule": "B",
        "tolerance_spec": None,
        "unit": None,
    },

    "solution_template": (
        "Newtons andra lag: $F = ma$ $\\Rightarrow$ "
        "$a = F/m = {{force}}\\;\\text{N} / {{mass}}\\;\\text{kg} "
        "= {{a_correct:.0f}}\\;\\text{m/s}^2$. Alternativ B."
    ),

    "rendering_hints": {
        "decimal_comma": False,
        "katex": True,
        "significant_figures": None,
        "display_unit": None,
    },

    "metadata": {
        "exam": "fysik12",
        "topic": "mechanics",
        "topic_display": "Mekanik",
        "points": 1,
        "exam_frequency": 1.0,
        "no_calculator": True,
    },
}
```

**Verification against original `fysik12_mech_mc_1`:**

| Field | Static (line 473) | Template with mass=2, force=10 |
|-------|-------------------|-------------------------------|
| Choice A | `$2\;\text{m/s}^2$` | `10/(2×2) = 2.5` → `$2\;\text{m/s}^2$` ✗ (rounds to 2 with :.0f) |

**Issue caught:** With `force=10, mass=2`, choice A = `10/4 = 2.5`, displayed
as `$2\;\text{m/s}^2$` due to `:.0f`. This collides with a plausible answer.

**Fix — add a constraint or use integer-clean pools:**

```python
# Constraint: all distractor expressions must produce distinct integers
# when evaluated with the chosen variables.
# Enforce by only allowing (force, mass) combos where force is divisible by mass
# and by 2*mass.
#
# Simpler: use a curated pool of (force, mass) pairs:
"variables": [
    {
        "name": "pair",
        "kind": "choice",
        "pool": [
            {"mass": 2, "force": 10},
            {"mass": 3, "force": 12},
            {"mass": 4, "force": 20},
            {"mass": 5, "force": 30},
            {"mass": 8, "force": 40},
            {"mass": 10, "force": 60},
        ],
    }
]
```

Or keep independent variables and add a `constraints` field:

```jsonc
"constraints": [
    "force % mass == 0",
    "force % (2 * mass) == 0",
    "force * mass != force / mass"  // D ≠ B
]
```

The engine's resample loop evaluates constraints and retries if any fail.
**Recommendation:** Use the `constraints` approach — it's more general and
keeps variable definitions simple.

**Updated schema addition — `constraints` field:**

```jsonc
{
  "template_id": "...",
  "constraints": [
    "sin_val < 1",                    // physics: asin domain
    "force % mass == 0",              // MC: integer-clean answers
    "val_A != val_B",                 // MC: distinct choices
    "val_C != val_B"
  ],
  // ...
}
```

Constraints are Python expressions evaluated in the same namespace as `expr`.
All must be truthy for the instance to be accepted. Failed constraints trigger
a resample (up to 100 attempts, then raise `TemplateConstraintError`).

---

### 5.3 `kexf01_ph_strong_base` — Numeric Chemistry (pH of NaOH)

Converts `kexf01_ph_1` (line 203, `questions_chemistry.py`).

```python
KEXF01_PH_STRONG_BASE_TEMPLATE = {
    "template_id": "kexf01_ph_strong_base",
    "version": 1,

    "prompt_template": (
        "Beräkna pH i en lösning av ${{conc_display}}\\;\\text{mol/dm}^3$ "
        "$\\text{{{compound}}}$."
    ),
    # Note: \\text{{{compound}}} — the outer {{ }} is the template placeholder,
    # the \text{} is KaTeX. This works because the regex matches {{compound}}
    # (word chars) and the surrounding \text{ } are literal braces.

    "variables": [
        {
            "name": "compound",
            "kind": "choice",
            "pool": ["NaOH", "KOH"],
        },
        {
            "name": "conc_exp",
            "kind": "int",
            "min": -6,
            "max": -3,
            "step": 1,
        },
        {
            "name": "conc_coeff",
            "kind": "float",
            "min": 1.0,
            "max": 9.0,
            "step": 0.1,
            "dp": 1,
        },
    ],

    "answer_spec": {
        "type": "numeric",
        "derived": {
            "conc":         "conc_coeff * 10 ** conc_exp",
            "poh":          "-log10(conc)",
            "ph":           "14 - poh",
            "conc_display": "conc_coeff * 10 ** conc_exp",
        },
        # conc_display is recomputed for display in the solution;
        # it equals conc but is available for solution_template formatting.
        "expr": "14 + log10(conc_coeff * 10 ** conc_exp)",
        "tolerance_spec": {
            "mode": "relative",
            "value": 0.02,
        },
        "unit": "",
    },

    "solution_template": (
        "$[\\text{OH}^-] = {{conc_coeff:.1f}} \\times 10^{ {{conc_exp}} }\\;\\text{mol/dm}^3$\n"
        "$\\text{pOH} = -\\log({{conc_coeff:.1f}} \\times 10^{ {{conc_exp}} }) \\approx {{poh:.2f}}$\n"
        "$\\text{pH} = 14 - \\text{pOH} \\approx {{answer:.2f}}$"
    ),

    "rendering_hints": {
        "decimal_comma": True,
        "katex": True,
        "significant_figures": 3,
        "display_unit": "",
    },

    "metadata": {
        "exam": "kexf01",
        "topic": "ph_berakningar",
        "topic_display": "pH-beräkningar",
        "points": 2,
        "exam_frequency": 1.0,
        "no_calculator": False,
    },
}
```

**Verification against original `kexf01_ph_1`:**

| Field | Static (line 203) | Template with compound=NaOH, coeff=1.2, exp=-5 |
|-------|-------------------|-------------------------------------------------|
| `conc` | `0.000012` | `1.2 × 10⁻⁵ = 0.000012` ✓ |
| `pOH` | `4.92` | `-log10(0.000012) = 4.9208` ✓ |
| `pH` | `9.08` | `14 - 4.9208 = 9.0792` ✓ |
| Tolerance | 0.02 relative | `0.02 × 9.08 = 0.182` — accepts 8.90–9.26 |
| `unit` | `""` | `""` ✓ |

**KaTeX brace analysis for this template:**

The prompt contains `$\\text{{{compound}}}$`. After template substitution:
- `{{compound}}` → `NaOH`
- Result: `$\text{NaOH}$` — valid KaTeX. ✓

The `{` before `compound` is the KaTeX `\text{` opener. The `}` after is the
KaTeX closer. The regex sees `{{compound}}` as a placeholder (word char
`c` after `{{`), and the surrounding single braces are left alone. ✓

**Additional pool expansion (future):** Add weak bases (`NH3` with Kb),
strong acids (`HCl`, `HNO3`). These would require different `expr` formulas,
so they become separate templates: `kexf01_ph_strong_acid`,
`kexf01_ph_weak_base`, etc.

---

## Appendix A: File-Level Migration Map

| Current file | Templates file | Phase |
|---|---|---|
| `questions_physics.py` (FYXF04_QUESTIONS, 21 questions) | `templates_physics.py` (FYXF04_TEMPLATES, ~10 templates) | 2 |
| `questions_physics.py` (FYSIK12_QUESTIONS, 14 questions) | `templates_physics.py` (FYSIK12_TEMPLATES, ~8 templates) | 3 |
| `questions_math.py` (MAXF02_QUESTIONS, 20 questions) | `templates_math.py` (MAXF02_TEMPLATES, ~12 templates) | 3 |
| `questions_chemistry.py` (KEXF01_QUESTIONS, 30 questions) | `templates_chemistry.py` (KEXF01_TEMPLATES, ~18 templates) | 4 |
| — | `question_engine.py` | 0 |
| — | `test_question_engine.py` | 0 |
| — | `test_shadow.py` | 1 |

**Estimated template count reduction:** 85 static questions → ~48 templates
(43% reduction), each generating unlimited unique instances.

## Appendix B: `scorer.py` Compatibility Checklist

Every function in `scorer.py` that touches question dicts — verified that the
template-generated dicts satisfy their contracts:

| Function (line) | Keys accessed | Template output provides | Status |
|---|---|---|---|
| `_question_points` (32) | `points` | `metadata.points` → `points` | ✓ |
| `_check_numeric` (42) | (args only) | N/A | ✓ |
| `_check_text` (63) | (args only) | N/A | ✓ |
| `_check_multiple_choice` (69) | (args only) | N/A | ✓ |
| `_answer_correct` (77) | `answer_type`, `correct_answer`, `tolerance` | All present | ✓ |
| `_question_id` (88) | `id`, `question_id` | `id` = instance_id | ✓ |
| `score_answers` (96) | `id`, `points`, `answer_type`, `correct_answer`, `tolerance`, `topic`, `topic_display` | All present | ✓ |
| `_exam_name` (172) | `exam` | `metadata.exam` → `exam` | ✓ |
| `_exam_frequency` (180) | `exam_frequency` | `metadata.exam_frequency` → `exam_frequency` | ✓ |
| `generate_diagnostic` (190) | all of the above | All present | ✓ |

**Zero changes needed in `scorer.py`.**

## Appendix C: `app.py` Change Summary

| Location | Current code | Required change | Phase |
|---|---|---|---|
| Line 14–16 (imports) | `from questions_physics import ...` | Add `from templates_physics import ...` | 2 |
| Line 22–24 (ALL_QUESTIONS) | Static concatenation | Conditional: templates + `instantiate()` or static | 2 |
| Line 57–79 (start_quiz) | `list(EXAM_SETS[mode])` | Materialize templates via `instantiate()` | 2 |
| Line 82 (submit_quiz) | `q_lookup` from ALL_QUESTIONS | Read from `session["materialized_questions"]` | 2 |
| Line 82 (submit_quiz) | Cookie session | Server-side session (flask-session) | 0 |
| Line 113–142 (explain) | Static q_lookup | Materialized q_lookup from session | 2 |

## Appendix D: Dependency Additions

| Package | Version | Purpose | Phase |
|---|---|---|---|
| `flask-session` | `>=0.8` | Server-side session storage | 0 |
| `pytest` | `>=8.0` (dev) | Unit tests for question_engine | 0 |
