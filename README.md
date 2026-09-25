# 240.1 Hz Femtosecond Period-Offset Construction

A minimal, reproducible repository for one mathematical construction:

$$\frac{1}{240.1}-\frac{1}{f}=10^{-15}\ \mathrm{s}$$

which gives

$$f=\frac{1}{\frac{1}{240.1}-10^{-15}}$$

and, at high decimal precision,

$$f\approx240.1000000000576480100000138412872\ \mathrm{Hz}.$$

The corresponding frequency offset is

$$\Delta f=f-240.1\approx5.764801000001384\times10^{-11}\ \mathrm{Hz}.$$

## Scientific status

- **SOURCE:** mathematical construction.
- **HYPOTHESIS:** the period difference is fixed at exactly 1 femtosecond.
- **CALCULATION:** algebraically defined and numerically reproducible.
- **CANDIDATE VALUE:** the frequency above follows from the stated hypothesis.
- **PHYSICAL INTERPRETATION:** not established by this repository and requires experiment.

This repository makes no claim that the offset is a measured resonance, a biological effect, or a new physical constant.
## Reproduce

Requires Python 3.10+ and no third-party packages.

```bash
python calculation/calculate.py
python -m unittest discover -s tests -v
```

## Contents

- `FORMULA.md` — definitions and core equation.
- `DERIVATION.md` — exact algebra and approximation check.
- `REPRODUCIBILITY.md` — numerical method and expected output.
- `STATUS.md` — claim boundaries.
- `calculation/calculate.py` — 80-digit Decimal calculation.
- `tests/test_formula.py` — invariant and regression checks.
- `figures/formula.svg` — compact visual summary.
- `.zenodo.json` — Zenodo GitHub-release metadata.
- `CITATION.cff` — citation metadata for GitHub.

## Version

Initial scientific snapshot: **v1.0.0**, 2026-09-25.

## License

MIT License. See `LICENSE`.

Repository: https://github.com/Topbrutus/brutus-2401-femtosecond-offset
