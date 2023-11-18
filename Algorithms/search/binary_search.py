#prerequsites list should be sorted
pos = -1
def binary_search(nums,x):
    l = 0
    h = len(nums)-1
    print(h)
    while(l <= h):
        m = (l + h)//2
        if nums[m] == x:
            print(nums[m],m)
            globals()['pos'] = m
            return True
        else:
            if nums[m] < x: # x will be in the right hand side
                l = m + 1
            else:
                h = m - 1
    return False
        



nums = [3,3,4,5,6,7,9,12]
x = 5
if binary_search(nums,x):
    print("found {} at pos {}".format(x,pos))
else:
    print("not found",x)
