from collections import deque

def mystical_array(arr):
    n = len(arr)
    nge = [-1] * n  # Next Greater Element indices
    nse = [-1] * n  # Next Smaller Element indices

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        nge[i] = stack[-1] if stack else -1
        stack.append(i)

    stack.clear()
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        nse[i] = stack[-1] if stack else -1
        stack.append(i)

    result = [-1] * n
    for i in range(n):
        nge_index = nge[i]
        if nge_index != -1:
            nse_index = nse[nge_index]
            if nse_index != -1:
                result[i] = arr[nse_index]
            else:
                result[i] = -1
        else:
            result[i] = -1
    return result

if __name__ == "__main__":
    arr = list(map(int, input("Enter array separated by space: ").strip().split()))
    print("Mystical array output:", mystical_array(arr))
