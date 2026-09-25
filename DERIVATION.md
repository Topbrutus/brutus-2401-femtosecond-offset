# Derivation

Start from

$$\frac{1}{f_0}-\frac{1}{f}=\delta T.$$

Move the unknown-period term:

$$\frac{1}{f}=\frac{1}{f_0}-\delta T.$$

Invert both sides:

$$f=\frac{1}{\frac{1}{f_0}-\delta T}.$$

Equivalently,

$$f=\frac{f_0}{1-f_0\delta T}.$$

Hence the exact frequency increment is

$$\Delta f=f-f_0=\frac{f_0^2\delta T}{1-f_0\delta T}.$$

Because $f_0\delta T=2.401\times10^{-13}\ll1$, the first-order check is

$$\Delta f\approx f_0^2\delta T=(240.1)^2\times10^{-15}=5.764801\times10^{-11}\ \mathrm{Hz}.$$

The first-order value agrees with the leading digits of the exact calculation.
