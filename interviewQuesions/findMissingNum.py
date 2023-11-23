# find missing number in array(using summationa nad XOR)

arr = [1,2,4,5,6,7]

#arr contains sequence of nums(1 to n+1) find missing number 
def sumation():
    n = len(arr) +1
    sum1 = (n * (n + 1))//2
    arrSum =sum(arr)
    # for i in arr:
    #     arrSum += i

    print(sum1-arrSum)

#with Xor operation
def xor_mtd():
    n = len(arr) 
    actual_xor = 0
    arr_xor = arr[0]
    for i in range(1,n):
        arr_xor ^= arr[i]

    for i in range(1,n + 2):
        actual_xor ^= i

    print(actual_xor^arr_xor)


sumation()
xor_mtd()