"""
Make a program that reads three floating point values: A, B and C. Then, calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of ​​the square that has side B.
e) the area of the rectangle that has sides A and B.

Input

The input file contains three double values with one digit after the decimal point.

Output

The output file must contain 5 lines of data. Each line corresponds to one of the areas described above, always with a
corresponding message (in Portuguese) and one space between the two points and the value. The value calculated must be
presented with 3 digits after the decimal point.
"""

pi = 3.14159

A, B, C = str(input()).split()

A = float(A)
B = float(B)
C = float(C)

triangle = A * C / 2
circle = pi * C ** 2
trapezium = (A + B) * C / 2
square = B ** 2
rectangle = A * B

print("TRIANGULO: %.3f" % triangle)
print("CIRCULO: %.3f" % circle)
print("TRAPEZIO: %.3f" % trapezium)
print("QUADRADO: %.3f" % square)
print("RETANGULO: %.3f" % rectangle)

