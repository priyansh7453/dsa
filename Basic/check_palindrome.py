# def palindrome(n):
#     dup =  n 
#     rev = 0
#     while (n!=0):
#         r = n%10
#         rev = rev*10 + r
#         n = n//10
#     if (dup == rev):
#         return True
#     else:
#         return False


# if __name__ == "__main__":
#     n=14441
#     print(palindrome(n))

def palindrome(n):
    dup =  n 
    rev = 0
    while (n!=0):
        r = n%10
        rev = rev*10 + r
        n = n//10
    if (dup == rev):
        print(True)
    else:
        print(False)

palindrome(1001)