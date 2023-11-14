def missing_number(arr):
    n = len(arr)
    s1 = sum(arr) #sum of elements
    s2 = 0 #sum till 1 to n
    for i in range(1,n+2):
        s2 += i
    print(s2-s1)

arr = [1,2,4,5,6,7]
missing_number(arr)
