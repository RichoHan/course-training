# Session 13

## Static vs. Dynamic Training

### Static Model - Trained Offline
- Easy to build and test
- Rerquires monitoring of inputs
- Easy for scaling

### Dynamic Model - Trained Online
- Continue to feed in training data over time
- [Prograssive validation](https://www.gss.com.tw/index.php/focus/eis/157-eis82/1540-eis82-2)
- Need monitoring, model rollback (version control), & data quarantine capabilities
- Will adapt to changes, staleness issues avoided

---
## Static vs. Dynamic Inference

### Offline Inference
- Upside
    - No worry about cost of inference
    - Batch mode
    - Post verification before pushing
- Downside
    - Can only predict things we know about
    - Update latency

### Online Inference
- Upside
    - Predict new item as it comes in
- Downside
    - Compute intensive, latenct sensitive
    - Monitering needed

---
## Data Dependencies
- Akin to code dependencies
    - Unit tests for data?
- Reliability
    - What happens when the signal is not available?
- Versioning
    - How would computation of data change over time?
- Necessity
    - Usefulness and cost of including a signal
- Correlations
    - Do signals tied together due to correlations?
- Feedback Loops
    - Will input signals be impacted by models' outputs?
    - E.g. stock market prediction models