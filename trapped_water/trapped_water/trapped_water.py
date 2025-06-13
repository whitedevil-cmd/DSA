def find_trapped_water(height):
  n = len(height)
  if n == 0:
    return 0
  left_max = [0] * n
  max_right = [0] * n
  total_water = 0
  left_max[0] = height[0]
  for i in range(1, n):
    left_max[i] = max(left_max[i - 1], height[i])
  max_right[n - 1] = height[n - 1]
  for i in range(n - 2, -1, -1):
    max_right[i] = max(max_right[i + 1], height[i])
  for i in range(n):
    total_water += min(left_max[i], max_right[i]) - height[i]
  return total_water

heights = list(map(int, input("enter heights: ").strip().split()))
print("total_trapped_water: ", find_trapped_water(heights))
