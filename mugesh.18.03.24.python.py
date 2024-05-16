##output
##* 
##* * 
##* * * 
##* * * * 
##* * * * * 
##* * * * * 
##* * * * 
##* * * 
##* * 
##* 


for i in range(1,6):
    for j in range(1,6):
        if(i>=j):
            print("*",end=" ")
    print()
for k in range(1,6):
    for l in range(1,6):
        if(l>=k):
            print("*",end=" ")
    print()    
