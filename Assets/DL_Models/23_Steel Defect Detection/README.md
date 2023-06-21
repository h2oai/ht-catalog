# STEEL DEFECT CLASSIFICATION
### Manufacturing  | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/23_Steel%20Defect%20Detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/23_Steel%20Defect%20Detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/23_Steel%20Defect%20Detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/23_Steel%20Defect%20Detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/23_Steel%20Defect%20Detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Steel Defect Detection model is a computer vision-based system used to identify and classify defects in steel surfaces such as cracks, scratches, and pitting. The model employs image processing techniques and deep learning algorithms to detect and classify the defects accurately. This system is useful for steel manufacturers to ensure the quality of their products and avoid costly repairs and recalls. The model can also be used for predictive maintenance, helping manufacturers identify potential defects before they become severe..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Steel defect detection plays a crucial role in the manufacturing and construction industries. By employing advanced imaging techniques and machine learning algorithms, it enables rapid and precise identification of defects in steel products. Early detection of defects such as cracks, corrosion, or uneven surfaces ensures the production of high-quality steel materials, reducing waste, and increasing operational efficiency. Steel defect detection also enhances safety standards, as it helps prevent structural failures and potential hazards. By ensuring the integrity of steel products, it fosters customer satisfaction, maintains industry reputation, and drives business growth..</p>

### DATASET
- Steel defect detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_segmentation/steel_defect_detection.zip).
- 7095 train images with 4 class ids.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/23_Steel%20Defect%20Detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Identify and classify defects in steel surfaces.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/23_Steel%20Defect%20Detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/23_Steel%20Defect%20Detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Attribution 4.0 International (CC BY 4.0)</p>
    