def Armstrong_num(n):
    dup = n
    armstrong_num=0
    size = len(str(n))
    while(n!=0):
        r = n%10
        armstrong_num = armstrong_num + r**size
        n=n//10
    if dup == armstrong_num:
        print(True)
    else:
        print(False)
    # print(armstrong_num)
        
        


Armstrong_num(1553)