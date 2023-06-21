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

This model can accurately identify and segment smoke in images. By distinguishing smoke from other objects and backgrounds, our model helps to improve the accuracy of fire detection systems and enhance safety in various industries, including manufacturing, transportation, and public safety.

Smoke segmentation in images has a profound impact across industries. In the field of fire prevention and safety, accurate smoke segmentation enables early detection and response, enhancing emergency management and minimizing property damage. In industrial settings, smoke segmentation helps monitor the presence of smoke, improving workplace safety and preventing accidents. Environmental agencies benefit from smoke segmentation in the detection and monitoring of wildfires, aiding in timely intervention and minimizing ecological damage. Furthermore, in the field of computer vision and image analysis, smoke segmentation contributes to various applications, including surveillance, image understanding, and object recognition.

### Dataset

64 train images segmented using class_id 'smoke'
Dataset path: s3://apac-cds/ht_datasets/instance_segmentation/bush_fire_image_segment.zip

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/smoke_segmentation/train%20data.png)

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

These datasets are free to use, but if you intend to use them in scientific research, it is necessary to reference this webpage and the Center for Wildfire Research.