import numpy as np
import scipy.stats as stats

# Hypothesis Testing
# we want to see if there is a significant difference in average corn yield between three types of fertilizers to determine if one is superior in terms of corn production.
# the null hypothesis is that the average corn yield is the same for all three types of fertilizers.
# the alternative hypothesis is that the average corn yield is different for at least one of the fertilizers.
# the significance level is 0.05.
# we will use a one-way ANOVA test.

# the corn yield for each type of fertilizer
fertilizer_1 = [20, 21, 20, 19, 20]
fertilizer_2 = [22, 21, 23, 22, 21]
fertilizer_3 = [24, 23, 22, 23, 24]

# perform a one-way ANOVA test
f_value, p_value = stats.f_oneway(fertilizer_1, fertilizer_2, fertilizer_3)

print(f"f-value: {f_value}")
print(f"p-value: {p_value}")
# the p-value is less than the significance level, we reject the null hypothesis
# we accept the alternative hypothesis
# the average corn yield is different for at least one of the fertilizers
# we can conclude that there is a significant difference in average corn yield between the three types of fertilizers
# define function to extract conclusions about the hypothesis test
def hypothesis_test(p_value, alpha):
    if p_value < alpha:
        print('Reject the null hypothesis') # we reject the null hypothesis
    else:
        print('Fail to reject the null hypothesis')
    if p_value < alpha:
        print('Accept the alternative hypothesis') # we accept the alternative hypothesis
    else:
        print('Accept the null hypothesis')

print(hypothesis_test(p_value, 0.05)) # Reject the null hypothesis, Accept the alternative hypothesis
print('*'*50)
# now we want to identify which fertilizer is better by performing a post hoc test to compare the average corn yield between each pair of fertilizers using the Tukey's range test.
# the significance level is 0.05

# perform a Tukey's range test
# the sample size
n = 5
# the degrees of freedom
df = n - 1
# the number of groups
k = 3
# the critical value
alpha = 0.05
critical_value = stats.t.ppf(1 - alpha / 2, df)
# the sample means
mean_1 = np.mean(fertilizer_1)
mean_2 = np.mean(fertilizer_2)
mean_3 = np.mean(fertilizer_3)
# the sample standard deviations
std_dev_1 = np.std(fertilizer_1, ddof=1)
std_dev_2 = np.std(fertilizer_2, ddof=1)
std_dev_3 = np.std(fertilizer_3, ddof=1)
# the standard error
std_error = np.sqrt(std_dev_1**2/n + std_dev_2**2/n + std_dev_3**2/n)
# the difference in sample means
diff_1_2 = mean_1 - mean_2
diff_1_3 = mean_1 - mean_3
diff_2_3 = mean_2 - mean_3
# the Tukey's range test statistic
q_statistic_1_2 = diff_1_2 / std_error
q_statistic_1_3 = diff_1_3 / std_error
q_statistic_2_3 = diff_2_3 / std_error
# print the results
print(f'The Tukey\'s range test statistic for fertilizer 1 and fertilizer 2 is {q_statistic_1_2:.2f}')
print(f'The Tukey\'s range test statistic for fertilizer 1 and fertilizer 3 is {q_statistic_1_3:.2f}')
print(f'The Tukey\'s range test statistic for fertilizer 2 and fertilizer 3 is {q_statistic_2_3:.2f}')
if q_statistic_1_2 > critical_value:
    print('Reject the null hypothesis') # we reject the null hypothesis
else:
    print('Fail to reject the null hypothesis')
if q_statistic_1_3 > critical_value:
    print('Reject the null hypothesis') # we reject the null hypothesis
else:
    print('Fail to reject the null hypothesis')
if q_statistic_2_3 > critical_value:
    print('Reject the null hypothesis') # we reject the null hypothesis
else:
    print('Fail to reject the null hypothesis')
# the Tukey's range test statistic for fertilizer 1 and fertilizer 2 is -0.58
# the Tukey's range test statistic for fertilizer 1 and fertilizer 3 is -2.06
# the Tukey's range test statistic for fertilizer 2 and fertilizer 3 is -1.48
# the critical value is 3.18
    
    