#dict

#key可以是任意对象， value只能是不可变对象
dict = {
    1:'one',
    '2': (1,2,3)
}
print(dict[1])
print(dict['2'])

#dict[]获取元素，如果元素不存在会抛出异常
#用get()不会抛异常，会返回None,也可以设定默认返回值
print(dict.get(3,'not exist'))

#setdefault: if the key exists, return the current val and not updata; otherwise, add new k-v to dict
dict.setdefault(3,'Three')
res = dict.setdefault('2','Two')
print(res)

#update: merge two dicts. If there are same keys in both dicts, it will use k-v in the second one
dict1 = {'1':1,'2':2}
dict2 = {'3':3,'4':4}
dict1.update(dict2)
print(dict1)

#delete
del dict1['1']
print(dict1)

res = dict1.popitem() #delete k-v randomly (usesally the last pair) and return a tuple
print(res)
res = dict1.pop('2') #delete by key and return val. If the key does not exist, throw an error. We can also set a default
                     #to be returned
print(res)
res = dict1.pop('1','default deleting val')
print(res)

#shellow copy: only copy  val instead of object
dict3 = dict1.copy()

#iterate
for k in dict1.keys():
    print(k,dict1[k])

for v in dict1.values():
    print(v)

for k,v in dict1.items():
    print(k,v)

