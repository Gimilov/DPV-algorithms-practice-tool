"""
Follow this format for test cases:
(test_name, input_args, expected_output)

Note: For problems with multiple valid solutions, multiple expected_output can be supplied.
Example: (test_name, input_args, expected_output1, expected_output2, ...)
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
    "6.3": [
        ('example_1', ([1, 3, 5], [10, 20, 30], 2), 60),  # All allowed: 10+20+30=60
        ('example_2', ([1, 3, 5], [10, 20, 30], 3), 40),  # 1 and 5: 10+30=40 (since |5-1|=4>=3)
        ('example_3', ([1, 2, 3], [5, 10, 15], 2), 20),   # 1 and 3: 5+15=20 (|3-1|=2>=2)
        ('all_spaced', ([10, 20, 30], [5, 10, 15], 10), 30), # All allowed: 5+10+15=30
        ('clustered', ([1, 2, 3, 10], [100, 1, 1, 200], 5), 300), # 1 and 10: 100+200=300
        ('single_location', ([5], [50], 3), 50),
        ('two_too_close', ([1, 2], [10, 20], 2), 20),     # Must choose one: max(10,20)=20
        ('two_just_right', ([1, 3], [10, 20], 2), 30),    # Both allowed: 10+20=30
        ('multiple_options', ([1, 4, 5, 8], [10, 20, 30, 40], 3), 80), # 1,5,8: 10+30+40=80
        ('greedy_trap', ([1, 2, 4], [100, 1, 100], 2), 200), # 1 and 4: 100+100=200
        ('large_k', ([1, 2, 3], [10, 20, 30], 10), 30),   # Only one: max(10,20,30)=30
        ('no_restaurants', ([], [], 5), 0)
    ],
    "6.4": [
        ('example_1', ("itwasthebestoftimes", {"it", "was", "the", "best", "of", "times"}), ["it", "was", "the", "best", "of", "times"]),
        ('example_2', ("applepenapple", {"apple", "pen"}), ["apple", "pen", "apple"]),
        ('example_3', ("catsanddog", {"cat", "cats", "and", "sand", "dog"}), ["cats", "and", "dog"], ["cat", "sand", "dog"]),
        ('single_word', ("hello", {"hello"}), ["hello"]),
        ('no_solution', ("abc", {"def"}), []),
        ('empty_string', ("", {"word"}), []),
        ('multiple_segmentations', ("abcd", {"a", "b", "ab", "cd", "abcd"}), ["a", "b", "cd"], ["ab", "cd"], ["abcd"]), 
        ('long_valid', ("thisisagoodday", {"this", "is", "a", "good", "day"}), ["this", "is", "a", "good", "day"]),
        ('partial_invalid', ("validinvalid", {"valid"}), []),
        ('overlapping_words', ("aaa", {"a", "aa", "aaa"}), ["a", "a", "a"], ["aa", "a"], ["a", "aa"], ["aaa"]),          
        ('exact_match', ("word", {"word"}), ["word"]),
        ('no_dict', ("test", {}), [])
    ],
        "6.11": [
        ('empty_strings', ("", ""), 0),
        ('one_empty', ("abc", ""), 0),
        ('identical_strings', ("abc", "abc"), 3),
        ('common_subsequence', ("abcde", "ace"), 3),
        ('no_common', ("abc", "def"), 0),
        ('partial_match', ("abc", "ac"), 2),
        ('longer_example', ("itwasthebestoftimes", "itwastheworstoftimes"), 17),
        ('single_char_common', ("a", "a"), 1),
        ('single_char_different', ("a", "b"), 0),
        ('substring', ("abc", "abcde"), 3),
        ('reverse_order', ("abc", "cba"), 1),
        ('numeric_strings', ("12345", "13579"), 3),
        ('mixed_case', ("AbC", "aBc"), 0),
        ('long_strings', ("abcdefghijklmnopqrstuvwxyz", "acegikmoqsuwy"), 13),
        ('repeated_chars', ("aaa", "aa"), 2),
        ('complex_case', ("XMJYAUZ", "MZJAWXU"), 4)
    ]
}