
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

def solution(input_arr: List[int]):
    # your solution here
    return [6, 5, 1, 5]
"""}
}

