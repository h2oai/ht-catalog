# PROTESTS RELATED TEXTS IDENTIFICATION
### Media | Text | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/62_Protests%20Related%20Texts/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/62_Protests%20Related%20Texts/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/62_Protests%20Related%20Texts/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/62_Protests%20Related%20Texts/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/62_Protests%20Related%20Texts/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Protests Related Texts Identification involves automatically identifying and categorizing text data related to protests or demonstrations. With the rise of social and political activism, there is a growing need to analyze and understand the sentiment, topics, and underlying messages expressed during protests. This use case is relevant for media organizations, social listening platforms, and government agencies to track public sentiment, assess social movements, and monitor potential risks or unrest. By automatically identifying and analyzing protest-related texts, organizations can gain insights into public opinions, identify emerging trends, and detect misinformation or propaganda. This information can be used for various purposes, such as informing media coverage, policy-making, crisis management, or public opinion research..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>The identification and analysis of protest-related texts can have significant business impacts in different industries. Media organizations can use this information to provide more comprehensive coverage of social movements, understand public sentiment, and align their reporting with current events. Social listening platforms can offer real-time monitoring and analysis of protests, helping businesses understand the impact of social issues on their brand reputation and customer sentiment. Government agencies can utilize protest-related text identification to track public sentiment, assess the effectiveness of policies, and identify potential risks or areas of concern. This can aid in decision-making, crisis response, and public engagement. Overall, protest-related text identification enables organizations to stay informed, make data-driven decisions, and effectively respond to societal changes..</p>

### DATASET
- Protests related texts dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/protests.zip).
- 21020 train and 5204 test texts with one label. The label has value either 0 or 1..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/62_Protests%20Related%20Texts/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Identify the Protests Related Texts.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/62_Protests%20Related%20Texts/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/62_Protests%20Related%20Texts/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    