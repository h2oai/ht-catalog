## Use Case 51: Online Reviews Classification

Classify the online reviews as positive, negative, and neutral

- `Industry: Media`
- `Problem Type: Text Classification`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/amazon_reviews/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/amazon_reviews/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/amazon_reviews/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/amazon_reviews/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/amazon_reviews/cover)

### Business Problem 

The Reviews Text Classification use case involves classifying customer reviews of products on the platform into different categories based on the sentiments expressed in the text. Sentiment analysis is performed on the textual data to determine whether a review is positive or negative. This classification enables businesses to gain insights into customer opinions, identify areas for improvement, and make data-driven decisions to enhance customer satisfaction.

### Impact

The Reviews Text Classification use case plays a key role. By accurately classifying customer reviews, businesses can gain valuable insights into customer opinions, preferences, and satisfaction levels. This enables them to make informed decisions to enhance products, address customer concerns, and manage their online reputation effectively. The classification helps identify areas for improvement, optimize marketing and sales strategies, and leverage positive reviews for brand promotion. By automating the review classification process, businesses can save time and resources while extracting actionable insights that drive customer-centric improvements, leading to increased customer satisfaction, loyalty, and ultimately, business growth.

### Dataset

48093 train texts with their labels Positive or Negative 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/amazon_reviews/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Classify the online reviews as positive, negative, and neutral

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    backbone: roberta-large
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
    group_fold_column: text
    label_columns:
    - label
    separator: ''
    test_dataframe: None
    text_column:
    - text
    train_dataframe: data/anon/amazon_reviews_text_classification/amazon_reviews_text_classification.csv
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
experiment_name: 51_amazon_reviews_text_classification
logging:
    logger: None
    neptune_project: ''
    number_of_texts: 10
prediction:
    metric: ROC_AUC
    probability_threshold: 0.5
tokenizer:
    lowercase: false
    max_length: 240
    padding_quantile: 1.0
training:
    automatically_adjust_batch_size: false
    batch_size: 12
    build_scoring_pipelines: true
    calculate_train_metric: false
    differential_learning_rate: 1.0e-05
    differential_learning_rate_layers: []
    drop_last_batch: true
    epochs: 4
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/amazon_reviews/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/amazon_reviews/Validation%20Predictions.png)

### License

License Type is Unknown

### Acknowledgements

Original dataset source is Unknown
