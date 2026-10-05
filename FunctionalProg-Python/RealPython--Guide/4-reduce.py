'''
reduce: (function, sequence[,initial])
reduce(function, sequence[,initial]) -> value

Apply a function of two arguments cumulatively to the items of a sequence, from left to right, so as to reduce the sequence to a single value.

e.g. -> `reduce(lambda x,y: x+y,[1,2,3,4,5])` -> ((((1+2)+3)+4)+5)
If initial is present, it is placed before the items of the sequence in the calculation, and serves as a default when the sequence is empty

'''
import collections
from functools import reduce
from pprint import pprint

Scientist = collections.namedtuple('Scientist',[
  'name',
  'field',
  'born',
  'nobel'
])

scientists = (
  Scientist(name='Ada Lovelace',field='math',born=1815,nobel=False),
  Scientist(name='Emmy Noether',field='math',born=1882,nobel=False),
  Scientist(name='Marie Curie',field='physics',born=1867,nobel=True),
  Scientist(name='Tu Youyou',field='chemistry',born=1930,nobel=True),
  Scientist(name='Ada Yonath',field='chemistry',born=1939,nobel=True),
  Scientist(name='Vera Rubin',field='astronomy',born=1928,nobel=False),
  Scientist(name='Sally Ride',field='physics',born=1951,nobel=False),
)

#names_and_ages = tuple(
#  {'name': x.name, 'age': 2026-x.born}
#  for x in scientists
#)

names_and_ages = tuple(map(lambda x: {'name': x.name, 'age': 2026-x.born},scientists))

pprint(names_and_ages)

total_age = reduce(
  lambda acc, val: acc + val['age'],
  names_and_ages,
  0 # <- accumulator start with 0
)

print(f"Total age of the scientists -> {total_age}")

# Pythonic way
print(sum(x['age'] for x in names_and_ages))
