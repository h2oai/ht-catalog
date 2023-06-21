## Use Case 75: Book Rating Regression

Predict the book rating using their reviews

- `Industry: Media`
- `Problem Type: Text Classification`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/book_rating_text_regression/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/book_rating_text_regression/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/book_rating_text_regression/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/book_rating_text_regression/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/book_rating_text_regression/cover)

### Business Problem 

Book rating text regression encompasses the analysis and regression of textual reviews or feedback provided by readers for books. This technology aims to extract sentiment, opinion, and other relevant features from the text, enabling the prediction and estimation of book ratings, assisting readers in making informed choices and aiding authors and publishers in understanding readers' preferences.

Book rating text regression has a significant impact on the publishing industry and consumer decision-making. By analyzing textual reviews and extracting sentiment and opinion, this technology provides valuable insights into readers' preferences, book quality, and market trends. Publishers and authors can utilize this information to optimize book marketing strategies, refine content offerings, and improve overall reader satisfaction. It enables data-driven decision-making, boosts sales, and cultivates a loyal reader base.

### Dataset

10000 train rows with its label

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/book_rating_text_regression/train%20data.png)

### Model Training

Objective: Predict the book rating using their reviews

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
    - Avg_Rating
    separator: ''
    test_dataframe: None
    text_column:
    - Book
    - Description
    - Genres
    - Num_Ratings
    - Author
    train_dataframe: data/anon/book-rating-text-regression/book-rating-text-regression.csv
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
experiment_name: 75_book_rating_text_regression
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/book_rating_text_regression/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/book_rating_text_regression/Validation%20Predictions.png)

### License

CC0: Public Domain
