'''
reduce(function,iterable,initializer)
- `reduce()` is a higher-order function that progressively combines the elements of an iterable into a single accumulated result
- `function` receives two arguments:
    function(accumulator, current_value)

- The value returned by each call becomes the accumulator for the next call.
- If an `initializer` is provided, it is used as the initial accumulator.

Conceptually:

  acc = initializer
  for value in iterable:
    acc = function(acc, value)

  return acc

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

field_groups = {'math':[],'physics':[],'chemistry':[],'astronomy':[]}

def reducer(acc, val):
  acc[val.field].append(val.name)
  return acc

scientists_by_field = reduce(
  reducer,
  scientists,
  field_groups
)

pprint(scientists_by_field)

# original way

scientists_by_field_2 = reduce(
  reducer,
  scientists,
  collections.defaultdict(list)
)

pprint(scientists_by_field_2)

# Testint `collections.deaultdict()`
print("\n========= Testing `collections.defaultdict()` ========\n")

# `defaultdict(list)` A dictionary that automatically creates an empty list for a missing key when the key is accessed
dd = collections.defaultdict(list)
print(dd)
print(dd['doesntexist'])

dd['xyz'].append(1)
dd['xyz'].append(2)
dd['xyz'].append(3)
print(dd)
