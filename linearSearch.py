def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
            
    return -1  

# --- Example Usage ---
numbers = [10, 50, 30, 70, 80, 20]
target_val = 30

result = linear_search(numbers, target_val)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")
