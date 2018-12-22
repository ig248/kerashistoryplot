import matplotlib.pyplot as plt

from IPython.display import clear_output

from .data import get_metric_vs_epoch


def _ceil_div(dividend, divisor):
    return dividend // divisor + (1 if dividend % divisor else 0)


def make_subplot(data, metric, axis, max_epoch=None):
    for trace in data:
        x, y, label = trace['x'], trace['y'], trace['label']
        if 'batch_' in label:
            style, alpha = 's', 0.3
        else:
            style, alpha = '-', 1.0
        axis.plot(x, y, style, alpha=alpha, label=label)
        axis.set_title(metric)
        if max_epoch:
            plt.axis.set_xlim([0, max_epoch])
        axis.set_xlabel('epoch')
        axis.legend()


def plot_history(
    history,
    clear=True,
    figsize=None,
    max_epoch=None,
    n_cols=2,
    batches=True,
):
    if clear:
        clear_output(wait=True)
    plot_metrics = [
        k for k in history.keys()
        if k not in ['epoch', 'batches'] and not k.startswith('val_')
    ]
    n_subplots = len(plot_metrics)
    n_cols = min(n_cols, n_subplots)
    n_rows = _ceil_div(n_subplots, n_cols)
    fig, axes = plt.subplots(
        nrows=n_rows, ncols=n_cols, figsize=figsize, sharex=True
    )
    if n_cols > 1 and n_rows > 1:
        axes = [a for row in axes for a in row]
    for metric, axis in zip(plot_metrics, axes):
        data = get_metric_vs_epoch(history, metric, batches=batches)
        make_subplot(data, metric, axis, max_epoch=max_epoch)
    plt.tight_layout()
    plt.show()
    return axes
