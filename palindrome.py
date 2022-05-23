def is_palindrome(string: str) -> bool:
  string = string.replace(" ", "").lower()
  return string == string[::-1]

def run():
  string = input("Give the word: ")
  print("Is Palindrome?: "+str(is_palindrome(string)))
  
if __name__ == "__main__":
  run()
  