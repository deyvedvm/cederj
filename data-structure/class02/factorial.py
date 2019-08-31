def fat(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * fat(number - 1)


print(fat(1))

print(fat(2))

print(fat(3))

print(fat(5))
