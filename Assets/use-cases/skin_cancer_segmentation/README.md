# SKIN CANCER SEGMENTATION
### Healthcare | Image | Segmentation

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/36_Skin%20Cancer%20Segmentation/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/36_Skin%20Cancer%20Segmentation/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/36_Skin%20Cancer%20Segmentation/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/36_Skin%20Cancer%20Segmentation/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/36_Skin%20Cancer%20Segmentation/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>A Skin Cancer image Segmentation model is a powerful tool for accurately detecting and segmenting skin lesions in medical images. By analyzing the images with advanced machine learning algorithms, the model can accurately identify and isolate the cancerous regions from the rest of the skin. This helps in early detection and diagnosis of skin cancer, which is crucial for effective treatment and prevention. The model can be used in hospitals, clinics, and other medical facilities to assist dermatologists and other healthcare professionals in diagnosing skin cancer..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Skin cancer segmentation has a significant impact on the field of dermatology and healthcare. By utilizing computer vision and deep learning algorithms, it enables the accurate identification and segmentation of skin cancer lesions from medical images. Precise segmentation assists dermatologists in diagnosing and monitoring skin cancer, improving the efficiency and accuracy of treatment plans. Skin cancer segmentation technology enhances early detection, promotes timely intervention, and contributes to improved patient outcomes, reducing the burden of skin cancer on individuals and healthcare systems..</p>

### DATASET
- Skin cancer segmentation dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_segmentation/skin_cancer_segmentation.zip).
- 10015 train images with their masks.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/36_Skin%20Cancer%20Segmentation/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Accurately detecting and segmenting skin lesions in medical images.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: resnet34</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 16</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 5</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/36_Skin%20Cancer%20Segmentation/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/36_Skin%20Cancer%20Segmentation/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Attribution 4.0 International (CC BY 4.0)</p>
    