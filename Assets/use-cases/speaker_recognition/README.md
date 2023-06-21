# SPEAKER RECOGNITION
### AI for good | Audio | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/89_speaker_recognition/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/89_speaker_recognition/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/89_speaker_recognition/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/89_speaker_recognition/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/89_speaker_recognition/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Speaker recognition refers to the identification and verification of individuals based on their unique vocal characteristics or speech patterns. This technology analyzes voice signals, speaker-specific features, and linguistic patterns to establish the identity of a speaker, facilitating applications such as access control, voice authentication, and forensic investigations..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Speaker recognition has significant business implications in various industries, including security, telecommunications, and customer service. By accurately identifying and verifying individuals based on their unique vocal characteristics, this technology enhances access control systems, voice authentication processes, and fraud prevention measures. It enables secure transactions, personalized customer experiences, and targeted communication. It finds applications in call centers, voice-based virtual assistants, and telecommunication networks, enhancing operational efficiency and customer satisfaction.</p>

### DATASET
- Speaker_recognition dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/audio_classification/speaker_recognition.zip).
- 2511 train audio samples with 50 different speakers.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/89_speaker_recognition/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Identify and verify individuals based on vocal characteristics or speech patterns using speaker recognition techniques for voice authentication and access control..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/89_speaker_recognition/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/89_speaker_recognition/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Unknown</p>
    