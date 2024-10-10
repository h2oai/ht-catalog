## Use Case 37: Bird Voice Classification

Identify the bird by using their audio

- `Industry: AI4Good`
- `Problem Type: Audio Classification`
- `Data Type: Audio`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/bird_voice_classification/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/bird_voice_classification/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/bird_voice_classification/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/bird_voice_classification/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/bird_voice_classification/cover)

### Business Problem 

The Bird Voice Classification model is a machine learning model designed to identify and classify bird species based on their vocalizations. By analyzing bird calls and songs, the model can identify different bird species and distinguish them from one another. This model can be useful for ecological studies, birdwatching, and conservation efforts, as it can provide information about the presence and abundance of different bird species in an area. Additionally, the model can be used to track changes in bird populations over time and monitor the impact of environmental factors on bird behavior and vocalizations.

### Impact

Bird voice classification plays a crucial role in ornithology, ecological research, and biodiversity conservation. By leveraging audio signal processing techniques and machine learning algorithms, it enables the identification and classification of bird species based on their vocalizations. Accurate bird voice classification assists researchers in studying bird populations, monitoring habitats, and assessing ecological health. It supports conservation efforts, species monitoring, and understanding the impact of environmental changes on bird populations. Bird voice classification technology contributes to biodiversity preservation, ecological research, and the conservation of avian species.

### Dataset

Dataset link - [s3://h2o-ht-catalog/audio_classification/whale_detection.zip](https://h2o-ht-catalog.s3.amazonaws.com/audio_classification/whale_detection.zip)

5407 train images and 687 test images with 41 uniques labels 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/bird_voice_classification/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Identify the bird by using their audio

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
    training_chunk_seconds: 15
augmentation:
    mix_audio: Disabled
    mix_concentration: 1.0
    mix_iterations: 1
    mix_probability: 1.0
    mix_target: Ratio
dataset:
    audio_column: image
    data_folder: data/anon/bird_voice_classification/train/
    data_folder_test: data/anon/bird_voice_classification/test/
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '4'
    group_fold_column: image
    label_columns:
    - class
    test_dataframe: data/anon/bird_voice_classification/test.pq
    train_dataframe: data/anon/bird_voice_classification/train.pq
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
experiment_name: bird_voice_classification
logging:
    logger: None
    neptune_project: ''
    number_of_audios: 8
prediction:
    inference_chunk_method: Fix
    inference_chunk_seconds: 15
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/bird_voice_classification/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/bird_voice_classification/Validation%20Predictions.png)

### License

CC0: Public Domain

### Acknowledgements

Original dataset source is https://xeno-canto.org
