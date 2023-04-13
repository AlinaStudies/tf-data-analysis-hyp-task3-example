import pandas as pd
import numpy as np
from scipy.stats import permutation_test


chat_id = 721973830

def statistic(x, y):
    return np.mean(x) - np.mean(y)

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.03
    _, pval, _ = permutation_test((x, y), statistic, vectorized=True, alternative='less')
    return pval < alpha
