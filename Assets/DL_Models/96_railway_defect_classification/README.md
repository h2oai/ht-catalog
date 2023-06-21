# RAILWAY DEFECT CLASSIFICATION
### AI for good | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/96_railway_defect_classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/96_railway_defect_classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/96_railway_defect_classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/96_railway_defect_classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/96_railway_defect_classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Railway defect classification involves the automated identification and categorization of defects or anomalies in railway infrastructure, such as tracks, switches, or signals. This technology utilizes computer vision algorithms and machine learning models to analyze images or video data captured during railway inspections and classify them into specific defect categories, such as cracks, breaks, or wear..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Railway defect classification has significant business implications in the transportation and railway maintenance industry. By automating the defect identification process, railway operators can improve safety measures, optimize maintenance schedules, and enhance overall infrastructure reliability. It allows for proactive maintenance planning, reduces downtime, and mitigates the risk of accidents or disruptions, resulting in improved operational efficiency and cost savings..</p>

### DATASET
- Railway_defect_classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/railway_defect_classification.zip).
- 300 train images with their labels(Defective or Non Defective).

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/96_railway_defect_classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>accurately classify an input image or video frame into the corresponding defect category, helping railway maintenance teams prioritize and address infrastructure issues effectively..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/96_railway_defect_classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/96_railway_defect_classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Data files © Original Authors</p>
    