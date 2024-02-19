import numpy as np
import scipy.stats as stats
from scipy.special import comb

# Binomial Distribution
# The number of successes in a fixed number of independent Bernoulli trials
# The probability of success and failure is constant
# The trials are independent
# The number of trials is fixed
# The random variable X is the number of successes in n trials
# The probability mass function (pmf) is given by: P(X=k) = (n choose k) * p^k * (1-p)^(n-k)
# The mean is given by: E(X) = n * p    
# The variance is given by: Var(X) = n * p * (1-p)
# The standard deviation is given by: sqrt(Var(X))
# The cumulative distribution function (cdf) is given by: P(X<=k) = sum(P(X=i), i=0 to k)

# a game called Sennet where players moves are decided by dropping 4 paddles with two colored faces. 
# The players are allowed to move based on the number of colored paddles that are facing up. 
# Our goal is to explore the likely outcomes of the drops to begin to understand probability.
# The probability of a paddle landing with the red face up is 0.6
# The probability of a paddle landing with the blue face up is 0.4
# The number of paddles is 4
# The number of paddles that are red is 2
# The number of paddles that are blue is 2
# The number of trials is 4

# The probability mass function (pmf) is given by: P(X=k) = (n choose k) * p^k * (1-p)^(n-k)
n = 4
p = 0.6
k = 0
pmf = comb(n, k) * p**k * (1-p)**(n-k)
print(f'The probability of {k} red paddles is {pmf:.2f}')
k = 1
pmf = comb(n, k) * p**k * (1-p)**(n-k)
print(f'The probability of {k} red paddles is {pmf:.2f}')
k = 2
pmf = comb(n, k) * p**k * (1-p)**(n-k)
print(f'The probability of {k} red paddles is {pmf:.2f}')
k = 3
pmf = comb(n, k) * p**k * (1-p)**(n-k)
print(f'The probability of {k} red paddles is {pmf:.2f}')

# now suppose we instead play the game of Sennet using 5 sticks 
# how many ways are there to get three white sticks?
n = 5
k = 3
combinations = comb(n, k)
print(f'There are {combinations} ways to get three white sticks')
# what is the probability of getting three white sticks?
p = 0.6
pmf = comb(n, k) * p**k * (1-p)**(n-k)
print(f'The probability of getting three white sticks is {pmf:.2f}')

# Suppose we toss 10 coins. How many different outcomes contain exactly three heads?
n = 10
k = 3
combinations = comb(n, k)
print(f'There are {combinations} different outcomes that contain exactly three heads')








