# FIBER SEGMENTATION IN CONCRETE
### Manufacturing | Image | Segmentation

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/18_Fiber%20Segmentation/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/18_Fiber%20Segmentation/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/18_Fiber%20Segmentation/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/18_Fiber%20Segmentation/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/18_Fiber%20Segmentation/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>The Fiber Segmentation in concrete model aims to accurately identify and segment fibers in concrete images, which can be useful for various engineering and construction applications. By using deep learning techniques, the model can automatically detect and classify fibers, providing a more efficient and accurate solution than traditional manual methods. This can improve the quality of concrete structures and reduce the risk of failure, ultimately leading to safer and more durable infrastructure..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>The fiber segmentation in concrete has significant business impact in the construction and infrastructure industries. By accurately segmenting and analyzing the distribution of fibers in concrete, it is possible to assess the structural integrity and durability of concrete structures. This information helps in optimizing the design and composition of concrete mixtures, ensuring the desired mechanical properties and performance. Moreover, fiber segmentation assists in quality control during the construction process, enabling early detection of any inconsistencies or defects in the fiber reinforcement. This ultimately leads to improved construction practices, increased safety, and enhanced longevity of concrete structures..</p>

### DATASET
- Fiber segmentation dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_segmentation/fiber-augmented.zip).
- 7902 train images with their mask.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/18_Fiber%20Segmentation/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Accurately identify and segment fibers in concrete images.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/18_Fiber%20Segmentation/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/18_Fiber%20Segmentation/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Unknown</p>
    