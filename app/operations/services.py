def create_list(times: int):
  my_list = []
  if times <= 0:
    return my_list
  for i in range(1,times+1):
    my_list.append({"id": i, "message": f"This is the message number {i}"})
  return my_list

def fibonacci_sum(n: int):
  fib = []
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  fib.append(0)
  fib.append(1)
  sum = fib[0] + fib[1]
  for i in range(2, n+1):
    fib.append(fib[i - 1] + fib[i - 2])
    sum += fib[i]
  return sum

def fibonacci_list(n: int):
  fib = []
  if n < 0:
    return fib
  elif n == 0:
    return [0]
  fib.append(0)
  fib.append(1)
  if n == 1:
    return fib
  for i in range(2, n+1):
    fib.append(fib[i - 1] + fib[i - 2])
  return fib