''' Concepts:

- ITERABLE -> An iterable is any Python object that can provide itselements one at a time, usually in a loop

examples:
[1,2,3]         -> # list
(1,2,3)         -> # tuple
"abc"           -> # string
{1,2,3}         -> # set
{"a":1, "b":2}  -> # dictionary

All of these can be used with:
`for x in iterable:`

Formally, an iterable is an object from which Python can obtain an iterator. Conceptually:

`iterator = iter(iterable)`
Then Python repeatedly calls:
`next(interator)`

Example:
`filter(lambda x: ..., iterable)`
(where iterable can be a tuple, dict, etc)
Returns a `filter` object, which is an iterator

- LAZY OPERATOR -> Means that Python does not compute all the results immediately.

`filter(lambda x: ..., iterable)` -> creates a `filter` object, and that objet is an iterator. Its evaluation is lazy.
(Is lazy because it only constructs the iterator)

`tuple(filter(lambda x: ..., iterable))` is diferent.
`filter(...)` is still lazy by itself, but then `tuple(...)` consumes the entire iterator in order to construct the tuple

'''
import collections

# `collections.namedtuple` -> creates and return a class called 'Scientist'
# Python the class are also objects (Normally the type is `type`)
Scientist = collections.namedtuple('Scientist',[
  'name',
  'field',
  'born',
  'nobel'
])

# `namedtuple` -> inmutable
print(type(Scientist))

ada = Scientist(name='Ada Lovelace',field='math',born=1815,nobel=False)

print(type(ada))
#print(ada)
#print(ada.born)

scientist_mutable = [
  Scientist(name='Ada Lovelace',field='math',born=1815,nobel=False),
  Scientist(name='Emmy Noether',field='math',born=1882,nobel=False)
]

print(f"\nList of scientist ('namedtuple') ->\n{scientist_mutable}")

del scientist_mutable[0]
print(f"\nList of scientist ('namedtuple') ->\n{scientist_mutable}")

# Completely Inmutable approach
scientists = (
  Scientist(name='Ada Lovelace',field='math',born=1815,nobel=False),
  Scientist(name='Emmy Noether',field='math',born=1882,nobel=False),
  Scientist(name='Marie Curie',field='physics',born=1867,nobel=True),
  Scientist(name='Tu Youyou',field='chemistry',born=1930,nobel=True),
  Scientist(name='Ada Yonath',field='chemistry',born=1939,nobel=True),
  Scientist(name='Vera Rubin',field='astronomy',born=1928,nobel=False),
  Scientist(name='Sally Ride',field='physics',born=1951,nobel=False),
)

print(scientists)
