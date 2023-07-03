## Use Case 8: Brain Tumor Classification

Predict the type of tumor based on medical imaging data

- `Industry: Healthcare`
- `Problem Type: Image Classification`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/brain_mri/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/brain_mri/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/brain_mri/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/brain_mri/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/brain_mri/cover)

### Business Problem 

Brain MRI classification model uses deep learning algorithms to classify MRI scans of the brain, detecting and classifying abnormalities such as tumors, hemorrhages, and other anomalies in brain tissue. It is an essential tool for healthcare professionals concerned with diagnosing and treating brain-related disorders, providing fast and accurate analysis of brain MRI scans to improve patient outcomes and enhance the efficiency of healthcare systems.

### Impact

It plays a crucial role in early detection, diagnosis, and treatment planning for brain tumors. By accurately classifying brain tumor images, healthcare professionals can make informed decisions about the appropriate course of treatment, leading to improved patient outcomes. This technology reduces the time and effort required for manual analysis, enabling healthcare providers to prioritize and allocate resources effectively. It also contributes to research and advancements in brain tumor treatment, aiding in the development of personalized therapies and improving overall patient care.

### Dataset

Dataset path: s3://apac-cds/ht_datasets/image_classification/brain-tumor-classification-mri-v2.zip

2870 images with 4 labels.Such as pituitary_tumor,no_tumor,meningioma_tumor,glioma_tumor Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/brain_mri/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Predict the type of tumor based on medical imaging data

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
    data_folder: data/anon/brain-tumor-classification-mri-v2/images/
    data_folder_test: data/anon/brain-tumor-classification-mri-v2/images/
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
    test_dataframe: data/anon/brain-tumor-classification-mri-v2/test.csv
    train_dataframe: data/anon/brain-tumor-classification-mri-v2/train.csv
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
experiment_name: brain-mri-classification
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/brain_mri/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/brain_mri/Validation%20Predictions.png)

### License

CC0: Public Domain

### Acknowledgements

Original dataset source is https://github.com/sartajbhuvaji/brain-tumor-classification-dataset
