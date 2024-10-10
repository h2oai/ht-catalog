## Use Case 70: Nerves Segmentation in Ultrasound Images

Segment a collection of nerves in the ultrasound images

- `Industry: Healthcare`
- `Problem Type: Image Semantic Segmentation`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/ultrasound_images_of_brachial_plexus/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/ultrasound_images_of_brachial_plexus/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/ultrasound_images_of_brachial_plexus/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/ultrasound_images_of_brachial_plexus/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/ultrasound_images_of_brachial_plexus/cover)

### Business Problem 

Nerves segmentation in ultrasound images involves the automated identification and segmentation of nerve structures in ultrasound scans. This solution aids in medical imaging and diagnostic procedures by enabling precise nerve localization, analysis, and evaluation

### Impact

Nerves segmentation in ultrasound images is very useful in the healthcare industry. It improves the accuracy and efficiency of nerve-related diagnostics, such as identifying nerve damage, guiding nerve blocks, and assisting in surgical procedures. This technology enhances the detection and monitoring of nerve-related conditions, such as neuropathies and nerve entrapments, facilitating early intervention and appropriate treatment planning. It also contributes to research and development in neurology and enables advancements in nerve-related therapies and interventions. Overall, nerves segmentation in ultrasound images enhances the quality of nerve-related medical imaging and diagnosis, leading to improved patient care and outcomes.

### Dataset

Dataset link - [s3://h2o-ht-catalog/nerves_image_semantic_segmentation.zip](https://h2o-ht-catalog.s3.amazonaws.com/nerves_image_semantic_segmentation.zip)

2323 train images with their masks. 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/ultrasound_images_of_brachial_plexus/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Segment a collection of nerves in the ultrasound images

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
    data_folder: data/anon/nerves_image_semantic_segmentation/images/
    data_folder_test: data/anon/nerves_image_semantic_segmentation/images/
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '4'
    group_fold_column: image
    image_column: image
    rle_mask_column: rle_mask
    test_dataframe: None
    train_dataframe: data/anon/nerves_image_semantic_segmentation/train.pq
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
experiment_name: 70_nerves_image_semantic_segmentation.4.1
image:
    image_channels: 3
    image_height: 448
    image_normalization: Simple
    image_width: 448
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/ultrasound_images_of_brachial_plexus/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/ultrasound_images_of_brachial_plexus/Validation%20Predictions.png)

### License

MIT License

### Acknowledgements

Original dataset source is https://www.kaggle.com/competitions/ultrasound-nerve-segmentation/data
