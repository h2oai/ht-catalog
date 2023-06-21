# FLOWER RECOGNITION FROM IMAGES
### AI for good | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/95_flower_recognition/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/95_flower_recognition/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/95_flower_recognition/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/95_flower_recognition/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/95_flower_recognition/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Flower recognition involves the automated identification and classification of different types of flowers based on their visual characteristics, such as color, shape, and petal arrangement. This technology utilizes computer vision algorithms and machine learning models to analyze flower images and assign them to specific flower species or categories..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Flower recognition has business implications in various industries, including horticulture, floriculture, and e-commerce. By automating the flower identification process, horticulturists and florists can quickly and accurately classify flowers, aiding in plant breeding, cultivation, and floral arrangement planning. E-commerce platforms can leverage flower recognition to improve search functionalities, offer personalized recommendations, and streamline product categorization, enhancing the customer shopping experience. Additionally, botanical gardens and conservation efforts can benefit from flower recognition in documenting and monitoring plant species, supporting biodiversity research, and preservation initiatives..</p>

### DATASET
- Flower_recognition dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/flower_recognition.zip).
- 5000 train images with their 5 labels such as lilly,lotus,orchid,sunflower,tulip.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/95_flower_recognition/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>accurately classify an input flower image into its corresponding species or category, such as roses, sunflowers, daisies, or tulips..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/95_flower_recognition/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/95_flower_recognition/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Unknown</p>
    