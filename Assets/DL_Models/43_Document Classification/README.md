# DOCUMENT CLASSIFICATION
### AI for Good | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/43_Document%20Classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/43_Document%20Classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/43_Document%20Classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/43_Document%20Classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/43_Document%20Classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>A Document Classification model is a machine learning model that can automatically classify different types of documents based on their content. In this case, the model is trained to classify documents into three categories: emails, scientific papers, and letters. The model analyzes the text and structure of each document and assigns it to the appropriate category based on patterns and features it has learned from a large training dataset. This model can be useful for businesses and organizations that deal with large volumes of documents and need to organize them efficiently.</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Document classification has a wide range of applications in industries such as legal,financial services, healthcare, and information management. By utilizing natural language processing and machine learning techniques, document classification enables the automated categorization and organization of textual documents based on their content and purpose. Accurate document classification streamlines information retrieval, enhances data management processes, and improves operational efficiency. In the legal industry, it supports document discovery, case management, and contract analysis. In financial services, it aids in fraud detection, risk assessment, and compliance with regulatory requirements. In healthcare, it facilitates patient record management and medical coding. Document classification technology contributes to enhanced productivity, data accuracy, and regulatory compliance across various industries..</p>

### DATASET
- Document classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/document_classification.zip).
- 165 train images with 3 uniques labels [scientific_publication, email, resume].

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/43_Document%20Classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Classify different types of documents based on their content.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: resnet50</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 32</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 5</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/43_Document%20Classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/43_Document%20Classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC0: Public Domain</p>
    