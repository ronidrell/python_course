def is_self_dividing(n):
    n = abs(n)
    num = n
    count = 0
    countOfNum = 0
    while n != 0:
        if num % (n % 10) == 0:
            count += 1
        countOfNum += 1
        n = n / 10
        if count == countOfNum:
            return True
        else:
            return False

if __name__ == "__main__":
    print(is_self_dividing(-24))
