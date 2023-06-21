# STAMP DETECTION IN DOCUMENTS
### Banking | Image | Segmentation

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/30_Stamp%20Detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/30_Stamp%20Detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/30_Stamp%20Detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/30_Stamp%20Detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/30_Stamp%20Detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Stamp detection model is designed to detect stamps from images using computer vision techniques. With the help of stamp datasets containing images of different stamps, the model can accurately identify and localize the stamps in the input image. The model can be used for various applications, such as stamp authentication and sorting, postal services, and philately. It employs object detection algorithms, including convolutional neural networks and feature extraction methods to recognize and segment the stamps from the background..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>A stamp detection model offers several valuable benefits to businesses. It automates the process of identifying stamps in documents or images, improving efficiency and accuracy while saving time and costs. It helps prevent fraud by detecting forged or counterfeit stamps, ensuring compliance with regulations. Additionally, it enhances customer experience in industries like postal services by facilitating faster processing. Overall, a stamp detection model provides businesses with increased efficiency, cost savings, fraud prevention, regulatory compliance, and improved customer experience, leading to improved operational effectiveness and a competitive edge..</p>

### DATASET
- Stamp detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_segmentation/stamp_detection.zip).
- 400 images with their coordinates.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/30_Stamp%20Detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Detect Stamps in Documents using Object Detection Techniques.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: resnet101</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 16</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 5</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/30_Stamp%20Detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/30_Stamp%20Detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Unknown</p>
    