import numpy as np

def base_metrics(outcome, label, weights=None):
    if outcome.shape != label.shape:
        raise ValueError(f"{outcome.shape=} != {label.shape=}")

    if weights is None:
        weights = np.ones(outcome.shape)
    elif weights.shape != label.shape:
        raise ValueError(f"{weights.shape=} != {label.shape=}")

    return {
        "tp": weights[(label == 1) & (outcome == 1)].sum(),
        "fn": weights[(label == 1) & (outcome == 0)].sum(),
        "fp": weights[(label == 0) & (outcome == 1)].sum(),
        "tn": weights[(label == 0) & (outcome == 0)].sum(),
    }


def safe_divide(a, b, fallback=np.nan):
    return a / b if b != 0 else fallback

