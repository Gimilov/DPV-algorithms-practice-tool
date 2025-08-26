"""
DPV 6.2:

You are going on a long trip. You start at mile post 0. Along the way 
there are n hotels, at mile posts a_1 < a_2 < ... < a_n, where each 
a_i is measured from the starting point. The only places you are 
allowed to stop are at these hotels, but you can choose which of 
the hotels you stop at. You must stop at the final hotel (at distance 
a_n), which is your destination.

You'd ideally like to travel 200 miles a day, but this may not be 
possible (depending on the spacing of the hotels). If you travel 
x miles during a day, the penalty for that day is (200 - x)^2. You 
want to plan your trip so as to minimize the total penalty - that 
is, the sum, over all travel days, of the daily penalties. Give an 
efficient algorithm that determines the optimal sequence of hotels at
which to stop.

Note: output a list
"""
from typing import List

def solution(hotels: List[int]) -> List[int]:
    n = len(hotels)
    # Add starting point (mile 0) to the beginning
    all_points = [0] + hotels
    
    # D(i) = minimum penalty to reach point i
    D = [0] * (n + 1)
    # prev[i] stores the previous hotel index for point i
    prev = [-1] * (n + 1)
    
    # Base case: starting at mile 0 has penalty 0
    D[0] = 0
    
    # Compute D(i) for each hotel i = 1 to n
    for i in range(1, n + 1):
        D[i] = float('inf')
        for j in range(i):
            distance = all_points[i] - all_points[j]
            penalty = (200 - distance) ** 2
            total_penalty = D[j] + penalty
            
            if total_penalty < D[i]:
                D[i] = total_penalty
                prev[i] = j
    
    # Backtrack 
    result = []
    current = n  # destination is the last hotel 
    
    while current > 0:  # stop when we reach starting point
        result.append(all_points[current])
        current = prev[current]
    
    return result[::-1] # reverse 

