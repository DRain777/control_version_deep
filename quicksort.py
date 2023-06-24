def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

my_array = [7, 4, 5, 9, 0, 2]
sorted_array = quicksort(my_array)
print(sorted_array)

'''    В этомquicksortфункцияarrкак

В противном случае он выбираетleft(элементы меньшеmiddle(right(элементы больше, чем точка опоры).

Затем функцияleftиrightразделяет и объединяетmiddleраздел для получения окончательной сортировки

С использованием[7, 4, 5, 9, 0, 2],quicksortфункция называется      '''