## Use Case 69: CT-Scan Chest and Lungs Segmentation

Segment the human chest and lungs in CT-Scan images

- `Industry: Healthcare`
- `Problem Type: 3D Image Semantic Segmentation`
- `Data Type: 3D Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/covid19_ct_scans/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/covid19_ct_scans/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/covid19_ct_scans/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/covid19_ct_scans/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/covid19_ct_scans/cover)

### Business Problem 

Chest and lungs segmentation in CT scans involves the automated extraction and delineation of chest and lung regions from CT (computed tomography) scans. This solution aids in medical image analysis and diagnosis by providing precise anatomical segmentation, which is crucial for identifying and analyzing abnormalities, tumors, or lung diseases.

### Impact

Chest and lungs segmentation in CT scans has significant role in the healthcare industry. It enables accurate and efficient diagnosis by providing detailed anatomical information to radiologists and physicians. It aids in the detection and tracking of lung diseases, tumors, and abnormalities, allowing for early intervention and improved patient outcomes. This technology also facilitates treatment planning, surgical guidance, and monitoring of disease progression. Overall, chest and lungs segmentation in CT scans enhances the accuracy and efficiency of medical imaging analysis, leading to better patient care and treatment decisions.

### Dataset

Dataset link - [s3://h2o-ht-catalog/covid_ct_image_semantic_segmentation_3d.zip](https://h2o-ht-catalog.s3.amazonaws.com/covid_ct_image_semantic_segmentation_3d.zip)

20 3d train images with their masks. 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/covid19_ct_scans/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Segment the human chest and lungs in CT-Scan images

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    decoder: Unet
    drop_path_rate: 0.0
    drop_rate: 0.0
    encoder: resnet18d
    number_of_blocks: 5
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
    mix_concentration: 1.0
    mix_image: Disabled
    mix_iterations: 1
    mix_probability: 1.0
    mix_target: Ratio
dataset:
    class_name_column: class_id
    data_folder: data/user/covid_ct_image_semantic_segmentation_3d/images/
    data_folder_test: data/user/covid_ct_image_semantic_segmentation_3d/images/
    data_sample: 1.0
    data_sample_choice:
    - Train
    - Validation
    group_fold_column: image
    image_column: image
    rle_mask_column: rle_mask
    selected_folds:
    - '0'
    test_dataframe: None
    train_dataframe: data/user/covid_ct_image_semantic_segmentation_3d/train.pq
    validation_dataframe: None
    validation_size: 0.2
    validation_strategy: kfold
environment:
    gpus:
    - '0'
    mixed_precision_inference: false
    mixed_precision_training: true
    number_of_seeds_per_run: 1
    number_of_workers: 4
    seed: -1
experiment_name: 69_covid_ct_image_semantic_segmentation_3d
image:
    image_channels: 1
    image_depth: 128
    image_height: 128
    image_normalization: Simple
    image_width: 128
logging:
    log_grad_norm: false
    logger: None
    neptune_project: ''
prediction:
    metric: IoU
    probability_threshold: 0.5
    test_time_augmentations: []
training:
    automatically_adjust_batch_size: false
    batch_size: 4
    bce_weight: 1.0
    build_scoring_pipelines: true
    calculate_train_metric: false
    dice_weight: 1.0
    differential_learning_rate: 0.001
    differential_learning_rate_layers: []
    drop_last_batch: true
    epochs: 10
    evaluate_before_training: false
    evaluation_epochs: 1
    focal_weight: 1.0
    grad_accumulation: 1
    gradient_clip: 0.0
    learning_rate: 0.001
    loss_function: BCEDice
    lovasz_weight: 1.0
    optimizer: AdamW
    save_best_checkpoint: false
    schedule: Cosine
    train_validation_data: false
    warmup_epochs: 0
    weight_decay: 0.0

```

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/covid19_ct_scans/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/covid19_ct_scans/Validation%20Predictions.png)

### License

CC BY 4.0

### Acknowledgements

Original dataset source is https://zenodo.org/record/3757476
