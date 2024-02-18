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
