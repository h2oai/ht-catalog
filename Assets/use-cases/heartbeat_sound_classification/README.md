## Use Case 48: Heartbeat Sound Classification

Classify heartbeat sounds into different categories

- `Industry: Healthcare`
- `Problem Type: Audio Classification`
- `Data Type: Audio`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/heartbeat_sound_classification/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/heartbeat_sound_classification/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/heartbeat_sound_classification/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/heartbeat_sound_classification/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/heartbeat_sound_classification/cover)

### Business Problem 

Heartbeat Sound Classification model is a machine learning model designed to classify heartbeat sounds into different categories such as normal heartbeat and abnormal heartbeats. The model is trained on a dataset of heartbeat sounds, which includes recordings of both healthy and unhealthy heartbeats. By analyzing the sound patterns in the recordings, the model can accurately classify the heartbeat sounds into their respective categories.The potential use cases of this model include early detection of heart problems, remote monitoring of heart health, and improving the accuracy of medical diagnoses. The model can be integrated into healthcare systems and wearable devices to provide real-time analysis of heartbeat sounds and alert medical professionals to any abnormalities.

Heartbeat sound classification has significant implications in healthcare and medical diagnostics. By analyzing audio data of heartbeat sounds, machine learning algorithms can classify and identify abnormal heart patterns or conditions. Accurate heartbeat sound classification aids in early detection of cardiac abnormalities, assisting medical professionals in diagnosing cardiovascular diseases and providing timely interventions. It contributes to improved patient care, personalized treatment plans, and better management of heart-related conditions. Heartbeat sound classification technology enhances diagnostic capabilities, supports preventive healthcare, and improves patient outcomes in cardiology.

### Dataset

832 train images with their labels (artifact,extrastole,murmur,normal,unlabel)
Dataset path: s3://apac-cds/ht_datasets/image_classification/heartbeat_sound_classification.zip

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/heartbeat_sound_classification/train%20data.png)

### Model Training

Objective: Classify heartbeat sounds into different categories

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
    sample_rate: 4000
    spectrogram_normalization: 'No'
    stft_window_size: 2048
    training_chunk_seconds: 28
augmentation:
    mix_audio: Disabled
    mix_concentration: 1.0
    mix_iterations: 1
    mix_probability: 1.0
    mix_target: Ratio
dataset:
    audio_column: audio
    data_folder: data/anon/heartbeat_sound_classification/Heartbeat_Sound/
    data_folder_test: None
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '0'
    group_fold_column: audio
    label_columns:
    - class
    test_dataframe: None
    train_dataframe: data/anon/heartbeat_sound_classification/train.pq
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
experiment_name: heartbeat_sound_classification
logging:
    logger: None
    neptune_project: ''
    number_of_audios: 8
prediction:
    inference_chunk_method: Fix
    inference_chunk_seconds: 28
    max_inference_chunk_seconds: 600
    metric: ROC_AUC
    probability_threshold: 0.5
training:
    automatically_adjust_batch_size: false
    batch_size: 32
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/heartbeat_sound_classification/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/heartbeat_sound_classification/Validation%20Predictions.png)

### License

CC0: Public Domain
