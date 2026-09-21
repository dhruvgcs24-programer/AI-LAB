def binary_Search(arr, target):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=low+(high-low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high=mid-1
        else:
            low=mid+1
    return low

numbers = [10, 50, 30, 70, 80, 20]
target_val = 30

result = binary_Search(numbers, target_val)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")