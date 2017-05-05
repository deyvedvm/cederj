"""
Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in
hours:minutes:seconds.

Input

The input file contains an integer N.

Output

Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.
"""

n = int(input())

seconds = n % 60
minutes = (n / 60) % 60
hours = n / 60 / 60

print("%d:%d:%d" % (hours, minutes, seconds))
