# RESISTOR IMAGE CLASSIFICATION
### Manufacturing | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/93_resistor_image_classification/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/93_resistor_image_classification/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/93_resistor_image_classification/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/93_resistor_image_classification/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/93_resistor_image_classification/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Resistor image classification involves the automated recognition and categorization of different types of resistors based on their visual characteristics and markings. This technology utilizes computer vision techniques and machine learning algorithms to analyze resistor images and assign them to specific classes or categories..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Resistor image classification has significant business implications in the electronics manufacturing and distribution industry. By automating the classification process, it streamlines quality control, inventory management, and product identification. Electronic component manufacturers can ensure accurate labeling and sorting of resistors, reducing errors and improving operational efficiency. Distributors can optimize inventory tracking and fulfillment, ensuring the right resistors are supplied to customers, thereby enhancing customer satisfaction and reducing returns or errors in orders..</p>

### DATASET
- Resistor_image_classification dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/Resistor.zip).
- 2881 train images with 37 different categories.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/93_resistor_image_classification/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>accurately classify an input resistor image into its corresponding type or category, such as carbon film resistors, metal film resistors, or surface mount resistors..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/93_resistor_image_classification/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/93_resistor_image_classification/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Open Data Commons Open Database License (ODbL) v1.0</p>
    