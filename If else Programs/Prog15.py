#WAP to Program to input three numbers and find largest and smallest number.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
largest_num = max(num1, num2, num3)
smallest_num = min(num1, num2, num3)
print("Largest number:", largest_num)
print("Smallest number:", smallest_num)