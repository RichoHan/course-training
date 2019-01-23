# Session 7

## Regularization: Simplicity

### Simplicity matters
If we encounter data with few noises, the model is more likely to fit to those noise if it is too complicated (one with many crosses).

### Be aware of overfitting
![Alt text](https://developers.google.com/machine-learning/crash-course/images/RegularizationTwoLossFunctions.svg "Overfitting")
- Common regularization presentation
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mtext>minimize(Loss(Data|Model) + complexity(Model))</mtext>
</math>
- L2 regularization
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <msub>
    <mi>L</mi>
    <mn>2</mn>
  </msub>
  <mtext>&#xA0;regularization term</mtext>
  <mo>=</mo>
  <mrow class="MJX-TeXAtom-ORD">
    <mo stretchy="false">|</mo>
  </mrow>
  <mrow class="MJX-TeXAtom-ORD">
    <mo stretchy="false">|</mo>
  </mrow>
  <mi mathvariant="bold-italic">w</mi>
  <mrow class="MJX-TeXAtom-ORD">
    <mo stretchy="false">|</mo>
  </mrow>
  <msubsup>
    <mrow class="MJX-TeXAtom-ORD">
      <mo stretchy="false">|</mo>
    </mrow>
    <mn>2</mn>
    <mn>2</mn>
  </msubsup>
  <mo>=</mo>
  <mrow class="MJX-TeXAtom-ORD">
    <msubsup>
      <mi>w</mi>
      <mn>1</mn>
      <mn>2</mn>
    </msubsup>
    <mo>+</mo>
    <msubsup>
      <mi>w</mi>
      <mn>2</mn>
      <mn>2</mn>
    </msubsup>
    <mo>+</mo>
    <mo>.</mo>
    <mo>.</mo>
    <mo>.</mo>
    <mo>+</mo>
    <msubsup>
      <mi>w</mi>
      <mi>n</mi>
      <mn>2</mn>
    </msubsup>
  </mrow>
</math>

### Regularization with Lambda
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mtext>minimize(Loss(Data|Model)</mtext>
  <mo>+</mo>
  <mi>&#x03BB;<!-- λ --></mi>
  <mtext>&#xA0;complexity(Model))</mtext>
</math>

- The goal is to balance between simplicity of model and training-data fit.
    1. Too high, our model will become too simple
    2. Too low, our model will become more complex (overfitting)
    - Tuning is needed

---
## Logistic Regression
- Many problem require a probability estimate as output
- Handy, because the estimates are caliberated

### LogLoss

### Logistic Regression & Regularization
- Regularization is super important in logistic regression
- Two strategies
    1. L2 regularization: penalizes huge weights
    2. Early stopping: limiting training steps or learning rate
