"""
Faça um programa que manipule strings. Especificamente, seu programa deverá:

a) Ler strings da entrada padrão até que uma string vazia seja digitada;
b) Escrever na saída padrão todas as strings que, quando lidas do primeiro até o último caractere, seja igual a string
lida do último para o primeiro caracter. Isto é, strings que sejam palíndromes. Por exemplo, “ana” é palíndrome,
enquanto que “banana” não é.
c) Ao final, escrever a quantidade de strings lidas, a quantidade de strings palíndromes e a quantidade de strings
palíndromes que contenham pelo menos uma vogal.

Restrição Serão aceitos na correção apenas programas que contenham pelo menos um subprograma.

"""

quantidade_strings_lidas = 0

quantidade_strings_palindromes = 0

quantidade_strings_palindromes_com_vogal = 0


def eh_palindrome(string):
    return string == string[::-1]


def contem_votal(string):
    for caracter in string:

        if caracter in {'a', 'e', 'i', 'o', 'u'}:
            return True

    return False


while True:
    string = input()

    if string == "":
        break

    quantidade_strings_lidas += 1

    if eh_palindrome(string):
        quantidade_strings_palindromes += 1

    if contem_votal(string):
        quantidade_strings_palindromes_com_vogal += 1

print("Quantidade de strings lidas {}".format(quantidade_strings_lidas))
print("Quantidade de strings palíndromes {}".format(quantidade_strings_palindromes))
print("Quantidade de strings palíndromes com vogal {}".format(quantidade_strings_palindromes_com_vogal))
