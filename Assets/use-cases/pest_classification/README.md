# PEST SPECIES CLASSIFICATION
### Agriculture | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/17_Pest_classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/17_Pest_classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/17_Pest_classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/17_Pest_classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/17_Pest_classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>The Pest Classification model is used to identify and classify different types of pests. This can help in pest management by accurately identifying the pests and taking appropriate measures to control or prevent their infestation. The model is trained on a dataset of images of various pests and can accurately classify new images of pests with high accuracy..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Pest species classification plays a crucial role in industries such as agriculture, forestry, and pest control. Accurately identifying and classifying pest species helps in implementing effective pest management strategies. By identifying the specific pests infesting crops, forests, or buildings, appropriate measures can be taken to prevent damage and reduce economic losses. Pest species classification also aids in determining the most suitable and targeted methods for pest control, such as the use of specific pesticides or biological agents. This enables more efficient and sustainable pest management practices, ensuring the protection of crops, natural resources, and infrastructure..</p>

### DATASET
- Pest_classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/pest_classification.zip).
- 55865 train images with 132 pest species.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/17_Pest_classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Accurately classify the pest species.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: resnet50</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 32</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 5</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/17_Pest_classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/17_Pest_classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Unknown</p>
    