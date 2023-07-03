## Use Case 60: Toxic Comment Classification

Classify the online comments into different categories

- `Industry: Media`
- `Problem Type: Text Classification`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/wikipedia_toxic_comments/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/wikipedia_toxic_comments/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/wikipedia_toxic_comments/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/wikipedia_toxic_comments/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/wikipedia_toxic_comments/cover)

### Business Problem 

Toxic Comment Classification is a natural language processing (NLP) task that involves identifying and categorizing toxic or offensive comments in online platforms, such as social media, discussion forums, or comment sections. The goal is to develop a model that can classify comments into different categories, such as toxic, non-toxic, hate speech, or spam, to ensure a safer and more respectful online environment. This use case is particularly relevant for social media platforms, online communities, and content moderation teams who aim to proactively identify and filter out harmful content. By automating the identification of toxic comments, platforms can protect users from harassment, bullying, and other negative experiences. Additionally, it helps moderators prioritize their efforts by flagging potentially harmful content for review, leading to a more efficient content moderation process.

### Impact

Implementing a toxic comment classification system can have several positive impacts on businesses and online communities. Firstly, it helps maintain a positive and inclusive online environment by promptly detecting and filtering out toxic comments, which enhances user satisfaction and engagement. By reducing the presence of offensive content, companies can protect their brand reputation and retain users. Furthermore, it contributes to fostering a safer online space, making it more appealing to a wider range of users. From a content moderation perspective, automating the identification of toxic comments allows moderation teams to handle a larger volume of user-generated content effectively. This results in improved efficiency, reduced manual effort, and quicker response times to address potentially harmful situations. Overall, toxic comment classification helps businesses and online platforms create a more welcoming and secure environment for their users.

### Dataset

159571 train texts with 6 labels. Each label has value either 0 or 1. 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/wikipedia_toxic_comments/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Classify the online comments into different categories

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
    group_fold_column: id
    label_columns:
    - toxic
    - severe_toxic
    - obscene
    - threat
    - insult
    - identity_hate
    separator: ''
    test_dataframe: None
    text_column:
    - comment_text
    train_dataframe: data/anon/jigsaw_text_classification/train.csv
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
experiment_name: 60_jigsaw
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/wikipedia_toxic_comments/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/wikipedia_toxic_comments/Validation%20Predictions.png)

### License

License Type is Unknown

### Acknowledgements

Original dataset source is Unknown
