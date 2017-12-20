"""
Compute distance between two points on Earth
"""
from math import acos, cos, sin, radians

AVG_RADIUS = 6371.01

print("Enter lat and long for two points")

# Get Input
lat_1 = float(input("Latitude for point 1: "))
t1 = radians(lat_1)
long_1 = float(input("Longitude for point 1: "))
g1 = radians(long_1)
lat_2 = float(input("Latitude for point 1: "))
t2 = radians(lat_2)
long_2 = float(input("Longitude for point 2: "))
g2 = radians(long_2)

# Compute
distance = AVG_RADIUS * acos(sin(t1) * sin(t2) + cos(t1) *
                             cos(t2) * cos(g1 - g2))

# Display
print(f"Distance between({lat_1}, {long_1}) and ({lat_2}, {long_2}) is \
{distance:.2f} kms")
