## Use Case 64: Search Queries Wellformedness

Rate the wellformedness of the online search engine queries

- `Industry: Media`
- `Problem Type: Text Regression`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/google_search_queries/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/google_search_queries/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/google_search_queries/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/google_search_queries/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/google_search_queries/cover)

### Business Problem 

Search Queries Wellformedness involves validating and improving the well-formedness of user search queries in search engines or information retrieval systems. The objective is to ensure that users' queries are properly formatted, contain the necessary syntax, and are correctly interpreted by the search engine. By validating and enhancing the well-formedness of search queries, this use case aims to improve search accuracy, relevance, and user satisfaction. It is particularly relevant for search engine providers, e-commerce platforms, and information retrieval systems where accurate interpretation of user queries is crucial for delivering relevant search results and improving the overall search experience.

Improving search query well-formedness can have significant business impacts for search engine providers and e-commerce platforms. Firstly, it enhances search accuracy and relevance by ensuring that user queries are correctly understood and interpreted. This leads to more accurate search results, improved user satisfaction, and increased engagement. By providing users with relevant search results, search engines can attract and retain more users, thereby increasing their market share and revenue potential. Additionally, well-formed search queries enable e-commerce platforms to deliver more targeted product recommendations and personalized search experiences, which can lead to higher conversion rates and customer satisfaction. Overall, search query well-formedness plays a crucial role in optimizing search performance, user experience, and business outcomes.

### Dataset

17375 train texts with one label. The label has value between 0 to 1.
Dataset path: s3://h2oai-hydrogen-torch-internal/dev_datasets/wellformed_query_text_regression.csv

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/google_search_queries/train%20data.png)

### Model Training

Objective: Rate the wellformedness of the online search engine queries

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
    group_fold_column: rating
    label_columns:
    - rating
    separator: ''
    test_dataframe: None
    text_column:
    - text
    train_dataframe: data/anon/wellformed_query_text_regression/wellformed_query_text_regression.csv
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
experiment_name: 64_wellformed_query_text_regression
logging:
    logger: None
    neptune_project: ''
    number_of_texts: 10
prediction:
    metric: MAE
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
    loss_function: MAE
    optimizer: AdamW
    run_interpretations: true
    save_best_checkpoint: false
    schedule: Cosine
    train_validation_data: false
    warmup_epochs: 0
    weight_decay: 0.0

```

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/google_search_queries/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/google_search_queries/Validation%20Predictions.png)

### License

NA
