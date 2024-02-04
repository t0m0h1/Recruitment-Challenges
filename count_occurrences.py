def element_count(arr):
    count = {}
    for el in arr:
        if el in count:
            count[el] += 1
        else:
            count[el] = 1
    return count

array = [1, 3, 4, 4, 4, 5]
print(element_count(array))