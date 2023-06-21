# BOOK RATING TEXT REGRESSION
### Content creation | Text | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/75_book-rating-text-regression/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/75_book-rating-text-regression/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/75_book-rating-text-regression/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/75_book-rating-text-regression/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/75_book-rating-text-regression/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Book rating text regression encompasses the analysis and regression of textual reviews or feedback provided by readers for books. This technology aims to extract sentiment, opinion, and other relevant features from the text, enabling the prediction and estimation of book ratings, assisting readers in making informed choices and aiding authors and publishers in understanding readers' preferences..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Book rating text regression has a significant impact on the publishing industry and consumer decision-making. By analyzing textual reviews and extracting sentiment and opinion, this technology provides valuable insights into readers' preferences, book quality, and market trends. Publishers and authors can utilize this information to optimize book marketing strategies, refine content offerings, and improve overall reader satisfaction. It enables data-driven decision-making, boosts sales, and cultivates a loyal reader base..</p>

### DATASET
- Book-rating-text-regression dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/text_regression/book-rating-text-regression.csv).
- 10000 train rows with its label.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/75_book-rating-text-regression/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Predict the rating of books based on textual reviews using regression analysis on book rating text data..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/75_book-rating-text-regression/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/75_book-rating-text-regression/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC0: Public Domain</p>
    