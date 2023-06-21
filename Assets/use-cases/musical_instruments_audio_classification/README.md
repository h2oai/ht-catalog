# MUSICAL INSTRUMENTS AUDIO CLASSIFICATION
### AI for good | Audio | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/85_musical_instruments_audio_classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/85_musical_instruments_audio_classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/85_musical_instruments_audio_classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/85_musical_instruments_audio_classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/85_musical_instruments_audio_classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Musical instruments audio classification involves the automatic recognition and classification of different musical instruments based on audio recordings. This technology analyzes acoustic features and timbral characteristics to distinguish between instruments, facilitating tasks such as instrument identification, music transcription, and sound synthesis..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Musical instruments audio classification has business implications in various industries, including music production, entertainment, and e-commerce. By automatically recognizing and classifying different musical instruments based on audio recordings, this technology enhances music transcription, instrument identification, and sound synthesis. Music producers can optimize their production workflows, create more immersive sound experiences, and develop innovative music technologies. E-commerce platforms can provide targeted recommendations and personalized shopping experiences for musical instrument enthusiasts, driving customer engagement and sales..</p>

### DATASET
- Musical_instruments_audio_classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/audio_classification/musical_instruments_audio_classification.zip).
- 2629 train audio samples with 4 classes..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/85_musical_instruments_audio_classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Classify different musical instruments based on audio recordings using audio classification techniques for music identification and sound synthesis..</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: resnet50</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 8</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 5</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/85_musical_instruments_audio_classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/85_musical_instruments_audio_classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC0: Public Domain</p>
    