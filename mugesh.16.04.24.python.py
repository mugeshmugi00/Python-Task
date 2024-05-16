##set unique elements

##def unique_elemants(a):
##    uniqueList=[]
##    for i in a:
##        if i not in uniqueList:
##            uniqueList.append(i)
##    for i in uniqueList:
##            print(i,end=" ")    
##a=[1,2,3,3,4,1,4,5]
##unique_elemants(a)


##Implement a Python program
##that performs union, intersection,
##and difference operations on two sets.
##Set Intersection

##Input :
##A = {0, 2, 4, 6, 8}
##B = {1, 2, 3, 4, 5}
##
##Output :
## Union : [0, 1, 2, 3, 4, 5, 6, 8]
## Intersection : [2, 4]
## Difference : [8, 0, 6]
## Symmetric difference : [0, 1, 3, 5, 6, 8]

##def set(a,b):
##    a.update(b)
##    print("Union:",a)
##    print("Symmetric difference:",a.symmetric_difference(b))
##    print("intersection:",a.intersection(b))
##    print("difference:",a.difference(b))
##
##a = {0, 2, 4, 6, 8}
##b = {1, 2, 3, 4, 5}
##set(a,b)


##Write a function to find the
##common elements between two sets
##and return them as a new set.
##Set Comprehension

##def set_commen(a,b):
##    newSet={}
##    newSet=a.intersection(b)
##    print(a,b,"=",newSet)
##a = {0, 2, 4, 6, 8}
##b = {1, 2, 3, 4, 5}
##set_commen(a,b)

##Create a Python program that
##uses set comprehension to
##generate a set of even numbers from 1 to 20.
##Remove Duplicates

##def findEven(mySet):
##    newSet=set()
##    for i in mySet:
##        if(i % 2 == 0):
##            newSet.add(i)
##    print(newSet)      
##mySet={1,2,2,3,4,5,5,6,8,10,10,12,13,14,14,16,18,17,20}
##print(mySet)
##findEven(mySet)


##unique elements


def unique_elementes(set1,set2):
    print(set1.symmetric_difference(set2))
set1=set(input("Enter the number set1:"))
set2=set(input("Enter the number set2:"))
unique_elementes(set1,set2)



























