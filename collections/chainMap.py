from collections import ChainMap

dict1 = {"a":1,"b":4}
dict2 = {"b":2,'c':3}

x = ChainMap(dict1,dict2)
print(x)

print(list(x))
x.update({"b":7})
print(x)
