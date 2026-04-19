# fx-9860GIII g1e rendering (e-ACT)

## Facts

1. **Raw Eact** tokens such as `\subn;` or `\subs0;` may appear **literally** on the device if passed through unchanged.
2. **Unicode Latin subscript letters** (U+209x, U+1D62–U+1D65) are often **not drawn**; the base letter can appear alone (looks like missing notation).
3. **Unicode subscript digits** (₀–₉, U+2080–U+2089) generally **display**; `\subs0;` … `\subs9;` are normalized to these in the g1e path.
4. **ASCII `_tag`** after a symbol (e.g. `f_o`, `v_k`, `E_res`) is the reliable fallback for letter subscripts in **g1e** output.

## Pipeline

Source `SECTIONS` in `generate_eam_g2e.py` stays in **Eact** form. Only **`build_eam(..., fmt="g1e")`** runs `normalize_calculator_export()` before EactMaker. **g2e** is unchanged Eact.

See `PLAN_G1E_AGENTS.md` for the eight-area checklist.
