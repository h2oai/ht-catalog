# CROWD COUNTING IN PUBLIC
### AI for Good | Image | Regression

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/29_Crowd%20Counting/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/29_Crowd%20Counting/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/29_Crowd%20Counting/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/29_Crowd%20Counting/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/29_Crowd%20Counting/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Crowd counting model is designed to estimate the number of people in a given area or image using computer vision techniques. It is commonly used in various applications such as public safety, crowd management, and event planning. .</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Crowd counting technology has widespread applications in various industries, including retail, transportation, and event management. By utilizing computer vision techniques, it enables accurate estimation of crowd sizes in different environments. Crowd counting helps businesses optimize resource allocation, enhance crowd management strategies, and improve overall operational efficiency. It aids in ensuring crowd safety, optimizing staffing levels, and streamlining customer experiences. Crowd counting also provides valuable insights for urban planning, public safety, and marketing strategies, making it a valuable tool for decision-making and business growth..</p>

### DATASET
- Crowd counting dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_regression/crowd_counting.zip).
- 2000 images with their value.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/29_Crowd%20Counting/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Estimate the number of people in a given area.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/29_Crowd%20Counting/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/29_Crowd%20Counting/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Unknown</p>
    