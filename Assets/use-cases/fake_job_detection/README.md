## Use Case 78: Fake Job Posting Detection

Detect and classify fraudulent job postings in online platforms

- `Industry: Security`
- `Problem Type: Text Classification`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/fake_job_detection/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/fake_job_detection/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/fake_job_detection/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/fake_job_detection/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/fake_job_detection/cover)

### Business Problem 

Fake job detection entails the identification and classification of fraudulent or misleading job postings in online job platforms. This solution leverages natural language processing and machine learning techniques to analyze job descriptions, qualifications, and other relevant factors, assisting job seekers in avoiding scams and ensuring a safe and trustworthy job search experience.

### Impact

Fake job detection offers critical business benefits for job platforms, recruitment agencies, and job seekers. By automatically identifying and flagging fraudulent job postings, this technology helps job platforms maintain their integrity, trustworthiness, and user satisfaction. It protects job seekers from scams, ensures a safe and reliable job search environment, and fosters a positive user experience. It contributes to building a reputable job marketplace, attracting top talent, and facilitating successful job placements.

### Dataset

17880 train text samples with 2 classes(0 or 1) 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/fake_job_detection/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Detect and classify fraudulent job postings in online platforms

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
    group_fold_column: job_id
    label_columns:
    - fraudulent
    separator: ''
    test_dataframe: None
    text_column:
    - title
    - department
    - salary_range
    - company_profile
    - description
    - requirements
    - benefits
    - employment_type
    - required_experience
    - required_education
    - industry
    - function
    - location
    train_dataframe: data/anon/fake_job_postings/fake_job_postings.csv
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
experiment_name: 78_fake-job
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/fake_job_detection/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/fake_job_detection/Validation%20Predictions.png)

### License

CC0: Public Domain

### Acknowledgements

Original dataset source is http://emscad.samos.aegean.gr
