# TEXTILE DEFECT CLASSIFICATION
### Manufacturing  | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/24_Textile%20Defect%20Detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/24_Textile%20Defect%20Detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/24_Textile%20Defect%20Detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/24_Textile%20Defect%20Detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/24_Textile%20Defect%20Detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Textile Defect classification model is used to classify defects in textiles as damaged or not damaged. The model uses computer vision and machine learning algorithms to detect and classify defects based on their properties such as shape, size, and texture. This helps manufacturers to identify and remove defective products and ensure product quality. The model can be trained on large datasets of images containing both defective and non-defective textiles to improve its accuracy and efficiency..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Textile defect detection has significant business impact in the textile and fashion industries. By leveraging computer vision and image analysis, it enables automated detection of defects in fabrics and garments during the production process. Timely identification of defects such as holes, stains, or misprints helps maintain product quality and reduces waste. Textile defect detection enhances production efficiency, as it allows for real-time monitoring and quality control, minimizing the need for manual inspection. By ensuring the delivery of defect-free textiles to customers, it enhances brand reputation, customer satisfaction, and overall business profitability..</p>

### DATASET
- Textile defect detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/textile_damage_classification.zip).
- 108000 train images with labels (good or damaged).

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/24_Textile%20Defect%20Detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Accurately identify whether the textile is damage or not.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/24_Textile%20Defect%20Detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/24_Textile%20Defect%20Detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC BY-NC-SA 4.0</p>
    