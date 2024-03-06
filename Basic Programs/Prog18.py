#WAP to calculate the distance between two points.
x1=(int(input("Enter the x coordinate of the first point: ")))
y1=(int(input("Enter the y coordinate of the first point: ")))
x2=(int(input("Enter the x coordinate of the second point: ")))
y2=(int(input("Enter the y coordinate of the second point: ")))
distance=((x2-x1)**2+(y2-y1)**2)**0.5
print("Distance= ")
print(distance)
