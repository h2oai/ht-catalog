## Use Case 76: Disease Classification

Predict potential diseases or medical conditions based on reported symptoms

- `Industry: Healthcare`
- `Problem Type: Text Classification`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/symptom_to_desease_prediction/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/symptom_to_desease_prediction/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/symptom_to_desease_prediction/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/symptom_to_desease_prediction/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/symptom_to_desease_prediction/cover)

### Business Problem 

Symptom to disease prediction involves the analysis and prediction of potential diseases or medical conditions based on reported symptoms. This solution employs machine learning algorithms and medical knowledge to correlate symptoms with specific diseases, facilitating early diagnosis, triage, and appropriate medical interventions.

### Impact

The usefulness symptom to disease prediction is substantial for healthcare providers and patients alike. By correlating reported symptoms with potential diseases, this technology enables early diagnosis, timely intervention, and personalized treatment planning. Healthcare providers can optimize resource allocation, reduce healthcare costs, and improve patient outcomes by delivering targeted and efficient care. Patients benefit from accurate diagnoses, faster access to appropriate treatments, and improved quality of life.

### Dataset

Dataset path: s3://apac-cds/ht_datasets/text_classification/Symptom2Disease.csv

1200 train rows with 24 different categories Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/symptom_to_desease_prediction/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Predict potential diseases or medical conditions based on reported symptoms

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    backbone: bert-base-uncased
    dropout: 0
    gradient_checkpointing: false
    intermediate_dropout: 0.0
    pool: '[CLS] token'
    pretrained: true
augmentation: {}
dataset:
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '4'
    group_fold_column: 'Unnamed: 0'
    label_columns:
    - label
    separator: ''
    test_dataframe: None
    text_column:
    - text
    train_dataframe: data/anon/Symptom2Disease/Symptom2Disease.csv
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
experiment_name: 76_symptom2disease
logging:
    logger: None
    neptune_project: ''
    number_of_texts: 10
prediction:
    metric: ROC_AUC
    probability_threshold: 0.5
tokenizer:
    lowercase: false
    max_length: 128
    padding_quantile: 1.0
training:
    automatically_adjust_batch_size: false
    batch_size: 16
    build_scoring_pipelines: true
    calculate_train_metric: false
    differential_learning_rate: 1.0e-05
    differential_learning_rate_layers: []
    drop_last_batch: true
    epochs: 2
    evaluation_epochs: 1
    grad_accumulation: 1
    gradient_clip: 0.0
    learning_rate: 1.0e-05
    loss_function: BCE
    optimizer: AdamW
    run_interpretations: true
    save_best_checkpoint: false
    schedule: Cosine
    train_validation_data: false
    warmup_epochs: 0
    weight_decay: 0.0

```

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/symptom_to_desease_prediction/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/symptom_to_desease_prediction/Validation%20Predictions.png)

### License

CC0: Public Domain
