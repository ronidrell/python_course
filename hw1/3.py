def is_power_of_two(n):
    answer = True
    while answer == True and n != 1:
        if n % 2 == 0 :
            answer = True
            n = n // 2
        else:
            answer = False
    return answer

if __name__ == "__main__":
    print(is_power_of_two(32))