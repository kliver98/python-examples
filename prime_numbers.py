import sys

def is_prime_number(number: int) -> bool:
  divisors = [2, 3, 5, 7]
  if (number in divisors):
    return True
  for ele in divisors:
    if (int(number/ele)*ele == number):
      number = -1
  return number not in [-1, 1]

def run():
  inp = input("Give the number: ")
  try:
    inp = int(inp)
  except:
    print("Not a valid number")
    sys.exit()
  output = []
  for i in range(inp):
    if (is_prime_number(i)):
      output.append(i)
  print(str(output)+" "+str(len(output)))

if __name__ == "__main__":
  run()
