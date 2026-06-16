# ML Experiment Tracker

Lightweight experiment tracking.

## Usage
```python
from tracker import ExperimentTracker
t = ExperimentTracker('my_run')
t.log_params({'lr': 1e-4, 'batch_size': 32})
t.log_metric('loss', 0.5, step=1)
```
