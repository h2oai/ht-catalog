# BIOMEDICAL TEXT PUBLICATION CLASSIFICATION
### Healthcare | Text | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/74_biomedical-text-publication-classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/74_biomedical-text-publication-classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/74_biomedical-text-publication-classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/74_biomedical-text-publication-classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/74_biomedical-text-publication-classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Biomedical text publication classification involves the categorization and organization of scientific articles and publications in the field of biomedicine. This technology employs natural language processing techniques to automatically assign relevant topics, domains, or subfields to scientific papers, aiding researchers and professionals in efficient literature review and knowledge discovery..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Biomedical text publication classification offers valuable business implications in the field of scientific research and healthcare. By automatically categorizing and organizing scientific articles and publications, this technology facilitates efficient literature review, accelerates knowledge discovery, and supports evidence-based decision-making. It aids researchers, healthcare professionals, and pharmaceutical companies in staying updated with the latest advancements, identifying potential collaborations, and driving innovation, thereby fostering scientific progress and enhancing competitiveness..</p>

### DATASET
- Biomedical-text-publication-classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/text_classification/biomedical-text-publication-classification.csv).
- 7570 train text samples with their labels.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/74_biomedical-text-publication-classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Classify scientific articles in the field of biomedicine using text classification techniques for effective literature review and knowledge discovery..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/74_biomedical-text-publication-classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/74_biomedical-text-publication-classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Other</p>
    