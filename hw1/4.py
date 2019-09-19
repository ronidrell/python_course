def is_prime(n):
    counter = 0
    for i in range (1, n//2+1):
        if n % i == 0:
            counter += 1
    if counter == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_prime(23))