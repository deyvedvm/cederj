"""
Write a program that read an integer number N (0 ≤ N ≤ 15) that correspont to the order of a bidimentional array of
integers, and build the array according to the above example.

Input

The input consists of several integers numbers, one per line, corresponding to orders from arrays to be built. The end
of input is indicated by zero (0).

Output

For each integer number of input, print the corresponding array according to the example. The values ​​of the array must
be formatted in a field of size T right justified and separated by a space, where T is equal to the number of digits of
the biggest number in the array. None space must be printed after the last character of each row of the array. A blank
line must be printed after each array.
"""

number = int
listNumbers = []

while number != 0:

    number = int(input())

    if 15 >= number >= 0 != number:
        listNumbers.append(number)

for x in listNumbers:

    m = listNumbers[x - 1]
    n = listNumbers[x - 1]

    matrix = [[0 for i in range(0, m)] for j in range(0, n)]

    for i in range(m):
        for j in range(n):
            matrix[i][j] = 2 ** (i + j)

    for row in matrix:
        print(''.join([str(elem).rjust(x) for elem in row]))
    print()
