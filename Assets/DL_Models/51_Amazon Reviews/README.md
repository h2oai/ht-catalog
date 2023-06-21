# AMAZON REVIEWS TEXT CLASSIFICATION
### E-commerce | Text | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/51_Amazon%20Reviews/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/51_Amazon%20Reviews/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/51_Amazon%20Reviews/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/51_Amazon%20Reviews/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/51_Amazon%20Reviews/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>The Amazon Reviews Text Classification use case involves classifying customer reviews of products on the Amazon platform into different categories based on the sentiments expressed in the text. Sentiment analysis is performed on the textual data to determine whether a review is positive or negative. This classification enables businesses to gain insights into customer opinions, identify areas for improvement, and make data-driven decisions to enhance customer satisfaction..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>The Amazon Reviews Text Classification use case has a significant business impact. By accurately classifying customer reviews, businesses can gain valuable insights into customer opinions, preferences, and satisfaction levels. This enables them to make informed decisions to enhance products, address customer concerns, and manage their online reputation effectively. The classification helps identify areas for improvement, optimize marketing and sales strategies, and leverage positive reviews for brand promotion. By automating the review classification process, businesses can save time and resources while extracting actionable insights that drive customer-centric improvements, leading to increased customer satisfaction, loyalty, and ultimately, business growth..</p>

### DATASET
- Amazon reviews dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/amazon_reviews_text_classification.csv).
- 48093 train texts with their labels Positive or Negative.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/51_Amazon%20Reviews/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Classify the Amazon Reviews using Text Classification Techniques.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: roberta-large</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 12</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 4</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 1e-05</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/51_Amazon%20Reviews/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/51_Amazon%20Reviews/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    