"""
DPV 6.27:

Alignment with gap penalties. The alignment algorithm of 
Exercise 6.26 helps to identify DNA sequences that are close to one 
another. The discrepancies between these closely matched sequences 
are often caused by errors in DNA replication. However, a closer 
look at the biological replication process reveals that the scoring 
function we considered earlier has a qualitative problem: nature 
often inserts or removes entire substrings of nucleotides (creating 
long gaps), rather than editing just one position at a time. Therefore, 
the penalty for a gap of length k should not be 10 times the penalty 
for a gap of length 1, but something significantly smaller.

Repeat Exercise 6.26, but this time use a modified scoring function 
in which the penalty for a gap of length k is c_0 + c_1k, where c_0 
and c_1 are given constants (and c_0 is larger than c_1).
"""

"""
(a) Subproblem Definition:
    Let E(i, j) be the maximum score of an alignment for x[1,...,i] and y[1,...,j] 
    that ends with a match or substitution.
    Let Ex(i, j) be the maximum score of an alignment for x[1,...,i] and y[1,...,j] 
    that ends with a gap in x (deletion from x).
    Let Ey(i, j) be the maximum score of an alignment for x[1,...,i] and y[1,...,j] 
    that ends with a gap in y (deletion from y).

    (b) Recurrence Definition:
Base Cases:
E(0, 0) = 0
E(i, 0) = -∞, where 1<=i<=m
E(0, j) = -∞, where 1<=j<=n
Ex(0, j) = -∞, where 0<=j<=n
Ey(i, 0) = -∞, where 0<=i<=m

E(i, j) = max{E(i-1, j-1), Ex(i-1, j-1), Ey(i-1, j-1)} + δ(x_i, y_j),
    where 1<=i<=m, 1<=j<=n

Ex(i, j) = max{E(i-1, j) - c0 - c1, Ex(i-1, j) - c1, Ey(i-1, j) - c0 - c1},
    where 1<=i<=m, 0<=j<=n

Ey(i, j) = max{E(i, j-1) - c0 - c1, Ex(i, j-1) - c0 - c1, Ey(i, j-1) - c1},
    where 0<=i<=m, 1<=j<=n

    (c) Implementation Analysis:
(1) Number of subproblems: O(m*n) 
(2) Runtime to fill table: O(m*n) 
(3) Final return extraction: max{E(m, n), Ex(m, n), Ey(m, n)}
(4) Runtime to extract final return: O(1)
"""

def solution(args: tuple) -> tuple:
    x, y, delta, c0, c1 = args
    m = len(x)
    n = len(y)
    
    # Initialize tables with proper base cases
    E = [[-10**9] * (n+1) for _ in range(m+1)]
    Ex = [[-10**9] * (n+1) for _ in range(m+1)]
    Ey = [[-10**9] * (n+1) for _ in range(m+1)]
    
    # Base cases
    E[0][0] = 0
    
    # Initialize first row (i=0)
    for j in range(1, n+1):
        # Can only have gaps in x (insertions in y)
        Ey[0][j] = max(Ey[0][j], 
                      E[0][j-1] - c0 - c1 if j == 1 else -10**9,
                      Ex[0][j-1] - c0 - c1,
                      Ey[0][j-1] - c1)
    
    # Initialize first column (j=0)
    for i in range(1, m+1):
        # Can only have gaps in y (deletions from x)
        Ex[i][0] = max(Ex[i][0],
                      E[i-1][0] - c0 - c1 if i == 1 else -10**9,
                      Ex[i-1][0] - c1,
                      Ey[i-1][0] - c0 - c1)
    
    # Fill tables
    for i in range(1, m+1):
        for j in range(1, n+1):
            # E table: ends with match/substitution
            E[i][j] = max(E[i-1][j-1], Ex[i-1][j-1], Ey[i-1][j-1]) + delta[x[i-1]][y[j-1]]
            
            # Ex table: ends with gap in x (deletion from x)
            Ex[i][j] = max(E[i-1][j] - c0 - c1, 
                          Ex[i-1][j] - c1, 
                          Ey[i-1][j] - c0 - c1)
            
            # Ey table: ends with gap in y (insertion in y)
            Ey[i][j] = max(E[i][j-1] - c0 - c1,
                          Ex[i][j-1] - c0 - c1,
                          Ey[i][j-1] - c1)
    
    # Find best score and starting point for backtracking
    best_score = max(E[m][n], Ex[m][n], Ey[m][n])
    
    # Backtracking to reconstruct alignment
    aligned_x = ""
    aligned_y = ""
    i, j = m, n
    
    # Determine which table we ended in
    if best_score == E[m][n]:
        current_table = 'E'
    elif best_score == Ex[m][n]:
        current_table = 'Ex'
    else:
        current_table = 'Ey'
    
    while i > 0 or j > 0:
        if current_table == 'E':
            # Came from match/substitution
            aligned_x = x[i-1] + aligned_x
            aligned_y = y[j-1] + aligned_y
            i -= 1
            j -= 1
            
            # Check which previous state we came from
            if i >= 0 and j >= 0:
                prev_scores = {
                    'E': E[i][j],
                    'Ex': Ex[i][j],
                    'Ey': Ey[i][j]
                }
                current_table = max(prev_scores, key=prev_scores.get)
                
        elif current_table == 'Ex':
            # Came from gap in x (deletion from x)
            aligned_x = x[i-1] + aligned_x
            aligned_y = '-' + aligned_y
            i -= 1
            
            # Check which previous state we came from
            if i >= 0:
                prev_scores = {
                    'E': E[i][j] - c0 - c1,
                    'Ex': Ex[i][j] - c1,
                    'Ey': Ey[i][j] - c0 - c1
                }
                # Find which one matches our current score
                for table, score in prev_scores.items():
                    if abs(Ex[i+1][j] - score) < 1e-6:  # Account for floating point issues
                        current_table = table
                        break
                
        elif current_table == 'Ey':
            # Came from gap in y (insertion in y)
            aligned_x = '-' + aligned_x
            aligned_y = y[j-1] + aligned_y
            j -= 1
            
            # Check which previous state we came from
            if j >= 0:
                prev_scores = {
                    'E': E[i][j] - c0 - c1,
                    'Ex': Ex[i][j] - c0 - c1,
                    'Ey': Ey[i][j] - c1
                }
                # Find which one matches our current score
                for table, score in prev_scores.items():
                    if abs(Ey[i][j+1] - score) < 1e-6:  # Account for floating point issues
                        current_table = table
                        break
    
    return (best_score, aligned_x, aligned_y)