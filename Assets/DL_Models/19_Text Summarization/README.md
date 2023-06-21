# TEXT SUMMARIZATION
### Content Creation  | Text | Text sequence to sequence

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/19_Text%20Summarization/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/19_Text%20Summarization/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/19_Text%20Summarization/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/19_Text%20Summarization/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/19_Text%20Summarization/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Text summarization is a natural language processing technique used to automatically generate a concise and coherent summary of a text. The need for text summarization model  arises when we need to quickly comprehend a large amount of text data. It is particularly useful for news articles, research papers, and legal documents, where the reader needs to quickly grasp the main points without having to read the entire document.</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Text summarization has a wide range of business applications, particularly in industries dealing with large volumes of textual information, such as news media, market research, and legal services. By automatically generating concise and coherent summaries from lengthy documents, text summarization improves information retrieval and comprehension. It allows users to quickly grasp the main points, key insights, and relevant details without having to read the entire text. This significantly enhances productivity, decision-making, and knowledge management. In news media, text summarization enables efficient content curation, aiding in the delivery of timely and relevant news to audiences. In legal services, it assists in digesting complex legal documents, conducting legal research, and preparing case summaries, saving valuable time and resources..</p>

### DATASET
- Text summarization dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/text_sequence_to_sequence/text_summarization.zip).
- 500 text documents with their summarization.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/19_Text%20Summarization/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Automatically generate a concise summary of a longer text.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: sshleifer/distilbart-cnn-12-6</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 4</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 10</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 1e-05</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/19_Text%20Summarization/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/19_Text%20Summarization/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Attribution-NonCommercial-ShareAlike 3.0 IGO (CC BY-NC-SA 3.0 IGO)</p>
    