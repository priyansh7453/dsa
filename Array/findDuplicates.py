def findDuplicate(arr,len):
    # Create a hash map to store the frequency of each element
    hash_map = {}
    for i in range(len):
        if arr[i] in hash_map:
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    
    
    for i in hash_map:
        # print(i ,' ', hash_map[i])
        # Find the element with frequency more than 1
        if hash_map[i] >1:
            print(i)
        
    
    
# Driver code
arr = [10, 20, 20, 10, 10, 20, 5, 20 ]
n = len(arr)
findDuplicate(arr,n)