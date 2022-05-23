from datetime import datetime
import time

def wait_until(func):
  def wrapper(*args, **kwargs):
    if "sleep" in kwargs:
      time.sleep(kwargs["sleep"])
      #print("I fell asleep for "+str(kwargs["sleep"])+" seconds")
      del kwargs["sleep"]
    return func(*args, **kwargs)
  return wrapper

@wait_until
def sum(a: int, b: int) -> int:
  return a + b

def execution_time(func):
  def wrapper(*args, **kwargs):
    initial_time = datetime.now()
    func(*args, **kwargs)
    final_time = datetime.now()
    time_elapsed = final_time - initial_time
    print("Pasaron "+ str(time_elapsed.total_seconds()) + " segundos")
  return wrapper

@wait_until
def random_func():
  for _ in range(1, 100000000):
    pass

if __name__ == "__main__":
  random_func()
  print(sum(1, 11, sleep = 2))
