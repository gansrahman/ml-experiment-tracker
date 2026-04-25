# ML Experiment Tracker
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/) [![PyTorch](https://img.shields.io/badge/pytorch-2.0+-ee4c2c.svg)](https://pytorch.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Lightweight experiment tracking.

## Usage
```python
from tracker import ExperimentTracker
t = ExperimentTracker('my_run')
t.log_params({'lr': 1e-4, 'batch_size': 32})
t.log_metric('loss', 0.5, step=1)
```
