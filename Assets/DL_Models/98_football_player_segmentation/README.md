# FOOTBALL  PLAYER SEGMENTATION
### AI for good | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/98_football_player_segmentation/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/98_football_player_segmentation/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/98_football_player_segmentation/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/98_football_player_segmentation/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/98_football_player_segmentation/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'> Football player segmentation involves the automated separation and extraction of football players from live game footage or video recordings. This technology utilizes computer vision algorithms and machine learning models to identify and segment individual players from complex scenes, enabling various applications such as player tracking, sports analytics, or immersive fan experiences..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Football player segmentation has business implications in the sports industry, including sports broadcasting, team analysis, and fan engagement. By accurately segmenting players from game footage, broadcasters can provide enhanced visual experiences, highlight specific player actions, and deliver more engaging sports content to viewers. Sports teams and analysts can utilize player segmentation for performance analysis, tactical evaluations, and injury prevention strategies. It contributes to improved sports coverage, enhanced fan experiences, and data-driven decision-making in professional football..</p>

### DATASET
- Football_player_segmentation dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_segmentation/football-player-segmentation.zip).
- 512 train images with their masks.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/98_football_player_segmentation/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>The prediction target for football player segmentation is to accurately segment each football player present in the video frames, allowing for detailed player tracking, performance analysis, and visual enhancements in sports broadcasts or video content..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/98_football_player_segmentation/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/98_football_player_segmentation/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC0: Public Domain</p>
    