import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm, uniform

def dbinom(x, size, prob = 0.5):
    """
    Calculates the point estimate of the binomial distribution
    """
    result = binom.pmf(k = x, n = size, p = prob, loc = 0)
    return result

def pbinom(q, size, prob = 0.5):
    """
    Calculates the cumulative of the binomial distribution
    """
    result = binom.cdf(k = q, n = size, p = prob, loc = 0)
    return result

def qbinom(p, size, prob = 0.5):
    """
    Calculates the quantile function from the binomial distribution
    """
    result = binom.ppf(q = p, n = size, p = prob, loc = 0)
    return result

def rbinom(n, size, prob = 0.5):
    """
    Generates random variables from the binomial distribution
    """
    result = binom.rvs(n = size, p = prob, size = n)
    return result

# Binomial(10, 0.2) distribution where n = 10 is the number of trials and p = 0.2 is the probability of success in a single trial.
np.random.seed(42)

# given the above functions for binomial distribution, write them for normal and uniform distributions
# the normal distribution is a continuous probability distribution, so the functions will be similar to the binomial distribution
# the uniform distribution is a continuous probability distribution, so the functions will be similar to the binomial distribution

def dnorm(x, mean = 0, sd = 1):
    """
    Calculates the point estimate of the normal distribution
    """
    result = norm.pdf(x, loc = mean, scale = sd)
    return result

def pnorm(q, mean = 0, sd = 1):
    """
    Calculates the cumulative of the normal distribution
    """
    result = norm.cdf(q, loc = mean, scale = sd)
    return result

def qnorm(p, mean = 0, sd = 1):
    """
    Calculates the quantile function from the normal distribution
    """
    result = norm.ppf(p, loc = mean, scale = sd)
    return result

def rnorm(n, mean = 0, sd = 1):
    """
    Generates random variables from the normal distribution
    """
    result = norm.rvs(loc = mean, scale = sd, size = n)
    return result

def dunif(x, min = 0, max = 1):
    """
    Calculates the point estimate of the uniform distribution
    """
    result = uniform.pdf(x, loc = min, scale = max - min)
    return result   

def punif(q, min = 0, max = 1):
    """
    Calculates the cumulative of the uniform distribution
    """
    result = uniform.cdf(q, loc = min, scale = max - min)
    return result

def qunif(p, min = 0, max = 1):
    """
    Calculates the quantile function from the uniform distribution
    """
    result = uniform.ppf(p, loc = min, scale = max - min)
    return result

def runif(n, min = 0, max = 1):
    """
    Generates random variables from the uniform distribution
    """
    result = uniform.rvs(loc = min, scale = max - min, size = n)
    return result

# test the functions