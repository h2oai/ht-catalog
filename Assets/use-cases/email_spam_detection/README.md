## Use Case 50: Email Spam Classification

Classify emails into spam or non-spam categories

- `Industry: Security`
- `Problem Type: Text Classification`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/email_spam_detection/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/email_spam_detection/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/email_spam_detection/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/email_spam_detection/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/email_spam_detection/cover)

### Business Problem 

Email Spam Detection model is designed to classify emails into spam or non-spam categories. Using a dataset of labeled emails, the model is trained to recognize common features of spam emails, such as specific keywords, suspicious URLs, or message formatting. Once trained, the model can classify new incoming emails as either spam or non-spam, helping to reduce the amount of unwanted emails in users' inboxes and prevent potential security risks associated with phishing or malware attacks. The Email Spam Detection model can be integrated into email services or used as a standalone tool to improve email management and security.

### Impact

Email spam detection is crucial for maintaining efficient communication channels and preventing cyber threats. By analyzing email content and metadata, machine learning algorithms can identify and filter out unsolicited and malicious emails. Accurate email spam detection protects users from phishing attacks, malware, and unwanted solicitations. It helps in safeguarding sensitive information, ensuring email security, and maintaining productivity by reducing the time and effort spent on dealing with spam messages. Email spam detection technology enhances email communication efficiency, protects against cyber threats, and preserves data integrity.

### Dataset

5729 train examples with their labels (spam or not_spam) 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/email_spam_detection/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Classify emails into spam or non-spam categories

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
    - spam
    separator: ''
    test_dataframe: None
    text_column:
    - text
    train_dataframe: data/anon/email_spam_classification/email_spam_classification.csv
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
experiment_name: email_spam_classification
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/email_spam_detection/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/email_spam_detection/Validation%20Predictions.png)

### License

Data files © Original Authors

### Acknowledgements

Original dataset source is https://www.kaggle.com/datasets/harshsinha1234/email-spam-classification
