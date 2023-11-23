from collections import namedtuple

'''
collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
Returns a new tuple subclass named typename. 
The new subclass is used to create tuple-like objects that have fields accessible by attribute lookup as well as being indexable and iterable. 
Instances of the subclass also have a helpful docstring (with typename and field_names) and a helpful __repr__() method which lists the tuple contents in a name=value format.
'''

x = namedtuple('courses' , 'skill,language')

t = x("ML","python")
print(t)
print(t._asdict()) 

Graph = namedtuple('Graph','node,adj_nodes')

adj_list = [Graph(0,[1,2,3]),Graph(1,[0,2,3]),
            Graph(2,[1,0,3]),Graph(3,[1,2,0])]

print(adj_list)
