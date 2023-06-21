# PRODUCT DEFECT CLASSIFICATION
### Manufacturing | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/13_Product%20Defect%20Classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/13_Product%20Defect%20Classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/13_Product%20Defect%20Classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/13_Product%20Defect%20Classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/13_Product%20Defect%20Classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Product Defect Classification model is a machine learning model designed to detect and classify defects in products using image analysis techniques. The model uses a dataset containing images of products with and without defects, and trains a deep learning algorithm to accurately classify the images into their respective categories. This model can be used to improve quality control processes in manufacturing industries, by detecting defects early in the production process and preventing defective products from reaching customers..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Product defect classification has a significant business impact in manufacturing and quality control. By automatically detecting and classifying defects in products during the production process, manufacturers can proactively identify and address quality issues, leading to improved product quality, reduced rework, and enhanced customer satisfaction. This technology helps minimize production costs, ensure compliance with quality standards, and maintain brand reputation by delivering high-quality products to the market..</p>

### DATASET
- Product defect classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/manufacturing/product_defect_classification.zip).
- nan.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/13_Product%20Defect%20Classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Classify the defects in the machinery.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: resnet50</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: False</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 32</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 5</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/13_Product%20Defect%20Classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/13_Product%20Defect%20Classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Unknown</p>
    