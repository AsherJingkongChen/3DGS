# Introduction

## Why 3DGS?

- [3DGS Original Project Home Page](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)

3DGS is a brand-new approach of 3D scene representation, and it is super fast on rendering.

Related works of 3DGS are:

1. Neural Rendering and Radiance Fields
2. Point-Based Rendering and Radiance Fields

## Overview of 3DGS

3D Gaussians are basically projective transformations of static points.

You train a 3D Gaussian model from Structure from Motion (SfM) inputs, and then you can render the trained model by giving it a camera pose.