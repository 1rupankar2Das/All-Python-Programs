#WAP to determine digit, Uppercase, lowercase character is entered by the user.
ch=input("Please Enter Your Own Character: ")
if(ch.isupper()):
    print("The given character",ch,"is an Uppercase Alphabet")
elif(ch.islower()):
    print("The given character",ch,"is a Lowercase Alphabet")
else:
    print("The given character",ch,"is not a Lowercase or Uppercase Alphabet")