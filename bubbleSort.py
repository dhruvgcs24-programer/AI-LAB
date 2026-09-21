def bubble_Sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]< arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    return arr

numbers = [10, 50, 30, 70, 80, 20]


result = bubble_Sort(numbers)

print(result)