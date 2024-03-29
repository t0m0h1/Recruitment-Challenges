# Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

def twosum(arr, target):
    l, r = 0, len(arr) -1

    while l < r:
        current_sum = arr[l]+ arr[r]
        if current_sum > target:
            r -= 1
        elif current_sum < target:
            l += 1
        else:
            return [l, r]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8

if __name__ == '__main__':
    # call twosum() with nums and target as arguments.
    result = twosum(nums, target)
    print("Result:", result)

    