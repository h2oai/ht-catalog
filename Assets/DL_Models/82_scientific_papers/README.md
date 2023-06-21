# SCIENTIFIC PAPERS NER
### AI for good | Text | Sequence to Sequence

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/82_scientific_papers/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/82_scientific_papers/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/82_scientific_papers/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/82_scientific_papers/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/82_scientific_papers/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Scientific papers NER (Named Entity Recognition) entails the identification and extraction of named entities such as names of researchers, organizations, chemicals, or biological entities from scientific articles and papers. This technology assists in organizing and indexing scientific literature, enabling efficient information retrieval and knowledge discovery in specific domains.</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Scientific papers NER has significant business implications in scientific research and knowledge management. By automatically extracting named entities from scientific articles and papers, this technology enhances information retrieval, literature review, and knowledge discovery. Researchers, academic institutions, and R&D departments can efficiently locate relevant literature, identify key authors or organizations, and establish collaborations. It fosters scientific progress, accelerates innovation, and supports evidence-based decision-making..</p>

### DATASET
- Scientific_papers dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/text_sequence_to_sequence/scientific papers.zip).
- 202914 train rows with their summaries.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/82_scientific_papers/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Extract and classify named entities from scientific papers using named entity recognition techniques for efficient organization and indexing of scientific literature..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/82_scientific_papers/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/82_scientific_papers/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Unknown</p>
    