from functools import cmp_to_key
def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

def largest_number(nums):
    nums_str = list(map(str, nums))
    nums_str.sort(key=cmp_to_key(compare))
    result = ''.join(nums_str)
    return result if result[0] != '0' else '0'

n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter the elements: ").split()))
print(largest_number(nums))
