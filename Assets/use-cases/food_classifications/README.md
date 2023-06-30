## Use Case 6: Food Type Classification

Categorize food types based on their visual characteristics

- `Industry: Media`
- `Problem Type: Image Classification`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/food_classifications/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/food_classifications/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/food_classifications/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/food_classifications/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/food_classifications/cover)

### Business Problem 

Food Classification model is used to identify and classify food items in images. This model is useful for food and nutrition professionals, allowing them to analyze and track dietary habits and trends.

### Impact

It enables automatic categorization and identification of food items, which can be utilized for various purposes. Restaurants and food delivery services can benefit from accurate food image classification to improve menu organization, streamline order processing, and enhance customer experience. Food manufacturers can use this technology to automate quality control processes, ensuring product consistency and reducing errors in packaging and labeling. Additionally, nutrition and diet tracking applications can leverage food image classification to provide users with accurate nutritional information and personalized dietary recommendations.

### Dataset

Dataset path: s3://apac-cds/ht_datasets/image_classification/food_classification.zip

9866 images with 11 labels. Such as Bread,Dairy product,Dessert,Egg,Fried food,Meat,Noodles-Pasta,Rice, Seafood,Soup,Vegetable-Fruit Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/food_classifications/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Categorize food types based on their visual characteristics

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
    data_folder: data/anon/food_classification/training/
    data_folder_test: data/anon/food_classification/evaluation/
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '0'
    group_fold_column: image_name
    image_column: image_name
    label_columns:
    - label
    test_dataframe: data/anon/food_classification/test.csv
    train_dataframe: data/anon/food_classification/train.csv
    unlabeled_dataframe: None
    validation_dataframe: data/anon/food_classification/val.csv
    validation_size: 0.2
    validation_strategy: custom
environment:
    gpus:
    - '0'
    mixed_precision_inference: false
    mixed_precision_training: true
    number_of_workers: 4
    seed: -1
experiment_name: food_classification
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/food_classifications/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/food_classifications/Validation%20Predictions.png)

### License

CC0: Public Domain

### Acknowledgements

The original dataset used in this use case comes from this source : https://www.epfl.ch/labs/mmspg/downloads/food-image-datasets/
