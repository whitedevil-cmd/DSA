# Trapped Water Problem

This script calculates the total amount of water that can be trapped after raining, given an elevation map represented by a list of integers.

## How It Works

It precomputes the maximum heights to the left and right of each bar, then calculates how much water each bar can trap using the formula:

```
min(left_max[i], right_max[i]) - height[i]
```

## Input Format

User is prompted to input the list of bar heights separated by spaces.

## Example

Input:
```
enter heights: 0 1 0 2 1 0 1 3 2 1 2 1
```

Output:
```
total_trapped_water: 6
```

## Files

- `trapped_water.py`: Main Python script
- `test_cases.txt`: Sample test cases to verify correctness
