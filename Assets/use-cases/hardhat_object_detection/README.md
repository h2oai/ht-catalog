## Use Case 47: Hardhat Detection

Detect the presence of hardhats in images

- `Industry: Manufacturing `
- `Problem Type: Object Detection`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hardhat_object_detection/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hardhat_object_detection/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hardhat_object_detection/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hardhat_object_detection/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hardhat_object_detection/cover)

### Business Problem 

Hardhat Object Detection model is designed to detect and classify the presence of hardhats in images. The model is based on object detection techniques that use deep learning algorithms to identify and locate objects in images. With the help of a dataset of labeled images that contain hardhats, the model can detect the presence and location of hardhats in new images. This model can be useful in various applications, such as construction site monitoring, safety analysis, and worker compliance monitoring.

### Impact

Hardhat object detection plays a vital role in construction site safety and worker protection. By analyzing visual data from cameras or surveillance systems, hardhat object detection technology identifies and tracks the presence of hardhats worn by workers in real-time. Accurate hardhat object detection ensures compliance with safety regulations, reduces the risk of head injuries, and enhances overall workplace safety. It enables proactive monitoring, alerts for non-compliance, and helps in assessing safety performance. Hardhat object detection technology contributes to accident prevention, injury reduction, and improved safety practices in construction and industrial settings.

### Dataset

4750 train images with their annotations 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hardhat_object_detection/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Detect the presence of hardhats in images

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    anchor_aspect_ratios:
    - '1.0'
    - '2.0'
    - '0.5'
    anchor_iou_match_threshold: 0.5
    anchor_num_scales: 3
    anchor_scale: 4
    backbone: tf_efficientdet_d0
    drop_path_rate: Default
    pretrained: true
augmentation:
    augmentations_strategy: Soft
    custom_inference_augmentations: '{"__version__": "1.1.0", "transform": {"__class_fullname__":
        "Compose", "p": 1.0, "transforms": [{"__class_fullname__": "Resize", "always_apply":
        true, "p": 1, "height": IMAGE_HEIGHT, "width": IMAGE_WIDTH, "interpolation":
        1}], "bbox_params": {"format": "pascal_voc", "label_fields": ["labels"], "min_area":
        0, "min_visibility": 0, "check_each_transform": true}, "keypoint_params":
        null, "additional_targets": {}}}'
    custom_train_augmentations: '{"__version__": "1.1.0", "transform": {"__class_fullname__":
        "Compose", "p": 1.0, "transforms": [{"__class_fullname__": "Resize", "always_apply":
        true, "p": 1, "height": IMAGE_HEIGHT, "width": IMAGE_WIDTH, "interpolation":
        1}], "bbox_params": {"format": "pascal_voc", "label_fields": ["labels"], "min_area":
        0, "min_visibility": 0, "check_each_transform": true}, "keypoint_params":
        null, "additional_targets": {}}}'
    mix_concentration: 1.0
    mix_image: Disabled
    mix_iterations: 1
    mix_probability: 1.0
dataset:
    class_name_column: name
    data_folder: data/anon/hardhat-object-detection/images/
    data_folder_test: None
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '4'
    group_fold_column: file_name
    image_column: file_name
    test_dataframe: None
    train_dataframe: data/anon/hardhat-object-detection/train.pq
    unlabeled_dataframe: None
    validation_dataframe: None
    validation_size: 0.2
    validation_strategy: kfold
    x_max_column: x_max
    x_min_column: x_min
    y_max_column: y_max
    y_min_column: y_min
environment:
    gpus:
    - '0'
    mixed_precision_inference: false
    mixed_precision_training: true
    number_of_workers: 4
    seed: -1
experiment_name: hardhat-object-detection
image:
    image_channels: 3
    image_height: 512
    image_normalization: Simple
    image_width: 512
logging:
    logger: None
    neptune_project: ''
    number_of_images: 8
prediction:
    max_det_per_image: 100
    metric: mAP
    metric_iou_threshold: 0.5
    nms_iou_threshold: 0.5
    probability_threshold: 0.3
training:
    automatically_adjust_batch_size: false
    batch_size: 16
    box_loss_weight: 50
    build_scoring_pipelines: true
    calculate_train_metric: false
    differential_learning_rate: 0.001
    differential_learning_rate_layers: []
    drop_last_batch: true
    epochs: 5
    evaluation_epochs: 1
    focal_cls_loss_alpha: 0.25
    focal_cls_loss_gamma: 1.5
    grad_accumulation: 1
    gradient_clip: 0.0
    learning_rate: 0.001
    optimizer: AdamW
    save_best_checkpoint: false
    schedule: Cosine
    train_validation_data: false
    warmup_epochs: 0
    weight_decay: 0.0

```

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hardhat_object_detection/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hardhat_object_detection/Validation%20Predictions.png)

### License

CC0: Public Domain

### Acknowledgements

Original dataset source is https://www.kaggle.com/datasets/rahulgolder/hardhat-data
