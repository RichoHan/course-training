# Session 12

## Embeddings
- Example application - *collaborative filtering*
- Embedding item into a low-dimensional space created such that similar items are nearby.

### Embeddings: Translating to a Lower-Dimensional Space
- Encode semantic meanings with position (distance and direction):
![Alt text](https://developers.google.com/machine-learning/crash-course/images/linear-relationships.svg "Embeddings analogies")
- Embeddings can be used for:
    1. Shrinking the network
    2. Used as lookup tables
        - Embedding lookup as matrix multiplication

###  Embeddings: Obtaining Embeddings
- Empirical rule-of-thumb (should be tuned using validation set)
    - dimensions ~= sqrt(4, "possible values")
