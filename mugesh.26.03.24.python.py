
##a = [1, 2, 3, 4, 5]
##b = [10, 6, 7, 8, 9]
##print(any(i in b for i in a))


##list1=[1,2,1,3,2,1,4,5,5]
##frequancy={}
##for i in list1:
##    if i in frequancy:
##        frequancy[i]+=1
##    else:
##        frequancy[i]=1
##print(frequancy)        


##list1=[1,2,3,4,5]
##list2=[2,3,6,7,8]
##list3=[]
##for i in list1:
##    if i not in list2:
##        list3.append(i)
##print(list3)        

list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
list=set(list1) & set(list2)
print(list)
        
