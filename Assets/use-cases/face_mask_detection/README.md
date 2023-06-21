# FACE MASK DETECTION IN IMAGES
### AI for good | Image | Object Detection

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/91_face_mask_detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/91_face_mask_detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/91_face_mask_detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/91_face_mask_detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/91_face_mask_detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Face mask detection entails the automated recognition and identification of individuals wearing or not wearing face masks from images or video streams. This technology employs computer vision algorithms to analyze facial features and detect the presence or absence of face masks, contributing to public health initiatives, crowd monitoring, and compliance enforcement.</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Face mask detection has business impact in various industries, particularly in public health, retail, and security. By automatically recognizing and identifying individuals wearing or not wearing face masks, this technology aids in enforcing public health guidelines, ensuring compliance, and mitigating the spread of infectious diseases. It enables businesses to implement mask-wearing policies, protect their customers and employees, and maintain a safe environment. Retailers can monitor compliance in their stores, while security personnel can identify potential risks and address non-compliance effectively.</p>

### DATASET
- Face_mask_detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/face-mask-detection.zip).
- 853 train images with their masks.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/91_face_mask_detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Detect and classify individuals wearing or not wearing face masks from images or video streams using computer vision techniques for public health initiatives and compliance enforcement.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: tf_efficientdet_d0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 16</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 5</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/91_face_mask_detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/91_face_mask_detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Unknown</p>
    