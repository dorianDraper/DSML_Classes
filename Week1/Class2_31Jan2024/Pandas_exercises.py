import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Exercise 1: create  a series with numbers 1 to 5 and index as a,b,c,d,e
serie = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(serie)
# access the 3rd element of the series by index and by position
print(serie['c']) # by index
print(serie[2]) # by position
# access 3rd element using ser.iloc
print(serie.iloc[2])
# change the value of the second element
serie['b'] = 10
print(serie)
# add 10 to all elements
serie = serie + 10
print(serie)
# calculate the sum of the elements
print(serie.sum())
print(' ')
print('*'*20)
# Exercise 2: create dataframe with 3 columns and 3 rows with numbers 1-9
df = pd.DataFrame(np.arange(1,10).reshape(3,3))
print(df)
print(' ')
# change the index to a,b,c and the columns to col A, col B, col C
df.index = ['a','b','c']
df.columns = ['col A','col B','col C']
print(df)
# access all the data in a column by index, by column name and by position
print(df['col A']) # by column name
print(df.iloc[:,0]) # by position
print(df.loc[:,'col A']) # by index
print(' ')
# acces to specific element (row, column)
print(df.iloc[1,1]) # by position
print(df.loc['b','col B']) # by index
print(' ')
# create new column with name col D and values 10, 11, 12
df['col D'] = [10,11,12]
print(df)
# create new row with index d and values 13, 14, 15
df.loc['d'] = [13,14,15,16]
print(df)
# add 10 to elements in column col A
df['col A'] = df['col A'] + 10
print(df)
# calculate the sum of all elements 
print(df.sum())
# delete column using drop
df = df.drop('col D', axis=1)
print(df)
print(' ')
# for c in df.columns:
#     print(df[c]) # or print(c) or print(df.loc[:,c])
print('Functions')
# Given below Series and DataFrame, perform some operations
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
d1 = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
d2 = pd.DataFrame([[7, 8, 9], [10, 11, 12]])
# Sum all series
print(s1.add(s2)) # or print(s1 + s2)
# Sum all dataframes
print(d1.add(d2)) # or print(d1 + d2)
# calculate mean for s1
print('Mean: ', s1.mean())
# calculate median for s1
print('Median: ', s1.median())
# count number of elemetns in s1
print('Count: ', s1.count())
# calculate standard deviation for s1
print('Standard deviation: ', s1.std())
# calculate variance for s1
print('Variance: ', s1.var())
# calculate maximum value for s1
print('Maximum value: ', s1.max())
# calculate minimum value for s1
print('Minimum value: ', s1.min())
# calculate correlation between s1 and s2
print('Correlation: ', s1.corr(s2))
# statistic summary for s1
print('Statistic summary: ', s1.describe())
# Custom Functions
# define a serie with numbers 1-5
s = pd.Series([1,2,3,4,5])
# define a square function and apply it to the serie
def squared(x):
    return x**2

s= s.apply(squared)
print(s)
# same as above but using lambda function
s = pd.Series([1,2,3,4,5])
s = s.apply(lambda x: x**2)
print(s)
# define a dataframe with numbers 1-6
df = pd.DataFrame({
    'A': [1,2,3],
    'B': [4,5,6]
})
# apply lambda function to column A
df['A'] = df['A'].apply(lambda x: x**2)
print(df)
# apply lambda function to row 1
df.iloc[0] = df.iloc[0].apply(lambda x: x**2)
print(df)
# apply lambda function to all elements in the dataframe
df = df.applymap(lambda x: x**2)
print(df)