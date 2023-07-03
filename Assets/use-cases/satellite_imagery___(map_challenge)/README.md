## Use Case 10: Building Segmentation

Segment buildings in the satellite images

- `Industry: Government`
- `Problem Type: Object Detection`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/satellite_imagery___(map_challenge)/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/satellite_imagery___(map_challenge)/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/satellite_imagery___(map_challenge)/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/satellite_imagery___(map_challenge)/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/satellite_imagery___(map_challenge)/cover)

### Business Problem 

The Building Segmentation in Satellite Images model uses image segmentation techniques to identify and delineate buildings in satellite imagery. The model can be trained on large datasets of satellite images with labeled building boundaries to learn to recognize building features such as roofs, walls, and windows. Once trained, the model can quickly and segment buildings in new satellite images, making it a tool for applications such as urban planning, disaster response, and environmental monitoring. By automating the process of building segmentation, this model can save time and resources compared to traditional manual method

### Impact

Building segmentation in images has significant implications in the fields of architecture, real estate, and urban planning. By automatically segmenting buildings in images, this technology assists in architectural design and visualization, allowing architects and designers to create accurate 3D models and renderings. Real estate professionals can leverage building segmentation to identify property boundaries, evaluate property features, and enhance marketing materials. Urban planners can utilize this technology to analyze building density, monitor urban growth, and make informed decisions regarding zoning and land use. Building segmentation contributes to more efficient urban development and improved decision-making processes in the built environment.

### Dataset

8366 train images with their object coordinates 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/satellite_imagery___(map_challenge)/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Segment buildings in the satellite images

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
    class_name_column: name
    data_folder: data/anon/mapping_challenge_v2/images/
    data_folder_test: data/anon/mapping_challenge_v2/images/
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '4'
    group_fold_column: file_name
    image_column: file_name
    test_dataframe: None
    train_dataframe: data/anon/mapping_challenge_v2/train.pq
    unlabeled_dataframe: None
    validation_dataframe: None
    validation_size: 0.2
    validation_strategy: kfold
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
experiment_name: mapping_challenge.1
image:
    image_channels: 3
    image_height: 1024
    image_normalization: Simple
    image_width: 1024
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
    batch_size: 12
    box_loss_weight: 50
    build_scoring_pipelines: true
    calculate_train_metric: false
    differential_learning_rate: 0.001
    differential_learning_rate_layers: []
    drop_last_batch: true
    epochs: 8
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/satellite_imagery___(map_challenge)/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/satellite_imagery___(map_challenge)/Validation%20Predictions.png)

### License

License Type is Unknown

### Acknowledgements

Original dataset source is https://www.aicrowd.com/challenges/mapping-challenge
