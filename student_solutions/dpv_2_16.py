"""
DPV 2.16:

You are given an infinite array A[.] in which the first n cells contain 
integers in sorted order and the rest of the cells are filled with ∞. You 
are not given the value of n. Describe an algorithm that takes an integer x 
as input and finds a position in the array containing x, if such a position 
exists, in O(log n) time.

Note: len(A) is 100 - pretend you don't know that.
"""

"""
(a) Algorithm
We solve this problem with two recursive procedures. First, we must determine
a finite interval of the infinite array that could contain x. Starting at
index 1, we recursively double the index (1, 2, 4, 8, ...) until we either
find x, or encounter a value greater than or equal to x, or reach ∞. This
guarantees that if x is present, it must lie between the previous index and
the current index. Once this interval is identified, we use a recursive binary
search. Given left and right bounds, we compute the midpoint. If A[mid] = x,
we return mid. If A[mid] > x, we recurse on the left half; if A[mid] < x, we
recurse on the right half. If the interval becomes empty, we return -1.

(b) Justification of Correctness
The exponential search phase is correct because doubling the index ensures we
will eventually either reach ∞ or surpass x. Thus the true index of x (if it
exists) lies within the identified interval. The binary search phase maintains
the invariant that if x exists, it is within the current interval. By halving
the interval at each recursive step, we eventually reach either the exact index
containing x or an empty interval. Therefore, the algorithm always finds x if
it is present, and correctly returns -1 otherwise.

(c) Runtime Analysis
The exponential search doubles the index at each step, requiring O(log n)
comparisons before bounding the interval. The recursive binary search on an
interval of size O(n) performs O(log n) recursive calls. Therefore the total
runtime is O(log n).
"""
def solution(args: tuple) -> int:
    A, x = args

    # Recursive exponential search
    def find_bound(i: int) -> int:
        if A[i] == float('inf') or A[i] >= x:
            return i
        return find_bound(i * 2)

    bound = find_bound(1)

    # Recursive binary search
    def binary_search(left: int, right: int) -> int:
        if left > right:
            return -1
        mid = (left + right) // 2
        if A[mid] == x:
            return mid
        elif A[mid] > x:
            return binary_search(left, mid - 1)
        else:
            return binary_search(mid + 1, right)

    return binary_search(bound // 2, bound)
