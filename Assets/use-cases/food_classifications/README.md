# FOOD IMAGE CLASSIFICATION 
### FnB | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/6_Food%20Classifications/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/6_Food%20Classifications/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/6_Food%20Classifications/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/6_Food%20Classifications/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/6_Food%20Classifications/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Our Food Classification model is used  to accurately identify and classify food items in images. This model is useful for food and nutrition professionals, allowing them to analyze and track dietary habits and trends accurately..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Food image classification has significant business impact in the food and beverage industry. It enables automatic categorization and identification of food items, which can be utilized for various purposes. Restaurants and food delivery services can benefit from accurate food image classification to improve menu organization, streamline order processing, and enhance customer experience. Food manufacturers can use this technology to automate quality control processes, ensuring product consistency and reducing errors in packaging and labeling. Additionally, nutrition and diet tracking applications can leverage food image classification to provide users with accurate nutritional information and personalized dietary recommendations..</p>

### DATASET
- Food classifications dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/food_classification.zip).
- 9866 images with 11 labels. Such as Bread,Dairy product,Dessert,Egg,Fried food,Meat,Noodles-Pasta,Rice, Seafood,Soup,Vegetable-Fruit.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/6_Food%20Classifications/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Categorize different types of food based on their visual characteristics.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/6_Food%20Classifications/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/6_Food%20Classifications/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC0: Public Domain</p>
    