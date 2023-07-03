## Use Case 82: Scientific Papers NER

Extract and classify named entities from scientific papers 

- `Industry: Research`
- `Problem Type: Text Sequence to Sequence`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/scientific_papers/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/scientific_papers/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/scientific_papers/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/scientific_papers/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/scientific_papers/cover)

### Business Problem 

Scientific papers NER (Named Entity Recognition) entails the identification and extraction of named entities such as names of researchers, organizations, chemicals, or biological entities from scientific articles and papers. The solution approach assists in organizing and indexing scientific literature, enabling efficient information retrieval and knowledge discovery in specific domains

### Impact

Scientific papers NER is very useful in scientific research and knowledge management. By automatically extracting named entities from scientific articles and papers, this technology enhances information retrieval, literature review, and knowledge discovery. Researchers, academic institutions, and R&D departments can efficiently locate relevant literature, identify key authors or organizations, and establish collaborations. It fosters scientific progress, accelerates innovation, and supports evidence-based decision-making.

### Dataset

Dataset path: s3://apac-cds/ht_datasets/text_sequence_to_sequence/scientific papers.zip

202914 train rows with their summaries Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/scientific_papers/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Extract and classify named entities from scientific papers 

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
    - '0'
    group_fold_column: article
    label_columns: abstract
    test_dataframe: data/anon/scientific papers/scientific_papers_test.csv
    text_column: article
    train_dataframe: data/anon/scientific papers/scientific_papers_train.csv
    validation_dataframe: data/anon/scientific papers/scientific_papers_validation.csv
    validation_size: 0.2
    validation_strategy: custom
environment:
    gpus:
    - '0'
    mixed_precision_inference: false
    mixed_precision_training: true
    number_of_workers: 4
    seed: -1
experiment_name: 82_paper_summary
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/scientific_papers/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/scientific_papers/Validation%20Predictions.png)

### License

CC BY-NC-SA 3.0

### Acknowledgements

Original dataset source is https://aclanthology.org/N18-2097/
