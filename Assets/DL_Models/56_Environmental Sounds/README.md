# ENVIRONMENTAL SOUND CLASSIFICATION
### AI for good | Audio | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/56_Environmental%20Sounds/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/56_Environmental%20Sounds/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/56_Environmental%20Sounds/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/56_Environmental%20Sounds/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/56_Environmental%20Sounds/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Environmental sound classification involves the categorization and identification of different types of sounds present in the environment, such as sirens, car horns, birdsong, and machinery noise. This technology utilizes machine learning algorithms to analyze audio data and assign relevant labels to the sounds. The aim is to develop a system that can automatically recognize and classify environmental sounds in real-time, enabling various applications in areas such as soundscape analysis, urban planning, wildlife monitoring, and noise pollution management..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Environmental sound classification has significant implications across industries. In urban planning, it helps identify noise hotspots and optimize city infrastructure for noise reduction. Industries like transportation and manufacturing can use it to detect and mitigate noise pollution. Environmental agencies can benefit from soundscape analysis for wildlife conservation and habitat monitoring. The technology also aids in improving public safety by alerting emergency services to specific sounds like explosions or gunfire. Overall, environmental sound classification empowers organizations to make data-driven decisions for sustainable development and enhances the quality of life for individuals in urban environments..</p>

### DATASET
- Environmental sounds dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/esc10_audio_classification.zip).
- 5-second-long 400 audio recordings organized into ten classes..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/56_Environmental%20Sounds/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Classify the Environmental Sounds using Audio Classification Techniques.</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/56_Environmental%20Sounds/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/56_Environmental%20Sounds/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    