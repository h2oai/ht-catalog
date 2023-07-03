## Use Case 19: Document Summarization

Generate a concise summary of a longer text

- `Industry: Media`
- `Problem Type: Text Sequence to Sequence`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/text_summarization/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/text_summarization/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/text_summarization/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/text_summarization/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/text_summarization/cover)

### Business Problem 

Text summarization is a natural language processing technique used to generate a concise and coherent summary of a text. The need for text summarization model arises when we need to quickly comprehend a large amount of text data. It is particularly useful for news articles, research papers, and legal documents, where the reader needs to quickly grasp the main points without having to read the entire document

### Impact

Text summarization has a wide range of business applications, particularly in industries dealing with large volumes of textual information, such as news media, market research, and legal services. By automatically generating concise and coherent summaries from lengthy documents, text summarization improves information retrieval and comprehension. It allows users to quickly grasp the main points, key insights, and relevant details without having to read the entire text. This significantly enhances productivity, decision-making, and knowledge management. In news media, text summarization enables efficient content curation, aiding in the delivery of timely and relevant news to audiences. In legal services, it assists in digesting complex legal documents, conducting legal research, and preparing case summaries, saving valuable time and resources.

### Dataset

Dataset path: s3://apac-cds/ht_datasets/text_sequence_to_sequence/text_summarization.zip

500 text documents with their summarization Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/text_summarization/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Generate a concise summary of a longer text

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    backbone: sshleifer/distilbart-cnn-12-6
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
    - '4'
    group_fold_column: text
    label_columns: summary
    test_dataframe: None
    text_column: text
    train_dataframe: data/anon/text_summarization/text_summarization.csv
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
experiment_name: text-summary
logging:
    logger: None
    neptune_project: ''
    number_of_texts: 10
prediction:
    do_sample: false
    max_length: 128
    metric: BLEU
    num_beams: 1
    temperature: 1.0
tokenizer:
    label_max_length: 128
    lowercase: false
    max_length: 128
training:
    automatically_adjust_batch_size: false
    batch_size: 4
    build_scoring_pipelines: true
    calculate_train_metric: false
    differential_learning_rate: 1.0e-05
    differential_learning_rate_layers: []
    drop_last_batch: true
    epochs: 10
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/text_summarization/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/text_summarization/Validation%20Predictions.png)

### License

CC BY-NC-SA 3.0

### Acknowledgements

Original dataset source is https://www.kaggle.com/datasets/nfedorov/audio-summarization
