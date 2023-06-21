# EMERGENCY VEHICLE SIREN SOUNDS DETECTION
### AI for good | Audio | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/88_emergency_vehicle_siren_sounds/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/88_emergency_vehicle_siren_sounds/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/88_emergency_vehicle_siren_sounds/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/88_emergency_vehicle_siren_sounds/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/88_emergency_vehicle_siren_sounds/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Emergency vehicle siren sounds detection involves the automated identification and classification of siren sounds emitted by emergency vehicles, such as police cars, ambulances, or fire trucks. This technology utilizes audio analysis and pattern recognition techniques to distinguish emergency vehicle sirens from background noise, enabling timely response and efficient traffic management.</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>The business impact of emergency vehicle siren sounds detection is vital in traffic management and emergency response systems. By automatically identifying and detecting emergency vehicle sirens from audio data, this technology enables efficient traffic routing, timely emergency response, and improved road safety. It optimizes emergency vehicle dispatching, reduces response times, and minimizes traffic congestion. It contributes to faster emergency assistance, enhances public safety, and supports effective urban planning..</p>

### DATASET
- Emergency_vehicle_siren_sounds dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/audio_classification/emergency-vehicle-siren-sounds.zip).
- 600 train audio samples with 3 different labels such as ambulance,traffic,firetruck..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/88_emergency_vehicle_siren_sounds/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Detect and classify emergency vehicle siren sounds from audio data using audio classification techniques for timely response and traffic management..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/88_emergency_vehicle_siren_sounds/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/88_emergency_vehicle_siren_sounds/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Other</p>
    