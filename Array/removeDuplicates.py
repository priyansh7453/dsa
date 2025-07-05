def remove_duplicates(arr):
    index = 1
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            arr[index] = i
            arr[index] += 1
    
    print(index)
    


    

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    remove_duplicates(arr)