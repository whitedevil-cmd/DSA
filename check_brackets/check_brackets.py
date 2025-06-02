from collections import deque

def check_brackets(expression):
    stack = deque()
    opens = '{(['
    closes = '})]'
    for char in expression:
        if char in opens:
            stack.append(char)
        elif char in closes:
            if not stack:
                return False
            top = stack.pop()
            if opens.index(top) != closes.index(char):
                return False
    return not stack

if __name__ == "__main__":
    expression = input("Enter string: ")
    print(check_brackets(expression))
