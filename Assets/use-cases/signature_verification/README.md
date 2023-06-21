# SIGNATURE VERIFICATION IN DOCUMENTS
### Banking | Image | Metric Learning

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/2_Signature%20Verification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/2_Signature%20Verification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/2_Signature%20Verification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/2_Signature%20Verification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/2_Signature%20Verification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Signature verification model is designed to ensure the authenticity and security of legal, financial, and personal transactions. By accurately identifying and authenticating signatures, this model helps prevent fraud and identity theft..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Signature verification in documents has a profound impact on business operations. In banking and financial services, it strengthens fraud prevention by accurately verifying signatures on checks, contracts, and financial documents, minimizing the risk of unauthorized transactions. The legal sector benefits from streamlined document authentication and integrity, ensuring the validity of legal agreements and reducing legal disputes. Healthcare organizations rely on signature verification to authenticate patient consent forms and medical records, ensuring compliance with regulations and enhancing patient safety. In government agencies, signature verification helps validate important documents, reducing the risk of forgery and ensuring the credibility of administrative processes. Overall, signature verification provides businesses with increased security, improved compliance, and enhanced operational efficiency..</p>

### DATASET
- Signature verification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/sign_verification/sign_verification.zip).
- 1100 train images with 55 unique labels..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/2_Signature%20Verification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Accurately identifying and authenticating signatures in documents using object detection techniques.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: tf_efficientnet_b0_ns</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 16</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 5</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/2_Signature%20Verification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/2_Signature%20Verification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    