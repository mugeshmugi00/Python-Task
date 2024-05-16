##def xyz_there(str):
##  for i in range(len(str)):
##    if(str[i]=='.'):
##      return False
##    else:
##      return True
##str=('abc.xyz')    
##print(xyz_there(str))    
##
##
##
##Set Intersection:
##    Write a Python program that takes
##    two sets as input from the user and
##    prints the intersection of the two sets.

def mySet(a,b):
    a.intersection(b)
    return a.intersection(b)
a=set(input("Enter the set1:"))
b=set(input("Enter the set2:"))
print(mySet(a,b))


##
##Set Union:
##    Create a Python program that generates
##    two sets of random integers between 1
##    and 10 and then prints the union of these
##    two sets.

def mySet(a,b):
    return a.union(b)
a={1,2,3,4,5}
b={6,7,8,9,10}
print(mySet(a,b))

##Set Difference:
##    Write a Python function that takes two
##    sets as input and returns a new set
##    containing elements that are present
##    in the first set but not in the second set.
def mySet(a,b):
    newSet={}
    newSet=a.difference(b)
    return newSet
a={1,2,3,4,5}
b={3,4,5,6,7}
print(mySet(a,b))
##
##Set Symmetric Difference:
##    Develop a Python program that prompts
##    the user to enter two sets of strings.
##    Then, print the symmetric difference
##    between the two sets.

def mySet(a,b):
    return a.symmetric_difference(b)
a={1,2,3,4,5}
b={3,4,5,10}
print(mySet(a,b))
























