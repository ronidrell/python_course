def get_digit_sum(n):
    n = abs(n)
    s=0
    while n != 0:
        s = s + n%10
        n = n//10
    return s

if __name__ == "__main__":
    print(get_digit_sum(-12345))