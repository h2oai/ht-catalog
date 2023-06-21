# SEARCH QUERIES WELLFORMEDNESS
### E-commerce | Text | Regression

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/64_Google%20Search%20Queries/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/64_Google%20Search%20Queries/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/64_Google%20Search%20Queries/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/64_Google%20Search%20Queries/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/64_Google%20Search%20Queries/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Search Queries Wellformedness involves validating and improving the well-formedness of user search queries in search engines or information retrieval systems. The objective is to ensure that users' queries are properly formatted, contain the necessary syntax, and are correctly interpreted by the search engine. By validating and enhancing the well-formedness of search queries, this use case aims to improve search accuracy, relevance, and user satisfaction. It is particularly relevant for search engine providers, e-commerce platforms, and information retrieval systems where accurate interpretation of user queries is crucial for delivering relevant search results and improving the overall search experience..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Improving search query well-formedness can have significant business impacts for search engine providers and e-commerce platforms. Firstly, it enhances search accuracy and relevance by ensuring that user queries are correctly understood and interpreted. This leads to more accurate search results, improved user satisfaction, and increased engagement. By providing users with relevant search results, search engines can attract and retain more users, thereby increasing their market share and revenue potential. Additionally, well-formed search queries enable e-commerce platforms to deliver more targeted product recommendations and personalized search experiences, which can lead to higher conversion rates and customer satisfaction. Overall, search query well-formedness plays a crucial role in optimizing search performance, user experience, and business outcomes..</p>

### DATASET
- Google search queries dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/wellformed_query_text_regression.csv).
- 17375 train texts with one label. The label has value between 0 to 1..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/64_Google%20Search%20Queries/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Rate the Wellformedness of the Search Queries.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: bert-base-uncased</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 16</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 2</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 1e-05</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/64_Google%20Search%20Queries/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/64_Google%20Search%20Queries/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    