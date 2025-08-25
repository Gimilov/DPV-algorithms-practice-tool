
exercise_details = {
    "6.1": {
        "description": """A contiguous subsequence of a list S is a subsequence made up of consecutive elements of S. 
For instance, if S is [5,15,-30,10,-5,40,10], then [15,-30,10] is a contiguous subsequence 
but [5,15,40] is not.

Input: A list of numbers [a_1, a_2, ..., a_n]
Output: The contiguous subsequence of maximum sum (a subsequence of length zero has sum zero)

For the preceding example, the answer would be [10,-5,40,10] with sum 55.

Hint: For each j ∈ {1,2,...,n}, consider contiguous subsequences ending exactly at position j.

Note: output a list, not just the sum.""",
        "user_solution_scaffold": """from typing import List

def solution(input_arr: List[int]) -> List[int]:
    # your solution here
    return []
"""},
    "6.2": {
    "description": """You are going on a long trip. You start at mile post 0. Along the way 
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

Note: output a list without including 0""",
    "user_solution_scaffold": """from typing import List

def solution(hotels: List[int]) -> List[int]:
    # Your DP and backtracking code here
    return [] 
"""},
    "6.3": {
    "description": """Yuckdonald's is considering opening a series of restaurants along 
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
profit subject to the given constraints.""",
    "user_solution_scaffold": """from typing import List

def solution(distances: List[int], profits: List[int], k: int) -> int:
    # distances: sorted list of mile positions [m1, m2, ..., mn]
    # profits: list of expected profits [p1, p2, ..., pn]
    # k: minimum required distance between any two restaurants
    # Return: maximum expected total profit
    return 6515
"""},
    "6.4": {
    "description": """You are given a string of n characters s[1...n], which you 
believe to be a corrupted text document in which all punctuation 
has vanished (so that it looks something like “itwasthebestoftimes…”). 
You wish to reconstruct the document using a dictionary, which is 
available in the form of a Boolean function dict(⋅): 

for any string w, dict(w) returns true if w is a 
valid word, false otherwise.

(a) Give a dynamic programming algorithm that determines whether 
the string s[⋅] can be reconstituted as a sequence of valid words. 
The running time should be at most O(n^2), assuming calls to dict 
take unit time.

(b) In the event that the string is valid, make your algorithm 
output the corresponding sequence of words.

Note: for practice, focus on b) only.""",
    "user_solution_scaffold": """from typing import List

def solution(s: str, dct: dict) -> List[str]:
    # Helper function to check if a word is in the dictionary
    def dict_func(word):
        return word in dct
    
    # Your DP and backtracking logic here
    return []
"""},
    "6.11": {
    "description": """Given two strings x = x_1x_2...x_n and y = y_1y_2...y_m, we wish 
to find the length of their longest common subsequence, that is, 
the largest k for which there are indices i_1 < i_2 < ... < i_k and 
j_1 < j_2 < ... < j_k with x_i1x_i2...x_ik = y_j1y_j2...y_jk. Show 
how to do this in time O(mn).""",
    "user_solution_scaffold": """def solution(x: str, y: str) -> int:
    # Return the length of the longest common subsequence
    return 0
"""}
}

