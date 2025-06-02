from collections import deque
import operator

def evaluate_postfix(tokens):
    stack = deque()
    
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': lambda a, b: int(a / b)
    }

    try:
        for token in tokens:
            if token in operations:
                if len(stack) < 2:
                    return f"Error: Not enough operands for '{token}'"
                b = stack.pop()
                a = stack.pop()
                if token == '/' and b == 0:
                    return "Error: Division by zero"
                stack.append(operations[token](a, b))
            else:
                try:
                    stack.append(int(token))
                except ValueError:
                    return f"Error: Invalid token '{token}'"

        if len(stack) != 1:
            return "Error: Malformed expression (too many or too few operands)"

        return stack.pop()

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_input = input("Enter postfix expression (space-separated): ").strip()
    tokens = user_input.split()
    result = evaluate_postfix(tokens)
    print("Answer:", result)
