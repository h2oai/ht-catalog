## Use Case 101: Deforestation Segmentation

Segment deforested areas with multi-modal satellite imagery

- `Industry: AI4Good`
- `Problem Type: Image Segmentation`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/78d74498d8534193d3208f31a38cc0aa936d3f86/Assets/use-cases/deforestation_segmentation/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/78d74498d8534193d3208f31a38cc0aa936d3f86/Assets/use-cases/deforestation_segmentation/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/78d74498d8534193d3208f31a38cc0aa936d3f86/Assets/use-cases/deforestation_segmentation/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/78d74498d8534193d3208f31a38cc0aa936d3f86/Assets/use-cases/deforestation_segmentation/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/78d74498d8534193d3208f31a38cc0aa936d3f86/Assets/use-cases/deforestation_segmentation/cover)

### Business Problem 

Deforestation estimation in the Amazon forest poses a significant challenge due to the vast size of the area and the limited accessibility for direct human observation. To effectively address this problem, multi-modal satellite imagery and remote sensing offer a promising solution for estimating deforestation. Our model achieves high precision deforestation estimation on unseen images from the region.

### Impact

The Amazon forest encompasses approximately 40% of the remaining rainforests in the world. Unfortunately, deforestation in the Amazon is reaching dangerous levels. In August 2022, deforestation in the Amazon was 1,661 km2, an amount 81% higher than that recorded in August last year. Multi-modal satellite imagery offer a powerful alternative for monitoring deforestation near real-time.

### Dataset

Dataset link - [s3://0xdata-public/beluga/wildfire/full_r6_image_semantic_segmentation.zip](https://0xdata-public.s3.amazonaws.com/beluga/wildfire/full_r6_image_semantic_segmentation.zip)

8866 train images and 1200 validation multi-modal images from various Sentinel-1, Sentinel-2, and Landsat-8 snapshots combined up to 152 channels. 

![train data](https://github.com/h2oai/ht-catalog/blob/78d74498d8534193d3208f31a38cc0aa936d3f86/Assets/use-cases/deforestation_segmentation/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Segment deforested areas with multi-modal satellite imagery

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    architecture: Unet
    backbone: efficientnet-b3
    pretrained: true
augmentation:
    augmentations_strategy: Custom
    custom_inference_augmentations: '{"__version__": "1.1.0", "transform": {"__class_fullname__":
        "Compose", "p": 1.0, "transforms": [{"__class_fullname__": "Resize", "always_apply":
        true, "p": 1, "height": IMAGE_HEIGHT, "width": IMAGE_WIDTH, "interpolation":
        1}], "bbox_params": null, "keypoint_params": null, "additional_targets": {}}}'
    custom_train_augmentations: '{"__version__": "1.1.0", "transform": {"__class_fullname__":
        "Compose", "p": 1.0, "transforms": [{"__class_fullname__": "Resize", "always_apply":
        true, "p": 1, "height": IMAGE_HEIGHT, "width": IMAGE_WIDTH, "interpolation":
        1}, {"__class_fullname__": "HorizontalFlip", "always_apply": false, "p": 0.5},
        {"__class_fullname__": "VerticalFlip", "always_apply": false, "p": 0.5}, {"__class_fullname__":
        "RandomRotate90", "always_apply": false, "p": 0.5}], "bbox_params": null,
        "keypoint_params": null, "additional_targets": {}}}'
    cutmix_corner: false
    mix_concentration: 1.0
    mix_image: Disabled
    mix_iterations: 1
    mix_probability: 1.0
    mix_target: Ratio
dataset:
    class_name_column: class_id
    data_folder: data/user/full_r6_image_semantic_segmentation/full_r6/images/
    data_folder_test: data/user/full_r6_image_semantic_segmentation/full_r6/images/
    data_sample: 1.0
    data_sample_choice:
    - Train
    - Validation
    group_fold_column: image_path
    image_column: image_path
    rle_mask_column: rle_mask
    selected_folds:
    - '0'
    test_dataframe: None
    train_dataframe: data/user/full_r6_image_semantic_segmentation/full_r6/train_df_s2.pq
    validation_dataframe: data/user/full_r6_image_semantic_segmentation/full_r6/valid_df_s2.pq
    validation_size: 0.2
    validation_strategy: custom
environment:
    gpus:
    - '0'
    - '1'
    - '2'
    mixed_precision_inference: false
    mixed_precision_training: true
    number_of_gpus_per_run: 3
    number_of_seeds_per_run: 1
    number_of_workers: 4
    seed: -1
    sync_batch_normalization: false
experiment_name: baseline_s2.1
image:
    image_channels: 152
    image_height: 256
    image_normalization: Simple
    image_width: 256
logging:
    log_grad_norm: false
    logger: None
    neptune_project: ''
prediction:
    batch_size_inference: 0
    metric: IoU
    probability_threshold: 0.5
    test_time_augmentations: []
training:
    automatically_adjust_batch_size: true
    batch_size: 16
    bce_weight: 1.0
    build_scoring_pipelines: false
    calculate_train_metric: false
    dice_weight: 1.0
    differential_learning_rate: 0.001
    differential_learning_rate_layers: []
    drop_last_batch: true
    epochs: 8
    evaluate_before_training: false
    evaluation_epochs: 1
    focal_weight: 1.0
    grad_accumulation: 1
    gradient_clip: 0.0
    learning_rate: 0.0005
    loss_function: BCEDice
    lovasz_weight: 1.0
    optimizer: AdamW
    save_best_checkpoint: false
    schedule: Cosine
    train_validation_data: false
    warmup_epochs: 0.0
    weight_decay: 0.0
```

![chart](https://github.com/h2oai/ht-catalog/blob/78d74498d8534193d3208f31a38cc0aa936d3f86/Assets/use-cases/deforestation_segmentation/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/78d74498d8534193d3208f31a38cc0aa936d3f86/Assets/use-cases/deforestation_segmentation/Validation%20Predictions.png)

### License

CC BY 4.0

### Acknowledgements

Original dataset source is https://sites.google.com/view/rainforest-challenge/multiearth-2023
