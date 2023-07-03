## Use Case 61: Person Re-Identification

Identify the images of the same person from set of person images

- `Industry: Banking`
- `Problem Type: Image Metric Learning`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/person_images/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/person_images/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/person_images/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/person_images/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/person_images/cover)

### Business Problem 

Person Re-Identification is a computer vision task that involves identifying and tracking individuals across multiple non-overlapping camera views. The goal is to develop an algorithm or model that can match a person's identity across different surveillance cameras or video frames, regardless of changes in appearance, pose, lighting conditions, or camera angles. This use case finds applications in various domains such as law enforcement, public safety, retail analytics, and crowd management. By re-identifying individuals, organizations can enhance security measures, detect suspicious activities, and gather insights for business optimization or safety purposes. The person re-identification technology enables the tracking of individuals in real-time or post-event analysis, providing a powerful tool for video surveillance systems.

### Impact

Person re-identification plays a key roles across multiple industries. In the field of law enforcement and public safety, it enables authorities to track and monitor individuals of interest across different camera feeds, aiding in investigations and crime prevention. Retail businesses can leverage person re-identification for customer behavior analysis, footfall tracking, and targeted marketing strategies. By understanding customer movement patterns and preferences, retailers can optimize store layouts, personalize shopping experiences, and improve customer satisfaction. Crowd management at large events or transportation hubs can also benefit from person re-identification to monitor crowd flow, identify potential security risks, and ensure public safety. Overall, person re-identification technology enhances security, enables efficient video analysis, and provides valuable insights for decision-making across various industries.

### Dataset

Dataset path: s3://h2oai-hydrogen-torch-internal/dev_datasets/market_1501_metric_learning.zip

12936 train images of 751 humans. 534 test images. Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/person_images/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Identify the images of the same person from set of person images

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
    data_folder: data/anon/market_1501_metric_learning/bounding_box_train/
    data_folder_test: data/anon/market_1501_metric_learning/bounding_box_train/
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '0'
    group_fold_column: image_id
    image_column: image_id
    label_columns: label
    test_dataframe: data/anon/market_1501_metric_learning/test.csv
    train_dataframe: data/anon/market_1501_metric_learning/train.csv
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
experiment_name: 61_market_1501
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
    weight_decay: 0.0

```

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/person_images/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/person_images/Validation%20Predictions.png)

### License

License Type is Unknown

### Acknowledgements

Original dataset source is Unknown
