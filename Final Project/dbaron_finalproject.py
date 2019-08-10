#SDSS AHP implementation

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

print ("Welcome to Deana's GTECH731 Final Project!")
print ("Part 0: Load the raster criteria")
#Load the rasters into Python as numpy arrays using arcpy

#I struggled with this immensely, therefore I'm generating random numpy arrays just to get this up and running

vesseldens = np.random.randint(0, 50, size=(3000,3000))
meanfishingrev = np.random.randint(0, 20000, size=(3000,3000))
cetaceanabun = np.random.randint(0, 1700, size=(3000,3000))

print ("Done!")

#Construct reciprocal matrix by hand for which all pairwise comparisons will be stored
#The criterion versus itself will have a comparison value of 1
pairwise_matrix = np.array([[1, 0, 0],
                            [0, 1, 0],
                            [0, 0, 1]], dtype=float)

print ("How much more important is one criterion versus another on a scale of 1 to 9?")
print ("AHP Scale: 1- Equal Importance, 3- Moderate importance, 5- Strong importance, 7- Very strong importance, 9- Extreme importance (2,4,6,8 values in-between).")
print ("If the latter criterion is more important than the former, use the inverse of each importance ranking, ie: 1/9 means that the former is much less important than the latter.")

#Get the numerical ranking for each criterion to figure out which is more important and by how much and input into appropriate matrix column
pairwise_matrix[0,1] = float(input("Criterion 1 vs Criterion 2?: "))
pairwise_matrix[0,2] = float(input("Criterion 1 vs Criterion 3?: "))
pairwise_matrix[1,2] = float(input("Criterion 2 vs Criterion 3?: "))

print ("Thank you, constructing pairwise matrix...")

#Compute the reciprocal of the matrix which is just the inverse of what is already in the matrix
pairwise_matrix[1,0] = 1 / (pairwise_matrix[0,1])
pairwise_matrix[2,0] = 1 / (pairwise_matrix[0,2])
pairwise_matrix[2,1] = 1 / (pairwise_matrix[1,2])

print pairwise_matrix

print ("Part 2: Computing the weights for each criterion")

#Determine the weights for the criteria based on pairwise matrix
eigenvalues, eigenvector = np.linalg.eig(pairwise_matrix) #Calculate the eigenvectors and eigenvalues of the matrix
maxindex = np.argmax(eigenvalues) #Returns the location of the maximum eigenvalue
weights = eigenvector.real[:, maxindex] #Extract the eigenvectors where the maximum eigenvalue is found

weights = weights/np.sum(weights) #Normalize the weights (sum of weights = 1)

print ("Layer Weights: " + str(np.around(weights,3)))

print ("Part 3: Applying the weights to each criterion")
#Apply each weight to the raster
crit1 = vesseldens * weights[0]
crit2 = meanfishingrev * weights[1]
crit3 = cetaceanabun * weights[2]

cumulativeuse = crit1 + crit2 + crit3 #linear combination of criteria

print ("Done making cumulative use raster.")

#Find max and minimum values in the raster to get the range of use classes
max_use = np.max(cumulativeuse)
print(max_use)
min_use = np.min(cumulativeuse)
print(min_use)

lowperc = np.percentile(cumulativeuse, 25) #Find the value that represents the 25th percentile of the data

#Reclassify raster based on 25th percentile
cumulativeuse[cumulativeuse < lowperc] = 1 #Values less than 25th percentile are "low use"
cumulativeuse[cumulativeuse > lowperc] = 0 #All other values that we don't care about

print(cumulativeuse)

print ("Done making low use raster.")

plt.plot(cumulativeuse)
plt.show(block=True)
