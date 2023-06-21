# TOXIC COMMENT CLASSIFICATION
### Content creation | Text | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/60_Wikipedia%20Toxic%20Comments/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/60_Wikipedia%20Toxic%20Comments/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/60_Wikipedia%20Toxic%20Comments/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/60_Wikipedia%20Toxic%20Comments/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/60_Wikipedia%20Toxic%20Comments/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Toxic Comment Classification is a natural language processing (NLP) task that involves identifying and categorizing toxic or offensive comments in online platforms, such as social media, discussion forums, or comment sections. The goal is to develop a model that can accurately classify comments into different categories, such as toxic, non-toxic, hate speech, or spam, to ensure a safer and more respectful online environment. This use case is particularly relevant for social media platforms, online communities, and content moderation teams who aim to proactively identify and filter out harmful content. By automating the identification of toxic comments, platforms can protect users from harassment, bullying, and other negative experiences. Additionally, it helps moderators prioritize their efforts by flagging potentially harmful content for review, leading to a more efficient content moderation process..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Implementing a toxic comment classification system can have several positive impacts on businesses and online communities. Firstly, it helps maintain a positive and inclusive online environment by promptly detecting and filtering out toxic comments, which enhances user satisfaction and engagement. By reducing the presence of offensive content, companies can protect their brand reputation and retain users. Furthermore, it contributes to fostering a safer online space, making it more appealing to a wider range of users. From a content moderation perspective, automating the identification of toxic comments allows moderation teams to handle a larger volume of user-generated content effectively. This results in improved efficiency, reduced manual effort, and quicker response times to address potentially harmful situations. Overall, toxic comment classification helps businesses and online platforms create a more welcoming and secure environment for their users..</p>

### DATASET
- Wikipedia toxic comments dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/jigsaw_text_classification.zip).
- 159571 train texts with 6 labels. Each label has value either 0 or 1..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/60_Wikipedia%20Toxic%20Comments/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Classify the Comments.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/60_Wikipedia%20Toxic%20Comments/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/60_Wikipedia%20Toxic%20Comments/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    