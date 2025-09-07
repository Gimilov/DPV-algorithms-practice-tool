"""
DPV 6.6:

Let us define a multiplication operation on three symbols a, b, c 
    according to the following table; thus ab = b, ba = c, and so on. 
    Notice that the multiplication operation defined by the table is 
    neither associative nor commutative.

          a  b  c
        a b  b  a
        b c  b  a
        c a  c  c

    Find an efficient algorithm that examines a string of these symbols, 
    say bbbbac, and decides whether or not it is possible to parenthesize 
    the string in such a way that the value of the resulting expression is 
    a. For example, on input bbbbac your algorithm should return yes
    because ((b(bb))(ba))c = a.
"""

"""
Let T(i, j) be the set of all possible values that 
can be obtained by parenthesizing the substring s[i...j] (inclusive).

T(i, i) = { s[i] } for all i.
T(i, j) = set_union(mul_table(x, y) : where x ∈ T(i, k), y ∈ T(k+1, j)),
    where 1<=i<=k<=j<=n

c. Implementation Analysis
   (1) Number of subproblems: O(n^2)
   (2) Runtime for table fill: O(n^3 * constant) 
   (3) How the return is extracted: Check if 'a' is in T(1, n)
   (4) Runtime of return extraction: O(1)
"""

def solution(s: str) -> bool:
    # Multiplication table definition
    mul_table = {
        ('a', 'a'): 'b',
        ('a', 'b'): 'b', 
        ('a', 'c'): 'a',
        ('b', 'a'): 'c',
        ('b', 'b'): 'b',
        ('b', 'c'): 'a',
        ('c', 'a'): 'a',
        ('c', 'b'): 'c',
        ('c', 'c'): 'c'
    }
    # Returns True if string can be parenthesized to yield 'a', else False
    # Your implementation here
    n = len(s)
    # Dynamic Programming Table: dp[i][j] = set of possible values for substring s[i:j+1]
    dp = [[set() for _ in range(n)] for _ in range(n)]
    
    # Base case: single character
    for i in range(n):
        dp[i][i].add(s[i])
    
    # Fill table for lengths from 2 to n
    for length in range(2, n+1):
        for i in range(0, n - length + 1):
            j = i + length - 1
            for k in range(i, j):  # k is the split point
                left_vals = dp[i][k]
                right_vals = dp[k+1][j]
                for l_val in left_vals:
                    for r_val in right_vals:
                        result = mul_table[(l_val, r_val)]
                        dp[i][j].add(result)
    
    return 'a' in dp[0][n-1]
    
