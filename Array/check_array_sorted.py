def check_sort_array(array):
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            return False
    return True


Array = [1, 2, 33, 4, 5]
res= check_sort_array(Array)
print(res)