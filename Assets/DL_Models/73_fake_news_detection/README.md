# FAKE NEWS DETECTION IN DOCUMENTS
### Media | Text | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/73_fake_news_detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/73_fake_news_detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/73_fake_news_detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/73_fake_news_detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/73_fake_news_detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Fake news detection in documents refers to the automated identification and classification of misinformation or fabricated content within textual documents. This technology helps combat the spread of false information by analyzing linguistic patterns, fact-checking sources, and assessing the credibility of the content, assisting users in distinguishing between reliable and unreliable information..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>The business impact of fake news detection in documents is crucial for maintaining trust, credibility, and reputation in the digital age. By automatically identifying and flagging fake or misleading content, this technology helps media organizations, news agencies, and online platforms to ensure the integrity of their news sources and protect their users from misinformation. It enhances user trust, fosters a reliable information ecosystem, and safeguards brands' credibility, contributing to sustained user engagement, customer loyalty, and brand loyalty..</p>

### DATASET
- Fake_news_detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/text_classification/fake_news_detection.csv).
- 78617 train rows with their labels.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/73_fake_news_detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Detect and classify fake news within textual documents using text classification techniques for accurate information assessment.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/73_fake_news_detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/73_fake_news_detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>GNU Lesser General Public License</p>
    