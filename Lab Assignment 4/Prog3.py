#WAP that concatenates two lists and removes duplicates,then sorts the resulting list.
def concatenate_and_sort_lists(list1, list2):
    concatenated_list=list1+list2
    unique_list=list(set(concatenated_list))
    sorted_list=sorted(unique_list)
    return sorted_list
list1=[1,3,5,7]
list2=[2,4,6,7]
result=concatenate_and_sort_lists(list1, list2)
print("concatenated, unique, and sorted list:",result)
