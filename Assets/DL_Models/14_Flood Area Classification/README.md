# FLOOD AREA MULTI LABEL SEGMENTATION
### AI for Good | Image | Segmentation

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/14_Flood%20Area%20Classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/14_Flood%20Area%20Classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/14_Flood%20Area%20Classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/14_Flood%20Area%20Classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/14_Flood%20Area%20Classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Flood area segmentation/classification is a computer vision application that aims to identify and delineate flooded regions in satellite or aerial images. This use case is important for disaster management and emergency response operations, as it can help officials to quickly assess the extent of flooding and plan their response accordingly. The model uses image segmentation and classification techniques to accurately identify flooded regions, which can aid in decision-making for evacuation, rescue, and relief efforts..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Flood area multi-label segmentation has a valuable business impact in disaster response and urban planning. By accurately segmenting flooded areas into multiple categories such as residential, commercial, or critical infrastructure, emergency responders can prioritize rescue and recovery operations based on the severity of the affected areas. Additionally, urban planners can use this information to develop effective flood management strategies, optimize land use, and improve infrastructure resilience to mitigate the impact of future flooding events..</p>

### DATASET
- Flood area classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_segmentation/flood_segmentation_multi_label.zip).
- 1450 train images and 448 test images with segmenting labels  ['Background' 'Building-flooded' 'Building-non-flooded' 'Road-flooded' 'Road-non-flooded' 'Water' 'Tree' 'Vehicle' 'Pool' 'Grass'].

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/14_Flood%20Area%20Classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Segment the flooding area in UAS imageries.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/14_Flood%20Area%20Classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/14_Flood%20Area%20Classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Community Data License Agreement (permissive).</p>
    