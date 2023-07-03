## Use Case 66: Speech Commands Classification

Transcribe the spoken commands and convert them into actionable instructions

- `Industry: Banking`
- `Problem Type: Speech Recognition`
- `Data Type: Speech`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/commands_speech_recognition/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/commands_speech_recognition/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/commands_speech_recognition/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/commands_speech_recognition/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/commands_speech_recognition/cover)

### Business Problem 

Commands speech recognition involves developing a system that can understand and interpret spoken commands or instructions given by users. This solution enables hands-free control and interaction with various devices, such as smartphones, smart home assistants, and vehicles. By converting speech into actionable commands, it enhances user experience and convenience.

### Impact

Implementing commands speech recognition is very useful across industries. It enables seamless voice control, improving accessibility and user engagement. In the automotive industry, it enhances driver safety by allowing hands-free operation of in-car systems. In the consumer electronics sector, it enables voice-activated control of devices, enhancing user convenience and satisfaction. In healthcare, it simplifies interactions with medical equipment, improving efficiency and reducing errors. Overall, commands speech recognition technology can revolutionize human-computer interaction, making devices and systems more user-friendly and intuitive.

### Dataset

Dataset path: s3://h2oai-hydrogen-torch-internal/dev_datasets/commands_speech_recognition.zip

6798 train audio samples with their transcript. Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/commands_speech_recognition/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Transcribe the spoken commands and convert them into actionable instructions

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
    data_folder: data/user/commands_speech_recognition/commands/
    data_folder_test: None
    data_sample: 1.0
    data_sample_choice:
    - Train
    - Validation
    group_fold_column: file
    label_columns: transcript
    selected_folds:
    - '4'
    test_dataframe: None
    train_dataframe: data/user/commands_speech_recognition/commands.csv
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
experiment_name: 66_commands_speech_recognition
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/commands_speech_recognition/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/commands_speech_recognition/Validation%20Predictions.png)

### License

License Type is Unknown

### Acknowledgements

Original dataset source is Unknown
