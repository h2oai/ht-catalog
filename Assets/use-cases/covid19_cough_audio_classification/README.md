## Use Case 71: Covid-19 Cough Audio Regression

Predict the severity of cough using cough audio

- `Industry: Healthcare`
- `Problem Type: Audio Regression`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/covid19_cough_audio_classification/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/covid19_cough_audio_classification/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/covid19_cough_audio_classification/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/covid19_cough_audio_classification/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/covid19_cough_audio_classification/cover)

### Business Problem 

Cough audio regression in COVID data involves the analysis and regression of cough sounds recorded from individuals with COVID-19. This solution aims to identify and quantify different acoustic features of coughs, allowing for the assessment and prediction of disease severity, progression, and potential complications.

### Impact

Cough audio regression in COVID data has substantial role in the healthcare sector. By accurately quantifying cough characteristics and analyzing disease progression, this technology aids in assessing the severity of COVID-19 cases, predicting potential complications, and monitoring treatment effectiveness. It enables healthcare providers to make informed decisions about patient management, allocate resources efficiently, and provide personalized care, ultimately leading to improved patient outcomes and optimized healthcare delivery.

### Dataset

Dataset path: s3://apac-cds/ht_datasets/audio_regression/covid19-cough-audio-classification.zip

25985 train audio samples with their values. Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/covid19_cough_audio_classification/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Predict the severity of cough using cough audio

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    backbone: resnet50
    dropout: 0.2
    pool: Average
    pretrained: true
audio:
    audio_parameters: Auto
    hop_size: 512
    maximum_frequency: 24000
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
    audio_column: filename
    data_folder: data/user/covid19-cough-audio-classification/covid19-cough-audio-classification/
    data_folder_test: None
    data_sample: 0.8
    data_sample_choice:
    - Train
    - Validation
    group_fold_column: datetime
    label_columns:
    - cough_detected
    selected_folds:
    - '0'
    test_dataframe: None
    train_dataframe: data/user/covid19-cough-audio-classification/audio.csv
    unlabeled_dataframe: None
    validation_dataframe: None
    validation_size: 0.2
    validation_strategy: kfold
environment:
    gpus:
    - '0'
    mixed_precision_inference: false
    mixed_precision_training: true
    number_of_seeds_per_run: 1
    number_of_workers: 4
    seed: -1
experiment_name: 71_covid19_cough_audio_regression
logging:
    log_grad_norm: false
    logger: None
    neptune_project: ''
    number_of_audios: 8
prediction:
    inference_chunk_method: Fix
    inference_chunk_seconds: 60
    max_inference_chunk_seconds: 600
    metric: MAE
training:
    automatically_adjust_batch_size: false
    batch_size: 13
    build_scoring_pipelines: true
    calculate_train_metric: false
    differential_learning_rate: 0.001
    differential_learning_rate_layers: []
    drop_last_batch: true
    epochs: 2
    evaluate_before_training: false
    evaluation_epochs: 1
    grad_accumulation: 1
    gradient_clip: 0.0
    learning_rate: 0.01
    loss_function: MAE
    optimizer: AdamW
    run_interpretations: true
    save_best_checkpoint: false
    schedule: Cosine
    train_validation_data: false
    warmup_epochs: 0
    weight_decay: 0.0

```

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/covid19_cough_audio_classification/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/covid19_cough_audio_classification/Validation%20Predictions.png)

### License

CC BY-SA 4.0

### Acknowledgements

Original dataset source is https://www.nature.com/articles/s41597-021-00937-4
