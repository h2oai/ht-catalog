# HARDHAT OBJECT DETECTION
### Manufacturing  | Image | Object Detection

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/47_Hardhat%20Object%20Detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/47_Hardhat%20Object%20Detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/47_Hardhat%20Object%20Detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/47_Hardhat%20Object%20Detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/47_Hardhat%20Object%20Detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Hardhat Object Detection model is designed to detect and classify the presence of hardhats in images. The model is based on object detection techniques that use deep learning algorithms to identify and locate objects in images. With the help of a dataset of labeled images that contain hardhats, the model can accurately detect the presence and location of hardhats in new images. This model can be useful in various applications, such as construction site monitoring, safety analysis, and worker compliance monitoring..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Hardhat object detection plays a vital role in construction site safety and worker protection. By analyzing visual data from cameras or surveillance systems, hardhat object detection technology identifies and tracks the presence of hardhats worn by workers in real-time. Accurate hardhat object detection ensures compliance with safety regulations, reduces the risk of head injuries, and enhances overall workplace safety. It enables proactive monitoring, alerts for non-compliance, and helps in assessing safety performance. Hardhat object detection technology contributes to accident prevention, injury reduction, and improved safety practices in construction and industrial settings..</p>

### DATASET
- Hardhat object detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/object_detection/hardhat-object-detection.zip).
- 4750 train images with their annotations.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/47_Hardhat%20Object%20Detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Detect the presence of hardhats in images.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/47_Hardhat%20Object%20Detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/47_Hardhat%20Object%20Detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC0: Public Domain</p>
    