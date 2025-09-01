exercise_details = {
    "2.1": {
        "description": """Use the divide-and-conquer integer multiplication algorithm to multiply the two
binary integers 10011011 and 10111010.

Note: x and y are given as strings, and so should be the output. Also, there's
only a single test for this exercise.""",
        "user_solution_scaffold": """def solution(args: tuple) -> str:
    x, y = args
    
    return '0101010'
"""},
    "2.5": {
    "description": """Solve the following recurrence relations and give a Θ (Big Theta) 
bound for each of them.

(a) T(n) = 2T(n/3) + 1

(b) T(n) = 5T(n/4) + n

(c) T(n) = 7T(n/7) + n

(d) T(n) = 9T(n/3) + n^2

(e) T(n) = 8T(n/2) + n^3

(f) T(n) = 49T(n/25) + n^{3/2} log n

(g) T(n) = T(n-1) + 2

(h) T(n) = T(n-1) + n^c, where c ≥ 1 is a constant

(i) T(n) = T(n-1) + c^n, where c > 1 is some constant

(j) T(n) = 2T(n-1) + 1

(k) T(n) = T(√n) + 1

Note: this exercise has no test suite, but if you run it, answers will be displayed.""",
    "user_solution_scaffold": """def solution():
    # no need for any implementation
    pass 
"""},
    "2.16": {
        "description": """You are given an infinite array A[.] in which the first n cells contain 
integers in sorted order and the rest of the cells are filled with ∞. You 
are not given the value of n. Describe an algorithm that takes an integer x 
as input and finds a position in the array containing x, if such a position 
exists, in O(log n) time. (If you are disturbed by the fact that the array A 
has infinite length, assume instead that it is of length n, but that you don't 
know this length, and that the implementation of the array data type in your 
programming language returns the error message ∞ whenever elements A[i] with 
i > n are accessed.)

Note: len(A) is 1,000,000 - pretend you don't know that.""",
        "user_solution_scaffold": """def solution(args: tuple) -> int:
    A, x = args # A: List, x: int
    # Your implementation here

    # Returns index of x if found, else -1
    return -1
"""
}
}