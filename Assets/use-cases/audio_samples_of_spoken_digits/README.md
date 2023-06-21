# SPOKEN DIGITS CLASSIFICATION
### Voice technology. | Audio | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/52_Audio%20Samples%20of%20Spoken%20Digits/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/52_Audio%20Samples%20of%20Spoken%20Digits/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/52_Audio%20Samples%20of%20Spoken%20Digits/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/52_Audio%20Samples%20of%20Spoken%20Digits/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/52_Audio%20Samples%20of%20Spoken%20Digits/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>The spoken digits classification use case involves developing a machine learning model that can accurately recognize and classify spoken digits. The model takes audio recordings of spoken digits as input and predicts the corresponding digit. This task is commonly used in various applications such as voice assistants, automated phone systems, and speech recognition technologies..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Accurate spoken digits classification has significant business impact across multiple industries. In the telecommunications sector, it can enhance call routing systems, enabling more efficient and automated customer support. In the finance industry, it can improve the security of voice-based authentication systems. Additionally, in the automotive sector, it can enhance hands-free calling and voice control functionalities in vehicles. By automating the recognition and classification of spoken digits, businesses can streamline operations, improve customer experiences, and enable more seamless interactions through voice interfaces..</p>

### DATASET
- Audio samples of spoken digits dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/amnist_audio_regression.zip).
- 30000 audio samples of spoken digits (0-9) of 60 different speakers..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/52_Audio%20Samples%20of%20Spoken%20Digits/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Classify the Spoken Digits into 0 to 9.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/52_Audio%20Samples%20of%20Spoken%20Digits/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/52_Audio%20Samples%20of%20Spoken%20Digits/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    