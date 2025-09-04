exercise_details = {
    "2.1": {
        "description": """Use the divide-and-conquer integer multiplication algorithm to multiply the two
binary integers 10011011 and 10111010.

Note: x and y are given as ints, and so should be the output. Also, there's
only a single test for this exercise.""",
        "user_solution_scaffold": """def solution(args: tuple) -> int:
    x, y = args
    
    return 6515
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
exists, in O(log n) time.

Note: len(A) is at least 100 - pretend you don't know that.""",
        "user_solution_scaffold": """def solution(args: tuple) -> int:
    A, x = args # A: List, x: int
    # Your implementation here

    # Returns index of x if found, else -1
    return -1
"""},
    "2.23": {
        "description": """An array A[1...n] is said to have a majority element if more than 
half of its entries are the same. Given an array, the task is to design an 
efficient algorithm to tell whether the array has a majority element, and, 
if so, to find that element. The elements of the array are not necessarily 
from some ordered domain like the integers, and so there can be no comparisons 
of the form "is A[i] > A[j]?". (Think of the array elements as GIF files, say). 
However you can answer questions of the form: "is A[i] = A[j]?" in constant time.

(a) Show how to solve this problem in O(n log n) time. (Hint: Split the array A 
    into two arrays A_1 and A_2 of half the size. Does knowing the majority elements 
    of A_1 and A_2 help you figure out the majority element of A? If so, you can use 
    a divide-and-conquer approach).

(b) Can you give a linear-time algorithm? (Hint: Here's another divide-and-conquer 
approach:
    - Pair up the elements of A arbitrarily, to get n/2 pairs
    - Look at each pair: if the two elements are different, discard both of them; 
    if they are the same, keep just one of them

    Show that after this procedure there are at most n/2 elements left, and that 
    they have a majority element if A does).

Note: regardless if you do a) or b), just return that element.""",
        "user_solution_scaffold": """from typing import List

def solution(A: List) -> any:
    # Your implementation here
    
    # Returns the majority element if exists, else None
    return None
"""
}
}