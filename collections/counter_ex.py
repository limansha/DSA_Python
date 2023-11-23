from collections import Counter
'''
A Counter is a dict subclass for counting hashable objects.
It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. 
'''
arr  = ['a','b','c','a','b','c','a','b','c','c']

a = Counter(arr)
print(a)

rem = Counter({'a':1,'b':2}) #Counter takes dict 
a.subtract(rem)
print(a)

print(a.most_common(2)) #returns list of tuples

c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
print(c + d)                      # add two counters together:  c[x] + d[x]

print(c - d)                       # subtract (keeping only positive counts)
print(c & d)                       # intersection:  min(c[x], d[x])
print(c | d)                       # union:  max(c[x], d[x])

print(c == d)                      # equality:  c[x] == d[x]

print(c <= d)                     # inclusion:  c[x] <= d[x]
