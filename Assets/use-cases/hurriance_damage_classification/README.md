# HURRIANCE DAMAGE CLASSIFICATION
### AI for Good | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/11_Hurriance%20Damage%20Classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/11_Hurriance%20Damage%20Classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/11_Hurriance%20Damage%20Classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/11_Hurriance%20Damage%20Classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/11_Hurriance%20Damage%20Classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Hurricane Damage Classification model is used to assess the extent of damage caused by hurricanes on buildings and infrastructure. It helps emergency responders and insurance companies to prioritize their response and allocate resources efficiently. The model uses drone imagery and classify the level of damage into categories, providing a faster and more accurate assessment of the damage..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Hurricane damage classification has a significant business impact in the insurance industry. By accurately identifying and categorizing the extent of damage caused by hurricanes, insurance companies can efficiently assess claims, determine coverage eligibility, and expedite the claims process. This technology enables prompt and fair settlements, reduces fraudulent claims, and enhances customer satisfaction by streamlining the insurance workflow..</p>

### DATASET
- Hurriance damage classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/Hurriance_Damage_Classification.zip).
- 10000 train images , 2000 validation images, 2000 test images with labels is damage or not.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/11_Hurriance%20Damage%20Classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Automatically classify if a given region is likely to contain flooding damage or not.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/11_Hurriance%20Damage%20Classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/11_Hurriance%20Damage%20Classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Attribution 4.0 International (CC BY 4.0)</p>
    