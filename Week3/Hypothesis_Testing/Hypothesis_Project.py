import numpy as np
import scipy.stats as stats

diet_1 = [2.0, 2.5, 3.0, 2.8, 2.3, 2.7, 2.5]
diet_2 = [3.0, 3.2, 3.1, 2.9, 2.8, 3.0, 3.2]

# ANOVA test
t_value, p_value = stats.ttest_ind(diet_1, diet_2)

print(f"t-value: {t_value}")
print(f"p-value: {p_value}")
# with the above data we want to know if there is a significatn difference in average weight loss between people who followed dietA and people who followed dietB.
# state the hypothesis: null and alternative hypothesis
# null hypothesis: the average weight loss is the same for both diets
# alternative hypothesis: the average weight loss is different for both diets
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

# the p-value is less than the significance level, we reject the null hypothesis
# we accept the alternative hypothesis
# the average weight loss is different for both diets
print(hypothesis_test(p_value, 0.05)) # Reject the null hypothesis, Accept the alternative hypothesis
# we can conclude that there is a significant difference in average weight loss between people who followed dietA and people who followed dietB
print('*'*50)
# perform a student's t-test of the hypothesis that the average weight loss is the same for both diets
# the significance level is 0.05
# the sample size
n = len(diet_1)
# the degrees of freedom
df = n - 1
# the sample means
mean_1 = np.mean(diet_1)
mean_2 = np.mean(diet_2)
# the sample standard deviations
std_dev_1 = np.std(diet_1, ddof=1)
std_dev_2 = np.std(diet_2, ddof=1)
# the standard error of the difference in sample means
std_error = np.sqrt(std_dev_1**2/n + std_dev_2**2/n)
# the t-score
t_score = (mean_1 - mean_2) / std_error
# the p-value
p_value = 2 * (1 - stats.t.cdf(abs(t_score), df))
# the critical value
alpha = 0.05
critical_value = stats.t.ppf(alpha / 2, df)
# print the results
print(f'The t-score is {t_score:.2f}')
print(f'The p-value is {p_value:.2f}')
print(f'The critical value is {critical_value:.2f}')
print(hypothesis_test(p_value, alpha)) # Reject the null hypothesis, Accept the alternative hypothesis
# the p-value is less than the significance level, we reject the null hypothesis    
# the average weight loss is different for both diets
# we can conclude that there is a significant difference in average weight loss between people who followed dietA and people who followed dietB

def hypothesis_test(p_value, alpha):
    if p_value < alpha:
        print('Reject the null hypothesis') # we reject the null hypothesis
    else:
        print('Fail to reject the null hypothesis')
    if p_value < alpha:
        print('Accept the alternative hypothesis') # we accept the alternative hypothesis
    else:
        print('Accept the null hypothesis')

# write more efficient code for the above function using a single if-else statement
        
def hypothesis_test(p_value, alpha):
    if p_value < alpha:
        print('Reject the null hypothesis') # we reject the null hypothesis
        print('Accept the alternative hypothesis') # we accept the alternative hypothesis
    else:
        print('Fail to reject the null hypothesis')
        print('Accept the null hypothesis') # we accept the null hypothesis

