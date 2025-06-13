# Find Duplicate and Missing Number

## Problem
Given an array `nums` representing `n` numbers from 1 to `n`, where one number is duplicated and one is missing, find the duplicate and missing numbers.

## How It Works
We calculate:
- The expected sum of numbers from 1 to n
- The actual sum of numbers in the list
- The sum of unique numbers in the list

Using:
- `duplicate = actual_sum - actual_set_sum`
- `missing = expected_sum - actual_set_sum`

## Files
- `find_duplicate_and_missing.py` — Main Python script.
- `test_cases.txt` — Sample test cases.
