import collections
from itertools import groupby
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

'''
`itertools.groupby(iterable, key=...)` groups consecutive elements that have the same key

Each value produced by `groupby()` is a pair:
  (key, group_iterator)
this e.g. --> item = ('math',<group iterator>)
'''
scientists_by_field = {
  item[0]: list(item[1])
  for item in groupby(scientists, lambda x: x.field)
}
''' equivalent to

result = {}
for item in groupby(scientist, lambda x: x.field):
  result[item[0]] = list(item[1])
'''

pprint(scientists_by_field)

print('\n\n')

# Expression more pythonic
scientists_by_field2 = reduce(
  lambda acc, val: {**acc, **{val.field: acc[val.field] + [val.name]}},
  scientists,
  {'math':[],'physics':[],'chemistry':[],'astronomy':[]}
)

pprint(scientists_by_field2)

