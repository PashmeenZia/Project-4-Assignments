def binary_search(arr, target):
    """Perform binary search on a sorted list."""
    low = 0  # Start of the list
    high = len(arr) - 1  # End of the list
    
    while low <= high:  # Continue searching until the range is valid
        mid = (low + high) // 2  # Find the middle index
        
        if arr[mid] == target:  # If the middle element is the target, return index
            return mid
        elif arr[mid] < target:  # If target is greater, ignore left half
            low = mid + 1
        else:  # If target is smaller, ignore right half
            high = mid - 1
    
    return -1  # Target not found

# Example usage
print("\nWelcome to Binary Search!")
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # Sorted list
print("Sorted list:", numbers)

target = int(input("Enter a number to search: "))
index = binary_search(numbers, target)

if index != -1:
    print(f"🎉 Found {target} at index {index}!")
else:
    print("❌ Number not found in the list.")