#Write a python program that create a list and print the largest and smallest number in the list. 
lst=[]
num=int(input('How many numbers: '))
for i in range(num):
    numbers=int(input('Enter number: '))
    lst.append(numbers)
print("Maximum element in the list is:",max(lst),"\nMinimum element in the list is:",min(lst))