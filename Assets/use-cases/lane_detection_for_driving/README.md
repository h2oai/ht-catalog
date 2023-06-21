# LANE DETECTION FOR DRIVING
### AI for Good | Image | Segmentation

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/41_Lane%20Detection%20for%20Driving/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/41_Lane%20Detection%20for%20Driving/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/41_Lane%20Detection%20for%20Driving/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/41_Lane%20Detection%20for%20Driving/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/41_Lane%20Detection%20for%20Driving/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Lane detection for driving is a technique used in autonomous vehicles to identify and track the lanes on the road. This is done using image segmentation, where the lanes are isolated from the rest of the image. The lane detection model analyzes the input image, identifies the lane markers, and generates an output image with the lane markers highlighted. This information is then used by the autonomous vehicle to maintain its position within the lane and navigate the road safely. Lane detection is a critical component of autonomous driving, as it helps ensure the safety of passengers and other drivers on the road..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Lane detection technology has a significant impact on the field of autonomous driving, advanced driver-assistance systems (ADAS), and road safety. By analyzing live or recorded video feeds from cameras mounted on vehicles, it enables the detection and tracking of lane markings on the road. Accurate lane detection assists in vehicle positioning, lane keeping, and autonomous navigation. It enhances road safety by providing warnings and assistance to drivers in maintaining their lanes. Lane detection technology contributes to the development of safer and more efficient transportation systems, reducing the risk of accidents and improving traffic flow..</p>

### DATASET
- Lane detection for driving dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_segmentation/lane-detection.zip).
- 3075 train images and 129 test images with 3 uniques segmentation labels ['left-lane' 'right-lane' 'background'].

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/41_Lane%20Detection%20for%20Driving/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Identify and segment the lanes on the road..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/41_Lane%20Detection%20for%20Driving/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/41_Lane%20Detection%20for%20Driving/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC BY-NC-SA 4.0</p>
    