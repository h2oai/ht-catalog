## Use Case 24: Textile Defect Classification

identify whether the textile is damage or not

- `Industry: Manufacturing `
- `Problem Type: Image Classification`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/textile_defect_detection/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/textile_defect_detection/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/textile_defect_detection/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/textile_defect_detection/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/textile_defect_detection/cover)

### Business Problem 

Textile Defect classification model is used to classify defects in textiles as damaged or not damaged. The model uses computer vision and machine learning algorithms to detect and classify defects based on their properties such as shape, size, and texture. This helps manufacturers to identify and remove defective products and ensure product quality. The model can be trained on large datasets of images containing both defective and non-defective textiles to improve its accuracy and efficiency.

Textile defect detection has significant business impact in the textile and fashion industries. By leveraging computer vision and image analysis, it enables automated detection of defects in fabrics and garments during the production process. Timely identification of defects such as holes, stains, or misprints helps maintain product quality and reduces waste. Textile defect detection enhances production efficiency, as it allows for real-time monitoring and quality control, minimizing the need for manual inspection. By ensuring the delivery of defect-free textiles to customers, it enhances brand reputation, customer satisfaction, and overall business profitability.

### Dataset

108000 train images with labels (good or damaged)

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/textile_defect_detection/train%20data.png)

### Model Training

Objective: identify whether the textile is damage or not

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
    data_folder: data/anon/textile_damage_classification/train/
    data_folder_test: None
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '4'
    group_fold_column: 'Unnamed: 0'
    image_column: image
    label_columns:
    - class
    test_dataframe: None
    train_dataframe: data/anon/textile_damage_classification/textile_damage_classification.csv
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
experiment_name: textile_damage_classification
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/textile_defect_detection/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/textile_defect_detection/Validation%20Predictions.png)

### License

CC BY-NC-SA 4.0
