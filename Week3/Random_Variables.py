import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats
from scipy.stats import norm
import math as m

# Generate an array of 100 elements following a normal distribution.
# data = np.random.normal(0, 1, 100)
# print("Mean: ", np.mean(data))
# print("Median: ", np.median(data))
# print("Mode: ", stats.mode(data))
# print("Variance: ", np.var(data))
# print("Standard Deviation: ", np.std(data))
# print("Range: ", np.max(data) - np.min(data))
# print("Percentile: ", np.percentile(data, 25))
# print("Quartile: ", np.percentile(data, [25, 50, 75]))

# # PMF - Probability Mass Function: discrete random variable (e.g. rolling a die) 
# data = np.arange(1, 7)
# pmf = [1/6 for _ in data]

# plt.figure(figsize=(10, 5))
# plt.stem(data, pmf)
# plt.title('PMF - Roll a die')   
# plt.xlabel('Die value')
# plt.ylabel('Probability')
# plt.xticks(data)
# plt.show()

# # PDF - Probability Density Function: continuous random variable (e.g. height of people)
# x = np.linspace(-5, 5, 100)
# pdf = norm.pdf(x)

# plt.figure(figsize=(10, 5))
# plt.plot(x, pdf, "r-")
# plt.title('PDF - Normal Distribution')
# plt.xlabel('Value')
# plt.ylabel('Density')
# plt.show()
# the above graph produces a bell curve with a mean of 0 and a standard deviation of 1 (default values) 

# the test scores of an exam with 800 students are distributed with a mean of 75 and a standard deviation of 7, what percentage of students scored between 68 and 82?
# cdf - Cumulative Density Function
mean = 75
std_dev = 7
x1 = 68
x2 = 82
cdf_x1 = norm.cdf(x1, mean, std_dev)
cdf_x2 = norm.cdf(x2, mean, std_dev)
percentage = (cdf_x2 - cdf_x1) * 100
print(f'{percentage:.2f}% of students scored between 68 and 82')

# below is a function to calculate the probability of a Bernoulli random variable (0 or 1) given a probability p of success (1) and a probability 1-p of failure (0) 
def bernoulli(k,p): # k is the value of the random variable (0 or 1), p is the probability of success
    return p*k + (1-p)*(1-k)

print(bernoulli(0, 0.4))
print(bernoulli(1, 0.4))

# a bag contains 8 red marbles and 3 blue marbles, what is the probability of drawing a red marble?
# probability = number of successful outcomes / total number of outcomes
red = 8
blue = 3
total = red + blue
probability = red / total
print(f'The probability of drawing a red marble is {probability:.2f}')
# what is the probability of drawing a blue marble?
probability = blue / total
print(f'The probability of drawing a blue marble is {probability:.2f}')
# now a bag contains 4 red marbles, 7 yellow marbles, and 2 blue marbles, what is the probability of drawing a red or yellow marble?
red = 4
yellow = 7
blue = 2
total = red + yellow + blue
probability = (red + yellow) / total
print(f'The probability of drawing a red or yellow marble is {probability:.2f}')
# what is the probability of drawing a blue marble?
probability = blue / total
print(f'The probability of drawing a blue marble is {probability:.2f}')
# how many ways can you select two colors of marbles from the bag?
# combinations = n! / (r!(n-r)!)
n = total
r = 2
combinations = np.math.factorial(n) / (np.math.factorial(r) * np.math.factorial(n-r))
print(f'There are {combinations} ways to select two colors of marbles from the bag')
# now we have a bag that contains 10 red marbles and 7 blue marbles, 
# you select one marble from the bag, what is probability of selecting a red marble?
red = 10
blue = 7
total = red + blue
probability = red / total
print(f'The probability of selecting a red marble is {probability:.2f}')
# select a blue marble, place it back to the bag and select another marble, what is the probability the second marble is blue?
probability = blue / total
print(f'The probability of selecting a blue marble is {probability:.2f}')
# now select a blue marble, do not replace it, and select another marble, what is the probability the second marble is blue?
probability = blue / (total - 1)
print(f'The probability of selecting a blue marble is {probability:.2f}')

