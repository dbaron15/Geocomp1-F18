# Deana Baron
# GTECH731
#
# Assignment 3
#
# Attempting to create the Diamond District in NYC using geojson data

import json #import appropriate library

#load, open, and convert the geojson file to a python dictionary
with open("pluto.geojson") as f:
    data = f.read()
    d = json.loads(data)
    for features in d["features"]: #reverse points for valid geojson (is this valid here?)
        pts = features["geometry"]["coordinates"][0][0]
        x = [p[0] for p in pts]
        y = [p[1] for p in pts]

#obtain the list of attributes for building area and lot area from geojson
BA = [features["properties"].get("bldgarea") for features in d["features"]]
LA = [features ["properties"].get("lotarea") for features in d["features"]]

#sum up building area and lot area
sBA = sum(BA)
sLA = sum(LA)

sBA /= 1.0 #for some reason the float() command wasn't working

tot_area = sBA + sLA #calculate the total area of the neighborhood

built_ratio = sBA / tot_area #calculate the built area ratio (this would be built space/total space right?)

#calculate the center point of the neighborhood
#this works, but the resulting coordinates are not the center of the neighborhood? not sure what I did wrong
avg_x = sum(x) / len(x)
avg_y = sum(y) / len(y)

#pseudocode for calculating center point using building volume?
# 1. Extract numfloors from geojson file into a list
# 2. Sum the total number of floors in the area
# 3. For each tax lot:
#     i. Divide the number of floors by the total number of floors in the area
#     ii. Multiply this value by the X coordinate(s) for the lot
#     iii. Multiply this value by the Y coordinate(s) for the lot
# 4. Sum the list of X coordinates and Y coordinates
# 5. Divide each by the number of tax lots
# 6. Output is the weighted center of the lot (?)

#compile and export new valid geojson data

g = {
    "type": "Feature",
    "geometry": {
        "type": "Point",
        "coordinates": [avg_x, avg_y]
    },
    "properties": {
        "name": "Diamond District",
        "total_area": tot_area,
        "built_area_ratio": built_ratio
    }
}

diam_dist = json.dumps(g)

print(diam_dist)