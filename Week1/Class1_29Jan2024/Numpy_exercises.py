import numpy as np
import pandas as pd

# create 1D array with numbers 1-10
my_array = np.arange(1,11)
print(my_array)
# access the third element in the array
print(my_array[2])
# access the last element in the array
print(my_array[-1])
# change the value of the second element to 20
my_array[1] = 20
print(my_array)
# add 10 to all elements in the array
my_array = my_array + 10
print(my_array)
# calculate the sum of all elements in the array
print(np.sum(my_array)) # or sum_all = np.sum(my_array)
print(' ')
print('*'*20)
# create 2D array with numbers 1-9
print('2-D Array')
my_array2 = np.arange(1,10).reshape(3,3)
print(my_array2)
print(' ')
print('*'*20)
# create 3D array with numbers 1-8
print('3-D Array')
my_array3 = np.arange(1,9).reshape(2,2,2)
print(my_array3)
print(' ')
print('*'*20)
# Aritmetic operations
print('Aritmetic operations')
# create 1D array with numbers 1-5
my_array_example = np.arange(1,6)
print(my_array_example)
# add 10 to all elements in the array
print('Sum: ', np.add(my_array_example,10))
# multiply all elements in the array by 2
print('Multiply: ', np.multiply(my_array_example,2))
# Logarithmic operations
print('Logarithmic operations')
# natural logarithm of all elements in the array
print('Natural logarithm: ', np.log(my_array_example))
# exponential of all elements in the array
print('Exponential: ', np.exp(my_array_example))
# Statistical Functions
print('Statistical Functions')
# mean of all elements in the array
print('Mean: ', np.mean(my_array_example))
# median of all elements in the array
print('Median: ', np.median(my_array_example))
# standard deviation of all elements in the array
print('Standard deviation: ', np.std(my_array_example))
# variance of all elements in the array
print('Variance: ', np.var(my_array_example))
# maximum value of all elements in the array
print('Maximum value: ', np.max(my_array_example))
# maximum index of all elements in the array
print('Maximum index: ', np.argmax(my_array_example))
# minimum value of all elements in the array
print('Minimum value: ', np.min(my_array_example))
# minimum index of all elements in the array
print('Minimum index: ', np.argmin(my_array_example))
# sum of all elements in the array
print('Sum: ', np.sum(my_array_example))
# Rouding Functions
print('Rouding Functions')
# create decimal random array with numbers 1-5
my_array_example2 = np.array([1.23, 2.47, 3.56, 4.89])
print('Decimal random array: ', my_array_example2)
# round all elements in the array
print('Rounding: ', np.round(my_array_example2))    
# minor integer (floor) of all elements in the array
print('Minor integer: ', np.floor(my_array_example2))
# major integer (ceil) of all elements in the array
print('Major integer: ', np.ceil(my_array_example2))
print(' ')
print('*'*20)
# Exercise 01: Create a null vector that contains 10 elements
print('Exercise 01 - Create a null vector that contains 10 elements')
null_vector = np.zeros(10)
print(null_vector)
print(' ')
print('*'*20)
# Exercise 02: Create a vector of ones with 10 elements
print('Exercise 02 - Create a vector of ones with 10 elements')
ones_vector = np.ones(10)
print(ones_vector)
print(' ')
print('*'*20)
# Exercise 03: With the linspace function of Numpy and create an array with 10 elements
print('Exercise 03 - With the linspace function of Numpy and create an array with 10 elements')
linspace_vector = np.linspace(1,10,10)
print(linspace_vector)
print(' ')
print('*'*20)
# Exercise 04: Create arrays using random numbers functions rand, randn and randint
# rand: random numbers between 0 and 1
print('Exercise 04 - Create arrays using random numbers functions rand, randn and randint')
rand_vector = np.random.rand(10)
print('rand: ', rand_vector)
# randn: random numbers with normal distribution which have mean of 0 and standard deviation of 1
randn_vector = np.random.randn(5,5)
print('randn: ', randn_vector)
# randint: random integers between 0 and 10
randint_vector = np.random.randint(1,10,size=(2,5))
print('randint: ', randint_vector)
print(' ')
print('*'*20)
# Exercise 05: Create a 5x5 identity matrix
print('Exercise 05 - Create a 3x3 identity matrix')
identity_matrix = np.eye(5)
print(identity_matrix)
print(' ')
print('*'*20)
# Exercise 06: Create a 3x2 random number matrix and calculate the minimum and maximum value
print('Exercise 06 - Create a 3x2 random number matrix and calculate the minimum and maximum value')
random_matrix = np.random.rand(3,2)
print(random_matrix)
print('Minimum value: ', np.min(random_matrix))
print('Maximum value: ', np.max(random_matrix))
print(' ')
print('*'*20)
# Exercise 07: Create a vector of 30 elements that are random numbers and calculate the mean
print('Exercise 07 - Create a vector of 30 elements that are random numbers and calculate the mean')
random_vector = np.random.randint(5,13,size=30)
print(random_vector)
print('Mean: ', np.mean(random_vector))
print(' ')
print('*'*20)
# Exercise 08: Converts the list [1, 2, 3] and the tuple (1, 2, 3) to arrays
print('Exercise 08 - Converts the list [1, 2, 3] and the tuple (1, 2, 3) to arrays')
list_example = [1,2,3]
tuple_example = (1,2,3)
print('List: ', np.array(list_example))
print('Tuple: ', np.array(tuple_example))
print(' ')
print('*'*20)
# Exercise 09: Invert the vector of the previous exercise (8)
print('Exercise 09 - Invert the vector of the previous exercise (8)')
print('List: ', np.array(list_example)[::-1])
# invert the list using np.flip
print('List: ', np.flip(list_example))
# Exercise 10: Change the size of a random array of dimensions 5x12 into 12x5
print('Exercise 10 - Change the size of a random array of dimensions 5x12 into 12x5')
random_matrix2 = np.random.rand(5,12)
print(random_matrix2)
print(' ')
print('Transpose: ')
print(random_matrix2.T) # or print(np.transpose(random_matrix2)) or using reshape function print(random_matrix2.reshape(12,5))
print(' ')
print('*'*20)
# Exercise 11: Convert the list [1, 2, 0, 0, 0, 4, 0] into an array and get the index of the non-zero elements
print('Exercise 11 - Convert the list [1, 2, 0, 0, 0, 4, 0] into an array and get the index of the non-zero elements')
list_example2 = [1,2,0,0,0,4,0]
print('List: ', np.array(list_example2))
print('Index of non-zero elements: ', np.nonzero(list_example2))
print(' ')
print('*'*20)
# Exercise 12: Convert the list [0, 5, -1, 3, 15] into an array, multiply its values by -2 and obtain the even elements
print('Exercise 12 - Convert the list [0, 5, -1, 3, 15] into an array, multiply its values by -2 and obtain the even elements')
list_example3 = [0,5,-1,3,15]
print('List: ', np.array(list_example3))
print('Multiply by -2: ', np.array(list_example3)*-2)
print('Even elements: ', np.array(list_example3)[::2]) 
print(' ')
print('*'*20)
# Exercise 13: Create a random vector of 10 elements and order it from smallest to largest
print('Exercise 13 - Create a random vector of 10 elements and order it from smallest to largest')
random_vector2 = np.random.randint(1,100,size=10)
print('Random vector: ', random_vector2)
print('Ordered vector: ', np.sort(random_vector2))
print(' ')
print('*'*20)
# Exercise 14: Generate two random vectors of 8 elements and apply the operations of addition, subtraction and multiplication between them
print('Exercise 14 - Generate two random vectors of 8 elements and apply the operations of addition, subtraction and multiplication between them')
random_vector3 = np.random.randint(1,100,size=8)
random_vector4 = np.random.randint(1,100,size=8)
print('Random vector 1: ', random_vector3)
print('Random vector 2: ', random_vector4)
print('Addition: ', random_vector3 + random_vector4)
print('Subtraction: ', random_vector3 - random_vector4)
print('Multiplication: ', random_vector3 * random_vector4)
print(' ')
print('*'*20)
# Exercise 15: Convert the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] into an array and transform it into a matrix with rows of 3 columns
print('Exercise 15 - Convert the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] into an array and transform it into a matrix with rows of 3 columns')
list_example4 = [1,2,3,4,5,6,7,8,9,10,11,12]
print('List: ', np.array(list_example4))
print('Matrix: ')
print(np.array(list_example4).reshape(3,4))
print(' ')
print('*'*20)
