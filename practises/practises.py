# i = int(input("Enter the num:"))
# j = int(input("Enter the num:"))
# i = ["hi","Hi"]

# while "Hi" in i :
#     print(i)
#     break

# sum of numbers 1 to n
# i = 1
# n = int(input("Enter the num:"))
# while i < n+1:
#     print(i)
#     i+=1
#Example 2: Sum of Even Numbers from 1 to N 
# i = 1
# n = int(input("Enter the num:"))
# while i < n+1:
#     if(i % 2 == 0):
#         print(i)
#     i+=1    
#  Sum of Digits of a Number
# i = 1
# n = int(input("Enter the num:"))
# sum = 0
# while i < n+1:
#     sum=i+i
#     i+=1
# print(sum)
#  Sum of Squre of a Number
# i = 1
# n = int(input("Enter the num:"))
# sum = 0
# while i < n+1:
#     sum=i**2
#     i+=1
# print(sum)

# factoriel
# user = int(input("Enter the num:"))
# fact = 1
# for i in range(1,user+1):
#     fact = fact*i
# print(fact)    

# palindrom
# user = input("Enter the str:")
# rev = user[::-1]
# if user == rev:
#     print(f'{user}is palindrom')
# else:
#     print(f'{user}is Not palindrom')    
    
#fibonacies
# user = int(input("Enter the num:"))
# a,b = 0,1
# for i in range(user+1):
#     print(a,end=" ")
#     a,b = b, a+b

# function
# def myfun(user):
#     rev = user1[::-1]
#     if(user1 == rev):
#         print("palindrom")
#     else:
#         print("Not palindrom")
# user1 = input("Enter :")
# myfun(user1)        
            
# Program to sum user input numbers

# Step 1: Get input from the user
# numbers = input("Enter numbers separated by spaces: ")

# # Step 2: Split the input string into a list of strings
# numbers_list = numbers.split()

# # Step 3: Convert each string to an integer
# numbers_list = [int(num) for num in numbers_list]

# # Step 4: Calculate the sum of the numbers
# total_sum = sum(numbers_list)

# # Step 5: Print the final sum
# print(f"The sum of the numbers is: {total_sum}")
# number = numbers.split()
# number = [int(num) for num in number] 
# total = sum(number)
# print(total)
 
 
# __init__()
# class person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = person("John", 36)

# print(p1.name)
# print(p1.age)

# filehandling
# import os
# import json

# def file(filename):
#     isfile = os.path.exists(filename)
#     print("File is exists")
#     personFile = open(filename,"x")
#     print("open")
# file("mugeshmugesh")    
    
num = 12345
total = 0
while num:
    digit = num % 10
    total += digit
    num = num // 10
print(total)     