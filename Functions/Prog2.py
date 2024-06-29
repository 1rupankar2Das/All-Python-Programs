def square(item_list):
    sq=[]
    for i in item_list:
        sq.append(i**2)
    return sq
my_list=[17,52,8]
result=square(my_list)
print("square of the list are: ",result)