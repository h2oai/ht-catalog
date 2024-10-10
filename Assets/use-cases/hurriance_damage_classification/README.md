## Use Case 11: Hurriance Damage Classification

Classify if a given region(area) contains flooding damage or not

- `Industry: AI4Good`
- `Problem Type: Image Classification`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hurriance_damage_classification/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hurriance_damage_classification/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hurriance_damage_classification/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hurriance_damage_classification/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hurriance_damage_classification/cover)

### Business Problem 

Hurricane Damage Classification model is used to assess the extent of damage caused by hurricanes on buildings and infrastructure. It helps emergency responders and insurance companies to prioritize their response and allocate resources efficiently. The model uses drone imagery and classify the level of damage into categories, providing a faster and more accurate assessment of the damage.

### Impact

By accurately identifying and categorizing the extent of damage caused by hurricanes, insurance companies can efficiently assess claims, determine coverage eligibility, and expedite the claims process. This technology enables prompt and fair settlements, reduces fraudulent claims, and enhances customer satisfaction by streamlining the insurance workflow.

### Dataset

Dataset link - [s3://h2o-ht-catalog/image_classification/Hurriance_Damage_Classification.zip](https://h2o-ht-catalog.s3.amazonaws.com/image_classification/Hurriance_Damage_Classification.zip)

10000 train images , 2000 validation images, 2000 test images with labels is damage or not 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hurriance_damage_classification/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Classify if a given region(area) contains flooding damage or not

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    backbone: resnet50
    dropout: 0
    pool: Average
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
    data_folder: data/anon/Hurriance_Damage_Classification/Images/
    data_folder_test: data/anon/Hurriance_Damage_Classification/Images/
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '0'
    group_fold_column: 'Unnamed: 0'
    image_column: images
    label_columns:
    - is_damage
    test_dataframe: data/anon/Hurriance_Damage_Classification/test.csv
    train_dataframe: data/anon/Hurriance_Damage_Classification/train_another.csv
    unlabeled_dataframe: None
    validation_dataframe: data/anon/Hurriance_Damage_Classification/validation_another.csv
    validation_size: 0.2
    validation_strategy: custom
environment:
    gpus:
    - '0'
    mixed_precision_inference: false
    mixed_precision_training: true
    number_of_workers: 4
    seed: -1
experiment_name: hurricane_damage_classification
image:
    image_channels: 3
    image_height: 224
    image_normalization: Simple
    image_width: 224
logging:
    logger: None
    neptune_project: ''
    number_of_images: 8
prediction:
    metric: ROC_AUC
    probability_threshold: 0.5
    test_time_augmentations: []
training:
    automatically_adjust_batch_size: false
    batch_size: 32
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
    loss_function: BCE
    optimizer: AdamW
    run_interpretations: true
    save_best_checkpoint: false
    schedule: Cosine
    train_validation_data: false
    warmup_epochs: 0
    weight_decay: 0.0

```

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hurriance_damage_classification/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hurriance_damage_classification/Validation%20Predictions.png)

### License

CC BY-SA 4.0

### Acknowledgements

Original dataset source is https://ieee-dataport.org/open-access/detecting-damaged-buildings-post-hurricane-satellite-imagery-based-customized
