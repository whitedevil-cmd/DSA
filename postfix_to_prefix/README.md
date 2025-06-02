# Postfix to Prefix Converter

This program converts a postfix expression into a prefix expression using a stack-based approach.

## Problem Statement

Given a postfix expression, convert it to a prefix expression. Each operand is a single character and operators are one of `+`, `-`, `*`, `/`.

### Input Format

- A single string representing the postfix expression (e.g. `ABC*+`)

### Output Format

- A single string representing the equivalent prefix expression.

## Example

**Input:**  
`ABC*+`

**Output:**  
`+A*BC`

## How to Run

```bash
python postfix_to_prefix.py
```

## Run Tests

```bash
python -m unittest test_postfix_to_prefix.py
```
