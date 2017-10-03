"""
Read 3 floating-point numbers. After, print the roots of bhaskara’s formula. If it's impossible to calculate the roots
because a division by zero or a square root of a negative number, presents the message “Impossivel calcular”.

Input

Read 3 floating-point numbers A, B and C.

Output

Print the result with 5 digits after the decimal point or the message if it is impossible to calculate.
"""

A, B, C = str(input()).split()

A = float(A)
B = float(B)
C = float(C)

delta = B ** 2 - 4 * A * C

if delta < 0 or A == 0:
    print("Impossivel calcular")
else:
    R1 = (-B + delta ** 0.5) / 2 * A
    R2 = (-B - delta ** 0.5) / 2 * A

    print("R1 = %.5f" % R1)
    print("R2 = %.5f" % R2)
