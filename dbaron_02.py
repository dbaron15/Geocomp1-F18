# Deana Baron
# GTECH731 Assignment 2
#
# Psuedocode for Part 3 of Assignment 1
#
# Coding the formula for population variance
#     1. Input is a list of numbers from the population
#     2. Add all numbers together
#         a. Divide by the number of numbers in that list
#         b. Call this value the average
#     3. For each number in the list:
#         a. Subtract the average from the given number
#         b. Multiply the result by itself
#         c. If there is a number before it in the list:
#                 i. Add this number to the previous number in the list
#                 ii. Else, add
#     4. Divide the result by the number of numbers in the list
#     5. Output is the population variance
#
# Part 2 for Assignment 2 is at the bottom of this file


def pop_var(L):
    avg = sum(L) / len(L) # Find the mean of the elements in the list
    float(avg)

    s = 0.0 # Set counter for summation loop

    # Loop to iterate over x, representative of Step 3 above but more succinct
    for i in range(len(L)):
        s += ((L[i] - avg) ** 2)

    pv = s / len(L) # divide the resulting summation by the length of list x
    return (pv)

#Test the function
x = [2.0, 545, 665, 33, 4306, 21, 98, 809] # Get the input of numbers

test = pop_var(x)
print(test)

# Let's try using random numbers and plotting the difference in population variance vs. the number of samples
# I hard coded this because I struggled :(

import random
import matplotlib.pyplot as plt  #Keep getting ImportError: No module named 'matplotlib' but this is a lab computer?

r = [10, 100, 1000, 10000, 100000, 1000000] #different ranges used to plot scatter

#Generate random numbers using different number of samples
a = [random.gauss(0.5,0.1) for i in range(10)]
b = [random.gauss(0.5,0.1) for j in range(100)]
c = [random.gauss(0.5,0.1) for k in range(1000)]
d = [random.gauss(0.5,0.1) for m in range(10000)]
e = [random.gauss(0.5,0.1) for n in range(100000)]
f = [random.gauss(0.5,0.1) for p in range(1000000)]

#Get the population variance
a_v = pop_var(a)
b_v = pop_var(b)
c_v = pop_var(c)
d_v = pop_var(d)
e_v = pop_var(e)
f_v = pop_var(f)

#Compile into a list
v = [a_v, b_v, c_v, d_v, e_v, f_v]

# Below is how you would plot it I guess but the lab computers aren't recognizing the module?
plt.scatter(r,v) #Number of samples vs pop variance?
plt.show()

# Hi Dr. Green, I really struggled writing the code for this!
# My intention was to have a list of ranges, and using that list, create another list with each item as a random generated list.
# This list would then be iterated over to form a new list with each variance for each random list
# Then I would like to plot this as a scatter plot (number of samples vs. pop variance)
# Somewhere my logic is failing! I appreciate any feedback!
#
# r = [10, 100, 1000, 10000, 100000, 1000000] #different ranges used to plot scatter
#
# for i in a[i]:
#     a[i] = [random.gauss(0.5, 0.1) for j in range(r[i])]
#
# for k in a:
#         v[k] = pop_var(a[i])


# Part 2 of Assignment 2
#
# Averages of raster data
# Rasters are defined as an array with dimensions of x and y (coordinates) and a value that corresponds to what each cell represents
# You can calculate the averages of multiple rasters, which will give an average value of each cell
# *The most important thing when averaging rasters is making sure they align and making sure they're all in the same extent and resolution
#
# Psuedocode for averaging rasters (?)
# 1. Input is a set of rasters
# 2. If each raster is equal in pixel size and boundaries:
#     a. Continue forward
#     b. If not, stop! You can't really compute a working average raster
# 3. For each pixel value in each raster:
#     a. Add each overlaying pixel value
#         i. This is the summed raster
# 4. For each pixel in the summed raster:
#     a. Divide by the number of input rasters
# 5. Output is the average raster


