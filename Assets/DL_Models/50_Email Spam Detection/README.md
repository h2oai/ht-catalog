# EMAIL SPAM CLASSIFICATION
### AI for Good | Text | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/50_Email%20Spam%20Detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/50_Email%20Spam%20Detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/50_Email%20Spam%20Detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/50_Email%20Spam%20Detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/50_Email%20Spam%20Detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Email Spam Detection model is designed to classify emails into spam or non-spam categories. Using a dataset of labeled emails, the model is trained to recognize common features of spam emails, such as specific keywords, suspicious URLs, or message formatting. Once trained, the model can accurately classify new incoming emails as either spam or non-spam, helping to reduce the amount of unwanted emails in users' inboxes and prevent potential security risks associated with phishing or malware attacks. The Email Spam Detection model can be integrated into email services or used as a standalone tool to improve email management and security..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Email spam detection is crucial for maintaining efficient communication channels and preventing cyber threats. By analyzing email content and metadata, machine learning algorithms can identify and filter out unsolicited and malicious emails. Accurate email spam detection protects users from phishing attacks, malware, and unwanted solicitations. It helps in safeguarding sensitive information, ensuring email security, and maintaining productivity by reducing the time and effort spent on dealing with spam messages. Email spam detection technology enhances email communication efficiency, protects against cyber threats, and preserves data integrity..</p>

### DATASET
- Email spam detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/text_classification/email_spam_classification.csv).
- 5729 train images with their labels (spam or not_spam).

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/50_Email%20Spam%20Detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Classify emails into spam or non-spam categories.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/50_Email%20Spam%20Detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/50_Email%20Spam%20Detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Unknown</p>
    