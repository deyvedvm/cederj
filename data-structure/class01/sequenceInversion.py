numbers = [6, 3, 7, 5, 8, 9, 1, 2]

print(numbers)

print(numbers[::-1])

floor = int(len(numbers) / 2)

for index in range(floor):
    temporaryVariable = numbers[index]
    numbers[index] = numbers[len(numbers) - index - 1]
    numbers[len(numbers) - index - 1] = temporaryVariable

print(numbers)
