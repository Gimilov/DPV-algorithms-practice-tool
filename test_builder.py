import unittest

def make_test(user_solution, test_name, input_args, expected_output):
    def new_test(self):
        # assert matching input type
        try:
            result = user_solution(input_args)
        except TypeError as e:
            raise TypeError(f'Exercise expects input type: {type(input_args).__name__}.')
        
        # assert correct output type
        if not isinstance(result, type(expected_output)):
            raise AssertionError(f'Exercise expects output type: {type(expected_output).__name__}.')
        
        # other than that, verify the output
        self.assertEqual(result, expected_output)

    new_test.__name__ = f'test_{test_name}'
    return new_test

def build_test_suite(test_cases, user_solution):
    class DynamicTestClass(unittest.TestCase):
        pass
        
    for name, input_args, expected_output in test_cases:
        test_method = make_test(user_solution, name, input_args, expected_output)
        setattr(DynamicTestClass, test_method.__name__, test_method)
        
    return unittest.TestLoader().loadTestsFromTestCase(DynamicTestClass)