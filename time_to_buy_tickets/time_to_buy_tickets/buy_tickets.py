def time_to_buy_tickets(tickets,k):
  total_time=0
  for i in range(len(tickets)):
    if i <= k:
      total_time+=min(tickets[i],tickets[k])
    else:
      total_time +=min(tickets[i],tickets[k] -1)
  return total_time

tickets=list(map(int,input("enter list:").strip().split()))
k=int(input("enter k: "))
print(time_to_buy_tickets(tickets,k))