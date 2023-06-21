# ASL ALPHABET CLASSIFICATION
### AI for Good | Image | Classification

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/31_ASL%20Alphabet%20Detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/31_ASL%20Alphabet%20Detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/31_ASL%20Alphabet%20Detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/31_ASL%20Alphabet%20Detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/31_ASL%20Alphabet%20Detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>The ASL Alphabet Detection model is designed to accurately recognize and classify the American Sign Language (ASL) alphabet letters from images. The model uses a convolutional neural network (CNN) architecture and is trained on a dataset of ASL alphabet images to learn the distinctive features of each letter. The model can be used to help individuals with hearing or speech impairments to communicate more effectively by accurately recognizing and interpreting their hand signs. Additionally, the model can be used in educational settings to teach ASL or in research for sign language recognition.</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>ASL (American Sign Language) alphabet detection has a significant impact on accessibility and communication for the deaf and hard of hearing community. By leveraging computer vision and deep learning techniques, it enables real-time detection and recognition of ASL hand gestures representing different alphabet letters. ASL alphabet detection technology enhances communication and inclusivity by providing a means for individuals to express themselves and interact with others effectively. It supports the development of applications and devices that facilitate seamless communication between ASL users and non-ASL users, promoting equal participation and bridging communication barriers..</p>

### DATASET
- Asl alphabet detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/image_classification/asl_alphabet_train.zip).
- 87000 train data with their 29 different labels (A-Z,del,nothing,space).

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/31_ASL%20Alphabet%20Detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Accurately recognize and classify the American Sign Language (ASL) alphabet letters from images..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/31_ASL%20Alphabet%20Detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/31_ASL%20Alphabet%20Detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>GPL 2</p>
    