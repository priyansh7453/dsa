# Python3 program to count frequencies 
# of array items
def sort01(arr, n):

    mp = dict()

    # Traverse through array elements 
    # and count frequencies
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
            

    # Traverse through map and print frequencies
    for x in sorted(mp.keys()):
        # print(x, " ", mp[x])
        for i in range(mp[x]):
            print(x,end="")
        

# Driver code
arr = [1,1,0,0,0,0,1,0]
n = len(arr)
sort01(arr, n)