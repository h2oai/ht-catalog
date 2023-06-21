# MENTAL DISORDER IDENTIFICATION
### Healthcare | Text | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/79_mental_disorder_identification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/79_mental_disorder_identification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/79_mental_disorder_identification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/79_mental_disorder_identification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/79_mental_disorder_identification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Mental disorder identification involves the automated screening and assessment of individuals for potential mental health conditions. This technology analyzes textual or behavioral data to detect patterns, symptoms, and risk factors associated with various mental disorders, aiding healthcare professionals in early intervention, treatment planning, and personalized care.</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>The business impact of mental disorder identification is significant in healthcare and well-being industries. By automating the screening and identification of potential mental health conditions, this technology enables early intervention, appropriate treatment planning, and personalized care. Mental healthcare providers can optimize resource allocation, streamline patient triage, and improve mental health outcomes. Additionally, businesses focused on mental well-being can develop targeted products and services, tailor interventions, and contribute to a healthier and more productive workforce..</p>

### DATASET
- Mental_disorder_identification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/text_classification/mental-disorders-identification.zip).
- 701787 train samples with 2 classes.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/79_mental_disorder_identification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Identify and classify mental disorders based on textual or behavioral data using machine learning techniques for early intervention and personalized care..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/79_mental_disorder_identification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/79_mental_disorder_identification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Reddit API Terms</p>
    