# Melanoma_Classification

## Repository to reproduce the results on SIM-ISIC Competition 2020 Dataset hosted on kaggle competitions

Steps performed:
  1. Image Preprocessing:
      * Hair Artifact Removal using Bottom Hat Filter and inpainting.
      * Color Constancy corrections using Gray world and max RGB algorithms
  
  2. Training CNN:
      **Efficient Nets are trained in both ensemble and stand-alone manner**
      
      * Stratified Group K-Fold Cross validation
      * Label Smoothing
      * Loss: <a href="https://medium.com/analytics-vidhya/how-focal-loss-fixes-the-class-imbalance-problem-in-object-detection-3d2e1c4da8d7">FOCAL LOSS</a>
  
  3. Testing CNN:
      
      * Tested using both public and private test data hosted on kaggle competition
      
Metrics Used:

The same metric AUC which is given in kaggle is used to measure the performance of the model since the dataset is highly skewed.

**PROGRESS**


- [x] Hair Artifact Removal
- [x] Color Constancy
- [ ] Stratified Group K-Fold Split
- [ ] Label Smoothing
- [ ] Training
- [ ] Testing
      
