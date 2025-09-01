"""
DPV 6.5:

Pebbling a checkerboard. We are given a checkerboard which has 4 rows and n 
columns, and has an integer written in each square. We are also given a set of 2n 
pebbles, and we want to place some or all of these on the checkerboard (each 
pebble can be placed on exactly one square) so as to maximize the sum of the 
integers in the squares that are covered by pebbles. There is one constraint: for a 
placement of pebbles to be legal, no two of them can be on horizontally or 
vertically adjacent squares (diagonal adjacency is fine).

    (a) Determine the number of legal patterns that can occur in any column (in 
    isolation, ignoring the pebbles in adjacent columns) and describe these 
    patterns.

Call two patterns compatible if they can be placed on adjacent columns to form a 
legal placement. Let us consider subproblems consisting of the first k columns  
1 ≤ k ≤ n. Each subproblem can be assigned a type, which is the pattern 
occurring in the last column.

(b) Using the notions of compatibility and type, give an O(n)-time dynamic
programming algorithm for computing an optimal placement.
"""

"""
a) The number of possible legal pattern is:
    > 1 pattern with no pebbles at all
    > 4 patterns with just a single pebble
    > 3 patterns with two pebbles
This gives us 8 different patterns.

b) First, number all legal patterns from 1 to 8 and define S ⊆ {1,...,8} × {1, ..., 8}
to be all pairs (a, b) so that pattern a is compatible with patter b. 

T[i, j] = maximum total sum achievable on columns 1,...,i such that column i uses pattern j.


Then, the recurrence relation is:
    T[0, j] = 0, 1<=j<=8
    T[i, j] = column_value(i, j) + max(T[i-1, k] : (k,j) ∈ S),
        where column_value(i, j) is the total value of numbers covered by pebbles 
        at column i, using pattern j.

To recover the optimal placement, store a backpointer:
    P[i, j] = argmax_{k : (k,j) ∈ S}(L[i-1, k])
Then pick j* = argmax_j(L[n,j]) and follow P backwards.

Number of subproblems: O(n)
Runtime to fill the table: O(n)
Method to extract the return: max(T[n, j] : 1<=j<=8) (if we consider just the sum, 
otherwise follow P backwards)
Runtime to extract final return: O(1) if just the sum, O(n) if backtracking

"""
from typing import List, Tuple

def solution(board: List) -> int:
    # board is a 4 x n 2D list of integers
    # Returns maximum sum achievable
    # Your implementation here
    n = len(board[0])  # number of columns

    # --- Step 1: enumerate legal patterns ---
    # Each pattern is a tuple of row indices (0-based)
    patterns = [
        (),                       # empty
        (0,), (1,), (2,), (3,),   # single pebbles
        (0,2), (0,3), (1,3)       # two pebbles
    ]
    num_patterns = len(patterns)

    # --- Step 2: compatibility check ---
    def compatible(p1: Tuple[int], p2: Tuple[int]) -> bool:
        # must not share same row (vertical adjacency across columns)
        return all(r1 != r2 for r1 in p1 for r2 in p2)

    compat = [[compatible(patterns[k], patterns[j])
               for j in range(num_patterns)]
              for k in range(num_patterns)]

    # --- Step 3: precompute column values for each pattern ---
    def column_value(col: int, pat: Tuple[int]) -> int:
        return sum(board[r][col] for r in pat)

    # --- Step 4: DP table ---
    # T[i][j] = max total sum up to column i with pattern j at column i
    T = [[float('-inf')] * num_patterns for _ in range(n)]
    P = [[-1] * num_patterns for _ in range(n)]  # backpointers

    # base case: first column
    for j in range(num_patterns):
        T[0][j] = column_value(0, patterns[j])

    # recurrence
    for i in range(1, n):
        for j in range(num_patterns):
            best_val = float('-inf')
            best_k = -1
            for k in range(num_patterns):
                if compat[k][j]:
                    val = T[i-1][k] + column_value(i, patterns[j])
                    if val > best_val:
                        best_val = val
                        best_k = k
            T[i][j] = best_val
            P[i][j] = best_k

    # --- Step 5: extract answer ---
    return max(T[n-1])

