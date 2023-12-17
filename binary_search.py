# Iterative Binary Search
# it works by repeatedly dividing the search interval in half

def binary_search(arr, left, right, x: int) -> int:
    while left <= right:
        mid = left + (right - left) // 2

        # check if x is mid
        if arr[mid] == x:
            return mid
        
        elif arr[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    return -1

# Test array
arr = [1, 2, 3, 4, 5, 6, 7, 8]

result = binary_search(arr, 0, len(arr)-1, 8)

if __name__ == '__main__':
    if result != -1:
        print(f'Element is present at index {result}')
    else:
        print('Element is not present in array')
