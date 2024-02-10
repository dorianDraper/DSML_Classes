# box contains 10 white balls, 20 red balls and 30 green balls, 5 balls are drawn with replacement
# run experiment 1000 times and calculate the probability of taking 3 white balls and 2 red balls and taking all of the same color
#
import numpy as np

count = 0
for i in range(1000):
    event = np.random.choice(["white", "red", "green"], 5)
    if list(event).count("white") == 3 and list(event).count("red") == 2:
        count += 1
    if list(event).count("white") == 5 or list(event).count("red") == 5 or list(event).count("green") == 5:
        count += 1

print("Probability of taking 3 white balls and 2 red balls: ", count / 1000)
print("Probability of taking all of the same color: ", count / 1000)
#
# find an alternative way to the above code using numpy
#
count = 0
for i in range(1000):
    event = np.random.choice(["white", "red", "green"], 5)
    if np.sum(event == "white") == 3 and np.sum(event == "red") == 2:
        count += 1
    if np.sum(event == "white") == 5 or np.sum(event == "red") == 5 or np.sum(event == "green") == 5:
        count += 1
    
print("Probability of taking 3 white balls and 2 red balls: ", count / 1000)
print("Probability of taking all of the same color: ", count / 1000)