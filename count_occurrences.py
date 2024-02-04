

def count(arr):
    count = []
    for el in arr:
        while arr[0] == arr[1]:
            count.append(arr[el])
        if arr[el] == len(arr-1):
            break
    return count



array = [1, 3, 4, 4, 4, 5]
print(count(array))








# old
# def count(arr, key=None):
#     occurences = {key: el.count() for el in arr}
#     return occurences



# if __name__ == '__main__':
#     array1 = [1, 1, 2, 3, 4, 4, 4]
#     print(count(array1))