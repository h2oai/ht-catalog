# GERMINATION SEEDLING DETECTION
### Agriculture | Image | Object Detection

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/44_Germination%20Seedling%20Detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/44_Germination%20Seedling%20Detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/44_Germination%20Seedling%20Detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/44_Germination%20Seedling%20Detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/44_Germination%20Seedling%20Detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Germination Seedling Detection is a computer vision model that is designed to detect and classify seedlings at different stages of growth. This model uses image processing techniques to analyze images of seedlings and classify them based on their growth stage. The model can be used in a variety of applications, such as monitoring crop growth, identifying plant diseases, and optimizing plant growth conditions. By accurately detecting and classifying seedlings, the model can help farmers and plant researchers make informed decisions about planting, harvesting, and plant management..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Germination seedling detection has applications in agriculture and plant science. By analyzing images or videos of seedlings, it enables the automated detection and tracking of germinating seeds and early-stage plant growth. Accurate germination seedling detection assists in monitoring crop development, optimizing planting techniques, and assessing seed quality. It facilitates early identification of plant diseases, nutrient deficiencies, or environmental stressors, enabling timely intervention and improved crop yield. Germination seedling detection technology supports precision agriculture, crop management, and sustainable farming practices, contributing to increased productivity and food security..</p>

### DATASET
- Germination seedling detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/object_detection/germination-seeing-detection.zip).
- 451 train images with their object coordinates.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/44_Germination%20Seedling%20Detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Detect Seedlings to assess quality of germination process.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: tf_efficientdet_d0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 16</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 5</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/44_Germination%20Seedling%20Detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/44_Germination%20Seedling%20Detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC BY-NC-SA 4.0</p>
    