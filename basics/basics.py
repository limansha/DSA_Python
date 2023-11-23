import functools
############*** decorators ***#####################
def div(a,b):
    c = a/b #float division
    print(c)

def smart_fun(fun):
    def inner(a,b):
        if a < b: #numarator always greaer than denominator is required and we can't edit div method
            a,b = b,a
        return div(a,b)
    return inner

div(2,4)

div1 = smart_fun(div) #this smart method is called decorators in python
div1(2,4)  

#####################################################

############*** lambda/Anonamous functns ***#####################

def is_even(a):
    return a % 2 == 0

even = lambda a : a % 2 == 0

for i in range(1,10):
    if even(i):
        print(i)

e = is_even(2)
e1 = even(2)
print(e)
print(e1)
# one liner function is called lambda expressions

#filter function we use lambda
arr = range(1,10)

evens = list(filter(is_even,arr)) #as filter returns an object we convert to list
print(evens)

evens = list(filter(lambda a : a%2 == 0,arr)) #as filter returns an object we convert to list
print(evens)

# map also uses lambda
#need to double the values in arr
double = list(map(lambda a : a * 2,arr))
print(double)

# reduce also used lambda
#supoose you need to sum all doubled values
sum_of_doubles = functools.reduce(lambda a,b : a+b,double)
print(sum_of_doubles)
#can also import reduce -> from funtools import reduce


#####################################################
# note ##
'''
method overloading is not there in python -> we implement it using fun(a=None,b=None,c=None) and using if else in code
operator overlaoding is prsent in python and can be achieved by magic functions like __add__,__sub__,__gt__ etc
method overriding is possible similar to java in python
Abstract classes is not supported directly in python so we import abc module and ABC class and abstractmethod annotation
from abc import ABC,abstractmethod
'''

#####################################################

############*** iterator ***#####################

nums = range(1,10)
itr = iter(nums) 
print(itr) # return object
#to get values use next method
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
#print(next(itr))


## we can write "custom iterator" using (iter and next) like range() method

class TenNums:
    def __init__(self): #default constructor or instance variable defination functn
        self.nums = 0
    def __iter__(self):
        return self
    def __next__(self):
        if(self.nums < 10):
            self.nums += 1
            return self.nums
        else:
            raise StopIteration #raise exception already present in default python package
    
nums = TenNums()
print("###############")
print(next(nums)) #prints 1 as its first value is 1 in init method

print(f'dtype TenNums: {type(nums)}')
n = range(0,5,2)
print(f'dtype range : {type(n)}')

for i in nums:
    print(i)

#####################################################

############*** Gnerators in python same as iterator ***#####################

"""
we use generators in python while dealing with huge data suppose if you have a 1 TB file which can't be fit in main memory but you need to read through it then we use generators
generators are used to perform some tasks one item at a time in list

diff b/w generators and iterators is -> suppose working on list
iterator will get the complete list and sotre it in main memory and prints it
where as generator will only get the first element of the list to main memory and do the operation like print and then gets the next element from list and overrids the first so reuses the same space.

we make generators using keyword called yeild
to make iterator we need to define two functions called __iter__ and __next__
"""

print("###############")
def topNums():
    yield 1
    yield 2
    yield 3
    yield 4

nums = topNums()
print(nums.__next__())
print(nums.__next__())
print(nums.__next__())

# print top 10 squares

def tenSquares():
    n = 1
    while n <= 10: # not using for loop because it internally uses iterator
        yield n * n #diff b/w return and yeild ? return terminates the function where as yield will not terminate a function.
        n = n + 1

values = []
for i in tenSquares():
    values.append(i)

print(values) 

