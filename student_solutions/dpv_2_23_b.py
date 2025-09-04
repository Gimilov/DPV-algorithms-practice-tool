"""
DPV 2.23:

An array A[1...n] is said to have a majority element if more than 
half of its entries are the same. Given an array, the task is to design an 
efficient algorithm to tell whether the array has a majority element, and, 
if so, to find that element. The elements of the array are not necessarily 
from some ordered domain like the integers, and so there can be no comparisons 
of the form "is A[i] > A[j]?". (Think of the array elements as GIF files, say). 
However you can answer questions of the form: "is A[i] = A[j]?" in constant time.

(b) Can you give a linear-time algorithm? (Hint: Here's another divide-and-conquer 
approach:
    - Pair up the elements of A arbitrarily, to get n/2 pairs
    - Look at each pair: if the two elements are different, discard both of them; 
    if they are the same, keep just one of them

    Show that after this procedure there are at most n/2 elements left, and that 
    they have a majority element if A does).
"""

"""
(a) Algorithm
Form arbitrary pairs of elements in A. For each pair:
- If the elements are equal, keep one copy.
- If the elements differ, discard both.
This produces a new array of size at most n/2. Recursively apply the same
procedure to the new array until only one element (or none) remains. The final
element, if any, is a candidate majority. To confirm, count its occurrences
in the original array and return it if it exceeds n/2, otherwise return None.

(b) Justification of Correctness
If A has a majority element m, then in every pair either both elements are m
(in which case one copy survives), or at least one element is not m (so at
worst m is discarded along with another). Therefore m can never be completely
eliminated and must survive into the smaller array. By repeating this process,
m remains as the final candidate. The verification step ensures that if no
majority exists, the algorithm returns None.

(c) Runtime Analysis
At each step, we form pairs and filter in O(n). The array size shrinks by at
least half, so the recurrence is T(n) = T(n/2) + O(n). This solves to T(n) = O(n).
Counting at the end is also O(n), so the overall runtime is O(n).
"""
from typing import List, Any

def solution(A: List[Any]) -> Any:
    # Recursive elimination procedure
    def eliminate(arr: List[Any]) -> Any:
        if not arr:
            return None
        if len(arr) == 1:
            return arr[0]
        
        reduced = []
        for i in range(0, len(arr) - 1, 2):
            if arr[i] == arr[i+1]:
                reduced.append(arr[i])
        if len(arr) % 2 == 1:  # carry forward odd element
            reduced.append(arr[-1])
        
        return eliminate(reduced)
    
    candidate = eliminate(A)
    if candidate is None:
        return None
    
    # Final verification
    if sum(1 for elem in A if elem == candidate) > len(A) // 2:
        return candidate
    return None

