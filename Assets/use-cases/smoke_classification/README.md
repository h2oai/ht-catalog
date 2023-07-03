## Use Case 4: Smoke Classification

Classify whether a given image contain smoke(s) or not

- `Industry: Manufacturing`
- `Problem Type: Image Classification`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/smoke_classification/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/smoke_classification/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/smoke_classification/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/smoke_classification/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/smoke_classification/cover)

### Business Problem 

Smoke Classification model can classify smoke. This model is an essential tool for fire safety professionals, allowing them to detect and classify smoke and efficiently.

### Impact

In fire detection systems, accurate smoke classification enhances early warning systems, allowing for prompt response and reducing the risk of fire-related damage. In industrial settings, smoke classification enables proactive monitoring of smoke emissions, ensuring compliance with environmental regulations and promoting sustainable practices. Public safety agencies benefit from smoke classification in surveillance systems, aiding in the identification of potential fire hazards and enhancing emergency response. Additionally, in insurance and risk assessment, smoke classification provides valuable insights for property underwriting and assessing fire-related risks. Overall, smoke classification in images enhances safety measures, regulatory compliance, and risk management.

### Dataset

Dataset path: s3://apac-cds/ht_datasets/image_classification/wildfire_image_classification.zip

343 images with label  0 or 1  Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/smoke_classification/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Classify whether a given image contain smoke(s) or not

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
    data_folder: data/anon/wildfire_image_classification/content/drive/MyDrive/BushFire/wildfire-smoke/images/
    data_folder_test: data/anon/wildfire_image_classification/content/drive/MyDrive/BushFire/wildfire-smoke/images/
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '0'
    group_fold_column: image
    image_column: image
    label_columns:
    - label
    test_dataframe: None
    train_dataframe: data/anon/wildfire_image_classification/content/drive/MyDrive/BushFire/wildfire-smoke/main.csv
    unlabeled_dataframe: None
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
experiment_name: wildfire_image_classification
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/smoke_classification/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/smoke_classification/Validation%20Predictions.png)

### License

License Type is Unknown

### Acknowledgements

Original dataset source is Unknown
