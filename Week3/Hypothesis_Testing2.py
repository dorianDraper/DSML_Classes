import numpy as np
import scipy.stats as stats

# Hypothesis Testing
# we have 2 different types of diets A and B and want to check the difference in weight loss between the two diets after one month.
# we choose two random groups of poeple, group A follows diet A and group B follows diet B.
# After one month we record the weight loss in kg for each group.
dietA = np.array([2.0, 2.5, 3.0, 2.8, 2.3, 2.7, 2.5])
dietB = np.array([3.0, 3.2, 3.1, 2.9, 2.8, 3.0, 3.2])
# with the above data we want to know if there is a significatn difference in average weight loss between people who followed dietA and people who followed dietB.
# state the hypothesis: null and alternative hypothesis
# null hypothesis: the average weight loss is the same for both diets
# alternative hypothesis: the average weight loss is different for both diets
# test the hypothesis: we will use a student's t-test
# the significance level is 0.05

# the sample size
n = len(dietA)
# the degrees of freedom
df = n - 1
# the sample means
meanA = dietA.mean()
meanB = dietB.mean()
# the sample standard deviations
std_devA = dietA.std(ddof=1)
std_devB = dietB.std(ddof=1)
# the standard error of the difference in sample means
std_error = np.sqrt(std_devA**2/n + std_devB**2/n)
# the t-score
t_score = (meanA - meanB) / std_error   
# the p-value
p_value = 2 * (1 - stats.t.cdf(abs(t_score), df))
# the critical value
alpha = 0.05
critical_value = stats.t.ppf(alpha / 2, df)
# print the results
print(f'The t-score is {t_score:.2f}')
print(f'The p-value is {p_value:.2f}')
print(f'The critical value is {critical_value:.2f}')
if p_value < alpha:
    print('Reject the null hypothesis') # we reject the null hypothesis
else:
    print('Fail to reject the null hypothesis')
if t_score < -critical_value or t_score > critical_value:
    print('Reject the null hypothesis') # we reject the null hypothesis
else:
    print('Fail to reject the null hypothesis')
if p_value < alpha:
    print('Accept the alternative hypothesis') # we accept the alternative hypothesis
else:
    print('Accept the null hypothesis')
# the p-value is less than the significance level, we reject the null hypothesis
# the t-score is less than the negative critical value or greater than the positive critical value, we reject the null hypothesis
# we accept the alternative hypothesis
# the average weight loss is different for both diets
# we can conclude that there is a significant difference in average weight loss between people who followed dietA and people who followed dietB
# we can also calculate the confidence interval for the difference in sample means
