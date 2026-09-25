# Formula

Let

- \(f_0 = 240.1\ \mathrm{Hz}\) be the reference frequency;
- \(T_0 = 1/f_0\) be its period;
- \(\delta T = 10^{-15}\ \mathrm{s}\) be the imposed period offset;
- \(f\) be the candidate frequency;
- \(N=2401\) be a dimensionless scale factor used for the v2 propagation check.

The construction is

\[
T_0-\frac{1}{f}=\delta T.
\]

Therefore

\[
\boxed{f=\frac{1}{\frac{1}{f_0}-\delta T}}
\]

or equivalently

\[
\boxed{f=\frac{f_0}{1-f_0\delta T}}.
\]

For \(f_0=240.1\ \mathrm{Hz}\) and \(\delta T=1\ \mathrm{fs}\),

\[
\boxed{f\approx240.1000000000576480100000138412872\ \mathrm{Hz}}
\]

and

\[
\boxed{\Delta f=f-f_0
\approx5.76480100000138412872\times10^{-11}\ \mathrm{Hz}}.
\]

## Scaled propagation

Multiplication by \(N=2401\) gives

\[
\boxed{Nf_0=576480.1}
\]

and

\[
\boxed{
Nf\approx576480.1000001384128720100332329305696
}.
\]

Therefore

\[
\boxed{
N\Delta f
\approx1.3841287201003323293\times10^{-7}
}.
\]

The scaled residual is not an additional fitted term: algebraically,

\[
N(f-f_0)=Nf-Nf_0.
\]
