"""
Which integer numbers can be represented by a sum of two integer squares?

That is the question that your program must respond!

For example, the number 41 can be represented as (-4)2 + 52 = 41, but 7 cannot be represented in the same way.

Input
The input consists of several lines, each line contains an integer with absolute value less than or equal to 10000.

Output
For each line, print "YES" if the number can be represented by a sum of two integer squares, otherwise print "NO".
"""

number = int(input())

if number <= 10000:

    if number % 4 == 1 or number == 2:
        print("YES")
    else:
        print("NO")
