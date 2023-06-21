# PHYSICAL OBJECTS NAME ENTITY RECOGNITION
### Retail | Text | Token Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/57_Physical%20Objects%20Name%20Specified%20Texts/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/57_Physical%20Objects%20Name%20Specified%20Texts/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/57_Physical%20Objects%20Name%20Specified%20Texts/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/57_Physical%20Objects%20Name%20Specified%20Texts/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/57_Physical%20Objects%20Name%20Specified%20Texts/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Physical Objects Name Entity Recognition (NER) is a natural language processing (NLP) task that aims to identify and classify physical objects mentioned in text. It involves extracting specific entities such as product names, brand names, or object categories from unstructured text data. By implementing NER for physical objects, businesses can automate the process of identifying and categorizing objects mentioned in customer reviews, social media posts, or product descriptions..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Implementing Physical Objects NER can have a significant impact on various industries. In e-commerce, it can automate the extraction of product names and categories from customer feedback, allowing businesses to quickly analyze sentiment and identify areas for improvement. For manufacturers, NER can help monitor mentions of their brand and products in social media, enabling them to gauge customer sentiment and track brand reputation. In the logistics industry, NER can automate the identification of objects mentioned in shipping or inventory documents, improving operational efficiency and reducing errors..</p>

### DATASET
- Physical objects name specified texts dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/conll2003_text_token_classification.zip).
- 14041 train, 3250 validation, and 3453 test texts with POS,CHUNK, and NER tags..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/57_Physical%20Objects%20Name%20Specified%20Texts/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Recognize the Physical Objects of the tokens in each Text.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/57_Physical%20Objects%20Name%20Specified%20Texts/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/57_Physical%20Objects%20Name%20Specified%20Texts/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    