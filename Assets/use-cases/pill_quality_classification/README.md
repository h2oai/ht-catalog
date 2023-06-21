# PILL QUALITY CLASSIFICATION
### Healthcare  | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/21_Pill%20Quality%20Classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/21_Pill%20Quality%20Classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/21_Pill%20Quality%20Classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/21_Pill%20Quality%20Classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/21_Pill%20Quality%20Classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Pill Quality Classification model is used for identifying and classifying pills based on their shape, color, and markings. This model is useful in pharmaceutical manufacturing, where quality control is critical for ensuring that medications are safe and effective. By accurately classifying pills, manufacturers can quickly detect and remove defective or counterfeit pills from the production line. The model uses image processing and machine learning techniques to classify pills based on their unique features, helping to improve the efficiency and accuracy of quality control processes..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Accurate pill quality classification holds immense business impact, particularly in the pharmaceutical industry. By leveraging computer vision and machine learning techniques, it enables pharmaceutical companies to ensure the quality and safety of their products. Reliable pill quality classification helps identify and eliminate defective or counterfeit pills from the market, safeguarding patient health and maintaining brand reputation. It streamlines quality control processes, reduces the risk of product recalls, and ensures compliance with regulatory standards, ultimately enhancing customer trust and overall business success..</p>

### DATASET
- Pill quality classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/pill_quality_classification.zip).
- 330 train images with their labels [chip,dirt,normal].

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/21_Pill%20Quality%20Classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Classify whether the pill is dirty or not.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/21_Pill%20Quality%20Classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/21_Pill%20Quality%20Classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>XSLA license, which is the most common license for MathWorks staff contributions.</p>
    