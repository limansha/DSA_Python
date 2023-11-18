def linear_search(nums,x):
    for i in nums:
        if(i == x):
            return True
    return False

nums = [3,3,4,5,6]
x = 11
if linear_search(nums,x):
    print("found",x)
else:
    print("not found",x)
