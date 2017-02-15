"""

In this problem you have to read an integer value and calculate the smallest possible number of banknotes in which the 
value may be decomposed. The possible banknotes are 100, 50, 20, 10, 5, 2 e 1. Print the read value and the list of 
banknotes.

Input

The input file contains an integer value N (0 < N < 1000000).

Output

Print the read number and the minimum quantity of each necessary banknotes in Portuguese language, as the given example. 
Do not forget to print the end of line after each line, otherwise you will receive “Presentation Error”.

"""

note = int(input())

print(note)
print('%d nota(s) de R$ 100,00' % (note / 100))
print('%d nota(s) de R$ 50,00' % (note % 100 / 50))
print('%d nota(s) de R$ 20,00' % ((note % 100) % 50 / 20))
print('%d nota(s) de R$ 10,00' % (((note % 100) % 50) % 20 / 10))
print('%d nota(s) de R$ 5,00' % ((((note % 100) % 50) % 20) % 10 / 5))
print('%d nota(s) de R$ 2,00' % (((((note % 100) % 50) % 20) % 10) % 5 / 2))
print('%d nota(s) de R$ 1,00' % ((((((note % 100) % 50) % 20) % 10) % 5) % 2 / 1))
