# print("hi")
# odd even

# num = 23
# if num %2 ==0:
#     print("Even")
# else:
#     print("Odd")   

# a=12
# b=13
# c=a+b
# print(c) 

# a=1
# b=2
# if a>b:
#     print(a,"maximum")
# else:
#     print(b,"maximum")  

# num =str("hi")
# def number():
#     print("hello "+num)
# number()

# x="fantastic"
# def srting():
#     x="hi"
#     print("Inner"+x)
# srting()
# print("outer"+x)    

# a=int(input("Enter the num1:"))
# b=int(input("Enter the num2:"))
# c=int(input("Enter the num3:"))
# if a>b and a>c:
#     print(a,"max")
# elif b>c and b>a:
#     print(b,"max")
# else:
#     print(c,"max")     

# a=25
# if a>2:
#     print("graterthen") 
#     if a<25:
#         print("lessthen")
# else:
#     print("hi")          

# while loop

# x=1
# while x<=6:
#     print(x)
#     x+=1
    
# i=1
# while i<=5:
#     print(i)
#     if i == 3:
#        break
#     i+=1   

# for loop
# def number():
#     num= (1,2,3,4,5)
#     for i in num:
#         print(i) 
# number()

# def lis():
#     a = ["hi","hello"]
#     for i in a:
#         print(i)
# lis()       

# for i in "hello":
#     print(i) 

# for i in range(1,6+1):
#     print(i)

# num = int(20)
# for i in range(1,num+1,2):
#     print(i,"odd")
    
# num1 = int(20)
# for i in range(2,num1+1,2):
#     print(i,"even")    

# for i in range(10,0,-1):
    # print(i)  

# for i in range(6):
#     print(i)
# else:
#     print("Fineal")    

# for i in range(6):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Fineal")   

# functions
# def my_function(demo):
#     print(demo+" hi")
# my_function("hellow")   

# def my_fun(food):
#     for i in food:
#         print(i)
# fruits = ["apple", "banana", "cherry"]        
# my_fun(fruits) 

# def sum(a):
#     return 2 * a
# print(sum(2))

# def palindrom():
#     a = "amma"
#     if a[::-1] == a:
#         print("palindrom")
#     else:
#         print("Not a palindrom")  
# palindrom()  

# factoriyal
# a = 5
# user = 0
# fact = 1
# for i in range(a,user,-1):
#     fact = fact * i
# print(fact)

# def fact(n):
#     start = 0
#     fact = 1
#     for i in range(user,start,-1):
#         fact = fact * i
#     print(fact)
# user = int (input("Enter the Number:"))    
# fact(user)  

def add(*a):
    temp =0
    for i in a:
        temp+=i
    print(temp)
add(1,2,3,4,5)        
    

      
        