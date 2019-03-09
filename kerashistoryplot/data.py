def get_metrics(history):
    plot_metrics = [
        k for k in history.keys()
        if k not in ['epoch', 'batches'] and not k.startswith('val_')
    ]
    return plot_metrics


def get_metric_vs_epoch(history, metric, batches=True):
    data = []
    val_metric = f'val_{metric}'
    for key in [metric, val_metric]:
        if key in history:
            values = history[key]
            if 'epoch' in history:
                epochs = history['epoch']
            else:
                epochs = range(len(values))
            data.append(
                {
                    'x': epochs,
                    'y': values,
                    'label': key
                }
            )
    if batches:
        batch_data = _get_batch_metric_vs_epoch(history, metric)
        if batch_data:
            data.append(batch_data)
    return data


def _get_batch_metric_vs_epoch(history, metric):
    if not history.get('batches') or metric not in history['batches'][0]:
        return
    epoch_value = [
        (epoch, value)
        for epoch, batch in zip(history['epoch'], history['batches'])
        for value in batch[metric]
    ]
    epoch, value = zip(*epoch_value)
    return {'x': list(epoch), 'y': list(value), 'label': f'batch_{metric}'}
