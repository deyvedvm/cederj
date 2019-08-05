numbers = [6, 3, 7, 5, 8, 9, 1, 2]


def reversingSequence(sequence):
    floor = int(len(sequence) / 2)

    for index in range(floor):
        temporaryVariable = sequence[index]
        sequence[index] = numbers[len(sequence) - index - 1]
        sequence[len(sequence) - index - 1] = temporaryVariable
    return sequence


# print(numbers)

# print(numbers[::-1])

print(numbers)

invertedNumbers = reversingSequence(numbers)

print(invertedNumbers)
