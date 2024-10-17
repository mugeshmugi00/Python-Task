user = int (input("Enter the number:"))
a,b = 0,1
i=0
# while i < user+1:
#     print(a ,end=" ")
#     a,b=b,a+b
#     i+=1

# using for loop
for i in range(user+1):
    print(a,end=" ")
    a,b=b,a+b
   