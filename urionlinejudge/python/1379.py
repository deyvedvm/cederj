"""
The mean of three integers A, B and C is (A + B + C)/3. The median of three integers is the one that would be in the
middle if they are sorted in non-decreasing order. Given two integers A and B, return the minimum possible integer C
such that the mean and the median of A, B and C are equal.

Input

Each test case is given in a single line that contains two integers A and B (1 ≤ A ≤ B ≤ 109). The last test case is
followed by a line containing two zeros.

Output

For each test case output one line containing the minimum possible integer C such that the mean and the median of A, B
and C are equal.
"""

A = int
B = int
C = int

while B != 0 and C != 0:

    B, C = map(int, input().split())

    if 1 <= B <= C <= 10 ** 9:
        A = 2 * B - C
        print(A)



