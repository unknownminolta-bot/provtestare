# EactMaker converter (planet-casio)

## Endpoint

- URL: `https://tools.planet-casio.com/EactMaker/system/converter.php`
- Method: POST, `application/x-www-form-urlencoded`

## Form fields (see `convert_via_eactmaker` in `generate_eam_g2e.py`)

| Field        | Role |
|-------------|------|
| `titre`     | Section title |
| `format`    | `g2e` or `g1e` |
| `texte`     | Body only (after the third `\x1e` in the `.eam` line) |
| `additional`| Empty string |
| `font`      | Empty |
| `password`  | Empty |

## Headers

- `Referer: https://tools.planet-casio.com/EactMaker/`

## Health checks

- Response size under ~100 bytes is usually an error page, not a calculator file.
- Timeout is set to **30 s** in code; slow networks may need a one-off retry.

## Local rebuild

```bash
cd casio
python3 generate_eam_g2e.py --convert --formats both
```

Outputs go to `g1e_fixed/` and `g2e_fixed/` (gitignored binaries; regenerate as needed).
