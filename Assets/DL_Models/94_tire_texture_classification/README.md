# TIRE TEXTURE CLASSIFICATION
### Manufacturing | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/94_tire_texture_classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/94_tire_texture_classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/94_tire_texture_classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/94_tire_texture_classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/94_tire_texture_classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Tire texture classification involves the automated identification and classification of tire textures or patterns based on their visual characteristics. This technology utilizes computer vision algorithms and machine learning techniques to analyze tire images and classify them into different categories, such as slick tires, all-terrain tires, or winter tires..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Tire texture classification has business implications in the automotive industry, particularly in areas such as tire manufacturing, retail, and vehicle safety. By automating the classification process, tire manufacturers can ensure consistent quality control and proper categorization of their products. Retailers can improve inventory management and provide more accurate product recommendations to customers based on their specific needs and preferences. Moreover, automotive safety systems can utilize tire texture classification to enhance vehicle performance and optimize driving conditions based on the type of tire in use, contributing to safer and more efficient transportation..</p>

### DATASET
- Tire_texture_classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/tire_texture_classification.zip).
- 703 train images with their labels such as cracked or normal..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/94_tire_texture_classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>accurately classify an input tire image into its corresponding texture category, helping to identify the type of tire being used..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/94_tire_texture_classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/94_tire_texture_classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC0: Public Domain</p>
    