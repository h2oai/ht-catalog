## Use Case 59: Article Readability Scoring

Calculate the readability scores of the texts

- `Industry: Marketing`
- `Problem Type: Text Regression`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/texts_with_readability_scores/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/texts_with_readability_scores/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/texts_with_readability_scores/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/texts_with_readability_scores/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/texts_with_readability_scores/cover)

### Business Problem 

The Readability Scoring for Texts use case involves developing an algorithm or tool that can assess the readability level of a given text. It aims to provide a numerical score or categorization indicating the difficulty of comprehending the text. This tool can be useful in various domains, such as education, publishing, content creation, and language learning, to evaluate and enhance the readability of written material.

### Impact

The Readability Scoring tool can have a significant impact on industries that heavily rely on written communication. In education, it can assist teachers in selecting appropriate reading materials for students based on their reading abilities. Publishers can utilize this tool to assess the readability of their content and make necessary modifications to cater to their target audience. Content creators can optimize their writing styles to ensure clarity and accessibility. Language learning platforms can integrate this tool to provide tailored reading materials for learners at different proficiency levels.

### Dataset

Dataset path: s3://h2oai-hydrogen-torch-internal/dev_datasets/commonlit_readability_text_regression.zip

2834 train texts with readability scores. Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/texts_with_readability_scores/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Calculate the readability scores of the texts

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    backbone: roberta-base
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
    group_fold_column: id
    label_columns:
    - target
    separator: ''
    test_dataframe: None
    text_column:
    - text
    train_dataframe: data/anon/commonlit_readability_text_regression/train.csv
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
experiment_name: 59_commonly_readability.1.1
logging:
    logger: None
    neptune_project: ''
    number_of_texts: 10
prediction:
    metric: MAE
tokenizer:
    lowercase: false
    max_length: 384
    padding_quantile: 1.0
training:
    automatically_adjust_batch_size: false
    batch_size: 12
    build_scoring_pipelines: true
    calculate_train_metric: false
    differential_learning_rate: 1.0e-05
    differential_learning_rate_layers: []
    drop_last_batch: true
    epochs: 6
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/texts_with_readability_scores/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/texts_with_readability_scores/Validation%20Predictions.png)

### License

License Type is Unknown

### Acknowledgements

Original dataset source is Unknown
