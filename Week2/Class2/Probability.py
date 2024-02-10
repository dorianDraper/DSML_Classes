import numpy as np


# event = np.random.choice(dice, 2)
# print(event)

# for i in range(10):
#     event = np.random.choice(dice)
#     print("Throw ", i + 1, ": ", event)

# dice = [1, 2, 3, 4, 5, 6]

# count_dices = {}

# for i in range(10): 
#     event = np.random.choice(dice)
#     if event in count_dices:
#         count_dices[event] += 1
#     else:
#         count_dices[event] = 1

# print(count_dices)

# 2 dices are thrown once and the sum is calculated, run 1000 times and sum the number of both dices in a dictionary
# keep track of the number of times the sum is greater than 7 or an even number
# print the probability of the sum being greater than 7 or an even number

dice = [1, 2, 3, 4, 5, 6]

count_dices = {}
count_greater_than_7 = 0
count_even = 0

for i in range(1000):
    event = np.random.choice(dice, 2)
    sum_event = sum(event)
    if sum_event in count_dices:
        count_dices[sum_event] += 1 # count_dices[sum_event] = count_dices[sum_event] + 1
    else:
        count_dices[sum_event] = 1
    if sum_event > 7:
        count_greater_than_7 += 1
    if sum_event % 2 == 0:
        count_even += 1

print(count_dices)
print("Probability of the sum being greater than 7: ", count_greater_than_7 / 1000)
print("Probability of the sum being an even number: ", count_even / 1000)
