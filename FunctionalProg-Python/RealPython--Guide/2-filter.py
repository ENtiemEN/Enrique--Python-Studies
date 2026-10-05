'''
filter(function, iterable)
`filter()` is a built-in Python function higher-order function that constructs an iterator containing only the elements of `iterable` for which `function` returns a truthy value.

Formally, given an iterable X = (x1,x2,...,xn) and a predicate P, filter(P,X) produces the subsequence

  (xi in X such that P(xi))

while preserving the original orden of the elements

Characteristics:
- `function` is typically a PREDICATE: a function that maps each element to a boolean-like value.
- `filter()` does not modify that original iterable
- In Python3, `filter()` returns a LAZY OPERATOR, not a list.
- Elements are evaluated only when they are requested (e.g. `next()`, iteration with `for`, or conversions with `list()`, `tuple()`)

'''
import collections

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

#print(filter(lambda x: x.nobel is True, scientists)) #e.g. -> <filter object at 0x7820cff6e5f0>
fs = filter(lambda x: x.nobel is True, scientists)

print(next(fs))
print(next(fs))
print(next(fs))

# ==============================================

#print(f"\nTupla:\n{tuple(filter(lambda x: x.nobel is True, scientists))}")

fs_tuple = tuple(filter(lambda x: x.field == 'astronomy', scientists))
print(f"\nAstronomy scientists:\n{fs_tuple}")

# ==============================================

print("\nPassing a function defined by us to the filter() func.\n")

def not_nobel_filter(x) -> bool:
  return x.nobel is False

not_nobel = tuple(filter(not_nobel_filter, scientists))
print(f"Not Nobel Filter:\n{not_nobel}")


