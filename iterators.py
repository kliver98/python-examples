from decorators import wait_until
import sys

class FiboIter():
  
  def __init__(self, **kwargs):
    self.counter = 0
    self.n1 = 0
    self.n2 = 1
    if "max" in kwargs:
      self.max = kwargs["max"]
    else:
      self.max = sys.maxsize
    print(str(self.max)+" <<>>")
  
  def __iter__(self):
    return self
  
  @wait_until
  def __next__(self):
    self.counter += 1
    if self.counter == 1:
      return self.n1
    elif self.counter == 2:
      return self.n2
    else:
      aux = self.n1 + self.n2
      if aux > self.max:
        raise StopIteration
      self.n1, self.n2 = self.n2, aux
      return aux

if __name__ == "__main__":
  fibonacci = FiboIter()
  for i in range(100):
    next_value = 0
    try:
      next_value = fibonacci.__next__(sleep = 0)
    except StopIteration:
      print("Value too large to continue")
      print(f"I can go upto {fibonacci.max}")
      print(f"Maximum number of iterations raised are {i}")
      sys.exit()
    print(next_value)
