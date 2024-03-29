# Iterative Binary Search
# it works by repeatedly dividing the search interval in half
# Time Complexity: O(log n)

def binary_search(arr, left, right, x: int) -> int:
    while left <= right:
        mid = left + (right - left) // 2

        # Check if x is at mid
        if arr[mid] == x:
            return mid
        
        elif arr[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    return -1

# Test array
arr = [1, 2, 3, 4, 5, 6, 7, 8]
x = 5

if __name__ == '__main__':
    result = binary_search(arr, 0, len(arr)-1, x)

    if result != -1:
        print(f'Element is present at index {result}')
    else:
        print('Element is not present in array')
