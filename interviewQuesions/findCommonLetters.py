#find common letters between strings

def common_letters(a,b):
    a_set = set(a)
    b_set = set(b) #returns lists of unique letters
    ans = b_set.intersection(a_set)
    #print(a_set)
    #print(b_set)
    print(ans)
    ans1 = a_set & b_set #& can be used to find common
    print(ans1)

a = "NAINA"
b = "REENE"

common_letters(a,b)




