# lambda fuction
result=lambda a,b:a+b
print(result(20,20))

# map fuction
num1=[1,2,3,4,20]
num2=[6,7,8,9,10]
def myNumber(a,b):
    if(a>b):
        return a
    else:
        return b
result=list(map(myNumber,num1,num2))
print(result)    

# filter fuction
num3=[1,2,3,4,5,6,7,8,9,10]
def myList(num3):
    if(num3%2==0):
        return True
result=list(filter(myList,num3))
print(result)    