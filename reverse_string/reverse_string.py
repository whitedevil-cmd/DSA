from collections import deque

def reverse(string):
    stack = deque()
    for i in string:
        stack.append(i)
    string = ""
    while stack:
        string += stack.pop()
    stack.clear()
    return string

if __name__ == "__main__":
    input_str = input("Enter string: ")
    print(reverse(input_str))
