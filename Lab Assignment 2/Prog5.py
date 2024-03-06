#WAP that prompts the user for an integer and then prints 
#all the prime numbers less than or equal to that integer. Use nested 
#loops and the concept of prime numbers to accomplish this task.
lower=100
upper=107
print("Prime numbers between",lower,"and",upper,"are:")
for num in range(lower, upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
            else:
                print(num)