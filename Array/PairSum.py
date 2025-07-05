def PairSum(arr,n,target):
    # Create a hash map to store the frequency of each element
    s = set(arr) 
    result = [] 
    
    for i in arr:
        compliment = target - i
        if compliment in s:
            result.append(compliment,i)
    return result

# Driver code
arr = [3, 2, 4, 3]
target = 6
n = len(arr)
print(PairSum(arr,n,target))