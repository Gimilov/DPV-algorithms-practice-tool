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
"""
test_cases = {
    "2.1": [
        ('single', ('10011011', '10111010'), '111000010011110')
    ]
}