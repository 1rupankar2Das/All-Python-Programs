#WAP to Program to work with string.
my_string = "Hello, world!"
print("Original string:", my_string)
print("First character:", my_string[0])
print("Last character:", my_string[-1])
substring = my_string[7:]
print("Substring:", substring)
new_string = my_string + " Have a nice day!"
print("Concatenated string:", new_string)
print("Uppercase:", my_string.upper())
print("Lowercase:", my_string.lower())
if "world" in my_string:
    print("Substring 'world' is present in the string")
else:
    print("Substring 'world' is not present in the string")
    words = my_string.split(",")
    print("Words in the string:", words)




