# Access Tuple Items 
# Allow Duplicates
list1 = (1,2,3,4,5,"hi","hello")
print(list1[-1])
# [:]
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
# update
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
# add
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
m = thistuple + y
print(m)
# Unpacking a tuple:
# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
# Multiply the fruits tuple by 2:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
# count
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x) 

# duplicat eliments
list2 = [1,2,3,4,5,1,2,3]
# list3 = list(set(list2))
# print(list3)
list3 = []
for item in list2:
    if item not in list3:
        list3.append(item)
print(list3)    