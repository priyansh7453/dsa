def find_all_pairs_two_pointer(arr,target):
    left = 0
    right = len(arr) - 1
    result = []
    
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            result.append((arr[left],arr[right]))
            left+=1
            right-=1
        elif curr_sum > target:
            right-=1
        else :
            left+=1
    return result


# Example usage
arr = [1, 5, 7, -1, 5, 2]
target = 6
print(find_all_pairs_two_pointer(arr, target))