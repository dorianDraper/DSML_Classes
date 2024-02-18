import numpy as np
import string

def process_text(text):
    # Text to lowercase
    text = text.lower()
    # Remove punctuation
    for p in string.punctuation:
        text = text.replace(p, "")
    # Split text into words
    words = text.split()
    # Count frecuencies
    frequencies = {}
    for w in words:
        if w in frequencies:
            frequencies[w] += 1
        else:
            frequencies[w] = 1
    sorted_frequencies = sorted(frequencies.items(), key = lambda x: x[1], reverse = True)
    # Get 5 most-common words
    top_5 = sorted_frequencies[:5]    
    for w, frequency in top_5:
        print(f"'{w}': {frequency} times")

text = """
    In the heart of the city, Emily discovered a quaint little café, hidden away from the bustling streets. 
    The aroma of freshly baked pastries wafted through the air, drawing in passersby. As she sipped on her latte, 
    she noticed an old bookshelf filled with classics, creating a cozy atmosphere that made her lose track of time.
"""
process_text(text)
print('*'*50)
# given the above code, write another function that performs the same tasks but using optimized code
# the optimized code should be more efficient and concise
# the optimized code should use the following libraries: numpy, string
# the optimized code should not use any for loops
# the optimized code should not use any if statements
# the optimized code should not use any dictionaries
# the optimized code should not use any lists
# the optimized code should not use any list methods

def process_text_optimized(text):
    text = text.lower() # Text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))    # Remove punctuation 
    words = np.array(text.split())  # Split text into words
    unique, counts = np.unique(words, return_counts=True) # Count frequencies using numpy arrays and numpy functions
    sorted_indices = np.argsort(-counts) # Sort the frequencies in descending order
    top_5 = unique[sorted_indices[:5]] # Get 5 most-common words
    counts_top_5 = counts[sorted_indices[:5]] # Get the frequencies of the 5 most-common words
    for w, frequency in zip(top_5, counts_top_5): # Print the 5 most-common words and their frequencies
        print(f"'{w}': {frequency} times")  

process_text_optimized(text)
# the optimized code should produce the same output as the original code
# the optimized code should have a time complexity of O(nlogn) and a space complexity of O(n)
# the optimized code should be more efficient than the original code
# the optimized code should be more concise than the original code
# the optimized code should be more readable than the original code
# the optimized code should use the following libraries: numpy, string












