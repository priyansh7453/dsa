def count_digits(n):
    cnt  =0
    while (n!=0):
        cnt = cnt + 1
        n = n//10
    return cnt


if __name__ == "__main__":
    n=100444
    print(count_digits(n))