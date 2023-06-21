# INTENT CLASSIFICATION IN SPEECH RECOGNITION
### AI for good | Speech/Audio | Recognition

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/67_intent_classification_speech_recognition/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/67_intent_classification_speech_recognition/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/67_intent_classification_speech_recognition/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/67_intent_classification_speech_recognition/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/67_intent_classification_speech_recognition/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Intent classification in speech recognition involves accurately determining the underlying intent or purpose behind a spoken sentence or phrase. This technology aims to understand the user's intended action or query by analyzing the content and context of the spoken input. It enables intelligent voice assistants and chatbots to provide appropriate responses and fulfill user requests effectively..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Intent classification in speech recognition has significant business implications across industries. It enhances customer service by enabling accurate identification of user needs and queries, leading to faster and more relevant responses. In e-commerce, it improves personalized recommendations and enables voice-based shopping experiences. In call centers, it automates call routing and improves the efficiency of customer support. Intent classification also finds applications in virtual assistants, smart home devices, and voice-controlled applications, enhancing user experience and engagement..</p>

### DATASET
- Intent_classification_speech_recognition dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/intent_classification_speech_recognition.zip).
- 563 train audio samples with their transcript..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/67_intent_classification_speech_recognition/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Accurately categorizing the user's intended action or query based on the spoken input.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: openai/whisper-base.en</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 1</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 3</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 1e-05</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/67_intent_classification_speech_recognition/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/67_intent_classification_speech_recognition/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    