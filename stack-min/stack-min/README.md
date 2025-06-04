# Stack with Constant-Time Minimum

This project implements a custom stack that supports the following operations:

- `PUSH x`: Push element `x` onto the stack.
- `POP`: Remove the top element from the stack.
- `MIN`: Return the minimum element in the stack in O(1) time.

### 💻 How to Run

```bash
python3 main.py
```

### 📥 Input Format
- First line: an integer `n`, the number of operations.
- Next `n` lines: each operation (`PUSH x`, `POP`, or `MIN`).

### 📤 Output Format
For every `MIN` operation, print the minimum element, or `EMPTY` if the stack is empty.

### 🧪 Sample Test

**Input**
```
6
PUSH 5
PUSH 2
MIN
POP
MIN
POP
```

**Output**
```
2
5
```

---

### 📁 Files

- `main.py`: Main logic
- `test_cases.txt`: Sample test case
- `.gitignore`: Ignore cache files

---
