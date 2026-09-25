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
scale = 2401
scaled_reference = 576480.1
scaled_candidate = 576480.10000013841287201003323293056960897922662976311591231380612413054654485040
scaled_residual = 1.3841287201003323293056960897922662976311591231380612413054654485040E-7
reconstructed_delta_T = 1.0000000000000000000000000000000000000000000000000000000000000000000E-15 s
```

The test suite verifies:

1. substitution back into the defining equation;
2. the expected candidate-frequency prefix;
3. positivity of the frequency increment;
4. the exact scaled reference \(2401\times240.1=576480.1\);
5. the expected scaled-candidate prefix;
6. consistency of the scaled residual with \(2401\Delta f\) within Decimal working precision.

No experimental data are used.

Because finite-precision decimal arithmetic rounds intermediate operations, two algebraically identical evaluation orders can differ in their final least-significant working digits. The tests therefore use a precision-aware tolerance for the residual identity.
