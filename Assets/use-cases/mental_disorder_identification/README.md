## Use Case 79: Mental Disorder identification

Identify and classify mental disorders 

- `Industry: Healthcare`
- `Problem Type: Text Classification`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/mental_disorder_identification/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/mental_disorder_identification/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/mental_disorder_identification/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/mental_disorder_identification/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/mental_disorder_identification/cover)

### Business Problem 

Mental disorder identification involves the automated screening and assessment of individuals for potential mental health conditions. This technology analyzes textual or behavioral data to detect patterns, symptoms, and risk factors associated with various mental disorders, aiding healthcare professionals in early intervention, treatment planning, and personalized care

The business impact of mental disorder identification is significant in healthcare and well-being industries. By automating the screening and identification of potential mental health conditions, this technology enables early intervention, appropriate treatment planning, and personalized care. Mental healthcare providers can optimize resource allocation, streamline patient triage, and improve mental health outcomes. Additionally, businesses focused on mental well-being can develop targeted products and services, tailor interventions, and contribute to a healthier and more productive workforce.

### Dataset

701787 train samples with 2 classes

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/mental_disorder_identification/train%20data.png)

### Model Training

Objective: Identify and classify mental disorders 

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
    group_fold_column: title
    label_columns:
    - subreddit
    separator: ''
    test_dataframe: None
    text_column:
    - selftext
    - title
    train_dataframe: data/anon/mental-disorders-identification/mental_disorders_reddit.csv
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
experiment_name: 79_mental-disorders-identification
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/mental_disorder_identification/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/mental_disorder_identification/Validation%20Predictions.png)

### License

Reddit API Terms
