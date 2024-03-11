# [⎗](./README.md) Introduction - Original Reference

> [The main reference](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)

## Why 3D Gaussian Splatting?

3DGS is a brand-new approach of 3D scene representation, and it is super fast on rendering.

Related works of 3D Gaussian Splatting are:

1. Neural Rendering and Radiance Fields
2. Point-Based Rendering and Radiance Fields

## Overview of 3D Gaussian Splatting

3D Gaussians are a set of ellipsoids with different color and opacity. Unlike neural networks in NeRF, the model is a explicit representation of the scene.

Once you have trained models, you can render images from certain viewpoints by anisotropic volumetric "splatting" of 3D Gaussians onto a 2D plane.

## Be aware of

- The main reference is non-commercial.
- The implementation of main reference is memory-consuming on training.
