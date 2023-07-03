## Use Case 73: Fake News Classification

Detect fake news using text classification techniques

- `Industry: Media`
- `Problem Type: Text Classification`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/fake_news_detection/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/fake_news_detection/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/fake_news_detection/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/fake_news_detection/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/fake_news_detection/cover)

### Business Problem 

Fake news detection in documents refers to the automated identification and classification of misinformation or fabricated content within textual documents. This solution helps combat the spread of false information by analyzing linguistic patterns, fact-checking sources, and assessing the credibility of the content, assisting users in distinguishing between reliable and unreliable information.

### Impact

The usefulness fake news detection in documents is crucial for maintaining trust, credibility, and reputation in the digital age. By automatically identifying and flagging fake or misleading content, this technology helps media organizations, news agencies, and online platforms to ensure the integrity of their news sources and protect their users from misinformation. It enhances user trust, fosters a reliable information ecosystem, and safeguards brands' credibility, contributing to sustained user engagement, customer loyalty, and brand loyalty.

### Dataset

78617 train rows with their labels 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/fake_news_detection/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Detect fake news using text classification techniques

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
    - label
    separator: ''
    test_dataframe: None
    text_column:
    - text
    train_dataframe: data/anon/fake_news_detection/fake_news_detection.csv
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
experiment_name: 73_fake_news_detection
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/fake_news_detection/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/fake_news_detection/Validation%20Predictions.png)

### License

GNU Lesser General Public License

### Acknowledgements

Original dataset source is https://www.kaggle.com/datasets/stevenpeutz/misinformation-fake-news-text-dataset-79k
