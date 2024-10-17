# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.




# collections
# list Allow Duplicates
list1 = [1,2,3,4,"hi","hello"]
print(list1)
# Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
# List Length
print(len(thislist))
# list()
thislist1 = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist1)
# access the list
thislist2 = ["apple", "banana", "cherry"]
print(thislist2[1])
# list[]
thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist3[2:5])
# if list
thislist4 = ["apple", "banana", "cherry"]
if "apple" in thislist4:
  print("Yes, 'apple' is in the fruits list")
# inser
thislist5 = ["apple", "banana", "cherry"]
thislist5.insert(2, "watermelon")
print(thislist5)  
# Using the append() method to append an item:
thislist6 = ["apple", "banana", "cherry"]
thislist6.append("orange")
print(thislist6)
# merge (extend)
thelist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thelist.extend(tropical)
print(thelist)
# remove
list2 = ["apple", "banana", "cherry"]
list2.remove("banana")
print(list2)
# pop (index)
t2 = ["apple", "banana", "cherry"]
t2.pop(1)
print(t2)
# pop()
popup = ["apple", "banana", "cherry"]
popup.pop()
print(popup)
# loop renge len
t3 = ["apple", "banana", "cherry"]
for i in range(len(t3)):
  print(t3[i])
# join list
list11 = ["a", "b" , "c"]
list22 = [1, 2, 3]

for x in list22:
  list11.append(x)

print(list11)
# update
num = [1,2,3,4,5]
num[1] = 10
print(num)