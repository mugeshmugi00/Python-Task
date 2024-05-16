import map function


myList=[1,2,3,4,20]
def evenNumber(myList):
    if(myList%2==0):
        return True
    else:
        return False
print(list(filter(evenNumber,myList)))    
