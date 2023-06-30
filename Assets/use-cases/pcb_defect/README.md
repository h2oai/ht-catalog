## Use Case 25: PCB Defect Detection

Detect and classify the defects in Printed Circuit Boards

- `Industry: Manufacturing `
- `Problem Type: Object Detection`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/pcb_defect/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/pcb_defect/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/pcb_defect/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/pcb_defect/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/pcb_defect/cover)

### Business Problem 

The PCB Defect model was created using a public synthetic dataset containing 1386 images with 6 different types of defects found in printed circuit boards (PCBs). The aim of this model is to detect and classify these defects, which include missing holes, mouse bites, open circuits, shorts, spurs, and spurious copper. The model was trained using deep learning algorithms and image processing techniques to identify the specific characteristics of each defect type and classify them accordingly. The model is designed to aid in quality control and product analysis in the electronics industry, ensuring that PCBs meet high standards and are free from defects that could affect their performance.

### Impact

PCB (Printed Circuit Board) defect detection is crucial in the electronics manufacturing industry. By employing advanced computer vision techniques, it enables the automated identification of defects in PCBs, such as short circuits, open circuits, or component misalignment. Timely detection of such defects during the production process ensures the delivery of reliable and high-quality electronic devices. PCB defect detection technology reduces production costs by minimizing the need for manual inspection and rework. It enhances manufacturing efficiency, speeds up the production cycle, and reduces the risk of faulty electronic products reaching the market. Overall, PCB defect detection improves product quality, customer satisfaction, and business competitiveness in the electronics industry.

### Dataset

Dataset path: s3://apac-cds/ht_datasets/object_detection/pcb_defect.zip

1500 images with their object labels ['open' 'short' 'mousebite' 'spur' 'copper' 'pin-hole']  Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/pcb_defect/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Detect and classify the defects in Printed Circuit Boards

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
    class_name_column: type
    data_folder: data/anon/pcb_defect/images/
    data_folder_test: data/anon/pcb_defect/images/
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '0'
    group_fold_column: filename
    image_column: filename
    test_dataframe: None
    train_dataframe: data/anon/pcb_defect/train.pq
    unlabeled_dataframe: None
    validation_dataframe: None
    validation_size: 0.2
    validation_strategy: kfold
    x_max_column: x2
    x_min_column: x1
    y_max_column: y2
    y_min_column: y1
environment:
    gpus:
    - '0'
    mixed_precision_inference: false
    mixed_precision_training: true
    number_of_workers: 4
    seed: -1
experiment_name: pcb_defect_object_detection
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/pcb_defect/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/pcb_defect/Validation%20Predictions.png)

### License

MIT License

### Acknowledgements

The original dataset used in this use case comes from this source : https://arxiv.org/abs/1902.06197
