from Earthquake import EarthClass
import sqlite3
import pandas as pd

conn = sqlite3.connect('earthquake2.sqlite')
# # forces database to return strings for TEXT attributes 
conn.text_factory = str 
cur = conn.cursor()
# # get the cursor for the connection 
cur.execute('''SELECT EarthQuake.earth_ID, earth_place, earth_region, earth_mag, earth_dep FROM EarthQuake''')
#executing sql table to load data in variable CUR
earth_list = [] #creating a list
for x in cur: #reading and appending earth quakes categoires from database
    earth_list.append(EarthClass(x[1], x[2], x[3], x[4])) 

# print(earth_list[0],'\n')
# print(earth_list[1],'\n') --> checking if earth quakes have been loaded in as members of a list

df = pd.DataFrame([earth_quake.to_dict() for earth_quake in earth_list]) 
#using data frame we can put the data in a structure and create a 2 Dimensional Data Plane 
#with data frame we will be using heads and tails method as well providing basic stastics for data below ↓
#setting eeart_quake to a dictionary for all the earth quakes in earth_list

print('Heads')
print(df.head(),'\n')
# print('Tails') --> displaying the last 5 earth quakes
# print(df.tail(),'\n')

print("Basic Stats for Earth Quakes ↓")
print(df.describe()) # .describe is describing basic stats like the count, mean and standard dev etc...

stats_CA = df[df.earth_region == "California"]
print("\nCalifornia")
print(stats_CA.describe())
stats_AL = df[df.earth_region == "Alaska"] #--> computing basic statistics for 2 regions, Alaska and Californa and using j describe to provide the basic statisitcs
print("\nAlaska")
print(stats_AL.describe())

dep_stats = df[df.earth_dep < 50] #computing basic stastics of the depth of earth quakes with a deoth less than 50
print("\nDepth less than 50")#using <50 it will show the statiscs for the earth quakes with depth less than 50
print(dep_stats.describe())
