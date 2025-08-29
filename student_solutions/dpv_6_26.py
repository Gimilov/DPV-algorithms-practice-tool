"""
DPV 6.26:

Sequence alignment. When a new gene is discovered, a standard 
approach to understanding its function is to look through a 
database of known genes and find close matches. The closeness 
of two genes is measured by the extent to which they are aligned. 
To formalize this, think of a gene as being a long string over
an alphabet Σ = {A, C, G, T}. Consider two genes (strings) 
x = ATGCC and y = TACGCA. An alignment of x and y is a way of 
matching up these two strings by writing them in columns, for instance:

    -   A   T   -   G   C   C
    T   A   -   C   G   C   A

Here the "-" indicates a "gap". The characters of each string 
must appear in order, and each column must contain a character 
from at least one of the strings. The score of an alignment is 
specified by a scoring matrix δ of size (|Σ| + 1) x (|Σ| + 1), 
where the extra row and column are to accommodate gaps. For 
instance the preceding alignment has the following score:

δ(-, T) + δ(A, A) + δ(T, -) + δ(-, C) + δ(G, G) + δ(C, C) + δ(C, A).

Give a dynamic programming algorithm that takes as input two 
strings x[1...n] and y[1...m] and a scoring matrix δ, and returns
the highest-scoring alignment. The running time should be O(mn).

"""
def solution(args: tuple) -> tuple:
    x, y, delta = args
    # Input: x:str, y:str, delta:dict
    # Note that delta is a nested dictionary. Where delta['A']['C'] is a score of A to C.
    # Returns: (score, aligned_x, aligned_y)
    # where aligned_x and aligned_y are strings with gaps ('-') inserted

    n = len(x)
    m = len(y)
    S = [[None] * (m+1) for _ in range(n+1)]

    S[0][0] = 0
    for i in range(1, n+1):
        S[i][0] = S[i-1][0] + delta[x[i-1]]['-']
    for j in range(1, m+1):
        S[0][j] = S[0][j-1] + delta['-'][y[j-1]]

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            S[i][j] = max(
                delta[x[i - 1]]['-']     + S[i - 1][j],      # gap in y
                delta['-'][y[j - 1]]     + S[i][j - 1],      # gap in x
                delta[x[i - 1]][y[j - 1]] + S[i - 1][j - 1]  # match/mismatch
            )

    # backtracking
    bt_i, bt_j = n, m
    aligned_x = ''
    aligned_y = ''
    while bt_i > 0 or bt_j > 0:
        x_and_y = delta[x[bt_i-1]][y[bt_j-1]] + S[bt_i-1][bt_j-1]
        x_gap = delta['-'][y[bt_j-1]] + S[bt_i][bt_j-1]
        y_gap = delta[x[bt_i-1]]['-'] + S[bt_i-1][bt_j]
        max_move = max(x_and_y, x_gap, y_gap)

        if max_move == x_and_y:
            aligned_x = x[bt_i-1] + aligned_x
            aligned_y = y[bt_j-1] + aligned_y
            bt_i -= 1
            bt_j -= 1

        elif max_move == x_gap:
            aligned_x = '-' + aligned_x
            aligned_y = y[bt_j-1] + aligned_y
            bt_j -= 1
        
        elif max_move == y_gap:
            aligned_x = x[bt_i-1] + aligned_x
            aligned_y = '-' + aligned_y
            bt_i -= 1

    return S[n][m], aligned_x, aligned_y
