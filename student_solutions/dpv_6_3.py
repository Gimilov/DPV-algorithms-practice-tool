"""
DPV 6.3:

Yuckdonald's is considering opening a series of restaurants along 
Quaint Valley Highway (QVH). The n possible locations are along a 
straight line, and the distances of these locations from the start 
of QVH are, in miles and in increasing order, m_1, m_2, ..., m_n. 
The constraints are as follows:

- At each location, Yuckdonald's may open at most one restaurant. 
The expected profit from opening a restaurant at location i is p_i, 
where p_i > 0 and i = 1, 2, ..., n.

- Any two restaurants should be at least k miles apart, where k 
is a positive integer.

Give an efficient algorithm to compute the maximum expected total 
profit subject to the given constraints.
"""
from typing import List

def solution(args: tuple) -> int:
    distances, profits, k = args  # unpack tuple: List[int], List[int], int
    
    n = len(distances)
    if n == 0:
        return 0
    S = [0] * n

    # base case (book solutions with different base case)
    S[0] = profits[0]
    # dp
    for i in range(1, n):
        max_j = 0
        for j in range(i):
            if distances[i] - distances[j] >= k and S[j] > max_j:
                max_j = S[j]
        
        S[i] = max(S[i-1] ,profits[i] + max_j)

    print(S)
    return max(S)
