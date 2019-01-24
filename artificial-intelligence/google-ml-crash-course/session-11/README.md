# Session 11

## Training Neural Nets

### Gradient Matters
- If it's differentiable, we can probably learn from it.
- Gradients can vanish
    - Used for reducing signal vs. noise
    - ReLUs are useful here
- Gradients can explode
    - Learning rate tuning matters
    - Batch normalization can help
- ReLU layers can die
    - Keep calm & lower your learning rates

### Dropout regularization
- Useful for NNs
- "Randomly" dropping out units in networks

---
## Multi-Class Neural Nets
- Reasonable when total number of classes is small
![Alt text](https://developers.google.com/machine-learning/crash-course/images/OneVsAll.svg "Multi-class NN")

### SoftMax
- Extend the idea of logistic regression into multi-class world
- The SoftMax layer must the same number of nodes as the output layer
![Alt text](https://developers.google.com/machine-learning/crash-course/images/SoftmaxLayer.svg "SoftMax layer")

### SoftMax Options
1. Full SOftMax
    - Softmax calculates a probability for every possible class.
2. Candidate sampling
    - calculates a probability for all the positive labels but only for a random sample of negative labels.

### One vs. Many Labels
SoftMax does not apply in the following situation:
    - examples are members of multiple classes
    - Use multiple logistic regression instead