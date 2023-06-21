# BRAIN MRI SEGMENTATION
### Healthcare | Image | Segmentation

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/27_Brain%20MRI%20Segmentation/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/27_Brain%20MRI%20Segmentation/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/27_Brain%20MRI%20Segmentation/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/27_Brain%20MRI%20Segmentation/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/27_Brain%20MRI%20Segmentation/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>The Brain MRI Segmentation model is designed to accurately segment FLAIR abnormality regions in brain MR images. With the help of the brain MRI dataset, which contains images of lower-grade glioma patients with manual segmentation masks, the model can identify and isolate regions of abnormality in the brain. The model can be used as a tool for assisting medical professionals in diagnosing and treating brain tumors, improving patient outcomes and quality of life..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Brain MRI segmentation plays a crucial role in the healthcare industry, specifically in the field of neurology. By utilizing advanced image processing techniques and deep learning algorithms, it enables accurate delineation and identification of different brain structures and abnormalities. Precise brain MRI segmentation aids in the diagnosis and treatment planning for various neurological conditions, including tumors, strokes, or degenerative diseases. It facilitates better understanding of brain anatomy, enhances clinical decision-making, and improves patient outcomes. Brain MRI segmentation technology improves medical imaging workflows, reduces interpretation time, and promotes efficient healthcare delivery..</p>

### DATASET
- Brain mri segmentation dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_segmentation/lgg-mri-segmentation_v1.zip).
- 1373 train images with it's segmentation mask.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/27_Brain%20MRI%20Segmentation/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Segment FLAIR abnormality regions in brain MR images.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/27_Brain%20MRI%20Segmentation/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/27_Brain%20MRI%20Segmentation/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>CC BY-NC-SA 4.1</p>
    