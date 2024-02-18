import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
from scipy.stats import norm
# Suppose a bag contains 8 Red Marbles and 3 Blue Marbles. what is the probability of choosing a Red Marble from a random draw?
# 
# # PMF - Probability Mass Function: discrete random variable (e.g. rolling a die)
red = 8
blue = 3
total = red + blue
pmf_red = red / total
pmf_blue = blue / total
print(f'Probability of choosing a Red Marble: {pmf_red:.2f}')
print(f'Probability of choosing a Blue Marble: {pmf_blue:.2f}')
# 
# same as above using bernoulli distribution from scipy.stats
from scipy.stats import bernoulli
p = red / total
bernoulli_dist = bernoulli(p)
print(f'Probability of choosing a Red Marble: {bernoulli_dist.pmf(1):.2f}')
print(f'Probability of choosing a Blue Marble: {bernoulli_dist.pmf(0):.2f}')
#
