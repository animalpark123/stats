import numpy as np
import scipy.stats as stats
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Generate sample data for three teaching methods
np.random.seed(42)
method_A = np.random.normal(loc=70, scale=5, size=30)
method_B = np.random.normal(loc=75, scale=5, size=30)
method_C = np.random.normal(loc=80, scale=5, size=30)

# Combine data into a single DataFrame
df = pd.DataFrame({'Method A': method_A, 'Method B': method_B, 'Method C': method_C})

# Melt the DataFrame for ANOVA
melted_df = pd.melt(df, var_name='Method', value_name='Scores')

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(method_A, method_B, method_C)

# Print ANOVA results
print(f'F-statistic: {f_statistic}\nP-value: {p_value}')

# Conduct post-hoc Tukey HSD test
tukey_results = pairwise_tukeyhsd(melted_df['Scores'], melted_df['Method'])

# Print post-hoc results
print(tukey_results)
