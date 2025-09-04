"""
DPV 2.1:

Use the divide-and-conquer integer multiplication algorithm to multiply the two
binary integers 10011011 and 10111010.

Note: x and y are given as ints, and so should be the output. Also, there's
only a single test for this exercise.
"""

"""
(a) Algorithm
We multiply two n-bit binary numbers using divide-and-conquer. Each number is
split into left and right halves. Three recursive products are computed:
    A = left(x) * left(y)
    B = right(x) * right(y)
    C = (left(x)+right(x)) * (left(y)+right(y))
The cross-term is C - A - B. The final result is obtained by shifting A left
by n bits, adding the cross-term shifted by n/2 bits, and adding B. Recursion
continues until the base case of single-bit multiplication.

(b) Justification of Correctness
The method covers all parts of the product: high (A), low (B), and cross-term.
The algebra ensures no information is lost when using three multiplications
instead of four. Since the base case is correct and each step combines results
faithfully, the overall product is correct.

(c) Runtime Analysis
Each step makes 3 recursive calls on size n/2 plus O(n) work for addition and
shifting. Thus T(n) = 3T(n/2) + O(n), giving T(n) = O(n^{log2 3}).
This improves over the naive O(n^2) method.
"""
def solution(args: tuple) -> int:
    x, y = args
    # base case
    if x < 2 or y < 2:
        return x * y

    # number of bits (take the larger one)
    n = max(x.bit_length(), y.bit_length())
    m = n // 2

    # split x and y into halves
    x_l, x_r = x >> m, x & ((1 << m) - 1)
    y_l, y_r = y >> m, y & ((1 << m) - 1)

    # recursive multiplications
    A = solution((x_l, y_l))
    B = solution((x_r, y_r))
    C = solution((x_l + x_r, y_l + y_r))

    # combine
    return (A << (2*m)) + ((C - A - B) << m) + B
