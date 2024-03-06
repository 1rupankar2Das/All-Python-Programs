# Wap to Krishnamurthy Number in Python
import math
number=int(input("Enter the Number to check Krishnamurthy Number="))
Temp=number
Sum=0
while Temp>0:
    fact=1
    i=1
    rem=Temp%10
    fact=math.factorial(rem)
    Sum=Sum+fact
    Temp=Temp//10
if Sum==number:
    print("%d is a Krishnamurthy Number."%number)
else:
    print("%d is not a Krishnamurthy number."%number)