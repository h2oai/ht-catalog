## Use Case 52: Spoken Digits Classification

Classify the spoken digits into 0 to 9

- `Industry: Manufacturing`
- `Problem Type: Audio Classification`
- `Data Type: Audio`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/audio_samples_of_spoken_digits/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/audio_samples_of_spoken_digits/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/audio_samples_of_spoken_digits/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/audio_samples_of_spoken_digits/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/audio_samples_of_spoken_digits/cover)

### Business Problem 

The spoken digits classification use case involves developing a machine learning model that can recognize and classify spoken digits. The model takes audio recordings of spoken digits as input and predicts the corresponding digit. This task is commonly used in various applications such as voice assistants, automated phone systems, and speech recognition technologies.

### Impact

Accurate spoken digits classification plays a key role across multiple industries. In the telecommunications sector, it can enhance call routing systems, enabling more efficient and automated customer support. In the finance industry, it can improve the security of voice-based authentication systems. Additionally, in the automotive sector, it can enhance hands-free calling and voice control functionalities in vehicles. By automating the recognition and classification of spoken digits, businesses can streamline operations, improve customer experiences, and enable more seamless interactions through voice interfaces.

### Dataset

Dataset path: s3://h2oai-hydrogen-torch-internal/dev_datasets/amnist_audio_regression.zip

30000 audio samples of spoken digits (0-9) of 60 different speakers. Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/audio_samples_of_spoken_digits/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Classify the spoken digits into 0 to 9

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
    sample_rate: 22050
    spectrogram_normalization: 'No'
    stft_window_size: 2048
    training_chunk_seconds: 1
augmentation:
    mix_audio: Disabled
    mix_concentration: 1.0
    mix_iterations: 1
    mix_probability: 1.0
    mix_target: Ratio
dataset:
    audio_column: audio
    data_folder: data/anon/amnist_audio_regression/amnist_audios/
    data_folder_test: None
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '4'
    group_fold_column: audio
    label_columns:
    - label
    test_dataframe: None
    train_dataframe: data/anon/amnist_audio_regression/amnist_meta.csv
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
experiment_name: 52_ambits
logging:
    logger: None
    neptune_project: ''
    number_of_audios: 8
prediction:
    inference_chunk_method: Fix
    inference_chunk_seconds: 1
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/audio_samples_of_spoken_digits/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/audio_samples_of_spoken_digits/Validation%20Predictions.png)

### License

License Type is Unknown

### Acknowledgements

Original dataset source is Unknown
