
Experiment 2: A/B Test Significance Testing
Tests whether a simulated win-back campaign significantly increased 
reactivation rate among At-Risk/Hibernating customers, using a 
chi-square test and 95% confidence interval on the lift.

Input: experiment_results.csv (CustomerID, Segment, Group_Type, Reactivated)


import pandas as pd
from scipy.stats import chi2_contingency

# Load the CSV you uploaded via the Files sidebar
df = pd.read_csv('/content/experiment_results.csv')

# Quick check it loaded correctly
print(df.head())
print(df.shape)

contingency = pd.crosstab(df['Group_Type'], df['Reactivated'])
print("Contingency Table:")
print(contingency)

chi2, p_value, dof, expected = chi2_contingency(contingency)

print(f"\nChi-square statistic: {chi2:.4f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print(f"\nResult: Statistically significant (p={p_value:.4f} < {alpha})")
    print("→ Reject the null hypothesis. The campaign appears to have a real effect on reactivation.")
else:
    print(f"\nResult: Not statistically significant (p={p_value:.4f} >= {alpha})")
    print("→ Fail to reject the null hypothesis. Can't conclude the campaign caused the difference.")

import numpy as np
from scipy.stats import norm

# Rates
p_control = 138/447
p_treatment = 179/450

# Standard error of the difference
se = np.sqrt(p_control*(1-p_control)/447 + p_treatment*(1-p_treatment)/450)

# 95% confidence interval
diff = p_treatment - p_control
ci_lower = diff - 1.96*se
ci_upper = diff + 1.96*se

print(f"Reactivation lift: {diff*100:.2f} percentage points")
print(f"95% CI: [{ci_lower*100:.2f}, {ci_upper*100:.2f}]")