def process_operations(operations):
    stack = []
    min_stack = []
    result = []

    for op in operations:
        if op.startswith("PUSH"):
            try:
                _, val = op.split()
                val = int(val)
            except:
                continue  # Skip malformed PUSH
            stack.append(val)
            if not min_stack or val <= min_stack[-1]:
                min_stack.append(val)
        elif op == 'POP':
            if stack:
                val = stack.pop()
                if min_stack and val == min_stack[-1]:
                    min_stack.pop()
        elif op == "MIN":
            if min_stack:
                result.append(str(min_stack[-1]))
            else:
                result.append("EMPTY")
    return result


if __name__ == "__main__":
    n = int(input())
    operations = [input().strip() for _ in range(n)]
    output = process_operations(operations)
    for line in output:
        print(line)
