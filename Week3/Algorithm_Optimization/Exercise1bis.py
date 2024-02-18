import numpy as np
import string
import math

# the following code is the original code that needs to be optimized. It performs the following tasks:
# 1. filter out even numbers
# 2. duplicate each number
# 3. add all numbers
# 4. check if the result is prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def process_list(list_):
    filtered_list = []
    for num in list_:
        if num % 2 == 0:
            filtered_list.append(num)
    
    duplicate_list = []
    for num in filtered_list:
        duplicate_list.append(num * 2)
        
    sum = 0
    for num in duplicate_list:
        sum += num

    prime = is_prime(sum)
    
    return sum, prime

list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result, result_prime = process_list(list_)
print(f"Result: {result}, ¿Prime? {'Yes' if result_prime else 'No'}")
# given the above code, write another function that performs the same tasks but using optimized code
# the optimized code should be more efficient and concise
# the optimized code should use the following libraries: numpy
# the optimized code should not use any for loops
# the optimized code should not use any if statements
# the optimized code should not use any dictionaries
# the optimized code should not use any lists

def process_list_optimized(list_):
    list_ = np.array(list_)
    filtered_list = list_[list_ % 2 == 0]
    duplicate_list = 2 * filtered_list
    sum = np.sum(duplicate_list)
    prime = is_prime(sum)
    return sum, prime

result, result_prime = process_list_optimized(list_)
print(f"Result: {result}, ¿Prime? {'Yes' if result_prime else 'No'}")
