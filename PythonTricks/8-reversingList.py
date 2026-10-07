values = [1,2,3,4,5,6,7,8]

# Classical Approach

revlist = []

for i in range(len(values)):
  revlist.append(values[len(values) - 1 - i])

print(revlist)

# Using `.reverse()` -> This applies to the og list directly

values.reverse()

print(values)

# Using `reversed()` -> Don't apply to the og list
values = [1,2,3,4,5,6,7,8]

revvalues = reversed(values) #-> An object |  <class 'list_reverseiterator'>

print(type(revvalues))
print(list(revvalues))

# Using Index Slicing
values = [1,2,3,4,5,6,7,8]

values = values[::-1]
print(values)
