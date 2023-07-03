## Use Case 56: Environmental Sound Classification

Classify the environmental sounds using audio classification techniques

- `Industry: Government`
- `Problem Type: Audio Classification`
- `Data Type: Audio`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/environmental_sounds/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/environmental_sounds/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/environmental_sounds/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/environmental_sounds/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/environmental_sounds/cover)

### Business Problem 

Environmental sound classification involves the categorization and identification of different types of sounds present in the environment, such as sirens, car horns, birdsong, and machinery noise. This solution utilizes machine learning algorithms to analyze audio data and assign relevant labels to the sounds. The aim is to develop a system that can recognize and classify environmental sounds in real-time, enabling various applications in areas such as soundscape analysis, urban planning, wildlife monitoring, and noise pollution management.

### Impact

Environmental sound classification has significant implications across industries. In urban planning, it helps identify noise hotspots and optimize city infrastructure for noise reduction. Industries like transportation and manufacturing can use it to detect and mitigate noise pollution. Environmental agencies can benefit from soundscape analysis for wildlife conservation and habitat monitoring. The technology also aids in improving public safety by alerting emergency services to specific sounds like explosions or gunfire. Overall, environmental sound classification empowers organizations to make data-driven decisions for sustainable development and enhances the quality of life for individuals in urban environments.

### Dataset

Dataset path: s3://h2oai-hydrogen-torch-internal/dev_datasets/esc10_audio_classification.zip

5-second-long 400 audio recordings organized into ten classes. Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/environmental_sounds/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Classify the environmental sounds using audio classification techniques

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
    training_chunk_seconds: 5
augmentation:
    mix_audio: Disabled
    mix_concentration: 1.0
    mix_iterations: 1
    mix_probability: 1.0
    mix_target: Ratio
dataset:
    audio_column: filename
    data_folder: data/anon/esc10_audio_classification/audio_esc10/
    data_folder_test: data/anon/esc10_audio_classification/audio_esc10/
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '0'
    group_fold_column: filename
    label_columns:
    - label
    test_dataframe: None
    train_dataframe: data/anon/esc10_audio_classification/esc10_meta.csv
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
experiment_name: 56_esc10_audio_classification
logging:
    logger: None
    neptune_project: ''
    number_of_audios: 8
prediction:
    inference_chunk_method: Fix
    inference_chunk_seconds: 5
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/environmental_sounds/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/environmental_sounds/Validation%20Predictions.png)

### License

License Type is Unknown

### Acknowledgements

Original dataset source is Unknown
