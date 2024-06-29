#Variables length Arguments
def fun1(* args_list):
    ans=[]
    for i in args_list:
        ans.append(i.upper())
    return ans
obj=fun1('python','program','easy')
print(obj)