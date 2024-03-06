#WAP that program that checks whether a given year is a leap 
#year or not. Prompt the user to enter a year and then display whether 
#it is a leap year or not.
year=int(input("Enter a year: "))
if year % 4==0:
    if year % 100==0:
        if year % 400==0:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is not a leap year")