#Create a Python program that checks if a given string is a 
#palindrome or not. A palindrome is a word, phrase, number, or other 
#sequence of characters that reads the same forward and backward.
my_str='ama'
my_str=my_str.casefold()
rev_str=reversed(my_str)
if list(my_str)==list(rev_str):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")