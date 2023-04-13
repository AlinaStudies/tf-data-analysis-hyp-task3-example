import pandas as pd
import numpy as np
from scipy.stats import permutation_test


chat_id = 721973830

def statistic(x, y, axis):
    return np.mean(x, axis=axis) - np.mean(y, axis=axis)

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.03
    test = permutation_test((x, y), statistic, vectorized=True, alternative='less')
    return test.pvalue < alpha
