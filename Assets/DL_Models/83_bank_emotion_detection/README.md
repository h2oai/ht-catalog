# BANK EMOTION DETECTION
### AI for good | Text | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/83_bank_emotion_detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/83_bank_emotion_detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/83_bank_emotion_detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/83_bank_emotion_detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/83_bank_emotion_detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Bank emotion detection involves the automated analysis and detection of customer emotions and sentiments during interactions with banking services or systems. This technology utilizes natural language processing and sentiment analysis techniques to discern customer satisfaction, frustration, or other emotional states, helping banks enhance customer experience and improve service quality.</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Bank emotion detection has substantial business impact in the banking and financial services industry. By analyzing customer emotions and sentiments during interactions, this technology provides valuable insights into customer satisfaction, frustration, or other emotional states. Banks can utilize this information to enhance customer experience, tailor their services, and improve customer retention. It enables proactive customer support, targeted marketing campaigns, and personalized financial solutions, fostering customer loyalty and driving business growth..</p>

### DATASET
- Bank_emotion_detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/text_classification/bank_emotion_detection.zip).
- 108 train samples with 2 classes.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/83_bank_emotion_detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Detect and classify customer emotions during interactions with banking services using text classification techniques for enhancing customer experience..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/83_bank_emotion_detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/83_bank_emotion_detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Unknown</p>
    