# GUN CLASSIFIER
### AI for good | Audio | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/87_Gun_Classifier/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/87_Gun_Classifier/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/87_Gun_Classifier/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/87_Gun_Classifier/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/87_Gun_Classifier/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Gun classifier refers to the automated recognition and classification of firearms or gun-related objects from images or video data. This technology employs computer vision algorithms and deep learning models to identify and distinguish between different types of guns, aiding in security applications, law enforcement, and public safety efforts.</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Gun classifier has business implications in security and public safety industries. By automatically recognizing and classifying firearms or gun-related objects from images or video data, this technology aids in threat detection, security screening, and law enforcement efforts. It enhances public safety measures, supports security personnel in identifying potential risks, and contributes to crime prevention. Deploying gun classifiers in critical infrastructure, public spaces, or high-risk areas helps mitigate security threats, safeguarding individuals and assets..</p>

### DATASET
- Gun_classifier dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/audio_classification/Gun_sound_detection.zip).
- 851 train audio samples with 9 different classes..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/87_Gun_Classifier/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Recognize and classify firearms or gun-related objects from images or video data using computer vision techniques for security and public safety applications..</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: resnet50</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 16</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 5</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/87_Gun_Classifier/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/87_Gun_Classifier/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Unknown</p>
    