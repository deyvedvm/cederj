"""
Read the start time and end time of a game, in hours. Then calculate the duration of the game, knowing that the game can
begin in a day and finish in another day, with a maximum duration of 24 hours. The message must be printed in portuguese
“O JOGO DUROU X HORA(S)” that means “THE GAME LASTED X HOUR(S)”

Input

Two integer numbers representing the start and end time of a game.

Output

Print the duration of the game as in the sample output.
"""

startGame, endGame = map(int, input().split())

if (startGame >= endGame):
    hours = (24 - startGame) + endGame
if (startGame < endGame):
    hours = (endGame- startGame)

print("O JOGO DUROU %d HORA(S)" % hours)
