"""
DPV 6.18:

Consider the following variation on the change-making problem (Exercise 6.17):  
you are given denominations x_1, x_2, ..., x_n, and you want to make 
change for a value v, but you are allowed to use each denomination 
at most once. For instance, if the denominations are 1, 5, 10, 20, 
then you can make change for 16 = 1 + 15 and for 31 = 1 + 10 + 20 
but not for 40 (because you can't use 20 twice).  

Input: Positive integers x_1, x_2, ..., x_n; another integer v.  
Output: Can you make change for v, using each denomination x_i at most once?  

Show how to solve this problem in time O(nv).
"""
def solution(args: tuple) -> bool:
    denominations, v = args
    n = len(denominations)
    S = [[None] * (n+1) for _ in range(v+1)]
    
    for j in range(v+1):
        S[j][0] = False # (no positive value with 0 coins)
    for i in range(n+1):
        S[0][i] = True # (0 can always be formed)

    for j in range(1, v+1):
        for i in range(1, n+1):
            if j >= denominations[i - 1]:
                # either use x_i once, or skip it
                S[j][i] = S[j][i - 1] or S[j - denominations[i - 1]][i - 1]
            else:
                # cannot use x_i, must skip
                S[j][i] = S[j][i - 1]
            
    return S[v][n]
