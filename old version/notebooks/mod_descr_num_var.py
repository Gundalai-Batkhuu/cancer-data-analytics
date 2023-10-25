import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats

sns.set_style('whitegrid')
pd.set_option('display.max_rows', None)


def descr(df, var_name):
    data = df[var_name]
    data.describe()
    sns.histplot(data, bins=20, kde=True)
    stats.t.interval(alpha=0.95, df=len(data) - 1, loc=np.mean(data), scale=stats.sem(data))
