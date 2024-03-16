# [⎗](./README.md) Procedure - Original Reference

## What components does it consist of?

Let's see [the description](https://github.com/graphdeco-inria/gaussian-splatting/?tab=readme-ov-file#overview) excerpted from the original manual:

> The codebase has 4 main components:
>
> - A PyTorch-based optimizer to produce a 3D Gaussian model from SfM inputs.
>
> - A network viewer that allows to connect to and visualize the optimization process.
>
> - An OpenGL-based real-time viewer to render trained models in real-time.
>
> - A script to help you turn your own images into optimization-ready SfM data sets.

Let's explain each of them in detail.

## Contents

- [Preprocessing](#preprocessing)
- [Loading](#loading)
- [Training](#training)
- [Evaluation](#evaluation)
- [Rendering](#rendering)
- [Extras](#extras)

## Preprocessing

> A script to help you turn your own images into optimization-ready SfM data sets.

Let's check out their repository. They've [told](https://github.com/graphdeco-inria/gaussian-splatting/?tab=readme-ov-file#processing-your-own-scenes) us to use [`COLMAP`](https://colmap.github.io/) and [`./convert.py`](https://github.com/graphdeco-inria/gaussian-splatting/blob/main/convert.py) to **process your own scenes**.

The repository structure looks like this now:

```plaintext
./
|- convert.py
```

## Loading

After preprocessing and before training, we need to load the data and initialize the model.

Where does loading process happen? Let's check out their modules.

This is the dependency graph of loader modules, where we can see that `colmap_loader` is the base loader:

```mermaid
graph RL
  dataset_readers --> colmap_loader
  render --> scene
  train --> scene
  scene --> dataset_readers
```

## Training

## Evaluation

## Rendering

## Extras

### Call Tree in Python modules

1. All items from [`diff_gaussian_rasterization`](https://github.com/graphdeco-inria/diff-gaussian-rasterization)
```mermaid
graph RL
  subgraph diff_gaussian_rasterization
    GaussianRasterizationSettings
    GaussianRasterizer
    _RasterizeGaussians
    rasterize_gaussians
  end
  subgraph diff_gaussian_rasterization._C
    mark_visible
    rasterize_gaussians_c[rasterize_gaussians]
    rasterize_gaussians_c_backward[rasterize_gaussians_backward]
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

  render_main --> render_sets
  render_sets --> render_set
  render_set --> render_function

  training --> render_function
  train_main --> training

  _RasterizeGaussians --> rasterize_gaussians_c
  _RasterizeGaussians --> rasterize_gaussians_c_backward
  rasterize_gaussians --> _RasterizeGaussians
  GaussianRasterizer --> rasterize_gaussians
  GaussianRasterizer --> mark_visible
```

2. All items from [`simple_knn`](https://gitlab.inria.fr/bkerbl/simple-knn)
```mermaid
graph RL
  subgraph simple_knn._C
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

---

### Call Tree in CUDA C++ modules

1. All items from [`diff_gaussian_rasterization`](https://github.com/graphdeco-inria/diff-gaussian-rasterization)
```mermaid
graph RL
  subgraph cuda_rasterizer/auxiliary.h
    ndc2Pix
    getRect
    transformPoint4x3
    transformPoint4x4
    transformVec4x3
    transformVec4x3Transpose
    dnormvdz
    dnormvdv
    sigmoid
    in_frustum
  end
  subgraph cuda_rasterizer/forward
    computeColorFromSH_f[computeColorFromSH]
    computeCov2D_f[computeCov2D]
    computeCov3D_f[computeCov3D]
    preprocessCUDA_f[preprocessCUDA]
    preprocess_f[preprocess]
    renderCUDA_f[renderCUDA]
    render_f[render]
  end
  subgraph cuda_rasterizer/backward
    computeColorFromSH_b[computeColorFromSH]
    computeCov2D_b[computeCov2DCUDA]
    computeCov3D_b[computeCov3D]
    preprocessCUDA_b[preprocessCUDA]
    preprocess_b[preprocess]
    renderCUDA_b[renderCUDA]
    render_b[render]
  end
  subgraph cuda_rasterizer/rasterizer_impl
    backward
    checkFrustum
    duplicateWithKeys
    BinningState::fromChunk
    GeometryState::fromChunk
    ImageState::fromChunk
    getHigherMsb
    identifyTileRanges
    markVisible_cuda[markVisible]
    forward
    obtain
    required
  end
  subgraph rasterize_points
    resizeFunctional
    RasterizeGaussiansCUDA
    RasterizeGaussiansBackwardCUDA
    markVisible
  end

  computeCov2D_b --> transformPoint4x3

  preprocessCUDA_b --> transformPoint4x4
  in_frustum --> transformPoint4x4
  in_frustum --> transformPoint4x3

  computeColorFromSH_b --> dnormvdv

  computeCov2D_b --> transformVec4x3Transpose

  preprocessCUDA_b --> computeCov3D_b
  preprocessCUDA_b --> computeColorFromSH_b
  preprocess_b --> preprocessCUDA_b
  preprocess_b --> computeCov2D_b
 
  render_b --> renderCUDA_b

  computeCov2D_f --> transformPoint4x3

  preprocessCUDA_f --> transformPoint4x4
  preprocessCUDA_f --> computeCov3D_f
  preprocessCUDA_f --> computeCov2D_f
  preprocessCUDA_f --> ndc2Pix
  preprocessCUDA_f --> computeColorFromSH_f
  preprocess_f --> preprocessCUDA_f

  render_f --> renderCUDA_f

  checkFrustum --> in_frustum
  duplicateWithKeys --> getRect
  markVisible_cuda --> checkFrustum

  BinningState::fromChunk --> obtain
  GeometryState::fromChunk --> obtain
  ImageState::fromChunk --> obtain

  forward --> required
  backward --> GeometryState::fromChunk
  forward --> GeometryState::fromChunk
  backward --> ImageState::fromChunk
  forward --> ImageState::fromChunk
  forward --> preprocess_f
  backward --> BinningState::fromChunk
  forward --> BinningState::fromChunk
  forward --> duplicateWithKeys
  forward --> getHigherMsb
  forward --> render_f

  backward --> render_b
  backward --> preprocess_b

  RasterizeGaussiansCUDA --> resizeFunctional
  RasterizeGaussiansCUDA --> forward

  RasterizeGaussiansBackwardCUDA --> backward

  markVisible --> markVisible_cuda
```

2. All items from [`simple_knn`](https://gitlab.inria.fr/bkerbl/simple-knn)
```mermaid
graph RL
  subgraph simple_knn
    knn[SimpleKNN::knn]
    boxMeanDist
    boxMinMax
    CustomMin
    CustomMax
    coord2Morton
    distBoxPoint
    prepMorton
    updateKBest
  end
  subgraph spatial
    distCUDA2
  end

  boxMeanDist --> distBoxPoint
  boxMeanDist --> updateKBest

  coord2Morton --> prepMorton

  distCUDA2 --> knn

  knn --> boxMeanDist
  knn --> boxMinMax
  knn --> CustomMin
  knn --> CustomMax
  knn --> coord2Morton
```
