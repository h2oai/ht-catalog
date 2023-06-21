# TEXT SUMMARIZATION IN NEWS STORIES
### Content creation | Text | Sequence to Sequence

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/58_CNN%20and%20Daily%20Mail%20News%20Stories/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/58_CNN%20and%20Daily%20Mail%20News%20Stories/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/58_CNN%20and%20Daily%20Mail%20News%20Stories/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/58_CNN%20and%20Daily%20Mail%20News%20Stories/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/58_CNN%20and%20Daily%20Mail%20News%20Stories/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Text summarization in news stories involves automatically condensing lengthy news articles into concise summaries, enabling readers to quickly grasp the key points and main ideas of the article. This technology utilizes natural language processing algorithms to identify important sentences and extract the most relevant information, providing users with a succinct overview of the news story..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Implementing text summarization in news stories can have a significant impact on the news industry. It enables news organizations to deliver information to readers more efficiently, saving their time and effort. With shorter and more digestible summaries, readers can quickly scan multiple articles and stay informed about various topics. Additionally, this technology can be integrated into news aggregators and personalized news apps, enhancing user experiences and attracting more engaged audiences. By automating the summarization process, news organizations can streamline their content production and dissemination, increasing their overall productivity and competitiveness..</p>

### DATASET
- Cnn and daily mail news stories dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/cnn_dailymail_text_sequence_to_sequence.zip).
- 4000 train, 4000 validation, and 4000 test texts with summaries..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/58_CNN%20and%20Daily%20Mail%20News%20Stories/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Summarize the News Stories.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: sshleifer/distilbart-cnn-12-6</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 4</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 2</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 1e-05</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/58_CNN%20and%20Daily%20Mail%20News%20Stories/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/58_CNN%20and%20Daily%20Mail%20News%20Stories/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    