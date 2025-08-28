"""
DPV 6.8:

Given two strings x = x1x2...xn and y = y1y2...ym, we wish to find the length
of their longest common substring, that is, the largest k for which there are
indices i and j with x_i x_{i+1} ... x_{i+k-1} = y_j y_{j+1} ... y_{j+k-1}. 
Show how to do this in time O(mn).
"""
def solution(args: tuple) -> int:
    x, y = args
    n = len(x)
    m = len(y)

    S = [[None] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        S[i][0] = 0
    for j in range(m+1):
        S[0][j] = 0

    max_len = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            S[i][j] = 1 + S[i-1][j-1] if x[i-1] == y[j-1] else 0
            max_len = max(max_len, S[i][j])  
            
    return max_len
