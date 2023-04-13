import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


chat_id = 721973830

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.03
    test = ttest_ind(x, y)
    return test.pvalue < alpha
