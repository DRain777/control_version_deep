def binary_search(lst, item):
    lst.sort()  # Sort the list in ascending order
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None



my_list = [1, 9, 8, 7, 5]
print(binary_search(my_list, 4))



