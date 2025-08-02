def max_min(array):
    maxv = array[0]
    minv = array[0]
    for i in array:
        if maxv < i :
            maxv = i
        elif minv > i:
            minv = i 
    print(maxv)
    print(minv)





Array = [3, 3, 0, 99, -40]
max_min(Array)