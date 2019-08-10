#GTECH731
#Deana Baron
#Assignment 7: Getting at risk buildings of flooding in Manhattan
#Step 1: Find the centroids of the buildings in Manhattan
#Step 2: Extract the values of the DEM raster for each of those points
#Step 3: Find and print out which of these elevations are below a certain storm surge (14 ft was the surge for Sandy)

import arcpy as ap
import os

current_path = os.getcwd()
ap.env.workspace = current_path + "/manh_data"
#ap.env.workspace = "C:\Users\dbaron\PycharmProjects\untitled\manh_data"
ap.env.overwriteOutput = True

#Step 1
#Get the building centroids
output1 = "bldg_centroids.shp"

rows = ap.SearchCursor("manh_bldgs.shp")
pts = []

#PointGeometry class has a function to grab the centroid and append to the empty pts list
for r in rows:
    feat = r.getValue("Shape")
    pts.append(ap.PointGeometry(feat.centroid))

#Save the centroids into a shapefile
ap.CopyFeatures_management(pts, output1)

#Create the spatial reference
sFile = "NAD 1983 StatePlane New York Long Isl FIPS 3104 (US Feet).prj" #Name of the projection we want
sPath = "Coordinate Systems\Projected Coordinate Systems\State Plane\NAD 1983 (US Feet)" #Location of the projection
prjFile = os.path.join(ap.GetInstallInfo()["InstallDir"], sPath, sFile) #Creating the path to the projection file without having to find it

spatialRef = ap.SpatialReference(prjFile)

#Create the shape file with a spatial reference defined
ap.DefineProjection_management(output1, spatialRef)

#Step 2
pts_feat = "bldg_centroids.shp"
raster = "manh_dem.tif"
output2 = "cen_el.shp"

#Spatial Analyst extension needed for this
ap.CheckOutExtension("Spatial")

#Extract the elevation values at the building centroids
#ERROR 010026: Unable to copy dataset C:\Users\dbaron\PycharmProjects\gtech731\manh_data\cen_el.shp to ./manh_data\cen_el.shp.
#What am I doing wrong here? This is exactly how you have it written in your example
ap.sa.ExtractValuesToPoints(pts_feat, raster, output2)

#Step 3
output3 = "bldg_elev.shp"

#Join the centroid elevations with the buildings shapefile
ap.SpatialJoin_analysis("manh_bldgs.shp",output2, output3)

#Print out the building names
rows = ap.SearchCursor(output2, "RASTERVALU <= 14")

for r in rows:
    feat = r.getValue("Shape")
    pnt = feat.getPart()
    print (str(pnt.X), str(pnt.Y))