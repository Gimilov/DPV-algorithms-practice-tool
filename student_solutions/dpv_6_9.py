"""
DPV 6.9:

A certain string-processing language offers a primitive operation 
which splits a string into two pieces. Since this operation involves
copying the original string, it takes n units of time for a string of 
length n, regardless of the location of the cut. Suppose, now, that 
you want to break a string into many pieces. The order in which the 
breaks are made can affect the total running time. For example, if 
you want to cut a 20-character string at positions 3 and 10, then 
making the first cut at position 3 incurs a total cost of 20 + 17 = 37, 
while doing position 10 first has a better cost of 20 + 10 = 30.

Give a dynamic programming algorithm that, given the locations of m cuts 
in a string of length n, finds the minimum cost of breaking the string 
into m + 1 pieces.
"""

"""
Problem definition in words: 
Let T(i, j) be the minimum cost of cutting the substring between boundaries i and j, 
where i and j are either the string ends or one of the cut positions.

Recurrence relation:
Base case: T(i, i+1) = 0   # no cuts possible between consecutive boundaries
DP: T(i, j) = min( (cuts[j] - cuts[i]) + T(i, k) + T(k, j) :  where i < k < j)
    , where 1<=i<j<=m

Number of subproblems: O(m^2)
Runtime to fill the table: O(m^3)
Method of return extraction: T(0, m-1)
Runtime of that return extraction: O(1)
"""

def solution(args: tuple) -> int:
    # n: length of string
    # cuts: sorted list of cut positions (0 < cut < n)
    n, cuts = args
    # Returns minimum cost
    
    # add boundaries at 0 and n
    cuts = [0] + cuts + [n]
    m = len(cuts)

    # DP table
    T = [[0] * m for _ in range(m)]

    # fill by increasing segment length
    for length in range(2, m):  # at least 2 apart (i, j)
        for i in range(m - length):
            j = i + length
            T[i][j] = min(
                (cuts[j] - cuts[i]) + T[i][k] + T[k][j]
                for k in range(i + 1, j)
            )

    return T[0][m - 1]

