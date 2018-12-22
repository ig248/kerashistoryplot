[![Build Status](https://travis-ci.com/ig248/livehistoryplot.svg?branch=master)](https://travis-ci.com/ig248/livehistoryplot)
[![Coverage Status](https://codecov.io/gh/ig248/livehistoryplot/branch/master/graph/badge.svg)](https://codecov.io/gh/ig248/livehistoryplot)

# Live history plot for Keras model training

![history plot with batches](livehistoryplot.png)

## Usage
Install package from source:

```
pip install git+https://github.com/ig248/livehistoryplot
```

Import function:

```python
from livehistoryplot.callbacks import PlotHistory
```

Use in callbacks:

```python
model.fit(
    X, y,
    epochs=20,
    callbacks=[
        ReduceLROnPlateau(),
        PlotHistory(batches=True, n_cols=3, figsize=(15, 7))
    ]
)
```

## Tests
Run
```bash
make dev-install
make test
```

## References
Original `livelossplot`: https://github.com/stared/livelossplot
