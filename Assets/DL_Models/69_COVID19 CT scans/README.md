# CHEST AND LUNGS SEGMENTATION IN CT SCANS
### Healthcare | 3D Image | Semantic Segmentation

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/69_COVID19%20CT%20scans/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/69_COVID19%20CT%20scans/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/69_COVID19%20CT%20scans/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/69_COVID19%20CT%20scans/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/69_COVID19%20CT%20scans/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Chest and lungs segmentation in CT scans involves the automated extraction and delineation of chest and lung regions from CT (computed tomography) scans. This technology aids in medical image analysis and diagnosis by providing precise anatomical segmentation, which is crucial for identifying and analyzing abnormalities, tumors, or lung diseases..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Chest and lungs segmentation in CT scans has significant business impact in the healthcare industry. It enables accurate and efficient diagnosis by providing detailed anatomical information to radiologists and physicians. It aids in the detection and tracking of lung diseases, tumors, and abnormalities, allowing for early intervention and improved patient outcomes. This technology also facilitates treatment planning, surgical guidance, and monitoring of disease progression. Overall, chest and lungs segmentation in CT scans enhances the accuracy and efficiency of medical imaging analysis, leading to better patient care and treatment decisions..</p>

### DATASET
- Covid19 ct scans dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/covid_ct_image_semantic_segmentation_3d.zip).
- 20 3d train images with their masks..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/69_COVID19%20CT%20scans/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Segment the Human Chest and Lungs in CT Images.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: None</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 4</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 10</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/69_COVID19%20CT%20scans/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/69_COVID19%20CT%20scans/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    