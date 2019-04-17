# Set: only contains immutable obj


set1 = {1,3,4,1,4,5}
print(set1)

set2 = set() # create an empty set. set = {} will create a dict
# convert other types to set
set2 = set([1,2,3,2])
print(set2)
set2 = set('hello')
print(set2)
set2 = set({'a':1,'b':2}) # only use keys
print(set2)


set2.add(100)
print(set2)

set2.update((10,30,40))
print(set2)

res = set2.pop()
print(res)

res = set2.remove(40)
print(set2)

# 交集、并集、差集、异或集、子集、真子集
#  &    |    -    ^      <=    <
