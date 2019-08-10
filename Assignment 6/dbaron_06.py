# Deana Baron
# GTECH731
#
# Assignment 6: Just trying to get this done since I've spent too long trying to work with netcdf files
# I apologize in advance how simple this is :(

def total(x):
    #Input is a list, output is the sum of all values in the list
    return sum(x)

def largest_elements(x, n):
    #Input is a list and the number of values you want from the list, output is the largest n values from your list
    #Side note: I know there's some way to do this with sort() or sorted(). I want to revisit this
    final_list = []
    for i in range(n):
        max1 = 0

        for j in range(len(x)):
            if x[j] > max1:
                max1 = x[j];

        x.remove(max1);
        final_list.append(max1)

    return(final_list)

#load manhattan building areas text file and load into a list
bldg_areas = []
with open("./manhattan_building_areas.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip() #get rid of the trailing whitespace
        bldg_areas.append(float(line)) #load each area value into a list as a float instead of a string

tot_area = total(bldg_areas)
print (tot_area)

#calculate the percentage of total area taken up by the top 5% of buildings in size
perc5 = int(0.05*len(bldg_areas))
top_5 = largest_elements(bldg_areas, perc5)

z = (sum(top_5) / tot_area) * 100
print (z)

#The percentage of total area taken by the large buildings is a smaller number. This might imply that there are a larger amount of smaller buildings than the
#large buildings we think of in Manhattan

#Plot a histogram
import matplotlib.pyplot as plt

plt.hist(bldg_areas, bins = 20)
plt.show()

#This histogram shows that a vast majority of the buildings in Manhattan are around 1000 to 2000 square feet in area,
#which is about the same size as a small house. Interesting!