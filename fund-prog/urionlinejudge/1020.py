i = int(input())

a = i / 365
m = (i % 365) / 30
d = (i % 365) % 30

print("%d ano(s)" % a)
print("%d mes(es)" % m)
print("%d dia(s)" % d)
