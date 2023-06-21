## Use Case 38: Urban Sound Classification

Classify categories of audio signals in the urban environments

- `Industry: Government`
- `Problem Type: Audio Classification`
- `Data Type: Audio`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/urban_sound_classification/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/urban_sound_classification/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/urban_sound_classification/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/urban_sound_classification/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/urban_sound_classification/cover)

### Business Problem 

The Urban Sound Classification model is designed to classify audio signals into different sound categories commonly heard in urban environments such as sirens, car horns, and street music. The model uses audio signal processing techniques and machine learning algorithms to extract features such as frequency, pitch, and amplitude from audio samples and then trains a classifier to recognize patterns in these features and categorize them into their respective sound classes. The model has applications in noise pollution monitoring, city planning, and urban soundscape analysis.

Urban sound classification has practical applications in urban planning, noise pollution management, and public health. By analyzing audio recordings using machine learning algorithms, it enables the classification and identification of different urban sounds, such as traffic noise, sirens, construction noise, and public transport sounds. Accurate urban sound classification aids in assessing noise pollution levels, identifying noise sources, and implementing mitigation strategies. It supports urban planning initiatives, noise regulation enforcement, and the improvement of living conditions in urban areas. Urban sound classification technology contributes to creating healthier and more livable cities.

### Dataset

8732 train images with 10 uniques labels
Dataset path: s3://apac-cds/ht_datasets/audio_classification/urban_sound_classification.zip

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/urban_sound_classification/train%20data.png)

### Model Training

Objective: Classify categories of audio signals in the urban environments

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
    audio_column: slice_file_name
    data_folder: data/anon/urban_sound_classification/data/
    data_folder_test: None
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '10'
    group_fold_column: slice_file_name
    label_columns:
    - class
    test_dataframe: None
    train_dataframe: data/anon/urban_sound_classification/UrbanSound8K.pq
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
experiment_name: urban_sound_classification
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/urban_sound_classification/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/urban_sound_classification/Validation%20Predictions.png)

### License

 CC BY-NC 3.0
