"""
You will be given an array of N numbers, where everyone will be in pairs. But one of those numbers ended up without 
peer, you can identify what is that number?

For example, A = {1, 1, 3, 3, 5, 5, 5}, the number stood alone was 5.

Input

The input consists of several test cases. Each test case is composed of a line having an integer N (1 ≤ N < 10^5), 
followed by N number (1 ≤ A ≤ 10^12).

Output

For each test case print only the number that stood alone. It is guaranteed that only one number is alone
"""

"""
def find_a_number(array, number):
    for n in range(1, len(array)):
        if array[n] == number:
            return number


def find_a_index(array, number):
    for n in range(1, len(array)):
        if array[n] == number:
            return n


sizeOfArray = int(input())

arrayOfNumbers = (input()).split()

numberFound = 0

arrayWithoutPairs = []

for i in range(sizeOfArray):

    indexFound = find_a_number(arrayOfNumbers, arrayOfNumbers[i])

    if arrayOfNumbers[i] == arrayOfNumbers[indexFound]:
        print()
        # del arrayOfNumbers[i]
        # del arrayOfNumbers[indexFound]
    else:
        numberFound = arrayOfNumbers[i]

print(numberFound)
"""


def lonelyinteger(a):
    answer = 0
    for candidate in a:
        answer ^= candidate
    return answer


sizeOfArray = int(input())
arrayOfNumbers = map(int, input().strip().split(" "))
print(lonelyinteger(arrayOfNumbers))



# rever o código antes de salvar no Github