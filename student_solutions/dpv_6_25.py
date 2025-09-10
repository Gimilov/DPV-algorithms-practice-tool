"""
DPV 6.25:

Consider the following 3-partition problem. Given integers a_1, ..., a_n, 
we want to determine whether it is possible to partition {1, ..., n} 
into three disjoint subsets I, J, K such that:

    ∑_{i ∈ I} a_i = ∑_{j ∈ J} a_j = ∑_{k ∈ K} a_k = (1/3) ∑_{i=1}^n a_i

For example, for input (1, 2, 3, 4, 4, 5, 8) the answer is yes, because 
there is the partition (1, 8), (4, 5), (2, 3, 4). On the other hand, for 
input (2, 2, 3, 5) the answer is no.

Devise and analyze a dynamic programming algorithm for 3-partition 
that runs in time polynomial in n and in ∑_i a_i.
"""

"""
Let T(i, s_1, s_2) be True if it's possible to construct two disjoint 
sets I, J, both of which are subsets of {a_1, ..., a_i}, such that
sum of elements of I and J are equal to s_1 and s_2, respectively, where each 
is equal to the 1/3 of the sum of {a_1, ..., a_i}.

The base case is then:
T[i, 0, 0] = False, where 0<=i<=n
T[i, s_1, s_2] = False if OR(i<0, s_1<0, s_2<0)
T[0, 0, 0] = True

Recurrence relation:
T(i, s_1, s_2) = OR(T(i-1, s_1 - a_i, s_2), T(i-1, s_1, s_2 - a_i), T(i-1, s_1, s_2)),
where 1<=i<=n, 0 <= s_1, s_2 <= S/3, where S is the sum of all numbers {a_1, ..., a_n}

Number of subproblems: O(nS^2)
Runtime of table fill: O(nS^2)
Method of return extraction: T(n, S/3, S/3)
Runtime of that method extraction: O(1)
"""
from typing import List

def solution(arr: List[int]) -> bool:
    n = len(arr)
    S = sum(arr)
    if S % 3 != 0:
        return False
    target = S // 3

    # DP table: T[i][s1][s2] = can we use first i elements to achieve sums s1 and s2?
    T = [[[False] * (target + 1) for _ in range(target + 1)] for _ in range(n + 1)]
    T[0][0][0] = True

    for i in range(1, n + 1):
        a = arr[i - 1]
        for s1 in range(target + 1):
            for s2 in range(target + 1):
                if T[i-1][s1][s2]:
                    T[i][s1][s2] = True
                else:
                    put_in_s1 = s1 >= a and T[i-1][s1 - a][s2]
                    put_in_s2 = s2 >= a and T[i-1][s1][s2 - a]
                    put_in_s3 = (S - (s1 + s2)) >= a and T[i-1][s1][s2]
                    T[i][s1][s2] = put_in_s1 or put_in_s2 or put_in_s3

    return T[n][target][target]
