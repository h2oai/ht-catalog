# NEWSGROUP DOCUMENT CLASSIFICATION
### Media | Text | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/72_newsgroup_document_classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/72_newsgroup_document_classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/72_newsgroup_document_classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/72_newsgroup_document_classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/72_newsgroup_document_classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Newsgroup document classification entails the automated categorization and classification of textual documents from various newsgroups or online forums. This technology facilitates efficient information retrieval and organization by accurately assigning relevant topics or categories to each document, enabling users to quickly locate and access the information they need..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Newsgroup document classification offers significant business benefits in information management and content organization. By automatically categorizing and classifying textual documents from various newsgroups or online forums, this technology enables efficient information retrieval, targeted advertising, and personalized content delivery. It enhances user experience, increases user engagement, and enables businesses to gain insights into customer preferences, trends, and market dynamics, supporting informed decision-making and driving competitive advantage..</p>

### DATASET
- Newsgroup_document_classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/text_classification/newsgroup_document_classification.csv).
- 1000 train data with their labels.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/72_newsgroup_document_classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Classify textual documents from various newsgroups using text classification techniques for efficient information organization and retrieval..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/72_newsgroup_document_classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/72_newsgroup_document_classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Database Contents License (DbCL) v1.0</p>
    