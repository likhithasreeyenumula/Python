import math
r=float(input("Enter radious of cones:"))
h=float(input("Enter height of cone:"))
l=math.sqrt((h*h)+(r*r))
volume=(1/3)*math.pi*(r*r)*h
TSA=math.pi*r*(l*r)
print("volume of cones:",volume)
print("Total surface area of cones:",TSA)