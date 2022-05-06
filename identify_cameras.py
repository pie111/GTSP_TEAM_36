# Python 3 program to calculate Distance Between Two Points on Earth
from math import radians, cos, sin, asin, sqrt


import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='u934542817_Driver', password='Emergency123', host='sql353.main-hosting.eu', database='u934542817_EmergencyVec')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving single row
sql = '''SELECT * from Camera_Collections'''

#Executing the query
cursor.execute(sql)

#Fetching 1st row from the table
result = cursor.fetchone();
print(result)

#Fetching 1st row from the table
result = cursor.fetchall();
print(result)

#Closing the connection
conn.close()




def distance(lat1, lat2, lon1, lon2):
	
	# The math module contains a function named
	# radians which converts from degrees to radians.
	lon1 = radians(lon1)
	lon2 = radians(lon2)
	lat1 = radians(lat1)
	lat2 = radians(lat2)
	
	# Haversine formula
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

	c = 2 * asin(sqrt(a))
	
	# Radius of earth in kilometers. Use 3956 for miles
	r = 6371
	
	# calculate the result
	return(c * r)
	
	
# driver code
lat1 = 10.0140796
lat2 = 10.0241605
lon1 = 76.3241747
lon2 = 76.3539327
print(distance(lat1, lat2, lon1, lon2), "K.M")




