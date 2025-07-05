def minimum(array):
    min = array[0]
    for i in range(len(array)):
        if min > array[i]:
            min = array[i]
    return min
        
def maximum(array):
    max = array[len(array) - 1]
    for i in range(len(array)):
        if max < array[i]:
            max = array[i]
    return max
    # return [min, max]
array = [1,8,9,6,4,3,7,2,1,]
print("min element of array ",(minimum(array)))
print("max element of array ",maximum(array))
