"""Generate basic rolling features for numeric time series."""
from __future__ import annotations

from statistics import mean


def rolling_features(values: list[float], window: int) -> list[dict[str, float | None]]:
    """Return trailing mean, min, max, and delta for each point."""
    if window < 1:
        raise ValueError("window must be positive")
    result: list[dict[str, float | None]] = []
    for index, value in enumerate(values):
        history = values[max(0, index - window + 1):index + 1]
        result.append({
            "value": value,
            "mean": mean(history),
            "min": min(history),
            "max": max(history),
            "delta": None if index == 0 else value - values[index - 1],
        })
    return result
