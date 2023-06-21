# TRASH OBJECT DETECTION
### AI for Good | Image | Object Detection

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/46_Trash%20Detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/46_Trash%20Detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/46_Trash%20Detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/46_Trash%20Detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/46_Trash%20Detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>The Trash Detection and Classification model is designed to identify and classify various types of trash objects in an image. This model can help in automated waste management by detecting and segregating different types of waste for efficient recycling and disposal. The model uses image classification techniques to classify trash objects into categories such as plastic, glass, paper, metal, and organic waste. The model can be trained on a large dataset of annotated images of trash objects to improve its accuracy in detecting and classifying various types of waste. Once deployed, the model can be used in various settings such as waste sorting plants, recycling centers, and smart waste bins..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Trash detection has significant business impact in waste management and environmental sustainability. By utilizing computer vision and machine learning algorithms, trash detection technology enables the automated identification and classification of different types of trash in images or videos. Accurate trash detection facilitates efficient waste sorting, recycling, and disposal processes. It helps in reducing contamination, optimizing recycling efforts, and minimizing environmental impact. Trash detection technology contributes to improved waste management practices, resource conservation, and a cleaner, more sustainable environment..</p>

### DATASET
- Trash detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/object_detection/trash-detection.zip).
- 369 train images with 4 unique labels {glass,paper,metal, plastic}.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/46_Trash%20Detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Identify and classify various types of trash objects .</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/46_Trash%20Detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/46_Trash%20Detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC BY-NC-SA 4.0</p>
    