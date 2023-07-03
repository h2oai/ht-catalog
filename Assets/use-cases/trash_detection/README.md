## Use Case 46: Trash Detection

Identify and classify various types of trash objects 

- `Industry: Government`
- `Problem Type: Object Detection`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/trash_detection/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/trash_detection/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/trash_detection/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/trash_detection/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/trash_detection/cover)

### Business Problem 

The Trash Detection and Classification model is designed to identify and classify various types of trash objects in an image. This model can help in automated waste management by detecting and segregating different types of waste for efficient recycling and disposal. The model uses image classification techniques to classify trash objects into categories such as plastic, glass, paper, metal, and organic waste. The model can be trained on a large dataset of annotated images of trash objects to improve its accuracy in detecting and classifying various types of waste. Once deployed, the model can be used in various settings such as waste sorting plants, recycling centers, and smart waste bins.

### Impact

Trash detection plays a key role in waste management and environmental sustainability. By utilizing computer vision and machine learning algorithms, trash detection technology enables the automated identification and classification of different types of trash in images or videos. Accurate trash detection facilitates efficient waste sorting, recycling, and disposal processes. It helps in reducing contamination, optimizing recycling efforts, and minimizing environmental impact. Trash detection technology contributes to improved waste management practices, resource conservation, and a cleaner, more sustainable environment.

### Dataset

Dataset path: s3://apac-cds/ht_datasets/object_detection/trash-detection.zip

369 train images with 4 unique labels {glass,paper,metal, plastic} Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/trash_detection/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Identify and classify various types of trash objects 

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
    class_name_column: class_name
    data_folder: data/anon/trash-detection/Images/
    data_folder_test: None
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '0'
    group_fold_column: image_name
    image_column: image_name
    test_dataframe: None
    train_dataframe: data/anon/trash-detection/train.pq
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
experiment_name: trash-detection
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/trash_detection/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/trash_detection/Validation%20Predictions.png)

### License

CC BY-NC-SA 4.0

### Acknowledgements

Original dataset source is https://www.sciencedirect.com/science/article/pii/S2666016420300244?via%3Dihub
