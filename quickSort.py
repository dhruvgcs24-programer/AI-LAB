def quick_Sort(arr,low=0,high=None):
    if high is None:
        high=len(arr)-1
    if low<high:
        pivot_index = partition(arr,low,high)
        quick_Sort(arr,low,pivot_index-1)
        quick_Sort(arr,pivot_index+1,high)
    return arr

def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    
    for j in range(low, high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

numbers = [10, 50, 30, 70, 80, 20]


result = quick_Sort(numbers)

print(result)