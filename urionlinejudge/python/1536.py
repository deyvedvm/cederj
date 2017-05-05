"""
The Libertadores Cup is the main soccer competition among professional clubs of South America, organized by the South 
American Confederation of Soccer (CONMEBOL). This cup is known for having a very complicated regulation, especially for 
the quarter finals and semi-final.

These stages are played roundtrip matches in the playoff system. Wins the team that makes the highest score accumulated 
in the two matches, with 3 points for a win and 1 point in case of a tie, both per match. In case of a tie in score, 
the tiebreaker criteria are:

1) goal difference (number of goals for minus the number of goals against)

2) most goals scored in the away match and

3) penalty shootout

All criteria must be applied considering the accumulated of the two matches.

Can you develop an algorithm that, given the results of the roundtrip matches, it identifies the winning team?

Input

The first line of input gives the number of test cases N (1 ≤ N ≤ 100). Each test case consists of two scores: the 
outcome of match 1 and the outcome of the 2. The score is represented by the format M x V, where M (1 ≤ M ≤ 100) is the 
number of goals for principal team and V (1 ≤ V ≤ 100) is the number of goals for the visiting team. As for each test 
case there are 2 matches, consider that Team 1 is always the principal of the first match and the visitor of the second 
and vice versa for Team 2.

Output

For each test case, print a line containing "Time 1" (without quotes) if Team 1 is the winner of the playoff, " Time 2" 
(without quotes) if the Team 2 is the winner of the playoff and "Penaltis" (without quotes) if you can not identify the 
winner in conventional time.
"""

n = int(input())

if 1 <= n <= 100:

    for i in range(n):

        somaGolsTime1 = 0
        somaGolsTime2 = 0
        somaGolsForaTime1 = 0
        somaGolsForaTime2 = 0

        for j in range(2):

            M, V = input().split("x")

            if j % 2 == 0:
                somaGolsTime1 += int(M)
                somaGolsTime2 += int(V)
                somaGolsForaTime2 = int(V)
            else:
                somaGolsTime1 += int(V)
                somaGolsTime2 += int(M)
                somaGolsForaTime1 = int(V)

        if somaGolsTime1 > somaGolsTime2:
            print("Time 1")
        elif somaGolsTime2 > somaGolsTime1:
            print("Time 2")
        elif somaGolsForaTime1 > somaGolsForaTime2:
            print("Time 1")
        elif somaGolsForaTime2 > somaGolsForaTime1:
            print("Time 2")
        else:
            print("Penaltis")
