#Variable length arguments
def fun1(**kwargs_list):
    ans=[]
    for key, value in kwargs_list.items():
        ans.append([key,value])
    return ans
obj=fun1(First="Python",Second="program",Third="easy")
print(obj)