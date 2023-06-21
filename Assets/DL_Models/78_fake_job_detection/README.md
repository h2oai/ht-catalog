# FAKE JOB POST DETECTION FROM POSTS
### AI for good | Text | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/78_fake_job_detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/78_fake_job_detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/78_fake_job_detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/78_fake_job_detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/78_fake_job_detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Fake job detection entails the identification and classification of fraudulent or misleading job postings in online job platforms. This technology leverages natural language processing and machine learning techniques to analyze job descriptions, qualifications, and other relevant factors, assisting job seekers in avoiding scams and ensuring a safe and trustworthy job search experience..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Fake job detection offers critical business benefits for job platforms, recruitment agencies, and job seekers. By automatically identifying and flagging fraudulent job postings, this technology helps job platforms maintain their integrity, trustworthiness, and user satisfaction. It protects job seekers from scams, ensures a safe and reliable job search environment, and fosters a positive user experience. It contributes to building a reputable job marketplace, attracting top talent, and facilitating successful job placements..</p>

### DATASET
- Fake_job_detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/text_classification/fake_job_postings.csv).
- 17880 train text samples with 2 classes(0 or 1).

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/78_fake_job_detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Detect and classify fraudulent job postings in online platforms using text classification techniques for a safe and trustworthy job search experience.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/78_fake_job_detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/78_fake_job_detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC0: Public Domain</p>
    