"""
DPV 6.11:

Given two strings x = x_1x_2...x_n and y = y_1y_2...y_m, we wish 
to find the length of their longest common subsequence, that is, 
the largest k for which there are indices i_1 < i_2 < ... < i_k and 
j_1 < j_2 < ... < j_k with x_i1x_i2...x_ik = y_j1y_j2...y_jk. Show 
how to do this in time O(mn).
"""
def solution(args: tuple) -> int:
    x, y = args
    # Return the length of the longest common subsequence
    n = len(x)
    m = len(y)
    S = [[None] * (m+1) for _ in range(n+1)]

    # base
    for i in range(n+1):
        S[i][0] = 0
    for j in range(m+1):
        S[0][j] = 0

    # dp 
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                S[i][j] = 1 + S[i-1][j-1]
            else:
                S[i][j] = max(S[i-1][j], S[i][j-1])

    return S[-1][-1]