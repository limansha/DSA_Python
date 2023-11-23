#find out pairs with given sum in a array

#elements must not be duplicates
ip_arr = [10,2,5,7,4,3,9,8,19,21]
in_sum = 17

rem_arr = {}
ans = {}

for i in ip_arr:
    rem_arr[in_sum-i] = i
    if i in rem_arr.keys():
        ans[i] = rem_arr[i]

print(rem_arr.items())
print(ans.items())
print(len(ans))