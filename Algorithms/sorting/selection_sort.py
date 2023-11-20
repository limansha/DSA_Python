#ascending order https://www.youtube.com/watch?v=xWBP4lzkoyM
def sort(arr):
    n = len(arr)

    for i in range(0,n):
        small_idx = i
        for j in range(i,n): #find smallest element in unsorted array
            if arr[j] < arr[small_idx]:
                small_idx = j
        arr[small_idx],arr[i] = arr[i],arr[small_idx] #swap smallest element to the first of the sorted aray that is i pos and increment i


arr = [4,3,12,2,6,7,67,8,9,67,90]
arr1 = [4]
sort(arr)
print(arr)

