list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
def add(list1,list2):
    return list1+list2
print(list(map(add,list1,list2)))
