# [⎗](./README.md) Algorithm - Original Reference

## Contents

1. Color: C(N)
- Equation 2
- Equation 3
- Equation 4

## Algorithm 1

1. Density: `d(i)`
2. Interval: `v(i)`
3. Color of each point: `c(i)`
5. Alpha: `a(i) = (1 - exp(d(i) * v(i)))`
4. Transmittance: `T(i) = prod(1 <= j <= i - 1)(1 - a(j))`
6. Color: `C(N) = sum(1 <= i <= N)(T(i) * a(i) * c(i))`

Adapted from point-based alpha-blending image formation model.

Specifically, the color `C` of pixel is determined by the sum of the color `c` of each point, weighted by the transmittance `T` and the alpha `a`.

The alpha `a` is given by evaluating a 2D Gaussian with covariance `S` multiplied with a learned per-point opacity.

### References

1. [Kopanas. 2022. Neural Point Catacaustics for Novel-View Synthesis of Reflections](https://www-sop.inria.fr/reves/Basilic/2022/KLRJD22/neural-catacaustics_small.pdf)
2. [YiFan et al. 2019. Differentiable Surface Splatting for Point-based Geometry Processing](https://igl.ethz.ch/projects/differentiable-surface-splatting/DSS-2019-SA-Yifan-etal.pdf)

## Equation 2

This is the second equation.

## Equation 3

This is the third equation.

## Equation 4

This is the fourth equation.
