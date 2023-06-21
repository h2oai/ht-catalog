# BUILDING SEGMENTATION IN IMAGES
### AI for Good | Image | Object Detection

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/10_Satellite%20imagery%20-%20(Map%20Challenge)/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/10_Satellite%20imagery%20-%20(Map%20Challenge)/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/10_Satellite%20imagery%20-%20(Map%20Challenge)/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/10_Satellite%20imagery%20-%20(Map%20Challenge)/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/10_Satellite%20imagery%20-%20(Map%20Challenge)/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>The Building Segmentation in Satellite Images model uses image segmentation techniques to accurately identify and delineate buildings in satellite imagery. The model can be trained on large datasets of satellite images with labeled building boundaries to learn to recognize building features such as roofs, walls, and windows. Once trained, the model can quickly and accurately segment buildings in new satellite images, making it a valuable tool for applications such as urban planning, disaster response, and environmental monitoring. By automating the process of building segmentation, this model can save time and resources compared to traditional manual method.</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Building segmentation in images has significant implications in the fields of architecture, real estate, and urban planning. By automatically segmenting buildings in images, this technology assists in architectural design and visualization, allowing architects and designers to create accurate 3D models and renderings. Real estate professionals can leverage building segmentation to identify property boundaries, evaluate property features, and enhance marketing materials. Urban planners can utilize this technology to analyze building density, monitor urban growth, and make informed decisions regarding zoning and land use. Building segmentation contributes to more efficient urban development and improved decision-making processes in the built environment..</p>

### DATASET
- Satellite imagery - (map challenge) dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/object_detection/mapping_challenge_v2.zip).
- 8366 train images with their object coordinates.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/10_Satellite%20imagery%20-%20(Map%20Challenge)/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Segmenting Buildings in Satellite Images.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: tf_efficientdet_d0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 12</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 8</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/10_Satellite%20imagery%20-%20(Map%20Challenge)/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/10_Satellite%20imagery%20-%20(Map%20Challenge)/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Unknown</p>
    