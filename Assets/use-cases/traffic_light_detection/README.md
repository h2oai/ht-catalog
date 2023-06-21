# TRAFFIC LIGHT OBJECT DETECTION
### AI for Good | Image | Object Detection

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/45_Traffic%20Light%20Detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/45_Traffic%20Light%20Detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/45_Traffic%20Light%20Detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/45_Traffic%20Light%20Detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/45_Traffic%20Light%20Detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>A Traffic Light Detection model is designed to detect the location and state (red, yellow, or green) of traffic lights in image data. This can be useful in a variety of applications, such as autonomous driving or traffic monitoring systems. The model uses object detection techniques to locate the traffic lights in the image and then applies image segmentation to determine the color of the traffic light. The model is typically trained on large datasets of annotated images containing traffic lights, including variations in lighting conditions, weather, and perspective. Once trained, the model can accurately detect and classify traffic lights in real-world scenarios..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Traffic light detection is a crucial component of intelligent transportation systems and autonomous vehicles. By analyzing visual data from cameras or sensors, it enables the identification and localization of traffic lights at intersections or roadways. Accurate traffic light detection assists in traffic flow optimization, autonomous vehicle navigation, and advanced driver-assistance systems. It enables vehicles to perceive and respond to traffic signals, improving road safety and reducing the risk of accidents. Traffic light detection technology contributes to the development of efficient and safe transportation systems, promoting smoother traffic operations and supporting the transition towards autonomous driving..</p>

### DATASET
- Traffic light detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/object_detection/traffic-light-detection.zip).
- 1222 train images with green,red,yellow labels.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/45_Traffic%20Light%20Detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Detect the traffic lights in image data.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/45_Traffic%20Light%20Detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/45_Traffic%20Light%20Detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>MIT License</p>
    