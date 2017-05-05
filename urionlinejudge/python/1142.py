"""
Write a program that reads an integer N. This N is the number of output lines printed by this program.

Input

The input file contains an integer N.

Output

Print the output according to the given example.
"""

number = int(input())
pum = 1

for number in range(0, number):
    print("%d %d %d PUM" % (pum, pum + 1, pum + 2))
    pum += 4

