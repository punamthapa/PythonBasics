_test ="abc"
ab_test =762
print(_test)
print(ab_test)

# case sensitive
AB_test=12
ab_test=123

print(AB_test)
print(ab_test)

# cannot use reserved keyword

# return =abc
# print(return)


# list of reserved keyword
import keyword

keywordList = keyword.kwlist
print(keywordList)

# testing for python keywords
print(keyword.iskeyword("try"))
print(keyword.iskeyword("abc"))