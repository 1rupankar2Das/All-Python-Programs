#WAP  program that checks whether a given set of three 
#numbers can form a valid triangle and if so, whether it is an 
#equilateral, isosceles, or scalene triangle. Prompt the user to enter 
#three numbers and then display the type of triangle.
print("Input lengths of the triangle sides: ")
x=int(input("x: "))
y=int(input("y: "))
z=int(input("z: "))
if x==y==z:
    print("Equilateral triangle")
elif x==y or y==z or z==x:
    print("Isosceles triangle")
else: 
    print("Scalene triangle")