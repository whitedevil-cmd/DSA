def has_triplets_with_sum(nums, target):
    nums.sort()
    n = len(nums)
    for i in range(n - 1):
        left = i + 1
        right = n - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if curr_sum == target:
                return True
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
    return False

if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    nums = list(map(int, input("Enter the numbers: ").split()))
    target = int(input("Enter the target sum: "))
    print("Triplet exists:" , has_triplets_with_sum(nums, target))
