# DESEASE CLASSIFICATION FROM SYMPTOM
### Healthcare | Text | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/76_symptom_to_desease_prediction/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/76_symptom_to_desease_prediction/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/76_symptom_to_desease_prediction/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/76_symptom_to_desease_prediction/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/76_symptom_to_desease_prediction/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Symptom to disease prediction involves the analysis and prediction of potential diseases or medical conditions based on reported symptoms. This technology employs machine learning algorithms and medical knowledge to correlate symptoms with specific diseases, facilitating early diagnosis, triage, and appropriate medical interventions..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>The business impact of symptom to disease prediction is substantial for healthcare providers and patients alike. By correlating reported symptoms with potential diseases, this technology enables early diagnosis, timely intervention, and personalized treatment planning. Healthcare providers can optimize resource allocation, reduce healthcare costs, and improve patient outcomes by delivering targeted and efficient care. Patients benefit from accurate diagnoses, faster access to appropriate treatments, and improved quality of life..</p>

### DATASET
- Symptom_to_desease_prediction dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/text_classification/Symptom2Disease.csv).
- 1200 train rows with 24 different categories.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/76_symptom_to_desease_prediction/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Predict potential diseases or medical conditions based on reported symptoms using machine learning techniques for early diagnosis and intervention..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/76_symptom_to_desease_prediction/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/76_symptom_to_desease_prediction/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC0: Public Domain</p>
    