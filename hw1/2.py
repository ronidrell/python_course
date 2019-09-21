def get_digit_sum(n):
    n = abs(n)
    s = 0
    while n != 0:
        s = s + n % 10
        n = n // 10
    return s


def is_beaty(n):
    sum = get_digit_sum(n)
    if n % sum == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_beaty(-31))
