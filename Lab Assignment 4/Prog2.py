#Create a program that takes a list of strings as input and filters out 
#words that contain a specific letter or have a length less than a given 
#threshold.
test_list=['Rupankar','is','a','student']
print("The original list: "+str(test_list))
thres=4
res=[ele for ele in test_list if len(ele)>=thres]
print("The above Threshold size strings are: "+str(res))
