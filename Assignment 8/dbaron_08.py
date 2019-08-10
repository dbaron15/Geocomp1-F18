#Deana Baron
#GTECH731
#Assignment 8: Do something with PostGIS

import psycopg2
import json

#input is a polygon, which is a list of point tuples or lists
#for simplicity sake, input only supports rectangle polygons (4 sets of point pairs and a final set to show it's closed)
def intersecting_bldgs(poly):

    #postgres query - select addresses that intersect an input polygon
    #polygon elements are being put into the query manually and converted to strings, not sure if there's an easy way
    query = "SELECT address, ST_AsGeoJSON(ST_Transform(geom, 4326)) FROM mnmappluto WHERE ST_Intersects(geom, ST_Transform(ST_GeomFromText('POLYGON(" + "(" + str(poly[0][0]) + " " + str(poly[0][1]) + "," + str(poly[1][0]) +" "+ str(poly[1][1]) + "," + str(poly[2][0]) +" "+ str(poly[2][1]) + "," + str(poly[3][0]) +" "+ str(poly[3][1]) + "," + str(poly[4][0]) + " " + str(poly[4][1]) + "))', 4326), 2263))"

    #set up postgis connection
    conn =  psycopg2.connect(host="localhost", database="dbaron", user="postgres", password="postgres")

    #select statement with cursor and execute it
    cursor = conn.cursor()
    cursor.execute(query)

    #get all the results and create blank python dictionary for GeoJSON
    rows = cursor.fetchall()
    results = {"type": "FeatureCollection","features": []}

    #loop through results to load into the dictionary then close the postgis connection and cursor
    for row in rows:
        s = row[1]
        obj = json.loads(s)
        results["features"].append({ "type": obj["type"], "geometry": obj["coordinates"][0], "properties": { "address": row[0]} })
    cursor.close()
    conn.close()

    json.dumps(results)

    return (results)


#Let's test this monstrosity
#Input polygon is in midtown, 4 sets of point pairs + first point to show closed ring

poly = [[-73.987255096441, 40.762538909912], [-73.984680175787, 40.769748687744], [-73.975582122808, 40.765628814697], [-73.978672027593, 40.760478973389], [-73.987255096441, 40.762538909912]]

some_bldgs = intersecting_bldgs(poly)

print(some_bldgs)
#yay it works!
