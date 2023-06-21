# READABILITY SCORING FOR TEXTS
### Content creation | Text | Regression

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/59_Texts%20with%20Readability%20Scores/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/59_Texts%20with%20Readability%20Scores/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/59_Texts%20with%20Readability%20Scores/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/59_Texts%20with%20Readability%20Scores/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/59_Texts%20with%20Readability%20Scores/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>The Readability Scoring for Texts use case involves developing an algorithm or tool that can assess the readability level of a given text. It aims to provide a numerical score or categorization indicating the difficulty of comprehending the text. This tool can be useful in various domains, such as education, publishing, content creation, and language learning, to evaluate and enhance the readability of written material..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>The Readability Scoring tool can have a significant impact on industries that heavily rely on written communication. In education, it can assist teachers in selecting appropriate reading materials for students based on their reading abilities. Publishers can utilize this tool to assess the readability of their content and make necessary modifications to cater to their target audience. Content creators can optimize their writing styles to ensure clarity and accessibility. Language learning platforms can integrate this tool to provide tailored reading materials for learners at different proficiency levels..</p>

### DATASET
- Texts with readability scores dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/commonlit_readability_text_regression.zip).
- 2834 train texts with readability scores..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/59_Texts%20with%20Readability%20Scores/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Calculate the readability scores of the Texts.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: roberta-base</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 12</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 6</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 1e-05</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/59_Texts%20with%20Readability%20Scores/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/59_Texts%20with%20Readability%20Scores/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    