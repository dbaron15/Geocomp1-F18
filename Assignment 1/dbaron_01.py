# Deana Baron
# GTECH73100
#
# Results of the code below (Part 2 of Assignment 1) [*Part 3 is below my code]
#
#     Hi, Dr. Green! My name is Deana Baron, and I am a first year M.S. GeoInformatics student.
#     I graduated with my B.S. in marine science and a GIS minor, and I'm mostly interested in computational
#     approaches for oceanographic questions, especially ecological in nature. I've used Postgresql and PostGIS
#     before for a spatial database class, and I've done remote sensing analysis with Matlab. I don't have too much
#     coding experience besides that. Excited for this class!
#     ******************************************************************************
#     My OS version of Windows is 10.0.17134 and my Python version is 2.7.14.

import platform # Platform module

os_type = platform.system() # Obtain type of OS on my computer

os_vers = platform.version() # Obtain the OS version on my computer

python_vers = platform.python_version() # Obtain the version of Python installed on my machine

# Print some information about me!
print("Hi, Dr. Green! My name is Deana Baron, and I am a first year M.S. GeoInformatics student.")
print("I graduated with my B.S. in marine science and a GIS minor, and I'm mostly interested in computational")
print("approaches for oceanographic questions, especially ecological in nature. I've used Postgresql and PostGIS")
print("before for a spatial database class, and I've done remote sensing analysis with Matlab. I don't have too much")
print("coding experience besides that. Excited for this class!")

print("******************************************************************************")

# Print some information about my system
print("My OS version of " + os_type + " is " + os_vers + " and my Python version is " + python_vers + ".")

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
