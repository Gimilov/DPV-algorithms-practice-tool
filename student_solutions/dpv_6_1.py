"""
DPV 6.1:

A contiguous subsequence of a list S is a subsequence made up of consecutive elements of S. 
For instance, if S is [5,15,-30,10,-5,40,10], then [15,-30,10] is a contiguous subsequence 
but [5,15,40] is not.

Input: A list of numbers [a_1, a_2, ..., a_n]
Output: The contiguous subsequence of maximum sum (a subsequence of length zero has sum zero)

For the preceding example, the answer would be [10,-5,40,10] with sum 55.

Hint: For each j ∈ {1,2,...,n}, consider contiguous subsequences ending exactly at position j.

Note: output a list, not just the sum.
"""

from typing import List

def solution(input_arr: List[int]) -> List[int]:
    n = len(input_arr)
    if n == 0:
        return []
    
    dp = [0] * n
    start = [0] * n
    
    dp[0] = input_arr[0]
    start[0] = 0
    max_sum = dp[0]
    max_index = 0

    for i in range(1, n):
        if dp[i-1] > 0:
            dp[i] = input_arr[i] + dp[i-1]
            start[i] = start[i-1]
        else:
            dp[i] = input_arr[i]
            start[i] = i
        
        if dp[i] > max_sum:
            max_sum = dp[i]
            max_index = i

    # If maximum sum is negative, return empty list
    if max_sum < 0:
        return []
    
    return input_arr[start[max_index] : max_index+1]