# INSURANCE HOLDER DETECTION
### E-commerce | Text | Span Prediction

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/84_insurance_holder_detection/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/84_insurance_holder_detection/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/84_insurance_holder_detection/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/84_insurance_holder_detection/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/84_insurance_holder_detection/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>Insurance holder detection refers to the automated identification and verification of individuals who hold insurance policies or claims. This technology utilizes various data sources and machine learning algorithms to match and associate relevant information, assisting insurance providers in accurately identifying policyholders, preventing fraud, and ensuring efficient claims processing..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>The business impact of insurance holder detection is significant for insurance providers and fraud prevention. By accurately identifying and verifying insurance policyholders, this technology helps mitigate fraud risks and ensures accurate claims processing. It enables insurance companies to streamline operations, reduce losses, and enhance underwriting accuracy. By maintaining the integrity of their policies and safeguarding against fraudulent activities, insurance providers can build trust with customers, strengthen their reputation, and improve overall business performance..</p>

### DATASET
- Insurance_holder_detection dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/text_span_prediction/insurance_holder_detection.zip).
- 7632 train rows with their answers..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/84_insurance_holder_detection/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Determine and classify individuals holding insurance policies or claims using text classification techniques for accurate identification and fraud prevention..</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: distilbert-base-cased-distilled-squad</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 16</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 2</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 1e-05</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/84_insurance_holder_detection/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/84_insurance_holder_detection/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>Unknown</p>
    