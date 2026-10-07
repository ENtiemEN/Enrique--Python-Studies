numbers = [18,16,22,99,23,11,54]

# List of even numbers
new_list = []
for number in numbers:
  if number % 2 == 0:
    new_list.append(number)

print(new_list)

## Pythonic way
even_list = [number for number in numbers if number % 2 == 0]
print(even_list)

# ==============================================
numbers = [1,2,3,4,5,6,7,8,9,10]

# Adding power of two to the list

new_list = []
for number in numbers:
  new_list.append(2**number)

print(new_list)

## Pythonic way
#power_of_two = [2**number for number in numbers]
power_of_two = [2**number for number in range(1,11)]
print(power_of_two)

# ==============================================

words = ['automobile','car','anger','fox','anchor']

# Make Uppercase the first char of each element


## Using map function
upper_words = map(
  #lambda x: x.upper(),
  #lambda x: x.capitalize(),
  lambda x: x[0].upper() + x[1:] if x.startswith('a') else x,
  words
)

print(f"Primer valor de mi iterator object -> {next(upper_words)}")

print(f"Todos los valores de mi objeto ya iniciados:\n{list(upper_words)}")

## Pythonic way -- Using Ternary operator e.g.
words_capitalized = [w[0].upper() + w[1:] if w.startswith('a') else w for w in words]
print(words_capitalized)

