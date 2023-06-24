def binary_search(list,item):
    low = 0
    high = len(list)-1


    while low <= high:
        mid = (low + high) / 2
        gues = list[mid]
        if gues == item:
            return mid
        if gues >item:
            high = mid -1
        else:
            low =mid +1
    return None

my_list = [1,9,8,7,5]
my_list.sort()
print(my_list)
binary_search(my_list,3)


print(binary_search(my_list,3))
