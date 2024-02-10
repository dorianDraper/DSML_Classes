import numpy as np
import pandas as pd

# create list named my_list with numbers 1-10
my_list = [1,2,3,4,5,6,7,8,9,10]
double = [x*2 for x in my_list]
print(double)

# create numpy array named my_array with numbers 1-10
my_array = np.array(my_list)
print(my_array)

# create numpy array named my_array2 with numbers 1-10
my_array2 = np.arange(1,11)
print(my_array2)

print(np.mean(my_array2))
# create matrix named my_matrix with numbers 1-10
my_matrix = np.arange(1,11).reshape(2,5)
print(my_matrix)
# create random matrix named my_random_matrix with shape 5,5
my_random_matrix = np.random.rand(3,3)
print(my_random_matrix)
# create list of 10 random people names and using np.random.choice select 1 random names
names = ['Bob','Joe','Will','Jane','Anna','Arthur','Dan','Susana','Maria','Edgar']
print(np.random.choice(names))
# create series with pandas with 10 random integer numbers 
my_series = pd.Series(np.random.randint(0,100,10))
print(my_series)
# create dataframe with pandas with numbers 1-10, 2 columns and 2 rows
my_dataframe = pd.DataFrame(np.arange(1,11).reshape(2,5))
print(my_dataframe)
print(' ')
print('*'*20)
data = {
    'person1' : [1.8, 80, 4],
    'person2' : [1.6, 60, 30],
}
df = pd.DataFrame(data, index=['height', 'weight', 'age'])
print(df)
# describe df 
print(df.describe())
# select person1 height
print(df.loc['height','person1'])
# select person1 height and weight
print(df.loc[['height','weight'],'person1'])
# select person1 height and weight and age
print(df.loc[['height','weight','age'],'person1'])
# create function named square_root that returns square root of a number
def square_root(x):
    return np.sqrt(x)
# apply funciton to df
print(df.apply(square_root))