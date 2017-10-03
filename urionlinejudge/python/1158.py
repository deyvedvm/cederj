"""
Read an integer N that is the number of test cases that follows. Each test case contains two integers X and Y. Print
one output line for each test case that is the sum of Y odd numbers from X including it if is the case. For example:
for the input 4 5, the output must be 45, that is: 5 + 7 + 9 + 11 + 13
for the input 7 4, the output must be 40, that is: 7 + 9 + 11 + 13

Input

The first line of the input is an integer N that is the number of test cases that follow. Each test case is a line
containing two integer X and Y.

Output

Print the sum of all consecutive odd numbers from X.
"""

listNumbers = []

N = int(input())

for i in range(N):

    X, Y = map(int, input().split())

    if X % 2 != 0:
        number = X
    else:
        number = 0

    for j in range(Y):
        X += 1
        if X % 2 != 0:
            number += X

    listNumbers.append(number)

for row in listNumbers:
    print(row)
