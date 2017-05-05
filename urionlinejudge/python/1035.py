"""
Read 4 integer values A, B, C and D. Then if B is greater than C and D is greater than A and if the sum of C and D is
greater than the sum of A and B and if C and D were positives values and if A is even, write the message “Valores
aceitos” (Accepted values). Otherwise, write the message “Valores nao aceitos” (Values not accepted).

Input

Four integer numbers A, B, C and D.

Output

Show the corresponding message after the validation of the values​​.
"""


def greater(x, y):
    if x > y:
        return True
    else:
        return False


def even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def positive(x):
    if x > 0:
        return True
    else:
        return False


A, B, C, D = str(input()).split()

A = int(A)
B = int(B)
C = int(C)
D = int(D)

BC = greater(B, C)
DA = greater(D, A)
CDAB = greater(C + D, A + B)

if BC and DA and CDAB and positive(C) and positive(D) and even(A):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
