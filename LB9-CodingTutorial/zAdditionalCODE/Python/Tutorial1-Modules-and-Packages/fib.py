# Module for fibonancci sequence
# Nov'2023 v1 dbe --- initial version for KETE HS23

# recursive fibonacci 
def fib_rec(n):
  if (n < 1):
     return n
  elif n == 1:
     return 1
  else:
     return fib_rec(n-1) + fib_rec(n-2)

  
# iterative fibonacci
def fib_iter(n):
  cur, nxt = 0,1
  for k in range(n):
    cur, nxt = nxt, cur + nxt
  return cur
  
# Given n, return list of fibonacci numbers <= n
def fib_upto(n):
  cur, nxt = 0,1
  lst = []
  while (cur < n):
    lst.append(cur)
    cur, nxt = nxt, cur + nxt
  return lst
