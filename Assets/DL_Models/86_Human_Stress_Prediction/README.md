# HUMAN STRESS PREDICTION
### Healthcare | Text | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/86_Human_Stress_Prediction/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/86_Human_Stress_Prediction/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/86_Human_Stress_Prediction/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/86_Human_Stress_Prediction/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/86_Human_Stress_Prediction/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Human stress prediction entails the analysis and prediction of individuals' stress levels based on various physiological or behavioral signals. This technology leverages machine learning algorithms and sensor data to detect patterns, changes, and indicators of stress, providing insights for stress management, mental health support, and overall well-being.</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Human stress prediction has significant business impact in the fields of healthcare, wellness, and human resources. By analyzing physiological or behavioral signals to detect stress levels, this technology enables proactive stress management, mental health support, and employee well-being initiatives. Healthcare providers can offer targeted interventions and treatments, while employers can implement stress reduction programs, improve workplace productivity, and foster a positive work environment. It contributes to enhanced employee satisfaction, reduced healthcare costs, and improved overall organizational performance..</p>

### DATASET
- Human_stress_prediction dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/text_classification/stress_prediction.csv).
- 2838 train text samples with 2 different labels..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/86_Human_Stress_Prediction/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Predict individuals' stress levels based on physiological or behavioral signals using machine learning techniques for stress management and mental health support..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/86_Human_Stress_Prediction/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/86_Human_Stress_Prediction/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Other</p>
    