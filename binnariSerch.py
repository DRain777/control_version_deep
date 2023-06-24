def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]

        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1

    return None
test_list = [9,7,5,0,3]
my_list = [1, 2, 3, 4, 5]
my_list.sort()  # Sort the list before performing binary search
print(my_list)
print(binary_search(my_list, 3))
test_list.sort()
print(test_list)
print(binary_search(test_list, 3))
