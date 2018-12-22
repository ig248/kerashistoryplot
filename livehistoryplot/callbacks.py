from .plot import plot_history


class Callback(object):
    """Abstract base class used to build new callbacks.

    # Properties
        params: dict. Training parameters
            (eg. verbosity, batch size, number of epochs...).
        model: instance of `keras.models.Model`.
            Reference of the model being trained.
    The `logs` dictionary that callback methods
    take as argument will contain keys for quantities relevant to
    the current batch or epoch.
    Currently, the `.fit()` method of the `Sequential` model class
    will include the following quantities in the `logs` that
    it passes to its callbacks:
        on_epoch_end: logs include `acc` and `loss`, and
            optionally include `val_loss`
            (if validation is enabled in `fit`), and `val_acc`
            (if validation and accuracy monitoring are enabled).
        on_batch_begin: logs include `size`,
            the number of samples in the current batch.
        on_batch_end: logs include `loss`, and optionally `acc`
            (if accuracy monitoring is enabled).
    """

    def __init__(self):
        self.validation_data = None
        self.model = None

    def set_params(self, params):
        self.params = params

    def set_model(self, model):
        self.model = model

    def on_epoch_begin(self, epoch, logs=None):
        pass

    def on_epoch_end(self, epoch, logs=None):
        pass

    def on_batch_begin(self, batch, logs=None):
        pass

    def on_batch_end(self, batch, logs=None):
        pass

    def on_train_begin(self, logs=None):
        pass

    def on_train_end(self, logs=None):
        pass


class BatchHistory(Callback):
    """Log all history, including per-batch losses and metrics.

    Based on keras.callbacks.History
    """

    def on_train_begin(self, logs=None):
        self.history = {}

    def on_epoch_begin(self, epoch, logs=None):
        batch_history = self.history.setdefault('batches', [])
        batch_history.append({})

    def on_batch_end(self, batch, logs=None):
        batch_history = self.history['batches'][-1]
        for k, v in logs.items():
            batch_history.setdefault(k, []).append(v)

    def on_epoch_end(self, epoch, logs=None):
        logs = logs or {}
        logs.update(epoch=epoch)
        for k, v in logs.items():
            self.history.setdefault(k, []).append(v)


class PlotHistory(BatchHistory):
    def __init__(self, **plot_kwargs):
        self.plot_kwargs = plot_kwargs

    def on_epoch_end(self, epoch, logs=None):
        super().on_epoch_end(epoch, logs=logs)
        plot_history(self.history, **self.plot_kwargs)
