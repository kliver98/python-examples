from decorators import wait_until
import sys

@wait_until
def fibo_gen(max = sys.maxsize):
  n1 = 0
  n2 = 1
  counter = 0
  while True:
    counter += 1
    if counter == 1:
      yield n1
    elif counter == 2:
      yield n2
    else:
      aux = n1 + n2
      if aux > max:
        break
      n1, n2 = n2, aux
      yield aux

if __name__ == "__main__":
  try:
    fibo = fibo_gen()
    for i in range(93):
      print(next(fibo))
  except StopIteration:
    print("Value too large to continue")
    print(f"I can go upto {max}")
    print(f"Maximum number of iterations raised are {i}")
    sys.exit()
  