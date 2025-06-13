from collections import deque
def max_path_score(nums,k):
  n=len(nums)
  dp=[0] * n
  dp[0] = nums[0]

  dq=deque([0])
  for i in range(1,n):
    while dq and dq[0] < i -k:
      dq.popleft()
    dp[i] =dp[dq[0]]+ nums[i]
    while dq and dp[i] >= dp[dq[-1]]:
      dq.pop()
    dq.append(i)
  return dp[-1]

nums=list(map(int,input("enter dungeon room values (space seperated): ").strip().split()))
k=int(input("Enter max jump length (K): "))
print("Maximum score to reach last room: ",max_path_score(nums,k))
