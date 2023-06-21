## Use Case 77: Tweet Emotion Detection

Detect and classify emotions expressed in tweets 

- `Industry: Media`
- `Problem Type: Text Classification`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/emotion_detection_from_tweets/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/emotion_detection_from_tweets/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/emotion_detection_from_tweets/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/emotion_detection_from_tweets/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/emotion_detection_from_tweets/cover)

### Business Problem 

Emotion detection from tweets refers to the automated identification and classification of emotions expressed within short messages posted on the social media platform Twitter. This solution analyzes linguistic cues, sentiment, and contextual information to discern various emotions, providing insights into public sentiment, opinion trends, and social dynamics

### Impact

Emotion detection from tweets is very useful in social media analytics and marketing. By automatically identifying and classifying emotions expressed in tweets, this technology allows businesses to gauge public sentiment, monitor brand reputation, and tailor marketing strategies accordingly. It enables real-time customer feedback analysis, facilitates proactive customer support, and enhances brand perception and customer satisfaction. Businesses can adapt their products, services, and communications to meet customer expectations, driving customer loyalty and market growth.

### Dataset

Dataset path: s3://apac-cds/ht_datasets/text_classification/tweet_emotions.csv

40000 train rows with 13 different classes Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/emotion_detection_from_tweets/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Detect and classify emotions expressed in tweets 

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
    group_fold_column: tweet_id
    label_columns:
    - sentiment
    separator: ''
    test_dataframe: None
    text_column:
    - content
    train_dataframe: data/anon/tweet_emotions/tweet_emotions.csv
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
experiment_name: 77_emotion_detection_from_tweets
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/emotion_detection_from_tweets/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/emotion_detection_from_tweets/Validation%20Predictions.png)

### License

CC0: Public Domain
