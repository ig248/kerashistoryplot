def get_metric_vs_epoch(history, metric, batches=True):
    data = []
    val_metric = f'val_{metric}'
    for key in [metric, val_metric]:
        if key in history:
            data.append(
                {
                    'x': history['epoch'],
                    'y': history[key],
                    'label': key
                }
            )
    if batches:
        batch_data = get_batch_metric_vs_epoch(history, metric)
        if batch_data:
            data.append(batch_data)
    return data


def get_batch_metric_vs_epoch(history, metric):
    if not history.get('batches') or metric not in history['batches'][0]:
        return
    epoch_value = [
        (epoch, value)
        for epoch, batch in zip(history['epoch'], history['batches'])
        for value in batch[metric]
    ]
    epoch, value = zip(*epoch_value)
    return {'x': list(epoch), 'y': list(value), 'label': f'batch_{metric}'}
