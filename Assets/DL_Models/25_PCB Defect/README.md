# PCB DEFECT OBJECT DETECTION
### Manufacturing  | Image | Object Detection

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/25_PCB%20Defect/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/25_PCB%20Defect/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/25_PCB%20Defect/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/25_PCB%20Defect/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/25_PCB%20Defect/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>The PCB Defect model was created using a public synthetic dataset containing 1386 images with 6 different types of defects found in printed circuit boards (PCBs). The aim of this model is to accurately detect and classify these defects, which include missing holes, mouse bites, open circuits, shorts, spurs, and spurious copper. The model was trained using deep learning algorithms and image processing techniques to identify the specific characteristics of each defect type and classify them accordingly. The model is designed to aid in quality control and product analysis in the electronics industry, ensuring that PCBs meet high standards and are free from defects that could affect their performance..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>PCB (Printed Circuit Board) defect detection is crucial in the electronics manufacturing industry. By employing advanced computer vision techniques, it enables the automated identification of defects in PCBs, such as short circuits, open circuits, or component misalignment. Timely detection of such defects during the production process ensures the delivery of reliable and high-quality electronic devices. PCB defect detection technology reduces production costs by minimizing the need for manual inspection and rework. It enhances manufacturing efficiency, speeds up the production cycle, and reduces the risk of faulty electronic products reaching the market. Overall, PCB defect detection improves product quality, customer satisfaction, and business competitiveness in the electronics industry..</p>

### DATASET
- Pcb defect dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/object_detection/pcb_defect.zip).
- 1500 images with their object labels ['open' 'short' 'mousebite' 'spur' 'copper' 'pin-hole'] .

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/25_PCB%20Defect/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Accurately detect and classify the defects, .</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: tf_efficientdet_d0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 16</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 5</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0.0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/25_PCB%20Defect/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/25_PCB%20Defect/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>MIT License</p>
    