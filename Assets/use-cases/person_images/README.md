# PERSON RE-IDENTIFICATION
### Retail | Image | Metric Learning

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/61_Person%20Images/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/61_Person%20Images/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/61_Person%20Images/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/61_Person%20Images/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/61_Person%20Images/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Person Re-Identification is a computer vision task that involves identifying and tracking individuals across multiple non-overlapping camera views. The goal is to develop an algorithm or model that can match a person's identity across different surveillance cameras or video frames, regardless of changes in appearance, pose, lighting conditions, or camera angles. This use case finds applications in various domains such as law enforcement, public safety, retail analytics, and crowd management. By accurately re-identifying individuals, organizations can enhance security measures, detect suspicious activities, and gather valuable insights for business optimization or safety purposes. The person re-identification technology enables the tracking of individuals in real-time or post-event analysis, providing a powerful tool for video surveillance systems..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Person re-identification has significant business impacts across multiple industries. In the field of law enforcement and public safety, it enables authorities to track and monitor individuals of interest across different camera feeds, aiding in investigations and crime prevention. Retail businesses can leverage person re-identification for customer behavior analysis, footfall tracking, and targeted marketing strategies. By understanding customer movement patterns and preferences, retailers can optimize store layouts, personalize shopping experiences, and improve customer satisfaction. Crowd management at large events or transportation hubs can also benefit from person re-identification to monitor crowd flow, identify potential security risks, and ensure public safety. Overall, person re-identification technology enhances security, enables efficient video analysis, and provides valuable insights for decision-making across various industries..</p>

### DATASET
- Person images dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/market_1501_metric_learning.zip).
- 12936 train images of 751 humans. 534 test images..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/61_Person%20Images/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Identify the images of the same person from set of person images.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: tf_efficientnet_b0_ns</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 16</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 5</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/61_Person%20Images/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/61_Person%20Images/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    