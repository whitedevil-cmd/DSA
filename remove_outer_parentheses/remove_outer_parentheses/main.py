def removeouterparanthesis(s: str) -> str:
    result = []
    depth = 0

    for char in s:
        if char == '(':
            if depth > 0:
                result.append(char)
            depth += 1
        elif char == ')':
            depth -= 1
            if depth > 0:
                result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    input_str = input("Enter string of parentheses: ")
    print("Output:", removeouterparanthesis(input_str))
