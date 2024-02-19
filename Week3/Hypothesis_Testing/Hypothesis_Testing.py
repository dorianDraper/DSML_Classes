import numpy as np
import scipy.stats as stats

# Hypothesis Testing
# We want to test if the mean of a population is equal to a specific value. 
# We have a sample of 100 elements with a mean of 100 and a standard deviation of 10.
# The null hypothesis is that the mean of the population is 100.
# The alternative hypothesis is that the mean of the population is not 100.
# The significance level is 0.05.
# We will use a two-tailed test.
# The z-score is the number of standard deviations from the mean.
# The z-score is calculated as (sample mean - population mean) / (standard deviation / sqrt(sample size))
# The z-score is 0 if the sample mean is equal to the population mean.
# The z-score is greater than 0 if the sample mean is greater than the population mean.
# The z-score is less than 0 if the sample mean is less than the population mean.
# The p-value is the probability of observing a sample mean as extreme as the one obtained, assuming the null hypothesis is true.
# The p-value is calculated as 2 * (1 - norm.cdf(abs(z-score))).
# If the p-value is less than the significance level, we reject the null hypothesis.
# If the p-value is greater than the significance level, we fail to reject the null hypothesis.
# If the p-value is less than the significance level, we accept the alternative hypothesis.
# If the p-value is greater than the significance level, we accept the null hypothesis.
# The critical value is the value that separates the rejection region from the non-rejection region.
# The critical value is calculated as norm.ppf(significance level / 2).
# If the z-score is less than the negative critical value or greater than the positive critical value, we reject the null hypothesis.
# If the z-score is greater than the negative critical value and less than the positive critical value, we fail to reject the null hypothesis.
# If the z-score is less than the negative critical value, we accept the alternative hypothesis.
# If the z-score is greater than the positive critical value, we accept the alternative hypothesis.
# If the z-score is greater than the negative critical value and less than the positive critical value, we accept the null hypothesis.

# the sample mean
sample_mean = 100
# the population mean
population_mean = 100
# the standard deviation
std_dev = 10
# the sample size
n = 100
# the significance level
alpha = 0.05
# the z-score
z_score = (sample_mean - population_mean) / (std_dev / np.sqrt(n))
# the p-value
p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
# the critical value
critical_value = stats.norm.ppf(alpha / 2)
# print the results
print(f'The z-score is {z_score:.2f}')
print(f'The p-value is {p_value:.2f}')
print(f'The critical value is {critical_value:.2f}')
if p_value < alpha:
    print('Reject the null hypothesis')
else:
    print('Fail to reject the null hypothesis')
if z_score < -critical_value or z_score > critical_value:
    print('Reject the null hypothesis')
else:
    print('Fail to reject the null hypothesis')
if p_value < alpha:
    print('Accept the alternative hypothesis')
else:
    print('Accept the null hypothesis')
if z_score < -critical_value:
    print('Accept the alternative hypothesis')
elif z_score > critical_value:
    print('Accept the alternative hypothesis')
else:
    print('Accept the null hypothesis')
