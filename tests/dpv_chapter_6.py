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
        ('positive_after_negative', [-1, -2, 3, 4], [3, 4]),
        ('negative_after_positive', [3, 4, -1, -2], [3, 4]),
        ('alternating', [1, -2, 3, -4, 5], [5]),
        ('large_numbers', [1000000, -1, 1000000], [1000000, -1, 1000000]),
        ('negative_middle', [10, -5, 40, 10], [10, -5, 40, 10]),
        ('decreasing_sequence', [10, 5, 1, -5, -10], [10, 5, 1]),
        ('increasing_sequence', [-10, -5, 1, 5, 10], [1, 5, 10])
    ],
    "6.2": [
        ('example_1', [0, 200, 400], [200, 400]),
        ('example_2', [0, 100, 200, 400], [200, 400]),
        ('example_3', [0, 50, 150, 250, 350, 450], [250, 450]),  
        ('exact_multiple', [0, 200, 400, 600], [200, 400, 600]),
        ('under_shot', [0, 100, 300], [300]),  
        ('over_shot', [0, 250, 450], [250, 450]), 
        ('single_hotel', [400], [400]),
        ('two_hotels', [0, 400], [400]),
        ('three_hotels_penalty', [0, 190, 400], [190, 400]),  
        ('clustered_hotels', [0, 50, 100, 201, 400], [201, 400]),  
        ('long_jump', [0, 500], [500]), 
        ('no_choice', [0, 100, 200, 300, 400], [200, 400]),  
        ('uneven_spacing', [0, 80, 160, 320, 400], [160, 400])
    ],
    "6.3": [], 
    "6.4": [],
    "6.11": []
}