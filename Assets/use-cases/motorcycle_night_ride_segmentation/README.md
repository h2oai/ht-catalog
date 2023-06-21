# MOTORCYCLE NIGHT RIDE SEGMENTATION
### AI for good | Image | Semantic Segmentation

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/97_motorcycle_night_ride_segmentation/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/97_motorcycle_night_ride_segmentation/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/97_motorcycle_night_ride_segmentation/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/97_motorcycle_night_ride_segmentation/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/97_motorcycle_night_ride_segmentation/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Motorcycle night ride segmentation involves the automated segmentation or separation of motorcycle objects from nighttime scenes or videos. This technology utilizes computer vision algorithms and image processing techniques to distinguish motorcycle riders and their vehicles from the background, even in low-light conditions..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Motorcycle night ride segmentation has business implications in areas such as traffic surveillance, safety analysis, and law enforcement. By accurately segmenting motorcycles and riders from nighttime scenes, traffic monitoring systems can track motorcycle movement, analyze traffic patterns, and identify potential safety risks. Law enforcement agencies can utilize this technology for traffic law enforcement, crime prevention, or accident investigations. It contributes to improved road safety, enhanced traffic management, and effective law enforcement measures..</p>

### DATASET
- Motorcycle_night_ride_segmentation dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_segmentation/Motorcycle_Night_Ride_Dataset.zip).
- 200 train imags with their masks.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/97_motorcycle_night_ride_segmentation/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>The prediction target for motorcycle night ride segmentation is to accurately segment the motorcycle and its rider from the surrounding nighttime environment, enabling various applications such as safety analysis, traffic monitoring, or video analytics..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/97_motorcycle_night_ride_segmentation/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/97_motorcycle_night_ride_segmentation/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Attribution 4.0 International (CC BY 4.0)</p>
    