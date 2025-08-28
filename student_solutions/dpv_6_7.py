"""
DPV 6.7:

A subsequence is palindromic if it is the same whether read 
left to right or right to left. For instance, the sequence 
    [A, C, G, T, G, T, C, A, A, A, A, T, C, G] 
has many palindromic subsequences, including [A, C, G, C, A], 
[A] and [A, A, A, A] (on the other hand, the subsequence [A, C, T] 
is not palindromic). Devise an algorithm that takes a sequence 
x[1...n] and returns the (length of the) longest palindromic 
subsequence. Its running time should be O(n^2).

Note: please return the longest palindromic subsequence, not just the length of it.
"""
def solution(x: str) -> str:
    n = len(x)
    S = [[0] * n for _ in range(n)]

    for i in range(n):
        S[i][i] = 1

    for i in range(n-1):
        S[i][i+1] = 2 if x[i] == x[i+1] else 1
    
    for s in range(2, n):
        for i in range(n-s):
            j = i + s 
            if x[i] == x[j]:
                # pretty sure you could just S[i][j] = 2 + S[i+1][j-1] here...
                S[i][j] = max(S[i+1][j], S[i][j-1], 2 + S[i+1][j-1])
            else:
                S[i][j] = max(S[i+1][j], S[i][j-1])
    
    # backtracking
    i, j = 0, n-1
    left_part = []
    right_part = []
    while i <= j:
        if i == j:
            left_part.append(x[i])
            break
        if x[i] == x[j]:
            left_part.append(x[i])
            right_part.append(x[j])
            i += 1
            j -= 1
        else:
            if S[i][j] == S[i+1][j]:
                i += 1
            else:
                j -= 1

    return ''.join(left_part) + ''.join(reversed(right_part))