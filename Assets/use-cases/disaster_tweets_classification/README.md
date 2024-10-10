## Use Case 49: Disaster Tweets Classification

Classify tweets as either disaster-related or not disaster-related

- `Industry: Government`
- `Problem Type: Text Classification`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/disaster_tweets_classification/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/disaster_tweets_classification/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/disaster_tweets_classification/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/disaster_tweets_classification/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/disaster_tweets_classification/cover)

### Business Problem 

The Disaster Tweets Classification model is designed to classify tweets as either disaster-related or not disaster-related using natural language processing techniques. The model was trained on a dataset of tweets labeled as either disaster-related or not disaster-related, and can be used to quickly identify tweets that may be relevant to emergency response efforts in the event of a disaster. This can be particularly useful for organizations involved in disaster response and relief efforts, as it can help them quickly identify and prioritize relevant information on social media

### Impact

Disaster tweets classification is essential for crisis management and emergency response. By analyzing text data from social media platforms, machine learning models can classify tweets related to disasters or emergencies. Accurate disaster tweets classification enables real-time monitoring of critical events, helps in assessing the severity and impact of disasters, and facilitates efficient resource allocation and coordination of response efforts. It aids in disseminating timely information, mobilizing support, and enhancing situational awareness during emergencies. Disaster tweets classification technology contributes to effective crisis communication, rapid response, and better disaster management.

### Dataset

Dataset link - [s3://h2o-ht-catalog/text_classification/disaster_tweets_classification.csv](https://h2o-ht-catalog.s3.amazonaws.com/text_classification/disaster_tweets_classification.csv)

11370 train images with their labels(0 or 1) 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/disaster_tweets_classification/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Classify tweets as either disaster-related or not disaster-related

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
    - '0'
    group_fold_column: id
    label_columns:
    - target
    separator: ''
    test_dataframe: None
    text_column:
    - text
    train_dataframe: data/anon/disaster_tweets_classification/disaster_tweets_classification.csv
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
experiment_name: disaster_tweets_classification
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/disaster_tweets_classification/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/disaster_tweets_classification/Validation%20Predictions.png)

### License

CC0: Public Domain

### Acknowledgements

Original dataset source is https://www.kaggle.com/c/nlp-getting-started
