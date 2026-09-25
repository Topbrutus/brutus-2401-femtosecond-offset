# 240.1 Hz Femtosecond Period-Offset Construction

A small, reproducible mathematical repository built around the exact relation

\[
\frac{1}{240.1}-\frac{1}{f}=10^{-15}\ \mathrm{s},
\]

which gives

\[
f=\frac{1}{\frac{1}{240.1}-10^{-15}}
=\frac{240.1}{1-240.1\times10^{-15}}.
\]

At high decimal precision,

\[
f\approx240.1000000000576480100000138412872\ \mathrm{Hz},
\]

so the residual relative to the reference value is

\[
\Delta f=f-240.1
\approx5.76480100000138412872\times10^{-11}\ \mathrm{Hz}.
\]

## Version 2: residual propagation

Version 2.0.0 makes explicit a consequence that was present in the original equation but was not separately documented in v1.

For the dimensionless scale factor

\[
N=2401,
\]

the reference value is

\[
Nf_0=2401\times240.1=576480.1,
\]

while the exact scaled candidate is

\[
Nf
\approx576480.1000001384128720100332329305696.
\]

Therefore the scaled residual is

\[
N\Delta f
\approx1.3841287201003323293\times10^{-7}.
\]

This is not introduced as a new independent correction. It is the same residual propagated through multiplication by 2401.

See `RESIDUAL_PROPAGATION.md` for the derivation and interpretation boundary.

## Scientific status

- **SOURCE:** mathematical construction.
- **HYPOTHESIS:** the period difference is fixed at exactly 1 femtosecond.
- **CALCULATION:** algebraically defined and numerically reproducible.
- **CANDIDATE VALUE:** the frequency follows from the stated hypothesis.
- **RESIDUAL PROPAGATION:** deterministic consequence of the same equation and chosen scale factor.
- **PHYSICAL INTERPRETATION:** not established by this repository and requires experiment.

This repository makes no claim that the offset is a measured resonance, a biological effect, a new physical constant, or evidence of a connection to the Brout-Englert-Higgs boson.

## Reproduce

Requires Python 3.10+ and no third-party packages.

```bash
python calculation/calculate.py
python -m unittest discover -s tests -v
```

## Contents

- `FORMULA.md` — definitions and core equation.
- `DERIVATION.md` — exact algebra and series structure.
- `RESIDUAL_PROPAGATION.md` — v2 scaled-residual derivation.
- `REPRODUCIBILITY.md` — numerical method and expected output.
- `STATUS.md` — claim boundaries.
- `RELEASE_NOTES_v2.0.0.md` — what changed and why.
- `calculation/calculate.py` — high-precision Decimal calculation.
- `tests/test_formula.py` — invariant and regression checks.
- `figures/formula.svg` — compact visual summary.
- `.zenodo.json` — Zenodo GitHub-release metadata.
- `CITATION.cff` — citation metadata for GitHub.

## Version

Current scientific snapshot: **v2.0.0**, 2026-09-25.

The original **v1.0.0** remains the immutable first archived snapshot.

## License

MIT License. See `LICENSE`.

Repository: https://github.com/Topbrutus/brutus-2401-femtosecond-offset
