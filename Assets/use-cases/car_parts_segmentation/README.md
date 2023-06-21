# CAR PARTS SEGMENTATION IN IMAGES
### E-commerce | Image | Semantic Segmentation

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/54_Car%20Parts%20Segmentation/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/54_Car%20Parts%20Segmentation/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/54_Car%20Parts%20Segmentation/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/54_Car%20Parts%20Segmentation/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/54_Car%20Parts%20Segmentation/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Car parts segmentation in images involves the task of identifying and delineating different components of a car in images, such as doors, windows, wheels, and bumpers. This is accomplished by applying computer vision techniques and machine learning algorithms to analyze and segment the relevant regions of the car parts. The goal is to accurately detect and segment these parts, enabling various applications in automotive industries, including autonomous driving, vehicle maintenance, and car design..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Accurate car parts segmentation in images has significant implications for the automotive industry. It enables advanced driver assistance systems (ADAS) and autonomous vehicles to better perceive their surroundings, leading to improved safety and reliability. Furthermore, in vehicle maintenance and repair, precise part segmentation can assist technicians in diagnosing and fixing issues efficiently. Additionally, car manufacturers and designers can leverage this technology to streamline the prototyping and design processes, allowing for faster iterations and reducing development costs..</p>

### DATASET
- Car parts segmentation dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/car_parts_coco_format_image_semantic_segmentation.zip).
- 400 train images with their masks..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/54_Car%20Parts%20Segmentation/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Segment the Parts of the Cars in images which contain a car or multiple cars.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/54_Car%20Parts%20Segmentation/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/54_Car%20Parts%20Segmentation/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    