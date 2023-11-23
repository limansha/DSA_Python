#itertools : product, permutations,combinations,accumalate,group by, and infinite iterators

from itertools import product,permutations,combinations,combinations_with_replacement

###### product ##########
a = [1,2]
b = [3,4]
c = product(a,b)
print(type(c))
print(list(c))

a1 = [1,2]
b1 = [3]
c1 = product(a1,b1,repeat=2)
print(list(c1))

c2 = product(b,a1,b1)
print(list(c2))

############ permutation/ rearrangements of charcters in a string ############
a = [1,2,3]
perm = permutations(a)
print(list(perm))

#permutations of substring
perm1 = permutations(a,2)
print(list(perm1))


############### Combinations ################
a = [1,2,3]
comb = combinations(a,2) #ncr n = len(a) r = 2
print(list(comb))

########## combinations_with_replacement ##########

comb1 = combinations_with_replacement(a,2) #considers itself as well
print(list(comb1)) #comb1 = perm1

