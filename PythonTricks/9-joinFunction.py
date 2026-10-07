# `.join()` -> Allows you to join multiple elements using a specific string

words = ['Enrique','Julca','Delgado']

# Classical Approach
sentence = ""
for w in words:
  sentence += w + " "

print(sentence)

# Using `.join()`

sentence = " ".join(words)
print(sentence)


