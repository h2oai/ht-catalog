# COMMANDS_SPEECH_RECOGNITION
### AI for good | Speech/Audio | Recognition

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/66_commands_speech_recognition/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/66_commands_speech_recognition/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/66_commands_speech_recognition/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/66_commands_speech_recognition/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/66_commands_speech_recognition/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Commands speech recognition involves developing a system that can accurately understand and interpret spoken commands or instructions given by users. This technology enables hands-free control and interaction with various devices, such as smartphones, smart home assistants, and vehicles. By converting speech into actionable commands, it enhances user experience and convenience..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Implementing commands speech recognition has significant business implications across industries. It enables seamless voice control, improving accessibility and user engagement. In the automotive industry, it enhances driver safety by allowing hands-free operation of in-car systems. In the consumer electronics sector, it enables voice-activated control of devices, enhancing user convenience and satisfaction. In healthcare, it simplifies interactions with medical equipment, improving efficiency and reducing errors. Overall, commands speech recognition technology can revolutionize human-computer interaction, making devices and systems more user-friendly and intuitive..</p>

### DATASET
- Commands_speech_recognition dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/commands_speech_recognition.zip).
- 6798 train audio samples with their transcript..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/66_commands_speech_recognition/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Accurately transcribing and understanding spoken commands, converting them into actionable instructions..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/66_commands_speech_recognition/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/66_commands_speech_recognition/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    