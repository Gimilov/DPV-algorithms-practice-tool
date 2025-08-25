"""
Build test cases dynamically based on specifications of the exercise.
"""
import sys
import re
import importlib
import unittest
from user_solution import solution
from helpers import ColorsHelper


# overriding key methods for compact results
class CompactTestResult(unittest.TextTestResult):
    def printErrors(self):
        for error in self.errors:
            print(error[1]) # index of formatted_msg

    def addError(self, test, err):
        formatted_msg = ''
        formatted_msg += ColorsHelper.colored_text('-' * 100, 'red', bold=True)
        formatted_msg += '\n'
        formatted_msg += ColorsHelper.colored_text(f'Error during {test._testMethodName}: ', 'red')
        formatted_msg += ColorsHelper.colored_text(sys.exc_info()[1], 'white', bold=True)
        formatted_msg += '\n'
        formatted_msg += ColorsHelper.colored_text('-' * 100, 'red', bold=True)
  
        self.errors.append((test, formatted_msg))

    def addFailure(self, test, err):
        formatted_msg = ''
        formatted_msg += ColorsHelper.colored_text('-' * 100, 'red', bold=True)
        formatted_msg += '\n'
        formatted_msg += ColorsHelper.colored_text(f'{test._testMethodName} failed: ', 'yellow')
        formatted_msg += ColorsHelper.colored_text(err[1], 'white', bold=True)
        formatted_msg += '\n'
        formatted_msg += ColorsHelper.colored_text('-' * 100, 'red', bold=True)

        self.failures.append((test, formatted_msg))
        print(formatted_msg)

    def addSuccess(self, test):
        formatted_msg = ''
        formatted_msg += ColorsHelper.colored_text('-' * 100, 'green', bold=False)
        formatted_msg += '\n'
        formatted_msg += ColorsHelper.colored_text(f'=> {test._testMethodName} passed!', 'green')
        formatted_msg += '\n'
        formatted_msg += ColorsHelper.colored_text('-' * 100, 'green', bold=False)

        print(formatted_msg)

    def stopTestRun(self):
        return super().stopTestRun()

# this class will be dynamically filled with test cases
class TestUserSolution(unittest.TestCase):
    pass

def make_test(user_solution, test_name, input_args, expected_output):
    def new_test(self):
        # assert matching input type
        try:
            result = user_solution(input_args)
        except TypeError as e:
            raise TypeError(f'Exercise expects input type: {type(input_args).__name__}.')
        
        # assert correct output type
        try:
            self.assertIsInstance(result, type(expected_output))
        except AssertionError as e:
            raise AssertionError(f'Exercise expects output type: {type(expected_output).__name__}.')
        
        # other than that, verify the output
        self.assertEqual(result, expected_output)

    new_test.__name__ = 'test_' + test_name
    return new_test
        

# parse CLI arguments
exercise = sys.argv[1]
r = re.compile(r'\d+[\._]\d+')
if r.match(exercise) is None or len(sys.argv) != 2:
    print(
        f"""
{ColorsHelper.colored_text('--------------------------------------------------------------------', 'magenta')}
{ColorsHelper.colored_text("""
USAGE:
    python3 test_runner.py <exercise_number>

ARGUMENT FORMAT:
    <exercise_number> must be in the format: CHAPTER.PROBLEM  or  CHAPTER_PROBLEM
    Examples: '4.5', '6_2', '12.11'
""", 'white', bold=True)}
{ColorsHelper.colored_text('--------------------------------------------------------------------', 'magenta')}
"""
    )
    exit(1)

# load test suite, dynamically create tests based on exercise specification
exercise = exercise.replace('_', '.')
test_suite = importlib.import_module('tests.dpv_chapter_' + exercise.split('.')[0])

for (name, input_args, expected_output) in test_suite.test_cases[exercise]:
    curr_test = make_test(solution, name, input_args, expected_output)
    setattr(TestUserSolution, curr_test.__name__, curr_test)


# execute tests
if __name__ == '__main__':
    sys.argv = [sys.argv[0]] # prevent unittest from processing <exercise_number>

    runner = unittest.TextTestRunner(resultclass=CompactTestResult, verbosity=0)
    unittest.main(failfast=True, testRunner=runner)