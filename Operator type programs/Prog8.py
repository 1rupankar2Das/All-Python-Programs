#WAP to perform addition, subtraction, division, and multiplication on two floating point numbers.
num1=float(input("Enter two numbers: "))
num2=float(input("Enter two numbers: "))
add_res=num1+num2
sub_res=num1+num2
mul_res=num1*num2
div_res=num1/num2
print(str(num1)+" + "+str(num2)+"="+"%.2f"%add_res)
print(str(num1)+" - "+str(num2)+"="+"%.2f"%sub_res)
print(str(num1)+" * "+str(num2)+"="+"%.2f"%mul_res)
print(str(num1)+" / "+str(num2)+"="+"%.2f"%div_res)