# g1e plan — eight agent areas (implemented)

Each row maps a **Cursor sub-agent** (`~/.dotfiles/cursor/agents/casio-*.md`) to **repo artifacts** in `exam-tester/casio/`.

| # | Agent | Implementation |
|---|--------|------------------|
| 1 | `casio-fx-g1e-rendering` | `G1E_RENDERING.md` — device rules (raw Eact, Unicode letters vs digits, ASCII `_tag`). |
| 2 | `casio-normalize-subscripts` | `normalize_eam_subscripts.py` — `normalize_calculator_export()` for g1e; `normalize_eam_text()` for other workflows. |
| 3 | `casio-generator-eam` | `generate_eam_g2e.py` — `SECTIONS`, `build_eam()`, `convert_via_eactmaker()`. |
| 4 | `casio-formula-audit-sync` | `formula_audit.py` — audits **raw** Eact in SECTIONS; must stay aligned with generator. |
| 5 | `casio-eactmaker-export` | `EACTMAKER.md` + POST implementation in `generate_eam_g2e.py`. |
| 6 | `casio-usb-deploy` | `deploy_g1e_to_usb.sh` — find `LABEL=CASIO`, copy `g1e_fixed/*.g1e`, `sha256sum`, `sync`, `umount`. |
| 7 | `casio-regression-suite` | `test_formula_audit.py` — run `python3 test_formula_audit.py` after changes. |
| 8 | `casio-notation-edge-cases` | Tests for Doppler (`f_o`, `_k \\frac`), `F\subs;s` → `F_s s`, multi-char `_res` / `_max`. |

## Regenerate and deploy

```bash
python3 generate_eam_g2e.py --convert --formats both
./deploy_g1e_to_usb.sh    # when USB is connected
```
