## Use Case 72: News Article Classification

Classify news articles in different categories

- `Industry: Media`
- `Problem Type: Text Classification`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/newsgroup_document_classification/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/newsgroup_document_classification/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/newsgroup_document_classification/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/newsgroup_document_classification/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/newsgroup_document_classification/cover)

### Business Problem 

Newsgroup document classification entails the automated categorization and classification of textual documents from various newsgroups or online forums. This technology facilitates efficient information retrieval and organization by accurately assigning relevant topics or categories to each document, enabling users to quickly locate and access the information they need.

Newsgroup document classification offers significant business benefits in information management and content organization. By automatically categorizing and classifying textual documents from various newsgroups or online forums, this technology enables efficient information retrieval, targeted advertising, and personalized content delivery. It enhances user experience, increases user engagement, and enables businesses to gain insights into customer preferences, trends, and market dynamics, supporting informed decision-making and driving competitive advantage.

### Dataset

1000 train data with their labels

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/newsgroup_document_classification/train%20data.png)

### Model Training

Objective: Classify news articles in different categories

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
    group_fold_column: doc_text
    label_columns:
    - class
    separator: ''
    test_dataframe: None
    text_column:
    - doc_text
    train_dataframe: data/anon/newsgroup_document_classification/newsgroup_document_classification.csv
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
experiment_name: 72_newsgroup_document_classification
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/newsgroup_document_classification/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/newsgroup_document_classification/Validation%20Predictions.png)

### License

Database Contents License (DbCL) v1.0
