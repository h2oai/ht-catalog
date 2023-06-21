## Use Case 81: Adversarial-QA

Develop and test robust question-answering systems against adversarial attacks 

- `Industry: Security`
- `Problem Type: Text Span Prediction`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/adversarialqa/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/adversarialqa/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/adversarialqa/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/adversarialqa/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/adversarialqa/cover)

### Business Problem 

AdversarialQA (Question Answering) involves the development and testing of robust question-answering systems against adversarial attacks or attempts to manipulate the system. This technology aims to enhance the reliability and security of QA models by identifying vulnerabilities, improving their resistance to adversarial inputs, and ensuring accurate and trustworthy responses.

The business impact of AdversarialQA lies in enhancing the reliability and security of question-answering systems. By identifying vulnerabilities and improving resistance to adversarial attacks, this technology strengthens trust in QA models and safeguards their integrity. It ensures accurate responses, reduces the risk of misinformation, and protects user confidence. Businesses can utilize robust QA systems to provide reliable information, enhance user experience, and differentiate themselves in competitive markets.

### Dataset

30000 train rows with their details

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/adversarialqa/train%20data.png)

### Model Training

Objective: Develop and test robust question-answering systems against adversarial attacks 

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    backbone: deepset/xlm-roberta-base-squad2
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
    - '0'
    group_fold_column: id
    number_of_predicted_answers: 3
    question_column: question
    test_dataframe: None
    train_dataframe: data/anon/adversarialqa-train/adversarialqa-train.csv
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
experiment_name: 81_adversarial_qa
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/adversarialqa/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/adversarialqa/Validation%20Predictions.png)

### License

cc-by-sa-4.0
