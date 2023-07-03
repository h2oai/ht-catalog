## Use Case 41: Driving Lane Detection

Identify and segment the lanes on the road

- `Industry: Government`
- `Problem Type: Image Segmentation`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/lane_detection_for_driving/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/lane_detection_for_driving/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/lane_detection_for_driving/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/lane_detection_for_driving/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/lane_detection_for_driving/cover)

### Business Problem 

Lane detection for driving is a technique used in autonomous vehicles to identify and track the lanes on the road. This is done using image segmentation, where the lanes are isolated from the rest of the image. The lane detection model analyzes the input image, identifies the lane markers, and generates an output image with the lane markers highlighted. This information is then used by the autonomous vehicle to maintain its position within the lane and navigate the road safely. Lane detection is a critical component of autonomous driving, as it helps ensure the safety of passengers and other drivers on the road.

### Impact

Lane detection technology has a significant impact on the field of autonomous driving, advanced driver-assistance systems (ADAS), and road safety. By analyzing live or recorded video feeds from cameras mounted on vehicles, it enables the detection and tracking of lane markings on the road. Accurate lane detection assists in vehicle positioning, lane keeping, and autonomous navigation. It enhances road safety by providing warnings and assistance to drivers in maintaining their lanes. Lane detection technology contributes to the development of safer and more efficient transportation systems, reducing the risk of accidents and improving traffic flow.

### Dataset

3075 train images and 129 test images with 3 uniques segmentation labels ['left-lane' 'right-lane' 'background'] 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/lane_detection_for_driving/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Identify and segment the lanes on the road

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    architecture: Unet
    backbone: resnet34
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
    data_folder: data/anon/lane-detection/train/
    data_folder_test: data/anon/lane-detection/val/
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '4'
    group_fold_column: image
    image_column: image
    rle_mask_column: rle_mask
    test_dataframe: data/anon/lane-detection/test.pq
    train_dataframe: data/anon/lane-detection/train.pq
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
experiment_name: lane-detection
image:
    image_channels: 3
    image_height: 256
    image_normalization: Simple
    image_width: 256
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/lane_detection_for_driving/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/lane_detection_for_driving/Validation%20Predictions.png)

### License

CC BY-NC-SA 4.0

### Acknowledgements

Original dataset source is https://www.kaggle.com/datasets/thomasfermi/lane-detection-for-carla-driving-simulator
