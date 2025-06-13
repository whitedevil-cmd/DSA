from collections import deque 
def prediction(senate: str):
  n=len(senate)
  radient  =deque()
  dire =deque()

  for i,ch in enumerate(senate):
    if ch == 'R':
      radient.append(i)
    else:
      dire.append(i)

  while radient and dire:
    r=radient.popleft()
    d=dire.popleft()

    if r<d:
      radient.append(r+n)
    else:
      dire.append(d+n)
  return "Radient" if radient else "Dire"
senate_input=input("Enter the senate string (only 'R' and 'D'): ").strip().upper()
print(prediction(senate_input))
