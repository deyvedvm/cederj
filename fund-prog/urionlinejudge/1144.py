"""
Write a program that reads an integer N. N * 2 lines must be printed by this program according to the example below.
For numbers with more than 6 digits, all digits must be printed (no cientific notation allowed).

Input

The input file contains an integer N (1 < N < 1000).

Output

Print the output according to the given example.
"""

number = int(input())

if 1 < number < 1000:

    for i in range(number):

        a = i + 1
        b = a * a
        c = a * a * a
        print(a, b, c)
        print(a, b + 1, c + 1)


