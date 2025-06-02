from collections import deque

def postfix_to_prefix(expr):
    stack = deque()
    operators = "+-*/"
    for char in expr:
        if char in operators:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(char + op1 + op2)
        else:
            stack.append(char)
    return stack.pop()

if __name__ == "__main__":
    expr = input("Enter postfix expression: ")
    print("Prefix expression:", postfix_to_prefix(expr))
