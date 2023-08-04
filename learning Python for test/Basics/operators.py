# arithmetic operators
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 % 5)
print(10 ** 5)

# assignment operator
x = 5
print(x)
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x %= 3
print(x)
x //= 3
print(x)
x **= 3
print(x)

# Comparison Operators
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Logical Operators
x = 5

print(x > 3 and x < 10)
print(x > 3 or x < 4)
print(not(x > 3 and x < 10))

# Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

# Membership Operators
x = ["apple", "banana"]
# in
print("banana" in x)
# not in
print("pineapple" not in x)


#  Bitwise Operators
# AND
print(6 & 3)
# or
print(6 | 3)
# xor
print(6 ^ 3)
# NOT
print(~3)
# Zero fill left shift
print(3 << 2)
# Signed right shift
print(8 >> 2)
