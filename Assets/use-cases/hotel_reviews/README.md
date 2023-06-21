# HOTEL RECOMMENDATION BASED ON RATINGS
### E-commerce | Text | Regression

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/55_Hotel%20Reviews/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/55_Hotel%20Reviews/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/55_Hotel%20Reviews/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/55_Hotel%20Reviews/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/55_Hotel%20Reviews/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>The use case involves recommending hotels based on ratings. Users can provide their preferences, such as destination, budget, and desired amenities, and the system will generate hotel recommendations based on the ratings received from previous guests. The ratings reflect the overall satisfaction and quality of service offered by the hotels. By considering these ratings, the system aims to provide users with reliable and trustworthy recommendations that align with their preferences, ensuring a positive hotel experience..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Implementing a hotel recommendation system based on ratings can have a significant impact on the hospitality industry. It enhances customer satisfaction by guiding them towards hotels that have consistently received high ratings from previous guests. This improves the overall quality of service provided, leading to positive guest experiences, increased customer loyalty, and improved customer reviews. Moreover, it enables hotels to differentiate themselves based on their ratings, attracting more potential guests and increasing their occupancy rates. The system also benefits travel agencies and online platforms by providing them with a valuable tool to enhance their user experience and generate higher customer engagement.
.</p>

### DATASET
- Hotel reviews dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/hotel_recommendation_text_regression.csv).
- 50000 train texts with 6 labels. Each label has value between 1 to 5..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/55_Hotel%20Reviews/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Rate the quality of 6 differnet facilities of the hotels using the reviews.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/55_Hotel%20Reviews/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/55_Hotel%20Reviews/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    