from kerashistoryplot.data import get_batch_metric_vs_epoch, get_metric_vs_epoch

HISTORY = {
    'batches': [
        {
            'batch': [0, 1],
            'size': [300, 200],
            'loss': [0.4, 0.3],
            'mean_absolute_error': [0.28948462, 0.2989089]
        },
        {
            'batch': [0, 1],
            'size': [300, 200],
            'loss': [0.2, 0.1],
            'mean_absolute_error': [0.30267844, 0.2740341]
        }
    ],
    'val_loss': [0.37, 0.17],
    'val_mean_absolute_error': [0.2915948450565338, 0.2897853195667267],
    'loss': [0.35, 0.15],
    'mean_absolute_error': [0.29325432777404786, 0.2912207067012787],
    'lr': [0.01, 0.01],
    'epoch': [0, 1]
}


class TestGetMetricVsEpoch:
    def test_simple_case(self):
        plot_data = get_metric_vs_epoch(HISTORY, metric='lr')
        expected_data = [{'x': [0, 1], 'y': [0.01, 0.01], 'label': 'lr'}]

        assert plot_data == expected_data

    def test_get_batch_metric_vs_epoch(self):
        batch_data = get_batch_metric_vs_epoch(HISTORY, metric='loss')
        expected_data = {
            'x': [0, 0, 1, 1],
            'y': [0.4, 0.3, 0.2, 0.1],
            'label': 'batch_loss'
        }

        assert batch_data == expected_data

    def test_case_with_val_and_batches(self):
        plot_data = get_metric_vs_epoch(HISTORY, metric='loss')
        expected_data = [
            {
                'x': [0, 1],
                'y': [0.35, 0.15],
                'label': 'loss'
            }, {
                'x': [0, 1],
                'y': [0.37, 0.17],
                'label': 'val_loss'
            },
            {
                'x': [0, 0, 1, 1],
                'y': [0.4, 0.3, 0.2, 0.1],
                'label': 'batch_loss'
            }
        ]
        assert plot_data == expected_data
