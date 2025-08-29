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
    "6.7": [
        ('empty_string', "", ""),
        ('single_char', "A", "A"),
        ('all_same', "AAAA", "AAAA"),
        ('palindrome', "racecar", "racecar"),
        ('example_sequence', "ACGTGTCAAAATCG", "GCAAAACG"),
        ('single_letter_palindrome', "ABCDEF", "A", "B", "C", "D", "E", "F"),
        ('first_name', "annabel", "anna"),
        ('numeric', "12321", "12321"),
        ('long_sequence', "character", "carac"),
        ('repeated_pattern', "ABCBAABCBA", "ABCBAABCBA"),
        ('complex_case', "amanaplanacanalpanama", "amanaplanacanalpanama"),
        ('canoes_in_polish', "kajaki", "kajak"),
        ('polish_tonguebreaker', "konstantynopolitańczykowianeczka", "knayopoyank")
        ],
    "6.8": [
        ('empty_strings', ("", ""), 0),
        ('one_empty', ("abc", ""), 0),
        ('identical_strings', ("abc", "abc"), 3),
        ('no_common', ("abc", "def"), 0),
        ('partial_match', ("abc", "ac"), 1),
        ('substring_match', ("abc", "abcde"), 3),
        ('multiple_occurrences', ("abc", "abcabc"), 3),
        ('overlapping', ("aaa", "aa"), 2),
        ('common_suffix', ("xyzabc", "abc"), 3),
        ('common_prefix', ("abcxyz", "abc"), 3),
        ('middle_substring', ("xyabcw", "zabcr"), 3),
        ('single_char_common', ("a", "a"), 1),
        ('single_char_different', ("a", "b"), 0),
        ('longer_strings', ("abcdefgh", "xdefghy"), 5),
        ('repeated_pattern', ("ababab", "bababa"), 5),
        ('case_sensitive', ("AbC", "aBc"), 0)
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
    ],
    "6.17": [
        ('exact_single_coin', ([5], 5), True),
        ('impossible_single_coin', ([3], 5), False),
        ('multiple_coins_exact', ([1, 2, 5], 11), True),
        ('multiple_coins_impossible', ([3, 7], 5), False),
        ('zero_value', ([1, 2, 5], 0), True),
        ('large_value_possible', ([2, 3, 5], 100), True),
        ('large_value_impossible', ([4, 6], 11), False),
        ('duplicate_denominations', ([1, 1, 2, 5], 7), True),
        ('single_coin_multiple_use', ([2], 6), True),
        ('all_larger_than_v', ([10, 20], 5), False),
        ('greedy_trap', ([1, 3, 4], 6), True),
        ('zero_denominations', ([], 5), False),
        ('zero_denominations_zero_v', ([], 0), True),
        ('multiple_ways', ([1, 2], 3), True),
        ('large_v_small_coins', ([1], 1000), True)
    ],
    "6.18": [
        ('exact_single_coin', ([5], 5), True),
        ('impossible_single_coin', ([3], 5), False),
        ('multiple_coins_exact', ([1, 2, 5], 6), True),
        ('multiple_coins_impossible', ([3, 7], 5), False),
        ('zero_value', ([1, 2, 5], 0), True),
        ('duplicate_denominations', ([1, 1, 2, 5], 7), True),
        ('all_larger_than_v', ([10, 20], 5), False),
        ('greedy_trap', ([1, 3, 4], 6), False),
        ('zero_denominations', ([], 5), False),
        ('zero_denominations_zero_v', ([], 0), True),
        ('multiple_ways', ([1, 2], 3), True),
        ('exact_match_multiple', ([1, 5, 10, 20], 16), True),
        ('exact_match_multiple2', ([1, 5, 10, 20], 31), True),
        ('impossible_40', ([1, 5, 10, 20], 40), False),
        ('large_v_small_coins', ([1, 2, 4, 8, 16, 32, 64], 127), True)
    ],
    "6.19": [
        ('exact_single_coin', ([5], 1, 5), True),
        ('impossible_single_coin', ([3], 1, 5), False),
        ('multiple_coins_exact', ([1, 2, 5], 3, 6), True),
        ('multiple_coins_impossible', ([3, 7], 2, 5), False),
        ('zero_value', ([1, 2, 5], 0, 0), True),
        ('zero_coins_nonzero_v', ([1, 2, 5], 0, 5), False),
        ('large_k_possible', ([2], 50, 100), True),
        ('large_k_impossible', ([3], 33, 100), False),
        ('exact_k_coins', ([1], 5, 5), True),
        ('fewer_coins_than_needed', ([1], 4, 5), False),
        ('multiple_denominations_k_limit', ([1, 5, 10], 2, 15), True),
        ('multiple_denominations_k_limit_fail', ([1, 5, 10], 1, 15), False),
        ('all_larger_than_v', ([10, 20], 5, 5), False),
        ('greedy_trap', ([1, 3, 4], 3, 6), True),
        ('zero_denominations', ([], 5, 5), False),
        ('zero_denominations_zero_v', ([], 5, 0), True)
    ], 
    "6.20": [
        (
            'single_node@(optional:1)', 
            (["a"], [1.0]), 
            (1.0, ("a", None, None))
        ),
        (
            'two_nodes_balanced@(optional:1)', 
            (["a", "b"], [0.5, 0.5]), 
            (1.5, ("a", None, ("b", None, None))),
            (1.5, ("b", None, ("a", None, None)))
        ),
        (
            'two_nodes_unbalanced@(optional:1)', 
            (["a", "b"], [0.8, 0.2]), 
            (1.2, ("a", None, ("b", None, None)))
        ),
        (
            'three_nodes_balanced@(optional:1)', 
            (["a", "b", "c"], [0.3, 0.4, 0.3]), 
            (1.6, ("b", ("a", None, None), ("c", None, None)))
        ),
        (
            'three_nodes_unbalanced@(optional:1)', 
            (["a", "b", "c"], [0.6, 0.3, 0.1]), 
            (1.5, ("a", None, ("b", None, ("c", None, None))))
        ),
        (
            'book_example@(optional:1)', 
            (["begin", "do", "else", "end", "if", "then", "while"], [0.05, 0.40, 0.08, 0.04, 0.10, 0.10, 0.23]), 
            (2.18, ("do", ("begin", None, None), ("while", ("if", ("else", None, ("end", None, None)), ("then", None, None)), None)))
        ),
        (
            'all_equal_freq@(optional:1)', 
            (["a", "b", "c", "d"], [0.25, 0.25, 0.25, 0.25]), 
            (2.00, ("b", ("a", None, None), ("c", None, ("d", None, None)))),
            (2.00, ("c", ("b", ("a", None, None), None), ("d", None, None)))
        ),
        (
            'increasing_freq@(optional:1)', 
            (["a", "b", "c", "d"], [0.1, 0.2, 0.3, 0.4]), 
            (1.8, ("c", ("b", ("a", None, None), None), ("d", None, None)))
        ),
        (
            'decreasing_freq@(optional:1)', 
            (["a", "b", "c", "d"], [0.4, 0.3, 0.2, 0.1]), 
            (1.8, ("b", ("a", None, None), ("c", None, ("d", None, None))))
        )
    ],
    "6.26": []
}