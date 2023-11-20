#ascending order https://www.youtube.com/watch?v=PgBzjlCcFvc&t=26s
def quick_sort(arr,low,high):
    if(low < high):
        pivot = partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)

def partition(arr,low,high):
    i = low - 1
    j = low
    p = arr[high]
    while(j < high):
        if arr[j] <= p:
            i =  i + 1 # i pointer is pointing to last value smaller than p 
            arr[i],arr[j] = arr[j],arr[i]
        
        j = j + 1
    
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1


arr = [4,3,12,2,6,7,67,8,9,67,90]
quick_sort(arr,0,len(arr)-1)
print(arr)



