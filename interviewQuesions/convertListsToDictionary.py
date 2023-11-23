# write a pgm to map two list as a dictionary based on index postions

#can also do it with for loop
def fun():
    list1 = ["Naina","Rahul","Gopal"]
    list2 = [345,678,890]
    dict2 = dict(zip(list1,list2))
    print(dict2)

fun() #called

#mtd 2
list1 = ["Naina","Rahul","Gopal"]
list2 = [345,678,890]

n = len(list1)

dict = {}
for i in range(0,n):
    dict[list1[i]] = list2[i]

print(dict.items())


#can we cinvert dict to list? -> yes convert to tuple then to list

for i in dict.items():
    print(list(i))