## Use Case 68: Speech Transcript Generation

Generate transcripts for US english speech samples

- `Industry: Government`
- `Problem Type: Speech Recognition`
- `Data Type: Speech`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/phone_banking_speech_samples/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/phone_banking_speech_samples/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/phone_banking_speech_samples/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/phone_banking_speech_samples/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/phone_banking_speech_samples/cover)

### Business Problem 

Transcript generation for US-EN speeches involves converting spoken content from US-English speeches or audio recordings into written transcripts. This solution aids in transcribing large volumes of audio data efficiently and, enabling easy access to spoken information in text format.

### Impact

Transcript generation for US-EN speeches is very useful in various domains. In media and entertainment, it enables the creation of closed captions for videos and enhances accessibility for individuals with hearing impairments. In education, it facilitates the transcription of lectures, making them searchable and enabling easy note-taking for students. In market research, it streamlines the analysis of recorded interviews or focus group discussions. It also finds applications in legal and compliance sectors for transcribing audio recordings of proceedings and interviews. Overall, transcript generation for US-EN speeches improves productivity, accessibility, and information retrieval from spoken content.

### Dataset

558 train audio samples with their transcript. 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/phone_banking_speech_samples/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Generate transcripts for US english speech samples

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
    data_folder: data/user/minds14_US_speech_recognition/audio/
    data_folder_test: data/user/minds14_US_speech_recognition/audio/
    data_sample: 1.0
    data_sample_choice:
    - Train
    - Validation
    group_fold_column: file
    label_columns: transcript
    selected_folds:
    - '0'
    test_dataframe: None
    train_dataframe: data/user/minds14_US_speech_recognition/annotations.csv
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
experiment_name: 68_minds14_US_speech_recognition
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/phone_banking_speech_samples/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/phone_banking_speech_samples/Validation%20Predictions.png)

### License

License Type is Unknown

### Acknowledgements

Original dataset source is Unknown
