## Use Case 2: Document Signature Verification

Verify, match, and compare the digital signatures

- `Industry: Banking`
- `Problem Type: Image Metric Learning`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/signature_verification/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/signature_verification/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/signature_verification/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/signature_verification/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/signature_verification/cover)

### Business Problem 

Signature verification model is designed to ensure the authenticity and security of legal, financial, and personal transactions. By accurately identifying and authenticating signatures, this model helps prevent fraud and identity theft.

Signature verification in documents has a profound impact on business operations. In banking and financial services, it strengthens fraud prevention by accurately verifying signatures on checks, contracts, and financial documents, minimizing the risk of unauthorized transactions. The legal sector benefits from streamlined document authentication and integrity, ensuring the validity of legal agreements and reducing legal disputes. Healthcare organizations rely on signature verification to authenticate patient consent forms and medical records, ensuring compliance with regulations and enhancing patient safety. In government agencies, signature verification helps validate important documents, reducing the risk of forgery and ensuring the credibility of administrative processes. Overall, signature verification provides businesses with increased security, improved compliance, and enhanced operational efficiency.

### Dataset

1100 train images with 55 unique labels.
Dataset path: s3://apac-cds/ht_datasets/sign_verification/sign_verification.zip

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/signature_verification/train%20data.png)

### Model Training

Objective: Verify, match, and compare the digital signatures

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
    data_folder: data/anon/sign_verification/train/
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
    train_dataframe: data/anon/sign_verification/train.csv
    validation_dataframe: data/anon/sign_verification/val.csv
    validation_size: 0.2
    validation_strategy: custom
environment:
    gpus:
    - '0'
    mixed_precision_inference: false
    mixed_precision_training: true
    number_of_workers: 4
    seed: -1
experiment_name: sign_verification
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/signature_verification/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/signature_verification/Validation%20Predictions.png)

### License

NA