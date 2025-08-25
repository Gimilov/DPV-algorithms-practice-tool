import sys
import re
import importlib
import unittest
from user_solution import solution
from .test_builder import build_test_suite
from .test_result import CompactTestResult
from .helpers import ColorsHelper

# parse CLI arguments
exercise = sys.argv[1]
r = re.compile(r'\d+[\._]\d+')
if r.match(exercise) is None or len(sys.argv) != 2:
    print(
        f"""
{ColorsHelper.colored_text('-' * 100, 'magenta')}
{ColorsHelper.colored_text('USAGE:', 'white', bold=True)}
    python -m src.test_runner <exercise_number>

{ColorsHelper.colored_text('ARGUMENT FORMAT:', 'white', bold=True)}
    <exercise_number> must be in format: CHAPTER.PROBLEM or CHAPTER_PROBLEM
    Examples: '4.5', '6_2', '8.11'
{ColorsHelper.colored_text('-' * 100, 'magenta')}
"""
    )
    exit(1)

exercise = exercise.replace('_', '.')
try:
    test_cases = importlib.import_module('tests.dpv_chapter_' + exercise.split('.')[0]).test_cases
    # lookup for arbitrary exercise test cases
    test_suite = test_cases[exercise] 
except ModuleNotFoundError as e:
    print(f"""
{ColorsHelper.colored_text('-' * 100, 'red')}
{ColorsHelper.colored_text(e, 'white', bold=True)}
{ColorsHelper.colored_text('-' * 100, 'red')}
""")
    exit(1)
except KeyError as e:
    print(f"""
{ColorsHelper.colored_text('-' * 100, 'red')}
{ColorsHelper.colored_text(f'Test cases for this exercise are not defined: {e}', 'white', bold=True)}
{ColorsHelper.colored_text('-' * 100, 'red')}
""")
    exit(1)

# build & execute tests in the main block
if __name__ == '__main__':
    suite = build_test_suite(test_suite, solution)
    
    sys.argv = [sys.argv[0]] # prevent unittest from processing <exercise_number>

    runner = unittest.TextTestRunner(resultclass=CompactTestResult, verbosity=0)
    runner.run(suite)