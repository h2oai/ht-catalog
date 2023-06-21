# ANOMALY DETECTION USING AUDIO
### Manufacturing | Audio | Audio Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/100_Anomaly%20Detection%20using%20audio%20-%20all/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/100_Anomaly%20Detection%20using%20audio%20-%20all/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/100_Anomaly%20Detection%20using%20audio%20-%20all/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/100_Anomaly%20Detection%20using%20audio%20-%20all/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/100_Anomaly%20Detection%20using%20audio%20-%20all/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Anomaly detection using audio - all refers to a comprehensive approach that combines the analysis of audio signals from various sources, such as fans, pumps, sliders, and valves, to detect anomalies across multiple components or systems. By capturing and analyzing audio data from different sources, abnormal sound patterns associated with mechanical faults, malfunctions, or other anomalies can be detected. Machine learning algorithms are applied to classify normal and anomalous sound patterns, enabling proactive maintenance and minimizing potential failures or disruptions across multiple equipment or processes..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Implementing anomaly detection using audio - all can have a broad business impact across industries where multiple components or systems are critical for operations. By integrating audio analysis from various sources, potential failures or abnormalities can be detected holistically, improving overall equipment reliability and operational efficiency. Proactive maintenance based on anomaly detection helps prevent costly breakdowns, reduces downtime, and enhances safety. Additionally, this comprehensive approach allows for optimized resource allocation, as maintenance activities can be scheduled based on the detected anomalies across multiple components or systems..</p>

### DATASET
- Anomaly detection using audio - all dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/manufacturing/anomaly_detection_using_audio_all.zip).
- nan.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/100_Anomaly%20Detection%20using%20audio%20-%20all/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Classifies the audio segments into 4 machine parts - valve, fan, slider and pump.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: resnet34</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: False</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 32</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 5</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/100_Anomaly%20Detection%20using%20audio%20-%20all/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/100_Anomaly%20Detection%20using%20audio%20-%20all/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC BY-SA 4.0</p>
    