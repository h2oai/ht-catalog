# BIRD VOICE CLASSIFICATION
### AI for Good | Audio | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/37_Bird%20Voice%20Classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/37_Bird%20Voice%20Classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/37_Bird%20Voice%20Classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/37_Bird%20Voice%20Classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/37_Bird%20Voice%20Classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>The Bird Voice Classification model is a machine learning model designed to identify and classify bird species based on their vocalizations. By analyzing bird calls and songs, the model can accurately identify different bird species and distinguish them from one another. This model can be useful for ecological studies, birdwatching, and conservation efforts, as it can provide information about the presence and abundance of different bird species in an area. Additionally, the model can be used to track changes in bird populations over time and monitor the impact of environmental factors on bird behavior and vocalizations..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Bird voice classification plays a crucial role in ornithology, ecological research, and biodiversity conservation. By leveraging audio signal processing techniques and machine learning algorithms, it enables the identification and classification of bird species based on their vocalizations. Accurate bird voice classification assists researchers in studying bird populations, monitoring habitats, and assessing ecological health. It supports conservation efforts, species monitoring, and understanding the impact of environmental changes on bird populations. Bird voice classification technology contributes to biodiversity preservation, ecological research, and the conservation of avian species..</p>

### DATASET
- Bird voice classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/audio_classification/whale_detection.zip).
- 5407 train images and 687 test images with 41 uniques labels.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/37_Bird%20Voice%20Classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Accurately identify the bird by using it's voice.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/37_Bird%20Voice%20Classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/37_Bird%20Voice%20Classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC0: Public Domain</p>
    