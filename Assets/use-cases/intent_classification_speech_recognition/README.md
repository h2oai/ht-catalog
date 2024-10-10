## Use Case 67: Speech Intent Classification

Categorize the user's intended action or query based on the spoken inputs

- `Industry: Banking`
- `Problem Type: Speech Recognition`
- `Data Type: Speech`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/intent_classification_speech_recognition/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/intent_classification_speech_recognition/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/intent_classification_speech_recognition/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/intent_classification_speech_recognition/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/intent_classification_speech_recognition/cover)

### Business Problem 

Intent classification in speech recognition involves determining the underlying intent or purpose behind a spoken sentence or phrase. This solution aims to understand the user's intended action or query by analyzing the content and context of the spoken input. It enables intelligent voice assistants and chatbots to provide appropriate responses and fulfill user requests effectively.

### Impact

Intent classification in speech recognition is very useful across industries. It enhances customer service by enabling accurate identification of user needs and queries, leading to faster and more relevant responses. In e-commerce, it improves personalized recommendations and enables voice-based shopping experiences. In call centers, it automates call routing and improves the efficiency of customer support. Intent classification also finds applications in virtual assistants, smart home devices, and voice-controlled applications, enhancing user experience and engagement.

### Dataset

Dataset link - [s3://h2o-ht-catalog/intent_classification_speech_recognition.zip](https://h2o-ht-catalog.s3.amazonaws.com/intent_classification_speech_recognition.zip)

563 train audio samples with their transcript. 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/intent_classification_speech_recognition/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Categorize the user's intended action or query based on the spoken inputs

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    backbone: openai/whisper-base.en
    freeze_encoder: false
    gradient_checkpointing: false
    language: en
    pretrained: true
audio:
    sample_rate: 16000
augmentation: {}
dataset:
    audio_column: file
    data_folder: data/user/intent_classification_speech_recognition/audios/
    data_folder_test: data/user/intent_classification_speech_recognition/audios/
    data_sample: 1.0
    data_sample_choice:
    - Train
    - Validation
    group_fold_column: file
    label_columns: transcription
    selected_folds:
    - '0'
    test_dataframe: None
    train_dataframe: data/user/intent_classification_speech_recognition/train.csv
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
experiment_name: 67_intent_classification_speech_recognition
logging:
    log_grad_norm: false
    logger: None
    neptune_project: ''
    number_of_audios: 8
prediction:
    duration_in_visualizations: 60
    metric: WER
    normalize_text: true
    suppress_default_tokens: false
training:
    automatically_adjust_batch_size: false
    batch_size: 1
    build_scoring_pipelines: true
    calculate_train_metric: false
    drop_last_batch: true
    epochs: 3
    evaluate_before_training: true
    evaluation_epochs: 1
    grad_accumulation: 1
    gradient_clip: 0.0
    learning_rate: 1.0e-05
    optimizer: AdamW
    save_best_checkpoint: false
    schedule: Cosine
    train_validation_data: false
    warmup_epochs: 0
    weight_decay: 0.0

```

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/intent_classification_speech_recognition/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/intent_classification_speech_recognition/Validation%20Predictions.png)

### License

CC BY-NC 4.0

### Acknowledgements

Original dataset source is https://github.com/skit-ai/speech-to-intent-dataset
