def my_function():
  print("Hello from a function")

my_function()

def my_function(fname):
  print(fname + " Thapa")

my_function("Punam")
my_function("Puja")
my_function("Pukar")

# passing list as an argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# recursion example
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

