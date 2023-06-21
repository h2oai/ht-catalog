# SQL CREATE CONTEXT
### Content creation | Text | Span Prediction

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/80_sql_create_context/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/80_sql_create_context/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/80_sql_create_context/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/80_sql_create_context/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/80_sql_create_context/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>SQL create context refers to the process of dynamically generating SQL queries or statements based on contextual information or user requirements. This technology allows for the flexible creation and customization of SQL commands, enabling efficient database management, data retrieval, and system integration.</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>SQL create context has important business implications for database management and software development. By dynamically generating SQL queries based on contextual information or user requirements, this technology enhances the flexibility and adaptability of database systems. It facilitates efficient data retrieval, streamlines application development, and enables seamless integration with external systems. It empowers businesses to leverage data-driven insights, improve decision-making processes, and optimize operational efficiency.</p>

### DATASET
- Sql_create_context dataset has been used.
- You can access the dataset [here](s3://apac-cds/ht_datasets/text_span_prediction/sql-create-context.csv).
- 202914 train rows with their details.

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/80_sql_create_context/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Automatically generate SQL queries or statements based on contextual information or user requirements for efficient database management and data retrieval..</p>

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

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/80_sql_create_context/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/80_sql_create_context/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>cc-by-4.0</p>
    