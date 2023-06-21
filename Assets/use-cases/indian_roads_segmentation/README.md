## Use Case 15: Road Segmentation

Segment the roads, potholes, and footpaths in a given image

- `Industry: Government`
- `Problem Type: Image Segmentation`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/indian_roads_segmentation/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/indian_roads_segmentation/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/indian_roads_segmentation/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/indian_roads_segmentation/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/indian_roads_segmentation/cover)

### Business Problem 

Indian roads, potholes, and footpaths segmentation model can be used to identify and locate areas such as potholes ,roads and footpaths. This information can be used by city planners and road maintenance teams to prioritize repairs, improve road safety, and reduce accidents caused by damaged roads. The model can also be used to monitor the progress of repairs and ensure that they are carried out effectively.

### Impact

Indian roads segmentation plays a key role in transportation and logistics. By accurately segmenting and mapping road networks in India, logistics companies can optimize route planning, fleet management, and delivery operations. This technology helps reduce transportation costs, improve delivery efficiency, and enhance customer service by providing accurate and up-to-date road network information. Additionally, government agencies can utilize this data for infrastructure planning, traffic management, and urban development, ultimately leading to improved transportation systems and economic growth.

### Dataset

Dataset path: s3://apac-cds/ht_datasets/instance_segmentation/indian_road_seg_v4.zip

2475 train images, 752 validation images, 753 validation images with labels ['roads' 'potholes' 'footpaths' 'shallow paths' 'backgrounds'] Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/indian_roads_segmentation/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Segment the roads, potholes, and footpaths in a given image

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
    data_folder: data/anon/indian_road_seg_v4/images/
    data_folder_test: data/anon/indian_road_seg_v4/images/
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '0'
    group_fold_column: image
    image_column: image
    rle_mask_column: rle_mask
    test_dataframe: data/anon/indian_road_seg_v4/test.pq
    train_dataframe: data/anon/indian_road_seg_v4/train.pq
    validation_dataframe: data/anon/indian_road_seg_v4/test.pq
    validation_size: 0.2
    validation_strategy: custom
environment:
    gpus:
    - '0'
    mixed_precision_inference: false
    mixed_precision_training: true
    number_of_workers: 4
    seed: -1
experiment_name: indian_road_segmentation
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/indian_roads_segmentation/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/indian_roads_segmentation/Validation%20Predictions.png)

### License

GPL 2
