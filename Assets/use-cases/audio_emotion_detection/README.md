## Use Case 42: Audio Emotion Detection

Classify human emotions from audio signals

- `Industry: Banking`
- `Problem Type: Audio Classification`
- `Data Type: Audio`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/audio_emotion_detection/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/audio_emotion_detection/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/audio_emotion_detection/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/audio_emotion_detection/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/audio_emotion_detection/cover)

### Business Problem 

Audio Emotion Detection model is designed to recognize human emotions from audio signals. With the help of various audio datasets, the model can be trained to identify different emotions such as happiness, sadness, anger, fear, and more. This solution can be applied in various industries such as entertainment, healthcare, and customer service to improve user experience and engagement. For example, in the entertainment industry, the model can be used to recommend music playlists based on the user's mood. In healthcare, the model can be used to detect emotions in patients' voices and provide personalized treatment plans accordingly. Similarly, in customer service, the model can be used to detect the customer's emotions during a call and provide customized solutions to improve customer satisfaction.

### Impact

Audio emotion detection has applications in various fields, including psychology, mental health, and market research. By analyzing speech signals using machine learning algorithms, it enables the identification and classification of emotions conveyed in audio recordings. Accurate audio emotion detection assists in understanding human emotions, facilitating psychological research, and supporting mental health assessments. It also has potential applications in market research, enabling companies to gauge customer sentiment and emotional responses to products or services. Audio emotion detection technology enhances emotional understanding, psychological analysis, and market insights.

### Dataset

12798 train images with 7 uniques labels [Angry, Disgusted, Fearful,Happy,Neutral,Sad,Suprised] 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/audio_emotion_detection/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Classify human emotions from audio signals

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
    sample_rate: 16000
    spectrogram_normalization: 'No'
    stft_window_size: 2048
    training_chunk_seconds: 6
augmentation:
    mix_audio: Disabled
    mix_concentration: 1.0
    mix_iterations: 1
    mix_probability: 1.0
    mix_target: Ratio
dataset:
    audio_column: audio
    data_folder: data/anon/audio_emotion_detection/Emotions/
    data_folder_test: None
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '4'
    group_fold_column: audio
    label_columns:
    - class
    test_dataframe: None
    train_dataframe: data/anon/audio_emotion_detection/train.pq
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
experiment_name: audio_emotion_detection
logging:
    logger: None
    neptune_project: ''
    number_of_audios: 8
prediction:
    inference_chunk_method: Fix
    inference_chunk_seconds: 6
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/audio_emotion_detection/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/audio_emotion_detection/Validation%20Predictions.png)

### License

CC BY-NC-SA 4.0

### Acknowledgements

Original dataset source is https://data.mendeley.com/datasets/xm232yxf7t/1
