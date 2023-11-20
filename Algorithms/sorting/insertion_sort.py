#ascending order https://www.youtube.com/watch?v=OGzPmgsI-pQ
def sort(arr):
    n = len(arr)
    if n <= 1:
        pass
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > key:
                arr[j+1] = arr[j]
            
            else:
                break
            j = j - 1
        arr[j+1] = key


arr = [4,3,12,2,6,7,67,8,9,67,90]
arr1 = [4]
sort(arr)
print(arr)
