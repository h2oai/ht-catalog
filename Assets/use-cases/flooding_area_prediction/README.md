# FLOODING AREA SEGMENTATION 
### AI for Good | Image | Segmentation

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/12_Flooding%20Area%20Prediction/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/12_Flooding%20Area%20Prediction/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/12_Flooding%20Area%20Prediction/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/12_Flooding%20Area%20Prediction/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/12_Flooding%20Area%20Prediction/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Flooding Area Segmentation Model is a computer vision model that can automatically identify and segment areas affected by flooding in images. This model can be useful for disaster response teams, allowing them to quickly identify and prioritize areas in need of aid..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Flooding area segmentation has a crucial business impact in urban planning and disaster management. By accurately delineating and mapping flooded areas, city authorities and emergency responders can effectively allocate resources, prioritize rescue efforts, and implement evacuation plans. This technology aids in real-time decision-making, reduces response time, and improves the overall efficiency of emergency management, ultimately minimizing the impact of flooding on infrastructure, public safety, and property..</p>

### DATASET
- Flooding area prediction dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_segmentation/Flooding Area Prediction.zip).
- 231 train images and 58 test images with class id "flood".

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/12_Flooding%20Area%20Prediction/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Segmenting the water regions in flooding area.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/12_Flooding%20Area%20Prediction/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/12_Flooding%20Area%20Prediction/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC0: Public Domain</p>
    