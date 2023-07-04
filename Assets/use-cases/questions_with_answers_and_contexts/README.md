## Use Case 65: Question Answering in Contexts

Answer the questions from given contexts

- `Industry: Media`
- `Problem Type: Text Span Prediction`
- `Data Type: Text`

![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/questions_with_answers_and_contexts/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/questions_with_answers_and_contexts/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/questions_with_answers_and_contexts/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/questions_with_answers_and_contexts/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/questions_with_answers_and_contexts/cover)

### Business Problem 

Question Answering in Contexts involves developing models or algorithms that can answer questions based on specific contexts or documents. This use case is particularly relevant for information retrieval systems, virtual assistants, and chatbot applications, where users seek answers or information from a given context. By understanding the context and answering questions, these systems can provide timely and relevant information, improve user experience, and streamline information access. Question answering in contexts finds applications in various domains, including customer support, education, healthcare, and research, where users need precise and contextually relevant answers to their queries.

### Impact

Implementing question answering in contexts can hplays a key roles across multiple industries. In customer support, it can reduce the need for manual assistance, enabling faster response times and enhancing customer satisfaction. Virtual assistants equipped with question answering capabilities can provide users with immediate and accurate information, improving their overall experience and productivity. In educational settings, question answering systems can support students' learning by providing contextual explanations and answers to their queries. In healthcare, such systems can assist healthcare professionals in accessing relevant medical information and guidelines quickly, enabling better decision-making and improving patient care. Overall, question answering in contexts enhances information retrieval, empowers users, and drives efficiency in various industry sectors.

### Dataset

87598 train questions for 18891 contexts 

![train data](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/questions_with_answers_and_contexts/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Answer the questions from given contexts

Model Configuration (Hydrogen Torch yaml)

```yaml
architecture:
    backbone: distilbert-base-cased-distilled-squad
    gradient_checkpointing: false
    intermediate_dropout: 0.0
    pretrained: true
augmentation: {}
dataset:
    answer_column: answer
    answer_start_column: None
    context_column: context
    data_sample: 1
    data_sample_choice:
    - Train
    - Validation
    folds:
    - '0'
    group_fold_column: question
    number_of_predicted_answers: 3
    question_column: question
    test_dataframe: None
    train_dataframe: data/anon/squad_text_span_prediction/squad_v1.csv
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
experiment_name: 65_squad
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
    batch_size: 20
    build_scoring_pipelines: true
    calculate_train_metric: false
    differential_learning_rate: 1.0e-05
    differential_learning_rate_layers: []
    drop_last_batch: true
    epochs: 2
    evaluation_epochs: 1
    grad_accumulation: 1
    gradient_clip: 0.0
    learning_rate: 0.001
    loss_function: CrossEntropy
    optimizer: AdamW
    save_best_checkpoint: false
    schedule: Cosine
    train_validation_data: false
    warmup_epochs: 0
    weight_decay: 0.0

```

![chart](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/questions_with_answers_and_contexts/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/questions_with_answers_and_contexts/Validation%20Predictions.png)

### License

CC BY-SA 4.0

### Acknowledgements

Original dataset source is https://rajpurkar.github.io/SQuAD-explorer/
