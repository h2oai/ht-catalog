## Use Case 53: Similar Ads Image Identification

Identify the images of same bicycle within the same advertisement

- `Industry: Manufacturing `
- `Problem Type: Image Metric Learning`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/online_bicycle_ads/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/online_bicycle_ads/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/online_bicycle_ads/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/online_bicycle_ads/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/online_bicycle_ads/cover)

### Business Problem 

The use case involves utilizing similar image grouping in bicycle ads. When advertising bicycles, it is essential to showcase a variety of models, features, and styles to attract potential customers. However, manually organizing and selecting images for ads can be time-consuming and challenging. By leveraging similar image grouping, an automated system can analyze the visual content of bicycle images and group them based on similarities in design, color, or style. This process helps streamline the ad creation process by providing a curated selection of images that can be easily incorporated into advertisements.

Implementing similar image grouping in bicycle ads can have several positive impacts on businesses. Firstly, it improves efficiency by reducing the time and effort required to manually sort and organize images for advertisements. This allows marketers to focus on other crucial tasks, leading to increased productivity. Secondly, by presenting visually coherent and appealing ads, businesses can enhance customer engagement and increase the likelihood of attracting potential buyers. This can result in higher conversion rates and improved sales for bicycle companies. Lastly, by automating the image grouping process, companies can reduce the chances of human error and inconsistencies in ad visuals, ensuring a more professional and polished advertising campaign.

### Dataset

8313 images of 1148 online bicycle ads. Each ad has multiple images marked by their class ID.
Dataset path: s3://h2oai-hydrogen-torch-internal/dev_datasets/bicycle_image_metric_learning.zip

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/online_bicycle_ads/train%20data.png)

### Model Training

Objective: Identify the images of same bicycle within the same advertisement

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    backbone: tf_efficientnet_b0_ns
    dropout: 0
    embedding_size: 512
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
dataset:
    data_folder: data/anon/bicycle_image_metric_learning/images/
    data_folder_test: None
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '0'
    group_fold_column: image
    image_column: image
    label_columns: label
    test_dataframe: None
    train_dataframe: data/anon/bicycle_image_metric_learning/train.csv
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
experiment_name: 53_bicycle_image_metric_learning
image:
    image_channels: 3
    image_height: 512
    image_normalization: Simple
    image_width: 512
logging:
    logger: None
    neptune_project: ''
    number_of_images: 8
prediction:
    metric: mAP
    test_time_augmentations: []
    top_k_similar: 50
training:
    arcface_margin: 0.1
    arcface_scale: 45
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
    loss_function: ArcFace
    optimizer: AdamW
    save_best_checkpoint: false
    schedule: Cosine
    train_validation_data: false
    warmup_epochs: 0
    weight_decay: 0

```

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/online_bicycle_ads/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/online_bicycle_ads/Validation%20Predictions.png)

### License

NA
