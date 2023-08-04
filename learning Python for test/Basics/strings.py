print("Hello")
print('Hello')
# assign multiline string to a variable by using three quotes Or three single quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# strings are array String Length
a = "Hello, World!"
print(a[1])
print(len(a))

# Looping Through a String
# for x in "banana":
#   print(x)

txt = "The best things in life are free!"
print("free" in txt)
print("expensive" not in txt)
if "free" in txt:
  print("Yes, 'free' is present.")

if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

  # slicing strings
# characters from position 2 to position 5 (not included)
print(a[2:5])

# characters from the start to position 5 (not included)
print(a[:5])

# characters from position 2, and all the way to the end
print(a[2:])

# Negative Indexing
print(a[-5:-2])

#  Modify Strings
print(a.upper())
print(a.lower())
# The strip() method removes any whitespace from the beginning or the end
print(a.strip())
# The replace() method replaces a string with another string
print(a.replace("H", "J"))
# The split() method splits the string into substrings if it finds instances of the separator
print(a.split(","))

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
d = a + " " + b
print(d)

# incorrect
# age = 36
# txt = "My name is John, I am " + age
# print(txt)
# Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
print(myorder.format(quantity, itemno, price))

# incorrect
# txt = "We are the so-called "Vikings" from the north."

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

txt = "Hello\nWorld!"
print(txt)