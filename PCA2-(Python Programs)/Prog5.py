#Write a python program that takes a user-defined input string and checks if it is a palindrome or not.
my_str='Rupankar'
my_str=my_str.casefold()
rev_str=reversed(my_str)
if list(my_str)==list(rev_str):
    print("The string is a palindrome")
else:
    print("The string is not palindrome")