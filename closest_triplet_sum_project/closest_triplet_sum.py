def closest_triplet_sum(arr, target):
    arr.sort()
    n = len(arr)
    closest_sum = float('inf')
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            diff = abs(total - target)
            closest_diff = abs(closest_sum - target)
            if diff < closest_diff or (diff == closest_diff and total > closest_sum):
                closest_sum = total
            if total < target:
                left += 1
            else:
                right -= 1
    return closest_sum

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter the array elements: ").split()))
    target = int(input("Enter the target sum: "))
    print("Closest triplet sum:", closest_triplet_sum(arr, target))
