# [⎗](./README.md) Dependency - Original Reference

- The curcial modules are: `arguments` and `gaussian_renderer`
- The feature modules are: `render` and `train`

```mermaid
flowchart RL
  subgraph External
    diff_gaussian_rasterization([diff_gaussian_rasterization - CUDA])
    lpipsPyTorch([lpipsPyTorch])
    numpy([numpy])
    Pillow([Pillow - PIL])
    plyfile([plyfile])
    pymeshlab([pymeshlab])
    scipy([scipy])
    simple_knn([simple_knn - CUDA])
    torch([torch])
    torchvision([torchvision])
  end
  subgraph Utilities
    utils
    camera_utils
    general_utils
    graphics_utils
    image_utils
    loss_utils
    sh_utils
    system_utils
  end
  subgraph Arguments
    arguments
  end
  subgraph Scene
    scene
    cameras
    colmap_loader
    dataset_readers
    gaussian_model
  end
  subgraph Metrics
    metrics
  end
  subgraph Render
    gaussian_renderer
    network_gui
    render
  end
  subgraph Train
    train
  end
  subgraph Evaluation
    full_eval
  end

  subgraph Utilities
    utils --> camera_utils
    utils --> general_utils
    utils --> graphics_utils
    utils --> image_utils
    utils --> loss_utils
    utils --> sh_utils
    utils --> system_utils

    camera_utils -.-> numpy
    camera_utils --> general_utils
    camera_utils --> graphics_utils
    camera_utils --> cameras

    general_utils -.-> torch
    general_utils -.-> numpy

    graphics_utils -.-> torch
    graphics_utils -.-> numpy

    image_utils -.-> torch

    loss_utils -.-> torch
  end
  subgraph Scene
    scene --> arguments
    scene --> utils
    scene --> dataset_readers
    scene --> gaussian_model
    scene --> utils

    cameras -.-> torch
    cameras -.-> numpy
    cameras --> utils

    colmap_loader -.-> numpy

    dataset_readers -.-> Pillow
    dataset_readers --> colmap_loader
    dataset_readers --> gaussian_model
    dataset_readers --> utils
    dataset_readers -.-> numpy
    dataset_readers -.-> plyfile

    gaussian_model --> utils
    gaussian_model -.-> torch
    gaussian_model -.-> numpy
    gaussian_model -.-> simple_knn
    gaussian_model -.-> plyfile
  end
  subgraph Metrics
    metrics -.-> lpipsPyTorch
    metrics -.-> Pillow
    metrics -.-> torch
    metrics -.-> torchvision
    metrics --> utils
  end
    subgraph Render
    gaussian_renderer -.-> diff_gaussian_rasterization
    gaussian_renderer -.-> torch
    gaussian_renderer --> utils
    gaussian_renderer --> gaussian_model

    network_gui -.-> torch
    network_gui --> cameras

    render -.-> torchvision
    render -.-> torch
    render --> utils
    render --> gaussian_model
    render --> gaussian_renderer
    render --> arguments
    render --> scene
  end
  subgraph Train
    train --> gaussian_renderer
    train --> network_gui
    train --> arguments
    train -.-> torch
    train --> utils
    train --> scene
    train --> gaussian_model
  end
  subgraph Evaluation
    full_eval --> metrics
    full_eval --> render
    full_eval --> train
  end
```
