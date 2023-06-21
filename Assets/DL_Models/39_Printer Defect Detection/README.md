# PRINTER DEFECT DETECTION
### AI for Good | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/39_Printer%20Defect%20Detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/39_Printer%20Defect%20Detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/39_Printer%20Defect%20Detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/39_Printer%20Defect%20Detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/39_Printer%20Defect%20Detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>The Printer Defect Detection model uses the provided dataset to identify and classify anomalies in 3D printer operations. The dataset contains two categories: defected and non-defected. Using machine learning algorithms and image processing techniques, the model can accurately detect defects in the printer operation and classify them accordingly. This model can be useful in the quality control of 3D printing processes, allowing for early detection and correction of defects, and improving the overall efficiency of the printing process..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Printer defect detection has a direct impact on the printing industry, quality control processes, and customer satisfaction. By analyzing printed images or documents using computer vision techniques, it enables the automated detection of defects, such as misprints, ink smudges, or color inaccuracies. Effective printer defect detection ensures the delivery of high-quality printed materials, reducing waste and production costs. It helps in maintaining brand reputation, meeting customer expectations, and minimizing the need for reprints. Printer defect detection technology enhances printing efficiency, quality control measures, and customer satisfaction..</p>

### DATASET
- Printer defect detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/3D_printer_defect_classification.zip).
- 1507 train images with defected or no_defected labels.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/39_Printer%20Defect%20Detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Detect malicious defects in 3D printer operations.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/39_Printer%20Defect%20Detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/39_Printer%20Defect%20Detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC BY-NC-SA 4.0</p>
    