"""
DPV 6.17:

Given an unlimited supply of coins of denominations x_1, x_2, ..., x_n, 
we wish to make change for a value v; that is, we wish to find a set 
of coins whose total value is v. This might not be possible: for instance, 
if the denominations are 5 and 10 then we can make change for 15 but not 
for 12. Give an O(nv) dynamic-programming algorithm for the following problem.

Input: x_1, ... , x_n; v

Question: Is it possible to make change for v using coins of denominations 
x_1, ... , x_n?
"""
def solution(args: tuple) -> bool:
    # unpack args
    denominations, v = args

    n = len(denominations)
    S = [False] * (v+1) 

    S[0] = True
    for i in range(1, v+1):
        for j in range(n):
            if i >= denominations[j] and S[i - denominations[j]]:
                S[i] = S[i - denominations[j]]

    return S[v]