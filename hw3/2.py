def devider_generator(number):
    cursor = 1
    while True:
        if number % cursor == 0:
            yield cursor
        cursor += 1
        if cursor > number:
            break

deviders = devider_generator(1024)
for i in deviders:
    print(i)
