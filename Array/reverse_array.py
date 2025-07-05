# normal reverse order
def reverse(array,k):
    # reversed = array[::-1]
    # return reversed
    # start=0
    end=len(array)-1    
    ind = array.index(k)
    print(ind)
    # if len(array) == 0:
    #     return array
    # if start == end:
    #     return array
    
    
    # while start <= end :
    #     array[start],array[end] = array[end],array[start]
    #     start += 1
    #     end -= 1
    # return array
    start=ind+1
    while start <= end :
        array[start],array[end] = array[end],array[start]
        start += 1
        end -= 1
    return array

array = [1,9,5,3,0]
k =5
print(reverse(array,k))

