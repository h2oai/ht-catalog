# URBAN SOUND CLASSIFICATION
### AI for Good | Audio | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/38_Urban%20Sound%20Classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/38_Urban%20Sound%20Classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/38_Urban%20Sound%20Classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/38_Urban%20Sound%20Classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/38_Urban%20Sound%20Classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>The Urban Sound Classification model is designed to classify audio signals into different sound categories commonly heard in urban environments such as sirens, car horns, and street music. The model uses audio signal processing techniques and machine learning algorithms to extract features such as frequency, pitch, and amplitude from audio samples and then trains a classifier to recognize patterns in these features and categorize them into their respective sound classes. The model has applications in noise pollution monitoring, city planning, and urban soundscape analysis..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Urban sound classification has practical applications in urban planning, noise pollution management, and public health. By analyzing audio recordings using machine learning algorithms, it enables the classification and identification of different urban sounds, such as traffic noise, sirens, construction noise, and public transport sounds. Accurate urban sound classification aids in assessing noise pollution levels, identifying noise sources, and implementing mitigation strategies. It supports urban planning initiatives, noise regulation enforcement, and the improvement of living conditions in urban areas. Urban sound classification technology contributes to creating healthier and more livable cities..</p>

### DATASET
- Urban sound classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/audio_classification/urban_sound_classification.zip).
- 8732 train images with 10 uniques labels.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/38_Urban%20Sound%20Classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Classify audio signals into different sound categories commonly heard in urban environments.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/38_Urban%20Sound%20Classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/38_Urban%20Sound%20Classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'> CC BY-NC 3.0</p>
    