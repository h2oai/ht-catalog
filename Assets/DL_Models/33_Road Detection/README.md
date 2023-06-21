# ROAD DETECTION IN URBAN AREAS
### AI for Good | Image | Segmentation

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/33_Road%20Detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/33_Road%20Detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/33_Road%20Detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/33_Road%20Detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/33_Road%20Detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Road detection models are essential for various applications, such as urban planning, transportation management, and autonomous driving. In urban areas, where roads can be complex and diverse, road detection from satellite images is a challenging task. This is because satellite images may contain various objects and features, such as buildings, trees, and cars, which can interfere with road detection. To overcome these challenges, the road detection model uses image processing techniques and machine learning algorithms to accurately identify and classify road segments in urban areas. The model can be trained on large datasets of satellite images labeled with road and non-road segments, and it can then be used to classify new satellite images for road detection applications..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Road detection technology is essential in the fields of autonomous driving, transportation planning, and infrastructure development. By analyzing aerial or satellite imagery using computer vision algorithms, it enables the automated identification and mapping of roads and road networks. Accurate road detection supports navigation systems, intelligent transportation systems, and urban planning initiatives. It aids in route planning, traffic management, and infrastructure maintenance. Road detection technology enhances road safety, improves transportation efficiency, and contributes to the development of smart cities and advanced transportation solutions..</p>

### DATASET
- Road detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_segmentation/road_data.zip).
- 6226 train images with class id ''road".

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/33_Road%20Detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Detect the roads in urban areas.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: resnet101</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 8</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 5</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/33_Road%20Detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/33_Road%20Detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    