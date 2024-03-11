# [⎗](./README.md) Introduction - Original Reference

> [The main reference](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)

## Why 3D Gaussian Splatting?

3DGS is a brand-new approach of 3D scene representation, and it is super fast on rendering.

Related works of 3D Gaussian Splatting are:

1. Neural Rendering and Radiance Fields
2. Point-Based Rendering and Radiance Fields

## Overview of 3D Gaussian Splatting

3DGS utilizes a differentiable rasterizer to facilitate real-time projection into the image space.

The models are a set of ellipsoid with color and opacity.

Once you have trained models, you can view rendered images by providing camera poses.

## Be aware of

- The main reference is non-commercial.
- The implementation of main reference is memory-consuming on training.
