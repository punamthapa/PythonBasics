thisset = {"apple", "banana", "cherry"}
print(thisset)
# duplicates not allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(len(thisset))

print(thisset)

# true and 1 is considered same
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# Once a set is created, you cannot change its items, but you can add new items.
thisset.add("orange")

print(thisset)
thisset.remove("banana")

print(thisset)

thisset.discard("banana")

print(thisset)

# random item remove
x = thisset.pop()

print(x)

print(thisset)

# clear emptythe set
thisset.clear()

print(thisset)