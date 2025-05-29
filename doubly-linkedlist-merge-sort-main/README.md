# doubly-linkedlist-merge-sort
# Doubly Linked List Merge Sort

This project implements **Merge Sort on a Doubly Linked List** in Python. It is a classic demonstration of sorting using pointer manipulation, rather than traditional array indexing.

## 🚀 Features

- Doubly Linked List structure with `prev` and `next` pointers
- Recursive Merge Sort implementation
- Efficient in-place splitting and merging
- Pretty print format showing sorted links as `val1 <-> val2 <-> ...`
- Handles edge cases like empty lists and single-element lists

## 📄 Description

Unlike array-based merge sort, this implementation performs sorting by directly manipulating node pointers in a doubly linked list. The algorithm divides the list recursively, sorts each half, and merges them back while maintaining correct `prev` and `next` links.

This project is excellent for:
- Understanding linked list operations
- Learning how recursion applies to data structures
- Practicing pointer-based sorting logic (common in interviews)

## 🧪 Sample Test Cases

| Input                             | Output                        |
|----------------------------------|-------------------------------|
| `size = 6`, values: `3 1 4 2 5 0` | `0 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5` |
| `size = 1`, values: `7`          | `7`                           |
| `size = 2`, values: `9 1`        | `1 <-> 9`                     |
| `size = 0`, values: `[]`         | `[]`                          |
| `size = 5`, values: `5 4 3 2 1`  | `1 <-> 2 <-> 3 <-> 4 <-> 5`   |

## 🛠️ How to Use

```bash
# Run the program
python3 merge_sort_doubly_ll.py
