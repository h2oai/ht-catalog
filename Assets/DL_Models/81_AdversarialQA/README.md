# ADVERSARIALQA
### Content creation | Text | Span Prediction

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/81_AdversarialQA/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/81_AdversarialQA/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/81_AdversarialQA/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/81_AdversarialQA/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/81_AdversarialQA/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>AdversarialQA (Question Answering) involves the development and testing of robust question-answering systems against adversarial attacks or attempts to manipulate the system. This technology aims to enhance the reliability and security of QA models by identifying vulnerabilities, improving their resistance to adversarial inputs, and ensuring accurate and trustworthy responses..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>The business impact of AdversarialQA lies in enhancing the reliability and security of question-answering systems. By identifying vulnerabilities and improving resistance to adversarial attacks, this technology strengthens trust in QA models and safeguards their integrity. It ensures accurate responses, reduces the risk of misinformation, and protects user confidence. Businesses can utilize robust QA systems to provide reliable information, enhance user experience, and differentiate themselves in competitive markets..</p>

### DATASET
- Adversarialqa dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/text_span_prediction/adversarialQA.zip).
- 30000 train rows with their details.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/81_AdversarialQA/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Develop and test robust question-answering systems against adversarial attacks using machine learning techniques for reliable and secure QA models..</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: deepset/xlm-roberta-base-squad2</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 16</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 2</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 1e-05</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/81_AdversarialQA/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/81_AdversarialQA/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>cc-by-sa-4.0</p>
    