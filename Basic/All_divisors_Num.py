# def All_divisor_Number(n):
#     for i in range(1,n+1):
#         if(n%i==0):
#             print(i)
#         else:
#             continue
    
# All_divisor_Number(21191)


def All_divisor_Number(n):
    ansarr = []
    for i in range(1,n+1):
        if(n%i==0):
            ansarr.append(i)
            # print(ansarr)
        else:
            continue
    print(ansarr)
All_divisor_Number(20)

