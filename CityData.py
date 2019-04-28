import numpy as np
from numpy import linalg as LA
import math


def load_city_coordinates():
    return np.loadtxt("coordinates.txt")

def load_city_distances():
    return np.loadtxt("distances.txt")

def create_city_names():
    return np.loadtxt("names.txt", dtype=str, delimiter=", ")

def create_city_coordinates(lat_lon_arr=load_city_coordinates()):
    index = 0
    degrees = np.zeros((len(lat_lon_arr), 2))
    for row in lat_lon_arr:
        first_int = row[0]
        first_min = row[1]
        first_sec = row[2]
        second_int = row[3]
        second_min = row[4]
        second_sec = row[5]
        degrees[index][0] = (first_int + first_min/60 + first_sec/360)
        degrees[index][1] = (second_int + second_min/60 + second_sec/360)
        index += 1
    return degrees


print(create_city_coordinates())
