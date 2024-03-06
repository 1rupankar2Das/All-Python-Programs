#WAP that prompts the user to enter a string and then 
#counts and prints the number of vowels (a, e, i, o, u) in that string. Use 
#a loop to iterate through each character in the string and count the 
#vowels.
example="Count number of vowels in a String in Python"
count=0
i=0
for i in range(len(example)):
    if((example[i]=="a")
       or (example[i]=="e")
       or (example[i]=="i")
       or (example[i]=="o")
       or (example[i]=="u")
       ):
        count+=1
print("Number of vowels in the given string is: ",count)