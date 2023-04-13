import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu


chat_id = 721973830

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.03
    test = mannwhitneyu(x, y, alternative = "less")
    return test.pvalue < alpha
