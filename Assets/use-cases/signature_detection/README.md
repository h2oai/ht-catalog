# SIGNATURE DETECTION IN DOCUMENTS
### Banking | Image | Object Detection

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/1_Signature%20Detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/1_Signature%20Detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/1_Signature%20Detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/1_Signature%20Detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/1_Signature%20Detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>The signature detection model automates signature detection in large volumes of documents, saving time and reducing errors. It offers a faster and more accurate alternative to manual detection, verifying authenticity, identifying forgeries, and detecting potential fraud.</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Signature detection in documents has a significant business impact across various industries. In the financial sector, accurate signature detection enables fraud prevention and identity verification, safeguarding transactions and protecting against financial losses. It streamlines the legal industry by simplifying the validation of legal documents, reducing the risk of fraudulent claims, and improving overall efficiency. In healthcare, signature detection ensures proper patient consent verification, enhancing regulatory compliance and patient safety. Additionally, in logistics and supply chain management, signature detection facilitates the verification of delivery receipts and shipping documents, reducing disputes and improving supply chain transparency. Government agencies and administrative departments benefit from signature detection by ensuring the authenticity of official documents, licenses, and permits, improving data integrity and compliance..</p>

### DATASET
- Signature detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/object_detection/signature_object_detection_v2.zip).
- 1000 train images with their masks.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/1_Signature%20Detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>The signature detection model automates signature detection in large volumes of documents, saving time and reducing errors. It offers a faster and more accurate alternative to manual detection, verifying authenticity, identifying forgeries, and detecting potential fraud.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: tf_efficientdet_d0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 16</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 5</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/1_Signature%20Detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/1_Signature%20Detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    