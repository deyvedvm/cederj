"""
Read two integer values (A and B). After, the program should print the message "Sao Multiplos" (are multiples)
or "Nao sao Multiplos" (aren’t multiples), corresponding to the read values.

Input

The input has two integer numbers.

Output

Print the relative message to the input as stated above.
"""

a, b = map(int, input().split())

if (b % a == 0) or (a % b == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
