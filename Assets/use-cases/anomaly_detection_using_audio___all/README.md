## Use Case 100: Audio Anonmaly Detection

Classifies the audio segments into 4 machine parts: valve, fan, slider and pump

- `Industry: Manufacturing`
- `Problem Type: Audio Classification`
- `Data Type: Audio`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/anomaly_detection_using_audio___all/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/anomaly_detection_using_audio___all/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/anomaly_detection_using_audio___all/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/anomaly_detection_using_audio___all/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/anomaly_detection_using_audio___all/cover)

### Business Problem 

Anomaly detection using audio-fan involves analyzing the sound patterns produced by a fan to identify any abnormal or unusual behavior. By capturing and processing the audio signals emitted by the fan, anomalies such as mechanical faults, bearing wear, or other malfunctions can be detected. The audio data is collected continuously or periodically from the fan, and machine learning algorithms are applied to classify normal and anomalous sound patterns. This enables proactive maintenance, as anomalies can be detected early, minimizing downtime and preventing further damage.

Implementing anomaly detection using audio - all can have a broad business impact across industries where multiple components or systems are critical for operations. By integrating audio analysis from various sources, potential failures or abnormalities can be detected holistically, improving overall equipment reliability and operational efficiency. Proactive maintenance based on anomaly detection helps prevent costly breakdowns, reduces downtime, and enhances safety. Additionally, this comprehensive approach allows for optimized resource allocation, as maintenance activities can be scheduled based on the detected anomalies across multiple components or systems.

### Dataset

NA

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/anomaly_detection_using_audio___all/train%20data.png)

### Model Training

Objective: Classifies the audio segments into 4 machine parts: valve, fan, slider and pump

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    backbone: resnet34
    dropout: 0
    pool: GeM
    pretrained: false
audio:
    audio_parameters: Manual
    hop_size: 512
    maximum_frequency: 16000
    mel_frequency_bins: 128
    minimum_frequency: 50
    sample_rate: 22050
    spectrogram_normalization: 'No'
    stft_window_size: 2048
    training_chunk_seconds: 10
augmentation:
    mix_audio: Disabled
    mix_concentration: 1.0
    mix_iterations: 1
    mix_probability: 1.0
    mix_target: Ratio
dataset:
    audio_column: audio
    data_folder: data/anon/audio_classification_all_1/sound_data_all/
    data_folder_test: data/anon/audio_classification_all_1/sound_data_all/
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '4'
    group_fold_column: 'Unnamed: 0'
    label_columns:
    - label
    test_dataframe: None
    train_dataframe: data/anon/audio_classification_all_1/audio_dataset_all_1.csv
    unlabeled_dataframe: None
    validation_dataframe: data/anon/audio_classification_all_1/audio_dataset_all_val_1.csv
    validation_size: 0.2
    validation_strategy: kfold
environment:
    gpus:
    - '0'
    mixed_precision_inference: false
    mixed_precision_training: true
    number_of_workers: 4
    seed: -1
experiment_name: final_machinetype_audio_classification
logging:
    logger: None
    neptune_project: ''
    number_of_audios: 8
prediction:
    inference_chunk_method: Fix
    inference_chunk_seconds: 5
    max_inference_chunk_seconds: 600
    metric: F1
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
    weight_decay: 0

```

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/anomaly_detection_using_audio___all/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/anomaly_detection_using_audio___all/Validation%20Predictions.png)

### License

CC BY-SA 4.0
