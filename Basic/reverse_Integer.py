def alternateSwap(arr,len):
    for i in range(0,len-1,2):
        arr[i],arr[i+1] = arr[i+1],arr[i]
    
    return arr




arr = [1, 2, 3, 4, 5, 6 ]
len = len(arr)
print(alternateSwap(arr,len))