## Use Case 20: Whale Audio Detection

Identify whether an audio signal is related to a whale or not

- `Industry: AI4Good`
- `Problem Type: Audio Classification`
- `Data Type: Audio`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/whale_detection/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/whale_detection/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/whale_detection/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/whale_detection/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/whale_detection/cover)

### Business Problem 

Whale detection model using audio data is designed to identify and classify sounds emitted by whale. This model can be used by marine biologists and researchers to study whale behavior, migration patterns, and population dynamics. By analyzing the acoustic features of whale sounds such as frequency, duration, and amplitude, the model can identify whale. The model uses various techniques such as signal processing, machine learning, and deep learning to extract features from audio recordings and classify them.

### Impact

Whale detection in audios plays a key role in industries related to marine research, environmental monitoring, and maritime operations. By accurately detecting and classifying whale vocalizations in audio recordings, it helps in understanding whale behavior, migration patterns, and population dynamics. This information is crucial for marine biologists, conservationists, and policymakers in making informed decisions regarding marine conservation and protection efforts. In the shipping and maritime industry, whale detection contributes to the implementation of measures to avoid collisions with whales, ensuring compliance with regulations and minimizing environmental impact. Furthermore, in the field of underwater acoustics, whale detection supports research and development of technologies for passive acoustic monitoring, providing valuable insights into the marine ecosystem and facilitating oceanic studies.

### Dataset

30000 audio rows with thei label 0 or 1 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/whale_detection/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Identify whether an audio signal is related to a whale or not

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
    sample_rate: 2000
    spectrogram_normalization: 'No'
    stft_window_size: 2048
    training_chunk_seconds: 2
augmentation:
    mix_audio: Disabled
    mix_concentration: 1.0
    mix_iterations: 1
    mix_probability: 1.0
    mix_target: Ratio
dataset:
    audio_column: clip_name
    data_folder: data/anon/whale_detection/audio/
    data_folder_test: None
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '0'
    group_fold_column: clip_name
    label_columns:
    - label
    test_dataframe: None
    train_dataframe: data/anon/whale_detection/train.csv
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
experiment_name: whale_detection
logging:
    logger: None
    neptune_project: ''
    number_of_audios: 8
prediction:
    inference_chunk_method: Fix
    inference_chunk_seconds: 2
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
    epochs: 8
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/whale_detection/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/whale_detection/Validation%20Predictions.png)

### License

Copyright © 2011 by Cornell University and the Cornell Research Foundation, Inc. 

### Acknowledgements

Original dataset source is https://www.kaggle.com/competitions/whale-detection-challenge/data
