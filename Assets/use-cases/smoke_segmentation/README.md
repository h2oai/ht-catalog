# SMOKE SEGMENTATION IN IMAGES
### AI for Good | Image | Segmentation

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/3_Smoke%20Segmentation/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/3_Smoke%20Segmentation/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/3_Smoke%20Segmentation/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/3_Smoke%20Segmentation/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/3_Smoke%20Segmentation/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>This model can accurately identify and segment smoke in images. By distinguishing smoke from other objects and backgrounds, our model helps to improve the accuracy of fire detection systems and enhance safety in various industries, including manufacturing, transportation, and public safety..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Smoke segmentation in images has a profound impact across industries. In the field of fire prevention and safety, accurate smoke segmentation enables early detection and response, enhancing emergency management and minimizing property damage. In industrial settings, smoke segmentation helps monitor the presence of smoke, improving workplace safety and preventing accidents. Environmental agencies benefit from smoke segmentation in the detection and monitoring of wildfires, aiding in timely intervention and minimizing ecological damage. Furthermore, in the field of computer vision and image analysis, smoke segmentation contributes to various applications, including surveillance, image understanding, and object recognition..</p>

### DATASET
- Smoke segmentation dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/instance_segmentation/bush_fire_image_segment.zip).
- 64 train images segmented using class_id 'smoke'.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/3_Smoke%20Segmentation/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Segment the presence and location of smoke within images.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: resnet34</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 16</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 5</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/3_Smoke%20Segmentation/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/3_Smoke%20Segmentation/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>These datasets are free to use, but if you intend to use them in scientific research, it is necessary to reference this webpage and the Center for Wildfire Research.</p>
    