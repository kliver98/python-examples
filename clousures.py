def make_repeater_of(n):
  def repeater(string):
    assert type(string) == str, "No es una cadena"
    return string * n
  return repeater

def make_divison_by(n):
  def division(x):
    return x/n
  return division

def run():
  #repeat_5 = make_repeater_of(5)
  #print(repeat_5(input("Dame el string: ")))
  make_division = make_divison_by(3)
  print(make_division(18))

if __name__ == "__main__":
  run()
