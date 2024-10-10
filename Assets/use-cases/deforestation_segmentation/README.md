## Use Case 101: Deforestation Segmentation

Segment deforested areas with multi-modal satellite imagery

- `Industry: AI4Good`
- `Problem Type: Image Segmentation`
- `Data Type: Image`

![](https://github.com/h2oai/ht-catalog/blob/78d74498d8534193d3208f31a38cc0aa936d3f86/Assets/use-cases/deforestation_segmentation/cover.png)
![](https://github.com/h2oai/ht-catalog/blob/78d74498d8534193d3208f31a38cc0aa936d3f86/Assets/use-cases/deforestation_segmentation/cover.jpg)
![](https://github.com/h2oai/ht-catalog/blob/78d74498d8534193d3208f31a38cc0aa936d3f86/Assets/use-cases/deforestation_segmentation/cover.jpeg)
![](https://github.com/h2oai/ht-catalog/blob/78d74498d8534193d3208f31a38cc0aa936d3f86/Assets/use-cases/deforestation_segmentation/cover.webp)
![](https://github.com/h2oai/ht-catalog/blob/78d74498d8534193d3208f31a38cc0aa936d3f86/Assets/use-cases/deforestation_segmentation/cover)

### Business Problem 

Deforestation estimation in the Amazon forest poses a significant challenge due to the vast size of the area and the limited accessibility for direct human observation. To effectively address this problem, multi-modal satellite imagery and remote sensing offer a promising solution for estimating deforestation. Our model achieves high precision deforestation estimation on unseen images from the region.

### Impact

The Amazon forest encompasses approximately 40% of the remaining rainforests in the world. Unfortunately, deforestation in the Amazon is reaching dangerous levels. In August 2022, deforestation in the Amazon was 1,661 km2, an amount 81% higher than that recorded in August last year. Multi-modal satellite imagery offer a powerful alternative for monitoring deforestation near real-time.

### Dataset

Dataset link - [s3://0xdata-public/beluga/wildfire/full_r6_image_semantic_segmentation.zip](https://0xdata-public.s3.amazonaws.com/beluga/wildfire/full_r6_image_semantic_segmentation.zip)

8866 train images and 1200 validation multi-modal images from various Sentinel-1, Sentinel-2, and Landsat-8 snapshots combined up to 152 channels. 

![train data](https://github.com/h2oai/ht-catalog/blob/78d74498d8534193d3208f31a38cc0aa936d3f86/Assets/use-cases/deforestation_segmentation/train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

### Model Training

Objective: Segment deforested areas with multi-modal satellite imagery

Model Configuration (Hydrogen Torch yaml)

```yaml

```

![chart](https://github.com/h2oai/ht-catalog/blob/78d74498d8534193d3208f31a38cc0aa936d3f86/Assets/use-cases/deforestation_segmentation/chart.png)


### Prediction

![Predictions](https://github.com/h2oai/ht-catalog/blob/78d74498d8534193d3208f31a38cc0aa936d3f86/Assets/use-cases/deforestation_segmentation/Validation%20Predictions.png)

### License

CC BY 4.0

### Acknowledgements

Original dataset source is https://sites.google.com/view/rainforest-challenge/multiearth-2023
