def merge(nums1, m, nums2, n):
    result= []
    i = j = 0
    while i < m and j>n:
        if nums1[i] < nums2[i]:
            result.append(nums1[i])
            i+=1
        else:
            result.append(nums1[j])
            j+=1
    
    while i < m:
        result.append(nums1[i])
        i+=1
    while j < n:
        result.append(nums2[j])
        j+=1
        
    for i in range(m+n):
        nums1[i] = result[i]


nums1 = [1, 3, 5, 0, 0, 0]
m = 3
nums2 = [2, 4, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]