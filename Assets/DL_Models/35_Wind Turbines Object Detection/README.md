# WIND TURBINES OBJECT DETECTION
### AI for Good | Image | Object Detection

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/35_Wind%20Turbines%20Object%20Detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/35_Wind%20Turbines%20Object%20Detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/35_Wind%20Turbines%20Object%20Detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/35_Wind%20Turbines%20Object%20Detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/35_Wind%20Turbines%20Object%20Detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>A Wind Turbines Object Detection model is used to identify and locate wind turbines in images. The model uses deep learning algorithms and image processing techniques to detect the presence and location of wind turbines in the image. It can be used for various applications such as renewable energy planning, maintenance scheduling, and environmental impact assessment. The model works by analyzing the image pixel by pixel and identifying patterns and shapes that resemble wind turbines. .</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Wind turbines object detection technology plays a crucial role in the renewable energy sector. By leveraging computer vision techniques, it enables the detection and localization of wind turbines in aerial or satellite imagery. Accurate wind turbines object detection aids in site selection, monitoring, and maintenance of wind farms. It assists in optimizing energy production, detecting potential issues or malfunctions, and ensuring proper functioning of wind turbines. Wind turbines object detection technology contributes to the efficient utilization of renewable energy resources, supports sustainable energy production, and helps in achieving climate change mitigation goals..</p>

### DATASET
- Wind turbines object detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/object_detection/wind_turbines_detection.zip).
- 2628 train images with their class ids.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/35_Wind%20Turbines%20Object%20Detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Detect the wind turbines using object detection techniques.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/35_Wind%20Turbines%20Object%20Detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/35_Wind%20Turbines%20Object%20Detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC0: Public Domain</p>
    