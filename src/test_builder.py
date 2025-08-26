import unittest

def make_test(user_solution, test_name, input_args, expected_output):
    def new_test(self):
        # assert that solution runs
        try:
            result = user_solution(input_args)
        except Exception as e:
            raise Exception(f'{e}.')
        
        # assert correct output type
        if not isinstance(result, type(expected_output[0])): # expected output always packed in a list
            raise AssertionError(f'Exercise expects output type: {type(expected_output).__name__}.')
        
        # verify the output - single expected output:
        if len(expected_output) == 1:
            self.assertEqual(result, *expected_output)
        # verify the output - multiple acceptable outputs
        else:
            self.assertIn(result, expected_output)

    new_test.__name__ = f'test_{test_name}'
    return new_test

def build_test_suite(test_cases, user_solution):
    class DynamicTestClass(unittest.TestCase):
        pass
        
    for name, input_args, *expected_output in test_cases:
        test_method = make_test(user_solution, name, input_args, expected_output)
        setattr(DynamicTestClass, test_method.__name__, test_method)
        
    return unittest.TestLoader().loadTestsFromTestCase(DynamicTestClass)