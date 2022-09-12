import numbers
import random

# ...............between zero and 1
print(random.random())

# ....... between two arbitrary number 
print(random.randint(1, 5))

# ........ Randomly choose between list names & using k to indicate range list
print(random.choices([1,2,3,4,5,6,7,8,9], k=4))

#  Shuffling a list 
numbers = [*range(1,  30)]
random.shuffle(numbers)
print(numbers)