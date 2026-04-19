# Deep Formula Audit

Date: 2026-04-19

## Scope

Audited layers:
- source text banks: `*.txt`
- generator and alternate viewer: `generate_eam_g2e.py`, `FORMLER.py`
- render-safe outputs: `eam_g2e/`, `g1e_fixed/`, `g2e_fixed/`

Excluded from the passing audit:
- `backups/` snapshots
- legacy `eam/` wrappers generated directly from plain TXT

## Fixed issue families

1. Ambiguous semantic subscripts such as `\submi;`
   - Replaced with explicit, render-safe forms such as `\subm;`, `\submax;`, `\submin;`, `\subhal;`, and `\subres;`.

2. Compound level indices in `MODERN`
   - Source: `E = |E(n1) - E(n2)|`
   - Render-safe EAM: `E = |E(n\subs1;) \minus; E(n\subs2;)|`

3. Merged math-function tokens
   - Fixed cases such as `dsin(...)` and `Asin(...)` by inserting explicit multiplication.

4. Unsupported subscript letters
   - Removed remaining unsupported output tokens such as `\subc;`, `\subb;`, `\subg;`, and `\subB;` from the authoritative generator/output path.

5. Semantic label drift
   - Normalized refraction labels to `i/r/k`.
   - Restored force formulas so unsupported labels do not leak into calculator output.
   - Expanded efficiency notation to `\eta = E_n/E_t = P_n/P_t`.

## Eight-area g1e plan (agents)

See `PLAN_G1E_AGENTS.md` for the mapping to Cursor sub-agents, `G1E_RENDERING.md`, `EACTMAKER.md`, and `deploy_g1e_to_usb.sh`.

## Current notation conventions

- `max` and `min` stay explicit when the letters are renderable: `\submax;`, `\submin;`
- half-life / half-thickness use `\subhal;`
- resultant force uses `\subres;`
- RMS-like AC peak formulas use `\submax;` on the source amplitude
- Schwarzschild radius uses `r\subs;` in render-safe output and `r_S` in plain source text
- unsupported semantic labels fall back to a plain symbol when the surrounding label already gives meaning

## Verification run

Commands run successfully:

```bash
python3 formula_audit.py --tree /home/maxandersson/exam-tester/casio
python3 -m py_compile /home/maxandersson/exam-tester/casio/*.py
python3 /home/maxandersson/exam-tester/casio/test_formula_audit.py
python3 /home/maxandersson/exam-tester/casio/generate_eam_g2e.py --convert --formats both
```

Audit status: `OK`
