"""
DPV 6.19:

Here is yet another variation on the change-making problem (Exercise 6.17).
Given an unlimited supply of coins of denominations x_1, x_2, ..., x_n, 
we wish to make change for a value v using at most k coins; that is, we 
wish to find a set of <= k coins whose total value is v. This might not 
be possible: for instance, if the denominations are 5 and 10 and k = 6, 
then we can make change for 55 but not for 65. Give an efficient 
dynamic-programming algorithm for the following problem.

Input: x_1, ..., x_n; k; v.
Question: Is it possible to make change for v using at most k coins,
of denominations x_1, ..., x_n?
"""
def solution(args: tuple) -> bool:
    denominations, k, v = args
    
    n = len(denominations)
    S = [[None] * (v+1) for _ in range(k+1)]

    for i in range(k+1):
        S[i][0] = True
    for j in range(1, v+1):
        S[0][j] = False

    for i in range(1, k+1):
        for j in range(1, v+1):
            S[i][j] = False
            for l in range(n):
                if j >= denominations[l] and S[i-1][j-denominations[l]]:
                    S[i][j] = True
                    break

    return S[k][v]