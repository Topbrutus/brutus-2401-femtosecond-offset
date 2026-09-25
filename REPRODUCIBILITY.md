# Reproducibility

The reference calculation uses Python's standard-library `decimal.Decimal` with 80 decimal digits of working precision.

Run:

```bash
python calculation/calculate.py
```

Expected leading output:

```text
f0 = 240.1 Hz
delta_T = 1E-15 s
f = 240.10000000005764801000001384128720100332329305696089792266297631159123138061241 Hz
delta_f = 5.764801000001384128720100332329305696089792266297631159123138061241E-11 Hz
```

The test suite verifies:

1. substitution back into the defining equation;
2. the expected numerical prefix;
3. positivity of the frequency increment.

No experimental data are used.
