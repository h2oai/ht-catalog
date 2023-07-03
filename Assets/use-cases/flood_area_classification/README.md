## Use Case 14: Flooding Area Segmentation (multi-label)

Segment the flooding area in UAS (Unarmed Aerial System) imageries

- `Industry: AI4Good`
- `Problem Type: Image Segmentation`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/flood_area_classification/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/flood_area_classification/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/flood_area_classification/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/flood_area_classification/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/flood_area_classification/cover)

### Business Problem 

Flood area segmentation/classification is a computer vision application that aims to identify and delineate flooded regions in satellite or aerial images. This use case is important for disaster management and emergency response operations, as it can help officials to quickly assess the extent of flooding and plan their response accordingly. The model uses image segmentation and classification techniques to identify flooded regions, which can aid in decision-making for evacuation, rescue, and relief efforts.

### Impact

Flood area multi-label segmentation has a valuable business impact in disaster response and urban planning. By accurately segmenting flooded areas into multiple categories such as residential, commercial, or critical infrastructure, emergency responders can prioritize rescue and recovery operations based on the severity of the affected areas. Additionally, urban planners can use this information to develop effective flood management strategies, optimize land use, and improve infrastructure resilience to mitigate the impact of future flooding events.

### Dataset

1450 train images and 448 test images with segmenting labels  ['Background' 'Building-flooded' 'Building-non-flooded' 'Road-flooded' 'Road-non-flooded' 'Water' 'Tree' 'Vehicle' 'Pool' 'Grass'] 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/flood_area_classification/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Segment the flooding area in UAS (Unarmed Aerial System) imageries

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    architecture: Unet
    backbone: resnet34
    pretrained: true
augmentation:
    augmentations_strategy: Soft
    custom_inference_augmentations: '{"__version__": "1.1.0", "transform": {"__class_fullname__":
        "Compose", "p": 1.0, "transforms": [{"__class_fullname__": "Resize", "always_apply":
        true, "p": 1, "height": IMAGE_HEIGHT, "width": IMAGE_WIDTH, "interpolation":
        1}], "bbox_params": null, "keypoint_params": null, "additional_targets": {}}}'
    custom_train_augmentations: '{"__version__": "1.1.0", "transform": {"__class_fullname__":
        "Compose", "p": 1.0, "transforms": [{"__class_fullname__": "Resize", "always_apply":
        true, "p": 1, "height": IMAGE_HEIGHT, "width": IMAGE_WIDTH, "interpolation":
        1}], "bbox_params": null, "keypoint_params": null, "additional_targets": {}}}'
    cutmix_corner: false
    mix_concentration: 1.0
    mix_image: Disabled
    mix_iterations: 1
    mix_probability: 1.0
    mix_target: Ratio
dataset:
    class_name_column: class_id
    data_folder: data/anon/flood_segmentation_multi_label/train-org-img/
    data_folder_test: data/anon/flood_segmentation_multi_label/test-org-img/
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '0'
    group_fold_column: image
    image_column: image
    rle_mask_column: rle_mask
    test_dataframe: data/anon/flood_segmentation_multi_label/test.pq
    train_dataframe: data/anon/flood_segmentation_multi_label/train.pq
    validation_dataframe: None
    validation_size: 0.2
    validation_strategy: kfold
environment:
    gpus:
    - '0'
    mixed_precision_inference: false
    mixed_precision_training: true
    number_of_workers: 4
    seed: -1
experiment_name: flood_segmentation_multilabel
image:
    image_channels: 3
    image_height: 256
    image_normalization: Simple
    image_width: 256
logging:
    logger: None
    neptune_project: ''
prediction:
    metric: IoU
    probability_threshold: 0.5
    test_time_augmentations: []
training:
    automatically_adjust_batch_size: false
    batch_size: 16
    build_scoring_pipelines: true
    calculate_train_metric: false
    differential_learning_rate: 0.001
    differential_learning_rate_layers: []
    drop_last_batch: true
    epochs: 5
    evaluation_epochs: 1
    grad_accumulation: 1
    gradient_clip: 0.0
    learning_rate: 0.001
    loss_function: BCEDice
    optimizer: AdamW
    save_best_checkpoint: false
    schedule: Cosine
    train_validation_data: false
    warmup_epochs: 0
    weight_decay: 0.0

```

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/flood_area_classification/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/flood_area_classification/Validation%20Predictions.png)

### License

Community Data License Agreement (permissive)

### Acknowledgements

Original dataset source is https://ieeexplore.ieee.org/abstract/document/9460988
