# INDIAN ROADS SEGMENTATION
### AI for Good | Image | Segmentation

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/15_Indian%20Roads%20segmentation/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/15_Indian%20Roads%20segmentation/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/15_Indian%20Roads%20segmentation/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/15_Indian%20Roads%20segmentation/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/15_Indian%20Roads%20segmentation/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Indian roads, potholes, and footpaths segmentation model can be used to accurately identify and locate areas  such as potholes ,roads and footpaths. This information can be used by city planners and road maintenance teams to prioritize repairs, improve road safety, and reduce accidents caused by damaged roads. The model can also be used to monitor the progress of repairs and ensure that they are carried out effectively..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Indian roads segmentation has a significant business impact in transportation and logistics. By accurately segmenting and mapping road networks in India, logistics companies can optimize route planning, fleet management, and delivery operations. This technology helps reduce transportation costs, improve delivery efficiency, and enhance customer service by providing accurate and up-to-date road network information. Additionally, government agencies can utilize this data for infrastructure planning, traffic management, and urban development, ultimately leading to improved transportation systems and economic growth..</p>

### DATASET
- Indian roads segmentation dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/instance_segmentation/indian_road_seg_v4.zip).
- 2475 train images, 752 validation images, 753 validation images with labels ['roads' 'potholes' 'footpaths' 'shallow paths' 'backgrounds'].

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/15_Indian%20Roads%20segmentation/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Segment the roads, potholes, and footpaths in the images.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/15_Indian%20Roads%20segmentation/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/15_Indian%20Roads%20segmentation/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>GPL 2</p>
    