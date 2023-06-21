# MALICIOUS DRONES PREDICTION
### AI for good | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/90_malicious_drones_prediction/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/90_malicious_drones_prediction/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/90_malicious_drones_prediction/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/90_malicious_drones_prediction/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/90_malicious_drones_prediction/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Malicious drones prediction involves the detection and prediction of potentially harmful or unauthorized drones in a given airspace or restricted area. This technology combines drone tracking, image analysis, and machine learning techniques to identify suspicious behaviors or patterns, assisting in early threat detection, security measures, and counter-drone strategies..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Malicious drones prediction has business implications in security, public safety, and critical infrastructure protection. By detecting and predicting potentially harmful or unauthorized drones, this technology assists in identifying security threats, preventing unauthorized surveillance or attacks, and safeguarding sensitive areas. It enhances the effectiveness of counter-drone measures, enables efficient response protocols, and contributes to maintaining public safety and security. It finds applications in airports, government facilities, public events, and high-security zones..</p>

### DATASET
- Malicious_drones_prediction dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/malicious_drones_prediction.zip).
- 776 train images with 5 different categories such as Aeroplane,Bird,Drone,Helicopter,Malicious UAV.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/90_malicious_drones_prediction/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Predict and classify potentially harmful or unauthorized drones using machine learning techniques for early threat detection and security measures..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/90_malicious_drones_prediction/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/90_malicious_drones_prediction/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Unknown</p>
    