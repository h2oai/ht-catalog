## Use Case 3: Smoke Segmentation

Segment the presence and location of smoke within images

- `Industry: Manufacturing`
- `Problem Type: Image Segmentation`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/smoke_segmentation/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/smoke_segmentation/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/smoke_segmentation/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/smoke_segmentation/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/smoke_segmentation/cover)

### Business Problem 

This model can identify and segment smoke in images. By distinguishing smoke from other objects and backgrounds, The model helps to improve the accuracy of fire detection systems and enhance safety in various industries, including manufacturing, transportation, and public safety.

### Impact

The utilization of a smoke detection model has far-reaching implications in various sectors. Within the realm of fire prevention and safety, precise smoke segmentation plays a crucial role in identifying smoke early on, thereby facilitating prompt response and bolstering emergency management efforts while minimizing the extent of property destruction. Industrial environments also benefit from smoke segmentation by enabling constant monitoring of smoke presence, thus enhancing workplace safety and preventing accidents. Environmental agencies find value in smoke segmentation for detecting and monitoring wildfires, aiding in timely intervention and reducing ecological harm. Additionally, the field of computer vision and image analysis benefits from smoke segmentation as it contributes to a multitude of applications, such as surveillance, image comprehension, and object recognition.

### Dataset

Dataset path: s3://apac-cds/ht_datasets/instance_segmentation/bush_fire_image_segment.zip

64 train images segmented using class_id 'smoke' Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/smoke_segmentation/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Segment the presence and location of smoke within images

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
    data_folder: data/anon/Smoke_segmentation/content/drive/MyDrive/BushFire/Image_segment/gt_training/
    data_folder_test: data/anon/Smoke_segmentation/content/drive/MyDrive/BushFire/Image_segment/gt_testing/
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '0'
    group_fold_column: image_id
    image_column: image_id
    rle_mask_column: rle_mask
    test_dataframe: data/anon/Smoke_segmentation/content/drive/MyDrive/BushFire/Image_segment/test.pq
    train_dataframe: data/anon/Smoke_segmentation/content/drive/MyDrive/BushFire/Image_segment/train.pq
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
experiment_name: Smoke_segmentation
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/smoke_segmentation/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/smoke_segmentation/Validation%20Predictions.png)

### License

As stated by Center for Wildfire Research

### Acknowledgements

Original dataset source is http://wildfire.fesb.hr/index.php?option=com_content&view=article&id=49&Itemid=54
