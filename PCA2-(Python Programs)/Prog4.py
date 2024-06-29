#Write a python program that takes a list of integers as input and returns the sum of all the even numbers in the list.
def sum_even_numbers(nums):
    total=0
    for num in nums:
        if num%2==0:
            total+=num
        return total 
numbers=[1,2,3,4,5,6,7,8,9,10]
print("Sum of even numbers:",sum_even_numbers(numbers))