# COUGH AUDIO REGRESSION IN COVID DATA
### Healthcare | Text | Regression

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/71_covid19-cough-audio-classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/71_covid19-cough-audio-classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/71_covid19-cough-audio-classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/71_covid19-cough-audio-classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/71_covid19-cough-audio-classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Cough audio regression in COVID data involves the analysis and regression of cough sounds recorded from individuals with COVID-19. This technology aims to identify and quantify different acoustic features of coughs, allowing for the assessment and prediction of disease severity, progression, and potential complications..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Cough audio regression in COVID data has substantial business impact in the healthcare sector. By accurately quantifying cough characteristics and analyzing disease progression, this technology aids in assessing the severity of COVID-19 cases, predicting potential complications, and monitoring treatment effectiveness. It enables healthcare providers to make informed decisions about patient management, allocate resources efficiently, and provide personalized care, ultimately leading to improved patient outcomes and optimized healthcare delivery..</p>

### DATASET
- Covid19-cough-audio-classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/audio_regression/covid19-cough-audio-classification.zip).
- 25985 train audio samples with their values..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/71_covid19-cough-audio-classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Predict the severity of cough in COVID-19 patients using regression analysis on cough audio data..</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: resnet50</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 13</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 2</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.01</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/71_covid19-cough-audio-classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/71_covid19-cough-audio-classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Attribution 4.0 International (CC BY 4.0)</p>
    