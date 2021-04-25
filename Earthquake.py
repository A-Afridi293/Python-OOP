import sqlite3
import pandas as pd

class EarthClass: #creating basic class
    
    def __init__(self,earth_place,earth_region,earth_mag,earth_dep): #creating constructor
        self.earth_place = earth_place #setting all of the values in constructor using .self
        self.earth_region = earth_region 
        self.earth_mag = earth_mag
        self.earth_dep = earth_dep
    
    @property
    def earth_placecounts(self):
        return self.__earth_place #one private property that is counts of places
    
    @earth_placecounts.setter #having a setter to validate the private property
    def earth_placecounts(self):
        print(self.__earth_place.isnumeric())
    def to_dict(self): #the converting to dictionary method we will be calling in Earthquake_stats.py
        return vars(self)


        
    def __str__(self): #overiding string method
        return f"Place: {self.earth_place}\nRegion:{self.earth_region}\nMagnitude:{self.earth_mag}\nEarthquake depth:{self.earth_dep}"
        #reasonable string representation of an Earthquake

class Position:# creating second class called position
    def __init__(self, earth_lng, earth_lat):
        self.earth_lng = earth_lng
        self.earth_lat = earth_lat
    def __str__(self):
        return f"Longitude: {self.earth_lng}\n Latitude:{self.earth_lat}\n"

# t = EarthClass(1,2,3,4,5,6)
# print(str(t)) just to test string override when it comes to printing a reasonable string representation of an earthquake
