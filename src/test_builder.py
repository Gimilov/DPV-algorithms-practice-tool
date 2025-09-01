import unittest
import re
from .helpers import AnswerDisplayer

""" 
Test case of format:
    'example_test@(optional:1; test_field)'
... has annotations parsed as:
{
  "optional": 1,
  "test_field": True
}

Test case of format:
    'example_test@(optional:1,2,3; test_field:4,5,6)'
... has annotations parsed as:
{
  "optional": [1,2,3],
  "test_field": [4,5,6]
}
"""
def parse_annotations(test_name):
    match = re.search(r'@\((.*)\)', test_name)
    if not match:
        return test_name, {}
    base = test_name[:match.start()]
    raw = match.group(1)

    annotations = {}
    for part in raw.split(";"):
        if not part.strip():
            continue

        if not ':' in part:
            annotations[part.strip()] = True
            continue

        key, val = part.split(":", 1)
        key = key.strip()
        vals = [v.strip() for v in val.split(",") if v.strip()]

        # try to cast numbers
        casted = []
        for v in vals:
            try:
                if "." in v or "e" in v.lower():
                    casted.append(float(v))
                else:
                    casted.append(int(v))
            except ValueError:
                casted.append(v)
        annotations[key] = casted if len(casted) > 1 else casted[0]

    return base, annotations


def round_floats(x):
    if isinstance(x, float):
        return round(x, 3)
    if isinstance(x, tuple):
        return tuple(round_floats(i) for i in x)
    return x # untouched if not any of the above


def make_test(user_solution, test_name, input_args, expected_output):
    base_name, annotations = parse_annotations(test_name)

    def new_test(self):
        # assert that solution runs
        try:
            result = user_solution(input_args)
        except Exception as e:
            raise Exception(f'{e}.')
        
        result = round_floats(result)
        # ---- handle "reference" annotation ----
        if "reference" in annotations and annotations["reference"] == True:
            AnswerDisplayer.display_answer(expected_output[0]) # answer is passed as a single expected output
            return 
        
        # ---- handle "optional" annotation ----
        if "optional" in annotations:
            if not isinstance(result, tuple):
                result = (result,)

            # each expected_output is one acceptable result tuple
            # (2.18,), (2.18, tree1), (2.18, tree2), ...
            valid = False
            for expected in expected_output:
                ok = True
                for i, exp in enumerate(expected):
                    # if index is optional and user didn't return that far, skip
                    if (isinstance(annotations["optional"], list) and i in annotations["optional"]) \
                    or (isinstance(annotations["optional"], int) and i == annotations["optional"]):
                        if len(result) <= i:
                            continue

                    # must compare values
                    if i >= len(result):
                        ok = False
                        fail_reason = f"missing value at index {i}, expected {exp}"
                        break

                    if result[i] != exp:
                        ok = False
                        fail_reason = f"mismatch at index {i}: expected {exp}, got {result[i]}"
                        break            
                if ok:
                    valid = True
                    break

            if not valid:
                raise AssertionError(
                    f"Result did not match any expected outputs.\n"
                    f"Reason: {fail_reason}"
                )

            return # don't proceed to default handling below

        # ---- default, simple handling ----
        if not isinstance(result, type(expected_output[0])): # expected output always packed in a list
            raise AssertionError(f'Exercise expects output type: {type(expected_output[0]).__name__}. Actual: {type(result)}.')
        
        # verify the output - single expected output:
        if len(expected_output) == 1:
            self.assertEqual(result, *expected_output)
        # verify the output - multiple acceptable outputs
        else:
            self.assertIn(result, expected_output)

    new_test.__name__ = f'test_{base_name}'
    return new_test

def build_test_suite(test_cases, user_solution):
    class DynamicTestClass(unittest.TestCase):
        pass
        
    for name, input_args, *expected_output in test_cases:
        test_method = make_test(user_solution, name, input_args, expected_output)
        setattr(DynamicTestClass, test_method.__name__, test_method)
        
    return unittest.TestLoader().loadTestsFromTestCase(DynamicTestClass)