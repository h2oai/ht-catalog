# NERVES SEGMENTATION IN ULTRASOUND IMAGES
### Healthcare | Image | Semantic Segmentation

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/70_Ultrasound%20Images%20of%20Brachial%20Plexus/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/70_Ultrasound%20Images%20of%20Brachial%20Plexus/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/70_Ultrasound%20Images%20of%20Brachial%20Plexus/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/70_Ultrasound%20Images%20of%20Brachial%20Plexus/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/70_Ultrasound%20Images%20of%20Brachial%20Plexus/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Nerves segmentation in ultrasound images involves the automated identification and segmentation of nerve structures in ultrasound scans. This technology aids in medical imaging and diagnostic procedures by enabling precise nerve localization, analysis, and evaluation.</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Nerves segmentation in ultrasound images has significant business implications in the healthcare industry. It improves the accuracy and efficiency of nerve-related diagnostics, such as identifying nerve damage, guiding nerve blocks, and assisting in surgical procedures. This technology enhances the detection and monitoring of nerve-related conditions, such as neuropathies and nerve entrapments, facilitating early intervention and appropriate treatment planning. It also contributes to research and development in neurology and enables advancements in nerve-related therapies and interventions. Overall, nerves segmentation in ultrasound images enhances the quality of nerve-related medical imaging and diagnosis, leading to improved patient care and outcomes..</p>

### DATASET
- Ultrasound images of brachial plexus dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/nerves_image_semantic_segmentation.zip).
- 2323 train images with their masks..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/70_Ultrasound%20Images%20of%20Brachial%20Plexus/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Segment a Collection of Nerves in Ultrasound Images.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/70_Ultrasound%20Images%20of%20Brachial%20Plexus/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/70_Ultrasound%20Images%20of%20Brachial%20Plexus/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    