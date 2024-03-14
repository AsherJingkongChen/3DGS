# [⎗](./README.md) Implementation - Original Reference

## Contents

- [External Dependencies](#external-dependencies)
- [Torch](#torch)
- [GPU Programming](#gpu-programming)
- [Torch Extension](#torch-extension)

## External Dependencies

The following external dependencies are required to fully evaluate the project:

- diff_gaussian_rasterization
- lpipsPyTorch
- numpy
- Pillow
- plyfile
- simple_knn
- torch
- torchvision

## Torch

The project heavily relies on PyTorch and its ecosystem.

## GPU Programming

Some parts of the training process of 3D Gaussians is written in CUDA C++ to make use of NVIDIA GPU's parallelized computation.

## Torch Extension

The project uses a custom PyTorch extension to accelerate the computation of Gaussian splatting. Specifically, it uses `diff_gaussian_rasterization` to render Gaussian splats and `simple_knn` to initialize from Point Cloud data.

### Call Tree in Python modules

1. All items from `diff_gaussian_rasterization`
```mermaid
graph TD
  subgraph diff_gaussian_rasterization
    GaussianRasterizer
    GaussianRasterizationSettings
  end
  subgraph gaussian_renderer
    render_function[render]
  end
  subgraph render
    render_set
    render_sets
    render_main[__main__]
  end
  subgraph train
    training
    train_main[__main__]
  end

  render_function --> GaussianRasterizer
  render_function --> GaussianRasterizationSettings
  render_set --> render_function
  render_sets --> render_set
  render_main --> render_sets
  training --> render_function
  train_main --> training
```

2. All items from `simple_knn`
```mermaid
graph TD
  subgraph simple_knn
    distCUDA2
  end
  subgraph gaussian_model
    gm_cfd[GaussianModel.create_from_pcd]
  end
  subgraph scene.__init__
    scene[Scene.__init__]
  end
  subgraph train
    training
    train_main[__main__]
  end

  gm_cfd --> distCUDA2
  scene --> gm_cfd
  training --> scene
  train_main --> training
```
