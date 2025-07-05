def prime_number(n):
    for i in range(2,n):
        if(n%i==0):
            return "False"
    return "True"
def count_prime(m):
    count = 0
    for i in range(2,m):
        if(prime_number(i)=="True"):
            count+=1
    return count
# print(prime_number(11)) # True
# print(prime_number(15)) # False
print(count_prime(20)) # 4
    
    
