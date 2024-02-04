

def element_count(arr):
    count = []
    for el in arr:
        while arr[0] == arr[1]:
            count.append(arr[el])
        if arr[el] == len(arr-1):
            break
    return count



array = [1, 3, 4, 4, 4, 5]
print(element_count(array))


