# SIMILAR QUESTIONS GROUPING IN ASKUBUNTU
### Support forums | Text | Metric Learning

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/63_AskUbuntu%20Questions/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/63_AskUbuntu%20Questions/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/63_AskUbuntu%20Questions/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/63_AskUbuntu%20Questions/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/63_AskUbuntu%20Questions/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Similar Questions Grouping in AskUbuntu involves automatically identifying and clustering similar questions posted on the AskUbuntu platform, which is a question and answer community for Ubuntu users. The objective is to group questions that are semantically or topically similar, allowing users to find relevant information efficiently and reducing duplicate or redundant questions. By applying natural language processing and machine learning techniques, this use case aims to enhance the user experience, promote knowledge sharing, and streamline the community's question answering process. Grouping similar questions helps moderators and experienced users provide targeted answers, reduces the time and effort required to address common queries, and facilitates the accumulation of knowledge within the AskUbuntu community..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Implementing similar questions grouping in AskUbuntu can have several positive impacts on the community and its users. Firstly, it improves the user experience by making it easier to find relevant information and solutions to common problems. This enhances user satisfaction, encourages engagement, and fosters a sense of community among Ubuntu users. By reducing duplicate questions, moderators and experienced users can focus their efforts on providing quality answers to unique or less frequent inquiries, improving the overall effectiveness of the platform. Additionally, similar questions grouping promotes knowledge sharing and collaboration within the community, as users can explore related questions and expand their understanding of Ubuntu. Overall, this use case contributes to a more efficient and effective question answering process, leading to a stronger and more vibrant AskUbuntu community..</p>

### DATASET
- Askubuntu questions dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/ubuntu_text_metric_learning.zip).
- 3134 train texts from 422 groups. 756 test texts..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/63_AskUbuntu%20Questions/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Identify the similar questions from AskUbuntu.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: distilbert-base-uncased</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 16</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 5</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.0001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/63_AskUbuntu%20Questions/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/63_AskUbuntu%20Questions/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    