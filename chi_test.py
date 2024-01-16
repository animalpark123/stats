import numpy as np
import scipy.stats as stats

# Create a contingency table (example data)
# Rows represent gender (0: male, 1: female)
# Columns represent job satisfaction (0: not satisfied, 1: satisfied)
observed_data = np.array([[25, 15], [20, 40]])

# Formulate hypotheses
# Null Hypothesis (H0): Gender and job satisfaction are independent.
# Alternative Hypothesis (Ha): There is a significant association between gender and job satisfaction.

# Conduct chi-square test
chi2_stat, p_value, dof, expected = stats.chi2_contingency(observed_data)

# Print results
print(f'Chi-square statistic: {chi2_stat}\nP-value: {p_value}\nDegrees of freedom: {dof}')
print('Expected frequencies:\n', expected)

# Interpret results
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant association between gender and job satisfaction.")
else:
    print("Fail to reject the null hypothesis. Gender and job satisfaction are independent.")
