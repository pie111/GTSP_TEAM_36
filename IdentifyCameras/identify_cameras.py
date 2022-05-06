from math import radians, cos, sin, asin, sqrt
from numbers import Real
import mysql.connector

#configuring mysql database
conn = mysql.connector.connect(
   user='u934542817_Driver', password='Emergency123', host='sql353.main-hosting.eu', database='u934542817_EmergencyVec')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Query to fetch details from the database
sql = '''SELECT * from Camera_Collections'''

#Executing the query
cursor.execute(sql)

#To display data retrieved from database
result = cursor.fetchall()
print(result)

#Closing the connection
conn.close()

def distance(ambulance_latitude, camera_latitude, ambulance_longitude, camera_longitude):
	# To convert degrees to radians.
	ambulance_longitude = radians(ambulance_longitude)
	camera_longitude = radians(camera_longitude)
	ambulance_latitude = radians(ambulance_latitude)
	camera_latitude = radians(camera_latitude)
	dlon = camera_longitude - ambulance_longitude
	dlat = camera_latitude - ambulance_latitude
	a = sin(dlat / 2)**2 + cos(ambulance_latitude) * cos(camera_latitude) * sin(dlon / 2)**2
	c = 2 * asin(sqrt(a))
	r = 6371
	return(c * r)
	


#function to find coordinates of upcoming cameras
def identify_cam(result):
	for i in result:
		if distance(ambulance_latitude, i[1], ambulance_longitude, i[2]) < 3:
			print(i[1],i[2])
	


# variables that takes coordinates of ambulance
ambulance_latitude = 10.0140796
ambulance_longitude = 76.3241747
identify_cam(result)



