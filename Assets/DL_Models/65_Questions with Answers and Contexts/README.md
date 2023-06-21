# QUESTION ANSWERING IN CONTEXTS
### AI for good | Text | Span Prediction

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/65_Questions%20with%20Answers%20and%20Contexts/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/65_Questions%20with%20Answers%20and%20Contexts/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/65_Questions%20with%20Answers%20and%20Contexts/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/65_Questions%20with%20Answers%20and%20Contexts/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/65_Questions%20with%20Answers%20and%20Contexts/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Question Answering in Contexts involves developing models or algorithms that can accurately answer questions based on specific contexts or documents. This use case is particularly relevant for information retrieval systems, virtual assistants, and chatbot applications, where users seek answers or information from a given context. By understanding the context and accurately answering questions, these systems can provide timely and relevant information, improve user experience, and streamline information access. Question answering in contexts finds applications in various domains, including customer support, education, healthcare, and research, where users need precise and contextually relevant answers to their queries..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Implementing question answering in contexts can have significant business impacts across multiple industries. In customer support, it can reduce the need for manual assistance, enabling faster response times and enhancing customer satisfaction. Virtual assistants equipped with question answering capabilities can provide users with immediate and accurate information, improving their overall experience and productivity. In educational settings, question answering systems can support students' learning by providing contextual explanations and answers to their queries. In healthcare, such systems can assist healthcare professionals in accessing relevant medical information and guidelines quickly, enabling better decision-making and improving patient care. Overall, question answering in contexts enhances information retrieval, empowers users, and drives efficiency in various industry sectors..</p>

### DATASET
- Questions with answers and contexts dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/squad_text_span_prediction.zip).
- 87598 train questions for 18891 contexts.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/65_Questions%20with%20Answers%20and%20Contexts/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Answer the Questions from given Contexts.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: distilbert-base-cased-distilled-squad</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 20</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 2</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/65_Questions%20with%20Answers%20and%20Contexts/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/65_Questions%20with%20Answers%20and%20Contexts/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    