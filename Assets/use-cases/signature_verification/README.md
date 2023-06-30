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

Signature verification model is designed to ensure the authenticity and security of legal, financial, and personal transactions. By identifying and authenticating signatures, this model helps prevent fraud and identity theft.

### Impact

The utilization of computer vision techniques for signature verification, particularly through the comparison of a signature with historical signatures, has a significant impact on various aspects of business operations. In sectors such as banking and financial services, this approach plays a crucial role in fortifying fraud prevention efforts by accurately validating signatures on checks, contracts, and financial documents. By doing so, it effectively minimizes the possibility of unauthorized transactions. Similarly, the legal sector benefits greatly from the streamlined authentication and integrity of documents, thereby ensuring the legitimacy of legal agreements and reducing the occurrence of legal disputes. Healthcare organizations heavily rely on signature verification to authenticate patient consent forms and medical records, ensuring adherence to regulations and promoting an elevated level of patient safety. Moreover, government agencies find signature verification invaluable in validating vital documents, thereby significantly mitigating the risk of forgery and reinforcing the credibility of administrative processes. Ultimately, the implementation of signature verification techniques provides businesses with heightened security measures, improved compliance, and increased operational efficiency.

### Dataset

Dataset path: s3://apac-cds/ht_datasets/sign_verification/sign_verification.zip

1100 train images with 55 unique labels. Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/signature_verification/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

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

### Acknowledgements

The original dataset used in this use case comes from this source : https://paperswithcode.com/dataset/cedar-signature
