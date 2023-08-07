# creating list
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#list length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# list data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

# A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]

print(list1)

# find type
thislist = ["apple", "banana", "cherry"]
print(type(thislist))

# using list constructor
print(thislist)

# access list item
print(thislist[1])
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# change list item
thislist[1] = "blackcurrant"
print(thislist)

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Change the second value by replacing it with two new values:
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist[1:3] = ["watermelon"]
print(thislist)

# insert item
thislist.insert(2, "watermelon")
print(thislist)

# add item
thislist.append("orange")
print(thislist)

# insert item in 2
thislist.insert(1, "orange")
print(thislist)

# Add the elements of tropical to thislist:

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# remove
thislist.remove("banana")
print(thislist)

# remove second item
thislist.pop(1)
print(thislist)

# remove last
thislist.pop()
print(thislist)

# remove specified index
del thislist[0]
print(thislist)

# delete entire list
del thislist

# using clear
thislist.clear()
print(thislist)

# sorting
thislist.sort()
print(thislist)