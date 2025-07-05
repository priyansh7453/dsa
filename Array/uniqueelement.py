def uniqueElement(arr,len):
    for i in range(len):
        count = 0
        for j in range(len):
            if arr[i] == arr[j]:
                count += 1

        if count == 1:
            return arr[i]
    return None




arr = [6, 2, 5, 2, 2, 6, 6]
len = len(arr)
print(uniqueElement(arr,len))