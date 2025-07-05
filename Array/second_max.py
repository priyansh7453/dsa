def second_max(array):
    maxv = array[0]
    second_max= array[0]
    for i in array:
        if maxv < i :
            maxv = i
        if second_max < i and maxv != i:
            second_max = i
    # print(second_max)
    return second_max
    




Array = [10, 25, 85, 40, 85, 2]
res=second_max(Array)
print(res)