#Create a program that generates a list of squares or cubes of numbers from 1 to n using list comprehension.
def generate_squares_or_cubes(n, mode='square'):
    if mode =='square':
        return[i**2 for i in range(1, n+1)]
    elif mode=='cube':
        return[i**3 for i in range(1, n+1)]
    else:
        return[]
n=int(input("Enter the value of n: "))
mode=input("Enter 'square' to generate square or 'cube' to generate cubes: ")
result=generate_squares_or_cubes(n, mode)
print("List of squares or cubes:", result)
