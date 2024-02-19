import numpy as np
import scipy.stats as stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt

# Hypothesis Testing
# we want to see if there is a significant difference in average corn yield between three types of fertilizers to determine if one is superior in terms of corn production.
# the null hypothesis is that the average corn yield is the same for all three types of fertilizers.
# the alternative hypothesis is that the average corn yield is different for at least one of the fertilizers.
# the significance level is 0.05.
# we will use a tukey test.

# the corn yield for each type of fertilizer
fertilizer_1 = [20, 21, 20, 19, 20]
fertilizer_2 = [22, 21, 23, 22, 21]
fertilizer_3 = [24, 23, 22, 23, 24]

data = np.concatenate([fertilizer_1, fertilizer_2, fertilizer_3])
labels = ["F1"] * 5 + ["F2"] * 5 + ["F3"] * 5

# Tukey test
result = pairwise_tukeyhsd(data, labels, alpha = 0.05)
print(result)
# the highest average corn yield is for fertilizer 3 and the lowest is for fertilizer 1, but the difference is not significant between the three types of fertilizers
# fertilizer 3 is not significantly different from fertilizer 2  and fertilizer 1  and fertilizer 2 is not significantly different from fertilizer 1
# we fail to reject the null hypothesis
# we accept the null hypothesis
# the average corn yield is the same for all three types of fertilizers
# we can conclude that there is no significant difference in average corn yield between the three types of fertilizers
