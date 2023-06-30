## Use Case 80: SQL Create Context

Generate SQL queries or statements based on contextual information 

- `Industry: Research`
- `Problem Type: Text Span Prediction`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/sql_create_context/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/sql_create_context/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/sql_create_context/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/sql_create_context/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/sql_create_context/cover)

### Business Problem 

SQL create context refers to the process of dynamically generating SQL queries or statements based on contextual information or user requirements. The solution approach allows for the flexible creation and customization of SQL commands, enabling efficient database management, data retrieval, and system integration

### Impact

SQL create context has important business implications for database management and software development. By dynamically generating SQL queries based on contextual information or user requirements, this technology enhances the flexibility and adaptability of database systems. It facilitates efficient data retrieval, streamlines application development, and enables seamless integration with external systems. It empowers businesses to leverage data-driven insights, improve decision-making processes, and optimize operational efficiency

### Dataset

Dataset path: s3://apac-cds/ht_datasets/text_span_prediction/sql-create-context.csv

202914 train rows with their details Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/sql_create_context/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Generate SQL queries or statements based on contextual information 

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    backbone: distilbert-base-cased-distilled-squad
    gradient_checkpointing: false
    intermediate_dropout: 0.0
    pretrained: true
augmentation:
    token_mask_probability: 0.0
dataset:
    answer_column: answer
    answer_start_column: None
    context_column: context
    data_sample: 1.0
    data_sample_choice:
    - Train
    - Validation
    group_fold_column: question
    number_of_predicted_answers: 3
    question_column: question
    selected_folds:
    - '0'
    test_dataframe: None
    train_dataframe: data/user/sql-create-context/sql-create-context.csv
    validation_dataframe: None
    validation_size: 0.2
    validation_strategy: kfold
environment:
    gpus:
    - '0'
    mixed_precision_inference: false
    mixed_precision_training: true
    number_of_seeds_per_run: 1
    number_of_workers: 4
    seed: -1
experiment_name: 80_sql-create-context
logging:
    log_grad_norm: false
    logger: None
    neptune_project: ''
    number_of_texts: 10
prediction:
    metric: Jaccard
tokenizer:
    doc_stride: 64
    lowercase: false
    max_length: 256
training:
    automatically_adjust_batch_size: false
    batch_size: 16
    build_scoring_pipelines: true
    calculate_train_metric: false
    differential_learning_rate: 1.0e-05
    differential_learning_rate_layers: []
    drop_last_batch: true
    epochs: 2
    evaluate_before_training: true
    evaluation_epochs: 1
    grad_accumulation: 1
    gradient_clip: 0.0
    learning_rate: 1.0e-05
    loss_function: CrossEntropy
    optimizer: AdamW
    save_best_checkpoint: false
    schedule: Cosine
    train_validation_data: false
    warmup_epochs: 0
    weight_decay: 0.0

```

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/sql_create_context/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/sql_create_context/Validation%20Predictions.png)

### License

cc-by-4.0

### Acknowledgements

The original dataset used in this use case comes from this source : https://huggingface.co/datasets/b-mc2/sql-create-context
