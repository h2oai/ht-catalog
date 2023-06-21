# FOOTPATH RECOGNITION IN ROADS
### AI for good | Image | Semantic Segmentation

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/92_footpath_recognition/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/92_footpath_recognition/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/92_footpath_recognition/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/92_footpath_recognition/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/92_footpath_recognition/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Footpath recognition involves the automated detection and recognition of footpaths or pedestrian walkways in images or video data. This technology utilizes computer vision techniques to identify and segment footpaths, assisting in urban planning, navigation systems, and pedestrian safety initiatives..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Footpath recognition has business implications in urban planning, transportation, and navigation systems. By automatically detecting and recognizing pedestrian walkways or footpaths in images or video data, this technology aids in pedestrian safety, infrastructure development, and navigation optimization. Urban planners can analyze footpath usage, identify areas needing improvement, and design pedestrian-friendly environments. Navigation systems can provide accurate pedestrian routing, enhance mobility options, and improve overall transportation efficiency..</p>

### DATASET
- Footpath_recognition dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_segmentation/footpath-image-dataset.zip).
- 3000 train images with their masks.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/92_footpath_recognition/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Detect and recognize footpaths or pedestrian walkways in images or video data using computer vision techniques for urban planning and pedestrian safety..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/92_footpath_recognition/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/92_footpath_recognition/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC BY-SA 4.0</p>
    