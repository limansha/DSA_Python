# sort ascending
def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                arr[i],arr[j]=arr[j],arr[i] #swap two elements


arr = [4,3,12,2,6,7,67,8,9,67,90]
bubble_sort(arr)
print(arr)
