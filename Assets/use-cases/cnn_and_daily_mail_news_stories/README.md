## Use Case 58: News Summarization

Summarize the news articles

- `Industry: Media`
- `Problem Type: Text Sequence to Sequence`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/cnn_and_daily_mail_news_stories/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/cnn_and_daily_mail_news_stories/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/cnn_and_daily_mail_news_stories/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/cnn_and_daily_mail_news_stories/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/cnn_and_daily_mail_news_stories/cover)

### Business Problem 

Text summarization in news stories involves condensing lengthy news articles into concise summaries, enabling readers to quickly grasp the key points and main ideas of the article. This solution utilizes natural language processing algorithms to identify important sentences and extract the most relevant information, providing users with a succinct overview of the news story.

### Impact

Implementing text summarization in news stories can have a significant impact on the news industry. It enables news organizations to deliver information to readers more efficiently, saving their time and effort. With shorter and more digestible summaries, readers can quickly scan multiple articles and stay informed about various topics. Additionally, this technology can be integrated into news aggregators and personalized news apps, enhancing user experiences and attracting more engaged audiences. By automating the summarization process, news organizations can streamline their content production and dissemination, increasing their overall productivity and competitiveness.

### Dataset

Dataset link - [s3://h2o-ht-catalog/cnn_dailymail_text_sequence_to_sequence.zip](https://h2o-ht-catalog.s3.amazonaws.com/cnn_dailymail_text_sequence_to_sequence.zip)

4000 train, 4000 validation, and 4000 test texts with summaries. 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/cnn_and_daily_mail_news_stories/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Summarize the news articles

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
    group_fold_column: text
    label_columns: summary
    test_dataframe: data/anon/cnn_dailymail_text_sequence_to_sequence/test.csv
    text_column: text
    train_dataframe: data/anon/cnn_dailymail_text_sequence_to_sequence/train.csv
    validation_dataframe: data/anon/cnn_dailymail_text_sequence_to_sequence/validation.csv
    validation_size: 0.2
    validation_strategy: custom
environment:
    gpus:
    - '0'
    mixed_precision_inference: false
    mixed_precision_training: true
    number_of_workers: 4
    seed: -1
experiment_name: 58_cnn_dailymail
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

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/cnn_and_daily_mail_news_stories/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/cnn_and_daily_mail_news_stories/Validation%20Predictions.png)

### License

MIT License

### Acknowledgements

Original dataset source is https://github.com/abisee/cnn-dailymail
