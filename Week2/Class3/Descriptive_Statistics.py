import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats

x = [3, 5, 7, 9, 11]
print("Mean: ", np.mean(x))
print("Median: ", np.median(x))
print("Mode: ", stats.mode(x))
print("Variance: ", np.var(x))
print("Standard Deviation: ", np.std(x))
print("Range: ", np.max(x) - np.min(x))
print("Percentile: ", np.percentile(x, 25))
print("Quartile: ", np.percentile(x, [25, 50, 75]))
print('*' * 50)
# Generate an array of 100 elements following a normal distribution.
data = np.random.normal(0, 1, 100)
print("Mean: ", np.mean(data))
print("Median: ", np.median(data))
print("Mode: ", stats.mode(data))
print("Variance: ", np.var(data))
print("Standard Deviation: ", np.std(data))
print("Range: ", np.max(data) - np.min(data))
print("Percentile: ", np.percentile(data, 25))
print("Quartile: ", np.percentile(data, [25, 50, 75]))

# Generate an array of 100 elements following a chi-square distribution with 3 degrees of freedom (df).
data = np.random.chisquare(3, 100)
print("Mean: ", np.mean(data))
print("Median: ", np.median(data))
print("Mode: ", stats.mode(data))
print("Variance: ", np.var(data))
print("Standard Deviation: ", np.std(data))

"""
generate 3 gaussian distributed numbers with mean 0 and standard deviation 1, sum the values, do this a lot of times and calculate the mean of these sums
sum the values squared
"""

# Define a function def to calculate the standard deviation of data = [4, 2, 5, 8, 6] without using numpy.
data = [4, 2, 5, 8, 6]

def std_deviation(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance ** 0.5

print("Standard Deviation: ", std_deviation(data))

# Define a function def to calculate the standard deviation of data = [4, 2, 5, 8, 6] using numpy.
def std_deviation(data):
    return np.std(data)

print("Standard Deviation: ", std_deviation(data))
