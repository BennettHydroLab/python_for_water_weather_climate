# %%
# This set of exercises works through
# some basic python functionality
# I'll still be using some functions from 
# numpy but nothing you write should need it
# although you can use it if you'd like
import numpy as np

# %%  1.)
# Write code to translate a boolean value
# to a string. Specifically, if the `testval` 
# is `True` then print "Yes" and if it is
# `False` then print "No"
testval = bool(np.random.choice([0, 1]))
# TODO: Your code here
message = None
# ...
print(message)

# %% 2.)
# You will be given a random integer, and 
# your goal is to return the same value, but
# as a negative number. Notice, the number you
# are given may already be negative
testval = np.random.random_integers(-100, 100)
# TODO: Your code here
negval = None
print(testval, negval)

# %% 3.)
# Given a list of random integers, return them
# sorted from low to high. 
# NOTE: I do not want you to write your own
#       sorting algorithm, but want you to 
#       look up how to do this using the 
#       python standard library
random_vals = np.random.random_integers(-100, 100, 10)
# TODO: Your code here
sorted_vals = None
print(sorted_vals)

# %% 4.)
# Given a list of US locations with the format:
# "CityName, StateAbbrev" filter out any that
# are not in Arizona (AZ).
city_list = [
    "New York, NY",
    "Chattanooga, TN",
    "Hobart, MN",
    "Kingman, AZ",
    "Yachats, OR",
    "Bisbee, AZ",
    "Muskogee, OK"
]
#TODO: Your code here
az_list = None
#...
print(az_list)

# %% 5.)
# This code doesn't work - can you fix it?
def multiply(a, b):
    # TODO: Your code in here
    a * b

print(multiply(5, 10))

# %% 6.)
# Time for a coding interview classic, FizzBuzz
# The rulse of the game:
#  - print numbers from 1 to 100
#  - if the number is divisible by 3 print "Fizz"
#  - if the number is divisible by 5 print "Buzz"
#  - if the number is divisible by both 3 and 5 print "FizzBuzz"
#  - otherwise, print the number
testvals = np.arange(1, 101)
#TODO: Your code here
# ...
for v in testvals:
    print('NONE')

# %%
