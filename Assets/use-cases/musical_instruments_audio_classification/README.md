## Use Case 85: Music Instrument Classification

Classify musical instruments based on audio recordings

- `Industry: Media`
- `Problem Type: Audio Classification`
- `Data Type: Audio`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/musical_instruments_audio_classification/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/musical_instruments_audio_classification/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/musical_instruments_audio_classification/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/musical_instruments_audio_classification/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/musical_instruments_audio_classification/cover)

### Business Problem 

Musical instruments audio classification involves the automatic recognition and classification of different musical instruments based on audio recordings. This technology analyzes acoustic features and timbral characteristics to distinguish between instruments, facilitating tasks such as instrument identification, music transcription, and sound synthesis.

Musical instruments audio classification has business implications in various industries, including music production, entertainment, and e-commerce. By automatically recognizing and classifying different musical instruments based on audio recordings, this technology enhances music transcription, instrument identification, and sound synthesis. Music producers can optimize their production workflows, create more immersive sound experiences, and develop innovative music technologies. E-commerce platforms can provide targeted recommendations and personalized shopping experiences for musical instrument enthusiasts, driving customer engagement and sales.

### Dataset

2629 train audio samples with 4 classes.
Dataset path: s3://apac-cds/ht_datasets/audio_classification/musical_instruments_audio_classification.zip

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/musical_instruments_audio_classification/train%20data.png)

### Model Training

Objective: Classify musical instruments based on audio recordings

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
    training_chunk_seconds: 60
augmentation:
    mix_audio: Disabled
    mix_concentration: 1.0
    mix_iterations: 1
    mix_probability: 1.0
    mix_target: Ratio
dataset:
    audio_column: FileName
    data_folder: data/anon/musical_instruments_audio_classification/Train_submission/
    data_folder_test: data/anon/musical_instruments_audio_classification/Test_submission/
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '4'
    group_fold_column: FileName
    label_columns:
    - Class
    test_dataframe: data/anon/musical_instruments_audio_classification/Metadata_Test.csv
    train_dataframe: data/anon/musical_instruments_audio_classification/Metadata_Train.csv
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
experiment_name: 85_musical_instruments_audio_classification
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
    batch_size: 8
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/musical_instruments_audio_classification/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/musical_instruments_audio_classification/Validation%20Predictions.png)

### License

CC0: Public Domain
