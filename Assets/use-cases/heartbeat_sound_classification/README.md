# HEARTBEAT SOUND CLASSIFICATION
### Healthcare | Audio | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/48_Heartbeat%20Sound%20Classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/48_Heartbeat%20Sound%20Classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/48_Heartbeat%20Sound%20Classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/48_Heartbeat%20Sound%20Classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/48_Heartbeat%20Sound%20Classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Heartbeat Sound Classification model is a machine learning model designed to classify heartbeat sounds into different categories such as normal heartbeat and abnormal heartbeats. The model is trained on a dataset of heartbeat sounds, which includes recordings of both healthy and unhealthy heartbeats. By analyzing the sound patterns in the recordings, the model can accurately classify the heartbeat sounds into their respective categories.The potential use cases of this model include early detection of heart problems, remote monitoring of heart health, and improving the accuracy of medical diagnoses. The model can be integrated into healthcare systems and wearable devices to provide real-time analysis of heartbeat sounds and alert medical professionals to any abnormalities..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Heartbeat sound classification has significant implications in healthcare and medical diagnostics. By analyzing audio data of heartbeat sounds, machine learning algorithms can classify and identify abnormal heart patterns or conditions. Accurate heartbeat sound classification aids in early detection of cardiac abnormalities, assisting medical professionals in diagnosing cardiovascular diseases and providing timely interventions. It contributes to improved patient care, personalized treatment plans, and better management of heart-related conditions. Heartbeat sound classification technology enhances diagnostic capabilities, supports preventive healthcare, and improves patient outcomes in cardiology..</p>

### DATASET
- Heartbeat sound classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/heartbeat_sound_classification.zip).
- 832 train images with their labels (artifact,extrastole,murmur,normal,unlabel).

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/48_Heartbeat%20Sound%20Classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Classify heartbeat sounds into different categories..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/48_Heartbeat%20Sound%20Classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/48_Heartbeat%20Sound%20Classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC0: Public Domain</p>
    