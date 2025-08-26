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
    # Your DP and backtracking code here
    n = len(hotels)
    ind_tracker = [-1] * n 
    S = [-1] * n 

    # base case
    S[0] = (200 - hotels[0])**2

    # recurrence relation
    for i in range(1, n):
        best_j_min = (200 - hotels[i])**2
        for j in range(i):
            from_hotel = S[j] + (200 - (hotels[i] - hotels[j]))**2
            if from_hotel < best_j_min:
                best_j_min = from_hotel
                ind_tracker[i] = j 
        
        S[i] = best_j_min

    # backtracking
    print(S)
    res = []
    curr_ind = n-1 # we have to finish in the last hotel
    while curr_ind != -1:
        res = [hotels[curr_ind]] + res 
        curr_ind = ind_tracker[curr_ind] 

    return res

