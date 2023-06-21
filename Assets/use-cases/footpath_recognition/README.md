## Use Case 92: Road Footpath Recognition

Detect and recognize footpaths or pedestrian walkways in images or video data

- `Industry: Government`
- `Problem Type: Image Semantic Segmentation`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/footpath_recognition/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/footpath_recognition/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/footpath_recognition/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/footpath_recognition/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/footpath_recognition/cover)

### Business Problem 

Footpath recognition involves the automated detection and recognition of footpaths or pedestrian walkways in images or video data. This technology utilizes computer vision techniques to identify and segment footpaths, assisting in urban planning, navigation systems, and pedestrian safety initiatives.

Footpath recognition has business implications in urban planning, transportation, and navigation systems. By automatically detecting and recognizing pedestrian walkways or footpaths in images or video data, this technology aids in pedestrian safety, infrastructure development, and navigation optimization. Urban planners can analyze footpath usage, identify areas needing improvement, and design pedestrian-friendly environments. Navigation systems can provide accurate pedestrian routing, enhance mobility options, and improve overall transportation efficiency.

### Dataset

3000 train images with their masks

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/footpath_recognition/train%20data.png)

### Model Training

Objective: Detect and recognize footpaths or pedestrian walkways in images or video data

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
    data_folder: data/anon/footpath-image-dataset/images/
    data_folder_test: None
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '0'
    group_fold_column: image
    image_column: image
    rle_mask_column: rle_mask
    test_dataframe: None
    train_dataframe: data/anon/footpath-image-dataset/train.pq
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
experiment_name: 92_footpath_recognition
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/footpath_recognition/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/footpath_recognition/Validation%20Predictions.png)

### License

CC BY-SA 4.0
