# Mystical Array Problem

This script processes an input array and returns a new array based on the following mystical logic:

For each element at index `i`, find the:
1. **Next Greater Element (NGE)** to its right.
2. Then, find the **Next Smaller Element (NSE)** to the right of the NGE.

If both exist, output the value at the NSE; otherwise, output `-1`.

## 🧪 Example

### Input
```
arr = [5, 1, 9, 2, 5, 1]
```

### Output
```
Mystical array output: [-1, 9, 2, -1, -1, -1]
```

## 📁 Files
- `mystical_array.py` — Main Python script
- `test_cases.txt` — Sample test cases with expected outputs
