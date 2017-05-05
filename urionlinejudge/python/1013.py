"""
Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior". Use the
following formula:

MaiorAB = (A + B + abs(A - B)) / 2

Input

The input file contains 3 integer values.

Output

Print the greatest of these three values followed by a space and the message “eh o maior”.
"""


def maiorXY(x, y):
    return (x + y + abs(x - y)) / 2

a, b, c = str(input()).split()

a = int(a)
b = int(b)
c = int(c)

greater = maiorXY(maiorXY(a, b), c)

print("%d eh o maior" % greater)
