"""
Follow this format for test cases:
(test_name, input_args, expected_output)
"""
test_cases = {
    "6.1": [
        ('example_test', [5, 15, -30, 10, -5, 40, 10], [10, -5, 40, 10]),  
        ('all_negative', [-1, -2, -3, -4], []),
        ('all_positive', [1, 2, 3, 4], [1, 2, 3, 4]),
        ('mixed_negative_start', [-1, 2, 3, -4, 5], [2, 3, -4, 5]),
        ('mixed_negative_end', [1, -2, 3, 4, -1], [3, 4]),
        ('single_positive', [5], [5]),
        ('single_negative', [-3], []),
        ('zeros', [0, 0, 0], []),
        ('positive_after_negative', [-1, -2, 3, 4], [3, 4]),
        ('negative_after_positive', [3, 4, -1, -2], [3, 4]),
        ('alternating', [1, -2, 3, -4, 5], [5]),
        ('large_numbers', [1000000, -1, 1000000], [1000000, -1, 1000000]),
        ('negative_middle', [10, -5, 40, 10], [10, -5, 40, 10]),
        ('decreasing_sequence', [10, 5, 1, -5, -10], [10, 5, 1]),
        ('increasing_sequence', [-10, -5, 1, 5, 10], [1, 5, 10])
    ],
    "6.2": [],
    "6.3": [], 
    "6.4": [],
    "6.11": []
}