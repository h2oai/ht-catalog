# ROAD QUALITY CLASSIFICATION 
### AI for Good | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/9_Road%20Quality%20Classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/9_Road%20Quality%20Classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/9_Road%20Quality%20Classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/9_Road%20Quality%20Classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/9_Road%20Quality%20Classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>The Road Quality Classification model is used to automatically classify road quality based on image, which can be used for road maintenance planning and improving safety. It provides a cost-effective and efficient solution for monitoring road conditions on a large scale..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Road quality classification has a substantial impact on transportation and infrastructure management. By automatically assessing the quality of road surfaces, this technology helps transportation authorities identify areas that require maintenance or repairs. It enables efficient resource allocation, ensuring that limited funds are directed towards the most critical areas. Road quality classification contributes to safer and smoother travel experiences, reducing vehicle damage and minimizing accidents caused by poor road conditions. Additionally, it supports urban planning efforts by providing valuable data on road infrastructure conditions, enabling authorities to make informed decisions regarding road improvement projects..</p>

### DATASET
- Road quality classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/road_image_sih_classification.zip).
- 1659 images with 4 labels.Such as good,poor,very_poor,satisfactory.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/9_Road%20Quality%20Classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Classify the roads based on their quality.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: resnet50</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 32</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 5</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/9_Road%20Quality%20Classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/9_Road%20Quality%20Classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    