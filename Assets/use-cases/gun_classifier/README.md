## Use Case 87: Gun Type Classification

Recognize and classify firearms or gun-related objects from images or video data

- `Industry: Government`
- `Problem Type: Audio Classification`
- `Data Type: Audio`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/gun_classifier/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/gun_classifier/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/gun_classifier/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/gun_classifier/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/gun_classifier/cover)

### Business Problem 

Gun classifier refers to the automated recognition and classification of firearms or gun-related objects from images or video data. The solution approach employs computer vision algorithms and deep learning models to identify and distinguish between different types of guns, aiding in security applications, law enforcement, and public safety efforts

### Impact

Gun type classification use-case is highly beneficial in security and public safety industries. By automatically recognizing and classifying firearms or gun-related objects from images or video data, this technology aids in threat detection, security screening, and law enforcement efforts. It enhances public safety measures, supports security personnel in identifying potential risks, and contributes to crime prevention. Deploying gun classifiers in critical infrastructure, public spaces, or high-risk areas helps mitigate security threats, safeguarding individuals and assets.

### Dataset

Dataset path: s3://apac-cds/ht_datasets/audio_classification/Gun_sound_detection.zip

851 train audio samples with 9 different classes. Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/gun_classifier/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Recognize and classify firearms or gun-related objects from images or video data

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    backbone: resnet50
    dropout: 0
    pool: Average
    pretrained: true
audio:
    audio_parameters: Auto
    hop_size: 512
    maximum_frequency: 16000
    mel_frequency_bins: 128
    minimum_frequency: 50
    sample_rate: 48000
    spectrogram_normalization: 'No'
    stft_window_size: 2048
    training_chunk_seconds: 60
augmentation:
    mix_audio: Disabled
    mix_concentration: 1.0
    mix_iterations: 1
    mix_probability: 1.0
    mix_target: Ratio
dataset:
    audio_column: image
    data_folder: data/anon/Gun_sound_detection/Gun_Classifier/
    data_folder_test: None
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '4'
    group_fold_column: image
    label_columns:
    - class
    test_dataframe: None
    train_dataframe: data/anon/Gun_sound_detection/train.pq
    unlabeled_dataframe: None
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
experiment_name: 87_gun_sound_classification
logging:
    logger: None
    neptune_project: ''
    number_of_audios: 8
prediction:
    inference_chunk_method: Fix
    inference_chunk_seconds: 60
    max_inference_chunk_seconds: 600
    metric: ROC_AUC
    probability_threshold: 0.5
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
    loss_function: BCE
    optimizer: AdamW
    run_interpretations: true
    save_best_checkpoint: false
    schedule: Cosine
    train_validation_data: false
    warmup_epochs: 0
    weight_decay: 0.0

```

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/gun_classifier/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/gun_classifier/Validation%20Predictions.png)

### License

Unknown
