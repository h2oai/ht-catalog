## Use Case 89: Speaker Recognition

Identify and verify individuals based on vocal characteristics or speech patterns

- `Industry: Banking`
- `Problem Type: Audio Classification`
- `Data Type: Audio`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/speaker_recognition/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/speaker_recognition/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/speaker_recognition/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/speaker_recognition/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/speaker_recognition/cover)

### Business Problem 

Speaker recognition refers to the identification and verification of individuals based on their unique vocal characteristics or speech patterns. This technology analyzes voice signals, speaker-specific features, and linguistic patterns to establish the identity of a speaker, facilitating applications such as access control, voice authentication, and forensic investigations.

Speaker recognition has significant business implications in various industries, including security, telecommunications, and customer service. By accurately identifying and verifying individuals based on their unique vocal characteristics, this technology enhances access control systems, voice authentication processes, and fraud prevention measures. It enables secure transactions, personalized customer experiences, and targeted communication. It finds applications in call centers, voice-based virtual assistants, and telecommunication networks, enhancing operational efficiency and customer satisfaction

### Dataset

2511 train audio samples with 50 different speakers

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/speaker_recognition/train%20data.png)

### Model Training

Objective: Identify and verify individuals based on vocal characteristics or speech patterns

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
    training_chunk_seconds: 60
augmentation:
    mix_audio: Disabled
    mix_concentration: 1.0
    mix_iterations: 1
    mix_probability: 1.0
    mix_target: Ratio
dataset:
    audio_column: audio
    data_folder: data/anon/speaker_recognition/50_speakers_audio_data/
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
    train_dataframe: data/anon/speaker_recognition/train.pq
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
experiment_name: 89_speaker_recognition
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/speaker_recognition/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/speaker_recognition/Validation%20Predictions.png)

### License

Unknown
