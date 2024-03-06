#WAP m that checks whether a given character is a 
#vowel or a consonant. Prompt the user to enter a character and then 
#display whether it is a vowel or a consonant.
character=input("Enter a character: ")
vowels=['a','e','i','o','u','A','E','I','O','U']
if character in vowels:
    print(f"The character'{character}'is a vowel")
else:
    print(f"The character'{character}'is a consonant")
