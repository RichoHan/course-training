# Session 5

## What Is Feature Engineering?
- Transforming raw data into a feature vector
![Alt text](https://developers.google.com/machine-learning/crash-course/images/RawDataToFeatureVector.svg "Feature Engineering")

## Mapping Categorical Data
- OOV (out-of-vocabulary) bucket
    - Also, **one-hot-encoding**
![Alt text](https://developers.google.com/machine-learning/crash-course/images/OneHotEncoding.svg "Feature Engineering")

## Sparse Representation
- It does not make sense when the classes of examples scales (e.g. up to 1,000,000 classes)
    - Try [sparse representation](https://developers.google.com/machine-learning/glossary/#sparse_representation)

## Defining Good Features
1. Should occur frequently in a dataset
2. Should have clear, obvious meaning
3. Shouldn't take on magic numbers
    - Use indicator instead
4. Shouldn't change its meaning over time
5. Shouldn't have crazy outliers
    - Same in doing quantitative research

## Maintaining Good Habits
- Visualize
    - Plot histograms
    - Rank most to least common
- Debug
    - Duplicates?
    - Missing values?
    - Similarity between training and validation set
- Monitor
    - Feature quantities
    - Number of examples over time

## Data Cleaning Tricks
### Scaling feature values
- Helpful when the feature set consists of multiple features
- Quicker gradient descent
- Avoids NaN trap
- Helps the model learn more appropriate weights distribution

**Simple practice**
- Linear mapping
- *`scaledvalue = (value-mean)/stddev`*

### Handling extreme outliers
1. Long tail distribution
![Alt text](https://developers.google.com/machine-learning/crash-course/images/ScalingNoticingOutliers.svg "Long tail")

2. Logarithmic scaling
![Alt text](https://developers.google.com/machine-learning/crash-course/images/ScalingLogNormalization.svg "Logarithmic scaling")

3. Clipping features
![Alt text](https://developers.google.com/machine-learning/crash-course/images/ScalingClipping.svg "Clipping features")

### Binning
- Make model learn completely differently weight for each bins
![Alt text](https://developers.google.com/machine-learning/crash-course/images/ScalingBinningPart2.svg "Binning values")

### Scrubbing
- Ommitted values
- Duplicate examples
- Bad labels
- Bad feature values