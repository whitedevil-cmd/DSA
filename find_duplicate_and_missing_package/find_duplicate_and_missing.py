def find_duplicate_and_missing(nums):
  n=len(nums)
  expected_sum=n*(n+1) // 2
  actual_sum =sum(nums)
  actual_set_sum= sum(set(nums))

  duplicate = actual_sum -actual_set_sum
  missing =expected_sum - actual_set_sum

  return [duplicate ,missing]

nums=list(map(int,input("enter values: ").strip().split()))
print(find_duplicate_and_missing(nums))
