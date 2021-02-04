import numpy as np


def base_metrics(outcome, label, weights=None):

    if not isinstance(outcome, np.ndarray):
        outcome = np.array(outcome)

    if not isinstance(label, np.ndarray):
        label = np.array(label)

    if weights is not None and not isinstance(weights, np.ndarray):
        weights = np.array(weights)

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

