from cmath import sqrt

x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())

d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("%.4f" % d)

