## Use Case 88: Siren Sounds Classification

Detect and classify emergency vehicle siren sounds from audio data

- `Industry: Government`
- `Problem Type: Audio Classification`
- `Data Type: Audio`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/emergency_vehicle_siren_sounds/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/emergency_vehicle_siren_sounds/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/emergency_vehicle_siren_sounds/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/emergency_vehicle_siren_sounds/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/emergency_vehicle_siren_sounds/cover)

### Business Problem 

Emergency vehicle siren sounds detection involves the automated identification and classification of siren sounds emitted by emergency vehicles, such as police cars, ambulances, or fire trucks. This technology utilizes audio analysis and pattern recognition techniques to distinguish emergency vehicle sirens from background noise, enabling timely response and efficient traffic management

### Impact

The usefulness emergency vehicle siren sounds detection is vital in traffic management and emergency response systems. By automatically identifying and detecting emergency vehicle sirens from audio data, this technology enables efficient traffic routing, timely emergency response, and improved road safety. It optimizes emergency vehicle dispatching, reduces response times, and minimizes traffic congestion. It contributes to faster emergency assistance, enhances public safety, and supports effective urban planning.

### Dataset

Dataset path: s3://apac-cds/ht_datasets/audio_classification/emergency-vehicle-siren-sounds.zip

600 train audio samples with 3 different labels such as ambulance,traffic,firetruck. Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/emergency_vehicle_siren_sounds/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Detect and classify emergency vehicle siren sounds from audio data

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
    sample_rate: 44100
    spectrogram_normalization: 'No'
    stft_window_size: 2048
    training_chunk_seconds: 4
augmentation:
    mix_audio: Disabled
    mix_concentration: 1.0
    mix_iterations: 1
    mix_probability: 1.0
    mix_target: Ratio
dataset:
    audio_column: audio
    data_folder: data/anon/emergency-vehicle-siren-sounds/sounds/
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
    train_dataframe: data/anon/emergency-vehicle-siren-sounds/train.pq
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
experiment_name: 88_vehicle-siren-sounds
logging:
    logger: None
    neptune_project: ''
    number_of_audios: 8
prediction:
    inference_chunk_method: Fix
    inference_chunk_seconds: 4
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/emergency_vehicle_siren_sounds/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/emergency_vehicle_siren_sounds/Validation%20Predictions.png)

### License

Other
