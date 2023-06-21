# AUDIO EMOTION DETECTION
### AI for Good | Audio | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/42_Audio%20Emotion%20Detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/42_Audio%20Emotion%20Detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/42_Audio%20Emotion%20Detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/42_Audio%20Emotion%20Detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/42_Audio%20Emotion%20Detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Audio Emotion Detection model is designed to recognize human emotions from audio signals. With the help of various audio datasets, the model can be trained to identify different emotions such as happiness, sadness, anger, fear, and more. This technology can be applied in various industries such as entertainment, healthcare, and customer service to improve user experience and engagement. For example, in the entertainment industry, the model can be used to recommend music playlists based on the user's mood. In healthcare, the model can be used to detect emotions in patients' voices and provide personalized treatment plans accordingly. Similarly, in customer service, the model can be used to detect the customer's emotions during a call and provide customized solutions to improve customer satisfaction..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Audio emotion detection has applications in various fields, including psychology, mental health, and market research. By analyzing speech signals using machine learning algorithms, it enables the identification and classification of emotions conveyed in audio recordings. Accurate audio emotion detection assists in understanding human emotions, facilitating psychological research, and supporting mental health assessments. It also has potential applications in market research, enabling companies to gauge customer sentiment and emotional responses to products or services. Audio emotion detection technology enhances emotional understanding, psychological analysis, and market insights..</p>

### DATASET
- Audio emotion detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/audio_classification/audio_emotion_detection.zip).
- 12798 train images with 7 uniques labels [Angry, Disgusted, Fearful,Happy,Neutral,Sad,Suprised].

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/42_Audio%20Emotion%20Detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Classify human emotions from audio signals.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/42_Audio%20Emotion%20Detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/42_Audio%20Emotion%20Detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC BY-NC-SA 4.0</p>
    