# BRAIN TUMOR CLASSIFICATION
### Healthcare | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/8_Brain%20MRI/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/8_Brain%20MRI/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/8_Brain%20MRI/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/8_Brain%20MRI/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/8_Brain%20MRI/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Brain MRI classification model uses deep learning algorithms to accurately classify MRI scans of the brain, detecting and classifying abnormalities such as tumors, hemorrhages, and other anomalies in brain tissue. It is an essential tool for healthcare professionals concerned with diagnosing and treating brain-related disorders, providing fast and accurate analysis of brain MRI scans to improve patient outcomes and enhance the efficiency of healthcare systems..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Brain tumor classification has significant implications in the healthcare industry. It plays a crucial role in early detection, diagnosis, and treatment planning for brain tumors. By accurately classifying brain tumor images, healthcare professionals can make informed decisions about the appropriate course of treatment, leading to improved patient outcomes. This technology reduces the time and effort required for manual analysis, enabling healthcare providers to prioritize and allocate resources effectively. It also contributes to research and advancements in brain tumor treatment, aiding in the development of personalized therapies and improving overall patient care..</p>

### DATASET
- Brain mri dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/brain-tumor-classification-mri-v2.zip).
- 2870 images with 4 labels.Such as pituitary_tumor,no_tumor,meningioma_tumor,glioma_tumor.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/8_Brain%20MRI/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Predict the type of tumor based on medical imaging data.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/8_Brain%20MRI/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/8_Brain%20MRI/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC0: Public Domain</p>
    