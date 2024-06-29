# Write a program that takes two tuples of integers as input and returns 
# a tuple containing the element-wise sum of the corresponding elements 
# of the input tuples.
def tuple_sum(tuple1,tuple2):
    return tuple(x+y for x,y in zip(tuple1,tuple2))
tuple1=(1,2,3)
tuple2=(4,5,6)
result=tuple_sum(tuple1,tuple2)
print(result)