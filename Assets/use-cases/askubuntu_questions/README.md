## Use Case 63: Similar Questions Grouping

Identify the similar questions asked in an online forum

- `Industry: Media`
- `Problem Type: Text Metric Learning`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/askubuntu_questions/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/askubuntu_questions/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/askubuntu_questions/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/askubuntu_questions/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/askubuntu_questions/cover)

### Business Problem 

Similar Questions Grouping in AskUbuntu involves automatically identifying and clustering similar questions posted on the AskUbuntu platform, which is a question and answer community for Ubuntu users. The objective is to group questions that are semantically or topically similar, allowing users to find relevant information efficiently and reducing duplicate or redundant questions. By applying natural language processing and machine learning techniques, this use case aims to enhance the user experience, promote knowledge sharing, and streamline the community's question answering process. Grouping similar questions helps moderators and experienced users provide targeted answers, reduces the time and effort required to address common queries, and facilitates the accumulation of knowledge within the AskUbuntu community.

Implementing similar questions grouping in AskUbuntu can have several positive impacts on the community and its users. Firstly, it improves the user experience by making it easier to find relevant information and solutions to common problems. This enhances user satisfaction, encourages engagement, and fosters a sense of community among Ubuntu users. By reducing duplicate questions, moderators and experienced users can focus their efforts on providing quality answers to unique or less frequent inquiries, improving the overall effectiveness of the platform. Additionally, similar questions grouping promotes knowledge sharing and collaboration within the community, as users can explore related questions and expand their understanding of Ubuntu. Overall, this use case contributes to a more efficient and effective question answering process, leading to a stronger and more vibrant AskUbuntu community.

### Dataset

3134 train texts from 422 groups. 756 test texts.
Dataset path: s3://h2oai-hydrogen-torch-internal/dev_datasets/ubuntu_text_metric_learning.zip

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/askubuntu_questions/train%20data.png)

### Model Training

Objective: Identify the similar questions asked in an online forum

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    backbone: distilbert-base-uncased
    dropout: 0
    embedding_size: 512
    gradient_checkpointing: false
    intermediate_dropout: 0.0
    pool: Average
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
    label_columns: label
    separator: ''
    test_dataframe: data/anon/ubuntu_text_metric_learning/test.csv
    text_column:
    - text
    train_dataframe: data/anon/ubuntu_text_metric_learning/train.csv
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
experiment_name: 63_ubuntu_text_metric_learning
logging:
    logger: None
    neptune_project: ''
    number_of_texts: 10
prediction:
    metric: mAP
    top_k_similar: 50
tokenizer:
    lowercase: false
    max_length: 128
    padding_quantile: 1.0
training:
    arcface_margin: 0.1
    arcface_scale: 45
    automatically_adjust_batch_size: false
    batch_size: 16
    build_scoring_pipelines: true
    calculate_train_metric: false
    differential_learning_rate: 0.0001
    differential_learning_rate_layers: []
    drop_last_batch: true
    epochs: 5
    evaluation_epochs: 1
    grad_accumulation: 1
    gradient_clip: 0.0
    learning_rate: 0.0001
    loss_function: ArcFace
    optimizer: AdamW
    save_best_checkpoint: false
    schedule: Cosine
    train_validation_data: false
    warmup_epochs: 0
    weight_decay: 0.0

```

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/askubuntu_questions/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/askubuntu_questions/Validation%20Predictions.png)

### License

NA
