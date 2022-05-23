from ast import List


def run():
  set1 = set([1,2,4,6,'Hola'])
  set2 = set(['Hola', True, 1, 5, 3, 11])
  set3 = set([1, 6, 0, 'Kliver'])
  set4 = set(['Daniel', 1, 5, 3])
  print(f"Union {set1 | set3}")
  print(f"Intersection {set2 & set4}")
  print(f"Difference {set3 - set1}")
  print(f"Inverse intersection {set4 ^ set1}")

def delete_repeated(list: List):
  return [x for x in set(list)]

if __name__ == "__main__":
  print(delete_repeated([1, 1, 2, 'a', 'b', 'a']))