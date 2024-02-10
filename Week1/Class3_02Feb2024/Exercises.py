import numpy as np
import matplotlib.pyplot as plt

# matrix of 3x3
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
# matrix of 3x3 ones
B = np.ones((3, 3))
print(B)
# multiplication of A and B
C = A * B
print(C)
# dot product of A and B
D = np.dot(A, B)
print(D)
# Calculus
def f(x):
    return x**2

x = np.linspace(-10, 10, 100)
print(x)
y = f(x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = x^2')
plt.show()
# linear function of distance = speed * time 
def distance(speed, time):
    return speed * time

speed = 2.5
time = np.linspace(0, 10, 10)
distance = distance(speed, time)
plt.plot(time, distance)
plt.xlabel('time')
plt.ylabel('distance')
plt.title('distance = speed * time')
plt.show()
# create a dataframe from the above data
import pandas as pd
df = pd.DataFrame({'time': time, 'distance': distance})
print(df)

# Given the following variables:
# initial_speed = 0, 
# t = time, 
# a = acceleration 
# and equations distance = initial_speed * t + 0.5 * a * (t^2) and speed = initial_speed + a * t 
# then find the acceleration value and build the quadratic function (t ∈ [0,10]). Also create a graph and a table.
initial_speed = 0
a = 2
t = np.linspace(0, 10, 100)
distance = initial_speed * t + 0.5 * a * (t**2)
speed = initial_speed + a * t
plt.plot(t, distance)
plt.xlabel('time')
plt.ylabel('distance')
plt.plot(t, speed)
plt.xlabel('time')
plt.ylabel('speed')
plt.show()
df = pd.DataFrame({'time': t, 'distance': distance, 'speed': speed})
print(df)

