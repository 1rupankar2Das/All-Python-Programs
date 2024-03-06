#WAP to take input of 3 numbers and find smallest number using nested if-else statement.
def smallest(x,y,z):
    if x<=y and x>=z:
        min=x
    elif y<=x and y<=z:
        min=y
    else:
        min=z
        print("Smallest number among",x,",",y,"and",z,"is:",min)
    smallest(100,50,25)
    smallest(50,50,25)