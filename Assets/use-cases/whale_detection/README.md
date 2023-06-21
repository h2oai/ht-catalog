# WHALE DETECTION IN AUDIOS
### AI for Good | Audio | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/20_Whale%20Detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/20_Whale%20Detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/20_Whale%20Detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/20_Whale%20Detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/20_Whale%20Detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Whale detection model using audio data is designed to identify and classify sounds emitted by whale. This model can be used by marine biologists and researchers to study whale behavior, migration patterns, and population dynamics. By analyzing the acoustic features of whale sounds such as frequency, duration, and amplitude, the model can accurately identify whale. The model uses various techniques such as signal processing, machine learning, and deep learning to extract features from audio recordings and classify them..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Whale detection in audios has significant business impact in industries related to marine research, environmental monitoring, and maritime operations. By accurately detecting and classifying whale vocalizations in audio recordings, it helps in understanding whale behavior, migration patterns, and population dynamics. This information is crucial for marine biologists, conservationists, and policymakers in making informed decisions regarding marine conservation and protection efforts. In the shipping and maritime industry, whale detection contributes to the implementation of measures to avoid collisions with whales, ensuring compliance with regulations and minimizing environmental impact. Furthermore, in the field of underwater acoustics, whale detection supports research and development of technologies for passive acoustic monitoring, providing valuable insights into the marine ecosystem and facilitating oceanic studies..</p>

### DATASET
- Whale detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/audio_classification/whale_detection.zip).
- 30000 audio rows with thei label 0 or 1.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/20_Whale%20Detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Identify whether the audio signal has whale or not.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: resnet50</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 32</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 8</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/20_Whale%20Detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/20_Whale%20Detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Copyright © 2011 by Cornell University and the Cornell Research Foundation, Inc. </p>
    