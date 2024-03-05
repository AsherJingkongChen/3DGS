# Entities

## Why 3DGS?

3DGS is a brand-new approach of 3D scene representation, and it is super fast on rendering.

Related works of 3DGS are:

1. Neural Rendering and Radiance Fields
2. Point-Based Rendering and Radiance Fields

## Overview of 3DGS

3D Gaussians are basically projective transformations of static points.

You train a 3D Gaussian model from Structure from Motion (SfM) inputs, and then you can render the trained model by giving it a camera pose.

## What components do 3DGS consist of?

Let's see the original paper:

> The codebase has 4 main components:

> - A PyTorch-based optimizer to produce a 3D Gaussian model from SfM inputs. (Train)

> - A network viewer that allows to connect to and visualize the optimization process. (Log)

> - An OpenGL-based real-time viewer to render trained models in real-time. (Render)

> - A script to help you turn your own images into optimization-ready SfM data sets. (Preprocess)

Let's explain each of them in detail later.
