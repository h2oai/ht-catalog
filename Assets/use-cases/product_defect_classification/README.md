## Use Case 13: Product Defect Classification

Classify the defects in the machinery

- `Industry: Manufacturing`
- `Problem Type: Image Classification`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/product_defect_classification/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/product_defect_classification/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/product_defect_classification/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/product_defect_classification/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/product_defect_classification/cover)

### Business Problem 

Product Defect Classification model is a machine learning model designed to detect and classify defects in products using image analysis techniques. The model uses a dataset containing images of products with and without defects, and trains a deep learning algorithm to classify the images into their respective categories. This model can be used to improve quality control processes in manufacturing industries, by detecting defects early in the production process and preventing defective products from reaching customers.

### Impact

Product defect classification plays a key role in manufacturing and quality control. By automatically detecting and classifying defects in products during the production process, manufacturers can proactively identify and address quality issues, leading to improved product quality, reduced rework, and enhanced customer satisfaction. This technology helps minimize production costs, ensure compliance with quality standards, and maintain brand reputation by delivering high-quality products to the market.

### Dataset

Dataset path: s3://apac-cds/ht_datasets/manufacturing/product_defect_classification.zip

6 classes, 1800 image samples split into training and validation Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/product_defect_classification/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Classify the defects in the machinery

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    backbone: resnet50
    dropout: 0.2
    pool: Average
    pretrained: false
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
    data_folder: data/anon/normal_defect/normal_defect/normaldefect_image/
    data_folder_test: data/anon/normal_defect/normal_defect/normaldefect_image/
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '4'
    group_fold_column: 'Unnamed: 0'
    image_column: images
    label_columns:
    - label
    test_dataframe: None
    train_dataframe: data/anon/normal_defect/normal_defect/normal_defect_dataset.csv
    unlabeled_dataframe: None
    validation_dataframe: data/anon/normal_defect/normal_defect/normal_defect_dataset2.csv
    validation_size: 0.2
    validation_strategy: kfold
environment:
    gpus:
    - '0'
    mixed_precision_inference: false
    mixed_precision_training: true
    number_of_workers: 4
    seed: -1
experiment_name: normal_defect_classification2
image:
    image_channels: 3
    image_height: 224
    image_normalization: Channel
    image_width: 224
logging:
    logger: None
    neptune_project: ''
    number_of_images: 8
prediction:
    metric: F1
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
    loss_function: CrossEntropy
    optimizer: AdamW
    run_interpretations: true
    save_best_checkpoint: false
    schedule: Cosine
    train_validation_data: false
    warmup_epochs: 0
    weight_decay: 0

```

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/product_defect_classification/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/product_defect_classification/Validation%20Predictions.png)

### License

License Type is Unknown

### Acknowledgements

Original dataset source is http://faculty.neu.edu.cn/songkc/en/zdylm/263265/list/index.htm
