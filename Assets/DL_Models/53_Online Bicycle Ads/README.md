# SIMILAR IMAGES GROUPING IN BICYCLE ADS
### E-commerce | Image | Metric Learning

![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/53_Online%20Bicycle%20Ads/cover.png)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/53_Online%20Bicycle%20Ads/cover.jpg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/53_Online%20Bicycle%20Ads/cover.jpeg)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/53_Online%20Bicycle%20Ads/cover.webp)
![](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/53_Online%20Bicycle%20Ads/cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>The use case involves utilizing similar image grouping in bicycle ads. When advertising bicycles, it is essential to showcase a variety of models, features, and styles to attract potential customers. However, manually organizing and selecting images for ads can be time-consuming and challenging. By leveraging similar image grouping, an automated system can analyze the visual content of bicycle images and group them based on similarities in design, color, or style. This process helps streamline the ad creation process by providing a curated selection of images that can be easily incorporated into advertisements..</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>Implementing similar image grouping in bicycle ads can have several positive impacts on businesses. Firstly, it improves efficiency by reducing the time and effort required to manually sort and organize images for advertisements. This allows marketers to focus on other crucial tasks, leading to increased productivity. Secondly, by presenting visually coherent and appealing ads, businesses can enhance customer engagement and increase the likelihood of attracting potential buyers. This can result in higher conversion rates and improved sales for bicycle companies. Lastly, by automating the image grouping process, companies can reduce the chances of human error and inconsistencies in ad visuals, ensuring a more professional and polished advertising campaign..</p>

### DATASET
- Online bicycle ads dataset has been used.
- You can access the dataset [here](s3://h2oai-hydrogen-torch-internal/dev_datasets/bicycle_image_metric_learning.zip).
- 8313 images of 1148 online bicycle ads. Each ad has multiple images marked by their class ID..

![train data](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/53_Online%20Bicycle%20Ads/train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>Identify the Images of same bicycle within the same advertisement.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: tf_efficientnet_b0_ns</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: True</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: 16</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: 5</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: 0.0</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: 0.001</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: AdamW</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: Cosine</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: 0</p>

![chart](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/53_Online%20Bicycle%20Ads/chart.png)

### MODEL PREDICTIONS

![Validation Predictions](https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/DL_Models/53_Online%20Bicycle%20Ads/Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>nan</p>
    