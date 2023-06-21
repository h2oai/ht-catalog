## Use Case 30: Document Stamp Detection

Detect stamps in the digital documents using object detection techniques

- `Industry: Banking`
- `Problem Type: Image Segmentation`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/stamp_detection/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/stamp_detection/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/stamp_detection/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/stamp_detection/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/stamp_detection/cover)

### Business Problem 

Stamp detection model is designed to detect stamps from images using computer vision techniques. With the help of stamp datasets containing images of different stamps, the model can identify and localize the stamps in the input image. The model can be used for various applications, such as stamp authentication and sorting, postal services, and philately. It employs object detection algorithms, including convolutional neural networks and feature extraction methods to recognize and segment the stamps from the background.

### Impact

A stamp detection model offers several valuable benefits to businesses. It automates the process of identifying stamps in documents or images, improving efficiency and accuracy while saving time and costs. It helps prevent fraud by detecting forged or counterfeit stamps, ensuring compliance with regulations. Additionally, it enhances customer experience in industries like postal services by facilitating faster processing. Overall, a stamp detection model provides businesses with increased efficiency, cost savings, fraud prevention, regulatory compliance, and improved customer experience, leading to improved operational effectiveness and a competitive edge.

### Dataset

Dataset path: s3://apac-cds/ht_datasets/image_segmentation/stamp_detection.zip

400 images with their coordinates Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/stamp_detection/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Detect stamps in the digital documents using object detection techniques

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    architecture: Unet
    backbone: resnet101
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
    data_folder: data/anon/stamp_detection/scans/
    data_folder_test: None
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '0'
    group_fold_column: image
    image_column: image
    rle_mask_column: rle_mask
    test_dataframe: None
    train_dataframe: data/anon/stamp_detection/stamp_detection.pq
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
experiment_name: stamp_detection
image:
    image_channels: 3
    image_height: 672
    image_normalization: Simple
    image_width: 672
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/stamp_detection/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/stamp_detection/Validation%20Predictions.png)

### License

Unknown
