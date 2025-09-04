"""
Follow this format for test cases:
(test_name, input_args, expected_output)

Notes:
- Simple tests with a single expected output are supported:
    ('example_test', [5, 15, -30, 10, -5, 40, 10], [10, -5, 40, 10]),

- Simple tests with multiple possible outputs are supported:
    ('single_letter_palindrome', "ABCDEF", "A", "B", "C", "D", "E", "F"),

- Annotations in the test name are supported to control special behavior:
    - @(optional:i[,j,...])  
        Marks output tuple elements at positions i, j, ... as optional.
        Example:
            ('example_keywords@(optional:1)', (words, freqs),
            (2.18,),                      # valid if only cost returned
            (2.18, expected_tree1),       # also valid if cost + tree returned
            (2.18, expected_tree2))       # multiple valid tree shapes allowed
    - @(reference)
        Marks a reference-only case. No assertions are run.
        Instead, the expected output is displayed.
        Example:
            'display_answers@(reference)', None, '<some answer here>')
"""
test_cases = {
    "2.1": [
        ('single', (155, 186), 28830)
    ],
    "2.5": [
        ('display_answers@(reference)', None, """
(a) T(n) = 2T(n/3) + 1 = Θ(n^{log_3 2}) by the Master theorem.

(b) T(n) = 5T(n/4) + n = Θ(n^{log_4 5}) by the Master theorem.

(c) T(n) = 7T(n/7) + n = Θ(n log_7 n) by the Master theorem.

(d) T(n) = 9T(n/3) + n^2 = Θ(n^2 log_3 n) by the Master theorem.

(e) T(n) = 8T(n/2) + n^3 = Θ(n^3 log_2 n) by the Master theorem.

(f) T(n) = 49T(n/25) + n^{3/2} log n = Θ(n^{3/2} log n). Apply the same 
reasoning of the proof of the Master Theorem. The contribution of level i 
of the recursion is

(49/(25^{3/2}))^i n^{3/2} log(n/(25^{3/2})) = (49/125)^i O(n^{3/2} log n)

Because the corresponding geometric series is dominated by the contribution 
of the first level, we obtain T(n) = O(n^{3/2} log n). But, T(n) is clearly 
Ω(n^{3/2} log n). Hence, T(n) = Θ(n^{3/2} log n).

(g) T(n) = T(n-1) + 2 = Θ(n).

(h) T(n) = T(n-1) + n^c = ∑_{i=0}^n i^c + T(0) = Θ(n^{c+1}).

(i) T(n) = T(n-1) + c^n = ∑_{i=0}^n c^i + T(0) = (c^{n+1}-1)/(c-1) + T(0) = Θ(c^n).

(j) T(n) = 2T(n-1) + 1 = ∑_{i=0}^{n-1} 2^i + 2^n T(0) = Θ(2^n).

(k) T(n) = T(√n) + 1 = ∑_{i=0}^k 1 + T(b), where k ∈ Z such that n^{1/(2^k)} is 
a small constant b, i.e. the size of the base case. This implies k = Θ(log log n) 
and T(n) = Θ(log log n).
""")
    ],
    "2.16": [
        ('x_at_start', (list(range(1, 1001)) + [float('inf')] * 3001, 1), 0),
        ('x_at_end', (list(range(1, 101)) + [float('inf')] * 801, 100), 99),
        ('x_in_middle', (list(range(1, 1001)) + [float('inf')] * 5001, 500), 499),
        ('x_not_found', (list(range(1, 1001)) + [float('inf')] * 4001, 1001), -1),
        ('x_smaller_than_min', (list(range(2, 1001)) + [float('inf')] * 3001, 1), -1),
        ('x_larger_than_max', (list(range(1, 1000)) + [float('inf')] * 3001, 10000), -1),
        ('single_element_found', ([5] + [float('inf')] * 999, 5), 0),
        ('single_element_not_found', ([5] + [float('inf')] * 999, 3), -1),
        ('empty_effective_array', ([float('inf')] * 1000, 5), -1),
        ('duplicate_values', ([1, 2, 2, 3, 4] + [float('inf')] * 995, 2), 1),
        ('negative_numbers', ([-5, -3, 0, 2, 4] + [float('inf')] * 995, -3), 1),
        ('all_inf', ([float('inf')] * 1000, 5), -1)
    ],
    "2.23": [
        ('majority_exists', [1, 2, 1, 1, 3, 1, 1], 1),
        ('no_majority', [1, 2, 3, 4, 5], None),
        ('all_same', [7, 7, 7, 7, 7, 7], 7),
        ('empty_array', [], None),
        ('single_element', [5], 5),
        ('two_elements_same', [3, 3], 3),
        ('two_elements_different', [1, 2], None),
        ('even_length_majority', [1, 1, 2, 2, 1, 1], 1),
        ('odd_length_majority', [1, 2, 1, 2, 1], 1),
        ('exactly_half', [1, 1, 1, 2, 2, 2], None),
        ('string_elements', ['a', 'b', 'a', 'a', 'c', 'a', 'a'], 'a'),
        ('mixed_types', [1, 'a', 1, 1, 2, 1, 1], 1),
        ('large_array_no_majority', [1] * 500 + [2] * 500, None)
    ]
}