from collections import deque
#append and pop will take O(1) time in deque
a = ['l','i','m','a','n','s','h','a']
a = deque(a)
a.append('safreen') #adds at last
print(a) #safreen added at the end 

a.pop() # remove at last
#these two are only in deque not in list
a.appendleft('Shaik')  #adds at first
print(a)
a.popleft() #removes frist element at begninig
print(a) 
# a = list(a) #convert to list
# print(a)

d = deque('ghi')                 # make a new deque with three items
for elem in d:                   # iterate over the deque's elements
    print(elem.upper())




d.append('j')                    # add a new entry to the right side
d.appendleft('f')                # add a new entry to the left side
print(d)                                # show the representation of the deque


d.pop()                          # return and remove the rightmost item

d.popleft()                      # return and remove the leftmost item

list(d)                          # list the contents of the deque

print(d[0])                             # peek at leftmost item

print(d[-1])                           # peek at rightmost item


list(reversed(d))                # list the contents of a deque in reverse

print('h' in d)                      # search the deque

d.extend('jkl')                  # add multiple elements at once
print(d)

d.rotate(1)                      # right rotation
print(d)

d.rotate(-1)                     # left rotation
print(d)


newd1 = deque(reversed(d))               # make a new deque in reverse order
print(newd1)
d.clear()                        # empty the deque
# d.pop()                          # cannot pop from an empty deque

     
    
d = deque('ghi')                 # make a new deque with three items



d.extendleft('abc')              # extendleft() reverses the input order and appends at start
print(d)