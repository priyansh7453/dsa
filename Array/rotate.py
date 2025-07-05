def rotate_array(arr,size,d):
    # temp = arr[0]
    # for i in range(size-1):
    #     arr[i] = arr[i+1]
    # arr[size-1] = temp
    # return arr
    temp = [0]*size
    d  = d%size
    # Copy last n - d elements to the front of temp
    for i in range(size - d):
        temp[i] = arr[d + i]
    # Copy the first d elements to the back of temp
    for i in range(d):
        temp[size - d + i] = arr[i]
        
    # Copying the elements of temp in arr
    # to get the final rotated array
    for i in range(size):
        arr[i] = temp[i]
    return arr

arr = [1,7,9,11]
size = len(arr)
d=2
print(rotate_array(arr,size,d))