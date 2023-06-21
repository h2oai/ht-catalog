# WEATHER CLASSIFICATION
### AI for Good | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/34_Weather%20Classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/34_Weather%20Classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/34_Weather%20Classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/34_Weather%20Classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/34_Weather%20Classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>A Weather Classification model is a type of image classification model that can categorize different weather conditions based on input images. The model can be trained on datasets of images that represent various weather conditions, such as sunny, cloudy, rainy, snowy, foggy, and stormy. Once the model is trained, it can be used to classify new images of weather conditions with high accuracy, which can be useful for a variety of applications such as weather forecasting, climate modeling, and transportation safety..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Weather classification has a wide range of applications in industries such as agriculture, aviation, energy, and tourism. By analyzing meteorological data, satellite imagery, and machine learning algorithms, it enables the categorization and prediction of different weather conditions. Accurate weather classification supports decision-making processes related to crop management, flight operations, energy production, and tourism planning. It helps in assessing risks, optimizing resource allocation, and ensuring safety measures in various industries. Weather classification technology facilitates better planning, preparedness, and mitigation strategies for weather-related events, contributing to operational efficiency, safety, and economic stability..</p>

### DATASET
- Weather classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/weather_classification.zip).
- 1491 train images with 6 labels. such as alien_test,cloudy,foggy,rainy,shine,sunrise,.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/34_Weather%20Classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Identify and Classify the weather.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/34_Weather%20Classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/34_Weather%20Classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC0: Public Domain</p>
    