# UNDERWATER STARFISH OBJECT DETECTION
### AI for Good | Image | Object Detection

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/5_Underwater%20Starfish%20Detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/5_Underwater%20Starfish%20Detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/5_Underwater%20Starfish%20Detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/5_Underwater%20Starfish%20Detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/5_Underwater%20Starfish%20Detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Underwater Starfish Detection model can accurately detect and classify starfish in underwater images. This model is useful for marine biologists and environmental scientists, helping them to monitor and protect underwater ecosystems..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Underwater starfish object detection offers valuable business impact. In marine biology and ecological research, accurate detection of starfish species aids in population monitoring, habitat conservation, and understanding ecosystem dynamics. For underwater exploration and mapping, starfish object detection contributes to mapping marine biodiversity, assisting in underwater surveys and conservation efforts. Fisheries management benefits from starfish detection by providing insights into the interactions between starfish and fish populations, informing sustainable fishing practices. Moreover, in the tourism and diving industry, underwater starfish object detection enhances the experience for divers and snorkelers, allowing them to observe and appreciate marine life more effectively. Overall, underwater starfish object detection has implications for ecological research, conservation, fisheries management, and marine tourism..</p>

### DATASET
- Underwater starfish detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/object_detection/cots_detection.zip).
- 429 images with their object coordinates.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/5_Underwater%20Starfish%20Detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Detect the starfish using object detection techniques.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/5_Underwater%20Starfish%20Detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/5_Underwater%20Starfish%20Detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC0: Public Domain</p>
    