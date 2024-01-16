import numpy as np
import scipy.stats as stats

# Generate sample data for two groups
np.random.seed(42)  # for reproducibility
scores_groupA = np.random.normal(loc=70, scale=10, size=30)
scores_groupB = np.random.normal(loc=75, scale=10, size=30)

# Formulate hypotheses
# Null Hypothesis (H0): The means of Group A and Group B are equal.
# Alternative Hypothesis (Ha): There is a significant difference in means between Group A and Group B.

# Conduct t-test
t_stat, p_value = stats.ttest_ind(scores_groupA, scores_groupB)

# Print results
print(f'T-statistic: {t_stat}\nP-value: {p_value}')

# Interpret results
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference in exam scores.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in exam scores.")
