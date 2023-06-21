# MALARIA CELL DETECTION
### Healthcare | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/99_Malaria_cell_detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/99_Malaria_cell_detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/99_Malaria_cell_detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/99_Malaria_cell_detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/99_Malaria_cell_detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'> Malaria cell detection involves the automated identification and detection of malaria-infected red blood cells in microscopic images. This technology utilizes image analysis algorithms and machine learning models to analyze and classify red blood cells as either infected or uninfected, aiding in the diagnosis and monitoring of malaria..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Malaria cell detection has significant business implications in the healthcare and medical diagnostics industry. By automating the detection of malaria-infected cells, healthcare providers can improve the efficiency and accuracy of malaria diagnosis, enabling timely treatment interventions. It aids in epidemiological studies, supports public health initiatives, and contributes to the overall management and control of malaria. It also helps researchers and pharmaceutical companies in developing new antimalarial drugs and vaccines.</p>

### DATASET
- Malaria_cell_detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/Malaria_cell_detection.zip).
- 27558 train images with their labels.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/99_Malaria_cell_detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>The prediction target for malaria cell detection is to accurately identify and classify red blood cells as infected or uninfected with malaria parasites, enabling early detection and effective treatment of the disease..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/99_Malaria_cell_detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/99_Malaria_cell_detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Unknown</p>
    