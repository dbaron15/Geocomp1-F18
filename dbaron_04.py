# Deana Baron
# GTECH731
#
# Assignment 4
#
# Attempting to project from geographic into an orthographic projection?
# Using different geojson data (NYC borough boundaries) since the projection makes no difference on an NYC block scale

import json
import matplotlib.pyplot as plt
import math

earth_circumference_meters = 40075000
radius = earth_circumference_meters / 2.0
center_x = 0.0
center_y = 0.0

def project(pt):
    #load coordinates as decimal degrees from the central meridians
    x = pt[0] - center_x
    y = pt[1] - center_y

    #Orthographic mathematics
    x_new = radius * math.cos(y) * math.sin(x - center_x)
    y_new = radius * ((math.cos(center_y) * math.sin(y)) - (math.sin(center_y) * math.cos(y) * math.cos(x - center_x)))

    return [x_new, y_new]

with open("query.geojson.txt") as f:
    data = f.read()
    d = json.loads(data)
    for feature in d["features"]:
        for i in range(len(feature["geometry"]["coordinates"])):
            if feature["geometry"]["type"] == "Polygon": # if the type is a polygon
                lst = feature["geometry"]["coordinates"][i] # get list of coordinates (one set)
                lst_new = [project(pt) for pt in lst] #project those points
                x = [p[0] for p in lst] #get the longitudes
                y = [p[1] for p in lst] #get the latitudes
                plt.plot(x, y)
            else: #multipolygon with double sets of coordinates?
                for j in range(len(feature["geometry"]["coordinates"][i])):
                    lst = feature["geometry"]["coordinates"][i][j]
                    lst_new = [project(pt) for pt in lst]  # project those points
                    x = [p[0] for p in lst]  # get the longitudes
                    y = [p[1] for p in lst]  # get the latitudes
                    plt.plot(x, y)

    plt.show(block=True) #keeps the plot active and shown

# This projection probably makes more of a difference on a country scale?

# with open("countries.geojson") as f:
#     data = f.read()
#     d = json.loads(data)
#     for feature in d["features"]:
#         for i in range(len(feature["geometry"]["coordinates"])):
#             if feature["geometry"]["type"] == "Polygon": # if the type is a polygon
#                 lst = feature["geometry"]["coordinates"][i] # get list of coordinates (one set)
#                 lst_new = [project(pt) for pt in lst] #project those points
#                 x = [p[0] for p in lst] #get the longitudes
#                 y = [p[1] for p in lst] #get the latitudes
#                 plt.plot(x, y)
#             else: #multipolygon with double sets of coordinates?
#                 for j in range(len(feature["geometry"]["coordinates"][i])):
#                     lst = feature["geometry"]["coordinates"][i][j]
#                     lst_new = [project(pt) for pt in lst]  # project those points
#                     x = [p[0] for p in lst]  # get the longitudes
#                     y = [p[1] for p in lst]  # get the latitudes
#                     plt.plot(x, y)
#
#     plt.show(block=True) #keeps the plot active and shown

# Okay the resulting plot doesn't look orthographic. Maybe my center_x and center_y are different for this sort of projection?