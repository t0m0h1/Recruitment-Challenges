def element_count(arr):
    count = {}
    for el in arr:
        if el in count:
            count[el] += 1
        else:
            count[el] = 1
    return count

array = [1, 3, 4, 4, 4, 5, 5]
print(element_count(array))


'''Inside the loop, it checks if the current element (el) is already a key in the count dictionary using the in operator.
If it is, it means that the element has already been encountered before.
so the code increments its count by 1 using the += operator.'''