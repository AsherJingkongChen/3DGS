# [⎗](./README.md) Introduction - Original Reference

> [The main reference](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)

## Why 3D Gaussian Splatting?

3DGS is a brand-new approach of 3D scene representation, and it is super fast on rendering.

Related works of 3D Gaussian Splatting are:

1. Neural Rendering and Radiance Fields
2. Point-Based Rendering and Radiance Fields

## Overview of 3D Gaussian Splatting

3D Gaussians are projective transformations of static points. It's a sort of explicit representation of volumetric data.

First, You train a 3D Gaussian model from Structure from Motion (SfM) inputs, and then you can render the trained model by giving it camera poses.

## Be aware of

- The main reference is non-commercial.
- The implementation of main reference is memory-consuming on training.
