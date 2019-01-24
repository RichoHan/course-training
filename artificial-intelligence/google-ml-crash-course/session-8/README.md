# Session 8

## Classification

### Evaluation Metrics
- Precision & Recall
- Visualized as ROC curve
![Alt text](https://developers.google.com/machine-learning/crash-course/images/ROCCurve.svg "ROC Curve")
- AUC: Area Under the ROC Curve
![Alt text](https://developers.google.com/machine-learning/crash-course/images/AUC.svg "AUC")

### Prediction Bias
- Logistic regression predictions should be unbiased:
    - *"average of predictions" should ≈ "average of observations"*
- If the model does not have zero bias, then there are concerns
- callibration layer (probably not a good idea)
    - You're fixing the symptom rather than the cause.
    - You've built a more brittle system that you must now keep up to date.

### Calibration
![Alt text](https://developers.google.com/machine-learning/crash-course/images/BucketingBias.svg "Valibration plot")
- There are serveral possible reasons behind:
    1. The training set doesn't adequately represent certain subsets of the data space.
    2. Some subsets of the data set are noisier than others.
    3. The model is overly regularized. (Consider reducing the value of lambda.)
