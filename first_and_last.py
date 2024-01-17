

# First and last integer type in a list


def first_and_last(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            start = i
            while i+1 < len(arr) and arr[i+1] == n:
                i += 1
            return [start, i]
    return [-1, -1]

if __name__ == '__main__':
    arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
    n = 5
    print(first_and_last(arr, n))
