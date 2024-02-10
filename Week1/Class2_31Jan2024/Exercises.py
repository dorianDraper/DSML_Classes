import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# # create plot with 2 lines, one with sin(x) and the other with cos(x)
# x = np.linspace(0,2*np.pi,100)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.title('Sin(x) and Cos(x)')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()
# # create scatter plot with 100 random numbers
# x = np.random.rand(1000)
# y = np.random.rand(1000)
# plt.scatter(x,y)
# plt.title('Scatter Plot')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()
# # create histogram with 1000 random numbers
# x = np.random.randn(1000)
# plt.hist(x)
# plt.title('Histogram')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()
print(' ')
# n equals to 10 random numbers from 1 to 9
# numbers = np.random.randint(1,10,10)
# print(numbers)
# hist = {}
# for n in numbers:
#     if n in hist:
#         hist[n] += 1 # or hist[n] = hist[n] + 1
#     else:
#         hist[n] = 1

# print(hist)
# create histogram with figsize 10,5
numbers = np.random.randint(100, size=1000)
lower_10 = [ n for n in numbers if n < 10 ]
plt.figure(figsize=(10,5))
plt.hist(numbers, bins=10, alpha=0.7, color='red')
plt.title('Histogram')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
# bar chart
categories = ['dogs', 'cats', 'fish', 'birds']
values = [4,2,1,3]
plt.bar(categories, values)
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
# pie chart
plt.pie(values, labels=categories)
plt.title('Pie Chart')
plt.show()