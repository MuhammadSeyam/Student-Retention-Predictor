# %%
import pandas as pd
pd.set_option('display.max_columns', None)      # Show all columns
pd.set_option('display.max_rows', None)         # Show all rows
pd.set_option('display.max_colwidth', None)     # Show full cell content
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_csv('phase1.csv')

# %%
df.describe()

# %%
from sklearn.preprocessing import StandardScaler, MinMaxScaler

mean_age = df['STDNT_AGE'].mean()
std_age = df['STDNT_AGE'].std()

lower_bound = mean_age - 3 * std_age
upper_bound = mean_age + 3 * std_age

# %%
lower_bound

# %%
upper_bound


