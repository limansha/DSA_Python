from collections import OrderedDict,defaultdict

d = OrderedDict()
d[1]="L"
d[2]= "i"
d[3]= "m"
print(d.items()) #remembers the input order in dictionary

x= {1:"gd",2:"df"} 
y = defaultdict(int)
y[1] ="gd"
y[2] = "df"
#defaultdict is used to overcome keyError when key is not present
print(y[1])
print(y[2])
print(y[3]) #no key error

print(x[1])
print(x[2])
print(x[3])


