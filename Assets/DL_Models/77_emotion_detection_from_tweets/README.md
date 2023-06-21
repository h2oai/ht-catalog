# EMOTION DETECTION FROM TWEETS
### AI for good | Text | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/77_emotion_detection_from_tweets/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/77_emotion_detection_from_tweets/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/77_emotion_detection_from_tweets/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/77_emotion_detection_from_tweets/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/77_emotion_detection_from_tweets/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Emotion detection from tweets refers to the automated identification and classification of emotions expressed within short messages posted on the social media platform Twitter. This technology analyzes linguistic cues, sentiment, and contextual information to discern various emotions, providing valuable insights into public sentiment, opinion trends, and social dynamics.</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Emotion detection from tweets has significant business implications in social media analytics and marketing. By automatically identifying and classifying emotions expressed in tweets, this technology allows businesses to gauge public sentiment, monitor brand reputation, and tailor marketing strategies accordingly. It enables real-time customer feedback analysis, facilitates proactive customer support, and enhances brand perception and customer satisfaction. Businesses can adapt their products, services, and communications to meet customer expectations, driving customer loyalty and market growth..</p>

### DATASET
- Emotion_detection_from_tweets dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/text_classification/tweet_emotions.csv).
- 40000 train rows with 13 different classes.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/77_emotion_detection_from_tweets/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Detect and classify emotions expressed in tweets using text classification techniques for understanding public sentiment and opinion trends..</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: bert-base-uncased</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 16</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 2</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 1e-05</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/77_emotion_detection_from_tweets/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/77_emotion_detection_from_tweets/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC0: Public Domain</p>
    