# TRANSCRIPT GENERATION FOR US-EN SPEECHES
### Media | Speech/Audio | Recognition

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/68_Phone%20Banking%20Speech%20Samples/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/68_Phone%20Banking%20Speech%20Samples/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/68_Phone%20Banking%20Speech%20Samples/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/68_Phone%20Banking%20Speech%20Samples/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/68_Phone%20Banking%20Speech%20Samples/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Transcript generation for US-EN speeches involves automatically converting spoken content from US-English speeches or audio recordings into written transcripts. This technology aids in transcribing large volumes of audio data efficiently and accurately, enabling easy access to spoken information in text format..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Transcript generation for US-EN speeches has significant business implications in various domains. In media and entertainment, it enables the creation of closed captions for videos and enhances accessibility for individuals with hearing impairments. In education, it facilitates the transcription of lectures, making them searchable and enabling easy note-taking for students. In market research, it streamlines the analysis of recorded interviews or focus group discussions. It also finds applications in legal and compliance sectors for transcribing audio recordings of proceedings and interviews. Overall, transcript generation for US-EN speeches improves productivity, accessibility, and information retrieval from spoken content..</p>

### DATASET
- Phone banking speech samples dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/minds14_US_speech_recognition.zip).
- 558 train audio samples with their transcript..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/68_Phone%20Banking%20Speech%20Samples/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Generate Transcript for US English Speech Samples.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: openai/whisper-base.en</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 1</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 3</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 1e-05</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/68_Phone%20Banking%20Speech%20Samples/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/68_Phone%20Banking%20Speech%20Samples/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    