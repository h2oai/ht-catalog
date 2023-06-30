## Use Case 84: Insurance Holder Detection

Determine and classify individuals holding insurance policies or claims

- `Industry: Banking`
- `Problem Type: Text Span Prediction`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/insurance_holder_detection/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/insurance_holder_detection/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/insurance_holder_detection/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/insurance_holder_detection/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/insurance_holder_detection/cover)

### Business Problem 

Insurance holder detection refers to the automated identification and verification of individuals who hold insurance policies or claims. The solution approach utilizes various data sources and machine learning algorithms to match and associate relevant information, assisting insurance providers in identifying policyholders, preventing fraud, and ensuring efficient claims processing.

### Impact

The usefulness insurance holder detection is significant for insurance providers and fraud prevention. By accurately identifying and verifying insurance policyholders, this technology helps mitigate fraud risks and ensures accurate claims processing. It enables insurance companies to streamline operations, reduce losses, and enhance underwriting accuracy. By maintaining the integrity of their policies and safeguarding against fraudulent activities, insurance providers can build trust with customers, strengthen their reputation, and improve overall business performance.

### Dataset

Dataset path: s3://apac-cds/ht_datasets/text_span_prediction/insurance_holder_detection.zip

7632 train rows with their answers. Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/insurance_holder_detection/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Determine and classify individuals holding insurance policies or claims

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    backbone: distilbert-base-cased-distilled-squad
    gradient_checkpointing: false
    intermediate_dropout: 0.0
    pretrained: true
augmentation: {}
dataset:
    answer_column: answers
    answer_start_column: None
    context_column: context
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '4'
    group_fold_column: id
    number_of_predicted_answers: 3
    question_column: question
    test_dataframe: data/anon/insurance_holder_detection.1/policies-named-insured-test.csv
    train_dataframe: data/anon/insurance_holder_detection.1/policies-named-insured-train.csv
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
experiment_name: 84_insurance_holder_detection
logging:
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/insurance_holder_detection/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/insurance_holder_detection/Validation%20Predictions.png)

### License

Unknown

### Acknowledgements

The original dataset used in this use case comes from this source : NA
