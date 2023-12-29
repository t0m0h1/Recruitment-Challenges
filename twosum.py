def twosum(arr, target):
    for i in arr:
        for j in arr:
            if i + j == target:
                return arr[i], arr[j]


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == '__main__':
    # call twosum with nums and the target number
    print(twosum(nums, 9))