## Use Case 55: Hotel Recommendations

Rate the quality of 6 differnet facilities of the hotels using their reviews

- `Industry: Marketing`
- `Problem Type: Text Regression`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hotel_reviews/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hotel_reviews/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hotel_reviews/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hotel_reviews/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hotel_reviews/cover)

### Business Problem 

The use case involves recommending hotels based on ratings. Users can provide their preferences, such as destination, budget, and desired amenities, and the system will generate hotel recommendations based on the ratings received from previous guests. The ratings reflect the overall satisfaction and quality of service offered by the hotels. By considering these ratings, the system aims to provide users with reliable and trustworthy recommendations that align with their preferences, ensuring a positive hotel experience.

### Impact

Implementing a hotel recommendation system based on ratings can have a significant impact on the hospitality industry. It enhances customer satisfaction by guiding them towards hotels that have consistently received high ratings from previous guests. This improves the overall quality of service provided, leading to positive guest experiences, increased customer loyalty, and improved customer reviews. Moreover, it enables hotels to differentiate themselves based on their ratings, attracting more potential guests and increasing their occupancy rates. The system also benefits travel agencies and online platforms by providing them with a valuable tool to enhance their user experience and generate higher customer engagement.

### Dataset

Dataset path: s3://h2oai-hydrogen-torch-internal/dev_datasets/hotel_recommendation_text_regression.csv

50000 train texts with 6 labels. Each label has value between 1 to 5. Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hotel_reviews/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Rate the quality of 6 differnet facilities of the hotels using their reviews

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
    group_fold_column: text
    label_columns:
    - target_sleep_quality
    - target_value
    - target_rooms
    - target_service
    - target_cleanliness
    - target_location
    separator: ''
    test_dataframe: None
    text_column:
    - text
    train_dataframe: data/anon/hotel_recommendation_text_regression/hotel_recommendation_text_regression.csv
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
experiment_name: 55_hotel_recommendation
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hotel_reviews/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/hotel_reviews/Validation%20Predictions.png)

### License

License Type is Unknown

### Acknowledgements

Original dataset source is Unknown
