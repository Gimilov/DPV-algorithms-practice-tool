# DPV Algorithms Practice Tool

A helper tool for studying algorithms from the Dasgupta, Papadimitriou, and Vazirani (DPV) textbook (1st edition), particularly for Georgia Tech's CS6515 course.

This repository provides scaffolding for implementing and testing DPV problem solutions, with test suites and solution templates. 

## Usage

```bash
# Scaffold a solution template for an exercise
python -m src.scaffold <exercise_number>

# Test your solution against exercise test cases  
python -m src.test_runner <exercise_number>
```

## Usage Examples
- **Scaffolding**:

![](assets/scaffold_example.png)

- **Testing**:

![](assets/test_example_pass_fail.png)

## Solutions
This directory contains my solution attempts for some of the DPV exercises. Please note that these are personal implementations and may contain errors or suboptimal approaches. When in doubt, always refer to the official book solutions or trusted academic sources for verified correctness.


## Adding and Managing Tests

All exercise tests are stored in files named `dpv_chapter_<chapter_number>.py`. Each file contains a set of test cases for that chapter’s exercises. The tests follow a consistent format.

---
### Test Case Format
Each test case is defined as a tuple:
```python
(test_name, input_args, expected_output1 [,expected_output2, ...])
```
For example:
```
('example_test', [5, 15, -30, 10, -5, 40, 10], [10, -5, 40, 10])
```
**Note**:
- **Multiple valid solutions**: If an exercise has more than one acceptable output, simply supply multiple `expected_output` values. The test will pass if the user solution matches any of them.

    ```python
    ('single_letter_palindrome', "ABCDEF", "A", "B", "C", "D", "E", "F")
    ```
---
### Annotations
Test names can include optional annotations to modify how the test is handled. Currently supported annotations:

- `@(optional:i[,j, ...])`: Marks one or more positions in the returned tuple as optional.
    ```python
    ('example_keywords@(optional:1)', (words, freqs),
    (2.18,),                      # valid if only cost returned
    (2.18, expected_tree1),       # also valid if cost + tree returned
    (2.18, expected_tree2))       # multiple valid tree shapes allowed
    ```
    - Indexing starts at 0, so optional:1 means the second element of the returned tuple is optional.

- `@(reference)`: Marks a reference-only case.  
    No assertions are run - instead, the expected output is simply displayed for theory-style questions.  
    ```python
    ('display_answers@(reference)', None, '<some answer here>')
    ```
