## Use Case 62: Protests Related Texts Identification

Identify the protests related texts

- `Industry: Security`
- `Problem Type: Text Classification`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/protests_related_texts/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/protests_related_texts/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/protests_related_texts/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/protests_related_texts/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/protests_related_texts/cover)

### Business Problem 

Protests Related Texts Identification involves identifying and categorizing text data related to protests or demonstrations. With the rise of social and political activism, there is a growing need to analyze and understand the sentiment, topics, and underlying messages expressed during protests. This use case is relevant for media organizations, social listening platforms, and government agencies to track public sentiment, assess social movements, and monitor potential risks or unrest. By identifying and analyzing protest-related texts, organizations can gain insights into public opinions, identify emerging trends, and detect misinformation or propaganda. This information can be used for various purposes, such as informing media coverage, policy-making, crisis management, or public opinion research.

### Impact

The identification and analysis of protest-related texts can hplays a key roles in different industries. Media organizations can use this information to provide more comprehensive coverage of social movements, understand public sentiment, and align their reporting with current events. Social listening platforms can offer real-time monitoring and analysis of protests, helping businesses understand the impact of social issues on their brand reputation and customer sentiment. Government agencies can utilize protest-related text identification to track public sentiment, assess the effectiveness of policies, and identify potential risks or areas of concern. This can aid in decision-making, crisis response, and public engagement. Overall, protest-related text identification enables organizations to stay informed, make data-driven decisions, and effectively respond to societal changes.

### Dataset

Dataset link - [s3://h2o-ht-catalog/protests.zip](https://h2o-ht-catalog.s3.amazonaws.com/protests.zip)

21020 train and 5204 test texts with one label. The label has value either 0 or 1. 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/protests_related_texts/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Identify the protests related texts

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
    group_fold_column: image_id
    label_columns:
    - label
    separator: ''
    test_dataframe: data/anon/protests/test_text.csv
    text_column:
    - text
    train_dataframe: data/anon/protests/train_text.csv
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
experiment_name: 62_protests
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/protests_related_texts/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/protests_related_texts/Validation%20Predictions.png)

### License

License Type is Unknown

### Acknowledgements

Original dataset source is Unknown
