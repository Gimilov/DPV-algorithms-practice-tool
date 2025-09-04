"""
DPV 2.23:

An array A[1...n] is said to have a majority element if more than 
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
"""

"""
(a) Algorithm
We use divide-and-conquer. If array has length 0, return None.
If the array has length 1, return its element as
the majority candidate. Otherwise, split A into two halves, recursively find
the majority element of each half, and combine. If both halves agree, that
element is the candidate. If they differ, count how many times each candidate
appears in the full array and return the one that exceeds n/2, if any. If
neither does, return None.

(b) Justification of Correctness
If the entire array has a majority element, then it must also be a majority
element in at least one of the two halves. Thus by recursively finding the
majority elements of each half, and then checking their counts in the full
array, we guarantee that we identify the true majority if one exists. The
verification step ensures no false positives are returned.

(c) Runtime Analysis
Each recursive step splits the array in half, producing two subproblems of
size n/2. Combining results requires O(n) time to count occurrences. The
recurrence is T(n) = 2T(n/2) + O(n), which solves to T(n) = O(n log n).
"""
from typing import List, Any

def solution(A: List[Any]) -> Any:
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]
    
    mid = len(A) // 2
    l_major = solution(A[:mid])
    r_major = solution(A[mid:])
    
    if l_major == r_major:
        return l_major
    
    l_count = sum(1 for elem in A if elem == l_major)
    r_count = sum(1 for elem in A if elem == r_major)
    
    if l_count > len(A) // 2:
        return l_major
    if r_count > len(A) // 2:
        return r_major
    
    return None

