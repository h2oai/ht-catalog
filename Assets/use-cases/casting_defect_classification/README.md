# CASTING DEFECT CLASSIFICATION
### Manufacturing  | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/28_Casting%20Defect%20Classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/28_Casting%20Defect%20Classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/28_Casting%20Defect%20Classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/28_Casting%20Defect%20Classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/28_Casting%20Defect%20Classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Casting Defect Classification model uses computer vision techniques to classify images of casting defects into their respective categories. By accurately identifying and classifying the defects, manufacturers can detect and prevent them during the casting process, leading to better product quality and reduced waste. The model can be used as a tool for quality control and inspection in the manufacturing industry..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Casting defect classification has a significant impact on the manufacturing and engineering industries. By applying computer vision and machine learning algorithms, it allows for the automated detection and classification of defects in casted components. Early identification of defects such as porosity, cracks, or surface irregularities ensures the production of high-quality casted parts. Casting defect classification enhances manufacturing efficiency, reduces scrap rates, and improves product reliability. It enables timely interventions, minimizing rework and production delays, thereby optimizing manufacturing processes and ensuring customer satisfaction..</p>

### DATASET
- Casting defect classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/casting_defect_classification.zip).
- 1300 images with labels. such as def or ok.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/28_Casting%20Defect%20Classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Accurately detect and classify the casting defects..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/28_Casting%20Defect%20Classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/28_Casting%20Defect%20Classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Attribution 4.0 International (CC BY 4.0)</p>
    