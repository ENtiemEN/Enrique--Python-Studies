'''
map: (func, *iterables)
map(func, *iterables) --> map object

Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.
--- --- --- --- --- --- ---
- `map()` is a higher-order function: it receives another function as an argument.
- It applies the function to each element of the iterable(s)
- It does NOT modify the original iterable
- It returns a new lazy iterator (`map` object), not a copied collection. Results are computed only when the iterator is consumed

'''
import collections
from pprint import pprint #pprint.pprint()

Scientist = collections.namedtuple('Scientist',['name','field','born','nobel'])

scientists = (
  Scientist(name='Ada Lovelace',field='math',born=1815,nobel=False),
  Scientist(name='Emmy Noether',field='math',born=1882,nobel=False),
  Scientist(name='Marie Curie',field='physics',born=1867,nobel=True),
  Scientist(name='Tu Youyou',field='chemistry',born=1930,nobel=True),
  Scientist(name='Ada Yonath',field='chemistry',born=1939,nobel=True),
  Scientist(name='Vera Rubin',field='astronomy',born=1928,nobel=False),
  Scientist(name='Sally Ride',field='physics',born=1951,nobel=False),
)

# lazy transformation: no full result is created yet. But `tuple()` consumes the lazy map iterator and materializes the results
names_and_ages = tuple(map(
  lambda x: {'name': x.name, 'age': 2026 - x.born},
  scientists
))

pprint(names_and_ages)

# Pythonic way
# List comprenhension: EAGER, creates the whole list immediately
eager_expression = [{'name':x.name, 'age':2026-x.born} for x in scientists]
pprint(eager_expression)

#pprint(tuple([{'name':x.name, 'age':2026-x.born} for x in scientists]))

# `tuple()` consumes the generator and materializes the result.
# Generator expression `({...} for x in iterable)` -> LAZY, similar to `map()` in evaluation behavior
pprint(tuple({'name':x.name, 'age':2026-x.born} for x in scientists))

'''
map(...)                --> lazy iterator
list comprehension      --> eager list
generator expression    --> lazy iterator
tuple(...) / list(...)  --> materialize/consume iterator
'''
