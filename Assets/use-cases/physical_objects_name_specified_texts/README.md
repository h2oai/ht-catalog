## Use Case 57: Physical Objects Entity Recognition

Recognize the physical objects of the tokens in each text

- `Industry: Media`
- `Problem Type: Text Token Classification`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/physical_objects_name_specified_texts/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/physical_objects_name_specified_texts/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/physical_objects_name_specified_texts/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/physical_objects_name_specified_texts/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/physical_objects_name_specified_texts/cover)

### Business Problem 

Physical Objects Name Entity Recognition (NER) is a natural language processing (NLP) task that aims to identify and classify physical objects mentioned in text. It involves extracting specific entities such as product names, brand names, or object categories from unstructured text data. By implementing NER for physical objects, businesses can automate the process of identifying and categorizing objects mentioned in customer reviews, social media posts, or product descriptions.

Implementing Physical Objects NER can have a significant impact on various industries. In e-commerce, it can automate the extraction of product names and categories from customer feedback, allowing businesses to quickly analyze sentiment and identify areas for improvement. For manufacturers, NER can help monitor mentions of their brand and products in social media, enabling them to gauge customer sentiment and track brand reputation. In the logistics industry, NER can automate the identification of objects mentioned in shipping or inventory documents, improving operational efficiency and reducing errors.

### Dataset

14041 train, 3250 validation, and 3453 test texts with POS,CHUNK, and NER tags.
Dataset path: s3://h2oai-hydrogen-torch-internal/dev_datasets/conll2003_text_token_classification.zip

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/physical_objects_name_specified_texts/train%20data.png)

### Model Training

Objective: Recognize the physical objects of the tokens in each text

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    backbone: bert-base-uncased
    dropout: 0
    gradient_checkpointing: false
    intermediate_dropout: 0.0
    pretrained: true
augmentation: {}
dataset:
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '0'
    group_fold_column: id
    label_columns: ner_tags
    test_dataframe: data/anon/conll2003_text_token_classification/data/conll2003/test.pq
    text_column: text
    train_dataframe: data/anon/conll2003_text_token_classification/data/conll2003/train.pq
    validation_dataframe: data/anon/conll2003_text_token_classification/data/conll2003/validation.pq
    validation_size: 0.2
    validation_strategy: custom
environment:
    gpus:
    - '0'
    mixed_precision_inference: false
    mixed_precision_training: true
    number_of_workers: 4
    seed: -1
experiment_name: 57_conll2003
logging:
    ignore_classes: O,NOT_WORD_START
    logger: None
    neptune_project: ''
    number_of_texts: 10
prediction:
    metric: MICRO_F1_SCORE
tokenizer:
    lowercase: false
    max_length: 128
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/physical_objects_name_specified_texts/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/physical_objects_name_specified_texts/Validation%20Predictions.png)

### License

NA
