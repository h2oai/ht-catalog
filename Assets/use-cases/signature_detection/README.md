## Use Case 1: Document Signature Detection

Detect signatures in the digital documents

- `Industry: Banking`
- `Problem Type: Object Detection`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/tree/main/Assets/use-cases/signature_detection/cover.png)
![](https://github.com/h2oai/ht-catalog/tree/main/Assets/use-cases/signature_detection/cover.jpg)
![](https://github.com/h2oai/ht-catalog/tree/main/Assets/use-cases/signature_detection/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/tree/main/Assets/use-cases/signature_detection/cover.webp)
![](https://github.com/h2oai/ht-catalog/tree/main/Assets/use-cases/signature_detection/cover)

### Business Problem 

The signature detection model automates signature detection in large volumes of documents, saving time and reducing errors. It offers a faster and more accurate alternative to manual detection, verifying authenticity, identifying forgeries, and detecting potential fraud

Signature detection in documents has a significant business impact across various industries. In the financial sector, accurate signature detection enables fraud prevention and identity verification, safeguarding transactions and protecting against financial losses. It streamlines the legal industry by simplifying the validation of legal documents, reducing the risk of fraudulent claims, and improving overall efficiency. In healthcare, signature detection ensures proper patient consent verification, enhancing regulatory compliance and patient safety. Additionally, in logistics and supply chain management, signature detection facilitates the verification of delivery receipts and shipping documents, reducing disputes and improving supply chain transparency. Government agencies and administrative departments benefit from signature detection by ensuring the authenticity of official documents, licenses, and permits, improving data integrity and compliance.

### Dataset

1000 train images with their masks

![train data](https://github.com/h2oai/ht-catalog/tree/main/Assets/use-cases/signature_detection/train%20data.png)

### Model Training

Objective: Detect signatures in the digital documents

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    anchor_aspect_ratios:
    - '1.0'
    - '2.0'
    - '0.5'
    anchor_iou_match_threshold: 0.5
    anchor_num_scales: 3
    anchor_scale: 4
    backbone: tf_efficientdet_d0
    drop_path_rate: Default
    pretrained: true
augmentation:
    augmentations_strategy: Soft
    custom_inference_augmentations: '{"__version__": "1.1.0", "transform": {"__class_fullname__":
        "Compose", "p": 1.0, "transforms": [{"__class_fullname__": "Resize", "always_apply":
        true, "p": 1, "height": IMAGE_HEIGHT, "width": IMAGE_WIDTH, "interpolation":
        1}], "bbox_params": {"format": "pascal_voc", "label_fields": ["labels"], "min_area":
        0, "min_visibility": 0, "check_each_transform": true}, "keypoint_params":
        null, "additional_targets": {}}}'
    custom_train_augmentations: '{"__version__": "1.1.0", "transform": {"__class_fullname__":
        "Compose", "p": 1.0, "transforms": [{"__class_fullname__": "Resize", "always_apply":
        true, "p": 1, "height": IMAGE_HEIGHT, "width": IMAGE_WIDTH, "interpolation":
        1}], "bbox_params": {"format": "pascal_voc", "label_fields": ["labels"], "min_area":
        0, "min_visibility": 0, "check_each_transform": true}, "keypoint_params":
        null, "additional_targets": {}}}'
    mix_concentration: 1.0
    mix_image: Disabled
    mix_iterations: 1
    mix_probability: 1.0
dataset:
    class_name_column: class_id
    data_folder: data/anon/signature_object_detection_v2/images/
    data_folder_test: None
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '0'
    group_fold_column: image
    image_column: image
    test_dataframe: None
    train_dataframe: data/anon/signature_object_detection_v2/train2.pq
    unlabeled_dataframe: None
    validation_dataframe: data/anon/signature_object_detection_v2/val2.pq
    validation_size: 0.2
    validation_strategy: custom
    x_max_column: x_max
    x_min_column: x_min
    y_max_column: y_max
    y_min_column: y_min
environment:
    gpus:
    - '0'
    mixed_precision_inference: false
    mixed_precision_training: true
    number_of_workers: 4
    seed: -1
experiment_name: signature_object_detection
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
    max_det_per_image: 100
    metric: mAP
    metric_iou_threshold: 0.5
    nms_iou_threshold: 0.5
    probability_threshold: 0.3
training:
    automatically_adjust_batch_size: false
    batch_size: 16
    box_loss_weight: 50
    build_scoring_pipelines: true
    calculate_train_metric: false
    differential_learning_rate: 0.001
    differential_learning_rate_layers: []
    drop_last_batch: true
    epochs: 5
    evaluation_epochs: 1
    focal_cls_loss_alpha: 0.25
    focal_cls_loss_gamma: 1.5
    grad_accumulation: 1
    gradient_clip: 0.0
    learning_rate: 0.001
    optimizer: AdamW
    save_best_checkpoint: false
    schedule: Cosine
    train_validation_data: false
    warmup_epochs: 0
    weight_decay: 0.0

```

![chart](https://github.com/h2oai/ht-catalog/tree/main/Assets/use-cases/signature_detection/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/tree/main/Assets/use-cases/signature_detection/Validation%20Predictions.png)

### License

NA

