import numpy as np


class SmoothFilter:
    def __init__(self, alpha=0.3):
        self.alpha = alpha
        self.last_value = None

    def update(self, value):
        if self.last_value is None:
            self.last_value = value
            return value

        smoothed = self.alpha * value + (1 - self.alpha) * self.last_value
        self.last_value = smoothed
        return smoothed


def calculate_distance(p1, p2):
    return np.hypot(p2[0] - p1[0], p2[1] - p1[1])
