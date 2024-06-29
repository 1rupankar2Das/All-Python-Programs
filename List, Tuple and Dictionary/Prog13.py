#Dictionary 
#Write a python program to find the highest 2 values in a dictionary 
n={31:111,22:222,43:333,14:444,25:555}
S=sorted(n.values())
print("Given dictionary is:",n)
print("Highest two values of given dictionary are:",S[-1],S[-2]) 