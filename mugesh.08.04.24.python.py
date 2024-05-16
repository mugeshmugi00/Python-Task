##x=int(input("Enter the number:"))
##a=0
##b=1
##c=0
##print(a,b,end=" ")
##for i in range(x-2):
##    c=a+b
##    i+=1
##    print(c,end=" ")
##    a=b
##    b=c
    
def fibonacci(f):
    a=0
    b=1
    c=0
    for i in range(f):
        print(a,end=" ")
        c=a+b
        i+=1
        a=b
        b=c
f=int(input("Enter the number:"))
fibonacci(f)
