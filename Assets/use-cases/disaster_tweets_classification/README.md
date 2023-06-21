# DISASTER TWEETS CLASSIFICATION
### AI for Good | Text | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/49_Disaster%20Tweets%20Classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/49_Disaster%20Tweets%20Classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/49_Disaster%20Tweets%20Classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/49_Disaster%20Tweets%20Classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/49_Disaster%20Tweets%20Classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>The Disaster Tweets Classification model is designed to classify tweets as either disaster-related or not disaster-related using natural language processing techniques. The model was trained on a dataset of tweets labeled as either disaster-related or not disaster-related, and can be used to quickly identify tweets that may be relevant to emergency response efforts in the event of a disaster. This can be particularly useful for organizations involved in disaster response and relief efforts, as it can help them quickly identify and prioritize relevant information on social media.</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Disaster tweets classification is essential for crisis management and emergency response. By analyzing text data from social media platforms, machine learning models can classify tweets related to disasters or emergencies. Accurate disaster tweets classification enables real-time monitoring of critical events, helps in assessing the severity and impact of disasters, and facilitates efficient resource allocation and coordination of response efforts. It aids in disseminating timely information, mobilizing support, and enhancing situational awareness during emergencies. Disaster tweets classification technology contributes to effective crisis communication, rapid response, and better disaster management..</p>

### DATASET
- Disaster tweets classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/text_classification/disaster_tweets_classification.csv).
- 11370 train images with their labels(0 or 1).

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/49_Disaster%20Tweets%20Classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Classify tweets as either disaster-related or not disaster-related.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/49_Disaster%20Tweets%20Classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/49_Disaster%20Tweets%20Classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC0: Public Domain</p>
    