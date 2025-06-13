from collections import deque 
def first_non_repeating(stream:str) -> str:
  freq=[0] *26
  q=deque()
  result=[]

  for ch in stream :
    idx=ord(ch) - ord('a')
    freq[idx]+=1
    q.append(ch)

    while q and freq[ord(q[0]) -ord('a')] > 1:
      q.popleft()
    result.append(q[0] if q else '#')
  return ''.join(result)
input_stream=input("Enter the stream of lowercase letters: ").strip()
print("Output: ",first_non_repeating(input_stream))
